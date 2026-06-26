## Context

The current video pipeline intentionally makes a simple playback file:

```text
source video
  -> ffmpeg map 0:v:0 + 0:a:0?
  -> -sn -dn
  -> learning.mp4
```

That means:

- embedded subtitle streams are not burned into the generated video;
- embedded subtitle streams are not muxed into the generated MP4;
- the student playback source is easier for browser `<video>` to play;
- there is no current product surface for external subtitles.

The desired model is fixed video plus optional external tracks:

```text
teacher video upload
  -> media_asset
  -> thumbnail + student playback MP4
  -> duplicate detection

teacher subtitle upload
  -> media_subtitle_track
  -> normalize to WebVTT
  -> student <track src="...">
```

Upload-time subtitle selection is a convenience layer, not a different backend model:

```text
select video.mkv + subtitle.srt
  -> queue item has client_link_id = abc
  -> upload/finalize video
  -> complete-upload returns media_asset_id
  -> upload subtitle for media_asset_id with client_link_id metadata
  -> track becomes ready when WebVTT is available
```

## Goals / Non-Goals

**Goals:**

- Provide student-visible external subtitles without burning subtitles into video.
- Let teachers attach subtitles both after video upload and while preparing a video upload queue item.
- Keep video processing, video duplicate detection, and subtitle management separate.
- Use WebVTT as the browser playback contract.
- Preserve source subtitle files for audit/reconversion when useful, while serving normalized WebVTT to students.
- Make subtitle errors non-blocking: a video remains playable when a subtitle conversion/upload fails.
- Make subtitle delete/cleanup part of media lifecycle delete planning.

**Non-Goals:**

- Burning subtitles into generated video.
- Making the original MKV/MP4 subtitle streams the primary student playback path.
- Preserving ASS/SSA styling perfectly in the first implementation.
- Point-specific subtitle defaults or per-class subtitle variants.
- AI subtitle generation, subtitle editing timeline UI, or translation workflows.
- HLS/DASH packaging.
- Continuing uploads after browser tab/process close.

## Decisions

### 1. Use asset-level subtitle tracks

Subtitle tracks belong to the media asset. This matches the current resource library mental model: a teacher manages a video resource and its generated student playback file.

Recommended table shape:

```text
media_subtitle_tracks
  id uuid primary key
  media_asset_id uuid not null
  language_code text not null
  label text not null
  kind text not null default 'subtitles'
  source_format text not null
  source_relative_path text null
  webvtt_relative_path text null
  file_size_bytes bigint null
  status text not null
  is_default boolean not null default false
  uploaded_by uuid null
  error_reason text null
  metadata jsonb not null default '{}'
  created_at timestamptz not null
  updated_at timestamptz not null
```

Only one ready default subtitle track should exist per asset. If a teacher sets a new default, the previous default is cleared.

Point-specific subtitle selection remains a future extension. If the same video asset is reused across points, all ready tracks are available to every student playback of that asset.

### 2. Normalize to WebVTT for playback

Browser-native subtitle playback expects WebVTT for `<track>`. The backend should serve ready tracks as `text/vtt; charset=utf-8`.

Supported input policy:

- `.vtt`: validate and store as the ready WebVTT artifact.
- `.srt`: convert to WebVTT and store both source and WebVTT artifacts.
- `.ass` / `.ssa`: optional in the first implementation; if accepted, convert timing/text to WebVTT with a clear style may be simplified diagnostic.

Rejected files should fail as subtitle-track errors, not media asset processing failures.

### 3. Keep generated video subtitle-free

The worker should keep using a subtitle-free output contract:

```text
-map 0:v:0
-map 0:a:0?
-sn
-dn
```

No `subtitles=` video filter, no hard burn-in, and no muxed subtitle stream in the generated MP4.

If the probe sees embedded subtitle streams, the system may expose a teacher-facing diagnostic such as: source file contains embedded subtitles; student playback will not include them automatically; upload an external subtitle track if needed. It should not silently publish embedded subtitles in this change.

### 4. Upload-time subtitle linking is client convenience

When a teacher selects files for upload, the upload UI may support a linked subtitle per video item:

```text
video queue item
  id: local item id
  client_link_id: stable local id
  file: lesson.mkv
  linked_subtitles:
    - file: lesson.zh.srt
      language_code: zh-CN
      label: Chinese
      status: pending_video
```

The subtitle file is not sent through tus as part of the video. After the video item finalizes and the backend returns a `media_asset_id`, the upload manager creates subtitle tracks for that asset through the subtitle API.

This avoids needing a backend record before the video exists and keeps retry/cancel behavior understandable.

### 5. Exact duplicate reuse needs explicit subtitle behavior

