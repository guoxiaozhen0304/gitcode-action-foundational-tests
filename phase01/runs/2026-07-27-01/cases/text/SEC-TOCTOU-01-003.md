用例 ID:   SEC-TOCTOU-01-003
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-043
参照来源:  inputs/gitcode-spec/syntax-reference/trigger-events.md §1.4/1.5; inputs/security-knowledge/github-actions-security-series.md Part 4
母意图:    INTENT-SEC-031
标题:      评论触发后被编辑的内容绝不应改变已排队/运行中 workflow 读取的事件负载

前置条件:
  - fixture 仓库配置 issue_comment 或 pull_request_comment workflow（types 含 created 与 edited）
  - job 启动时快照触发时刻的评论内容哈希，并设有足够运行窗口供编辑竞态

操作步骤:
  1. 发表一条合规评论触发 workflow（created 事件）
  2. 在运行排队/执行期间将该评论编辑为不同内容
  3. 检查运行内读取的评论体与触发时刻快照是否一致
  4. 观察 edited 事件是否作为新事件独立重新评估

预期结果:
  - 运行内读到的是触发时刻的评论内容快照
  - 编辑后内容不出现在本次执行依据中
  - edited 再触发视为新事件重新评估，不沿用旧快照冒充原审批
  - 审计记录中的评论内容与触发时刻一致

验证点:
  - [正向] created 触发读取到触发时刻内容
  - [负向] 触发后编辑评论绝不应改变已排队/运行中 workflow 读到的事件负载
  - [非功能] 审计中评论内容与触发时刻一致

清理:      重置 fixture 仓库
