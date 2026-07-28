# USE-INPT-01-002  - **标题**: 使用 boolean 类型 input 时报错应提示仅支持 string   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

YAML 校验报错，明确说明 GitCode 仅支持 string 类型，并给出转换指引

## 做了什么

- 1. 声明 workflow_dispatch inputs 的 type: boolean

- - [负向] 不应静默降级为 string
- - [非功能] 报错中应包含 string 与类型转换相关提示

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: type:boolean畸形YAML→平台应拒绝; 状态可观察 |
| 2 | error_message | positive | must_contain=`string` | COVERED | error_message+must_contain: 错误信息从校验日志获取 |
| 3 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 报错文案质量需LLM评估 |
