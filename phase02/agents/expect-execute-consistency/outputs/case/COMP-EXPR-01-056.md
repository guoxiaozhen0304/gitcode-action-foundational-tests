# COMP-EXPR-01-056

- **标题**: toJson 函数边界行为
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `toJson` 将对象序列化为合法 JSON 字符串，支持嵌套对象。

## 做了什么
step 使用 `${{ toJson(atomgit.event) }}` 序列化事件对象（期望以 `{` 开头）；用 `${{ toJson(env) }}` 序列化 env 上下文（env 中包含 TEST_KEY）；用 `${{ toJson(atomgit) }}` 序列化完整上下文（期望包含嵌套键 `"event"`）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: EVENT_JSON={ | COVERED | `toJson(atomgit.event)` 输出 JSON，以 `{` 开头 |
| 2 | run_logs | positive | must_contain: ENV_JSON={ | COVERED | `toJson(env)` 输出 JSON，以 `{` 开头 |
| 3 | run_logs | positive | must_contain: TEST_KEY | COVERED | env 中注入的 TEST_KEY=test_value 出现在 JSON 输出中 |
| 4 | run_logs | positive | must_contain: "event": | COVERED | `toJson(atomgit)` 中嵌套 `event` 键被正确序列化 |
