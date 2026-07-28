# USE-NEST-01-001
- **标题**: workflow_call 嵌套 3 层时报错应明确提示上限为 2 层
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
关键修复：step 级 `uses: .yml` 为平台非法写法（VALIDATION-RULES 4b），且带 runs-on/steps 的 job 不是真正的 workflow_call——已改为 job 级 uses（与 COMP-CALL-01-001 一致），用例 now 真实触发 3 层嵌套拒绝路径。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | job 级 workflow_call 真实触发嵌套上限校验 |
| 2 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 报错关键词组合判读（至少两项） |

### 残留问题
报错文案判读保留 llm_assisted；调用形式已修正为真实 workflow_call。
