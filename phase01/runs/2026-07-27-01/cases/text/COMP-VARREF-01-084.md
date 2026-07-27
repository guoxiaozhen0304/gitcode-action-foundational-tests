用例 ID:   COMP-VARREF-01-084
维度标签:   [completeness]
维度:      完备性
优先级:    P2
溯源意图:  INTENT-COMP-032
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/workflow-samples/testorg/full_pr.yaml L28-86 (2026-07-22)
母意图:    —
标题:      ${gitcode_*} 与 ${PIPELINE_*} 非标准插值的求值行为记录

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 编写 step 中同时输出单引号保留形式与双引号 shell 展开形式的 ${gitcode_SOURCE_BRANCH}、${PIPELINE_RUN_ID}
  2. 手动触发，对比两种形式的日志输出，裁定平台是否在运行前求值 ${...} 占位符

预期结果:
  - 平台对 ${...} 风格占位符的处理确定：求值（来源上下文明确）/ 原样保留 / 报错；逐字记录运行时值

验证点:
  - [正向/记录] ${gitcode_*} 与 ${PIPELINE_*} 的实际求值结果逐字记录
  - [负向] 未求值占位符不应以字面量静默流入下游 job 参数且无提示
  - [非功能] 与 ${{ env.* }} / ${{ atomgit.* }} 混用时的行为一致性

清理:      重置 fixture 仓库