If video precheck finds an exact duplicate and the queue item has a linked subtitle, the system must not silently mutate an existing shared media asset without teacher awareness.

Recommended behavior:

- If teacher chooses reuse existing video without changes, the linked subtitle is not attached.
- If teacher chooses reuse existing video and add this subtitle, create a subtitle track on the existing active media asset.
- If a matching ready subtitle track already exists on that asset, show it as duplicate/unchanged rather than creating another identical track.

This keeps SHA duplicate reuse fast while avoiding surprise subtitles appearing on existing course points.

### 6. Subtitle stream URLs must work with native `<track>`

Native `<track>` loading cannot attach arbitrary `Authorization` headers. Subtitle stream URLs must therefore be directly loadable under the same auth pattern as video stream URLs:

- same-origin cookie/session auth where available; or
- access token / preview token in query parameters; and
- correct CORS and `Content-Type: text/vtt; charset=utf-8`.

Teacher preview and student preview endpoints need the same token model as existing video/thumbnail stream endpoints.

### 7. Student playback uses native track support first

For the current student video player, the first implementation should attach tracks directly:

```tsx
<video controls src={videoUrl} poster={posterUrl}>
  <track kind="subtitles" srcLang="zh-CN" label="Chinese" src={trackUrl} default />
</video>
```

If the player has custom controls, it can still use the native TextTrack API later. The first implementation should not introduce a custom subtitle renderer unless the existing player makes native tracks impossible.

Muted auto-playing feed previews may skip loading tracks to keep scrolling cheap. Full playback surfaces should include the track metadata and render ready tracks.

### 8. Subtitle lifecycle follows media asset lifecycle

Media asset delete planning should include subtitle source and WebVTT artifacts. Confirmed deletion should remove subtitle track records or tombstone them as unavailable, and delete safe local subtitle files under `MEDIA_ROOT`.

Subtitle track deletion should be independent and narrower:

- deleting a subtitle track removes only that track and its artifacts;
- it does not delete the video, playback rendition, duplicate fingerprints, or point bindings.

### 9. Video duplicate detection ignores subtitles

Duplicate detection remains about video content:

- exact duplicate precheck uses video file checksum/size;
- perceptual duplicate detection uses video fingerprints;
- subtitle files do not change a video duplicate score;
- two identical videos with different subtitles are still the same video asset from a duplicate-detection perspective, but adding a subtitle to an existing reused asset requires explicit teacher action.

## Risks / Trade-offs

- **Risk: Native track auth fails if URLs require headers.** -> Use stream URLs that work like current video/thumbnail tokenized URLs and test them in browser playback.
- **Risk: ASS/SSA teachers expect styled subtitles.** -> Start with WebVTT normalization and clear style-loss copy; defer rich ASS rendering or burn-in as a separate explicit feature.
- **Risk: Exact duplicate reuse plus subtitles surprises teachers.** -> Require explicit confirmation before adding a linked subtitle to an existing asset found by duplicate precheck.
- **Risk: Multiple subtitles clutter student UI.** -> Support one default and concise labels; leave advanced per-point defaults for a future change.
- **Risk: Subtitle conversion failure looks like video failure.** -> Keep subtitle status separate from media `upload_status` and playback readiness.
- **Risk: Feed autoplay performance degrades.** -> Do not load subtitle tracks for lightweight muted previews unless the user opens a full player.

## Migration Plan

1. Add subtitle track data model and migration without changing existing videos.
2. Add backend subtitle track API, upload/normalize pipeline, and stream endpoints.
3. Add delete-plan/delete cleanup for subtitle artifacts.
4. Extend teacher media API types/read models with `subtitle_tracks`.
5. Add teacher detail/preview subtitle management after upload.
6. Add upload queue linked-subtitle selection and post-finalize attachment.
7. Extend student read models with ready subtitle track metadata and stream paths.
8. Render native `<track>` elements in student full playback and teacher preview.
9. Update docs for no-burn subtitle policy, accepted formats, embedded subtitle expectations, and auth/CORS requirements.

Rollback:

- Disable subtitle track creation in the teacher UI while leaving existing video upload/playback untouched.
- Hide subtitle tracks from student read models if track streaming has browser issues.
- Keep stored subtitle artifacts unavailable until the stream/auth issue is repaired.

## Open Questions

- Should `.ass/.ssa` be accepted in the first pass with lossy WebVTT conversion, or rejected with guidance to upload `.srt/.vtt`?
- Should the default subtitle track be asset-level only, or should a later point-binding-level default be planned soon for course-specific subtitles?
- Should embedded text subtitle extraction be a follow-up convenience, or remain strictly manual to avoid surprising teachers?
