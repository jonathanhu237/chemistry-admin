import { cleanup, fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import { LegacyTeacherApp } from "./LegacyTeacherApp";
import { setAuthToken } from "./api";

const forbiddenVisibleTerms = [
  "Atom",
  "RAG",
  "Agent",
  "chunk",
  "embedding",
  "rerank",
  "Qwen",
  "BGE",
  "OpenAI",
  "学习助手",
  "智能监控",
];

function jsonResponse(payload: unknown, status = 200): Response {
  return new Response(JSON.stringify(payload), {
    status,
    headers: { "content-type": "application/json" },
  });
}

function installTeacherFetchMock() {
  return vi.fn(async (input: RequestInfo | URL, init?: RequestInit) => {
    const url = String(input);
    const legacyPointItems = [
      {
        id: "point-1",
        node_id: "point-1",
        chapter_id: "chapter-halogen",
        title: "氯水漂白性实验",
        summary: "观察氯水漂白现象。",
        snippet: "试纸逐渐褪色。",
        catalog_path: ["第13章 卤族元素", "氯的氧化性", "氯水漂白性实验"],
        media_count: 1,
        published_media_count: 1,
        is_recommended: init?.method === "PUT",
        recommended_order: init?.method === "PUT" ? 0 : null,
      },
    ];
    if (url.includes("/api/auth/me")) {
      return jsonResponse({
        id: "teacher-1",
        username: "teacher",
        display_name: "王老师",
        role: "teacher",
        status: "active",
      });
    }
    if (url.includes("/api/admin/legacy/video-points") && init?.method === "PUT") {
      return jsonResponse({
        status: "ok",
        query: "",
        total: legacyPointItems.length,
        items: legacyPointItems,
      });
    }
    if (url.includes("/api/admin/legacy/video-points")) {
      return jsonResponse({
        status: "ok",
        query: "",
        total: legacyPointItems.length,
        items: legacyPointItems.map((item) => ({ ...item, is_recommended: false, recommended_order: null })),
      });
    }
    if (url.includes("/api/admin/experiments")) {
      return jsonResponse({
        total: 1,
        items: [
          {
            id: "exp-1",
            code: "EXP-001",
            title: "氯水漂白性实验",
            status: "published",
            published_question_count: 12,
            draft_question_count: 2,
            generated_draft_count: 1,
            media_resources: [{ media_id: "media-1", title: "实验视频" }],
          },
        ],
      });
    }
    if (url.includes("/api/admin/classes")) {
      return jsonResponse([{ id: "class-1", class_name: "无机化学一班", status: "active", student_count: 38 }]);
    }
    if (url.includes("/api/admin/question-banks/catalog")) {
      return jsonResponse({
        total: 1,
        items: [
          {
            node_id: "point-1",
            node_kind: "point",
            title: "氯水漂白性实验",
            status: "published",
            counts: {
              question_count: 5,
              published_count: 4,
              draft_count: 1,
            },
          },
        ],
      });
    }
    if (url.includes("/api/admin/question-banks/workbench-sessions") && init?.method === "POST") {
      return jsonResponse({
        id: "session-1",
        mode: "create",
        experiment_id: "exp-1",
        status: "draft",
      });
    }
    if (url.includes("/api/admin/question-banks")) {
      return jsonResponse({
        total: 1,
        items: [
          {
            id: "exp-1",
            code: "EXP-001",
            title: "氯水漂白性实验",
            status: "published",
            published_question_count: 12,
            draft_question_count: 2,
            generated_draft_count: 1,
            media_resources: [],
            banks: [
              {
                id: "bank-1",
                title: "氯水漂白性实验",
                status: "active",
                question_count: 5,
                published_count: 4,
                draft_count: 1,
              },
            ],
          },
        ],
      });
    }
    if (url.includes("/api/admin/analytics/classes/class-1/dashboard")) {
      return jsonResponse({
        metrics: {
          class_size: 38,
          active_students: 30,
          completion_rate: 78.5,
          average_score: 83.2,
        },
        matrix: [
          {
            student_id: "2026001",
            student_name: "李同学",
            average_score: 82,
            experiment_groups: {
              group1: {
                evidence_count: 3,
                mastery_score: 72,
                score: 82,
                attempt_count: 2,
                has_mastery: true,
              },
            },
          },
        ],
      });
    }
    return jsonResponse({}, 404);
  });
}

function assertNoForbiddenVisibleTerms(container: HTMLElement) {
  const text = container.textContent || "";
  for (const term of forbiddenVisibleTerms) {
    expect(text).not.toContain(term);
  }
}

describe("LegacyTeacherApp", () => {
  beforeEach(() => {
    window.history.pushState({}, "", "/");
    window.localStorage.clear();
    setAuthToken("teacher-token");
    vi.stubGlobal("fetch", installTeacherFetchMock());
  });

  afterEach(() => {
    setAuthToken("");
    cleanup();
    vi.unstubAllGlobals();
  });

  it("renders legacy teacher navigation without excluded monitoring or assistant surfaces", async () => {
    const { container } = render(<LegacyTeacherApp />);

    expect(await screen.findByRole("heading", { name: "教学工作台" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "实验资源" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "推荐学习" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "AI出题与题库" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "学情分数" })).toBeTruthy();
    assertNoForbiddenVisibleTerms(container);
  });

  it("lets teachers mark old student video points as recommended learning", async () => {
    const { container } = render(<LegacyTeacherApp />);

    fireEvent.click(await screen.findByRole("button", { name: "推荐学习" }));
    expect(await screen.findByRole("heading", { name: "推荐学习点位" })).toBeTruthy();
    expect(await screen.findByText("氯水漂白性实验")).toBeTruthy();
    fireEvent.click(screen.getByRole("button", { name: "设为推荐" }));

    expect(await screen.findByText("已设为推荐学习：氯水漂白性实验")).toBeTruthy();
    expect(screen.getAllByText("推荐学习").length).toBeGreaterThan(0);
    expect(screen.getByRole("button", { name: "取消推荐" })).toBeTruthy();
    expect(vi.mocked(fetch).mock.calls.some((call) => String(call[0]).includes("/api/admin/legacy/video-points/point-1/recommendation"))).toBe(true);
    assertNoForbiddenVisibleTerms(container);
  });

  it("keeps AI question generation, teacher review, and legacy source labels", async () => {
    const { container } = render(<LegacyTeacherApp />);

    fireEvent.click(await screen.findByRole("button", { name: "AI出题与题库" }));
    expect(await screen.findByRole("heading", { name: "题库建设与教师审核" })).toBeTruthy();
    expect(screen.getByText("出题依据")).toBeTruthy();
    expect(screen.getByText("教材依据")).toBeTruthy();
    fireEvent.click(screen.getByRole("button", { name: "AI出题" }));
    expect(await screen.findByText("已创建教师审核会话：session-1")).toBeTruthy();
    fireEvent.click(screen.getByRole("button", { name: "退回修改" }));
    expect(screen.getByText("已退回修改，需补充教材依据或实验资料依据。")).toBeTruthy();
    assertNoForbiddenVisibleTerms(container);
  });

  it("reads shared class analytics and explains scores through BKT", async () => {
    const { container } = render(<LegacyTeacherApp />);

    fireEvent.click(await screen.findByRole("button", { name: "学情分数" }));
    expect(await screen.findByRole("heading", { name: "BKT 班级学情" })).toBeTruthy();
    expect(await screen.findByText("李同学")).toBeTruthy();
    expect(await screen.findByText("已有BKT证据")).toBeTruthy();
    assertNoForbiddenVisibleTerms(container);
  });

  it("redirects stale monitoring routes to the safe dashboard", async () => {
    window.history.pushState({}, "", "/monitoring/runtime");
    const { container } = render(<LegacyTeacherApp />);

    expect(await screen.findByRole("heading", { name: "教学工作台" })).toBeTruthy();
    await waitFor(() => expect(window.location.pathname).toBe("/"));
    assertNoForbiddenVisibleTerms(container);
  });
});
