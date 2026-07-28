## 失败分诊 · COMP-ACT-01-002 · 含连字符 input_id 的 INPUT_ 环境变量命名裁定

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED
- assertions[1] (positive, run_logs) — 期望 log contains 'INPUT_DRY'，实际 absent

**根因初判**: 环境问题

**责任人**: Phase 02 — 测试夹具问题（`repo_fixture: local-action-hyphen` 中的本地 action `.gitcode/actions/hyphen-input` 未正确部署或编译）

**证据**:

- **Job 日志全文**（仅 1 行）:
  ```
  [2026/07/28 13:30:31.370 GMT+08:00] [INFO] Job(1531655091641790464_1531655091616624647) duration check: true  (行 1)
  ```
  与 COMP-ACT-01-001 完全相同的失败模式：Job 被调度后无任何步骤执行，零 shell 输出。

- **预期行为**（用例 YAML COMP-ACT-01-002，P2，维度 completeness）:
  - 调用本地 action `.gitcode/actions/hyphen-input`，传入含连字符的 `dry-run: "yes"`
  - 验证 `INPUT_` 环境变量的命名裁定（连字符 `-` 如何转换为环境变量名中的字符）
  - 第 38-39 行标注为非功能性验证（`nonfunctional` + `llm_assisted`）：逐字记录实际注入的环境变量名

- **实际行为**:
  - Job 被调度后立即失败，未进入任何步骤执行
  - 失败模式与 COMP-ACT-01-001 一致：零步骤执行 → `uses: ./.gitcode/actions/hyphen-input` 引用可能无法解析

- **Fixture 分析**:
  - 用例 YAML 第 8 行声明 `repo_fixture: local-action-hyphen`
  - 此 fixture 需包含 `.gitcode/actions/hyphen-input/action.yml` 定义（含 `inputs.dry-run`）
  - 失败模式强烈指向该 fixture 未正确部署/编译

**置信度**: 高（与 COMP-ACT-01-001 一致的零步骤执行模式，fixture 问题是唯一合理解释）

**影响**:
- **阻塞性**: 🔴阻塞 — 整个 workflow 在解析阶段失败，命名裁定验证完全未进行
- **静默性**: 🟡可察觉 — 用户可从日志中看到 job 无步骤执行
- **影响面**: 🟢单用例 — fixture 问题
- **综合**: 阻塞但可察觉，本地 action fixture 缺失
- **是否有规避手段**: 是 — 检查并修复 `local-action-hyphen` fixture

**建议**:
- 与 COMP-ACT-01-001 合并排查所有 `local-action-*` 系 fixture 的部署状态
- 此 FAIL 与平台能力无关
- 相关用例: COMP-ACT-01-001
