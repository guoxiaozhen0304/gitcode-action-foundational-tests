# USE-DOC-01-005
- **标题**: configure-steps 的 shell 类型与命令语言不匹配示例照抄失败
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
照抄文档示例（shell bash 配 PowerShell 命令、shell python 配 shell 命令）应失败，实证示例不可复刻。

## 做了什么
workflow 中配置 `shell: bash` 执行 `Write-Host "hello"` (PowerShell)，`shell: python` 执行 `echo "hello"` (shell)。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | failure | COVERED | 真实命令执行，shell 与语言不匹配应导致失败 |
| 2 | documentation | negative | 示例 shell 类型与命令语言不匹配即不合格 | COVERED | 文档扫描确定性判定 |

