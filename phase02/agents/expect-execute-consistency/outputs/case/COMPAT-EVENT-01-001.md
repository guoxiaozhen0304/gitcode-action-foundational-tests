# COMPAT-EVENT-01-001
- **标题**: GitHub 全量事件集中不受支持事件（release 等）的降级方式   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证含 on: release 的 workflow 在保存/解析阶段明确报错（含事件不受支持说明与受支持清单），不被静默保存且永不触发。
## 做了什么
workflow `on: release: types: [published]`，job echo `RELEASE_JOB_RAN`；trigger: manual 提交探测。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | save_result | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应静默保存成功且永无触发记录 |
| 2 | save_result | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；保存/解析应明确报错含受支持事件清单 |
| 3 | save_result | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；报错应指明为 GitCode/GitHub 差异而非纯 YAML 错 |
