# SEC-SECMGMT-01-002

- **标题**: 无权限角色对 secret 的创建/更新/删除必须被拒且不改变现有集合
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**无权限角色对 secret 的创建/更新/删除必须被拒且不改变现有集合**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-038

通过标准：
1. type=positive, target=secret_mgmt_api, equals=http_403_and_secret_set_unchanged
2. type=negative, target=secret_mgmt_api

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `with-secrets` |
| Secrets | `['DEPLOY_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | secret_mgmt_api | positive | equals=http_403_and_secret_set_unchanged | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | secret_mgmt_api | negative |  | ✅ GENUINE | 通用断言匹配 |

---