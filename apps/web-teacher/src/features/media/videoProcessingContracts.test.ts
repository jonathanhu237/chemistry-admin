import { describe, expect, it } from "vitest";

import type { MediaAsset } from "../../api/media";
import { isPreviewableVideo } from "../../lib/resourceUtils";
import { isBackgroundAnalysisActive, isBackgroundAnalysisFailed, processingPhaseText } from "./mediaHelpers";

function asset(overrides: Partial<MediaAsset>): MediaAsset {
  return {
    id: "asset-1",
    title: "Video",
    original_file_name: "video.mp4",
    upload_status: "ready",
    mime_type: "video/mp4",
    primary_file_available: true,
    ...overrides,
  };
}

describe("video processing playback readiness contracts", () => {
  it("allows preview when playback output exists while duplicate detection runs", () => {
    const item = asset({
      upload_status: "ready",
      playback_relative_path: "renditions/asset-1/learning.mp4",
      processing_phase: "fingerprinting",
      processing_progress: 78,
      processing_job: {
        id: "job-1",
        status: "processing",
        phase: "fingerprinting",
        progress: 78,
      },
    });

    expect(isPreviewableVideo(item)).toBe(true);
    expect(isBackgroundAnalysisActive(item)).toBe(true);
    expect(processingPhaseText(item)).toBe("生成重复检测签名");
  });

  it("does not allow preview without playback output unless the asset is fully ready", () => {
    expect(isPreviewableVideo(asset({ upload_status: "processing", playback_relative_path: null }))).toBe(false);
    expect(isPreviewableVideo(asset({ upload_status: "ready", playback_relative_path: null }))).toBe(true);
  });

  it("keeps preview enabled when only duplicate detection failed", () => {
    const item = asset({
      playback_relative_path: "renditions/asset-1/learning.mp4",
      processing_phase: "duplicate_detection_failed",
      processing_job: {
        id: "job-1",
        status: "failed",
        phase: "failed",
        progress: 0,
        error_reason: "Duplicate detection failed: vpdq failed",
      },
    });

    expect(isPreviewableVideo(item)).toBe(true);
    expect(isBackgroundAnalysisFailed(item)).toBe(true);
    expect(processingPhaseText(item)).toBe("重复检测失败");
  });
});
