用例 ID:   COMP-PR-01-004
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-033
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/actions-market.md; inputs/workflow-samples/testorg (2026-07-22)
母意图:    —
标题:      pre-merge ref 在 PR 存续期可解析且语义裁定

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库存在开放 PR（编号固定为 1），源分支含标记文件 pre_merge_marker.txt（内容 PRE_MERGE_MARKER）

操作步骤:
  1. 编写 on.pull_request 的 workflow，checkout ref 指定 refs/merge-requests/1/merge
  2. 通过 PR 事件触发，验证 checkout 成功并检查取到的代码内容
  3. 裁定该 ref 指向语义（merge commit 合并预览 vs 源分支头）

预期结果:
  - 该 ref 在 PR 存续期内可解析；其指向语义被实测确定并逐字记录；不应出现解析成功但内容为陈旧合并结果而无标识

验证点:
  - [正向] PR 打开状态下 checkout 该 ref 成功
  - [正向/记录] 取到的代码内容符合实测裁定的语义（逐字记录）
  - [负向] 不应 ref 解析成功但内容为陈旧合并结果而无任何标识

清理:      重置 fixture 仓库（含关闭夹具 PR）
