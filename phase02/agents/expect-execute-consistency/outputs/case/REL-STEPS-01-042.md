# REL-STEPS-01-042
- **标题**: 超多 step——单 job 内 50 个 step 应全部串行执行无丢失   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证单 job 内 50 个 step 全部按顺序串行执行，无丢失、无顺序错乱。
## 做了什么
创建含单 job 50 个 step 的 workflow（每个 step echo step NN），触发并核对步骤详情。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_count | positive | equals "50" | COVERED | harness 统计运行详情页中显示的 step 数 |
| 2 | step_order | positive | equals "correct" | COVERED | harness 解析各 step 日志中的唯一标识验证顺序 |
