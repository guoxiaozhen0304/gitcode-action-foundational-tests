# COMPAT-ENV-01-004

- **标题**: ATOMGIT_ENV 覆写系统默认变量的防护（对齐 GitHub 同名禁止）
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证通过 ATOMGIT_ENV 覆写系统变量（如 ATOMGIT_WORKSPACE）被拒绝或忽略。

## 做了什么
记录原始 WORKSPACE → 经 env 文件尝试覆写 ATOMGIT_WORKSPACE → 读取 WORKSPACE_NOW 和 CUSTOM_NOW。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | llm_assisted | LLM_DEPENDENT | 需人工判定 WORKSPACE_NOW 不等于被污染值 |
| 2 | run_logs | positive | must_contain: CUSTOM_NOW=custom-ok | COVERED | env 文件写入 CUSTOM_PROBE 后 echo 读取 |
| 3 | run_logs | positive | llm_assisted | LLM_DEPENDENT | 需人工判定覆写尝试产生警告或拒绝痕迹 |
