# REL-VCJOB-01-002
- **标题**: 大规模 vcjob 并发提交（≥50）无丢失、无级联失败
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
静默丢失断言由 llm 转确定性（negative lost_count equals 0，由对账直接支撑）；加注释说明平台操作型设计；级联失败归因判读保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | vcjob_terminal_reconciliation | positive | submitted==recorded==terminal==50 | ✅ COVERED | 平台对账可判定 |
| 2 | lost_count | negative | equals 0 | ✅ COVERED | 丢失计数由对账直接得出 |
| 3 | cascading_failure | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 级联失败归因判读（Pending 属合法终态需排除） |

### 残留问题
级联失败的归因（资源不足 Pending vs 真级联）需判读，保留 llm_assisted（YAML 已注释）。
