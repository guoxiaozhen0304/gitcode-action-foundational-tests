# REL-CPU-01-022
- **标题**: Runner CPU 饱和——small runner 运行 4 个 CPU 密集型进程应完成但耗时延长
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
small runner 上 4 个 CPU burn 进程运行 60s，job success，耗时约 120±24s。

## 做了什么
for 循环启动 4 个 python3 burn 进程，wait 等待全部完成。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "success" | COVERED | 4 进程 wait 完成，exit 0 则 success |
| 2 | job_duration_seconds | nonfunctional | ge 96, le 144 | LLM_DEPENDENT | 非功能耗时指标，由 harness 测量 |
