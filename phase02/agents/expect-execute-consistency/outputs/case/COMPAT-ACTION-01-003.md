# COMPAT-ACTION-01-003

- **标题**: GitHub 风格 action 引用 actions/checkout@v4 的解析域探测
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
探测 uses: actions/checkout@v4（GitHub 全名引用）在 GitCode 平台的解析结局。

## 做了什么
probe job 引用 actions/checkout@v4 后 echo "GITHUB_STYLE_REF_EXECUTED"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | save_result | positive | llm_assisted | LLM_DEPENDENT | 需人工判定保存/解析阶段的明确报错或运行成功 |
| 2 | run_status | negative | llm_assisted | LLM_DEPENDENT | 需人工判定不出现长期 queued 或模糊失败 |
| 3 | save_result | nonfunctional | llm_assisted | LLM_DEPENDENT | 需人工判定报错中映射指引的可理解性 |
