用例 ID:   COMP-ISOLATION-01-001
维度标签:   [completeness, reliability, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-011
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      同一 workflow 先后 job 的文件系统相互隔离

前置条件:
  - workflow 含两个串行 jobs（job2 needs job1），另有 artifact 传递验证 job（job3 needs job1）

操作步骤:
  1. job 1 写入标记文件到本地路径，同时通过 artifact 显式上传共享文件
  2. job 2 尝试读取 job 1 的本地标记文件（预期不可见）
  3. job 3 通过 artifact 下载共享文件并读取（预期可见）

预期结果:
  - job 2 无法看到 job 1 写入的本地文件（文件系统隔离）
  - 显式通过 artifact 传递后，job 3 可读取共享文件内容

验证点:
  - [负向] job 2 不应访问到 job 1 的文件
  - [正向] 显式通过 artifact 传递后 job 可访问

清理:      none
