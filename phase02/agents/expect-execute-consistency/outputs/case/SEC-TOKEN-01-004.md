# SEC-TOKEN-01-004
- **标题**: 残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-037
通过标准：
1. 新 run 自身的 ATOMGIT_TOKEN 在其权限范围内可用
2. 残留于 artifact 的旧 token 绝不应在新 run 中通过鉴权

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt auth with residual token | `echo "RESIDUAL_TOKEN_AUTH_ATTEMPT: harness supplies residual token from prior run artifact"` | - | 仅 echo 标记 |
| 2 | Confirm current run token works | `echo "CURRENT_RUN_TOKEN_CHECK: in scope read with own token"` | - | 仅 echo 标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-artifacts |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals: "current_run_token_operational" | ❌ MISSING_SOURCE | 步骤 echo "CURRENT_RUN_TOKEN_CHECK: ..."，不匹配期望字符串 "current_run_token_operational" |
| 2 | api_response | negative | must_not_equal: "http_2xx_with_residual_token" | ❌ UNEXERCISED | api_response 依赖 harness 外部 API 调用，workflow 无对应步骤 |

### 问题
**断言 1 — MISSING_SOURCE**: 步骤仅 echo 标记文字，不执行真实 token 验证，且输出字符串与断言不匹配。
**断言 2 — UNEXERCISED**: api_response target 需 harness 外部持残留 token 调用 API，workflow 内部无该行为。
---
