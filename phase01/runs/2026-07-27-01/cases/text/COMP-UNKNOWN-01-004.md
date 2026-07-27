用例 ID:   COMP-UNKNOWN-01-004
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-021
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/workflow-samples/testorg/full_pr.yaml; actions-market.md L1317/1560/2496
母意图:    —
标题:      select 与 selected_by_default 声明时的实际行为记录

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 编写在 stage 与 job 两级声明 select: selected_by_default 的 workflow
  2. 保存并手动触发，逐字记录平台处理（校验报错 / 静默忽略 / 生效）
  3. 与 COMP-UNKNOWN-01-003 对比，判定声明与未声明是否等价

预期结果:
  - select 字段的处理方式唯一确定并逐字记录；若生效，其与 if 的求值顺序被记录

验证点:
  - [正向/记录] select: selected_by_default 的实际行为（与未声明是否等价）
  - [非功能] select 与 if 并存时的求值顺序（先 select 后 if / 反之 / 报错）
  - [负向] 不应出现字段看似声明实则被静默忽略且无提示

清理:      重置 fixture 仓库
