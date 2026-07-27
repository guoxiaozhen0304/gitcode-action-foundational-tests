用例 ID:   REL-DEBOUNCE-01-002
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-073
参照来源:  history/issues-encountered.md #67
母意图:    REL-DEBOUNCE-01-001（变体：批量 tag 推送的触发对账）
标题:      触发幂等——10 秒内推送 10 个 tag 的 run 记录应与 tag 事件 100% 可解释

前置条件:
  - fixture 仓库配置 tag 推送触发的 workflow
  - harness 可在 10 秒窗口内批量创建并推送 10 个 tag

操作步骤:
  1. 在 10 秒内连续推送 10 个不同 tag
  2. 待全部触发稳定后，拉取 run 列表与 10 个 tag 事件对账

预期结果:
  - 每个 tag 事件均能对应到 run 记录（10/10），或平台有文档化的去抖/合并语义且数量一致
  - 无重复触发、无无法解释的丢失

验证点:
  - [正向] run 创建与 tag 事件对账 100% 可解释（10/10 或文档化去抖后的确定数量）
  - [负向] 不应出现 tag 事件无对应 run 且无文档说明（#67 回归点）
  - [负向] 同一 tag 不应触发 2 次

清理:      重置 fixture 仓库
