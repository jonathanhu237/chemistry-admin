## Why

Teacher video uploads currently produce a browser-friendly student playback file by keeping only the first video stream and optional first audio stream. The worker explicitly strips subtitle and attachment streams, which is the right default for stable MP4 playback, but it leaves the system with no supported way to provide subtitles to students.

We need a subtitle model that keeps videos fixed, avoids burn-in, and lets teachers add external subtitle tracks either after a video exists or while they are selecting/uploading a video. Upload-time subtitle selection should be convenient, but the persisted model should still bind subtitles to the resulting media asset rather than mixing subtitle files into video transcode.

## What Changes

- Add external subtitle tracks as first-class artifacts attached to video media assets.
- Keep student playback video generation subtitle-free: no burn-in, no subtitle stream muxing into the MP4 learning rendition.
- Support teacher-managed subtitle tracks after upload: upload, list, preview, delete, set default, language/label metadata, and conversion status.
- Support upload-time subtitle linking: a teacher can select a subtitle file alongside a video queue item, shown with a link marker, and the upload manager attaches it to the created/reused media asset after video finalization.
- Normalize supported subtitle inputs to WebVTT for student playback.
- Expose subtitle tracks in teacher preview and student playback read models with directly loadable stream URLs.
- Include subtitle artifacts in media delete planning and physical cleanup.
- Keep duplicate detection based on video content only; subtitles do not affect exact or perceptual video duplicate detection.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `teacher-video-resource-library`: add subtitle track management and upload-time linked subtitle selection for video resources.
- `media-asset-lifecycle`: add subtitle track artifacts, normalization, serving, deletion cleanup, and worker policy that keeps generated video subtitle-free.
- `student-h5-learning-experience`: render available subtitle tracks during student point video playback.
- `student-h5-video-discovery`: carry subtitle metadata where feed/library videos can open a full playback surface, while lightweight muted previews may omit subtitle loading.

## Impact

- Teacher frontend: video upload modal/queue item model, video detail/preview modal, resource card actions, media API types, and focused contract tests.
- Student frontend: point video player, catalog/video detail playback surfaces, optional feed/library playback details, and tests for `<track>` rendering.
- Backend media API: subtitle track CRUD, subtitle upload/normalization endpoints, authenticated/preview/student stream endpoints, and API response models.
- Backend media domain: media asset read models, file state/delete planning, subtitle path containment checks, lifecycle cleanup, and exact duplicate reuse rules when a linked subtitle is selected.
- Worker/processing: continue stripping subtitle streams from generated playback output; optionally probe embedded subtitle stream counts for diagnostics without publishing them.
- Data model/migrations: subtitle track table, optional conversion job/status fields, artifact paths, default track uniqueness, and safe cleanup indexes.
- Operations/docs: document accepted subtitle formats, WebVTT normalization, no burn-in policy, browser auth/CORS requirements for `<track>`, and teacher expectations for embedded subtitles.
