# COMPAT-ENV-01-002

- **标题**: GITHUB_SHA 环境变量在 GitCode 中应为空或未定义
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 GITHUB_SHA 环境变量在 GitCode 中为空或未定义，不被错误映射。

## 做了什么
echo "github_sha=$GITHUB_SHA"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | llm_assisted | LLM_DEPENDENT | 需人工判定 github_sha 为空不含 40 位 SHA |
| 2 | error_message | nonfunctional | llm_assisted | LLM_DEPENDENT | 需人工判定报错提示使用 ATOMGIT_* 替代 |
