# COMPAT-RUNSON-01-003
- **标题**: 自托管 runs-on 对象式写法的实测仲裁
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `runs-on: {type: self-hosted, group: default, labels: [linux, x64]}` 对象式写法在已注册自托管Runner上的调度结局。

## 做了什么
workflow_dispatch触发，runs-on对象式写法；step输出 `echo "OBJECT_FORM_SCHEDULED"` 作为调度成功标记。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive llm | "对象式runs-on结局确定：调度成功或解析期报错" | COVERED | echo "OBJECT_FORM_SCHEDULED"为GENUINE(R1)；调度成功/报错都通过run_status+日志可观测 |
| 2 | run_status | negative llm | "不应表现为job无限queued且无提示" | COVERED | run_status持续观察可判断无限排队(R2)；负向验证 |
