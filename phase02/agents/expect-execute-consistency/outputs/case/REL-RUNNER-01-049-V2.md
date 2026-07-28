# REL-RUNNER-01-049-V2
- **标题**: Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存/磁盘 vs 声明值   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 xlarge/2xlarge 两种大规格 Runner 的实际资源不低于声明值的 90%，失败时归因清晰。
## 做了什么
对 xlarge/2xlarge 各触发探针 job，读取系统资源信息。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | resource_ratio | positive | ge "0.9" | COVERED | harness 从探针输出解析实际资源并计算比率 |
| 2 | failure_attribution | positive | equals "clear" | COVERED | harness 检查失败时日志是否清晰归因 |
