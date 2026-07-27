用例 ID:   REL-DEBOUNCE-01-001
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-073
参照来源:  history/issues-encountered.md #67
母意图:    —
标题:      触发幂等——同分支 10 秒内连续 5 次 push 的 run 记录应与事件一一对账

前置条件:
  - fixture 仓库配置 push 触发的 workflow
  - harness 可在 10 秒窗口内连续推送 5 个不同 commit

操作步骤:
  1. 在同一分支 10 秒内连续 push 5 次（每次不同 commit sha）
  2. 待全部触发稳定后，拉取 run 列表与 5 个 push sha 对账

预期结果:
  - 每次 push 均能在 run 列表中找到对应 sha 的 run 记录（5/5 一一对应）；
    或平台有明确文档化的去抖窗口且对账数量与文档一致
  - 同一 sha 不被重复触发

验证点:
  - [正向] run 记录与 push 事件对账一致（5/5，或文档化去抖后的确定数量）
  - [负向] 不应出现 run 数小于 push 数且无文档化去抖说明（#67 回归点）
  - [负向] 同一 sha 不应触发 2 次

清理:      重置 fixture 仓库
