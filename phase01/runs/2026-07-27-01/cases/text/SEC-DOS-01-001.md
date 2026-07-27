用例 ID:   SEC-DOS-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-033
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      大 artifact / 大 cache 必须受配额与边界限制

前置条件:
  - 仓库支持 artifact 和 cache 上传

操作步骤:
  1. 提交一个 workflow，尝试上传超大 artifact 或写入超大 cache
  2. 触发 workflow 并查看上传结果

预期结果:
  - 超过大小上限的 artifact/cache 上传绝不应成功写入（运行状态绝不应为 success）
  - 超限时 job 以 failure 结束，并给出明确报错（大小限制值），不应静默截断或卡死

验证点:
  - [负向] 超过大小上限的 artifact/cache 上传绝不应成功写入（run 状态绝不应为 success）
  - [正向] 超限 job 的最终状态为 failure（job_status 可观测）
  - [非功能] 超限时应给出明确报错（大小限制值），不应静默截断或卡死

清理:      重置 fixture 仓库
