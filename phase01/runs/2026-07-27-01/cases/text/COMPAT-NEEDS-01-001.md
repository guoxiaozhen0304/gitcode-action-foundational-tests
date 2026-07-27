```
用例 ID:   COMPAT-NEEDS-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-041
参照来源:  inputs/github-reference/reference/contexts.md; inputs/gitcode-spec/syntax-reference/context.md; inputs/gitcode-spec/writing-pipelines/pass-output-between-jobs.md
母意图:    —（父集于 INTENT-COMPAT-NEW-006，其未声明 output 返空边界并入本组证据链）
标题:      needs 上下文存在性与 outputs/result 字段对齐（规格矛盾仲裁）

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个含上游 job 声明 output、下游 job 经 needs 引用该 output 并读取 needs 上游 result 的 workflow
  2. 触发并读取下游 job 日志中的取值

预期结果:
  - needs 上下文存在且 outputs 取值正确（GitCode 官方文档已承诺）
  - needs 上游 result 字段存在且取值与 GitHub 语义（success/failure/cancelled/skipped）对齐
  - context.md 未列 needs 的规格矛盾被记录

验证点:
  - [正向] needs 上游 outputs 取值正确
  - [正向] needs 上游 result 在上游成功时取值与 GitHub 对齐
  - [负向] 不应出现 needs 在条件表达式中不可用而文档未声明的情况

清理:      重置 fixture 仓库
```
