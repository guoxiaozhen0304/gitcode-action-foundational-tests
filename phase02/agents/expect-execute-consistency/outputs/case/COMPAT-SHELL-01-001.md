# COMPAT-SHELL-01-001
- **标题**: 默认 shell 隐式行为差异 - 未显式声明时是否为 bash
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证未显式声明shell时默认使用bash——$SHELL和ps输出应包含bash。

## 做了什么
step1使用 `uses: checkout`；step2输出 `echo "Current shell: $SHELL"` + `echo "Shell via ps: $(ps -p $$ -o comm=)"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive contains | "bash" | COVERED | $SHELL和ps -p $$ -o comm=为真实命令(GENUINE R1)，run_logs中直接检查bash字样 |
