# COMPAT-SHELL-01-002
- **标题**: 默认工作目录隐式行为差异 - 未显式声明时是否为仓库根目录
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 在未显式声明 working-directory 时默认工作目录为仓库根目录。
## 做了什么
在不声明 working-directory 的 step 中输出当前工作目录并列出内容，触发后检查日志。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | contains=README | COVERED | 日志含 README 表明当前目录为仓库根，直接字符串匹配 |
