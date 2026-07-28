# REL-RUNNER-01-049
- **标题**: Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
三种flavor实际资源不低于声明90%、调度≤5min、不应显著低于声明。

## 做了什么
三个并行job各读取/proc/cpuinfo、free -m、df。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | resource_ratio | positive | ge=0.9 | COVERED | 文本"CPU/内存/磁盘最小比率≥0.9"精确对应 |
| 2 | queued_to_running_minutes | nonfunctional | le=5 | COVERED | 文本"queued→running≤5min"精确对应 |
| 3 | (文本负向) 实际资源不应显著低于声明 | — | — | TRIVIAL | 文本"实际资源不应显著低于声明"被resource_ratio≥0.9完全覆盖 |
