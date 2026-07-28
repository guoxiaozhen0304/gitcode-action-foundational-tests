# USE-YAML-01-001
- **标题**: 缺少必填字段 on 时报错应指出具体字段名与位置
- **维度**: 易用性
- **评级**: 部分不符

## 想测什么
验证提交缺少 on 字段的 workflow 时平台应报错并指出缺失字段名、文件路径/行号，最好给出正确写法示例。

## 做了什么
workflow 仅有 jobs 定义而缺少 on 字段。期望平台在校验阶段报错。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | 缺少必填字段应导致校验失败 → GENUINE |
| 2 | error_message | nonfunctional | 报错含字段名、行号、正确写法示例三项中至少两项 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
