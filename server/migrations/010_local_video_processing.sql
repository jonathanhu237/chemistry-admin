ALTER TABLE media_assets
  DROP CONSTRAINT IF EXISTS media_assets_upload_status_check;

ALTER TABLE media_assets
  ADD CONSTRAINT media_assets_upload_status_check
  CHECK (upload_status IN ('pending', 'processing', 'ready', 'failed', 'replaced'));

ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS source_relative_path text;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS thumbnail_relative_path text;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS playback_relative_path text;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS playback_mime_type text;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS width int;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS height int;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS fps numeric;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS bitrate bigint;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS video_codec text;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS audio_codec text;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS processing_phase text;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS processing_progress int NOT NULL DEFAULT 0;
ALTER TABLE media_assets ADD COLUMN IF NOT EXISTS processed_at timestamptz;

UPDATE media_assets
SET source_relative_path = COALESCE(source_relative_path, relative_path),
    playback_relative_path = COALESCE(playback_relative_path, relative_path),
    playback_mime_type = COALESCE(playback_mime_type, mime_type),
    processing_phase = COALESCE(processing_phase, CASE WHEN upload_status = 'ready' THEN 'ready' ELSE upload_status END),
    processing_progress = CASE WHEN upload_status = 'ready' THEN 100 ELSE processing_progress END
WHERE source_relative_path IS NULL
   OR playback_relative_path IS NULL
   OR playback_mime_type IS NULL
   OR processing_phase IS NULL;

CREATE TABLE IF NOT EXISTS media_processing_jobs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  media_asset_id uuid NOT NULL REFERENCES media_assets(id) ON DELETE CASCADE,
  job_type text NOT NULL DEFAULT 'process_uploaded_video',
  status text NOT NULL DEFAULT 'queued' CHECK (status IN ('queued', 'processing', 'ready', 'failed', 'cancelled')),
  phase text NOT NULL DEFAULT 'queued',
  progress int NOT NULL DEFAULT 0 CHECK (progress >= 0 AND progress <= 100),
  attempts int NOT NULL DEFAULT 0,
  max_attempts int NOT NULL DEFAULT 3,
  error_reason text,
  worker_id text,
  outputs jsonb NOT NULL DEFAULT '{}'::jsonb,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  started_at timestamptz,
  finished_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_media_processing_jobs_status
  ON media_processing_jobs(status, created_at);
CREATE INDEX IF NOT EXISTS idx_media_processing_jobs_asset
  ON media_processing_jobs(media_asset_id, created_at DESC);

CREATE TABLE IF NOT EXISTS media_renditions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  media_asset_id uuid NOT NULL REFERENCES media_assets(id) ON DELETE CASCADE,
  kind text NOT NULL,
  relative_path text NOT NULL,
  mime_type text,
  file_size_bytes bigint,
  duration_seconds numeric,
  width int,
  height int,
  fps numeric,
  bitrate bigint,
  video_codec text,
  audio_codec text,
  status text NOT NULL DEFAULT 'ready' CHECK (status IN ('processing', 'ready', 'failed')),
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (media_asset_id, kind)
);

CREATE INDEX IF NOT EXISTS idx_media_renditions_asset
  ON media_renditions(media_asset_id);

CREATE TABLE IF NOT EXISTS media_video_fingerprints (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  media_asset_id uuid NOT NULL REFERENCES media_assets(id) ON DELETE CASCADE,
  algorithm text NOT NULL,
  algorithm_version text,
  relative_path text,
  status text NOT NULL DEFAULT 'ready' CHECK (status IN ('ready', 'skipped', 'failed')),
  signature_hash text,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (media_asset_id, algorithm)
);

CREATE INDEX IF NOT EXISTS idx_media_video_fingerprints_algorithm
  ON media_video_fingerprints(algorithm, status);

CREATE TABLE IF NOT EXISTS media_duplicate_candidates (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  media_asset_id uuid NOT NULL REFERENCES media_assets(id) ON DELETE CASCADE,
  candidate_asset_id uuid REFERENCES media_assets(id) ON DELETE SET NULL,
  duplicate_type text NOT NULL CHECK (duplicate_type IN ('exact', 'suspected')),
  score numeric,
  algorithm text NOT NULL,
  status text NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'kept', 'reused', 'ignored')),
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  decided_by uuid REFERENCES app_users(id) ON DELETE SET NULL,
  decided_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (media_asset_id, candidate_asset_id, duplicate_type, algorithm)
);

CREATE INDEX IF NOT EXISTS idx_media_duplicate_candidates_asset
  ON media_duplicate_candidates(media_asset_id, status);
