```
用例 ID:   COMPAT-NEEDS-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-041
参照来源:  inputs/github-reference/reference/contexts.md; inputs/gitcode-spec/writing-pipelines/pass-output-between-jobs.md
母意图:    —（变体自 COMPAT-NEEDS-01-001：上游 skipped 结局的 result 语义）
标题:      needs 上游 job 被跳过时的 result 取值语义

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个上游 job 以恒假条件跳过、下游 job 以 always 条件执行并读取 needs 上游 result 的 workflow
  2. 触发并读取下游日志中 result 取值

预期结果:
  - 上游 skipped 时 needs 上游 result 取值与 GitHub（skipped）对齐，或差异被文档化

验证点:
  - [正向] skipped 上游的 result 取值确定并与 GitHub 对齐

清理:      重置 fixture 仓库
```
