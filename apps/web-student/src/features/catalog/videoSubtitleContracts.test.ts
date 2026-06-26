import { describe, expect, it } from "vitest";

import apiSource from "../../api.ts?raw";
import catalogPointDetailPanelSource from "./CatalogPointDetailPanel.tsx?raw";
import pointVideoPlayerSource from "./PointVideoPlayer.tsx?raw";
import homeRootPageSource from "../../routes/home/HomeRootPage.tsx?raw";

describe("student video subtitle contracts", () => {
  it("carries ready subtitle metadata in student video API types", () => {
    expect(apiSource).toContain("export type StudentVideoSubtitleTrack");
    expect(apiSource).toContain('kind: "subtitles" | "captions" | string');
    expect(apiSource).toContain("stream_path: string");
    expect(apiSource).toContain("subtitle_tracks?: StudentVideoSubtitleTrack[]");
  });

  it("maps point video subtitle stream paths into full playback tracks", () => {
    expect(catalogPointDetailPanelSource).toContain("video?.subtitle_tracks || []");
    expect(catalogPointDetailPanelSource).toContain("resolveMediaUrl(track.stream_path)");
    expect(catalogPointDetailPanelSource).toContain("subtitleTracks={subtitleTracks}");
  });

  it("attaches native track elements to the full video player and removes them on cleanup", () => {
    expect(pointVideoPlayerSource).toContain("subtitleTracks = []");
    expect(pointVideoPlayerSource).toContain('document.createElement("track")');
    expect(pointVideoPlayerSource).toContain('element.kind = track.kind === "captions" ? "captions" : "subtitles"');
    expect(pointVideoPlayerSource).toContain('element.srclang = track.language_code || "und"');
    expect(pointVideoPlayerSource).toContain("element.default = true");
    expect(pointVideoPlayerSource).toContain("art.video.appendChild(element)");
    expect(pointVideoPlayerSource).toContain("trackElements.forEach((element) => element.remove())");
  });

  it("keeps lightweight home previews from eager subtitle track loading", () => {
    expect(homeRootPageSource).not.toContain("<track");
    expect(homeRootPageSource).not.toContain("subtitle_tracks");
  });
});
