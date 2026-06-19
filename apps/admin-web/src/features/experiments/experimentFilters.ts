import type { ExperimentVideoPoint } from "../../api/experiments";

export type VideoPointFilter =
  | "all"
  | "empty"
  | "referenced"
  | "published"
  | "missing_content"
  | "draft_content"
  | "published_content"
  | "unpublished_video"
  | "sync_error";

export const videoPointFilterOptions: Array<{ value: VideoPointFilter; label: string }> = [
  { value: "all", label: "全部" },
  { value: "empty", label: "无视频" },
  { value: "referenced", label: "有视频" },
  { value: "published", label: "已发布视频" },
  { value: "missing_content", label: "缺内容" },
  { value: "draft_content", label: "草稿内容" },
  { value: "published_content", label: "已发布内容" },
  { value: "unpublished_video", label: "视频未发布" },
  { value: "sync_error", label: "索引异常" },
];

export function filterVideoPointsForAdmin(points: ExperimentVideoPoint[], filter: VideoPointFilter): ExperimentVideoPoint[] {
  if (filter === "empty") return points.filter((point) => point.resource_count === 0);
  if (filter === "referenced") return points.filter((point) => point.resource_count > 0);
  if (filter === "published") return points.filter((point) => point.published_count > 0);
  if (filter === "missing_content") return points.filter((point) => !point.content || point.content.content_status === "missing");
  if (filter === "draft_content") return points.filter((point) => point.content?.content_status === "draft");
  if (filter === "published_content") return points.filter((point) => point.content?.content_status === "published");
  if (filter === "unpublished_video") return points.filter((point) => point.resource_count > 0 && point.published_count === 0);
  if (filter === "sync_error") return points.filter((point) => point.index_state?.sync_status === "failed");
  return points;
}
