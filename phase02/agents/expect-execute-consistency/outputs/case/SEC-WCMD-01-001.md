# SEC-WCMD-01-001
- **标题**: Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
add-mask 命令的响应中绝不应包含 secret 原值，payload 位置显示脱敏标记 ***。

## 做了什么
workflow 中 `echo "::add-mask::${{ secrets.API_KEY }}"` 调用 add-mask 工作流命令。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret: API_KEY | COVERED | `::add-mask::${{ secrets.API_KEY }}` 真实表达式和 workflow 命令，平台日志脱敏 |
| 2 | run_logs | positive | contains: *** | COVERED | 平台日志中 mask 位置应显示 *** 脱敏标记 |

