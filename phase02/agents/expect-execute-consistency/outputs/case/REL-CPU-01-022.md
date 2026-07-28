# REL-CPU-01-022
- **标题**: Runner CPU 饱和——small runner 运行 4 个 CPU 密集型进程应完成但耗时延长
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
small runner 上启动 4 个并行 CPU burn 进程各 60 秒，验证 job 状态=success、总耗约 120±24 秒、不应被强制终止。
## 做了什么
YAML 使用 python3 真实 CPU burn 循环（含 `time.time()` + list comprehension），4 进程并行 `&` + `wait`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals success | COVERED | YAML python3 CPU burn 真实命令，platform 日志确认 job 正常完成 |
| 2 | job_duration_seconds | nonfunctional | ge 96 le 144 | COVERED | YAML assert 耗时范围 96-144s（120±24），对应文本"总耗时约为 120±24 秒" |
| 3 | not_force_killed | negative | 不应被系统强制终止 | COVERED | job_status=success 隐含未被终止，对应文本负向断言 |
