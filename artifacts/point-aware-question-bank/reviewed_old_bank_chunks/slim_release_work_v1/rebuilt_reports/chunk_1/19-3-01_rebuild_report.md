# 19-3-01 rebuild report

## Packet

- chunk: chunk_1
- packet: 19-3-01
- rebuilt JSON: `rebuilt_packages/chunk_1/19-3-01_rebuilt_v1.json`
- source packet: `semantic_work_packets/chunk_1/19-3-01.json`
- release JSON was not modified.

## Counts

- total questions: 30
- single_choice: 19
- true_false: 8
- fill_blank: 3
- keep: 21
- rewrite: 9
- reject: 0

## RAG Evidence IDs

- `expchunk_00228_5e99fe31b9`: 二氧化硫制备实验，蒸馏瓶中亚硫酸钠、分液漏斗中浓硫酸、缓慢滴加、点燃酒精灯。
- `expchunk_00224_166bfb5a4a`: 二氧化硫安全要点，减少有毒气体逸出并在通风橱中操作。
- `textbook_prose_00348_84bcfd0185`: 实验室用亚硫酸盐和非氧化性酸制取二氧化硫。
- `textbook_prose_00339_d6cda7bf18`: 二氧化硫有刺激性气味。
- `expchunk_00036_cce608cf7d`: 有毒气体相关操作应在通风橱中进行。

## Rewrite List

- Q003: 重写为“通过分液漏斗缓慢滴加浓硫酸”的发生控制题，去掉只背仪器名的浅层表述。
- Q007: 重写为选择浓硫酸的理由，限定在“强酸性、非氧化性且可控滴加”的证据边界内。
- Q014: 重写为先控滴加再加热的顺序判断，强调速率控制。
- Q015: 重写为尾气和逸散风险识别题，和通风橱证据绑定。
- Q019: 重写为气体性质与安全措施的关系题，避免单纯记“有毒”。
- Q025: 重写为填空题，答案固定为“分液漏斗”，降低多答案风险。
- Q026: 重写为完整装置链路题，覆盖蒸馏瓶、分液漏斗、加热和通风橱。
- Q028: 重写为操作异常识别题，错误项集中在快速加入和开放环境。
- Q030: 重写为综合判断题，要求同时识别制气条件与安全边界。

## Keep But Edge

- Q001, Q002, Q005, Q009, Q021, Q022, Q023: 保留为基础事实锚点，直接对应亚硫酸钠、浓硫酸和二氧化硫制备。
- Q004, Q006, Q010, Q013, Q017, Q024, Q029: 保留为安全锚点，依据通风橱、毒性和减少逸出证据。
- Q008, Q011, Q012, Q016, Q018, Q020, Q027: 保留为仪器或顺序识别题，但解释中补足“控速/发生装置/加热”理由。
- 边缘风险：若题目只问“装置名称”或“气体名称”，信息量偏低；本轮保留是因为它们与后续链路题共同形成基础层级。

## Evidence Insufficient

- none. 本 packet 发布题均有 RAG 证据支撑。

## Multipoint Questions

- Q010, Q026, Q030 同时涉及制备链路和安全边界，属于多点综合题。
- 其余题主要围绕一个点位，避免把“制备操作”和“性质检验”混在同一题中。

## Fill Blank Risk

- Q022 accepted answer: 浓硫酸。风险低，唯一对应分液漏斗中试剂。
- Q024 accepted answer: 通风橱。风险低，安全场所表述明确。
- Q027 accepted answer: 分液漏斗。风险低，仪器名称唯一。

## Manual Reconstruction Statement

本 packet 已逐题人工阅读原题、选项、答案、解析、point keys、video_points 和 RAG 证据后重建；rebuilt JSON 与本报告不是脚本生成结果。脚本/命令仅用于只读检查、计数、RAG id 查找和 JSON 结构校验。
