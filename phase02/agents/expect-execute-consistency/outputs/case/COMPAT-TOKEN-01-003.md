# COMPAT-TOKEN-01-003
- **标题**: GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证GITHUB_TOKEN环境变量和secrets引用均为空/未定义，不与ATOMGIT_TOKEN混淆映射。

## 做了什么
step1输出 `echo "GITHUB_TOKEN=$GITHUB_TOKEN"` + `echo "ATOMGIT_TOKEN=$ATOMGIT_TOKEN"` + `echo "done"`；step2输出 `echo "secret_github_token=${{ secrets.GITHUB_TOKEN }}"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative llm | "GITHUB_TOKEN不应等于ATOMGIT_TOKEN" | COVERED | $GITHUB_TOKEN和$ATOMGIT_TOKEN为环境变量(GENUINE R1真实cmd来源)；两值在同一日志可直接对比 |
| 2 | run_logs | positive llm | "GITHUB_TOKEN为空或未定义" | COVERED | echo $GITHUB_TOKEN和${{ secrets.GITHUB_TOKEN }}为GENUINE(R1)；空值在日志中表现为空输出 |
| 3 | run_logs | negative llm | "secrets.GITHUB_TOKEN不应被静默映射为有值" | COVERED | ${{ secrets.GITHUB_TOKEN }}为GENUINE(R1)；与#1/#2联合比对可证未映射 |
