用例 ID:   USE-DOC-01-004
维度标签:   ['usability']
维度:      usability
优先级:    P0
溯源意图:  INTENT-USE-033
参照来源:  inputs/gitcode-spec/syntax-reference/workflow-commands.md
母意图:    —
标题:      workflow-commands 多行输出示例漏写重定向照抄得空输出

前置条件:
  - 隔离测试实例可正常调度 workflow

操作步骤:
  1. 按 workflow-commands.md 多行输出示例照抄编写 step（不写重定向）
  2. 在后续 step 读取该输出并打印
  3. 比对读取结果与文档声称的输出行为

预期结果:
  照抄文档示例应得到文档声称的多行输出；若得到空输出，则示例漏写关键重定向行（示例缺陷）

验证点:
  - [正向] 照抄示例后读取到的输出值应为空，实证示例缺少重定向
  - [负向] 文档示例不应省略会导致行为相反的关键行；如省略应显式标注

清理:      无
