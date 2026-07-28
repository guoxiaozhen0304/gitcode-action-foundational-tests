# REL-RUNNER-01-049
- **标题**: Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 small/medium/large 三种 Runner 的实际 CPU/内存/磁盘资源不低于声明值的 90%。
## 做了什么
对 small/medium/large 各触发探针 job，读取 nproc、free -m、df -BG，计算实际资源与声明值的比率。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | resource_ratio | positive | ge "0.9" | COVERED | harness 从探针输出解析实际资源，计算最小比率 |
| 2 | queued_to_running_minutes | nonfunctional | le "5" | COVERED | harness 测量调度延迟 |
