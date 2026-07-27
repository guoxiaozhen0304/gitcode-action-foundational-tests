用例 ID:   COMP-CTX-01-054
维度标签:   [completeness, compatibility]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-020
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/manually-trigger-pipeline.md L89; runtime-environment-variables.md L74; syntax-reference/context.md L21/L291
母意图:    —
标题:      pull_request 触发下 inputs 上下文求值裁定

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库存在指向 main 的开放 PR

操作步骤:
  1. 编写 on.pull_request 的 workflow，step 中引用 inputs.pr_id（未在任何触发器声明）
  2. 通过 PR 事件触发运行，逐字记录该引用的求值结果

预期结果:
  - inputs 在非 dispatch/call 触发下的求值行为唯一确定（报错 / 空字符串 / 顶层 inputs 默认值），逐字记录并与三方文档矛盾裁定对应

验证点:
  - [正向/记录] inputs.pr_id 的实际求值结果逐字记录
  - [负向] 同一引用在不同运行间结果应一致（求值确定性）
  - [非功能] 若报错，报错应指明 inputs 不可用而非泛化表达式错误

清理:      重置 fixture 仓库（含关闭夹具 PR）
