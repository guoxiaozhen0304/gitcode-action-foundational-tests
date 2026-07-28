# COMP-STAGES-01-002

- **标题**: fail_fast true 时 stage 内任一 job 失败终止同阶段其余 job
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 fail_fast: true 时一个 job 失败导致同 stage 其他 job 被跳过，后续 stage 不执行。

## 做了什么
Stage 1: fail-job 执行 `exit 1`（故意失败），should-skip 含 `echo "should not execute"`。Stage 2: deploy 含 `echo "should not execute"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals skipped_for_should_skip | COVERED | `exit 1` 故意失败触发 fail_fast，harness 观测 should-skip job 被 skip |
| 2 | stage_execution | negative | equals deploy_stage_executed | COVERED | fail_fast 应阻止后续 stage，harness 验证 deploy stage 未执行；type=negative |
