用例 ID:   COMP-BOUND-01-087
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-331~333
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      步骤输出与跨 job 传递边界验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 在 step 中通过 ATOMGIT_OUTPUT 写入输出（key1 / key2 两个键值对）
  2. 在同 job 后续 step 中引用 steps.id.outputs
  3. 在 job outputs 中仅映射 key1，下游 job 通过 needs 引用已声明的 key1 与未声明的 key2

预期结果:
  - ATOMGIT_OUTPUT 写入的键值对可在同 job 后续 step 中通过 steps.id.outputs 引用
  - 跨 job 引用时仅 job outputs 中声明的键可传递，未声明的键引用为空

验证点:
  - [正向] ATOMGIT_OUTPUT 写入后同 job 可读取
  - [正向] 多行输出值被正确处理
  - [负向] 跨 job 未声明 outputs 时引用为空

清理:      重置 fixture 仓库
