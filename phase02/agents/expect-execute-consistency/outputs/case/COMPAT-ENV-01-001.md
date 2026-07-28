# COMPAT-ENV-01-001
- **标题**: ATOMGIT_SHA 环境变量应正确返回触发提交 SHA   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 $ATOMGIT_SHA 返回 40 位十六进制 SHA。
## 做了什么
workflow_dispatch 触发，step 用 `grep -qE '^[0-9a-f]{40}$'` 校验 $ATOMGIT_SHA 格式，成功则 echo `ATOMGIT_SHA_FORMAT_OK`，否则 exit 1。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | positive | equals: success | GENUINE→COVERED | SHA 格式校验 + exit 1 为真实 fail path |
| 2 | run_logs | positive | must_contain: ATOMGIT_SHA_FORMAT_OK | GENUINE→COVERED | successful branch echo 产生，失败则 exit 1 阻断 |
| 3 | run_logs | negative | must_not_contain: ATOMGIT_SHA_FORMAT_BAD | GENUINE→COVERED | 仅失败分支输出该文本，成功时不应出现 |
