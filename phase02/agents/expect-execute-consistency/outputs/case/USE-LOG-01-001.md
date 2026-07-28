# USE-LOG-01-001
- **标题**: 多 step 日志按时间线组织且边界清晰
- **维度**: 易用性
- **评级**: 部分不符

## 想测什么
验证含多个 step 的 workflow 日志面板中 step 按定义顺序排列、step 名称可见、长输出可折叠。

## 做了什么
workflow 含 5 个 step（prepare/build/test/package/summary），每个 step echo 输出一条标记信息。断言日志含 "step one prepare" 字符串。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | 日志含 "step one prepare" | COVERED | step name 在平台日志中展示 → GENUINE |
| 2 | ui_layout | nonfunctional | 用户在 3 秒内定位到失败 step | UNVERIFIABLE | eval: llm_assisted，UI 视觉判定需人工主观评判 → LLM_DEPENDENT |
