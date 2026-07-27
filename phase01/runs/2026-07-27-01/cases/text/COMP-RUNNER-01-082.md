用例 ID:   COMP-RUNNER-01-082
维度标签:   [completeness, compatibility]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-029
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/manually-trigger-pipeline.md L42; configuring-images-toolchains.md
母意图:    —
标题:      flow-mapping 写法 runs-on 的处理结果裁定

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 编写 runs-on 为 flow-mapping 写法（runs-on: {ubuntu-24,x64,small}）的 workflow
  2. 尝试保存/触发，逐字记录平台处理结果

预期结果:
  - flow-mapping 写法的处理唯一确定：预期与 VALIDATION-RULES §1 实测一致（对象格式被校验拒绝）；若被特判解析为等价数组，逐字记录调度结果

验证点:
  - [正向/记录] flow-mapping 写法的实际处理（等价解析 / 报错 / 排队不匹配）逐字记录
  - [负向] 不应语法被接受但调度到非预期 Runner 且无提示

清理:      无需清理（校验期拒绝，无运行副作用）
