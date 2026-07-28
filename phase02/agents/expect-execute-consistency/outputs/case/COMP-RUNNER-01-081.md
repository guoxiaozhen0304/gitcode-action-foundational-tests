# COMP-RUNNER-01-081

- **标题**: 四段式 runs-on（codearts-hosted 首段）调度行为裁定
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证四段式 runs-on 标签（codearts-hosted 首段）的调度行为。

## 做了什么
runs-on: ['codearts-hosted', 'ubuntu-latest', 'x64', 'large']，step 使用 `${{ runner.name }}` 输出 Runner 身份。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain RUNNER_NAME= | COVERED | step 含 `${{ runner.name }}` 表达式（Rule 6） |
| 2 | runner_identity | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | 需人工逐字记录实际 Runner 身份 |
| 3 | runner_mismatch | negative | eval=llm_assisted | LLM_DEPENDENT | 需人工判断调度是否与标签不符 |
