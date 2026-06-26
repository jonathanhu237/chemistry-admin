## 1. Data Model And Backend Subtitle Domain

- [x] 1.1 Add a migration for `media_subtitle_tracks` with media asset foreign key, language/label/kind/source format, source path, WebVTT path, status, default flag, metadata, uploaded actor, error diagnostics, and timestamps.
- [x] 1.2 Add uniqueness/guard logic so each media asset has at most one default ready subtitle track.
- [x] 1.3 Add subtitle path helpers that store artifacts under a dedicated `MEDIA_ROOT/subtitles/<asset_id>/...` layout and enforce `MEDIA_ROOT` containment.
- [x] 1.4 Add backend validation for subtitle file extension, MIME guess, size limit, language code, label, and supported kind values.
- [x] 1.5 Implement WebVTT validation for `.vtt` uploads and SRT-to-WebVTT normalization for `.srt` uploads.
- [x] 1.6 Decide first-pass `.ass/.ssa` behavior and implement either explicit rejection or lossy conversion with diagnostics.
- [x] 1.7 Add backend tests for valid VTT upload, valid SRT conversion, invalid subtitle rejection, default uniqueness, and path safety.

## 2. Subtitle APIs And Streaming

- [x] 2.1 Add authenticated admin APIs to list, create/upload, update label/language/default, delete, and retry-normalize subtitle tracks for a media asset.
- [x] 2.2 Add admin subtitle stream endpoint compatible with teacher preview and direct browser `<track>` loading.
- [x] 2.3 Add preview subtitle stream endpoint using existing preview-token scoping.
- [x] 2.4 Add student subtitle stream endpoint scoped to published/student-visible media assets.
- [x] 2.5 Ensure stream responses use `text/vtt; charset=utf-8`, correct filename handling, and auth/CORS behavior compatible with native `<track>`.
- [x] 2.6 Add API/read-model tests for admin, preview, and student subtitle access control.

## 3. Media Lifecycle And Worker Policy

- [x] 3.1 Keep learning rendition generation subtitle-free with explicit `-sn` / `-dn` behavior documented in worker policy tests.
- [x] 3.2 Optionally expose embedded subtitle stream counts from probe metadata for teacher diagnostics without publishing embedded subtitles automatically.
- [x] 3.3 Extend media asset list/detail read models with `subtitle_tracks` summaries and subtitle file-state counts.
- [x] 3.4 Include subtitle source/WebVTT artifacts in media asset delete plans and destructive file cleanup.
- [x] 3.5 Ensure subtitle track deletion removes only that track and does not delete video artifacts, point bindings, duplicate fingerprints, or playback renditions.
- [x] 3.6 Ensure duplicate detection and exact duplicate scoring ignore subtitle files.
- [x] 3.7 Add backend tests for delete plan subtitle artifacts, asset delete subtitle cleanup, subtitle-only delete, and duplicate detection independence.

## 4. Teacher Resource UI

- [x] 4.1 Add media API types/functions for subtitle track list/create/update/delete/stream URLs.
- [x] 4.2 Add subtitle track management to the video resource detail/preview modal: upload, language, label, default marker, status, delete, and retry/error display.
- [x] 4.3 Show clear teacher copy that generated student playback does not burn or carry embedded subtitles; external subtitles must be managed as tracks.
- [x] 4.4 Render ready subtitle tracks in teacher video preview using native `<track>`.
- [x] 4.5 Prevent subtitle conversion/upload failures from changing the video's primary ready/playable status.
- [x] 4.6 Add focused frontend tests/contracts for subtitle management actions, preview track rendering, and non-blocking subtitle errors.

## 5. Upload-Time Linked Subtitle Selection

- [x] 5.1 Extend video upload queue item state with a stable `client_link_id` and optional linked subtitle entries.
- [x] 5.2 Let the teacher attach/remove a subtitle file to a video queue item before starting upload, shown with a link indicator and language/label controls.
- [x] 5.3 Validate linked subtitle files before video upload starts, but keep subtitle upload separate from tus video upload.
- [x] 5.4 After video `complete-upload` returns a media asset id, upload linked subtitle files to that asset and show per-subtitle progress/status.
- [x] 5.5 If exact duplicate precheck reuses an existing asset, require explicit teacher choice before attaching linked subtitles to that existing asset.
- [x] 5.6 Deduplicate linked subtitles against existing ready subtitle tracks on the target asset when source content/language/label already matches.
- [x] 5.7 Add frontend tests for linked subtitle selection, attachment after finalize, exact-duplicate reuse confirmation, cancellation, and retry.

## 6. Student Playback

- [x] 6.1 Extend student point/detail read models with ready subtitle tracks: id, kind, language code, label, default flag, and stream path.
- [x] 6.2 Extend preview/student catalog media read models so teacher preview sees the same subtitle metadata students will get.
- [x] 6.3 Render native `<track>` elements in student full video playback for ready tracks.
- [x] 6.4 Keep lightweight muted feed/home previews from eagerly loading subtitle tracks unless they enter a full playback mode.
- [x] 6.5 Handle subtitle stream failures gracefully without breaking video playback.
- [x] 6.6 Add student frontend tests for default track rendering, multiple language labels, no-track behavior, and failed track non-blocking behavior.

## 7. Documentation And Verification

- [x] 7.1 Document accepted subtitle formats, WebVTT normalization, size limits, and no-burn policy in deployment/media docs.
- [x] 7.2 Document that embedded source subtitles are not automatically included in student playback.
- [x] 7.3 Document `<track>` auth/CORS/token requirements for operators and future frontend work.
- [x] 7.4 Run targeted backend media tests, worker policy tests, and route inventory checks if routes are added.
- [x] 7.5 Run teacher frontend tests/typecheck for media resource UI changes.
- [x] 7.6 Run student frontend tests/typecheck for video player changes.
- [x] 7.7 Manually smoke test: upload video only, upload video with linked SRT, add VTT after upload, preview as teacher, play as student, delete subtitle only, delete whole video.
