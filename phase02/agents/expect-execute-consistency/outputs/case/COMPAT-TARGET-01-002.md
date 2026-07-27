# COMPAT-TARGET-01-002
- **标题**: pull_request_target 在 fork 场景下应保持 secret 隔离
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**pull_request_target 在 fork 场景下应保持 secret 隔离**
- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMPAT-032
通过标准：
1. [负向] 日志中不应出现 DEPLOY_TOKEN 明文
2. [正向] pull_request_target 场景下 workflow 能成功引用 secrets.DEPLOY_TOKEN
3. [正向] 普通 pull_request 场景下 fork PR 无法访问 secrets

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | `uses: checkout` | - | checkout 内部日志 |
| 2 | echo secret masked | `echo "Token is: ${{ secrets.DEPLOY_TOKEN }}"` | - | `Token is: ***` (脱敏后) |

## 3. 触发与运行环境
| 触发事件 | pull_request_target |
| 触发身份 | untrusted_contributor |
| Repo 环境 | with-fork-pr |
| Secrets | [DEPLOY_TOKEN] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret=DEPLOY_TOKEN, eval=deterministic | ✅ GENUINE | 步骤引用 `${{ secrets.DEPLOY_TOKEN }}` 并 echo 到日志，测试平台脱敏机制 |
| 2 | run_status | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 token 引用是否成功 |

---
