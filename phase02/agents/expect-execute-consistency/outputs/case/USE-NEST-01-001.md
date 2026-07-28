# USE-NEST-01-001
- **标题**: workflow_call 嵌套 3 层时报错应明确提示上限为 2 层
- **维度**: 易用性
- **评级**: 部分不符

## 想测什么
验证主 workflow 调用 A→A 调用 B→B 调用 C 的三层嵌套应被平台拒绝，报错明确说明 workflow_call 嵌套上限为 2 层。

## 做了什么
主 workflow 通过 job 级 uses 调用 reusable-level1.yml（该文件又调用 reusable-level2.yml，构成三层嵌套）。期望平台在调度阶段报错。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | 超出嵌套上限应导致调度失败 → GENUINE |
| 2 | error_message | nonfunctional | 报错含 workflow_call、嵌套、2 层等关键词 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
