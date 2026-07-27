# SEC-ENV-01-002
- **标题**: 环境级 secret 审批前 workflow 不可读取
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**审批前环境 secret 为空，job 状态为挂起或失败**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-027
通过标准：
1. 日志不含 "secret accessible unexpectedly"
2. run_status 为 pending_or_failed
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Try use env secret | `if [ -z "$PROD_TOKEN" ]; then echo "secret not accessible before approval"; else echo "secret accessible unexpectedly"; exit 1; fi` | environment: production | 空值检测结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-env-secrets |
| Secrets | PROD_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 "secret accessible unexpectedly" | negative | run_logs must_not_contain | ✅ GENUINE | 步骤有 if 条件判断，有 exit 1 失败路径；环境 secret 审批前为空 → 打印否定消息 |
| 2 | pending_or_failed | positive | run_status equals | ✅ GENUINE | 步骤有 exit 1 路径（secret 意外可访问时），审批前 secret 为空时 echo 无 exit，但 environment: production 未审批 → job 挂起/失败；平台审批机制决定 |
### 问题
(无)
---
