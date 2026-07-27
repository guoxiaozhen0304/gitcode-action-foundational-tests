用例 ID:   REL-REG-01-001
维度标签:   [reliability, completeness]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-072
参照来源:  history/issues-encountered.md #17
母意图:    —
标题:      新仓库 workflow 注册——首次 push 含合法流水线配置即应触发，无需手动再改一次

前置条件:
  - 可新建/销毁测试仓库（fixture 级）
  - 备有极简合法 workflow 文件（push 触发）

操作步骤:
  1. 新建 3 个空仓库，各首次提交推入同一条极简 workflow（push 触发）
  2. 记录每个仓库从 push 完成到 run 创建的时延
  3. 不做任何「手动再改一次 yml」的干预动作

预期结果:
  - 3/3 仓库首次 push 即创建对应 run
  - 注册延迟（push→run 创建）≤5 分钟

验证点:
  - [正向] 3/3 仓库首次 push 后 run 被创建
  - [负向] 不应出现「workflow 文件存在但 push 无任何 run 记录」的静默丢失（#17 回归点）
  - [非功能] 注册延迟 ≤5 分钟（300 秒）

清理:      重置 fixture（销毁测试仓库）
