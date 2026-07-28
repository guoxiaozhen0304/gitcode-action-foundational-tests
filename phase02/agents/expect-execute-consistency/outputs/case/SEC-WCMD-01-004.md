# SEC-WCMD-01-004
- **标题**: ATOMGIT_OUTPUT 不被不可信输入污染提权
- **维度**: security
- **评级**: 断言一致

## 想测什么
含换行/协议控制字符的不可信值写入 ATOMGIT_OUTPUT 时不应注入额外 output 条目。

## 做了什么
step1 将多行恶意值写入 `$ATOMGIT_OUTPUT`，step2 检查 `steps.bad.outputs.hijacked` 是否被设置，分别 echo "hijack succeeded" 或 "no hijack"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain:hijack succeeded | COVERED | step 仅在劫持成功时输出该字符串，为有效负向验证 |
| 2 | run_logs | positive | equals:no hijack | COVERED | step 在防御成功时显式 echo "no hijack" |
