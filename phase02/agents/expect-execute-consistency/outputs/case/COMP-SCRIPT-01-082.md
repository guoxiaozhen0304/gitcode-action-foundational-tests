# COMP-SCRIPT-01-082

- **标题**: 脚本权限设置与直接执行验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 run 中可通过 chmod +x 赋予脚本权限后直接执行。

## 做了什么
Step: `chmod +x ./scripts/hello.sh && ./scripts/hello.sh`（真实 chmod 命令 + 真实脚本执行）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | chmod 和 script 执行可能真实失败，run_status 非必然成功 |
