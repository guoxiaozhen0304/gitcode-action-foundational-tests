用例 ID:   SEC-TOCTOU-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-031
参照来源:  inputs/gitcode-spec/syntax-reference/runner-images-tools.md; inputs/gitcode-spec/writing-pipelines/using-script-commands.md
母意图:    —
标题:      审批后推送新 commit 不应被已授权特权运行执行

前置条件:
  - 仓库配置了审批触发 workflow

操作步骤:
  1. 管理员审批一个 workflow 运行，harness 记录审批时刻锁定的 commit SHA（approved_locked_sha）
  2. 在审批后、执行前，攻击者推送恶意 commit（post_approval_commit_sha）
  3. 观察特权运行实际执行的 commit（executed_commit_sha，从运行日志的 EXECUTED_SHA 输出提取）

预期结果:
  - 特权运行应绑定审批时刻的具体 commit SHA
  - 审批后推送的新 commit 不应被已授权的特权运行自动采用
  - 判定逻辑（harness 可确定性比对）：从运行日志提取 EXECUTED_SHA，与审批锁定的 approved_locked_sha 比对；二者相等判通过，等于 post_approval_commit_sha 判不通过

验证点:
  - [负向] 审批后推送的恶意代码绝不应被已授权特权运行执行（executed_commit_sha 绝不应等于 post_approval_commit_sha）
  - [正向] 特权运行执行的 commit 与审批时锁定的 SHA 一致（executed_commit_sha == approved_locked_sha）

清理:      重置 fixture 仓库
