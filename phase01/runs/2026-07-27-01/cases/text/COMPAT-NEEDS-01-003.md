```
用例 ID:   COMPAT-NEEDS-01-003
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-041
参照来源:  inputs/github-reference/reference/contexts.md; inputs/gitcode-spec/writing-pipelines/pass-output-between-jobs.md
母意图:    —（变体自 COMPAT-NEEDS-01-001：matrix 上游聚合与未声明 output 边界，并入 INTENT-COMPAT-NEW-006 证据）
标题:      matrix 上游 job 的 needs outputs 聚合语义与未声明 output 边界

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个上游为 matrix job（各实例写不同 output 值）、下游经 needs 读取该 output 的 workflow
  2. 下游同时读取一个上游从未声明的 output 键
  3. 触发并记录下游观测值

预期结果:
  - matrix 上游 outputs 聚合行为可观测且确定（明确取哪个实例的值），与 GitHub（取最后完成实例）对齐或差异文档化
  - 引用未声明 output 返回空值（NEW-006 已有边界）在本场景下保持

验证点:
  - [正向] matrix 上游聚合取值确定且语义明确
  - [正向] 未声明 output 引用返回空而非报错
  - [负向] 不应出现聚合取值随机或不可复现

清理:      重置 fixture 仓库
```
