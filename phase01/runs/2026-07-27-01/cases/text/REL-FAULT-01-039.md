用例 ID:   REL-FAULT-01-039
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-082
参照来源:  history/issues-encountered.md #12/#54; platform-config/instance-config.md
母意图:    —
标题:      故障注入——排队期唯一匹配 runner 下线，job 应重调度或有界等待后明确失败

前置条件:
  - 具备实例级故障注入能力（下线指定 runner / 停 agent 进程）
  - 存在唯一匹配目标 runs-on 标签的 runner（K8s 自托管池）
  - 本用例操作实例级 runner 池，破坏级别=full_instance

操作步骤:
  1. 触发一条 job，使其处于 queued 等待目标 runner
  2. 在 queued 期间下线该唯一匹配 runner（停 agent 进程）
  3. 观察 10 分钟窗口内 job 状态流转；随后将 runner 重新上线
  4. runner 恢复后新触发一条 job，验证池自恢复接管

预期结果:
  - runner 下线后 ≤10 分钟，job 脱离 queued：重调度到其他匹配 runner，或明确报无可用资源
  - 不无限 queued 挂起
  - runner 重新上线后，新触发 job 正常调度

验证点:
  - [正向] job 在 ≤600 秒内脱离 queued（转 running 或明确失败）
  - [负向] 不应 queued 挂起 >10 分钟无任何状态变化或提示（#12/#54 回归点）
  - [正向] runner 恢复上线后新触发 job 调度成功（池自恢复）

恢复预期:  优雅降级（重调度或明确报资源不可用；runner 恢复后调度功能自动复原）
清理:      full_instance（恢复 runner 注册状态，重置实例级 runner 池）
