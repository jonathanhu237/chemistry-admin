CREATE EXTENSION IF NOT EXISTS vector;

ALTER TABLE chunk_embeddings
  ALTER COLUMN embedding TYPE vector(1024)
  USING embedding::vector(1024);

CREATE INDEX IF NOT EXISTS idx_source_chunks_content_status
  ON source_chunks(content_status);

CREATE INDEX IF NOT EXISTS idx_source_chunks_metadata_gin
  ON source_chunks USING gin(metadata);

CREATE INDEX IF NOT EXISTS idx_source_chunks_source_collection
  ON source_chunks((metadata->>'source_collection'));

CREATE INDEX IF NOT EXISTS idx_source_chunks_content_type
  ON source_chunks((metadata->>'content_type'));

CREATE INDEX IF NOT EXISTS idx_chunk_embeddings_cosine
  ON chunk_embeddings USING hnsw (embedding vector_cosine_ops);
