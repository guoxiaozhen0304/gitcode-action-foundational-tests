# COMPAT-ACTION-01-004

- **标题**: 官方文档示例 docker/build-push-action@v6 引用的可用性仲裁
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
探测官方文档示例 docker/build-push-action@v6 在 GitCode 的可用性。

## 做了什么
probe job 引用 docker/build-push-action@v6 后 echo "DOCKER_ACTION_REF_EXECUTED"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | save_result | positive | llm_assisted | LLM_DEPENDENT | 需人工判定文档示例可用性 |
| 2 | run_status | negative | llm_assisted | LLM_DEPENDENT | 需人工判定不出现无限排队或模糊失败 |
