import { beforeEach, describe, expect, it, vi } from "vitest";

import {
  activatePreviewTarget,
  applyPreviewScroll,
  findScrollablePreviewTarget,
  resolvePreviewActionTarget,
} from "./PreviewInputRuntime";
import {
  parsePreviewInputMessage,
  storePreviewInputHandshake,
  studentPreviewInputNamespace,
  studentPreviewInputVersion,
} from "./previewInputProtocol";

function defineScrollMetrics(element: HTMLElement, metrics: { scrollHeight: number; clientHeight: number; scrollTop?: number }) {
  Object.defineProperty(element, "scrollHeight", { configurable: true, value: metrics.scrollHeight });
  Object.defineProperty(element, "clientHeight", { configurable: true, value: metrics.clientHeight });
  Object.defineProperty(element, "scrollTop", {
    configurable: true,
    get: () => metrics.scrollTop ?? 0,
    set: (value) => {
      metrics.scrollTop = value;
    },
  });
}

describe("student preview input runtime helpers", () => {
  beforeEach(() => {
    document.body.innerHTML = "";
    sessionStorage.clear();
    vi.restoreAllMocks();
  });

  it("parses only versioned preview input messages", () => {
    const valid = {
      namespace: studentPreviewInputNamespace,
      version: studentPreviewInputVersion,
      frameId: "frame-1",
      sequenceId: "sequence-1",
      type: "tap",
      point: { x: 12, y: 24 },
      timestamp: 123,
      primaryButton: false,
      modifiers: { alt: false, ctrl: false, meta: false, shift: false },
    };

    expect(parsePreviewInputMessage(valid)).toMatchObject(valid);
    expect(parsePreviewInputMessage({ ...valid, namespace: "other" })).toBeNull();
    expect(parsePreviewInputMessage({ ...valid, point: { x: Number.NaN, y: 24 } })).toBeNull();
  });

  it("stores preview frame and teacher origin handshake data", () => {
    storePreviewInputHandshake("frame-1", "http://127.0.0.1:5174");

    expect(sessionStorage.getItem("chem_student_preview_frame_id")).toBe("frame-1");
    expect(sessionStorage.getItem("chem_student_preview_teacher_origin")).toBe("http://127.0.0.1:5174");
  });

  it("activates real actionable elements through click without leaving desktop focus", () => {
    const button = document.createElement("button");
    const clickHandler = vi.fn();
    button.addEventListener("click", clickHandler);
    document.body.appendChild(button);

    const target = resolvePreviewActionTarget(button, { x: 0, y: 0 });
    expect(activatePreviewTarget(target)).toBe(true);

    expect(clickHandler).toHaveBeenCalledTimes(1);
    expect(document.activeElement).toBe(document.body);
  });

  it("focuses editable elements without replacing them", () => {
    const input = document.createElement("input");
    const clickHandler = vi.fn();
    input.addEventListener("click", clickHandler);
    document.body.appendChild(input);

    expect(activatePreviewTarget(input)).toBe(true);
    expect(document.activeElement).toBe(input);
    expect(clickHandler).toHaveBeenCalledTimes(1);
  });

  it("finds the nearest scrollable ancestor for upward and downward drags", () => {
    const outer = document.createElement("div");
    const inner = document.createElement("div");
    const child = document.createElement("button");
    outer.style.overflowY = "auto";
    inner.style.overflowY = "auto";
    defineScrollMetrics(outer, { scrollHeight: 1000, clientHeight: 300, scrollTop: 100 });
    defineScrollMetrics(inner, { scrollHeight: 800, clientHeight: 200, scrollTop: 20 });
    inner.appendChild(child);
    outer.appendChild(inner);
    document.body.appendChild(outer);

    expect(findScrollablePreviewTarget(child, 30)).toMatchObject({ kind: "element", element: inner });
    applyPreviewScroll(findScrollablePreviewTarget(child, 30), 30);
    expect(inner.scrollTop).toBe(50);

    applyPreviewScroll(findScrollablePreviewTarget(child, -40), -40);
    expect(inner.scrollTop).toBe(10);
  });

  it("clamps scroll positions to valid ranges", () => {
    const scroller = document.createElement("div");
    scroller.style.overflowY = "auto";
    defineScrollMetrics(scroller, { scrollHeight: 500, clientHeight: 100, scrollTop: 390 });
    document.body.appendChild(scroller);

    applyPreviewScroll({ kind: "element", element: scroller }, 100);
    expect(scroller.scrollTop).toBe(400);

    applyPreviewScroll({ kind: "element", element: scroller }, -999);
    expect(scroller.scrollTop).toBe(0);
  });
});
