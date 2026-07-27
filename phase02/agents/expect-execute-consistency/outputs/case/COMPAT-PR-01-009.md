# COMPAT-PR-01-009
- **标题**: pull_request 触发时 atomgit.sha/ref 的代码版本语义（对齐 GitHub merge commit 模型）
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**pull_request 触发时 atomgit.sha/ref 的代码版本语义（对齐 GitHub merge commit 模型）**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMPAT-039
通过标准：
1. [正向] 观测 atomgit.sha / atomgit.ref 实际取值并与 head/base/试合并 sha 比对定位语义
2. [负向] 不应出现 checkout 检出版本与 atomgit.sha 指向版本不一致
3. [非功能] 语义确认后回写 Parity Matrix 作为该点 oracle

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Record context sha and ref | `echo "CTX_SHA=${{ atomgit.sha }}"` → `echo "CTX_REF=${{ atomgit.ref }}"` → `echo "ENV_SHA=$ATOMGIT_SHA"` | - | `CTX_SHA=<sha>`, `CTX_REF=<ref>`, `ENV_SHA=<sha>` |
| 2 | (TC) checkout source | `uses: checkout` | - | checkout 内部日志 |
| 3 | Record checked out commit | `echo "CHECKOUT_HEAD=$(git rev-parse HEAD)"` → `echo "PROBE_DONE"` | - | `CHECKOUT_HEAD=<sha>`, `PROBE_DONE` |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | with-pull-request |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain="PROBE_DONE" | ✅ GENUINE | 步骤先执行 `git rev-parse HEAD`（实质命令）再 echo 哨兵；${{ }} 表达式输出动态上下文值，非纯字面量 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 比对 CTX_SHA/ENV_SHA 与 PR head sha |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 CHECKOUT_HEAD 与 CTX_SHA 一致性 |

---
