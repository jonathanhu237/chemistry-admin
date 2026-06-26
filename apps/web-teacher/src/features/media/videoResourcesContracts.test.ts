import { describe, expect, it } from "vitest";
import mediaApiSource from "../../api/media.ts?raw";
import videoResourcesSource from "./VideoResourcesPage.tsx?raw";

describe("video resource page contracts", () => {
  it("loads upload policy before accepting oversized local videos", () => {
    expect(mediaApiSource).toContain("type MediaUploadPolicy");
    expect(mediaApiSource).toContain("getMediaUploadPolicy");
    expect(mediaApiSource).toContain('"/api/admin/media/upload-policy"');
    expect(videoResourcesSource).toContain('queryKey: ["media-upload-policy"]');
    expect(videoResourcesSource).toContain("file.size > maxUploadBytes");
    expect(videoResourcesSource).toContain("file.size <= maxUploadBytes");
    expect(videoResourcesSource).toContain("超过原始视频大小限制");
    expect(videoResourcesSource).toContain("disabled={batchRunning || !uploadPolicyReady}");
    expect(videoResourcesSource).toContain("const canStartUpload = uploadPolicyReady");
  });

  it("stops preview video playback when the preview modal closes", () => {
    expect(videoResourcesSource).toContain("const previewVideoRef = useRef<HTMLVideoElement | null>(null)");
    expect(videoResourcesSource).toContain("const closePreviewModal = () =>");
    expect(videoResourcesSource).toContain("video.pause()");
    expect(videoResourcesSource).toContain('video.removeAttribute("src")');
    expect(videoResourcesSource).toContain("video.load()");
    expect(videoResourcesSource).toContain("onCancel={closePreviewModal}");
    expect(videoResourcesSource).toContain("ref={previewVideoRef}");
  });

  it("exposes subtitle track APIs and browser-loadable stream URLs", () => {
    expect(mediaApiSource).toContain("type MediaSubtitleTrack");
    expect(mediaApiSource).toContain("subtitle_tracks?: MediaSubtitleTrack[]");
    expect(mediaApiSource).toContain("listMediaSubtitleTracks");
    expect(mediaApiSource).toContain("uploadMediaSubtitleTrack");
    expect(mediaApiSource).toContain("updateMediaSubtitleTrack");
    expect(mediaApiSource).toContain("deleteMediaSubtitleTrack");
    expect(mediaApiSource).toContain("retryMediaSubtitleTrack");
    expect(mediaApiSource).toContain("getMediaSubtitleTrackStreamUrl");
    expect(mediaApiSource).toContain("/subtitle-tracks");
    expect(mediaApiSource).toContain("access_token=");
  });

  it("renders and manages external subtitle tracks without mutating the video asset", () => {
    expect(videoResourcesSource).toContain("renderSubtitlePanel");
    expect(videoResourcesSource).toContain("uploadSubtitle(asset");
    expect(videoResourcesSource).toContain("updateMediaSubtitleTrack(asset.id, track.id, { is_default: true })");
    expect(videoResourcesSource).toContain("retryMediaSubtitleTrack(asset.id, track.id)");
    expect(videoResourcesSource).toContain("deleteMediaSubtitleTrack(asset.id, track.id)");
    expect(videoResourcesSource).toContain("不会删除视频、学生播放源或目录绑定");
    expect(videoResourcesSource).toContain("不会烧录或携带内嵌字幕");
    expect(videoResourcesSource).not.toContain("deleteMediaAsset(asset.id, track.id");
    expect(videoResourcesSource).not.toContain("archiveMediaAsset(asset.id, track.id");
  });

  it("renders ready subtitle tracks in the teacher preview video element", () => {
    expect(videoResourcesSource).toContain("previewSubtitleTracks.map");
    expect(videoResourcesSource).toContain("<track");
    expect(videoResourcesSource).toContain('kind={track.kind === "captions" ? "captions" : "subtitles"}');
    expect(videoResourcesSource).toContain('srcLang={track.language_code || "und"}');
    expect(videoResourcesSource).toContain('label={track.label || track.language_code || "字幕"}');
    expect(videoResourcesSource).toContain("src={track.streamUrl}");
    expect(videoResourcesSource).toContain("default={Boolean(track.is_default) || undefined}");
  });

  it("keeps subtitle errors separate from primary video processing state", () => {
    expect(videoResourcesSource).toContain("track.error_reason");
    expect(videoResourcesSource).toContain('track.status === "failed"');
    expect(videoResourcesSource).toContain("处理失败");
    expect(videoResourcesSource).toContain("retrySubtitle(asset, track)");
    expect(videoResourcesSource).toContain("previewUrl ? (");
    expect(videoResourcesSource).toContain("renderSubtitlePanel(previewAsset)");
  });

  it("links subtitle files to upload queue items before the video asset exists", () => {
    expect(videoResourcesSource).toContain("clientLinkId");
    expect(videoResourcesSource).toContain("linkedSubtitles: []");
    expect(videoResourcesSource).toContain("addLinkedSubtitle");
    expect(videoResourcesSource).toContain("updateLinkedSubtitle");
    expect(videoResourcesSource).toContain("removeLinkedSubtitle");
    expect(videoResourcesSource).toContain("subtitleUploadAccept");
    expect(videoResourcesSource).toContain("外挂字幕会在视频入库后单独绑定");
  });

  it("uploads linked subtitles only after video finalization returns a media asset", () => {
    expect(videoResourcesSource).toContain("uploadLinkedSubtitlesForAsset(asset, item)");
    expect(videoResourcesSource).toContain('body.append("client_link_id", item.clientLinkId)');
    expect(videoResourcesSource).toContain("await uploadMediaSubtitleTrack(asset.id, body)");
    expect(videoResourcesSource).toContain('const asset = await postJson<MediaAsset>("/api/admin/media/assets/complete-upload"');
    expect(videoResourcesSource).toContain('const asset = JSON.parse(xhr.responseText || "{}") as MediaAsset');
  });

  it("requires an explicit duplicate reuse choice before mutating an existing asset with linked subtitles", () => {
    expect(videoResourcesSource).toContain("attachLinkedSubtitlesToDuplicate");
    expect(videoResourcesSource).toContain("markLinkedSubtitlesSkipped");
    expect(videoResourcesSource).toContain("只复用视频");
    expect(videoResourcesSource).toContain("复用并添加字幕");
    expect(videoResourcesSource).not.toContain("if (precheck.duplicateAsset) await uploadLinkedSubtitlesForAsset");
  });
});
