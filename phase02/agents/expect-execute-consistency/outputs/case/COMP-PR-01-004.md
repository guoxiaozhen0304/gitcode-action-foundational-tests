# COMP-PR-01-004
- **标题**: pre-merge ref 在 PR 存续期可解析且语义裁定
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
refs/merge-requests/1/merge 在 PR 存续期内可解析，其指向语义（merge commit 合并预览 vs 源分支头）被实测确定。

## 做了什么
1. step `Checkout merge ref`：`uses: checkout` with ref: refs/merge-requests/1/merge
2. step `Inspect content`：`cat pre_merge_marker.txt` 和 `echo "REF_CONTENT_DUMPED"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: PRE_MERGE_MARKER | COVERED | cat 输出文件内容 |
| 2 | run_logs | positive | must_contain: REF_CONTENT_DUMPED | COVERED | echo 固定标记 |
| 3 | ref_semantics | nonfunctional | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
