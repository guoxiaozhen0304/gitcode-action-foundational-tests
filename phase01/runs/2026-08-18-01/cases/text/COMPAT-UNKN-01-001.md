用例 ID:   COMPAT-UNKN-01-001
维度标签:   ['compatibility', 'usability']
维度:      compatibility
优先级:    P1
溯源意图:  INTENT-COMPAT-002
母意图:    —
标题:      含未知顶层字段的 YAML 应给出精确字段路径与有效值提示

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 提交含 permissions 未知字段的 workflow
  2. 观察校验器报错
  3. 验证报错是否给出字段路径与 GitCode 替代方案

预期结果:
  1. 校验失败并指出 permissions 字段未知
  2. 提示删除 permissions 或使用其他机制

验证点:
  - [负向] workflow 不应成功运行
  - [正向] 错误提及 permissions 字段

清理:      none
