import { useEffect, useMemo, useRef, useState } from "react";
import { Alert, Button, Flex, Form, Input, Radio, Space, Tag, Typography, type FormInstance } from "antd";
import { CheckCircleOutlined, ReloadOutlined, RobotOutlined, SaveOutlined } from "@ant-design/icons";

import {
  assistCatalogReactionEquations,
  previewCatalogReactionEquations,
  type CatalogEquationAssistDraft,
  type CatalogEquationPreviewResponse,
  type CatalogNodeDetail,
} from "../../api/catalogTree";
import { AssistantMarkdownContent } from "../../lib/assistant-markdown";
import type { CatalogMutations } from "./catalogTreeHooks";
import {
  buildCatalogNodeUpdatePayload,
  type CatalogNodeFormValues,
  type CatalogPointContentFormValues,
} from "./catalogTreeMappers";
import {
  buildEquationReviewModel,
  type CatalogEquationReviewCandidate,
} from "./catalogEquationReview";

const { Text } = Typography;

const equationStatusMeta: Record<CatalogEquationPreviewResponse["equations"][number]["validation_status"], { label: string; color: string }> = {
  valid: { label: "已识别", color: "green" },
  warning: { label: "需确认", color: "gold" },
  invalid: { label: "需修改", color: "red" },
};

function pointContentStatusLabel(status?: string | null): string {
  if (status === "published") return "已发布";
  if (status === "draft") return "草稿";
  if (status === "missing") return "未配置";
  return "未配置";
}

function splitEquationText(value: string): string[] {
  return value
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
}

function replaceEquationLine(value: string, rowOrder: number, replacement: string): string {
  const lines = value.split(/\r?\n/);
  const nonEmptyIndexes = lines
    .map((line, index) => ({ line, index }))
    .filter((item) => item.line.trim())
    .map((item) => item.index);
  const targetIndex = nonEmptyIndexes[rowOrder - 1] ?? lines.length;
  if (targetIndex >= lines.length) {
    return [...lines, replacement].join("\n").trim();
  }
  const next = [...lines];
  next[targetIndex] = replacement;
  return next.join("\n");
}

