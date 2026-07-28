# SEC-WCMD-01-003
- **标题**: ATOMGIT_ENV 不被不可信输入污染提权
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
含换行/协议控制字符的不可信值写入 ATOMGIT_ENV 时，不应注入计划外的环境变量。

## 做了什么
workflow step 写多行内容到 `$ATOMGIT_ENV`，后续 step 检查 INJECTED_VAR 是否被注入。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain: injection succeeded | COVERED | step 通过 `if [ -n "$INJECTED_VAR" ]` 检查注入，`exit 1` 真实命令，验证无注入 |
| 2 | run_logs | positive | no injection | COVERED | 真实条件分支产出 `echo "no injection"`，验证防护生效 |

