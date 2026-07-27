```
用例 ID:   COMPAT-LIMIT-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P2
溯源意图:  INTENT-COMPAT-052
参照来源:  inputs/github-reference/reference/events.md（push 批量上限）; inputs/gitcode-spec/syntax-reference/trigger-events.md
母意图:    —（与 INTENT-COMPAT-012 同属平台限额子类）
标题:      单次推送多个 tag 的事件生成上限行为（GitHub 超过 3 个不生成事件）

前置条件:
  - 仓库已启用 GitCode Action，配置 tag 推送触发的 workflow

操作步骤:
  1. 单次推送 4 个 tag 到仓库
  2. 观察事件生成与运行记录数量

预期结果:
  - 触发行为确定（全部触发 / 部分触发 / 不触发）且与文档一致；超限时不应静默丢弃事件且无任何记录
  - GitCode 对应限额（或明确无限额）文档化

验证点:
  - [正向] 推送 4 个 tag 的触发行为确定并与文档比对
  - [负向] 超限场景不应静默丢事件且无任何记录

清理:      重置 fixture 仓库
```
