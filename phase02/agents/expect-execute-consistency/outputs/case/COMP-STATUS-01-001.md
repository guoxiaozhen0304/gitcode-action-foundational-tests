# COMP-STATUS-01-001
- **标题**: 运行状态机 queued 到 completed 转换正确
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
run_status 原 STATUS_GUARANTEED（裸 echo "running"）。步骤改为真实探针：校验 atomgit.run_number 非空（为空 exit 1），输出 STATUS_PROBE_OK。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status_sequence | positive | equals queued_in_progress_completed | ✅ COVERED | harness 轮询状态序列 |
| 2 | run_status | positive | equals success | ✅ GENUINE | 探针校验有真实失败路径 |
