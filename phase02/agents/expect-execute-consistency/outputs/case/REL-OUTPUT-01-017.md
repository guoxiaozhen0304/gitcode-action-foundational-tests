# REL-OUTPUT-01-017
- **标题**: step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 ATOMGIT_OUTPUT 写入 1,048,577 bytes（超出 1 MB）时应被平台拒绝或报错，不得静默截断。
## 做了什么
step 通过 python3 生成 1048577 个 A 字符写入 ATOMGIT_OUTPUT 的 data 变量。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval "llm_assisted" | LLM_DEPENDENT | 日志关键字判据（limit/exceed/too large 等）交由 LLM 辅助评判 |
| 2 | job_status | positive | equals "failure" | COVERED | 平台 API 查询 job 终态 |
