```
用例 ID:   COMPAT-EXPR-01-015
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-036
参照来源:  inputs/github-reference/reference/expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md
母意图:    —（与 INTENT-COMPAT-006 互补：006 为文档未明，本条为两侧文档直接矛盾）
标题:      startsWith/endsWith 大小写敏感性两侧文档矛盾的差异确认

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 workflow，在步骤中以混合大小写调用 startsWith 与 endsWith 表达式并输出求值结果
  2. 触发该 workflow，读取日志中的求值结果
  3. 将实测结果与两侧文档声明（GitHub 不区分大小写 / GitCode 文档声明区分大小写）逐一比对

预期结果:
  - GitCode 实测求值结果得到确定结论，且与其自身文档声明一致，或实测与文档的矛盾被记录为缺陷
  - 若确认为有意差异（区分大小写），该结论回写 Parity Matrix 并在迁移指引中显式声明

验证点:
  - [正向] startsWith('Hello World', 'hello') 的实测求值与 GitCode 文档（区分大小写则应为 false）一致
  - [正向] endsWith 对大小写不同后缀的求值结果与文档声明一致
  - [负向] 不应出现文档声明与实际求值不一致且无任何记录的情况
  - [非功能] 差异确认结论回写 Parity Matrix 作为该点权威 oracle

清理:      重置 fixture 仓库
```
