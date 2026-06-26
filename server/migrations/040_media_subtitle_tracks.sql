CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS media_subtitle_tracks (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  media_asset_id uuid NOT NULL REFERENCES media_assets(id) ON DELETE CASCADE,
  language_code text NOT NULL,
  label text NOT NULL,
  kind text NOT NULL DEFAULT 'subtitles' CHECK (kind IN ('subtitles', 'captions')),
  source_format text NOT NULL CHECK (source_format IN ('vtt', 'srt')),
  source_relative_path text,
  webvtt_relative_path text,
  file_size_bytes bigint,
  status text NOT NULL DEFAULT 'ready' CHECK (status IN ('processing', 'ready', 'failed')),
  is_default boolean NOT NULL DEFAULT false,
  uploaded_by uuid REFERENCES app_users(id) ON DELETE SET NULL,
  error_reason text,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_media_subtitle_tracks_asset_status
  ON media_subtitle_tracks(media_asset_id, status, is_default DESC, created_at);

CREATE UNIQUE INDEX IF NOT EXISTS idx_media_subtitle_tracks_one_default_ready
  ON media_subtitle_tracks(media_asset_id)
  WHERE status = 'ready' AND is_default;
