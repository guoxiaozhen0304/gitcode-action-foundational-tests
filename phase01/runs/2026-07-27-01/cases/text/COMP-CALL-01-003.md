用例 ID:   COMP-CALL-01-003
维度标签:   [completeness, security]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-030
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/syntax-reference/trigger-events.md L204-233; inputs/workflow-samples/testorg/build_job.yaml
母意图:    —
标题:      本地路径 workflow_call 完整 secrets 映射正常执行

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库含本地被调 workflow（声明 secrets OBS_AK/OBS_SK 为 required，成功执行输出 REUSABLE_OK）
  - 仓库配置 OBS_AK/OBS_SK 占位 secret

操作步骤:
  1. 编写以 uses: ./.gitcode/workflows/reusable.yml 本地路径调用并完整映射 secrets 的 workflow
  2. 手动触发，验证被调 workflow 正常执行

预期结果:
  - 完整传参（含 secrets 映射）的本地路径调用正常执行（样本路径回归）；本地路径解析基准（调用方当前 ref）被记录

验证点:
  - [正向] 本地路径调用正常执行，被调 workflow 输出完成标记
  - [正向/记录] 本地路径解析基准（取调用方还是被调方 ref）逐字记录

清理:      重置 fixture 仓库
