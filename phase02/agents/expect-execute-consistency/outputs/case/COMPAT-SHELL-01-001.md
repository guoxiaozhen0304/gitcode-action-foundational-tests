# COMPAT-SHELL-01-001
- **标题**: 默认 shell 隐式行为差异 - 未显式声明时是否为 bash
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 在未显式声明 shell 时默认使用 bash 执行命令。
## 做了什么
在不声明 shell 字段的 step 中输出当前进程使用的 shell 名称，手动触发后检查日志。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | contains=bash | COVERED | 日志包含 bash 可通过字符串匹配直接验证 |
