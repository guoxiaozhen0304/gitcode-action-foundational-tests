# SEC-WCMD-01-001
- **标题**: Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值
- **维度**: security
- **评级**: 断言一致

## 想测什么
add-mask 命令的响应中绝不应包含被遮蔽前的 secret 原值；payload 位置显示脱敏标记 ***。

## 做了什么
step `echo "::add-mask::${{ secrets.API_KEY }}"` 触发 add-mask 命令。平台日志中应脱敏处理。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret:API_KEY | COVERED | `${{ secrets.API_KEY }}` 引用真实 secret，平台日志应执行脱敏 |
| 2 | run_logs | positive | contains:*** | COVERED | add-mask 命令响应中 payload 位置平台替换为 ***；可观察 |
