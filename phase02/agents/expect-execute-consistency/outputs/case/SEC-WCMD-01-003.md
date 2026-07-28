# SEC-WCMD-01-003
- **标题**: ATOMGIT_ENV 不被不可信输入污染提权
- **维度**: security
- **评级**: 断言一致

## 想测什么
含换行/协议控制字符的不可信值写入 ATOMGIT_ENV 时不应注入额外环境变量。

## 做了什么
step1 将多行恶意值写入 `$ATOMGIT_ENV`，step2 检查 `$INJECTED_VAR` 是否被设置，分别 echo "injection succeeded" 或 "no injection"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain:injection succeeded | COVERED | step 仅在注入成功时输出该字符串，为有效负向验证 |
| 2 | run_logs | positive | equals:no injection | COVERED | step 在注入防御成功时显式 echo "no injection" |
