# REL-RUNNER-01-049-V2
- **标题**: Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存/磁盘 vs 声明值
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
xlarge/2xlarge实际资源不低于声明90%，失败时归因清晰，不应因架构不匹配随机失败。

## 做了什么
两个大规格probe job各读取系统资源。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | resource_ratio | positive | ge=0.9 | COVERED | 文本"CPU/内存/磁盘最小比率≥0.9"精确对应 |
| 2 | failure_attribution | positive | equals=clear | COVERED | 文本"失败时归因清晰"对应 |
| 3 | (文本负向) 不应因架构不匹配而随机失败 | — | — | MISSING | 文本"不应因架构不匹配而随机失败"在YAML中无独立negative断言 |
