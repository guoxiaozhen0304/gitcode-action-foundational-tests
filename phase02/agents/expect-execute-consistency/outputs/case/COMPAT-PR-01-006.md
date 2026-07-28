# COMPAT-PR-01-006
- **标题**: PR 目标分支过滤行为差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 GitCode 对 `pull_request.branches: [main]` 的目标分支过滤——目标main触发、目标develop不触发。

## 做了什么
workflow 配置 `pull_request.branches: [main]`，step输出 `echo "event_name=${{ atomgit.event_name }}"` + `echo "done"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | "目标分支main的PR应触发workflow" | COVERED | run_status可观测；${{ atomgit.event_name }}为GENUINE(R1)上下文证据 |
| 2 | run_status | negative | "目标分支不为main的PR不应触发" | COVERED | 不触发时run_list中无对应条目即证明；负向验证通过run_list缺失判定 |
