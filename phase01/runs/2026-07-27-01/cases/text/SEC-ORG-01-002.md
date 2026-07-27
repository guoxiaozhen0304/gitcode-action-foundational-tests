用例 ID:   SEC-ORG-01-002
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-039
参照来源:  inputs/gitcode-spec/security-permissions/using-secrets.md; inputs/history/issues-encountered.md #51
母意图:    —
标题:      fork PR 触发的运行绝不应读取组织级 secret（与项目级同等隔离）

前置条件:
  - 组织级 secret ORG_SHARED_KEY（占位值）可见范围包含主仓
  - 存在一个来自外部 fork 的 PR

操作步骤:
  1. 以外部 fork 贡献者身份提交一个引用 ORG_SHARED_KEY 并试图输出的 workflow
  2. 在 fork PR 场景下触发该 workflow
  3. 全文搜索运行日志中的 secret 原值

预期结果:
  - fork PR 路径下组织级 secret 与项目级 secret 同等隔离
  - workflow 拿不到该值，日志中原值命中数为 0

验证点:
  - [正向] 主仓 maintainer 触发的运行可正常引用组织级 secret
  - [负向] fork PR 触发的运行绝不应读到组织级 secret 原值，日志命中数为 0

清理:      重置 fixture 仓库
