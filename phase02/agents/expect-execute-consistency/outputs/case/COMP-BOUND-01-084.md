# COMP-BOUND-01-084

- **标题**: 路径与分支过滤组合及否定模式边界验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 push 触发时 `branches` 与 `paths` 组合过滤（含 `!` 否定模式）的正确性：命中肯定模式且未被排除时触发，仅命中否定模式时不触发。

## 做了什么
workflow 的 `on.push` 配置了组合过滤（branches: main, feature/**, !feature/experimental；paths: src/**, !src/docs/**）。step 使用 `${{ atomgit.ref }}` 输出触发上下文。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | push 触发命中肯定模式且未被排除，workflow 执行成功 |
| 2 | run_logs | positive | must_contain: TRIGGER_REF=refs/ | COVERED | `echo "TRIGGER_REF=${{ atomgit.ref }}"` 直接产生 |
| 3 | run_logs | negative | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言，排除侧观测由 harness 单独执行 |
