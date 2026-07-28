# USE-TOGGLE-01-001
- **标题**: 隐藏安全开关 ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS 默认值与文档缺失
- **维度**: 易用性/安全性
- **评级**: 断言一致

## 想测什么
探测 ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS 的实际注入值（或 UNSET），检查文档 workflow-commands.md 与 using-script-commands.md 是否列出该开关及其默认值与安全影响。

## 做了什么
workflow 读取该环境变量并 echo 输出（默认值或 UNSET）。文档侧检查是否列出该开关。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | 记录开关实际注入值或 UNSET | COVERED | eval: deterministic，echo 输出环境变量值 → GENUINE |
| 2 | documentation | negative | 文档未列出该开关即不合格 | COVERED | eval: deterministic，文档搜索可程序化 |
