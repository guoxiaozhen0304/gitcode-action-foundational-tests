# COMPAT-CACHE-01-001
- **标题**: cache 行为等价性——缓存命中场景   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 uses: cache 缓存命中场景：第二次运行识别已有缓存并恢复，不丢失内容。
## 做了什么
workflow_dispatch 触发，step1 restore cache，step2 检查缓存命中（CACHE_HIT/CACHE_MISS 分支），step3 save cache（if: always()）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；第二次运行需出现 CACHE_HIT |
| 2 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应有持久化失败 |
说明：首次运行产生 CACHE_MISS 并创建缓存，第二次运行应 CACHE_HIT。步骤逻辑正确覆盖命中/未命中两条路径，但命中判定依赖 LLM 读取日志。 |
