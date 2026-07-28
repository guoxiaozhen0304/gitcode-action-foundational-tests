# USE-YAML-01-002
- **标题**: YAML 缩进错误时报错应指出具体行号与列号
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 复核：维持原判定，已符合最优形态）

## 修复内容
本次未改动。缩进错误的 workflow 为平台验证型（解析失败 → run_status 断言 GENUINE）；行号列号为动态值（取决于错误位置），无法作为固定串确定性断言，保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | 缩进错误应解析失败 |
| 2 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 行号/列号/示例组合判读 |

### 残留问题
报错位置信息判读保留 llm_assisted。
