# SEC-SECMGMT-01-001
- **标题**: Secret 写入后任何 API/UI 路径绝不应回读明文
- **维度**: 安全性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**Secret 写入后任何 API/UI 路径绝不应回读明文**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-038
通过标准：
1. workflow 正常引用 secret 且日志脱敏
2. 任何读取接口/UI 均不返回 secret 明文

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Reference secret in workflow | `echo "SECRET_REFERENCE_CHECK: ${{ secrets.DEPLOY_TOKEN }}"` | - | 平台动态求值 secret，runner 脱敏输出 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | [DEPLOY_TOKEN] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals: "masked_with_asterisks" | ✅ GENUINE | 步骤使用 `${{ secrets.DEPLOY_TOKEN }}` 表达式，平台对 secret 引用做脱敏处理 |
| 2 | secret_mgmt_api | negative | must_not_contain_secret: "DEPLOY_TOKEN" | ❌ UNEXERCISED | 无任何 workflow 步骤调用 secret 管理面 API，仅由 harness 侧外部校验 |

### 问题
**断言 2 — UNEXERCISED**: workflow 仅包含一个 echo secret 的步骤，未包含调用 secret 管理面 API 的步骤。该断言依赖 harness 外部测试，workflow 内部无对应行为。
---
