# SEC-TOKEN-01-002
- **标题**: fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝
- **维度**: security
- **评级**: 部分不符

## 想测什么
fork PR 中 ATOMGIT_TOKEN 推送操作返回权限拒绝（403），日志显示权限不足。

## 做了什么
step 执行 git push，失败时 `|| echo "push denied"`。但该输出与断言期望不完全匹配。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | equals:push_denied_or_403 | COVERED | step 在 push 失败时 echo "push denied"，接近于 equals 期望；且类型 negative 搭配 equals 语义不标准 |
| 2 | run_status | positive | equals:completed | COVERED | 平台 run_status，push 被拒后 run 仍可 completed |
