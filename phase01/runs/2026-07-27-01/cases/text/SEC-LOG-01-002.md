用例 ID:   SEC-LOG-01-002
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-040
参照来源:  inputs/security-knowledge/issues.md §3; inputs/gitcode-spec/running-pipelines/view-job-logs.md
母意图:    —
标题:      导出/历史日志副本中 secret 原值命中数必须为 0，遮蔽状态不可回退

前置条件:
  - fixture 仓库配置 secret DEPLOY_TOKEN（占位值）
  - 存在引用过该 secret 的当前 run 与历史 run（历史 run 产生于 secret 轮换前）

操作步骤:
  1. 下载当前 run 与历史 run 的日志导出件
  2. 对所有日志副本全文搜索 DEPLOY_TOKEN 原值
  3. 对历史 run 执行 rerun，确认新日志不复活已失效信息

预期结果:
  - 所有日志副本（含导出件）中 secret 原值命中数为 0
  - 历史日志的遮蔽状态不随后续操作回退
  - rerun 新日志不出现已失效 secret 的明文

验证点:
  - [正向] 日志可正常下载导出
  - [负向] 任何日志副本（含导出件与历史日志）中 secret 原值命中数绝不应大于 0

清理:      重置 fixture 仓库
