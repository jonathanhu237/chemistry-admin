import { useEffect, useRef } from "react";

import { isTeacherStudentPreview } from "../previewSandbox";
import { useStudentRuntime } from "../../shell/studentAppContext";
import {
  parsePreviewInputMessage,
  readPreviewInputHandshake,
  type PreviewInputMessage,
  type PreviewInputPoint,
} from "./previewInputProtocol";

type ActivePreviewInputSequence = {
  sequenceId: string;
  initialTarget: Element | null;
  lastPoint: PreviewInputPoint;
  moved: boolean;
};

type ScrollTarget =
  | { kind: "element"; element: HTMLElement }
  | { kind: "document"; element: Element };

const actionableSelector = [
  "button",
  "a[href]",
  "input",
  "textarea",
  "select",
  "summary",
  "label",
  "[role='button']",
  "[role='tab']",
  "[role='link']",
  "[tabindex]",
].join(",");

function isHTMLElement(value: Element | null): value is HTMLElement {
  return value instanceof HTMLElement;
}

function isDisabledControl(element: Element): boolean {
  return (
    (element instanceof HTMLButtonElement && element.disabled) ||
    (element instanceof HTMLInputElement && element.disabled) ||
    (element instanceof HTMLTextAreaElement && element.disabled) ||
    (element instanceof HTMLSelectElement && element.disabled)
  );
}

function isEditableElement(element: Element): element is HTMLElement {
  return (
    element instanceof HTMLInputElement ||
    element instanceof HTMLTextAreaElement ||
    element instanceof HTMLSelectElement ||
    (element instanceof HTMLElement && element.isContentEditable)
  );
}

function canOverflowY(element: HTMLElement): boolean {
  const style = window.getComputedStyle(element);
  return /(auto|scroll|overlay)/.test(`${style.overflowY} ${style.overflow}`);
}

function scrollRange(element: Element): { top: number; max: number } {
  const top = "scrollTop" in element ? Number(element.scrollTop) : 0;
  const scrollHeight = "scrollHeight" in element ? Number(element.scrollHeight) : 0;
  const clientHeight = "clientHeight" in element ? Number(element.clientHeight) : 0;
  return { top, max: Math.max(0, scrollHeight - clientHeight) };
}

function canScrollInDirection(element: Element, deltaScroll: number): boolean {
  const { top, max } = scrollRange(element);
  if (max <= 0) return false;
  if (deltaScroll > 0) return top < max;
  if (deltaScroll < 0) return top > 0;
  return false;
}

export function elementFromPreviewPoint(point: PreviewInputPoint): Element | null {
  if (typeof document.elementFromPoint !== "function") return null;
  return document.elementFromPoint(point.x, point.y);
}

export function findScrollablePreviewTarget(start: Element | null, deltaScroll: number): ScrollTarget | null {
  let current: Element | null = start;
  while (current && current !== document.body && current !== document.documentElement) {
    if (isHTMLElement(current) && canOverflowY(current) && canScrollInDirection(current, deltaScroll)) {
      return { kind: "element", element: current };
    }
    current = current.parentElement;
  }

  const scrollingElement = document.scrollingElement || document.documentElement;
  return canScrollInDirection(scrollingElement, deltaScroll) ? { kind: "document", element: scrollingElement } : null;
}

export function applyPreviewScroll(target: ScrollTarget | null, deltaScroll: number): void {
  if (!target || deltaScroll === 0) return;
  const { top, max } = scrollRange(target.element);
  const nextTop = Math.min(Math.max(top + deltaScroll, 0), max);
  if ("scrollTop" in target.element) {
    target.element.scrollTop = nextTop;
  }
}

