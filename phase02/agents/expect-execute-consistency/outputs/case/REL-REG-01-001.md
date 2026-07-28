# REL-REG-01-001
- **标题**: 新仓库 workflow 注册——首次 push 含合法流水线配置即应触发，无需手动再改一次   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证新仓库首次 push 含合法 workflow 配置时应立即注册并触发，无需手动再改一次 yml（#17 回归点）。
## 做了什么
新建 3 个空仓库，各首次提交推入同一条极简 workflow（push 触发），记录注册时延，不做手动干预。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_created | positive | equals "true" | COVERED | harness 验证 push 后 run 被创建 |
| 2 | run_records_count | negative | equals "0" | COVERED | 检测"0 条 run 记录"的静默丢失场景（#17 回归点） |
| 3 | registration_delay_seconds | nonfunctional | le "300" | COVERED | harness 测量 push→run 创建的注册延迟 |
| 4 | successful_repo_ratio | nonfunctional | equals "3/3" | COVERED | harness 统计 3/3 仓库注册成功 |
