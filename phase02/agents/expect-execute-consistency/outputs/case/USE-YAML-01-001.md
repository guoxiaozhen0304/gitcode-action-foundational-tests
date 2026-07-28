# USE-YAML-01-001
- **标题**: 缺少必填字段 on 时报错应指出具体字段名与位置
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 复核：维持原判定，已符合最优形态）

## 修复内容
本次未改动。缺 on 字段的 workflow 为平台验证型（校验期拒绝 → run_status 断言 GENUINE）；报错三项中至少两项（字段名/行号/示例）为组合判读，"on" 单串过短无法作为确定性锚点，保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | 缺必填字段应校验失败 |
| 2 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 字段名/行号/示例组合判读 |

### 残留问题
报错内容组合判读保留 llm_assisted。
