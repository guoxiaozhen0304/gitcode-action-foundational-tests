# REL-PREEMPT-01-006
- **标题**: preemption events 越界值——配置 11 个应被拒绝   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 concurrency.preemption.events 配置 11 个事件（超出 10 上限）时平台应在解析阶段明确拒绝。
## 做了什么
创建 concurrency.preemption.events 含 11 个事件的 workflow（新增 pr 事件）并尝试保存。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | yaml_validation | positive | equals "rejected" | COVERED | harness 检查 workflow YAML 保存/校验是否被拒绝 |
