# COMP-PR-01-005

- **标题**: 源分支更新后 pre-merge ref 指向刷新验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证源分支新增提交后 pre-merge ref 指向刷新（SHA 变化），PR 合并/关闭后解析行为被记录。

## 做了什么
`on: pull_request`；step 中使用 checkout action 指定 `ref: refs/merge-requests/1/merge`，随后 `git rev-parse HEAD` 输出当前 HEAD SHA。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: REF_SHA_RECORDED | COVERED | echo 直接产生 marker |
| 2 | ref_refresh | nonfunctional | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
| 3 | stale_ref | negative | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
