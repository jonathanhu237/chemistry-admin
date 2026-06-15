# Ideal Package Preview: chunk_2 / 19-3-03

Demo only. This package has not been merged into the release JSON.

## Summary

- Experiment: `19-3-03 SO₃²⁻ 的检出`
- Questions: `30`
- Types: `20` single choice, `6` true/false, `4` fill blank
- Supporting-theory dependent questions: `6`
- Multi-point questions: `11`
- Mobile-risk fill blanks: low risk only; no formula/name fill blanks
- Evidence mode: every question points to RAG chunk ids; inherited ids were not treated as proof

## Quality Intent

This ideal package removes the duplicate-heavy pattern from the old packet. It covers:

- SO₄²⁻ interference and pre-removal
- Required separation/verification output
- SO₂ preparation and safety
- SO₂ reducing, oxidizing, and bleaching operations
- Theory-backed explanations only where needed
- Point binding as a real semantic decision

## Representative Questions

### Q001

Stem: 在《19-3-03 SO₃²⁻ 的检出》中，检出 SO₃²⁻ 前为什么要预先除去 SO₄²⁻？

Options:

- A. SO₄²⁻ 会干扰 SO₃²⁻ 的检出
- B. SO₄²⁻ 是本实验的目标检出离子
- C. SO₄²⁻ 能使品红溶液褪色
- D. SO₄²⁻ 必须在通风橱内制备

Answer: A

Point: `candidate-1-26a8e36e`

Evidence: `expchunk_00228_5e99fe31b9`

### Q004

Stem: 教材在 SO₃²⁻ 检出任务中要求学生最终写出哪一组内容？

Answer: 分离过程示意图及有关反应的化学方程式

Points: `candidate-1-26a8e36e`, `candidate-2-795f5a0b`

Evidence: `expchunk_00228_5e99fe31b9`

### Q010

Stem: 按教材的 SO₂ 实验室制备操作，蒸馏瓶和分液漏斗中分别放入什么？

Answer: 蒸馏瓶中放 Na₂SO₃ 固体，分液漏斗中装浓硫酸

Point: `candidate-2-795f5a0b`

Evidence: `expchunk_00228_5e99fe31b9`

### Q014

Stem: 若进一步解释 SO₂ 使酸性 KMnO₄ 溶液褪色，最合适的证据组合是哪一项？

Answer: KMnO₄ 水溶液呈紫红色，酸性介质中 MnO₄⁻ 可氧化 SO₃²⁻ 为 SO₄²⁻

Point: `candidate-2-795f5a0b`

Evidence:

- Experiment: `expchunk_00228_5e99fe31b9`
- Theory: `textbook_prose_01251_89ce24842f`, `textbook_prose_01253_29e4ee4b73`

### Q021

Stem: 若要解释 SO₂ 为什么可用于品红褪色类观察，最贴合的 supporting theory 是哪一项？

Answer: SO₂ 分子能与一些有机色素分子结合形成无色有机物

Point: `candidate-2-795f5a0b`

Evidence:

- Experiment: `expchunk_00228_5e99fe31b9`
- Theory: `textbook_prose_00344_07bf4af806`

### Q027

Stem: 教材要求写出分离过程____及有关反应的化学方程式。

Answer: 示意图

Points: `candidate-1-26a8e36e`, `candidate-2-795f5a0b`

Why fill blank is acceptable: answer is a short ordinary Chinese word, not a formula.

## Validation

- JSON parse: pass
- Question ids: unique
- Single-choice option count: pass
- Single-choice option_links count: pass
- Evidence ids found in RAG JSONL: pass
- Visible ASCII digit formula hits: `0`
- Formula-like fill-blank answers: `0`
