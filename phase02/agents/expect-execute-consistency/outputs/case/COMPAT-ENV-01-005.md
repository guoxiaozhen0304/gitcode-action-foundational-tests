# COMPAT-ENV-01-005

- **标题**: RUNNER_* 系列环境变量在 GitCode Runner 上的注入情况探测
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
逐一记录 RUNNER_OS、RUNNER_ARCH、RUNNER_NAME、RUNNER_TEMP、RUNNER_TOOL_CACHE、RUNNER_ENVIRONMENT 在 GitCode Runner 的实际取值。

## 做了什么
分两个 step 依次 echo 六个 RUNNER_* 变量。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: PROBE_DONE | COVERED | run 步骤 echo "PROBE_DONE" |
| 2 | run_logs | positive | llm_assisted | LLM_DEPENDENT | 需人工逐字记录各变量取值 |
| 3 | run_logs | negative | llm_assisted | LLM_DEPENDENT | 需人工判定无不一致的部分注入 |
