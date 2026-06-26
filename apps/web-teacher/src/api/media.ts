import type { ApiList } from "./common";
import { apiBase, api, patchJson, postJson } from "./http";
import { getAuthToken } from "./auth";

export type MediaSubtitleTrack = {
  id: string;
  media_asset_id: string;
  language_code: string;
  label: string;
  kind: "subtitles" | "captions" | string;
  source_format?: "vtt" | "srt" | string;
  file_size_bytes?: number | null;
  status: "processing" | "ready" | "failed" | string;
  is_default?: boolean;
  error_reason?: string | null;
  metadata?: Record<string, unknown>;
  created_at?: string;
  updated_at?: string;
  reused_existing?: boolean;
};


export type MediaAsset = {
  id: string;
  title: string;
  original_file_name: string;
  relative_path?: string;
  source_relative_path?: string | null;
  thumbnail_relative_path?: string | null;
  playback_relative_path?: string | null;
  playback_mime_type?: string | null;
  checksum_sha256?: string | null;
  mime_type?: string | null;
  file_size_bytes?: number | null;
  duration_seconds?: number | null;
  width?: number | null;
  height?: number | null;
  fps?: number | null;
  bitrate?: number | null;
  video_codec?: string | null;
  audio_codec?: string | null;
  upload_status: string;
  lifecycle_status?: "active" | "archived" | "tombstoned" | string;
  archived_at?: string | null;
  archived_by?: string | null;
  archive_reason?: string | null;
  archive_metadata?: Record<string, unknown>;
  processing_phase?: string | null;
  processing_progress?: number | null;
  error_reason?: string | null;
  created_at?: string;
  updated_at?: string;
  association_count?: number;
  legacy_association_count?: number;
  catalog_binding_count?: number;
  file_state?: "available" | "partial" | "missing" | "pending" | "untracked" | "policy_rejected" | string;
  primary_file_available?: boolean;
  existing_file_count?: number;
  missing_file_count?: number;
  media_files?: MediaFileEntry[];
  processing_job?: MediaProcessingJob | null;
  renditions?: MediaRendition[];
  duplicate_candidates?: MediaDuplicateCandidate[];
  subtitle_tracks?: MediaSubtitleTrack[];
};

export type MediaFileEntry = {
  kind: string;
  kinds?: string[];
  relative_path: string;
  exists: boolean;
  file_size_bytes?: number | null;
  error?: string | null;
};

export type MediaProcessingJob = {
  id: string;
  status: string;
  phase?: string | null;
  progress?: number | null;
  attempts?: number | null;
  error_reason?: string | null;
  updated_at?: string | null;
};

export type MediaRendition = {
  id?: string;
  kind: string;
  relative_path?: string | null;
  mime_type?: string | null;
  file_size_bytes?: number | null;
  duration_seconds?: number | null;
  width?: number | null;
  height?: number | null;
  status?: string | null;
  video_codec?: string | null;
  audio_codec?: string | null;
};

export type MediaDuplicateCandidate = {
  id: string;
  duplicate_type: "exact" | "suspected";
  score?: number | null;
  algorithm: string;
  status: "pending" | "kept" | "reused" | "ignored";
  candidate_asset_id?: string | null;
  candidate_title?: string | null;
  candidate_thumbnail_relative_path?: string | null;
};

export type MediaDuplicatePrecheck = {
  exists: boolean;
  asset?: MediaAsset | null;
};

export type MediaUploadPolicy = {
  max_media_upload_mb: number;
  max_media_upload_bytes: number;
  allowed_extensions?: string[];
};

export type MediaArchiveCatalogBinding = {
  binding_id: string;
  placement_node_id?: string | null;
  canonical_point_id?: string | null;
  point_title?: string | null;
  catalog_path?: string[];
  placement_status?: string | null;
  canonical_point_status?: string | null;
  content_status?: string | null;
  student_visible?: boolean;
  has_other_ready_video?: boolean;
};

export type MediaAssetArchivePlan = {
  asset: MediaAsset;
  can_archive: boolean;
  already_archived: boolean;
  catalog_binding_count: number;
  student_visible_catalog_binding_count: number;
  legacy_generic_binding_count: number;
  processing_job_count: number;
  active_processing_job_count: number;
  rendition_count: number;
  fingerprint_count: number;
  duplicate_candidate_count: number;
  catalog_bindings: MediaArchiveCatalogBinding[];
  message: string;
};

export type MediaAssetArchiveResult = {
  archived: boolean;
  already_archived: boolean;
  asset_id: string;
  lifecycle_status?: string;
  cancelled_processing_jobs?: number;
  plan: MediaAssetArchivePlan;
  catalog_cleanup?: {
    status?: string;
    archived_binding_count?: number;
    affected_placement_count?: number;
    affected_placement_node_ids?: string[];
    error?: string;
  };
};

export type MediaAssetDeleteArtifact = {
  kind?: string;
  kinds?: string[];
  relative_path: string;
  path_safe?: boolean;
  exists?: boolean;
  path_type?: string;
  file_size_bytes?: number | null;
  error?: string | null;
};

export type MediaAssetDeletePlan = {
  asset: MediaAsset;
  can_delete: boolean;
  already_deleted: boolean;
  catalog_binding_count: number;
  student_visible_catalog_binding_count: number;
  legacy_generic_binding_count: number;
  processing_job_count: number;
  active_processing_job_count: number;
  rendition_count: number;
  fingerprint_count: number;
  duplicate_candidate_count: number;
  delete_artifact_count: number;
  existing_delete_artifact_count: number;
  unsafe_delete_artifact_count: number;
  catalog_bindings: MediaArchiveCatalogBinding[];
  delete_artifacts?: MediaAssetDeleteArtifact[];
  message: string;
};

