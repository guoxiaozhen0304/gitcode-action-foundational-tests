用例 ID:   REL-TIMEOUT-01-011
维度标签:   [reliability]
维度:      稳定性
优先级:    P2
溯源意图:  INTENT-REL-075
参照来源:  platform-config/README.md（default_job_timeout_minutes=360，最大值未声明）
母意图:    —
标题:      自定义 timeout 超默认值——timeout-minutes=720 的接受/拒绝语义探测

前置条件:
  - fixture 仓库可提交自定义 timeout-minutes 的 workflow
  - 平台默认 job 超时 360 分钟，最大值未公开（探测型用例）

操作步骤:
  1. 提交 job 级 timeout-minutes=720 的 workflow（探针 step 输出标记）
  2. 观察平台在解析/保存/执行阶段的行为：接受并按 720 执行，或明确报错并指出上限
  3. 若被接受，按 harness 成本约束以缩比方式验证运行可超过 360 分钟等效点（目标 370 分钟或缩比探针）

预期结果:
  - 平台行为二选一并可判定：接受（可运行超过 360 分钟）或拒绝（明确报错含上限值）
  - 实测行为回写 platform-config，闭环未公开配额

验证点:
  - [正向] 行为确定可归因：接受→超 360 仍运行；拒绝→错误信息含上限数值
  - [负向] 不应「保存成功但按 360 静默截断」（发现静默截断则本条升 P1）
  - [非功能] 探测结果（接受/拒绝/上限值）记录完整，可回写 platform-config

清理:      无需重置（探测型，无破坏性副作用）
