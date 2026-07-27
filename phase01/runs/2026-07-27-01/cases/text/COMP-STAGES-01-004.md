用例 ID:   COMP-STAGES-01-004
维度标签:   [completeness, usability]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-019
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/workflow-file-location-structure.md L88
母意图:    —
标题:      map 形式 stages 按定义顺序串行执行（回归保护）

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库可写入 workflow

操作步骤:
  1. 编写 map 形式 stages（build_stage 先于 test_stage）的 workflow 并推送
  2. 手动触发运行，观察两个 stage 的执行顺序与日志时间戳

预期结果:
  - workflow 运行成功，两个 stage 的 job 均执行
  - stage 二不早于 stage 一完成（串行语义保持）

验证点:
  - [正向] 两个 stage 的 job 均运行成功并输出标记
  - [正向] stage 按定义顺序串行（日志时间戳可证）
  - [负向] 不应出现 stage 顺序被打乱或全部并行且无说明

清理:      重置 fixture 仓库
