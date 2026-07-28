# COMPAT-EVENT-01-001

- **标题**: GitHub 全量事件集中不受支持事件（release 等）的降级方式
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 GitCode 不支持的事件（如 release）在保存/解析阶段明确报错。

## 做了什么
on.release.types: [published]，echo "RELEASE_JOB_RAN"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | save_result | negative | llm_assisted | LLM_DEPENDENT | 需人工判定不被静默保存且无触发 |
| 2 | save_result | positive | llm_assisted | LLM_DEPENDENT | 需人工判定保存/解析报错含受支持事件清单 |
| 3 | save_result | nonfunctional | llm_assisted | LLM_DEPENDENT | 需人工判定报错指出 GitCode/GitHub 能力差异 |
