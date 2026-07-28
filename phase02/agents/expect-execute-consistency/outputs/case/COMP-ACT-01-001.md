# COMP-ACT-01-001
- **标题**: action inputs.required 未传参时平台不自动校验
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
验证平台不因 action.yml 声明 required: true 但调用方未传参而在调度层失败；action 内读取对应环境变量为空值。

## 做了什么
1. 步骤 `Call without required input`：`uses: ./.gitcode/actions/req-check`（调用本地 action，不传 with）
2. action 执行时对应 INPUT_ 变量为空，action 内输出 REQ_INPUT_EMPTY

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | workflow 无失败点，但 `uses:` 调用真实 action，action 可能因缺少输入失败，status 断言有意义 |
| 2 | run_logs | positive | must_contain: REQ_INPUT_EMPTY | COVERED | action 内部在检测到输入为空时输出此标记，由真实 action 代码产生 |
