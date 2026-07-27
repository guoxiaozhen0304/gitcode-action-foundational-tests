```
用例 ID:   COMPAT-CTX-01-005
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-040
参照来源:  inputs/github-reference/reference/contexts.md; inputs/gitcode-spec/syntax-reference/context.md; inputs/gitcode-spec/syntax-reference/variables.md
母意图:    —（变体自 COMPAT-CTX-01-004：GitHub 有而 atomgit 表缺位的其余字段探测）
标题:      atomgit 缺位字段（job/run_attempt/triggering_actor/ref_protected）求值行为探测

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个逐一输出 atomgit.job、atomgit.run_attempt、atomgit.triggering_actor、atomgit.ref_protected 的 workflow
  2. 触发并记录各字段的求值行为（有值 / 求值为空 / 解析报错）

预期结果:
  - 各字段求值行为得到逐字记录；缺失字段清单进入迁移对照文档
  - 对照环境变量侧（如 ATOMGIT_RUN_ATTEMPT）确认上下文侧缺位是否有替代

验证点:
  - [正向] 四个缺位字段的求值行为逐一确定并记录
  - [非功能] 缺失字段清单进入迁移对照文档并回写 Parity Matrix

清理:      重置 fixture 仓库
```
