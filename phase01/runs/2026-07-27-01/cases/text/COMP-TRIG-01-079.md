用例 ID:   COMP-TRIG-01-079
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-234~560
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      触发事件 types 取值与过滤边界验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 配置 on.pull_request 的 types 为允许值（open / merge）
  2. 以 open 类型 PR 事件触发，步骤内读取当前事件 action 并判断其是否命中 types 白名单，输出判断结果
  3. 变体：将 types 配置为非法值（如 opened）提交 workflow，观察平台校验行为

预期结果:
  - pull_request types 允许 open / merge / reopen / update，合法 types 通过校验，触发事件的 action 命中白名单
  - 非法 types 变体被平台拒绝并提示允许取值
  - 未指定 types 时默认行为生效（全部类型触发）

验证点:
  - [正向] 合法 types 通过校验，触发事件的 action 命中白名单
  - [负向] 非法 types 被平台拒绝
  - [正向] 默认 types 在未指定时生效

清理:      重置 fixture 仓库
