# COMPAT-TARGET-01-001
- **标题**: pull_request_target 默认 checkout 应为 base 分支而非 head 分支
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**pull_request_target 默认 checkout 应为 base 分支而非 head 分支**
- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMPAT-032
通过标准：
1. [负向] 日志中显示的 SHA 不应等于 fork PR head SHA
2. [正向] 日志中显示的 SHA 等于 base 分支 SHA
3. [正向] workflow 能访问仓库 secrets

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | `uses: checkout` | - | checkout 内部日志 |
| 2 | print sha info | `echo "Current SHA: ${{ atomgit.sha }}"` → `echo "Base SHA: ${{ atomgit.event.pull_request.base.sha }}"` → `echo "Head SHA: ${{ atomgit.event.pull_request.head.sha }}"` | - | `Current SHA: <sha>`, `Base SHA: <sha>`, `Head SHA: <sha>` |

## 3. 触发与运行环境
| 触发事件 | pull_request_target |
| 触发身份 | untrusted_contributor |
| Repo 环境 | with-fork-pr |
| Secrets | [DEPLOY_TOKEN] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 对比 SHA 确认未检出 head |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认检出 SHA 等于 base |
| 3 | run_status | positive | equals=success, eval=deterministic | ✅ GENUINE | 步骤含 `uses: checkout` 和 `${{ atomgit.sha }}` 等动态表达式，平台上下文求值即功能执行 |

---
