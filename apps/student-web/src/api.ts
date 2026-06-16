export type AuthUser = {
  id: string;
  username: string;
  role: "admin" | "teacher" | "student";
  display_name: string;
  status: string;
  must_change_password: boolean;
  password_version: number;
  student_id?: string | null;
  class_id?: string | null;
  class_name?: string | null;
};

export type LoginResponse = {
  access_token: string;
  token_type: "bearer";
  expires_at: string;
  user: AuthUser;
};

export const apiBase = (import.meta.env.VITE_API_BASE_URL || "").replace(/\/$/, "");
const tokenKey = "chem_student_token";

let authToken = localStorage.getItem(tokenKey) || "";

export function getAuthToken(): string {
  return authToken;
}

export function setAuthToken(token: string): void {
  authToken = token;
  if (token) {
    localStorage.setItem(tokenKey, token);
  } else {
    localStorage.removeItem(tokenKey);
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

export function errorMessage(error: unknown): string {
  if (error instanceof ApiError) {
    if (error.status === 409) return "账号配置异常，请联系教师";
    if (typeof error.detail === "string") return error.detail;
    return "请求失败，请稍后重试";
  }
  if (error instanceof Error) return error.message;
  return "请求失败，请稍后重试";
}

async function api<T>(path: string, options: RequestInit = {}): Promise<T> {
  const headers = new Headers(options.headers || {});
  if (!(options.body instanceof FormData) && !headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }
  if (authToken) {
    headers.set("Authorization", `Bearer ${authToken}`);
  }
  const response = await fetch(`${apiBase}${path}`, { ...options, headers });
  const contentType = response.headers.get("content-type") || "";
  const payload = contentType.includes("application/json") ? await response.json() : await response.text();
  if (response.status === 401) {
    setAuthToken("");
  }
  if (!response.ok) {
    throw new ApiError(response.status, typeof payload === "object" && payload ? payload.detail : payload);
  }
  return payload as T;
}

function postJson<T>(path: string, body: unknown): Promise<T> {
  return api<T>(path, { method: "POST", body: JSON.stringify(body) });
}

export function studentLogin(studentId: string, password: string): Promise<LoginResponse> {
  return postJson<LoginResponse>("/api/auth/student/login", {
    student_id: studentId,
    password,
  });
}

export function changeStudentPassword(currentPassword: string, newPassword: string): Promise<LoginResponse> {
  return postJson<LoginResponse>("/api/auth/student/password", {
    current_password: currentPassword,
    new_password: newPassword,
  });
}

export function loadCurrentUser(): Promise<AuthUser> {
  return api<AuthUser>("/api/auth/me");
}

export async function logout(): Promise<void> {
  if (!authToken) return;
  try {
    await postJson<{ ok: boolean }>("/api/auth/logout", {});
  } finally {
    setAuthToken("");
  }
}
