# USE-DOC-01-005
- **标题**: configure-steps 的 shell 类型与命令语言不匹配示例照抄失败
- **维度**: usability
- **评级**: 断言一致

## 想测什么
照抄文档 shell/bash 配 PowerShell、shell/python 配 shell 命令示例应失败，实证示例不可复刻。

## 做了什么
两个 job：bash shell 执行 `Write-Host "hello"`（PowerShell 语法），python shell 执行 `echo "hello"`（shell 语法）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals:"failure" | COVERED | 平台 run_status，shell 与命令语言不匹配应导致 failure |
| 2 | documentation | negative | eval:deterministic | COVERED | 文档示例缺陷检查 |
