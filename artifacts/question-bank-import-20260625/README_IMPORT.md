# 当前题库导入说明

## 文件

- `current_question_bank_seed.json`: 当前题库数据，包含 54 个实验、1965 道题。
- `current_question_bank_seed_export_report.json`: 导出摘要和校验信息。

## 数据摘要

- 实验数：54
- 题目数：1965
- 单选题：785
- 判断题：785
- 填空题：395
- 所有题目均为 `published`
- 所有题目均带点位绑定、canonical point 绑定和 source refs

## 后台导入

如果朋友的后台已经有题库导入入口：

1. 登录老师/管理员后台。
2. 进入题库管理。
3. 选择导入题库。
4. 上传 `current_question_bank_seed.json`。
5. 选择发布导入，或确保导入后题目状态为已发布。

## API 导入

如果没有 UI 导入口，可以用接口导入：

```bash
curl -X POST "http://127.0.0.1:8000/api/admin/question-banks/import" \
  -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  -F "publish=true" \
  -F "file=@current_question_bank_seed.json;type=application/json"
```

把 `http://127.0.0.1:8000` 换成朋友自己的后端地址，把 `YOUR_ADMIN_TOKEN` 换成管理员登录后的 token。

## 注意

- 导入接口会重新生成题目 ID，不要求保留本机数据库里的 `question_id`。
- 导入接口会把题目写入默认题库；学生测评按已发布题目抽题，不依赖原始 `generated` bank kind。
- 朋友那边需要先有相同的实验目录/实验 ID，否则导入会出现找不到实验的问题。
