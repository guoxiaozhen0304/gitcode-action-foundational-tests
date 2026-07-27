# SEC-TOKEN-01-003
- **标题**: run 结束后旧 ATOMGIT_TOKEN 调用任何 API 必须失效
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**run 结束后旧 ATOMGIT_TOKEN 调用任何 API 必须失效**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-037
通过标准：
1. run 进行中 token 可完成权限内只读操作
2. run 结束后旧 token 任何 API 调用绝不应成功
3. rerun 的 token 签发行为可确定性判定

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use token for in scope read | `git ls-remote https://x-access-token:${{ atomgit.token }}@... HEAD` | - | git ls-remote 输出 |
| 2 | Emit in run marker | `echo "IN_RUN_TOKEN_OPERATIONAL: token worked within scope during run"` | - | 标记字符串 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals: "in_run_token_operational" | ❌ MISSING_SOURCE | 步骤输出 "IN_RUN_TOKEN_OPERATIONAL: ..."（大写），与期望的 "in_run_token_operational"（小写）不匹配 |
| 2 | api_response | negative | must_not_equal: "http_2xx_with_post_run_token" | ❌ UNEXERCISED | api_response 非 workflow 步骤产生，run 结束后 token 验证需 harness 外部发起 |
| 3 | rerun_behavior | nonfunctional | equals: "new_token_issued_or_explicit_reuse" | 🔶 LLM_DEPENDENT | 非功能断言 |

### 问题
**断言 1 — MISSING_SOURCE**: 步骤 echo 大写的 "IN_RUN_TOKEN_OPERATIONAL"，断言期望小写 "in_run_token_operational"，不匹配。
**断言 2 — UNEXERCISED**: api_response target 依赖 harness 在 run 结束后持旧 token 发起 API 调用，workflow 内部无对应步骤。
---
