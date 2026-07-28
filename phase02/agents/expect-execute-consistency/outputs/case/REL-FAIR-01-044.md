# REL-FAIR-01-044
- **标题**: 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调度
- **维度**: reliability
- **评级**: 部分不符
## 想测什么
同时触发 workflow X 和 workflow Y（各 3 个 jobs），验证启动时延差 ≤60s、不应出现一个 workflow 全部完成后另一个才开始。
## 做了什么
YAML 定义 wx_job1..3 和 wy_job1..3 各 sleep 30，由 harness 拆分为两个 workflow 同时触发。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | startup_time_diff_seconds | nonfunctional | le 60 | COVERED | YAML 使用 sleep 30 真实命令，harness 测量两 workflow 首 job 启动时延差 |
| 2 | no_serial_execution | negative | 不应 X 全部完成后 Y 才开始 | MISSING | 文本有负向断言"不应出现 workflow X 全部完成后 workflow Y 才开始"，YAML 无对应 assertion |
