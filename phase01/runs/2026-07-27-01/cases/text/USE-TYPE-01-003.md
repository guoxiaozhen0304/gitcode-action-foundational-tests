用例 ID:   USE-TYPE-01-003
维度标签:   ['usability', 'compatibility']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-036
参照来源:  inputs/workflow-samples/cann/ops-nn_action.yml; inputs/gitcode-spec/syntax-reference/trigger-events.md
母意图:    —
标题:      pull_request_comment 与 pr_comment 事件名双轨的文档说明

前置条件:
  - 隔离测试实例可提交 PR 评论触发的 workflow；真实样本已就绪

操作步骤:
  1. 用样本中的别名事件名提交 workflow
  2. 记录平台是否识别该别名及触发行为
  3. 检查文档是否说明两个事件名的关系

预期结果:
  平台若接受别名，文档应显式声明等价关系；若不接受，应明确报错而非静默忽略

验证点:
  - [正向] 记录平台对别名事件名的识别情况
  - [负向] 文档只提一个事件名而样本用另一个且无任何说明即不合格

清理:      重置 fixture 仓库
