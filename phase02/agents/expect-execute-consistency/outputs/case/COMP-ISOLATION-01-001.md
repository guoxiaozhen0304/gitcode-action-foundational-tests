# COMP-ISOLATION-01-001
- **标题**: 同一 workflow 先后 job 的文件系统相互隔离
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
job2 无法看到 job1 写入的本地文件（文件系统隔离）；显式通过 artifact 传递后 job3 可读取共享文件。

## 做了什么
1. job1：`echo "secret data" > /tmp/isolation_test.txt`，`echo "shared payload" > ./artifact_out/shared.txt`，upload-artifact
2. job2 (needs: job1)：检查 `/tmp/isolation_test.txt` 是否存在，不存在则输出 "file not found as expected"，存在则 exit 1
3. job3 (needs: job1)：download-artifact，`cat shared.txt` 输出内容并 echo "artifact_read_ok"

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | job2 期望文件不存在（不 exit 1），job3 读取 artifact |
| 2 | run_logs | negative | must_not_contain: secret data | COVERED | job2 中文件不存在，不会 cat 输出 "secret data"；job1 输出到文件非 stdout |
| 3 | run_logs | positive | must_contain: file not found as expected | COVERED | job2 检查文件不存在时 echo |
| 4 | run_logs | positive | must_contain: PAYLOAD=shared payload | COVERED | job3 cat shared.txt 输出 |
| 5 | run_logs | positive | must_contain: artifact_read_ok | COVERED | job3 echo 固定标记 |
