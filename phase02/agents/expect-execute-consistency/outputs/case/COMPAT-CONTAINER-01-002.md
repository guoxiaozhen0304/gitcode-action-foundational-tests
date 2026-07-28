# COMPAT-CONTAINER-01-002
- **标题**: container 自定义镜像被拒绝时应给出替代指引   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证自定义 container image 被拒绝时给出替代方案（使用默认 Runner 或 runs-on 标签）。
## 做了什么
workflow_dispatch 触发，container.image: myregistry.com/build-env:v1, options:--cpus 1，step echo `hello`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | validation_error | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；报错应说明自定义镜像不支持 |
| 2 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；报错应给出替代方案（默认 Runner/runs-on） |
