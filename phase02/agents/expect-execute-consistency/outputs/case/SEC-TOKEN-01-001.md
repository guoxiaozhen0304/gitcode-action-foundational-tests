# SEC-TOKEN-01-001
- **标题**: fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限
- **维度**: security
- **评级**: 部分不符

## 想测什么
ATOMGIT_TOKEN 在 fork PR 场景下可执行 clone 等读操作，但写操作应被平台强制拒绝（403）。

## 做了什么
step1 git clone 使用 `${{ atomgit.token }}`，step2 curl POST 创建 issue 测试写权限。但未显式 echo 断言期望字符串。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals:clone_successful | VACUOUS | step git clone 输出不包含该字面量；需通过 exit code 间接判断 |
| 2 | run_logs | negative | must_not_contain:write_permission_granted | VACUOUS | step 从不输出该字符串 |
