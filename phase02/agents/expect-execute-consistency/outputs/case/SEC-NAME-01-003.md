# SEC-NAME-01-003
- **标题**: 可遮蔽系统变量的 secret 命名（ATOMGIT_ 前缀/非法字符/数字开头）创建时必须被拒
- **维度**: security
- **评级**: 断言一致

## 想测什么
ATOMGIT_TOKEN、my-secret、1SECRET 创建被拒；合法命名 DEPLOY_KEY 创建成功。

## 做了什么
workflow=null（平台操作型）；harness 通过 secret_mgmt_api 逐一尝试创建。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | secret_mgmt_api | positive | equals "valid_name_created" | COVERED | 对应"合法命名创建成功"；harness→GENUINE |
| 2 | secret_mgmt_api | negative | must_not_equal "invalid_name_accepted" | COVERED | 对应"违规命名全部被拒绝"；harness→GENUINE |
| 3 | error_message | nonfunctional | eval llm_assisted | COVERED | 对应"报错指明命名规则"；LLM 辅助 = 断言一致 |
