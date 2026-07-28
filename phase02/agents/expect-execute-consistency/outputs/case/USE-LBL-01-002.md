# USE-LBL-01-002  - **标题**: runs-on 标签因容量不足排队时应提示排队状态而非无可用 runner   - **维度**: usability   - **评级**: 断言一致

## 想测什么

系统提示当前无空闲 Runner，正在排队，而非报无可用 runner

## 做了什么

- 1. 触发一个使用正确标签但需要等待的 workflow

- - [非功能] 状态或日志中是否出现排队/等待字样
- - [非功能] 错误信息是否区分无匹配与容量不足

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 排队提示文案需LLM评估; 无确定性断言 |
