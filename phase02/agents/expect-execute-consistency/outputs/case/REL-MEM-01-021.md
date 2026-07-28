# REL-MEM-01-021
- **标题**: Runner 内存越界——small runner 分配 9 GB 应被 OOM kill
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
small runner 分配9GB应被OOM kill，日志含OOM/Killed，不影响同Runner其他job。

## 做了什么
python3 分配 9216*1024*1024 bytearray。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals=failure | COVERED | 文本"job状态=failure"精确对应 |
| 2 | run_logs | positive | contains=Killed | COVERED | 文本"日志含OOM或Killed信息"对应(contains Killed可覆盖) |
| 3 | (文本负向) 不应导致Runner宿主机崩溃 | — | — | MISSING | 文本"不应导致Runner宿主机崩溃"在YAML中无独立断言 |
