```
用例 ID:   COMPAT-PERM-01-006
维度标签:   [compatibility, security]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-053
参照来源:  inputs/github-reference/reference/workflow-syntax.md; inputs/github-reference/security/github-token.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md; inputs/gitcode-spec/writing-pipelines/workflow-file-location-structure.md
母意图:    —（与 INTENT-COMPAT-030 正交：030 为权限域命名，本条为 job 级字段存在性与覆盖语义；本用例为负向探测，permissions 块属预期报错对象）
标题:      job 级 permissions 字段的支持度与降级方式（权限不得宽于声明）

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 workflow 级声明只读权限、某 job 级声明写权限覆盖的 workflow
  2. 观察解析期响应；若被接受，进一步核验该 job 实际 TOKEN 权限与声明的关系

预期结果:
  - job 级 permissions 若支持：覆盖语义与 GitHub 对齐（替换而非并集）
  - 若不支持：解析期明确报错提示仅支持 workflow 级（平台实测为 unknown property 拒绝）
  - 不应静默忽略导致该 job 实际权限宽于声明

验证点:
  - [负向] 含 job 级 permissions 的 workflow 不应被静默接受后该 job 获得更宽权限
  - [正向] 不支持时解析期明确报错指明 job 级 permissions 不可用
  - [非功能] 覆盖语义（替换 vs 合并）文档化

清理:      重置 fixture 仓库
```