export type MediaAssetDeleteResult = {
  deleted: boolean;
  already_deleted: boolean;
  asset_id: string;
  lifecycle_status?: string;
  cancelled_processing_jobs?: number;
  plan: MediaAssetDeletePlan;
  catalog_cleanup?: {
    status?: string;
    deleted_binding_count?: number;
    affected_placement_count?: number;
    affected_placement_node_ids?: string[];
    error?: string;
  };
  file_cleanup?: {
    status?: string;
    artifact_count?: number;
    deleted_artifact_count?: number;
    failed_artifact_count?: number;
    failed_artifacts?: MediaAssetDeleteArtifact[];
  };
};

export function listMediaAssets(limit = 200): Promise<ApiList<MediaAsset>> {
  return api<ApiList<MediaAsset>>(`/api/admin/media/assets?limit=${limit}`);
}

export function getMediaUploadPolicy(): Promise<MediaUploadPolicy> {
  return api<MediaUploadPolicy>("/api/admin/media/upload-policy");
}

export function getMediaAssetThumbnailUrl(assetId: string): string {
  const accessToken = getAuthToken();
  if (accessToken) {
    return `${apiBase}/api/admin/media/assets/${assetId}/thumbnail-stream?access_token=${encodeURIComponent(accessToken)}`;
  }
  return `${apiBase}/api/admin/media/assets/${assetId}/thumbnail`;
}

export function getMediaAssetFileUrl(assetId: string): string {
  const accessToken = getAuthToken();
  if (accessToken) {
    return getMediaAssetStreamUrl(assetId, accessToken);
  }
  return `${apiBase}/api/admin/media/assets/${assetId}/file`;
}

export function getMediaAssetStreamUrl(assetId: string, accessToken: string): string {
  return `${apiBase}/api/admin/media/assets/${assetId}/stream?access_token=${encodeURIComponent(accessToken)}`;
}

export function getMediaAssetUploadUrl(): string {
  return apiBase + "/api/admin/media/assets";
}

export function precheckMediaDuplicate(payload: unknown): Promise<MediaDuplicatePrecheck> {
  return postJson<MediaDuplicatePrecheck>("/api/admin/media/assets/precheck", payload);
}

export function completeMediaUpload(payload: unknown): Promise<MediaAsset> {
  return postJson<MediaAsset>("/api/admin/media/assets/complete-upload", payload);
}

export function retryMediaProcessing(assetId: string): Promise<unknown> {
  return postJson("/api/admin/media/assets/" + assetId + "/retry-processing", {});
}

export function getMediaAssetArchivePlan(assetId: string): Promise<MediaAssetArchivePlan> {
  return api<MediaAssetArchivePlan>("/api/admin/media/assets/" + assetId + "/archive-plan");
}

export function archiveMediaAsset(assetId: string, reason?: string): Promise<MediaAssetArchiveResult> {
  return postJson<MediaAssetArchiveResult>("/api/admin/media/assets/" + assetId + "/archive", { reason });
}

export function getMediaAssetDeletePlan(assetId: string): Promise<MediaAssetDeletePlan> {
  return api<MediaAssetDeletePlan>("/api/admin/media/assets/" + assetId + "/delete-plan");
}

export function deleteMediaAsset(assetId: string, reason?: string): Promise<MediaAssetDeleteResult> {
  return postJson<MediaAssetDeleteResult>("/api/admin/media/assets/" + assetId + "/delete", { reason });
}

export function updateMediaDuplicateCandidate(id: string, status: string): Promise<unknown> {
  return patchJson("/api/admin/media/duplicate-candidates/" + id, { status });
}

export function listMediaSubtitleTracks(assetId: string): Promise<ApiList<MediaSubtitleTrack>> {
  return api<ApiList<MediaSubtitleTrack>>(`/api/admin/media/assets/${assetId}/subtitle-tracks`);
}

export function uploadMediaSubtitleTrack(assetId: string, payload: FormData): Promise<MediaSubtitleTrack> {
  return api<MediaSubtitleTrack>(`/api/admin/media/assets/${assetId}/subtitle-tracks`, { method: "POST", body: payload });
}

export function updateMediaSubtitleTrack(assetId: string, trackId: string, payload: Partial<Pick<MediaSubtitleTrack, "language_code" | "label" | "kind" | "is_default">>): Promise<MediaSubtitleTrack> {
  return patchJson<MediaSubtitleTrack>(`/api/admin/media/assets/${assetId}/subtitle-tracks/${trackId}`, payload);
}

export function deleteMediaSubtitleTrack(assetId: string, trackId: string): Promise<{ deleted: boolean }> {
  return api<{ deleted: boolean }>(`/api/admin/media/assets/${assetId}/subtitle-tracks/${trackId}`, { method: "DELETE" });
}

export function retryMediaSubtitleTrack(assetId: string, trackId: string): Promise<MediaSubtitleTrack> {
  return postJson<MediaSubtitleTrack>(`/api/admin/media/assets/${assetId}/subtitle-tracks/${trackId}/retry`, {});
}

export function getMediaSubtitleTrackStreamUrl(assetId: string, trackId: string, accessToken: string): string {
  return `${apiBase}/api/admin/media/assets/${assetId}/subtitle-tracks/${trackId}/stream?access_token=${encodeURIComponent(accessToken)}`;
}
