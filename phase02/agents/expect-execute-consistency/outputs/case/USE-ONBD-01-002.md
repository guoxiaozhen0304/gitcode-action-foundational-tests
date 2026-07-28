# USE-ONBD-01-002  - **标题**: quick-start 示例提交后运行结果可见性检查点   - **维度**: usability   - **评级**: 断言一致

## 想测什么

push 后运行条目应在运行列表可见，状态与文档成功结果描述一致

## 做了什么

- 1. 按 quick-start 示例创建 workflow 文件并 push 到默认分支
- 2. 在文档声称的位置查看运行列表
- 3. 确认运行条目出现且结果与文档描述一致

- - [正向] workflow 运行成功
- - [正向] 运行条目在运行列表可见（可经 API 确定性判定）
- - [非功能] 从 push 到条目可见的时延应在分钟级

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=`success` | COVERED | run_status: 测试push触发+workflow调度基础设施; echo仅占位 |
| 2 | run_list | positive | eval=deterministic | COVERED | run_list+deterministic: API端点确定性判定运行条目可见 |
