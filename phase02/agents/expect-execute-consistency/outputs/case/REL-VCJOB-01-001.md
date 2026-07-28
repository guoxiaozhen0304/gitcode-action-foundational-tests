# REL-VCJOB-01-001
- **标题**: 【回归】vcjob（volcano job）格式任务解析与运行——当前已知不通过，修复后回归   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证标准 vcjob（volcano job）格式任务被正常解析并运行，各 task 按声明获得 NPU 资源——当前已知不通过（xlsx 实测），断言按修复后的正确行为编写。
## 做了什么
按 vcjob 标准格式构造并提交 1 个请求 NPU 的训练任务（platform_op: vcjob_submit），观察平台解析结果与运行状态。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | vcjob_parse_status | positive | equals "success" | COVERED | harness 提交 vcjob 并检查平台解析状态 |
| 2 | vcjob_run_status | positive | equals "Running" | COVERED | harness 查询 vcjob 任务运行状态 |
| 3 | vcjob_field_handling | negative | eval "llm_assisted" | LLM_DEPENDENT | 字段级静默丢弃/资源声明忽略判定需结合实测环境与 LLM 辅助 |
