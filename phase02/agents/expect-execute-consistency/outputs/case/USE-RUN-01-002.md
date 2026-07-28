# USE-RUN-01-002
- **标题**: 使用单标签 ubuntu-latest 时报错应给出三段式格式指引
- **维度**: 易用性/兼容性
- **评级**: 部分不符

## 想测什么
验证使用单标签 `runs-on: [ubuntu-latest]`（缺少 arch/flavor）时平台应报错并给出三段式标签格式示例或可用标签列表。

## 做了什么
workflow 使用不完整单标签 runs-on，step 执行 echo。期望平台因标签不匹配而报错。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | 单标签不匹配应导致调度失败 → GENUINE |
| 2 | error_message | nonfunctional | 报错含 runs-on 相关说明并给出正确示例 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
