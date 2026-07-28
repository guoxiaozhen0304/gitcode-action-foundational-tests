# COMP-ISOLATION-01-001

- **标题**: 同一 workflow 先后 job 的文件系统相互隔离
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证同一 workflow 的不同 job 之间文件系统隔离：job1 写入的本地文件对 job2 不可见；通过 artifact 显式传递后 job3 可访问。

## 做了什么
job1 写入 `/tmp/isolation_test.txt`（含 "secret data"）并 upload-artifact；job2 检测文件是否存在（不存在则输出 "file not found as expected"，存在则 cat 并 exit 1）；job3 通过 download-artifact 获取共享文件后 cat 输出 "shared payload"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | 三 job 完整执行（job2 验证隔离通过无 exit 1，job3 验证 artifact 传递成功） |
| 2 | run_logs | negative | must_not_contain: secret data | COVERED | 若隔离失效 job2 会 cat 该文件输出 "secret data" 并 exit 1；不出现即隔离正确 |
| 3 | run_logs | positive | must_contain: file not found as expected | COVERED | job2 检测文件不存在后 echo 输出 |
| 4 | run_logs | positive | must_contain: PAYLOAD=shared payload | COVERED | job3 cat 下载的 artifact 文件输出 |
| 5 | run_logs | positive | must_contain: artifact_read_ok | COVERED | job3 验证 artifact 传递成功的 marker |
