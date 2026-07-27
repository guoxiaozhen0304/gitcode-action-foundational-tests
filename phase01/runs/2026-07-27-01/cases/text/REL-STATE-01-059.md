用例 ID:   REL-STATE-01-059
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-071
参照来源:  history/issues-encountered.md #55/#19; gitcode-api/api-reference.md
母意图:    —
标题:      运行状态收敛——job 全部终态后 run 状态应在有界时间内脱离 RUNNING 且单调无抖动

前置条件:
  - fixture 仓库可触发含多并行 job 的 workflow
  - harness 可每 10 秒轮询 run/job 状态（API）

操作步骤:
  1. 触发含 3 个并行 job（各 sleep 60 秒）的 workflow
  2. 自触发起每 10 秒轮询 run 级与 job 级状态，持续 10 分钟
  3. 记录状态序列与全部 job 终态到 run 终态的收敛时延

预期结果:
  - 全部 job 进入终态后 ≤120 秒，run.status 收敛为 completed
  - run.conclusion 与 job 聚合结果一致（本组全 success → success）
  - 状态序列单调（QUEUED→RUNNING→COMPLETED），无倒退抖动

验证点:
  - [正向] run 终态 status=completed 且 conclusion=success
  - [负向] 不应出现 job 全 success 而 run 超过 10 分钟停留 in_progress（#55 回归点）
  - [非功能] 收敛时延 ≤120 秒
  - [非功能] 轮询状态序列单调，无 RUNNING↔COMPLETED 抖动（#19 回归点）

清理:      无需重置（仅状态观测）
