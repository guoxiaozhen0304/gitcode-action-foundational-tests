# COMP-PR-01-005
- **标题**: 源分支更新后 pre-merge ref 指向刷新验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
源分支新增提交后 pre-merge ref 指向刷新（两次 HEAD sha 不同），PR 关闭后的解析行为被确定。

## 做了什么
1. step `Checkout merge ref again`：`uses: checkout` with ref: refs/merge-requests/1/merge
2. step `Record head sha`：`git rev-parse HEAD` 和 `echo "REF_SHA_RECORDED"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: REF_SHA_RECORDED | COVERED | echo 固定标记 |
| 2 | ref_refresh | nonfunctional | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
| 3 | stale_ref | negative | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
