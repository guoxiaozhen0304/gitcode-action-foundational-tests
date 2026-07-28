# SEC-WCMD-01-004
- **标题**: ATOMGIT_OUTPUT 不被不可信输入污染提权
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
含换行/协议控制字符的不可信值写入 ATOMGIT_OUTPUT 时，不应注入计划外的 output 条目。

## 做了什么
workflow step 写多行内容到 `$ATOMGIT_OUTPUT`，后续 step 通过 `${{ steps.bad.outputs.hijacked }}` 检查是否被注入。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain: hijack succeeded | COVERED | `${{ steps.bad.outputs.hijacked }}` 真实表达式读取 output，`exit 1` 真实命令 |
| 2 | run_logs | positive | no hijack | COVERED | 真实条件分支产出 `echo "no hijack"`，验证无劫持 |

