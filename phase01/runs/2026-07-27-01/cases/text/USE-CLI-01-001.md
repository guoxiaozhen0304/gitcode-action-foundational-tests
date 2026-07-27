用例 ID:   USE-CLI-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-045
参照来源:  inputs/gitcode-spec/security-permissions/token-permissions.md; inputs/existing-cases/cases.md 问题 sheet TC-502
母意图:    —
标题:      Runner 无 gh 等效 CLI 时迁移指引的替代方案说明

前置条件:
  - 隔离测试实例可正常调度 workflow

操作步骤:
  1. 在 Runner 上探测 gh、gitcode、atomgit 命令是否存在
  2. 检查文档迁移指引或常见问题中是否有 gh CLI 替代方案小节

预期结果:
  CLI 不存在时文档应显式说明，并给出 curl 加 ATOMGIT_TOKEN 的对照示例

验证点:
  - [正向] 记录 Runner 上各 CLI 命令的存在性
  - [负向] Runner 无等效 CLI 且文档无对应说明即不合格
  - [非功能] 从 GitHub 迁移章节应包含 gh CLI 替代方案小节

清理:      无
