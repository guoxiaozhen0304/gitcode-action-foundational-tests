# REL-VCJOB-01-001
- **标题**: 【回归】vcjob（volcano job）格式任务解析与运行——当前已知不通过，修复后回归
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
标准vcjob格式任务正常解析并运行(NPU资源)，不应字段静默丢弃或资源声明忽略。已知不通过，修复后回归。

## 做了什么
手动提交vcjob格式NPU训练任务(workflow=null，触发方式为manual)。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | vcjob_parse_status | positive | equals=success | COVERED | 文本"标准vcjob格式任务被正常解析"精确对应 |
| 2 | vcjob_run_status | positive | equals=Running | COVERED | 文本"被正常运行"对应(run_status=Running) |
| 3 | vcjob_field_handling | negative | eval=llm_assisted | LLM_DEPENDENT | 文本"不应出现字段静默丢弃或NPU资源声明忽略"→YAML用llm_assisted+rubric，符合无平台文档支撑的退化场景合理性 |
