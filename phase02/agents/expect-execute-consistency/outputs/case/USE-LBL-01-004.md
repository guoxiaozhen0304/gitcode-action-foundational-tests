# USE-LBL-01-004  - **标题**: quick-start 单标签写法 runs-on ubuntu-latest 的可调度性验证   - **维度**: usability   - **评级**: 断言一致

## 想测什么

若 quick-start 示例写法合法，workflow 应被接受并成功调度；若平台拒绝，则证明 quick-start 示例本身错误（文档缺陷）

## 做了什么

- 1. 按 01-quick-start.md 示例写法，以单标签字符串形式声明 runs-on 并提交 workflow
- 2. 观察平台校验与调度结果

- - [正向] 文档示例写法应可被平台接受并运行成功
- - [负向] 平台不应接受一种写法而文档示例给出另一种却不加说明

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=`success` | COVERED | run_status: runs-on:ubuntu-latest格式验证→被测的是平台YAML解析而非echo步骤 |
| 2 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: quick-start示例一致性确定性判定 |
