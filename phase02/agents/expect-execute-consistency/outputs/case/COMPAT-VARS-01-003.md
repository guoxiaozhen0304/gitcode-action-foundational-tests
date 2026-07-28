# COMPAT-VARS-01-003
- **标题**: vars 项目级覆盖组织级的优先级差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证vars项目级值覆盖组织级值——ORG_VAR应返回proj_value而非org_value。

## 做了什么
setup配置 `variables: {ORG_VAR: proj_value}`，step输出 `echo "org_var=${{ vars.ORG_VAR }}"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive llm | "ORG_VAR应返回项目级值proj_value" | COVERED | ${{ vars.ORG_VAR }}为GENUINE(R1上下文表达式) |
| 2 | run_logs | negative llm | "不应返回组织级值" | COVERED | 同#1，若返回org_value则与编排的proj_value冲突 |
