## 失败分诊 · COMP-ENVCTX-01-050 · env 优先级链 step 大于 job 大于 workflow

**判定结果**: FAIL
**失败断言**:
- assertions[2] (positive, run_logs) — 期望 log contains 'WF_VAR=workflow_value'，实际 absent
- assertions[0] (positive, run_logs) — 期望 log contains 'MY_VAR=step_value'，实际 present（PASS）
- assertions[1] (positive, run_logs) — 期望 log contains 'JOB_VAR=job_value'，实际 present（PASS）

**根因初判**: 环境问题 / 需人工判断

**责任人**: 多方联合 — Phase 02 与平台方联合复查：`verify-inherit` job 是否实际运行、日志是否被采集

**证据**:

- **Job 日志全文**（共 10 行，全部来自 `verify` job）:
  ```
  MY_VAR=step_value          (行 5)
  JOB_VAR=job_value          (行 10)
  ```
  `verify` job 内的 step 级和 job 级 env 优先级均正常（step 级覆盖 job 级 → MY_VAR=step_value；job 级被 step 级覆盖后仍保持 job_value → JOB_VAR=job_value）。

  但 `verify-inherit` job（仅依赖 workflow 级 env `MY_VAR: workflow_value`，无 job/step 覆盖）的日志**不在采集结果中**。

- **Runner 元数据**: `job_count: 1`（JSON 第 14 行），但 YAML 定义了 2 个 job（`verify` 和 `verify-inherit`）

- **预期行为**（用例 YAML COMP-ENVCTX-01-050，P1，维度 completeness）:
  - step 级 env 覆盖 job 级 → MY_VAR=step_value ✓
  - job 级 env 覆盖 workflow 级 → JOB_VAR=job_value ✓
  - 无 job/step 覆盖时 fallback 到 workflow 级 → WF_VAR=workflow_value ✗（job 未执行/日志缺失）

- **实际行为**:
  - 同一 workflow 内，两个独立 job（不存在 `needs` 依赖）中仅第一个 job 的日志被采集
  - `verify-inherit` 的 workflow 级 env fallback 行为未被验证

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/context.md` 第 117-148 行和 `configure-steps.md` 第 215-216 行:
  - env 优先级文档完整，测试 YAML 精确复现了文档描述的三层覆盖模型

**置信度**: 中 — `verify-inherit` 的缺失原因不确定；已有的 `verify` job 数据完整且符合预期

**影响**:
- **阻塞性**: 🔴阻塞 — workflow 级 env fallback 的行为完全未被验证
- **静默性**: 🟡可察觉 — 日志文件明显缺少第二个 job
- **影响面**: 🟢单用例 — 直接影响本用例和类似的多 job env 优先级测试
- **综合**: 阻塞，workflow 级 env fallback 验证缺失
- **是否有规避手段**: 否 — 需先确认 `verify-inherit` 是否被平台调度执行

**建议**:
- Phase 02 排查 `verify-inherit` job 的调度状态（与 COMP-BOUND-01-087 的 crossjob 缺失模式一致，可能同属日志采集只取首个 job 的 bug）
- 平台方确认当前 run 中 `verify-inherit` 是否被成功调度及执行
- 如平台方确认 `verify-inherit` 已执行完成，则此为 harness 日志采集仅覆盖单 job 的缺陷
