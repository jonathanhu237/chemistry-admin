CREATE TABLE IF NOT EXISTS experiment_question_workbench_sessions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  mode text NOT NULL CHECK (mode IN ('repair', 'create')),
  experiment_id text NOT NULL REFERENCES formal_experiments(id) ON DELETE CASCADE,
  point_key text,
  question_id uuid REFERENCES experiment_questions(id) ON DELETE SET NULL,
  original_question_snapshot jsonb NOT NULL DEFAULT '{}'::jsonb,
  context_snapshot jsonb NOT NULL DEFAULT '{}'::jsonb,
  status text NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'closed', 'discarded')),
  created_by uuid REFERENCES app_users(id) ON DELETE SET NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS experiment_question_workbench_turns (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id uuid NOT NULL REFERENCES experiment_question_workbench_sessions(id) ON DELETE CASCADE,
  role text NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
  content text NOT NULL DEFAULT '',
  provider text,
  model text,
  error_state jsonb,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS experiment_question_workbench_candidates (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id uuid NOT NULL REFERENCES experiment_question_workbench_sessions(id) ON DELETE CASCADE,
  turn_id uuid REFERENCES experiment_question_workbench_turns(id) ON DELETE SET NULL,
  draft_id uuid REFERENCES experiment_question_drafts(id) ON DELETE SET NULL,
  payload jsonb NOT NULL DEFAULT '{}'::jsonb,
  validation_errors jsonb NOT NULL DEFAULT '[]'::jsonb,
  status text NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'rejected', 'published')),
  lineage jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_question_workbench_sessions_experiment ON experiment_question_workbench_sessions(experiment_id, status);
CREATE INDEX IF NOT EXISTS idx_question_workbench_sessions_question ON experiment_question_workbench_sessions(question_id, status);
CREATE INDEX IF NOT EXISTS idx_question_workbench_turns_session ON experiment_question_workbench_turns(session_id, created_at);
CREATE INDEX IF NOT EXISTS idx_question_workbench_candidates_session ON experiment_question_workbench_candidates(session_id, created_at);
CREATE INDEX IF NOT EXISTS idx_question_workbench_candidates_draft ON experiment_question_workbench_candidates(draft_id);