export function CatalogNodeContentPanel({
  detail,
  nodeForm,
  pointForm,
  principleMode,
  mutations,
  onSavePointContent,
}: {
  detail: CatalogNodeDetail;
  nodeForm: FormInstance<CatalogNodeFormValues>;
  pointForm: FormInstance<CatalogPointContentFormValues>;
  principleMode?: string;
  mutations: CatalogMutations;
  onSavePointContent: (values: CatalogPointContentFormValues) => Promise<void>;
}) {
  const { node } = detail;
  const equationText = Form.useWatch("reaction_equations_text", pointForm) || "";
  const [equationPreview, setEquationPreview] = useState<CatalogEquationPreviewResponse | null>(null);
  const [previewLoading, setPreviewLoading] = useState(false);
  const [previewError, setPreviewError] = useState("");
  const [assistLoading, setAssistLoading] = useState(false);
  const [assistLoadingRow, setAssistLoadingRow] = useState<number | null>(null);
  const [assistMessage, setAssistMessage] = useState("");
  const [assistDrafts, setAssistDrafts] = useState<CatalogEquationAssistDraft[]>([]);
  const previewSeq = useRef(0);
  const reviewModel = useMemo(() => buildEquationReviewModel(equationPreview, assistDrafts), [equationPreview, assistDrafts]);
  const hasEquationInput = Boolean(equationText.trim());
  const activePlacementCount = detail.canonical_point?.active_placement_count ?? node.active_placement_count ?? 0;
  const reusedPlacements = (detail.placements || []).filter((placement) => placement.node_id !== node.node_id);

  const requestPreview = async (textValue: string, seq: number) => {
    const rows = splitEquationText(textValue).map((rawText, index) => ({ raw_text: rawText, row_order: index + 1 }));
    if (!rows.length) {
      setEquationPreview(null);
      setPreviewLoading(false);
      setPreviewError("");
      return;
    }
    setPreviewLoading(true);
    setPreviewError("");
    try {
      const response = await previewCatalogReactionEquations(rows, textValue);
      if (seq === previewSeq.current) {
        setEquationPreview(response);
      }
    } catch (error) {
      if (seq === previewSeq.current) {
        setPreviewError(error instanceof Error ? error.message : "实时检查失败，请稍后重试。");
      }
    } finally {
      if (seq === previewSeq.current) {
        setPreviewLoading(false);
      }
    }
  };

  useEffect(() => {
    if (principleMode !== "equation") return;
    const seq = previewSeq.current + 1;
    previewSeq.current = seq;
    const textValue = equationText.trim();
    if (!textValue) {
      setEquationPreview(null);
      setPreviewLoading(false);
      setPreviewError("");
      return;
    }
    const timer = window.setTimeout(() => {
      void requestPreview(textValue, seq);
    }, 500);
    return () => window.clearTimeout(timer);
  }, [equationText, principleMode]);

  useEffect(() => {
    setAssistMessage("");
    setAssistDrafts([]);
  }, [equationText]);

  const refreshPreview = () => {
    const seq = previewSeq.current + 1;
    previewSeq.current = seq;
    void requestPreview(equationText.trim(), seq);
  };

  const applyCandidate = (candidate: CatalogEquationReviewCandidate) => {
    const replacement = candidate.replacement_text || candidate.draft_text || candidate.canonical_display;
    if (!replacement) return;
    if (candidate.row_order) {
      pointForm.setFieldValue("reaction_equations_text", replaceEquationLine(equationText, candidate.row_order, replacement));
      return;
    }
    const current = equationText.trim();
    pointForm.setFieldValue("reaction_equations_text", [current, replacement].filter(Boolean).join("\n"));
  };
  const mergeRowAssistDrafts = (incoming: CatalogEquationAssistDraft[], rowOrder?: number) => {
    if (!rowOrder) {
      setAssistDrafts(incoming);
      return;
    }
    setAssistDrafts((current) => [
      ...current.filter((draft) => draft.row_order !== rowOrder),
      ...incoming.filter((draft) => !draft.row_order || draft.row_order === rowOrder),
    ]);
  };

  const runEquationAssist = async (rowOrder?: number) => {
    if (rowOrder) {
      setAssistLoadingRow(rowOrder);
    } else {
      setAssistLoading(true);
    }
    setAssistMessage("");
    if (!rowOrder) setAssistDrafts([]);
    try {
      const response = await assistCatalogReactionEquations({
        mode: "suggest",
        multiline_text: equationText,
        point_title: pointForm.getFieldValue("point_title") || detail.point_content?.point_title || detail.node.title,
        catalog_path_text: detail.breadcrumbs.map((item) => item.title).join(" / "),
        phenomenon_explanation: pointForm.getFieldValue("phenomenon_explanation") || "",
        safety_note: pointForm.getFieldValue("safety_note") || "",
      });
      setAssistMessage(response.reason || "");
      mergeRowAssistDrafts(response.drafts || [], rowOrder);
    } catch (error) {
      setAssistMessage(error instanceof Error ? error.message : "助手暂时不可用。");
    } finally {
      if (rowOrder) {
        setAssistLoadingRow(null);
      } else {
        setAssistLoading(false);
      }
    }
  };

  if (node.node_kind === "directory") {
    return (
      <section className="catalog-editor-section catalog-editor-panel-section">
        <div className="catalog-editor-section-intro">
          <Text strong>基础信息</Text>
          <Text type="secondary">目录负责学生端导航与分类，不承载点位知识或视频绑定。</Text>
        </div>
        <Form
          form={nodeForm}
          layout="vertical"
          onFinish={(values) => mutations.updateNode.mutate({ nodeId: node.node_id, payload: buildCatalogNodeUpdatePayload(values) })}
        >
          <Form.Item name="node_kind" hidden>
            <Input />
          </Form.Item>
          <Form.Item name="title" label="目录标题" rules={[{ required: true, message: "请输入目录标题" }]}>
            <Input />
          </Form.Item>
          <Form.Item name="teacher_note" label="教学备注" extra="仅教师端可见，不进入学生端、学生搜索或题目证据链。">
            <Input.TextArea className="catalog-teacher-note" autoSize={{ minRows: 2, maxRows: 5 }} />
          </Form.Item>
          <Alert type="info" showIcon title="学生可见描述和卡片样式在“学生卡片”面板维护。" />
          <Button type="primary" htmlType="submit" icon={<SaveOutlined />} loading={mutations.updateNode.isPending}>
            保存目录内容
          </Button>
        </Form>
      </section>
    );
  }

  return (
    <section className="catalog-editor-section catalog-editor-panel-section">
      <Flex className="catalog-editor-section-heading" align="center" justify="space-between" gap={12}>
        <div className="catalog-editor-section-intro">
          <Text strong>知识字段</Text>
          <Text type="secondary">默认只显示老师最常维护的点位知识字段。</Text>
        </div>
        <Space wrap>
          <Tag color={detail.point_content?.content_status === "published" ? "green" : "gold"}>
            {pointContentStatusLabel(detail.point_content?.content_status)}
          </Tag>
          <Button
            icon={<CheckCircleOutlined />}
            onClick={() => mutations.changePointPublication.mutate({ nodeId: node.node_id, action: "publish" })}
            loading={mutations.changePointPublication.isPending}
          >
            发布点位内容
          </Button>
        </Space>
      </Flex>
      <Form form={pointForm} layout="vertical" onFinish={onSavePointContent}>
        <div className="catalog-field-scope-note">
          <Tag color="green">共享实验字段</Tag>
          <Text type="secondary">点位名、原理、现象、安全说明、视频和相关实验按同一个实验保存。</Text>
        </div>
        {activePlacementCount > 1 ? (
          <Alert
            className="catalog-shared-content-alert"
            type="warning"
            showIcon
            message={`此实验已同步到 ${activePlacementCount} 个目录位置`}
            description={
              <div className="catalog-shared-content-copy">
                <span>实验内容、视频、AI 证据和相关实验会在所有位置同步更新。</span>
                {reusedPlacements.length ? (
                  <div className="catalog-shared-placement-list">
                    {reusedPlacements.slice(0, 5).map((placement) => (
                      <Tag key={placement.node_id}>
                        {(placement.breadcrumbs || []).map((item) => item.title).join(" / ") || placement.title}
                      </Tag>
                    ))}
                    {reusedPlacements.length > 5 ? <Tag>+{reusedPlacements.length - 5}</Tag> : null}
                  </div>
                ) : null}
              </div>
            }
          />
        ) : null}
        <Form.Item name="point_title" label="点位名" rules={[{ required: true, message: "请输入点位名" }]}>
          <Input />
        </Form.Item>
        <Form.Item name="teacher_note" label="教学备注" extra="仅教师端可见，不进入学生端、学生搜索或题目证据链。">
          <Input.TextArea className="catalog-teacher-note" autoSize={{ minRows: 2, maxRows: 5 }} />
        </Form.Item>
        <Form.Item name="principle_mode" label="实验原理形式" rules={[{ required: true }]}>
          <Radio.Group optionType="button" buttonStyle="solid">
            <Radio.Button value="equation">化学方程式</Radio.Button>
            <Radio.Button value="text">文字描述</Radio.Button>
          </Radio.Group>
        </Form.Item>
        {principleMode === "equation" ? (
          <div className="catalog-equation-natural-editor">
            <div className="catalog-equation-natural-header">
              <div className="catalog-equation-natural-copy">
                <Text strong>实验反应式</Text>
                <Text type="secondary">直接输入或粘贴反应式，一行一个；系统会自动识别、纠错并提示配平建议。</Text>
              </div>
            </div>
            <Form.Item name="reaction_equations_text" rules={[{ required: true, message: "请输入实验反应式，或切换为文字描述" }]}>
              <Input.TextArea
                className="catalog-equation-natural-input"
                autoSize={{ minRows: 4, maxRows: 10 }}
                placeholder={"例如：CL2+H2=HCL\nCl2 + 2KBr -> 2KCl + Br2\n氯气 + 氢气 = 氯化氢"}
              />
            </Form.Item>
            <div className="catalog-equation-natural-actions">
              <div className="catalog-equation-natural-action-copy">
                <Text type="secondary">先看系统理解；需要进一步修正或补全时，再让 AI 基于这些结果给建议。</Text>
              </div>
              <Space wrap>
                <Button type="primary" icon={<RobotOutlined />} loading={assistLoading} onClick={() => void runEquationAssist()}>
                  AI 建议
                  {/*
                  {hasEquationInput ? "AI 校对全部" : "AI 生成候选"}
                  */}
                </Button>
                <Button icon={<ReloadOutlined />} loading={previewLoading} onClick={refreshPreview}>
                  重新检查
                </Button>
              </Space>
            </div>
            {previewError ? <div className="catalog-equation-natural-feedback is-error">{previewError}</div> : null}
            {previewLoading ? <div className="catalog-equation-natural-feedback">正在识别反应式...</div> : null}
            {reviewModel.rows.length || reviewModel.supplementalCandidates.length ? (
              <div className="catalog-equation-natural-preview">
                <div className="catalog-equation-natural-preview-title">
                  <Text strong>系统理解为</Text>
                  <Space wrap>
                    <Text type="secondary">保存时仍以当前输入为准，后端会重新规范化。</Text>
                    {reviewModel.rows.some((row) => row.candidates.length) ? (
                      <Button size="small" type="primary" onClick={() => reviewModel.rows.forEach((row) => row.candidates[0] && applyCandidate(row.candidates[0]))}>
                        采用全部
                      </Button>
                    ) : null}
                  </Space>
                </div>
                {reviewModel.rows.map(({ equation, candidates }) => {
                  const status = equationStatusMeta[equation.validation_status];
                  const messages = [...(equation.corrections || []), ...equation.warnings, ...equation.errors];
                  const hasDetails = Boolean(messages.length || equation.formulae.length);
                  return (
                    <div className={`catalog-equation-natural-row is-${equation.validation_status}`} key={`${equation.row_order}-${equation.raw_text}`}>
                      <span className="catalog-equation-natural-index">{equation.row_order}</span>
                      <div className="catalog-equation-natural-result">
                        <div className="catalog-equation-natural-result-line">
                          <div className="catalog-equation-natural-rendered">
                            {equation.canonical_mhchem ? (
                              <AssistantMarkdownContent text={`$${equation.canonical_mhchem}$`} inline />
                            ) : (
                              equation.canonical_display || equation.raw_text
                            )}
                          </div>
                          <Space wrap size={8}>
                            <Tag color={status.color}>{status.label}</Tag>
                            {equation.validation_status !== "valid" ? (
                              <Button
                                size="small"
                                icon={<RobotOutlined />}
                                loading={assistLoadingRow === equation.row_order}
                                onClick={() => void runEquationAssist(equation.row_order)}
                              >
                                让 AI 修这行
                              </Button>
                            ) : null}
                          </Space>
                        </div>
                        {candidates.length ? (
                          <div className="catalog-equation-natural-candidates">
                            <Text className="catalog-equation-natural-candidates-title" type="secondary">推荐采用</Text>
                            {candidates.map((candidate) => (
                              <div className="catalog-equation-natural-candidate" key={candidate.key}>
                                <Tag color={candidate.sources.includes("ai") ? "green" : "blue"}>{candidate.sourceLabel}</Tag>
                                <div className="catalog-equation-natural-candidate-body">
                                  <div className="catalog-equation-natural-rendered">
                                    {candidate.canonical_mhchem ? (
                                      <AssistantMarkdownContent text={`$${candidate.canonical_mhchem}$`} inline />
                                    ) : (
                                      candidate.canonical_display
                                    )}
                                  </div>
                                  {candidate.rationale || candidate.formulae.length || candidate.warnings.length || candidate.errors.length ? (
                                    <details className="catalog-equation-natural-details">
                                      <summary>查看详情</summary>
                                      {candidate.rationale ? <Text type="secondary">{candidate.rationale}</Text> : null}
                                      {candidate.formulae.length ? <Text type="secondary">识别到：{candidate.formulae.join("、")}</Text> : null}
                                      {[...candidate.warnings, ...candidate.errors].map((item) => (
                                        <Text key={item} type={candidate.errors.includes(item) ? "danger" : "secondary"}>
                                          {item}
                                        </Text>
                                      ))}
                                      <Text type="secondary">替换文本：{candidate.replacement_text}</Text>
                                    </details>
                                  ) : null}
                                </div>
                                <Button size="small" type="primary" onClick={() => applyCandidate(candidate)}>
                                  采用这个反应式
                                </Button>
                              </div>
                            ))}
                          </div>
                        ) : null}
                        {hasDetails ? (
                          <details className="catalog-equation-natural-details">
                            <summary>查看识别详情</summary>
                            {equation.formulae.length ? <Text type="secondary">识别到：{equation.formulae.join("、")}</Text> : null}
                            {messages.map((item) => (
                              <Text key={item} type={equation.errors.includes(item) ? "danger" : "secondary"}>
                                {item}
                              </Text>
                            ))}
                          </details>
                        ) : null}
                      </div>
                    </div>
                  );
                })}
                {reviewModel.supplementalCandidates.length ? (
                  <div className="catalog-equation-natural-supplemental">
                    <Text strong>候选补充反应式</Text>
                    {reviewModel.supplementalCandidates.map((candidate) => (
                      <div className="catalog-equation-natural-candidate" key={candidate.key}>
                        <Tag color="green">{candidate.sourceLabel}</Tag>
                        <div className="catalog-equation-natural-candidate-body">
                          <div className="catalog-equation-natural-rendered">
                            {candidate.canonical_mhchem ? <AssistantMarkdownContent text={`$${candidate.canonical_mhchem}$`} inline /> : candidate.canonical_display}
                          </div>
                          {candidate.rationale ? <Text type="secondary">{candidate.rationale}</Text> : null}
                        </div>
                        <Button size="small" type="primary" onClick={() => applyCandidate(candidate)}>
                          采用这个反应式
                        </Button>
                      </div>
                    ))}
                  </div>
                ) : null}
              </div>
            ) : !hasEquationInput ? (
              <div className="catalog-equation-natural-empty">
                <Text strong>还没有反应式</Text>
                <Text type="secondary">AI 可以根据当前点位内容生成候选反应式，生成后仍需老师采纳。</Text>
                <Button type="primary" icon={<RobotOutlined />} loading={assistLoading} onClick={() => void runEquationAssist()}>
                  AI 生成候选
                </Button>
              </div>
            ) : null}
            {assistMessage ? <div className="catalog-equation-natural-feedback">{assistMessage}</div> : null}
          </div>
        ) : (
          <Form.Item name="principle_text" label="文字原理" rules={[{ required: true, message: "请输入文字原理" }]}>
            <Input.TextArea autoSize={{ minRows: 3, maxRows: 7 }} />
          </Form.Item>
        )}
        <Form.Item name="phenomenon_explanation" label="现象解释" rules={[{ required: true, message: "请输入现象解释" }]}>
          <Input.TextArea autoSize={{ minRows: 3, maxRows: 7 }} />
        </Form.Item>
        <Form.Item name="safety_note" label="安全提示" rules={[{ required: true, message: "请输入安全提示" }]}>
          <Input.TextArea autoSize={{ minRows: 2, maxRows: 5 }} />
        </Form.Item>
        <Button
          type="primary"
          htmlType="submit"
          icon={<SaveOutlined />}
          loading={mutations.savePointContent.isPending || mutations.updateNode.isPending}
        >
          保存点位内容
        </Button>
      </Form>
    </section>
  );
}
