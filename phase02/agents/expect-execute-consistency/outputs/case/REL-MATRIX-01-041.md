# REL-MATRIX-01-041
- **标题**: matrix 组合数越界——300 组合超上限时应明确报错（含上限值）不得静默截断
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
同 REL-MATRIX-01-040：加注释澄清 negative silent_truncation_detected 语义（不应检测到静默截断）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | overflow_outcome | positive | expanded_300_or_explicit_rejection_with_limit | ✅ GENUINE | 10x30=300 组合真实触发平台处理 |
| 2 | silent_truncation_detected | negative | equals true | ✅ GENUINE | 负向：不得静默截断（语义已注释澄清） |
| 3 | measured_matrix_limit | nonfunctional | equals recorded | 🔶 LLM_DEPENDENT | 实测记录指令，非机器可判值 |

### 残留问题
measured_matrix_limit=recorded 无数值阈值，保留。
