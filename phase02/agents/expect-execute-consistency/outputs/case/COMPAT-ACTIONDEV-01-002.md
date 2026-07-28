# COMPAT-ACTIONDEV-01-002
- **标题**: action 运行时 runs.using 类型覆盖（node16/composite/docker/node20）探测   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
探测 GitCode 支持哪些 runs.using 类型（node16/composite/docker/node20），不支持的类型应加载期报错而非运行期模糊失败。
## 做了什么
repo_fixture: with-local-actions，workflow_dispatch 触发，依次引用四种本地 action，最后 echo `USING_PROBE_DONE`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；rubric 需 LLM 逐一判定四种 runtime 的响应 |
| 2 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不支持类型不应模糊失败 |
| 3 | run_logs | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；运行清单写入差异文档 |
