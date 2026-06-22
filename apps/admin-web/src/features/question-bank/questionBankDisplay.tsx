import { Tag } from "antd";

import type { LearningAssistantRuntime } from "../../api/learningAssistant";
import type {
  Question,
  QuestionWorkbenchCandidate,
} from "../../api/questionBank";
import { statusTag } from "../../lib/status";

export function questionTypeLabel(type?: string) {
  if (type === "single_choice") return "??";
  if (type === "true_false") return "??";
  if (type === "fill_blank") return "??";
  return type || "-";
}

export function coverageTagLabel(tag?: string) {
  const labels: Record<string, string> = {
    experiment_purpose: "????",
    true_false: "???",
    single_choice: "???",
    fill_blank: "???",
    evidence_based: "???",
    diagnostic: "???",
  };
  return labels[String(tag || "")] || String(tag || "-").replace(/_/g, " ");
}

export function answerText(answer?: Record<string, unknown>) {
  if (!answer) return "-";
  if (Array.isArray(answer.accepted_answers)) return answer.accepted_answers.map(String).join("，");
  if (answer.value !== undefined) {
    if (typeof answer.value === "boolean") return answer.value ? "正确" : "错误";
    return String(answer.value);
  }
  return JSON.stringify(answer);
}

export function sourceRefLabel(ref: Record<string, unknown>) {
  const file = String(ref.source_file || "资料片段");
  const page = ref.page_number ? ` p.${ref.page_number}` : "";
  const section = ref.section_title ? ` · ${ref.section_title}` : "";
  return `${file}${page}${section}`;
}

export function questionPoints(question: Question) {
  const points = question.metadata?.primary_points || [];
  if (points.length) {
    return points
      .map((point) => ({
        point_key: String(point.point_key || "").trim(),
        point_title: String(point.point_title || point.point_key || "").trim(),
      }))
      .filter((point) => point.point_key || point.point_title);
  }
  return (question.metadata?.primary_point_keys || [])
    .map((key) => ({ point_key: String(key), point_title: String(key) }))
    .filter((point) => point.point_key);
}

export function questionPointTitles(question: Question) {
  return questionPoints(question).map((point) => point.point_title || point.point_key).filter(Boolean);
}

export function candidatePayload(candidate: QuestionWorkbenchCandidate) {
  return candidate.payload || {};
}

export function candidateStem(candidate: QuestionWorkbenchCandidate) {
  return String(candidatePayload(candidate).stem || "");
}

export function candidateQuestionType(candidate: QuestionWorkbenchCandidate) {
  return String(candidatePayload(candidate).question_type || "");
}

export function candidateQuestionPoints(candidate: QuestionWorkbenchCandidate) {
  const metadata = candidatePayload(candidate).metadata || {};
  const points = Array.isArray(metadata.primary_points) ? metadata.primary_points : [];
  if (points.length) {
    return points
      .map((point) => ({
        point_key: String(point?.point_key || "").trim(),
        point_title: String(point?.point_title || point?.point_key || "").trim(),
      }))
      .filter((point) => point.point_key || point.point_title);
  }
  const keys = Array.isArray(metadata.primary_point_keys) ? metadata.primary_point_keys : [];
  return keys.map((key) => ({ point_key: String(key), point_title: String(key) })).filter((point) => point.point_key);
}

export function candidateValidationErrors(candidate: QuestionWorkbenchCandidate) {
  return candidate.validation_errors?.length
    ? candidate.validation_errors
    : candidate.draft_validation_errors?.length
      ? candidate.draft_validation_errors
      : [];
}

export function questionHasAnyPoint(question: Question, pointKeys: string[]) {
  if (!pointKeys.length) return true;
  const selected = new Set(pointKeys);
  return questionPoints(question).some((point) => selected.has(point.point_key));
}

export function evidenceStatusTag(question: Question) {
  if (question.metadata?.source_audit?.evidence_sufficient) return <Tag color="green">证据已核对</Tag>;
  if (question.source_refs?.length) return <Tag color="gold">有来源</Tag>;
  return <Tag>待核对</Tag>;
}

export function evidenceStatusText(question: Question) {
  if (question.metadata?.source_audit?.evidence_sufficient) return "证据已核对";
  if (question.source_refs?.length) return "有来源";
  return "待核对";
}

export function reviewDecisionText(decision?: string) {
  if (decision === "keep") return "审查保留";
  if (decision === "rewrite") return "建议改写";
  if (decision === "reject") return "已拒绝";
  return "未审查";
}

export function questionBankStatusTag(status?: string) {
  if (status === "published") return <Tag color="green">启用</Tag>;
  if (status === "disabled") return <Tag>未启用</Tag>;
  return statusTag(status);
}

export function questionBankStatusText(status?: string) {
  if (status === "published") return "启用";
  if (status === "disabled") return "未启用";
  return status || "-";
}

