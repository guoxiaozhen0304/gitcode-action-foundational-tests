# COMPAT-CACHE-01-002
- **标题**: cache 行为等价性——fork PR 写隔离   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 fork PR 场景下 cache 写入被隔离或拒绝，不应覆盖主干缓存条目。
## 做了什么
PR 事件触发（trigger: pr, as: untrusted_contributor），step1 restore cache，step2 写入 fork marker 并 echo `FORK_WRITE_ATTEMPTED`（确定性断言），step3 save cache（if: always()）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | must_contain: FORK_WRITE_ATTEMPTED | GENUINE→COVERED | 步骤中 echo 该文本，确定性断言 |
| 2 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；fork 写入是否成功覆盖需 LLM 判断 cache 插件输出 |
| 3 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；需 LLM 识别 cache 插件隔离/拒绝标识 |
