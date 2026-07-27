# SEC-NAME-01-003
- **标题**: 可遮蔽系统变量的 secret 命名（ATOMGIT_ 前缀/非法字符/数字开头）创建时必须被拒
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**违规 secret 命名创建被拒，合法命名创建成功**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-041
通过标准：
1. 合法命名创建成功
2. 违规命名全部被拒
3. 报错指明命名规则
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | (workflow: null) | — | — | — |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch (invalid_names: [ATOMGIT_TOKEN, my-secret, 1SECRET], valid_name: DEPLOY_KEY) |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 合法命名创建成功 | positive | secret_mgmt_api equals | ❌ MISSING_SOURCE | target=secret_mgmt_api 为平台管理面接口，workflow 为 null，无任何步骤调用 API |
| 2 | 违规命名被拒 | negative | secret_mgmt_api must_not_equal | ❌ MISSING_SOURCE | 同上 |
| 3 | 报错指明命名规则 | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | llm 辅助判定 |
### 问题
workflow 为 null，所有断言 target=secret_mgmt_api 为外部管理面接口，YAML 无法驱动验证。
---
