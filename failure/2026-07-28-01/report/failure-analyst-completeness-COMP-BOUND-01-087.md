## 失败分诊 · COMP-BOUND-01-087 · 步骤输出与跨 job 传递边界验证

**判定结果**: FAIL
**失败断言**:
- assertions[3] (positive, run_logs) — 期望 log contains 'DECLARED=val1'，实际 absent
- assertions[4] (positive, run_logs) — 期望 log contains 'UNDECLARED=[]'，实际 absent
- assertions[0] (positive, run_logs) — 期望 log contains 'K1=val1'，实际 present（PASS）
- assertions[1] (positive, run_logs) — 期望 log contains 'K2=val2'，实际 present（PASS）
- assertions[2] (positive, run_logs) — 期望 log contains 'output_ok'，实际 present（PASS）
- assertions[5] (negative, run_logs, leak) — 期望 plaintext 'UNDECLARED=[val2]' 0 hits，实际 0（PASS）

**根因初判**: 环境问题 / 需人工判断

**责任人**: 多方联合 — Phase 02 与平台方联合复查：crossjob 是否实际启动、日志是否被采集

**证据**:

- **Job 日志全量**（共 11 行，全部来自 `verify` job）:
  ```
  K1=val1                   (行 9)
  K2=val2                   (行 10)
  output_ok                 (行 11)
  ```
  `verify` job 内步骤间输出传递正常（K1/K2/output_ok 均出现在此 job 日志）。但**整个日志文件中没有任何 `crossjob` 的输出**。

- **Runner 元数据**: `job_count: 1`（JSON 第 14 行），但 YAML 定义了 2 个 job（`verify` 和 `crossjob`）。说明 `crossjob` 要么未调度、要么调度失败了、要么其日志未被采集。

- **预期行为**（用例 YAML COMP-BOUND-01-087，P1，维度 completeness）:
  - Job `verify` 内步骤间输出传递并读取 K1/K2
  - Job `crossjob`（`needs: verify`）通过 `needs.verify.outputs.key1` 读取已声明的 key1=val1，通过 `needs.verify.outputs.key2` 测试未声明的 key2 应为空

- **实际行为**:
  - `verify` job 成功完成（断言 0/1/2 均 PASS）
  - `crossjob` 没有任何日志输出，无法验证跨 job 的输出边界
  - 被阻断的功能：跨 job 输出传递（声明 key 可读、未声明 key 应该为空/不可读）

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/pass-output-between-jobs.md`:
  - 第 29-44 行给出完整的跨 job 输出传递示例（`outputs` + `needs.<job_id>.outputs.<key>`），测试 YAML 的写法（`outputs: key1: ${{ steps.writer.outputs.key1 }}` + `needs: verify` + `${{ needs.verify.outputs.key1 }}`）与此精确对应
  - 文档第 34 行示例明确展示 `outputs: version: ${{ steps.version.outputs.version }}`

**置信度**: 中 — `crossjob` 的缺失原因不确定（是平台未调度、调度失败、还是日志采集遗漏）

**影响**:
- **阻塞性**: 🔴阻塞 — crossjob 未执行/未采集导致跨 job 输出传递的验证完全未进行
- **静默性**: 🟡可察觉 — 日志中明显缺少 crossjob 部分，但原因不明确
- **影响面**: 🟢单用例 — 直接影响本用例和类似的跨 job 传递用例
- **综合**: 阻塞，crossjob 缺失使跨 job 输出边界验证无法完成
- **是否有规避手段**: 否 — 无法从现有信息中判断是平台调度问题还是 harness 采集问题，需先排查

**建议**:
- Phase 02 检查 crossjob 的调度状态（是否被平台接受、job_id 是否生成、是否在 queue 中）
- 如果 crossjob 实际已运行，排查日志采集链路是否只采集了第一个 job
- 平台方确认 `needs` 依赖链是否正常工作（verify COMPLETED 后是否触发 crossjob）
