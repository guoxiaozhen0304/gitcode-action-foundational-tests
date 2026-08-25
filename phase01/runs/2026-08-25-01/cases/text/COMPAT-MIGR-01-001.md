用例 ID:   COMPAT-MIGR-01-001
维度标签:   ['compatibility', 'usability']
维度:      compatibility
优先级:    P0
溯源意图:  INTENT-COMPAT-028
母意图:    —
标题:      使用 GitHub Actions 语法时校验器报错应指明 GitCode 差异

前置条件:
  - 仓库 fixture:  ComputingActionTest/gitcode_api

操作步骤:
  1. 提交含 GitHub 专有语法的 workflow
  2. 观察平台校验器报错
  3. 验证报错信息是否指明 GitCode 不支持及替代写法

预期结果:
  1. 校验失败
  2. 错误信息包含 GitCode 特有替代建议或文档链接

验证点:
  - [负向] workflow 不应成功运行
  - [正向] 错误提及 actions/checkout 不支持
  - [正向] 错误提及 github 上下文不支持

清理:      none
