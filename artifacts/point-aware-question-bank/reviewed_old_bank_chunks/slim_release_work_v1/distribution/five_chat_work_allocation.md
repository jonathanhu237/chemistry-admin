# Five-Chat Work Allocation

Use one chat per chunk. Each chat processes its packets sequentially and writes rebuilt packages only. Do not edit release JSON directly.

## Shared Inputs

- OpenSpec change: `E:\chemistry-exam\openspec\changes\full-question-bank-semantic-release-repair`
- Execution spec: `E:\chemistry-exam\openspec\changes\full-question-bank-semantic-release-repair\small_packet_reconstruction_spec.md`
- Packet root: `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\semantic_work_packets`
- RAG source root: `E:\chemistry-rag\data\rag_ready`
- Ideal sample:
  - `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\ideal_packages\chunk_2_19-3-03_ideal_package_v1.json`
  - `E:\chemistry-admin\artifacts\point-aware-question-bank\reviewed_old_bank_chunks\slim_release_work_v1\ideal_packages\chunk_2_19-3-03_ideal_package_preview.md`

## Chat 1

Chunk: `chunk_1`

Packets:

- `19-1-01`
- `19-1-02`
- `19-1-03`
- `19-1-04`
- `19-1-05`
- `19-1-06`
- `19-1-07`
- `19-1-08`
- `19-2-01`
- `19-2-02`
- `19-2-03`
- `19-2-04`
- `19-2-05`
- `19-3-01`
- `19-3-02`

## Chat 2

Chunk: `chunk_2`

Packets:

- `19-3-03`
- `19-3-04`
- `19-3-05`
- `19-3-06`
- `19-4-01`
- `19-4-02`
- `19-4-03`
- `19-4-04`
- `19-4-05`
- `19-4-06`
- `19-4-07`
- `19-4-08`
- `19-4-09`
- `19-5-01`
- `19-6-01`

## Chat 3

Chunk: `chunk_3`

Packets:

- `19-6-02`
- `19-6-03`
- `19-6-04`
- `19-8-01`
- `19-8-02`
- `19-8-03`
- `19-8-04`
- `19-8-05`
- `19-8-06`
- `19-8-07`
- `19-8-08`
- `19-8-09`
- `19-8-10`
- `19-8-11`
- `20-1-01`

## Chat 4

Chunk: `chunk_4`

Packets:

- `20-1-02`
- `20-1-03`
- `20-1-04`
- `20-1-05`
- `20-1-06`
- `20-1-07`
- `20-1-08`
- `20-1-09`
- `20-2-01`
- `20-2-02`
- `20-2-03`
- `20-2-04`
- `20-2-05`
- `20-2-06`
- `20-2-07`

## Chat 5

Chunk: `chunk_5`

Packets:

- `20-2-08`
- `20-2-09`
- `20-2-10`
- `20-3-01`
- `20-3-02`
- `20-3-03`
- `20-3-04`
- `20-3-05`
- `20-3-06`
- `20-3-07`
- `20-3-08`
- `20-3-09`
- `20-3-10`
- `20-3-11`
- `20-3-12`
- `20-3-13`
- `20-3-14`

## Completion Rule

A chat is complete only when every assigned packet has both:

- `rebuilt_packages/chunk_X/<experiment_code>_rebuilt_v1.json`
- `rebuilt_reports/chunk_X/<experiment_code>_rebuild_report.md`

Final merge is a separate task after all five chats finish.
