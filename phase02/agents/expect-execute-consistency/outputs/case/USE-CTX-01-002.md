# USE-CTX-01-002
- **标题**: 使用 github 上下文时报错应提示 atomgit 替代
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用 github 上下文时报错应提示 atomgit 替代**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-002
通过标准：
1. 不应静默求值为空字符串
2. 报错信息中应同时出现 github 与 atomgit 字样

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo github ref | `echo "ref=${{ github.ref }}"` | - | 若平台拒绝 github 上下文表达式，求值失败/报错 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: COMPLETED | ✅ GENUINE | 步骤使用 `${{ github.ref }}`（非 GitCode 上下文），平台可能拒绝表达式求值，运行不应完成 |
| 2 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 判定报错是否包含 github/atomgit 对照 |

### 问题
(无 — 断言 1 为平台表达式验证测试，报错由平台产生。)
---
