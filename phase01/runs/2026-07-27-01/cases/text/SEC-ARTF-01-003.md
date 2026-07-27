用例 ID:   SEC-ARTF-01-003
维度标签:   [security]
维度:      安全性
优先级:    P2
溯源意图:  INTENT-SEC-045
参照来源:  inputs/security-knowledge/issues.md §4; inputs/business-context/testing-focus.md §8
母意图:    —
标题:      宽通配打包含敏感文件名的 artifact 绝不应在无警示情况下静默成功且可被无痕下载

前置条件:
  - fixture 仓库 workspace 中含占位敏感文件名（.env.fixture、credentials.fixture，内容均为占位符，非真实凭据）

操作步骤:
  1. 触发一个以宽通配（整个 workspace）上传 artifact 的 workflow
  2. 检查运行日志/结果中是否存在针对敏感文件名的可识别警示
  3. 以另一角色下载该 artifact，确认下载行为是否留痕
  4. 检索文档是否说明该风险与推荐写法

预期结果:
  - 打包时日志/结果中存在可识别警示记录；若平台无防护，文档必须明示该风险
  - 跨角色下载行为留痕可查

验证点:
  - [负向] 含常见敏感文件名的打包绝不应在无警示的情况下静默成功
  - [负向] 含敏感文件的 artifact 绝不应可被跨角色下载而无痕
  - [非功能] 若平台无防护机制，文档必须明示风险与推荐写法（llm 辅助判定）

清理:      重置 fixture 仓库