export type QuestionWorkbenchGateState = {
  healthy: boolean;
  label: string;
  message: string;
  tagColor: string;
  alertType: "success" | "info" | "warning" | "error";
  bgeStatus: string;
  route: string;
  tone: "ready" | "checking" | "blocked";
};

export const textbookSectionLabels: Record<string, string> = {
  principle: "实验原理",
  phenomenon: "现象解释",
  safety: "安全提示",
};

export type WorkbenchEvidenceSection = {
  pointKey: string;
  pointTitle: string;
  section: string;
  sufficient: boolean;
  sourceCount: number;
  sources: Record<string, unknown>[];
  missingReason: string;
};

function asRecord(value: unknown): Record<string, unknown> {
  return value && typeof value === "object" && !Array.isArray(value) ? (value as Record<string, unknown>) : {};
}

export function workbenchEvidenceSectionsFromPackage(evidencePackage?: Record<string, unknown> | null): WorkbenchEvidenceSection[] {
  const pointPackages = asRecord(evidencePackage?.point_packages);
  return Object.entries(pointPackages).flatMap(([pointKey, rawPointPackage]) => {
    const pointPackage = asRecord(rawPointPackage);
    const point = asRecord(pointPackage.point);
    const sections = asRecord(pointPackage.sections);
    return Object.entries(sections).map(([section, rawSectionPackage]) => {
      const sectionPackage = asRecord(rawSectionPackage);
      const sources = Array.isArray(sectionPackage.sources)
        ? sectionPackage.sources.map((source) => asRecord(source))
        : [];
      return {
        pointKey,
        pointTitle: String(point.point_title || pointKey),
        section,
        sufficient: Boolean(sectionPackage.sufficient),
        sourceCount: sources.length,
        sources,
        missingReason: String(sectionPackage.missing_reason || ""),
      };
    });
  });
}

export function questionWorkbenchGateFromRuntime(runtime?: LearningAssistantRuntime): QuestionWorkbenchGateState {
  const ragRuntime = runtime?.rag_runtime;
  const textbookStatus = ragRuntime?.textbook_rag_status || "disabled";
  const bgeStatus = runtime?.bge_metrics?.ok
    ? "healthy"
    : runtime?.bge_status || (runtime?.bge_error ? "unreachable" : ragRuntime?.bge_service_required ? "checking" : "not_required");
  const route = ragRuntime?.textbook_rag_enabled
    ? `教材 RAG · ${ragRuntime.textbook_rag_index || "Qwen/ES"}`
    : ragRuntime?.rag_enabled
      ? "教材 RAG 未启用"
      : "来源检索关闭";

  if (!runtime || !ragRuntime) {
    return {
      healthy: false,
      label: "正在检查",
      message: "正在确认来源检索状态，稍等一下再使用 AI 建议。",
      tagColor: "#356f9c",
      alertType: "info",
      bgeStatus: textbookStatus || bgeStatus,
      route,
      tone: "checking",
    };
  }
  if (!ragRuntime.rag_enabled) {
    return {
      healthy: false,
      label: "AI 暂不可用",
      message: "来源检索还没开启，暂时不能让 AI 出题或修题。",
      tagColor: "#b42318",
      alertType: "error",
      bgeStatus: textbookStatus || bgeStatus,
      route,
      tone: "blocked",
    };
  }
  if (textbookStatus !== "healthy") {
    const statusText: Record<string, string> = {
      disabled: "教材 RAG 未启用",
      elasticsearch_not_configured: "Elasticsearch 未配置",
      embedding_not_configured: "Embedding 模型未配置",
      rerank_not_configured: "Rerank 模型未配置",
      index_missing: "教材 chunk 索引不存在",
      index_stale: "教材 chunk 索引需要重建",
      elasticsearch_unreachable: "Elasticsearch 连接不上",
      elasticsearch_error: "Elasticsearch 检查失败",
    };
    return {
      healthy: false,
      label: "AI 暂不可用",
      message: `${statusText[textbookStatus] || ragRuntime.textbook_rag_message || "教材 RAG 还没准备好"}，暂时不能使用 AI 建议。`,
      tagColor: "#b42318",
      alertType: "error",
      bgeStatus: textbookStatus,
      route,
      tone: "blocked",
    };
  }
  if (!ragRuntime.query_generation_enabled) {
    return {
      healthy: false,
      label: "AI 暂不可用",
      message: "来源检索的扩展查询未开启，暂时不能使用 AI 建议。",
      tagColor: "#b42318",
      alertType: "error",
      bgeStatus: textbookStatus,
      route,
      tone: "blocked",
    };
  }
  return {
    healthy: true,
    label: "AI 建议可用",
    message: "会先按点位三段式描述检索教材证据，再生成出题/修题建议。",
    tagColor: "#005826",
    alertType: "success",
    bgeStatus: textbookStatus,
    route,
    tone: "ready",
  };
}
