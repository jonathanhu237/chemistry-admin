CREATE INDEX IF NOT EXISTS idx_media_assets_active_ready_duration
  ON media_assets(duration_seconds)
  WHERE upload_status = 'ready'
    AND COALESCE(lifecycle_status, 'active') = 'active'
    AND duration_seconds IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_media_video_fingerprints_ready_algorithm_asset
  ON media_video_fingerprints(algorithm, media_asset_id)
  WHERE status = 'ready';
