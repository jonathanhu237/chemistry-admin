import { describe, expect, it } from "vitest";
import type { ExperimentVideoPoint } from "../../api/experiments";
import { filterVideoPointsForAdmin } from "./experimentFilters";

type Filter = Parameters<typeof filterVideoPointsForAdmin>[1];

function point(key: string, overrides: Partial<ExperimentVideoPoint> = {}): ExperimentVideoPoint {
  return {
    point_key: key,
    point_title: key,
    source: "manual",
    resources: [],
    resource_count: 0,
    published_count: 0,
    ...overrides,
  };
}

function keys(points: ExperimentVideoPoint[], filter: Filter): string[] {
  return filterVideoPointsForAdmin(points, filter).map((item) => item.point_key);
}

describe("filterVideoPointsForAdmin", () => {
  const points = [
    point("missing", { content: { principle_mode: "text", content_status: "missing" } }),
    point("draft", { content: { principle_mode: "text", content_status: "draft" } }),
    point("published", { content: { principle_mode: "text", content_status: "published" }, resource_count: 1, published_count: 1 }),
    point("unpublished-video", { resource_count: 1, published_count: 0 }),
    point("sync-error", { index_state: { document_id: "point:1", desired_action: "upsert", sync_status: "failed", attempts: 2 } }),
  ];

  it("filters by content status, video status, and search sync state", () => {
    expect(keys(points, "missing_content")).toEqual(["missing", "unpublished-video", "sync-error"]);
    expect(keys(points, "draft_content")).toEqual(["draft"]);
    expect(keys(points, "published_content")).toEqual(["published"]);
    expect(keys(points, "unpublished_video")).toEqual(["unpublished-video"]);
    expect(keys(points, "sync_error")).toEqual(["sync-error"]);
  });
});
