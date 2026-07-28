# USE-INPT-01-001  - **标题**: 使用 string 类型 input 时正常通过校验   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

YAML 校验通过，可手动触发

## 做了什么

- 1. 声明 workflow_dispatch inputs 的 type: string

- - [正向] 运行可手动触发
- - [正向] 输入参数正常传递

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=`COMPLETED` | COVERED | run_status: echo带有${{ inputs.env }}表达式→GENUINE; 测试type:string可接受性 |
