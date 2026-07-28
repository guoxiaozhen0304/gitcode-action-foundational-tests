# COMPAT-SCHEDULE-01-003
- **标题**: schedule 在非默认分支不触发与 GitHub 差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证schedule workflow仅默认分支触发——非默认分支(develop)上schedule不应触发。

## 做了什么
workflow配置 `schedule cron: '0 2 * * *'`，step输出 `echo "branch=${{ atomgit.ref_name }}"` + `echo "done"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative llm | "非默认分支的schedule不应触发运行" | COVERED | run_status+run_list可观测；${{ atomgit.ref_name }}为GENUINE(R1)，输出分支名提供证据 |
| 2 | run_status | positive llm | "默认分支的schedule正常触发" | COVERED | run_status平台可观测；与#1互补 |
