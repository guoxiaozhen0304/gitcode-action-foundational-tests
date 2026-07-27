用例 ID:   USE-DOC-01-007
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-043
参照来源:  inputs/gitcode-spec/security-permissions/using-secrets.md; inputs/existing-cases/cases.md 问题 sheet TC-010
母意图:    —
标题:      environment 字段能力描述存在而语法参考缺失及平台报错指引

前置条件:
  - 隔离测试实例可提交 workflow；文档版本为 2026-07-20 抓取版本

操作步骤:
  1. 检查 using-secrets.md 环境级 Secret 能力描述与语法参考中 environment 字段条目的对应关系
  2. 提交含 environment 字段的 workflow，记录平台报错信息

预期结果:
  文档能力描述与语法参考应一一对应；平台对未识别字段的报错应给出是否未来支持的指引

验证点:
  - [负向] 能力描述存在但语法参考缺失即不合格
  - [非功能] 平台报错信息应包含该字段是否未来支持的指引

清理:      无
