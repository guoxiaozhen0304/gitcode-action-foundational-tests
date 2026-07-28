# REL-CHILDSTATE-01-064
- **标题**: 子任务状态传播——workflow_call 失败时父 workflow 不应假阳性完成
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
子 workflow（child_fail.yml）失败时父 workflow=failure，下游 job skip。

## 做了什么
父 workflow 通过 uses: 调用 child_fail.yml（必然 exit 1 失败）；下游 job needs call_child。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | parent_status | positive | equals "failure" | COVERED | 子 workflow 失败导致调用 job 失败，父状态应为 failure |
| 2 | downstream_status | positive | equals "skipped" | COVERED | needs 依赖的 job 失败时下游被 skip，平台行为可观测 |
| 3 | parent_status | negative | equals "success" | COVERED | 子失败时父不应 success |
