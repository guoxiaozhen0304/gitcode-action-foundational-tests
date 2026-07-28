# COMP-RUNNER-01-080

- **标题**: runner 上下文属性可访问性验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 runner.name / temp / tool_cache / os / arch 等上下文属性可正常访问。

## 做了什么
步骤使用 `${{ runner.name }}`、`${{ runner.temp }}`、`${{ runner.tool_cache }}` 等表达式输出 runner 上下文属性值。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain NAME= | COVERED | step 含 `${{ runner.name }}` 表达式，平台上下文求值即功能执行（Rule 6） |
| 2 | run_logs | positive | must_contain TEMP= | COVERED | step 含 `${{ runner.temp }}` 表达式 |
| 3 | run_logs | positive | must_contain TOOL_CACHE= | COVERED | step 含 `${{ runner.tool_cache }}` 表达式 |
| 4 | run_logs | positive | must_contain runner_ok | COVERED | marker signal: step has run through all runner expressions |
