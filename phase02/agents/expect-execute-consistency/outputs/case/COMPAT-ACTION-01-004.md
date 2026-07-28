# COMPAT-ACTION-01-004
- **标题**: 官方文档示例 docker/build-push-action@v6 引用的可用性仲裁   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
探测官方文档示例 `docker/build-push-action@v6` 是否可用；不可用时需有明确报错及文档勘误。
## 做了什么
workflow_dispatch 触发，step 使用 uses: docker/build-push-action@v6，后续 echo `DOCKER_ACTION_REF_EXECUTED`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | save_result | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；可用则记录，不可用则保存期报错 |
| 2 | run_status | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应无限排队或模糊失败 |
