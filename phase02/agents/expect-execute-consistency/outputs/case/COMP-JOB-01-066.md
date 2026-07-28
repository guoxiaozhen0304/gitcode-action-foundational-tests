# COMP-JOB-01-066
- **标题**: job 必填字段 name runs-on steps 验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
job 必须包含 name/runs-on/steps，完整 job 通过校验，缺 name 或缺 steps 被平台拒绝。

## 做了什么
1. step `Echo ok`：`echo "job_fields_ok"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | 完整 job 定义通过校验 |
| 2 | run_logs | positive | must_contain: job_fields_ok | COVERED | echo 固定标记 |
| 3 | workflow_parse | negative | llm_assisted | LLM_DEPENDENT | eval=llm_assisted，变体 V1（缺 name） |
| 4 | workflow_parse | negative | llm_assisted | LLM_DEPENDENT | eval=llm_assisted，变体 V2（缺 steps） |
