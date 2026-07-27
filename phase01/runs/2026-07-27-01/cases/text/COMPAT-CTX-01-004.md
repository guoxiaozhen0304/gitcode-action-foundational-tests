```
用例 ID:   COMPAT-CTX-01-004
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-040
参照来源:  inputs/github-reference/reference/contexts.md; inputs/gitcode-spec/syntax-reference/context.md; inputs/gitcode-spec/running-pipelines/view-job-logs.md; inputs/gitcode-spec/writing-pipelines/configure-conditional-execution.md
母意图:    —（与 INTENT-COMPAT-016/017 互补：本条为前缀替换后的字段级差距）
标题:      atomgit.actor 规格自相矛盾的实测仲裁

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个在步骤中输出 atomgit.actor 的 workflow（官方另两页文档示例使用该字段，但 context.md 属性表未列出）
  2. 触发并读取日志中的求值结果

预期结果:
  - atomgit.actor 有确定行为：返回触发者用户名（与文档示例一致），或被明确定义为不支持
  - 规格自相矛盾（一处有一处无）被消除或记录为文档缺陷

验证点:
  - [正向] atomgit.actor 求值得到确定结果（触发者用户名或明确不支持）
  - [负向] 不应维持规格自相矛盾而不作任何记录

清理:      重置 fixture 仓库
```
