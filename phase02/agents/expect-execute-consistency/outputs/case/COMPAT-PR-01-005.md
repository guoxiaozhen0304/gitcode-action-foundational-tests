# COMPAT-PR-01-005
- **标题**: PR paths 过滤不工作时的兼容性差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 GitCode 对 `pull_request.paths: ['api/**']` 的路径过滤行为——修改匹配路径的PR是否触发workflow。

## 做了什么
workflow 配置 `pull_request.paths: ['api/**']`，step输出 `echo "event_name=${{ atomgit.event_name }}"` + `echo "done"`。workflow自身即为paths过滤被测对象。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | "PR修改api/路径后不应无workflow触发" | COVERED | step输出${{ atomgit.event_name }}为GENUINE(R1)；断言为LLM_DEPENDENT(R5)，但run_status可通过平台run_list观测 |
| 2 | run_status | positive | "若平台已修复匹配路径PR应触发workflow" | COVERED | run_status平台可观测；触发行为直接反映在run_list中 |
