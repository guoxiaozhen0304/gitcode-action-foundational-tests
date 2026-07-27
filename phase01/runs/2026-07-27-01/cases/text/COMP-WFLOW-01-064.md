用例 ID:   COMP-WFLOW-01-064
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-366~401
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      workflow stages 阶段结构字段验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 定义含 stages 的 workflow，使用 map 格式，build stage 设 fail_fast: true，test stage 设 fail_fast: false
  2. 在 build stage 内制造一个失败 job，观察 fail_fast 是否中断后续 test stage
  3. 变体说明：缺省 stages 字段的 workflow（仅顶层 jobs）等价于单 stage，应被平台接受

预期结果:
  - stages 为 map 格式，每个 stage 含 jobs，stage 间串行执行
  - fail_fast true 时 build stage 某 job 失败将中断后续 stage，test stage 不执行，运行失败

验证点:
  - [正向] stages map 格式通过校验
  - [正向] 单 stage 可缺省 stages 字段
  - [正向] fail_fast true 时某 job 失败中断后续 stage

清理:      重置 fixture 仓库
