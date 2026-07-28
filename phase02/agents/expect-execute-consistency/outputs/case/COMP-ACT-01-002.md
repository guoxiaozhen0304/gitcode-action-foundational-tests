# COMP-ACT-01-002
- **标题**: 含连字符 input_id 的 INPUT_ 环境变量命名裁定
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
含连字符的 input_id（如 dry-run）经过平台转换后的实际环境变量名裁定（INPUT_DRY-RUN / INPUT_DRY_RUN / 其他）。

## 做了什么
1. 步骤 `Call with hyphenated input`：`uses: ./.gitcode/actions/hyphen-input`，with `dry-run: "yes"`
2. action 内部枚举并输出所有匹配 INPUT_DRY 的环境变量名与值

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | 真实 action 调用，可能因输入处理失败，status 断言有意义 |
| 2 | run_logs | positive | must_contain: INPUT_DRY | COVERED | action 内部输出包含 INPUT_DRY 前缀的环境变量名 |
| 3 | env_naming | nonfunctional | llm_assisted | LLM_DEPENDENT | eval=llm_assisted，由 LLM 裁定命名规则 |
