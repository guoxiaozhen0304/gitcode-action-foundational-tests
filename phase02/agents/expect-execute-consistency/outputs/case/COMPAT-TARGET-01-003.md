# COMPAT-TARGET-01-003
- **标题**: pull_request_target 默认 types 与 GitHub 差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证pull_request_target不声明types时的默认触发行为——open和synchronize应触发。

## 做了什么
workflow配置 `on: pull_request_target`（不声明types），step输出 `echo "event_name=${{ atomgit.event_name }}"` + `echo "done"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive llm | "默认types下PR open应触发workflow" | COVERED | ${{ atomgit.event_name }}为GENUINE(R1)；触发行为通过run_list可观测 |
| 2 | run_status | positive llm | "默认types下PR synchronize应触发workflow" | COVERED | 同#1；两种触发事件各自通过run_list验证 |
