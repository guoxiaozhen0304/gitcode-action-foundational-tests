# USE-ONBD-01-001  - **标题**: 新手快速开始路径端到端可复刻走查（判定方式：llm_assisted）   - **维度**: usability   - **评级**: 断言一致

## 想测什么

新手应能在 30 分钟内看到第一个成功运行；每一步有可验证检查点；卡壳点数量应为 0

## 做了什么

- 1. 按 00-overview 到 01-quick-start 顺序逐步操作
- 2. 每一步记录是否有可观察验证点、是否卡壳
- 3. 记录全部卡壳点（开通入口、仓库内容要求、push 后查看位置等）

- - [正向] 每步有可观察验证点
- - [负向] 不应存在文档假设用户知道但新手不知道的隐式前提（如 Action 功能开通步骤）
- - [非功能] 全流程应在 30 分钟内可完成

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | documentation | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 新手体验走查需LLM模拟 |
| 2 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 前提清单完整性确定性检查 |
