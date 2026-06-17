import { ChangeEvent, FormEvent, useRef, useState } from "react";
import { Camera, CheckCircle2, LoaderCircle, MessageCircle, Paperclip, X } from "lucide-react";

import { AuthUser, StudentFeedbackType, errorMessage, submitStudentFeedback } from "../api";

const maxAttachmentBytes = 5 * 1024 * 1024;

const feedbackTypes: Array<{ value: StudentFeedbackType; label: string }> = [
  { value: "system_issue", label: "页面/系统问题" },
  { value: "course_content", label: "题目/内容问题" },
  { value: "experiment_resource", label: "实验/视频资源问题" },
  { value: "ai_answer", label: "AI 解答问题" },
  { value: "other", label: "其他建议" },
];

export type PageFeedbackContext = {
  pageType: string;
  pageTitle: string;
  chapterId?: string | null;
  unitId?: string | null;
  knowledgePointId?: string | null;
  experimentId?: string | null;
  context?: Record<string, unknown>;
};

function currentPagePath(): string {
  if (typeof window === "undefined") return "";
  return `${window.location.pathname}${window.location.search}${window.location.hash}`;
}

function viewportSnapshot(): Record<string, unknown> {
  if (typeof window === "undefined") return {};
  return {
    width: window.innerWidth,
    height: window.innerHeight,
    device_pixel_ratio: window.devicePixelRatio,
    screen_width: window.screen?.width,
    screen_height: window.screen?.height,
  };
}

function buildMetadata(user: AuthUser, context: PageFeedbackContext): Record<string, unknown> {
  const navigatorInfo = typeof navigator === "undefined" ? null : navigator;
  return {
    page_type: context.pageType,
    page_title: context.pageTitle,
    context: context.context || {},
    student: {
      student_id: user.student_id || user.username,
      class_id: user.class_id || null,
      class_name: user.class_name || null,
    },
    viewport: viewportSnapshot(),
    user_agent: navigatorInfo?.userAgent || null,
    platform: navigatorInfo?.platform || null,
    language: navigatorInfo?.language || null,
    online: navigatorInfo?.onLine ?? null,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
    submitted_at: new Date().toISOString(),
  };
}

function attachmentError(file: File): string {
  const nameOk = /\.(png|jpe?g|webp)$/i.test(file.name);
  const typeOk = !file.type || ["image/png", "image/jpeg", "image/webp"].includes(file.type);
  if (!nameOk || !typeOk) return "附件仅支持 png、jpg、jpeg、webp 图片";
  if (file.size > maxAttachmentBytes) return "附件不能超过 5MB";
  return "";
}

export function PageFeedback({ user, context }: { user: AuthUser; context: PageFeedbackContext }) {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [open, setOpen] = useState(false);
  const [feedbackType, setFeedbackType] = useState<StudentFeedbackType>("system_issue");
  const [content, setContent] = useState("");
  const [attachment, setAttachment] = useState<File | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const resetDraft = () => {
    setFeedbackType("system_issue");
    setContent("");
    setAttachment(null);
    setError("");
    if (fileInputRef.current) fileInputRef.current.value = "";
  };

  const closePanel = () => {
    setOpen(false);
    setSuccess("");
    resetDraft();
  };

  const handleAttachment = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.currentTarget.files?.[0] || null;
    setError("");
    if (!file) {
      setAttachment(null);
      return;
    }
    const validationError = attachmentError(file);
    if (validationError) {
      setAttachment(null);
      setError(validationError);
      event.currentTarget.value = "";
      return;
    }
    setAttachment(file);
  };

  const submit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const trimmed = content.trim();
    if (trimmed.length < 5) {
      setError("请至少写 5 个字说明问题或建议");
      return;
    }
    setSubmitting(true);
    setError("");
    setSuccess("");
    try {
      await submitStudentFeedback({
        feedback_type: feedbackType,
        content: trimmed,
        page_path: currentPagePath(),
        chapter_id: context.chapterId || null,
        unit_id: context.unitId || null,
        knowledge_point_id: context.knowledgePointId || null,
        experiment_id: context.experimentId || null,
        metadata: buildMetadata(user, context),
        attachment,
      });
      resetDraft();
      setSuccess("反馈已提交");
    } catch (requestError) {
      setError(errorMessage(requestError));
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="page-feedback">
      {open ? (
        <section className="page-feedback-panel" role="dialog" aria-modal="true" aria-label="页面反馈">
          <div className="page-feedback-head">
            <div>
              <span>页面反馈</span>
              <h2>{context.pageTitle}</h2>
            </div>
            <button type="button" aria-label="关闭页面反馈" onClick={closePanel}>
              <X size={18} />
            </button>
          </div>

          {success ? (
            <div className="feedback-success">
              <CheckCircle2 size={22} />
              <div>
                <strong>{success}</strong>
                <span>老师后台会收到这条页面反馈。</span>
              </div>
            </div>
          ) : (
            <form className="page-feedback-form" onSubmit={submit}>
              <div className="feedback-type-grid" aria-label="反馈类型">
                {feedbackTypes.map((item) => (
                  <button
                    key={item.value}
                    type="button"
                    className={feedbackType === item.value ? "selected" : ""}
                    aria-pressed={feedbackType === item.value}
                    onClick={() => setFeedbackType(item.value)}
                  >
                    {item.label}
                  </button>
                ))}
              </div>

              <label className="feedback-content-field">
                <span>问题或建议</span>
                <textarea
                  value={content}
                  maxLength={4000}
                  rows={5}
                  placeholder="请描述你遇到的问题或建议"
                  onChange={(event) => setContent(event.target.value)}
                />
              </label>

              <div className="feedback-attachment-row">
                <button type="button" onClick={() => fileInputRef.current?.click()}>
                  <Paperclip size={17} />
                  <span>{attachment ? "更换截图" : "添加截图"}</span>
                </button>
                <input
                  ref={fileInputRef}
                  type="file"
                  accept="image/png,image/jpeg,image/webp"
                  onChange={handleAttachment}
                />
                {attachment ? (
                  <button
                    type="button"
                    className="feedback-file-pill"
                    onClick={() => {
                      setAttachment(null);
                      if (fileInputRef.current) fileInputRef.current.value = "";
                    }}
                  >
                    <Camera size={15} />
                    <span>{attachment.name}</span>
                    <X size={14} />
                  </button>
                ) : null}
              </div>

              {error ? <div className="form-error">{error}</div> : null}

              <div className="page-feedback-actions">
                <button type="button" onClick={closePanel}>
                  取消
                </button>
                <button type="submit" disabled={submitting || content.trim().length < 5}>
                  {submitting ? <LoaderCircle className="spin" size={17} /> : <MessageCircle size={17} />}
                  <span>{submitting ? "正在提交" : "提交反馈"}</span>
                </button>
              </div>
            </form>
          )}
        </section>
      ) : (
        <button className="page-feedback-toggle" type="button" onClick={() => setOpen(true)}>
          <MessageCircle size={17} />
          <span>页面反馈</span>
        </button>
      )}
    </div>
  );
}
