用例 ID:   REL-SCHED-01-058
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-085
参照来源:  gitcode-spec/trigger-events.md（最短 5 分钟、UTC、仅默认分支）; parity-matrix（schedule 🟡）
母意图:    —
标题:      schedule 触发准点性与丢失率——cron 最短 5 分钟间隔下 2 小时窗口的触发可靠性

前置条件:
  - fixture 仓库默认分支配置 cron=*/5 * * * *（UTC）的 schedule workflow
  - 对照组：非默认分支配置相同 schedule
  - harness 可连续观察 2 小时并对账 run 记录

操作步骤:
  1. 在默认分支启用 */5 cron 的 schedule workflow，连续观察 2 小时（理论 24 次触发）
  2. 记录每次实际触发的 run 创建时刻与 sha，计算丢失率与触发延迟
  3. 对照组观察非默认分支是否产生任何 run

预期结果:
  - 2 小时内实际触发 ≥23 次（丢失率 ≤5%）
  - 每次触发延迟（计划时刻→run 创建）P95 ≤5 分钟；无重复触发
  - 每次 run 的 sha=默认分支 HEAD；非默认分支不产生任何 run

验证点:
  - [正向] 触发次数 ≥23/24，每次 run 的 sha=默认分支 HEAD
  - [负向] 非默认分支的 schedule 配置不应产生任何 run
  - [负向] 同一计划时刻不应触发 2 次（重复触发=0）
  - [非功能] 丢失率 ≤5%；触发延迟 P95 ≤300 秒

清理:      重置 fixture 仓库（停用 schedule 配置）
