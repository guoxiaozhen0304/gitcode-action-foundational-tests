# REL-MEM-01-020
- **标题**: Runner 内存边界——small runner 分配 7.5 GB 应成功
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
small runner 分配7.5GB内存应成功，内存占用峰值约7.5GB，不应OOM。

## 做了什么
python3 分配 7680*1024*1024 bytearray。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=success | COVERED | 文本"job状态=success"精确对应 |
| 2 | (文本负向) 不应在7GB时OOM | — | — | MISSING | 文本"不应在7GB时OOM"在YAML中无对应negative断言(可被success隐含) |
| 3 | (文本) 内存占用峰值约7.5GB | — | — | MISSING | 文本"内存占用峰值约7.5GB"在YAML中无独立资源监控断言 |
