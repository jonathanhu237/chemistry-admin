import type { ApiList } from "./common";
import { api, patchJson, postJson, putJson } from "./http";

export type ChapterBinding = {
  chapter_id: string;
  chapter_title?: string;
  chapter_number?: number;
  coverage_type: "primary" | "partial" | "supporting";
  notes?: string | null;
  sort_order?: number;
};

export type MediaResource = {
  binding_id?: string;
  media_id?: string;
  title?: string;
  original_file_name?: string;
  mime_type?: string;
  file_size_bytes?: number;
  thumbnail_relative_path?: string | null;
  upload_status?: string;
  binding_status?: string;
  point_key?: string | null;
  point_title?: string | null;
  published_at?: string;
};

export type Experiment = {
  id: string;
  code: string;
  title: string;
  title_en?: string;
  summary?: string;
  metadata?: Record<string, unknown>;
  family_id?: string;
  family_code?: string;
  family_title?: string;
  status: "draft" | "published" | "archived";
  display_order: number;
  chapter_bindings: ChapterBinding[];
  media_resources: MediaResource[];
  published_question_count: number;
  draft_question_count: number;
  generated_draft_count: number;
};

export type ExperimentVideoPointResource = {
  binding_id: string;
  experiment_id: string;
  experiment_title?: string;
  binding_title?: string | null;
  binding_status: string;
  point_key?: string | null;
  point_title?: string | null;
  media_id: string;
  media_title: string;
  title?: string;
  original_file_name: string;
  mime_type?: string | null;
  file_size_bytes?: number | null;
  thumbnail_relative_path?: string | null;
  upload_status: string;
  error_reason?: string | null;
  published_at?: string | null;
  created_at?: string;
  updated_at?: string;
};

export type ExperimentVideoPoint = {
  point_key: string;
  point_title: string;
  display_order?: number;
  source: "candidate" | "stored" | "legacy" | "seed_candidate" | "media_binding" | "manual";
  status?: "active" | "archived";
  metadata?: Record<string, unknown>;
  resources: ExperimentVideoPointResource[];
  resource_count: number;
  published_count: number;
  content?: {
    principle_mode: "equation" | "text";
    principle_equation?: string | null;
    principle_text?: string | null;
    phenomenon_explanation?: string | null;
    safety_note?: string | null;
    content_status: "missing" | "draft" | "published" | "archived";
    published_at?: string | null;
    updated_at?: string | null;
    metadata?: Record<string, unknown>;
  };
  validation?: {
    complete: boolean;
    errors: string[];
    warnings: string[];
  };
  related_links?: Array<{
    id?: string | null;
    source?: "default" | "default_override" | "manual" | string;
    relation_type?: string;
    hidden?: boolean;
    sort_order?: number;
    label?: string | null;
    target_experiment_id: string;
    target_point_key: string;
    target_point_title?: string | null;
    target_experiment_title?: string | null;
  }>;
  related_link_count?: number;
  index_state?: {
    document_id: string;
    desired_action: "upsert" | "delete";
    sync_status: "pending" | "synced" | "failed" | "disabled";
    attempts: number;
    last_error?: string | null;
    indexed_at?: string | null;
    updated_at?: string | null;
  };
};

export type ExperimentVideoPointsResponse = {
  experiment: {
    id: string;
    code: string;
    title: string;
    status: Experiment["status"];
  };
  points: ExperimentVideoPoint[];
  total_points: number;
  total_resources: number;
  published_resources: number;
};

export type ExperimentListParams = string | URLSearchParams;

function paramsSuffix(params: ExperimentListParams = ""): string {
  const value = typeof params === "string" ? params : params.toString();
  if (!value) return "";
  return value.startsWith("?") ? value : `?${value}`;
}

export function listExperiments(params: ExperimentListParams = ""): Promise<ApiList<Experiment>> {
  return api<ApiList<Experiment>>(`/api/admin/experiments${paramsSuffix(params)}`);
}

export function getExperiment(experimentId: string): Promise<Experiment> {
  return api<Experiment>(`/api/admin/experiments/${experimentId}`);
}

export function createExperiment(payload: { title: string; summary?: string; status: string; chapter_ids: string[] }): Promise<Experiment> {
  return postJson<Experiment>("/api/admin/experiments", payload);
}

export function updateExperiment(
  experimentId: string,
  payload: { title?: string; summary?: string; status?: string; chapter_ids?: string[] },
): Promise<Experiment> {
  return patchJson<Experiment>(`/api/admin/experiments/${experimentId}`, payload);
}

export function listExperimentVideoPoints(experimentId: string): Promise<ExperimentVideoPointsResponse> {
  return api<ExperimentVideoPointsResponse>(`/api/admin/experiments/${experimentId}/video-points`);
}

export function bindExperimentPointResource(
  experimentId: string,
  pointKey: string,
  payload: { media_asset_id: string; title: string; status: string },
): Promise<Record<string, unknown>> {
  return postJson<Record<string, unknown>>(
    `/api/admin/experiments/${experimentId}/video-points/${encodeURIComponent(pointKey)}/resources`,
    payload,
  );
}

export function saveExperimentPointContent(experimentId: string, pointKey: string, payload: Record<string, unknown>): Promise<ExperimentVideoPointsResponse> {
  return putJson<ExperimentVideoPointsResponse>(`/api/admin/experiments/${experimentId}/video-points/${encodeURIComponent(pointKey)}/content`, payload);
}

export function saveExperimentPointRelatedLinks(experimentId: string, pointKey: string, payload: Record<string, unknown>): Promise<ExperimentVideoPointsResponse> {
  return putJson<ExperimentVideoPointsResponse>(`/api/admin/experiments/${experimentId}/video-points/${encodeURIComponent(pointKey)}/related-links`, payload);
}

export function changeExperimentPointPublication(
  experimentId: string,
  pointKey: string,
  payload: { action: "publish" | "unpublish" | "archive" },
): Promise<ExperimentVideoPointsResponse> {
  return postJson<ExperimentVideoPointsResponse>(`/api/admin/experiments/${experimentId}/video-points/${encodeURIComponent(pointKey)}/publication`, payload);
}

export function publishExperimentPointResource(resource: ExperimentVideoPointResource): Promise<Record<string, unknown>> {
  return postJson<Record<string, unknown>>(`/api/admin/media/bindings/${resource.binding_id}/publish`, {});
}

export function unpublishExperimentPointResource(resource: ExperimentVideoPointResource): Promise<Record<string, unknown>> {
  return postJson<Record<string, unknown>>(`/api/admin/media/bindings/${resource.binding_id}/unpublish`, {});
}

export function deleteExperimentPointResource(resource: ExperimentVideoPointResource): Promise<Record<string, unknown>> {
  return api<Record<string, unknown>>(`/api/admin/media/bindings/${resource.binding_id}`, { method: "DELETE" });
}
