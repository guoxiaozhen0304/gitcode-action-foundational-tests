# COMP-CALL-01-002
- **标题**: 3 层 workflow_call 嵌套应被拒绝
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
关键修复：原 workflow 仅 echo "attempting 3 layer call"，无任何嵌套调用（IMPOSSIBLE——必然 success）。已改为 job 级 `uses: ./.gitcode/workflows/reusable-level1.yml` 真实触发 3 层嵌套拒绝路径。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals success | ✅ GENUINE | 真实 3 层 workflow_call 应被平台拒绝 |
| 2 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 报错是否说明 2 层上限属文案判读 |

### 残留问题
报错文案判读保留 llm_assisted；嵌套调用已真实化（评级由完全不符升为部分不符）。
