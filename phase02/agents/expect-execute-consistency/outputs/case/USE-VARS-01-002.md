# USE-VARS-01-002
- **标题**: 变量插值双语法与 atomgit 属性名的文档清单 diff 及求值探测
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
探测遗留 `${}` 单括号插值语法是否被求值，检查文档是否列出全部插值语法与 atomgit 上下文合法属性名清单。

## 做了什么
workflow 使用 `${gitcode_SOURCE_BRANCH}` 和 `${PIPELINE_RUN_ID}` 遗留语法及 `${{ atomgit.repository }}` 标准语法。记录各语法求值情况。文档侧做属性名集合 diff。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | 检查遗留插值是否被求值并记录结果 | COVERED | eval: deterministic，日志输出可观察 → GENUINE |
| 2 | documentation | negative | 样本插值语法/属性名集合与文档 diff，未列数量为 0 | COVERED | eval: deterministic，集合 diff 可程序化 |
