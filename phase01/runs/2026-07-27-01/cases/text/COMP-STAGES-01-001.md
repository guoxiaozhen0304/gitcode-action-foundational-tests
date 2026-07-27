用例 ID:   COMP-STAGES-01-001
维度标签:   [completeness]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-007
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      stages 阶段间串行、阶段内 job 并行执行

前置条件:
  - workflow 定义多个 stages（map 格式），每个 stage 含多个 jobs

操作步骤:
  1. 触发 workflow
  2. 各 job 步骤输出 Unix 时间戳（date +%s），使执行先后关系在日志层面可观测
  3. 比对日志时间戳：stage 2 的开始时间应晚于 stage 1 各 job 的结束时间；同 stage 内各 job 开始时间应相近

预期结果:
  - stage 1 的所有 job 完成后，stage 2 才开始
  - 同 stage 内的 jobs 并行执行

验证点:
  - [正向] stage 2 的 job 开始时间晚于 stage 1 所有 job 的结束时间
  - [正向] 同 stage 内 job 的开始时间相近（并行）

清理:      none
