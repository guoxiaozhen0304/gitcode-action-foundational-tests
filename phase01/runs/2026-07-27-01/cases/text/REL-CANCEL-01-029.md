用例 ID:   REL-CANCEL-01-029
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-070
参照来源:  history/issues-encountered.md #10; gitcode-api/api-reference.md（run 取消端点）
母意图:    —
标题:      多并发 run 中取消指定 run——取消应按 run_id 寻址而非栈序误杀最新一条

前置条件:
  - fixture 仓库可对同一 workflow 触发多条并发 run
  - harness 可通过 API 按 run_id 发起取消

操作步骤:
  1. 对同一 workflow 连续触发 3 条并发 run（RUN-1/RUN-2/RUN-3，单 job sleep 300 秒）
  2. 触发后 30 秒，通过 API 按 run_id 取消中间的 RUN-2
  3. 观察三条 run 至终态

预期结果:
  - RUN-2 状态=canceled
  - RUN-1/RUN-3 不受干扰，继续运行至 completed(success)

验证点:
  - [正向] RUN-2 状态=canceled
  - [正向] RUN-1/RUN-3 状态=success
  - [负向] RUN-1/RUN-3 不应被取消或中断；取消不应作用于「最新一条」而非指定 run_id（#10 回归点）
  - [非功能] 取消请求到 RUN-2 终态稳定 ≤60 秒

清理:      重置 fixture 仓库
