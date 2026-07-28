# SEC-SECMGMT-01-002
- **标题**: 无权限角色对 secret 的创建/更新/删除必须被拒且不改变现有集合
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
无权限角色对 secret 的创建/更新/删除操作全部返回 403，且 secret 集合与值保持不变。

## 做了什么
workflow 为 null，harness 通过管理面 API 以 untrusted_contributor 身份执行 secret 操作并检查结果。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | secret_mgmt_api | positive | http_403_and_secret_set_unchanged | COVERED | harness 通过 API 检查越权操作返回 403 且 secret 集合未变 |
| 2 | secret_mgmt_api | negative | must_not_equal: unauthorized_write_applied | COVERED | 外部 API 面验证越权操作未被应用 |

