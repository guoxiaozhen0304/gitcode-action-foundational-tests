# COMPAT-RUNSON-01-004
- **标题**: 自托管 runs-on 数组式写法的实测仲裁
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `runs-on: [self-hosted, linux, x64]` 数组式写法在已注册自托管Runner上的调度结局，并与对象式结论合并裁定匹配语义。

## 做了什么
workflow_dispatch触发，runs-on数组式写法；step输出 `echo "ARRAY_FORM_SCHEDULED"` 作为调度成功标记。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive llm | "数组式runs-on结局确定：调度成功或解析期报错" | COVERED | echo "ARRAY_FORM_SCHEDULED"为GENUINE(R1)；与003同策略 |
| 2 | run_status | negative llm | "不应表现为job无限queued且无提示" | COVERED | run_status持续观察可判断无限排队 |
| 3 | run_status | nonfunctional llm | "与003结论合并裁定匹配语义等价性" | LLM_DEPENDENT | R5: nonfunctional + llm；合并分析需人工/LLM |
