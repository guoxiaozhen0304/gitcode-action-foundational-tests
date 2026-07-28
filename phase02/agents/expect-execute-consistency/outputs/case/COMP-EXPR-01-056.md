# COMP-EXPR-01-056
- **标题**: toJson 函数边界行为
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
toJson 将对象序列化为合法 JSON 字符串，嵌套对象可被正确序列化。

## 做了什么
1. step `Serialize event`：`echo "EVENT_JSON=${{ toJson(atomgit.event) }}"`
2. step `Serialize env context`：`echo "ENV_JSON=${{ toJson(env) }}"`
3. step `Serialize atomgit context`：`echo "ATOMGIT_JSON=${{ toJson(atomgit) }}"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: EVENT_JSON={ | COVERED | toJson(atomgit.event) 输出以 { 开头 |
| 2 | run_logs | positive | must_contain: ENV_JSON={ | COVERED | toJson(env) 输出以 { 开头 |
| 3 | run_logs | positive | must_contain: TEST_KEY | COVERED | env 中 TEST_KEY=test_value 出现在 toJson(env) 输出中 |
| 4 | run_logs | positive | must_contain: "event": | COVERED | toJson(atomgit) 包含嵌套 event 键 |
