import "@testing-library/jest-dom/vitest";
import { cleanup, fireEvent, render, screen, waitFor } from "@testing-library/react";
import { App as AntApp } from "antd";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import type { Experiment } from "../../api/experiments";
import type { AIConfiguration } from "../../api/settings";
import { LearningAssistantPage } from "./LearningAssistantPage";

const httpMocks = vi.hoisted(() => ({
  api: vi.fn(),
  postJsonStream: vi.fn(),
}));

const catalogHookMocks = vi.hoisted(() => ({
  useAdminChapters: vi.fn(),
  useAdminExperiments: vi.fn(),
}));

vi.mock("../../api/http", () => ({
  api: httpMocks.api,
  apiBase: "",
  isJsonStreamAbort: (error: unknown) => error instanceof DOMException && error.name === "AbortError",
  postJsonStream: httpMocks.postJsonStream,
}));

vi.mock("../../api/auth", () => ({
  getAuthToken: () => "teacher-token",
}));

vi.mock("../../lib/adminCatalogHooks", () => ({
  useAdminChapters: catalogHookMocks.useAdminChapters,
  useAdminExperiments: catalogHookMocks.useAdminExperiments,
}));

vi.mock("../../lib/assistant-markdown", () => ({
  AssistantMarkdownContent: ({ text }: { text?: string | null }) => <span>{text}</span>,
}));

const experiment: Experiment = {
  id: "EXP_17_1",
  code: "17-1",
  title: "卤素置换实验",
  status: "published",
  display_order: 1,
  chapter_bindings: [{ chapter_id: "CH13", chapter_title: "第 13 章", coverage_type: "primary" }],
  media_resources: [
    {
      point_key: "point-1",
      point_title: "氯水 + KBr + CCl4",
      title: "氯水 + KBr + CCl4",
      upload_status: "published",
      binding_status: "active",
    },
  ],
  published_question_count: 0,
  draft_question_count: 0,
  generated_draft_count: 0,
};

const aiConfiguration: AIConfiguration = {
  provider: "openai",
  base_url: "",
  model: "gpt-test",
  connection_check_interval_minutes: 10,
  api_key_configured: true,
  enabled_features: {
    rag_access_enabled: true,
    student_ai_assistant: true,
    student_learning_analytics: true,
    question_bank_assistant: true,
    teacher_learning_analytics: true,
  },
  status: {
    ready: true,
    message: "ok",
    effective_mode: "openai",
    connectivity_status: "connected",
    check_interval_minutes: 10,
    recent_request_count: 0,
    recent_error_count: 0,
    usage_buckets: [],
    usage_trends: {},
  },
  student_ai_policy: {
    active: true,
    version: "test",
    model: "gpt-test",
    coverage: [],
    recent_decision_count: 0,
    invalid_decision_count: 0,
    outcomes: [],
  },
  rag_runtime: {
    rag_enabled: true,
    query_generation_enabled: true,
    keyword_top_k: 16,
    vector_top_k: 20,
    rerank_top_k: 10,
    final_top_k: 5,
    status: "external_textbook_rag",
    message: "External textbook RAG is healthy.",
    textbook_rag_enabled: true,
    textbook_rag_status: "healthy",
    textbook_rag_message: "External textbook RAG is healthy.",
    textbook_rag_index: "canonical-rag-chunks-qwen-v1",
    textbook_rag_models: { embedding: "qwen-embedding", rerank: "qwen-rerank" },
    textbook_rag_diagnostics: { index_exists: true },
  },
  can_edit: true,
};

function renderPage() {
  const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false, gcTime: 0 } },
  });
  return render(
    <QueryClientProvider client={queryClient}>
      <AntApp>
        <LearningAssistantPage />
      </AntApp>
    </QueryClientProvider>,
  );
}

function startTeacherStream() {
  const textarea = screen.getByPlaceholderText("输入学生问题");
  fireEvent.change(textarea, { target: { value: "请解释氯水置换溴离子的现象" } });
  fireEvent.click(screen.getByRole("button", { name: /发送/ }));
}

beforeEach(() => {
  vi.clearAllMocks();
  vi.stubGlobal("matchMedia", vi.fn(() => ({
    matches: false,
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
    addListener: vi.fn(),
    removeListener: vi.fn(),
    dispatchEvent: vi.fn(),
  })));
  vi.stubGlobal("ResizeObserver", class ResizeObserver {
    observe() {}
    unobserve() {}
    disconnect() {}
  });
  Element.prototype.scrollTo = vi.fn();
  catalogHookMocks.useAdminChapters.mockReturnValue({
    data: [{ chapter_id: "CH13", chapter_title: "第 13 章" }],
    isLoading: false,
  });
  catalogHookMocks.useAdminExperiments.mockReturnValue({
    data: { items: [experiment] },
    isLoading: false,
  });
  httpMocks.api.mockImplementation((path: string) => {
    if (path.includes("/api/admin/learning-assistant/runtime")) {
      return Promise.resolve({
        checked_at: "2026-06-25T00:00:00Z",
        rag_runtime: aiConfiguration.rag_runtime,
        textbook_rag_status: "healthy",
        textbook_rag_error: null,
        textbook_rag_diagnostics: { index_exists: true },
      });
    }
    if (path.includes("/api/admin/ai-configuration")) {
      return Promise.resolve(aiConfiguration);
    }
    return Promise.resolve({});
  });
});

afterEach(() => {
  cleanup();
  vi.unstubAllGlobals();
});

describe("LearningAssistantPage stream lifecycle", () => {
  it("aborts the active debug stream on clear and ignores stale stream events", async () => {
    let signal: AbortSignal | undefined;
    let staleDelivered = false;
    httpMocks.postJsonStream.mockImplementationOnce(async (_path, _body, onEvent, options?: { signal?: AbortSignal }) => {
      signal = options?.signal;
      await new Promise<void>((resolve) => {
        signal?.addEventListener("abort", () => resolve(), { once: true });
      });
      onEvent({ event: "delta", data: { delta: "Late admin answer" } });
      onEvent({ event: "final", data: { response: { answer: "Late admin answer" } } });
      staleDelivered = true;
    });

    renderPage();
    startTeacherStream();

    await waitFor(() => expect(httpMocks.postJsonStream).toHaveBeenCalledTimes(1));
    await waitFor(() => expect(screen.getByText("1 轮")).toBeInTheDocument());
    fireEvent.click(screen.getByRole("button", { name: /清\s*空/ }));

    await waitFor(() => expect(signal?.aborted).toBe(true));
    await waitFor(() => expect(staleDelivered).toBe(true));
    expect(screen.queryByText("Late admin answer")).not.toBeInTheDocument();
    expect(screen.getByText("0 轮")).toBeInTheDocument();
  });

  it("aborts the active debug stream on unmount", async () => {
    let signal: AbortSignal | undefined;
    httpMocks.postJsonStream.mockImplementationOnce(async (_path, _body, _onEvent, options?: { signal?: AbortSignal }) => {
      signal = options?.signal;
      await new Promise<void>((resolve) => {
        signal?.addEventListener("abort", () => resolve(), { once: true });
      });
    });

    const view = renderPage();
    startTeacherStream();

    await waitFor(() => expect(httpMocks.postJsonStream).toHaveBeenCalledTimes(1));
    expect(signal).toBeInstanceOf(AbortSignal);

    view.unmount();

    await waitFor(() => expect(signal?.aborted).toBe(true));
  });
});
