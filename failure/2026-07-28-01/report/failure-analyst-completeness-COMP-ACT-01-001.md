## 失败分诊 · COMP-ACT-01-001 · action inputs.required 未传参时平台不自动校验

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED
- assertions[1] (positive, run_logs) — 期望 log contains 'REQ_INPUT_EMPTY'，实际 absent

**根因初判**: 环境问题

**责任人**: Phase 02 — 测试夹具/工作流配置问题（`repo_fixture: local-action-required` 中的本地 action `.gitcode/actions/req-check` 未正确部署或编译）

**证据**:

- **Job 日志全文**（仅 1 行）:
  ```
  [2026/07/28 13:30:20.682 GMT+08:00] [INFO] Job(1531655046779641856_1531655046746087431) duration check: true  (行 1)
  ```
  日志中**没有任何步骤执行痕迹**——没有脚本创建（`::debug::Script file created`）、没有脚本执行（`::debug::Executing:`）、没有任何 shell 输出。Job 被调度但似乎在步骤启动阶段就失败了。

- **预期行为**（用例 YAML COMP-ACT-01-001，P2，维度 completeness）:
  - 调用本地 action `./.gitcode/actions/req-check`（该 action 的 `action.yml` 中应有 `inputs.required: true` 的 input 声明）
  - 调用时**不传**该 required input
  - 期望平台允许 workflow 运行到 action 内部，在 action 内通过检查 `INPUT_*` 是否为空来验证

- **实际行为**:
  - Job 被调度（`duration check: true`），但之后立即结束——无任何步骤执行。这表明 workflow 可能在**解析/编译阶段**就失败了（例如 `uses: ./.gitcode/actions/req-check` 引用的路径不存在或其 `action.yml` 无效）
  - 被阻断的功能：无法验证平台对 `inputs.required` 未传参时的处理行为

- **Fixture 分析**:
  - 用例 YAML 第 8 行声明 `repo_fixture: local-action-required`
  - 此 fixture 需包含有效的本地 action（`.gitcode/actions/req-check/action.yml` + 配套脚本）
  - 若 fixture 未正确部署该 action 到测试仓库，`uses` 引用将失败
  - 失败模式（无任何步骤执行）与本地 action 路径不存在的典型症状一致

**置信度**: 高（零 shell 输出是路径不存在或无效引用的典型症状）

**影响**:
- **阻塞性**: 🔴阻塞 — 整个 workflow 在解析阶段失败，核心验证（required input 行为）完全未进行
- **静默性**: 🟡可察觉 — 用户可从日志中看到 job 无任何步骤执行
- **影响面**: 🟢单用例 — fixture 问题，不影响平台本身的评估
- **综合**: 阻塞但可察觉，本地 action fixture 缺失导致无法验证平台行为
- **是否有规避手段**: 是 — 检查并修复 `local-action-required` fixture 的内容

**建议**:
- Phase 02 harness 检查 `repo_fixture: local-action-required` 是否已正确定义（包含 `.gitcode/actions/req-check/` 目录及有效的 `action.yml`）
- 若 fixture 存在但编译阶段未将其推送到测试仓库，检查推送流程
- 此 FAIL 与平台能力无关，不应计入 GitCode Actions 能力边界指标
- 相关用例: COMP-ACT-01-002（同 fixture 问题模式）
