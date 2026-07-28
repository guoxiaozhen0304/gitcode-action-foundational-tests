# USE-API-01-001
- **标题**: API 字段值与事件类型命名同一概念分裂的对照检查
- **维度**: usability
- **评级**: 断言一致

## 想测什么
同一概念在事件类型与 API 字段值上命名应一致或文档有对照表。

## 做了什么
workflow: null。纯 API/documentation 验证用例，断言指向 api_response 和 documentation。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | api_response | negative | eval:deterministic | COVERED | API 响应与文档对照检查，无需 workflow 步骤；harness 外部完成 |
