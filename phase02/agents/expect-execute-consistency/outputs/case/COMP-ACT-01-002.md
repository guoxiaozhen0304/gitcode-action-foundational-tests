# COMP-ACT-01-002

- **标题**: 含连字符 input_id 的 INPUT_ 环境变量命名裁定
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证含连字符（如 `dry-run`）的 action input_id 对应的环境变量命名规则（`INPUT_DRY-RUN` / `INPUT_DRY_RUN` / 其他）。

## 做了什么
通过 `uses: ./.gitcode/actions/hyphen-input` 并以 `with: dry-run: "yes"` 传参调用本地 action，action 枚举并输出所有匹配 `INPUT_DRY` 前缀的环境变量。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | action 内部运行真实枚举逻辑，状态校验完整 |
| 2 | run_logs | positive | must_contain: INPUT_DRY | COVERED | action 脚本枚举环境变量，输出包含 INPUT_DRY 前缀的变量名和值 |
| 3 | env_naming | nonfunctional | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言，不参与 TRIVIAL/MISSING 判定 |
