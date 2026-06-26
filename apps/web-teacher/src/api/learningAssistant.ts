import { api, apiBase, postJson, postJsonStream } from "./http";
import { getAuthToken } from "./auth";
import type { AIConfiguration } from "./settings";

export type LearningAssistantAskRequest = {
  question: string;
  student_id?: string | null;
  chapter_id?: string | null;
  experiment_id?: string | null;
  point_key?: string | null;
  knowledge_point_ids?: string[];
  allow_progress_lookup: boolean;
  allow_rag_lookup: boolean;
  conversation_history?: Array<{
    role: "user" | "assistant";
    content: string;
  }>;
  max_answer_chars?: number | null;
};

export type LearningAssistantSourceAsset = {
  path: string;
  file_name: string;
  kind: "figure" | "page" | string;
  caption?: string | null;
};

export type LearningAssistantSource = {
  chunk_id: string;
  source_file?: string | null;
  page_number?: number | null;
  text_preview: string;
  content_type?: string | null;
  caption?: string | null;
  section_path?: string[];
  assets?: LearningAssistantSourceAsset[];
};

export type LearningAssistantResponse = {
  answer: string;
  sources: LearningAssistantSource[];
  mode: string;
  classification: Record<string, unknown>;
  tool_calls: Array<Record<string, unknown>>;
  guardrail_decisions: Array<{
    code?: string;
    action?: string;
    reason?: string;
    [key: string]: unknown;
  }>;
  rag_trace?: Record<string, unknown>;
  review_required: boolean;
};

export type LearningAssistantRuntime = {
  checked_at: string;
  rag_runtime?: AIConfiguration["rag_runtime"];
  textbook_rag_status?: string;
  textbook_rag_error?: string | null;
  textbook_rag_diagnostics?: Record<string, unknown>;
};

export function getLearningAssistantRuntime(): Promise<LearningAssistantRuntime> {
  return api<LearningAssistantRuntime>("/api/admin/learning-assistant/runtime");
}

export function askLearningAssistant(request: LearningAssistantAskRequest): Promise<LearningAssistantResponse> {
  return postJson<LearningAssistantResponse>("/api/learning/assistant/ask", request);
}

export function streamLearningAssistant<T>(path: string, body: unknown, onEvent: Parameters<typeof postJsonStream<T>>[2]): Promise<void> {
  return postJsonStream<T>(path, body, onEvent);
}

export function getRagAssetUrl(path: string): string {
  return `${apiBase}/api/admin/rag-assets?path=${encodeURIComponent(path)}`;
}

export function getAuthenticatedHeaders(): Headers {
  const headers = new Headers();
  const token = getAuthToken();
  if (token) headers.set("Authorization", `Bearer ${token}`);
  return headers;
}
