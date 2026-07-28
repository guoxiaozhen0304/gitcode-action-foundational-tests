# COMP-VARREF-01-083
- **标题**: YAML 表达式与 Shell 环境变量引用方式验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么
验证 `${{ env.VAR }}` 与 `$VAR` 引用同一变量时值一致，`${{ atomgit.sha }}` 与 `$ATOMGIT_SHA` 值一致。
## 做了什么
workflow_dispatch 触发，env 设 TEST_VAR=hello，step 中分别以表达式和 shell 变量方式 echo 四个标记。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | must_contain: EXPR=hello | GENUINE→COVERED | `${{ env.TEST_VAR }}` + `$TEST_VAR` 均为真实变量引用，按 R6 GENUINE |
| 2 | run_logs | positive | must_contain: ENV=hello | GENUINE→COVERED | 同上 |
| 3 | run_logs | positive | must_contain: ref_ok | GENUINE→COVERED | 工作流含 ${{ }} 引用和真实 shell 变量，按 R6 echo 标记 GENUINE |
