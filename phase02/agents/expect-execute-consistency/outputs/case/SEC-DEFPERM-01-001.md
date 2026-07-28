# SEC-DEFPERM-01-001
- **标题**: ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效
- **维度**: security
- **评级**: 断言一致

## 想测什么
顶层 permissions: repository: read 被 job 继承；job 级覆盖 write 后读操作成功；未覆盖的 job 写操作返回 403。

## 做了什么
workflow 两个 job：inherit-test(read 权限尝试写)、override-write(write 覆盖后读)；real curl 判 HTTP 码。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "WRITE_201" | COVERED | 对应"日志中绝不应出现写操作成功的 201"；real curl→GENUINE |
| 2 | run_logs | positive | contains "WRITE_403" | COVERED | 对应"声明 read 时写操作返回 HTTP 403"；real curl→GENUINE |
| 3 | run_logs | positive | contains "READ_200" | COVERED | 对应"job 级覆盖 write 后读操作返回 READ_200"；real curl→GENUINE |
