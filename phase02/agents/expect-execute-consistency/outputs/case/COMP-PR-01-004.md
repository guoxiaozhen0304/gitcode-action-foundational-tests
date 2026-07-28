# COMP-PR-01-004

- **标题**: pre-merge ref 在 PR 存续期可解析且语义裁定
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `refs/merge-requests/1/merge` 在 PR 存续期可 checkout 并裁定其语义（merge commit 合并预览 vs 源分支头）。

## 做了什么
`on: pull_request`；step 中使用 checkout action 指定 `ref: refs/merge-requests/1/merge`，随后 `cat pre_merge_marker.txt` 读取夹具标记文件内容。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: PRE_MERGE_MARKER | COVERED | `cat pre_merge_marker.txt` 实际读取 checkout 的 ref 内容并输出 |
| 2 | run_logs | positive | must_contain: REF_CONTENT_DUMPED | COVERED | echo 直接产生 marker |
| 3 | ref_semantics | nonfunctional | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
