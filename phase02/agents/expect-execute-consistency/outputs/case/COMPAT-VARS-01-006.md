# COMPAT-VARS-01-006
- **标题**: vars 在 Action 中的可用性差异
- **维度**: 兼容性
- **评级**: 部分不符

## 想测什么
验证 `${{ vars.ACTION_VAR }}` 在Action的with参数中正确求值。

## 做了什么
setup配置 `variables: {ACTION_VAR: action_value}`；step使用 `uses: checkout` with `ref: ${{ vars.ACTION_VAR }}`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive llm | "若支持vars，Action的with参数应正确接收值" | COVERED | ${{ vars.ACTION_VAR }}在with中引用(GENUINE R1上下文表达式)；run_status反映checkout是否成功 |
| 2 | run_logs | negative llm | "vars不应被静默视为空字符串" | COVERED | 若vars被静默为空，checkout with ref为空可能导致checkout默认分支而非报错——需LLM辅助判断(R5) |

**部分不符原因**: 断言#2 target为run_logs，但checkout action的输出不直接在run_logs中——若vars为空，checkout静默回退到默认分支，run_logs不会明确报错。此断言更适合target=run_status或需在step后追加`git rev-parse HEAD`验证实际检出SHA。断言与目标错位。
