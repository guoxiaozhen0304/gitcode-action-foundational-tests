# USE-LBL-01-001  - **标题**: runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表   - **维度**: usability   - **评级**: 断言一致

## 想测什么

系统在合理超时后失败，报错包含用户指定的标签和可用 runner 类型列表

## 做了什么

- 1. 使用完全不存在的标签组合如 [nonexistent-os, x64, small]

- - [负向] 不应无限 queued 且无提示
- - [非功能] 错误信息中是否包含用户指定的标签文本

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: runs-on含不存在标签→平台无法匹配runner; 状态可观察 |
| 2 | error_message | positive | must_contain=`nonexistent-os` | COVERED | error_message+must_contain: 报错信息可验证包含标签名 |
| 3 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 报错文案质量需LLM评估 |
