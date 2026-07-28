# REL-OUTPUT-01-017
- **标题**: step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
写入1,048,577字节应报错或截断并告警，不应静默截断。

## 做了什么
step写出1048577字节到ATOMGIT_OUTPUT。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval=llm_assisted | LLM_DEPENDENT | 文本"日志含超出大小限制的报错/告警(limit/exceed/too large/truncated/1MB)"→YAML用llm_assisted+rubric覆盖 |
| 2 | job_status | positive | equals=failure | COVERED | 文本"step状态=failure"精确对应 |
