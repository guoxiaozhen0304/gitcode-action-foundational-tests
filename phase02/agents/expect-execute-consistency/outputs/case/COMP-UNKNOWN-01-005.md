# COMP-UNKNOWN-01-005

- **标题**: 顶层 inputs 与 manual_override 字段的实际处理记录
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
逐字记录顶层 inputs 字段（含 default 与 manual_override）的实际处理行为和对手动触发表单的影响。

## 做了什么
顶层声明 inputs.branch_name（default: main, manual_override: true），probe job echo "TOP_INPUT=${{ inputs.branch_name }}"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: TOP_INPUT= | COVERED | run 步骤 echo 输出该字符串，表达式注入真实值 |
| 2 | top_inputs_handling | nonfunctional | llm_assisted | LLM_DEPENDENT | 需人工判定顶层 inputs 是否被识别 |
| 3 | silent_ignore | negative | llm_assisted | LLM_DEPENDENT | 需人工判定是否静默忽略且无提示 |
