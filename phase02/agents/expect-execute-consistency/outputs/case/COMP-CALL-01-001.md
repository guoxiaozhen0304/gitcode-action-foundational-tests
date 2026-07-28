# COMP-CALL-01-001
- **标题**: 2 层 workflow_call 嵌套正常执行
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 复核：前一轮已修复，本次未改动）

## 修复内容
本次未改动。当前 YAML 已为 job 级 `uses: ./.gitcode/workflows/reusable-sub.yml` 真实嵌套调用（原分析时 workflow 仅含 echo，问题已不存在）；sub_workflow_marker 由被调用的子 workflow（fixture）产出。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | ✅ GENUINE | 真实 workflow_call，子 workflow 失败则 run 失败 |
| 2 | run_logs | positive | must_contain sub_workflow_marker | ✅ GENUINE | 子 workflow 步骤日志（fixture 产出），即规格"子 workflow 日志可见"验证点 |
