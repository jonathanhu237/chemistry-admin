CREATE TABLE IF NOT EXISTS textbook_rag_evidence_cache (
  cache_key text PRIMARY KEY,
  point_node_id text NOT NULL REFERENCES experiment_catalog_nodes(id) ON DELETE CASCADE,
  canonical_point_id text REFERENCES experiment_catalog_points(id) ON DELETE SET NULL,
  content_fingerprint text NOT NULL,
  config_fingerprint text NOT NULL,
  package jsonb NOT NULL,
  diagnostics jsonb NOT NULL DEFAULT '{}'::jsonb,
  source_count int NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  CHECK (cache_key = btrim(cache_key)),
  CHECK (length(btrim(cache_key)) > 0),
  CHECK (content_fingerprint = btrim(content_fingerprint)),
  CHECK (config_fingerprint = btrim(config_fingerprint)),
  CHECK (source_count >= 0)
);

CREATE INDEX IF NOT EXISTS idx_textbook_rag_evidence_cache_point
  ON textbook_rag_evidence_cache(point_node_id, updated_at DESC);

CREATE INDEX IF NOT EXISTS idx_textbook_rag_evidence_cache_canonical
  ON textbook_rag_evidence_cache(canonical_point_id, updated_at DESC)
  WHERE canonical_point_id IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_textbook_rag_evidence_cache_config
  ON textbook_rag_evidence_cache(config_fingerprint, updated_at DESC);
