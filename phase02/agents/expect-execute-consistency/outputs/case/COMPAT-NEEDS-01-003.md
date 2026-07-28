# COMPAT-NEEDS-01-003
- **标题**: matrix 上游 job 的 needs outputs 聚合语义与未声明 output 边界
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 matrix 上游 job 的 outputs 聚合行为（多实例取哪个值），以及引用未声明 output 的边界行为。

## 做了什么
上游 matrix job（idx: [1,2]）各实例写不同 mark 值；下游通过 needs 读取聚合后的 mark 和从未声明的 never_declared。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "PROBE_DONE" | COVERED | echo 输出可验证步骤完成 |
| 2 | run_logs | positive | llm_assisted rubric | LLM_DEPENDENT | AGG_MARK 聚合取值确定性需 LLM 辅助判断 |
| 3 | run_logs | positive | llm_assisted rubric | LLM_DEPENDENT | UNDECLARED 空值行为需 LLM 辅助判断 |
