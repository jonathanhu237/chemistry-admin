export type User = {
  id: string;
  username: string;
  role: "platform_admin" | "admin" | "teacher" | "student";
  display_name: string;
  status: string;
};

export type LoginResponse = {
  access_token: string;
  token_type: string;
  user: User;
};

export type ApiList<T> = {
  items: T[];
  total: number;
};

export type Experiment = {
  id: string;
  code?: string | null;
  title: string;
  summary?: string | null;
  status: string;
  published_question_count?: number;
  draft_question_count?: number;
  generated_draft_count?: number;
  media_resources?: Array<{
    media_id?: string;
    title?: string;
    upload_status?: string;
    binding_status?: string;
    point_title?: string | null;
  }>;
};

export type ClassItem = {
  id: string;
  class_name: string;
  status?: string;
  student_count?: number;
};

export type QuestionBankSummary = Experiment & {
  banks: Array<{
    id: string;
    title: string;
    status: string;
    question_count: number;
    published_count?: number;
    draft_count?: number;
    choice_count?: number;
    true_false_count?: number;
    fill_blank_count?: number;
  }>;
};

export type CatalogQuestionBankNode = {
  node_id: string;
  chapter_id?: string | null;
  node_kind: "directory" | "point";
  title: string;
  status: string;
  experiment_id?: string | null;
  breadcrumb_titles?: string[];
  media_count?: number;
  published_media_count?: number;
  counts: {
    question_count: number;
    published_count: number;
    draft_count: number;
    disabled_count?: number;
    choice_count?: number;
    true_false_count?: number;
    fill_blank_count?: number;
  };
};

export type CatalogQuestionBankResponse = ApiList<CatalogQuestionBankNode> & {
  totals?: CatalogQuestionBankNode["counts"];
  chapters?: Array<{ chapter_id: string; chapter_title: string; point_count: number }>;
};

export type LegacyVideoPointItem = {
  id: string;
  node_id: string;
  chapter_id?: string | null;
  title: string;
  summary?: string | null;
  snippet?: string | null;
  catalog_path?: string[];
  media_count?: number;
  published_media_count?: number;
  thumbnail_path?: string | null;
  is_recommended?: boolean;
  recommended_order?: number | null;
};

export type LegacyVideoPointResponse = {
  status: "ok" | "empty";
  query: string;
  total: number;
  items: LegacyVideoPointItem[];
};

export type QuestionWorkbenchSession = {
  id: string;
  mode: "repair" | "create";
  experiment_id: string;
  experiment_title?: string;
  status: string;
};

export type AnalyticsDashboard = {
  metrics: {
    class_size: number;
    active_students: number;
    published_experiments?: number;
    published_experiment_groups?: number;
    completion_rate: number;
    average_score: number;
    missing_students?: number;
  };
  matrix: Array<{
    student_id: string;
    student_name: string;
    average_score?: number;
    experiment_groups?: Record<
      string,
      {
        mastery_score?: number;
        score?: number;
        evidence_count?: number;
        attempt_count?: number;
        has_mastery?: boolean;
      }
    >;
  }>;
  experiment_groups?: Array<{ id: string; title: string; experiment_count: number }>;
};

export const apiBase = (import.meta.env.VITE_API_BASE_URL || "").replace(/\/$/, "");
const tokenKey = "chem_teacher_old_token";
let authToken = readStoredToken();

function readStoredToken(): string {
  try {
    return globalThis.localStorage?.getItem(tokenKey) || "";
  } catch {
    return "";
  }
}

export function getAuthToken(): string {
  return authToken;
}

export function setAuthToken(token: string): void {
  authToken = token;
  try {
    if (token) globalThis.localStorage?.setItem(tokenKey, token);
    else globalThis.localStorage?.removeItem(tokenKey);
  } catch {
    // Keep in-memory auth usable in tests and restricted browser contexts.
  }
}

export class ApiError extends Error {
  status: number;
  detail: unknown;

  constructor(status: number, detail: unknown) {
    super(typeof detail === "string" ? detail : `HTTP ${status}`);
    this.status = status;
    this.detail = detail;
  }
}

export function legacyTeacherErrorMessage(error: unknown): string {
  if (error instanceof ApiError) {
    if (error.status === 401) return "登录状态已失效，请重新登录。";
    if (error.status >= 500) return "教学服务暂不可用，请稍后再试。";
    return "当前操作未完成，请检查条件后重试。";
  }
  return "当前操作未完成，请稍后再试。";
}

export async function api<T>(path: string, options: RequestInit = {}): Promise<T> {
  const headers = new Headers(options.headers || {});
  if (!(options.body instanceof FormData) && !headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }
  if (authToken) headers.set("Authorization", `Bearer ${authToken}`);
  const response = await fetch(`${apiBase}${path}`, { ...options, headers });
  const contentType = response.headers.get("content-type") || "";
  const payload = contentType.includes("application/json") ? await response.json() : await response.text();
  if (response.status === 401) setAuthToken("");
  if (!response.ok) {
    const detail = typeof payload === "object" && payload ? (payload as { detail?: unknown }).detail : payload;
    throw new ApiError(response.status, detail);
  }
  return payload as T;
}

function postJson<T>(path: string, body: unknown): Promise<T> {
  return api<T>(path, { method: "POST", body: JSON.stringify(body) });
}

export function teacherLogin(username: string, password: string): Promise<LoginResponse> {
  return postJson<LoginResponse>("/api/auth/login", { username, password });
}

export function loadCurrentUser(): Promise<User> {
  return api<User>("/api/auth/me");
}

export function listExperiments(): Promise<ApiList<Experiment>> {
  return api<ApiList<Experiment>>("/api/admin/experiments");
}

export function listClasses(): Promise<ClassItem[]> {
  return api<ClassItem[]>("/api/admin/classes");
}

export function listQuestionBanks(): Promise<ApiList<QuestionBankSummary>> {
  return api<ApiList<QuestionBankSummary>>("/api/admin/question-banks");
}

export function listCatalogQuestionBank(): Promise<CatalogQuestionBankResponse> {
  return api<CatalogQuestionBankResponse>("/api/admin/question-banks/catalog");
}

export function listLegacyVideoPoints(query = ""): Promise<LegacyVideoPointResponse> {
  const params = new URLSearchParams({ limit: "500" });
  if (query.trim()) params.set("q", query.trim());
  return api<LegacyVideoPointResponse>(`/api/admin/legacy/video-points?${params.toString()}`);
}

export function setLegacyVideoPointRecommendation(nodeId: string, recommended: boolean, sortOrder = 0): Promise<LegacyVideoPointResponse> {
  return api<LegacyVideoPointResponse>(`/api/admin/legacy/video-points/${encodeURIComponent(nodeId)}/recommendation`, {
    method: "PUT",
    body: JSON.stringify({ recommended, sort_order: sortOrder }),
  });
}

export function createQuestionWorkbenchSession(payload: {
  mode: "create" | "repair";
  experiment_id: string;
  prompt: string;
  point_node_id?: string | null;
}): Promise<QuestionWorkbenchSession> {
  return postJson<QuestionWorkbenchSession>("/api/admin/question-banks/workbench-sessions", payload);
}

export function getAnalyticsDashboard(classId: string): Promise<AnalyticsDashboard> {
  return api<AnalyticsDashboard>(`/api/admin/analytics/classes/${encodeURIComponent(classId)}/dashboard`);
}
