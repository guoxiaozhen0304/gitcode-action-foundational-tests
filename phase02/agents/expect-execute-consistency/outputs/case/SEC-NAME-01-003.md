# SEC-NAME-01-003
- **标题**: 可遮蔽系统变量的 secret 命名（ATOMGIT_前缀/非法字符/数字开头）创建时必须被拒   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
ATOMGIT_前缀、含中划线、数字开头的secret创建应被拒绝，合法命名应成功，报错应指明命名规则。
## 做了什么
YAML中workflow:null，trigger params携带invalid_names列表和valid_name。所有断言target secret_mgmt_api平台管理API，第三个断言为llm_assisted。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | secret_mgmt_api | positive | equals "valid_name_created" | COVERED | 合法命名创建结果为平台API可判定 |
| 2 | secret_mgmt_api | negative | must_not_equal "invalid_name_accepted" | COVERED | 非法命名拒绝为平台API可判定 |
| 3 | error_message | nonfunctional | 报错应指明命名规则 | UNVERIFIABLE | eval:llm_assisted，报错质量判定需LLM辅助 |
