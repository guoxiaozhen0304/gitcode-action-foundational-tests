# SEC-SECMGMT-01-002
- **标题**: 无权限角色对 secret 的创建/更新/删除必须被拒且不改变现有集合
- **维度**: security
- **评级**: 部分不符

## 想测什么
无权限角色对 secret 的越权管理操作全部返回 403，且 secret 集合与值保持不变。

## 做了什么
workflow: null，无任何 job/step。两条断言均指向 secret_mgmt_api 外部接口。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | secret_mgmt_api | positive | equals:http_403_and_secret_set_unchanged | MISSING_SOURCE | 无 workflow 步骤产生可观察证据，完全依赖外部 API 调用 |
| 2 | secret_mgmt_api | negative | must_not_equal:unauthorized_write_applied | MISSING_SOURCE | 同上，无运行时输出可供断言匹配 |