export function resolvePreviewActionTarget(initialTarget: Element | null, fallbackPoint: PreviewInputPoint): Element | null {
  const fallbackTarget = elementFromPreviewPoint(fallbackPoint);
  const candidate = initialTarget?.isConnected ? initialTarget : fallbackTarget;
  if (!candidate) return null;
  if (isDisabledControl(candidate)) return null;
  const actionable = candidate.closest(actionableSelector);
  if (!actionable || isDisabledControl(actionable)) return null;
  return actionable;
}

export function activatePreviewTarget(target: Element | null): boolean {
  if (!target || !target.isConnected || isDisabledControl(target)) return false;
  if (isEditableElement(target)) {
    target.focus({ preventScroll: true });
    target.click();
    return true;
  }
  if (target instanceof HTMLElement || target instanceof SVGElement) {
    target.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
    return true;
  }
  return false;
}

function allowedOrigins(teacherOrigin: string): Set<string> {
  const origins = new Set<string>();
  if (teacherOrigin) origins.add(teacherOrigin);
  if (document.referrer) {
    try {
      origins.add(new URL(document.referrer).origin);
    } catch {
      // Ignore malformed referrers.
    }
  }
  origins.add(window.location.origin);
  if (window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost") {
    origins.add(`${window.location.protocol}//${window.location.hostname}:5174`);
    origins.add(`${window.location.protocol}//${window.location.hostname}:4174`);
  }
  return origins;
}

function messageMatchesHandshake(message: PreviewInputMessage, origin: string, frameId: string, teacherOrigin: string): boolean {
  if (frameId && message.frameId !== frameId) return false;
  return allowedOrigins(teacherOrigin).has(origin);
}

export function PreviewInputRuntime() {
  const runtime = useStudentRuntime();
  const activeSequenceRef = useRef<ActivePreviewInputSequence | null>(null);
  const enabled = isTeacherStudentPreview(runtime);

  useEffect(() => {
    if (!enabled) {
      activeSequenceRef.current = null;
      return;
    }

    const { frameId, teacherOrigin } = readPreviewInputHandshake();

    const clearSequence = () => {
      activeSequenceRef.current = null;
    };

    const handleMessage = (event: MessageEvent) => {
      const message = parsePreviewInputMessage(event.data);
      if (!message || !messageMatchesHandshake(message, event.origin, frameId, teacherOrigin)) {
        if (message?.type === "touchCancel") clearSequence();
        return;
      }

      if (message.type === "hover") return;

      if (message.type === "touchCancel") {
        clearSequence();
        return;
      }

      if (message.type === "touchStart") {
        activeSequenceRef.current = {
          sequenceId: message.sequenceId,
          initialTarget: elementFromPreviewPoint(message.point),
          lastPoint: message.point,
          moved: false,
        };
        return;
      }

      const activeSequence = activeSequenceRef.current;
      if (!activeSequence || activeSequence.sequenceId !== message.sequenceId) {
        return;
      }

      if (message.type === "longPress") {
        return;
      }

      if (message.type === "tap") {
        const target = resolvePreviewActionTarget(activeSequence.initialTarget, message.point);
        activatePreviewTarget(target);
        clearSequence();
        return;
      }

      if (message.type === "touchMove") {
        const previousPoint = message.previousPoint || activeSequence.lastPoint;
        const deltaScroll = previousPoint.y - message.point.y;
        const hitTarget = elementFromPreviewPoint(message.point) || activeSequence.initialTarget;
        const scrollTarget = findScrollablePreviewTarget(hitTarget, deltaScroll);
        applyPreviewScroll(scrollTarget, deltaScroll);
        activeSequence.lastPoint = message.point;
        if (Math.abs(deltaScroll) > 0) activeSequence.moved = true;
        return;
      }

      if (message.type === "touchEnd") {
        clearSequence();
      }
    };

    window.addEventListener("message", handleMessage);
    window.addEventListener("beforeunload", clearSequence);
    return () => {
      window.removeEventListener("message", handleMessage);
      window.removeEventListener("beforeunload", clearSequence);
      clearSequence();
    };
  }, [enabled]);

  return null;
}
