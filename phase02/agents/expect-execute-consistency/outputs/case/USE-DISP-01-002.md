# USE-DISP-01-002
- **标题**: workflow_dispatch 未提供参数但存在 default 时应使用默认值运行
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
workflow_dispatch 有 default 值的 input，未提供时使用默认值。

## 做了什么
workflow 定义 `environment` input（default: staging），step 中 `echo "env=${{ inputs.environment }}"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: env=staging | COVERED | `${{ inputs.environment }}` 真实表达式引用 input，验证默认值生效 |

