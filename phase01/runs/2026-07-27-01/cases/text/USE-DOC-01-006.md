用例 ID:   USE-DOC-01-006
维度标签:   ['usability']
维度:      usability
优先级:    P2
溯源意图:  INTENT-USE-034
参照来源:  inputs/gitcode-spec/syntax-reference/workflow-commands.md; inputs/gitcode-spec/syntax-reference/trigger-events.md; inputs/gitcode-spec/INDEX.md
母意图:    —
标题:      syntax-reference 章节编号连续性扫描

前置条件:
  - 文档版本为 2026-07-20 抓取版本；INDEX.md 已注明跳号系官方原文

操作步骤:
  1. 扫描 syntax-reference 下各页二级标题编号
  2. 检测编号连续性（如 5.4 之后应为 5.5）
  3. 检查跳号处是否有编号沿革说明

预期结果:
  章节号应连续；若官方确有跳号，应在跳号处显式注明沿革

验证点:
  - [负向] 存在跳号且无说明即不合格
  - [非功能] 跳号位置应补编号沿革一句话说明

清理:      无
