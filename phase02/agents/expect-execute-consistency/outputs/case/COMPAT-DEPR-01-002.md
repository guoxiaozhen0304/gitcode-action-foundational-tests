# COMPAT-DEPR-01-002

- **标题**: ::add-path:: 废弃命令应被拒绝或给出迁移指引
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证废弃命令 ::add-path:: 在 GitCode 中被拒绝或给出迁移警告。

## 做了什么
echo '::add-path::/custom/path' 后 echo $PATH。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | llm_assisted | LLM_DEPENDENT | 需人工判定不静默忽略导致成功 |
| 2 | error_message | positive | llm_assisted | LLM_DEPENDENT | 需人工判定系统给出明确响应 |
| 3 | error_message | positive | llm_assisted | LLM_DEPENDENT | 需人工判定警告含 ATOMGIT_PATH 替代示例 |
