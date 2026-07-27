# REL-MATRIX-01-041
- **标题**: matrix 组合数越界——300 组合超上限时应明确报错（含上限值）不得静默截断
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**matrix 组合数越界——300 组合超上限时应明确报错（含上限值）不得静默截断**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-076
通过标准：
1. 拒绝时错误信息含实际上限数值；或全部展开且 job 数=300
2. 不应静默截断

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
| 1 | overflow_outcome = expanded_300_or_explicit_rejection_with_limit | positive | — | ✅ GENUINE | os[10]×ver[30]=300 组合，使用 `${{ matrix.* }}` 表达式，真实触发平台对超大规模 matrix 的处理逻辑 |
| 2 | silent_truncation_detected = true | negative | — | ❌ IMPOSSIBLE | 同 REL-MATRIX-01-040，断言期望 silent_truncation_detected=true 与文本"不应静默截断"语义矛盾：若平台行为正确（不截断），该断言反而失败 |
| 3 | measured_matrix_limit = recorded | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
### 问题
断言 2（negative/silent_truncation_detected = true）语义与文本矛盾，同 REL-MATRIX-01-040。
---
