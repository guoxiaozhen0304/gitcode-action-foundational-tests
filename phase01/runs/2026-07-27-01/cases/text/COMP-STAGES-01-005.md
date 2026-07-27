用例 ID:   COMP-STAGES-01-005
维度标签:   [completeness, usability]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-019
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/manually-trigger-pipeline.md; configuring-images-toolchains.md
母意图:    —
标题:      list 形式 stages 的实际处理裁定记录

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库可写入 workflow

操作步骤:
  1. 编写 list 形式 stages（stages: - name: ... jobs: ...）的 workflow
  2. 尝试保存/触发，逐字记录平台处理结果（校验报错 / 接受并等价 / 静默忽略）

预期结果:
  - 平台处理结果唯一确定：预期与 VALIDATION-RULES §17 实测一致（校验期报错 Cannot deserialize Map from Array value）；若实际被接受，逐字记录阶段结构与执行语义

验证点:
  - [正向/记录] list 形式 stages 的实际处理结果逐字记录
  - [负向] 不应出现 stages 被接受但串行语义丢失（job 全部并行）且无任何告警
  - [非功能] 若报错，报错应定位到 stages 字段而非泛化解析错误

清理:      无需清理（校验期拒绝，无运行副作用）
