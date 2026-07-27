# REL-MATRIX-01-040
- **标题**: matrix 组合数边界——256 组合（GitHub 上限）应全部展开或被明确拒绝
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**matrix 组合数边界——256 组合（GitHub 上限）应全部展开或被明确拒绝**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-076
通过标准：
1. job 数与声明组合数一致（256），或收到明确错误
2. 不应静默截断
3. 展开/入队时延 ≤600 秒（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | combo marker step | `echo "combo=${{ matrix.os }}-${{ matrix.ver }}"` | — | 输出组合标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | jobs_expanded_count = 256_or_explicit_rejection | positive | — | ✅ GENUINE | os[8]×ver[32]=256 组合，使用 `${{ matrix.* }}` 表达式，大规模 matrix 真实触发平台展开逻辑 |
| 2 | silent_truncation_detected = true | negative | — | ❌ IMPOSSIBLE | 该断言期望 `silent_truncation_detected = true`（即应检测到静默截断），但这与文本"不应静默截断"矛盾——文本要求不应截断，断言却期望检测到截断为 true。此断言方向错误 |
| 3 | expand_enqueue_seconds ≤ 600 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
### 问题
断言 2（negative/silent_truncation_detected = true）与文本语义矛盾：文本明确"不应静默截断"，但断言期望 silent_truncation_detected=true（即应成功检测到截断），若未截断则断言反而失败。negative 断言的 equals:"true" 在此上下文中语义不清晰。
---
