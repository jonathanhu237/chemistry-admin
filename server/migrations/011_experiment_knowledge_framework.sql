CREATE TABLE IF NOT EXISTS experiment_framework_nodes (
  id text PRIMARY KEY,
  parent_id text REFERENCES experiment_framework_nodes(id) ON DELETE CASCADE,
  source_collection text NOT NULL,
  doc_id text NOT NULL,
  book_title text NOT NULL,
  node_key text NOT NULL,
  node_type text NOT NULL CHECK (node_type IN ('book', 'chapter', 'section', 'protocol')),
  title text NOT NULL,
  full_path text[] NOT NULL DEFAULT '{}',
  depth int NOT NULL DEFAULT 0,
  display_order int NOT NULL DEFAULT 0,
  page_start int,
  page_end int,
  content_status text NOT NULL DEFAULT 'published' CHECK (content_status IN ('draft', 'published', 'archived')),
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (source_collection, doc_id, node_key)
);

CREATE TABLE IF NOT EXISTS experiment_framework_chunk_links (
  node_id text NOT NULL REFERENCES experiment_framework_nodes(id) ON DELETE CASCADE,
  chunk_id text NOT NULL REFERENCES source_chunks(id) ON DELETE CASCADE,
  relation_type text NOT NULL DEFAULT 'primary_evidence',
  sort_order int NOT NULL DEFAULT 0,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (node_id, chunk_id, relation_type)
);

CREATE TABLE IF NOT EXISTS experiment_framework_formal_links (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  node_id text NOT NULL REFERENCES experiment_framework_nodes(id) ON DELETE CASCADE,
  experiment_id text NOT NULL REFERENCES formal_experiments(id) ON DELETE CASCADE,
  relation_type text NOT NULL CHECK (relation_type IN ('formal_parent_title', 'canonical_evidence')),
  link_source text,
  evidence_chunk_id text REFERENCES source_chunks(id) ON DELETE SET NULL,
  confidence numeric NOT NULL DEFAULT 1,
  sort_order int NOT NULL DEFAULT 0,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_experiment_framework_formal_links_unique_parent
  ON experiment_framework_formal_links(node_id, experiment_id, relation_type)
  WHERE evidence_chunk_id IS NULL;

CREATE UNIQUE INDEX IF NOT EXISTS idx_experiment_framework_formal_links_unique_evidence
  ON experiment_framework_formal_links(node_id, experiment_id, relation_type, evidence_chunk_id)
  WHERE evidence_chunk_id IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_experiment_framework_nodes_parent
  ON experiment_framework_nodes(parent_id, display_order);

CREATE INDEX IF NOT EXISTS idx_experiment_framework_nodes_source
  ON experiment_framework_nodes(source_collection, doc_id, node_type);

CREATE INDEX IF NOT EXISTS idx_experiment_framework_nodes_path
  ON experiment_framework_nodes USING gin(full_path);

CREATE INDEX IF NOT EXISTS idx_experiment_framework_chunk_links_chunk
  ON experiment_framework_chunk_links(chunk_id);

CREATE INDEX IF NOT EXISTS idx_experiment_framework_formal_links_experiment
  ON experiment_framework_formal_links(experiment_id);

CREATE INDEX IF NOT EXISTS idx_experiment_framework_formal_links_chunk
  ON experiment_framework_formal_links(evidence_chunk_id);
