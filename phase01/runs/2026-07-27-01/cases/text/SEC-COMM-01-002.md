用例 ID:   SEC-COMM-01-002
维度标签:   [security, compatibility]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-042
参照来源:  inputs/gitcode-spec/syntax-reference/trigger-events.md §1.5; inputs/gitcode-spec/COMPAT-NOTES.md
母意图:    INTENT-SEC-026
标题:      引用/反讽/代码块内嵌指令文本绝不应造成 pull_request_comment 预期外触发

前置条件:
  - fixture 仓库配置 pull_request_comment workflow，comments 过滤的配置意图为「精确指令评论触发」
  - 存在一个 PR 供评论

操作步骤:
  1. 依次在 PR 下发表语义边界评论：引用块内包含指令文本（如「请不要执行某指令」）、代码块内嵌指令文本、反讽语句
  2. 发表一条符合配置意图的精确指令评论作为对照
  3. 统计各类评论的触发结果

预期结果:
  - 精确指令评论正常触发
  - 引用/反讽/代码块内嵌指令文本造成预期外触发的次数为 0
  - 触发记录可回溯到匹配的具体评论内容（审计断言挂靠 SEC-AUDIT-01-001）

验证点:
  - [正向] 符合配置意图的精确指令评论正常触发
  - [负向] 引用/反讽/代码块内嵌指令文本绝不应造成预期外触发
  - [非功能] 每次触发可回溯到具体评论内容

清理:      重置 fixture 仓库
