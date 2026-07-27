```
用例 ID:   COMPAT-PR-01-010
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-039
参照来源:  inputs/github-reference/reference/events.md; inputs/gitcode-spec/syntax-reference/trigger-events.md
母意图:    —（变体自 COMPAT-PR-01-009：合并冲突 PR 的触发策略；与 INTENT-COMP-033 共享夹具）
标题:      存在合并冲突的 PR 的触发行为（GitHub 不触发）对齐确认

前置条件:
  - fixture 仓库存在一个与 main 有合并冲突的开放 PR

操作步骤:
  1. 向该冲突 PR 推送更新，制造 pull_request update 活动
  2. 观察是否产生 workflow 运行记录

预期结果:
  - 触发行为与 GitHub 对齐（合并冲突时不触发），或差异被明确文档化
  - 不应跑在一个无法合并的状态上而对外呈现正常 CI 结果且无任何说明

验证点:
  - [正向] 冲突 PR 的触发行为得到确定结论并与 GitHub（不触发）比对
  - [负向] 若触发，其运行不应被当作正常 PR 验证结果且无差异说明

清理:      重置 fixture 仓库
```
