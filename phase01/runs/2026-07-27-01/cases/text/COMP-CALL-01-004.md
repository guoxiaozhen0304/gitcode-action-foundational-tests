用例 ID:   COMP-CALL-01-004
维度标签:   [completeness, security]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-030
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/syntax-reference/trigger-events.md L204-233
母意图:    —
标题:      未传 required secret 的 workflow_call 不应空值执行

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库含本地被调 workflow（声明 secrets required，若执行上传会输出 UPLOAD_DONE）

操作步骤:
  1. 编写本地路径调用但不传 required secret 的 workflow
  2. 保存并手动触发，逐字记录处理结果（校验报错 / 运行期空值 / 静默通过）

预期结果:
  - 调用方未传 required secret 时应在校验/调度期明确失败并指明缺失项；不应以空 secret 静默进入被调 workflow 执行

验证点:
  - [负向] 未传 required secret 时不应以空值静默进入执行
  - [负向] 不应出现以空 secret 执行副作用（如空 OBS_AK 上传）
  - [非功能] 缺参报错信息应指明缺失的 secret 名

清理:      重置 fixture 仓库
