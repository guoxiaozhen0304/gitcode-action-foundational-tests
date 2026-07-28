# REL-REG-01-001
- **标题**: 新仓库 workflow 注册——首次 push 含合法流水线配置即应触发，无需手动再改一次
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
新建3个空仓库首次push含合法workflow，3/3 run被创建、注册延迟≤300s、不应静默丢失(#17回归)。

## 做了什么
fixture new_repo_count=3，push触发含echo探测step。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_created | positive | equals=true | COVERED | 文本"3/3仓库首次push后run被创建"对应(harness聚合跨仓库) |
| 2 | run_records_count | negative | equals=0 | COVERED | 文本"不应静默丢失(#17回归)"精确对应(negative+equals=0) |
| 3 | registration_delay_seconds | nonfunctional | le=300 | COVERED | 文本"注册延迟≤5分钟(300秒)"精确对应 |
| 4 | successful_repo_ratio | nonfunctional | equals=3/3 | COVERED | 文本"3/3仓库首次push即创建对应run"精确对应 |
