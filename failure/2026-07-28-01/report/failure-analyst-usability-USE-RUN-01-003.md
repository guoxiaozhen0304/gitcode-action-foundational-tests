## 失败分诊 · USE-RUN-01-003 · rerun 上限与 6 小时时限在 UI 的明示（判定方式：llm_assisted）

**判定结果**: FAIL

**失败断言**: assertions[0] (positive, status) — 期望 all job/step green，实际 job 'failing job for rerun probe' status=FAILED。此断言是系统 fallback 产物（见证据），非 YAML 原始断言。

**根因初判**: 编译缺口

**责任人**: Phase 01 — `compile_asserts.py` 无法编译 `target: ui` + `eval: llm_assisted` 的断言，将其降级为 needs_review。该 needs_review 断言在引擎执行时被 fallback 为 `[{"kind": "status"}]`，对故意设计为失败（`exit 1`）的用例产生假 FAIL。

**证据**:

- **Job 日志全量**（5 行，含 shell 执行证据）:
  ```
  [2026/07/28 13:28:23.807 GMT+08:00] [INFO] Job(1531654556755038208_1531654556734066689) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: /home/slave1/runner/workers/0.0.4.4.version/_temp/49e20012-dfa4-4821-b426-d06da1294670.sh
  ::debug::Executing: bash -e /home/slave1/runner/workers/0.0.4.4.version/_temp/49e20012-dfa4-4821-b426-d06da1294670.sh
  ::error::Process exited with code 1
  ```
  Job 正常执行了 `exit 1` 步骤，如预期失败。Job 日志完整，有 runner 调试信息 + shell 执行痕迹 + 退出码。

- **断言编译链路**（证明 fallback 退化）:
  1. YAML 原始断言 (`phase02/agents/valid-classify/output/VALID/USE-RUN-01-003.yaml` 第 34-37 行):
     ```yaml
     - type: nonfunctional
       target: ui
       eval: "llm_assisted"
       rubric: "用户在不查文档的情况下，通过 UI 自身即可理解为什么不能重跑..."
     ```
  2. `compile_asserts.py` 处理路径 (`phase02/scripts/compile_asserts.py`):
     - 第 42-46 行: `_NO_DATASOURCE_TARGETS` 包含 `"run_ui"` / `"ui_layout"` / `"ui_visual"`，但**不包含** `"ui"` → `target: ui` 未被拦截
     - 第 48-171 行: `target: ui` 不匹配任何明确的编译规则（非 run_status/job_status/step_status/run_logs/计时/制品家族）
     - 第 173-175 行: `atype == "nonfunctional"` → **return None** → 进入 needs_review
  3. `assertion_engine.py` 执行时 (`phase02/scripts/run_case.py` 第 232 行):
     ```python
     engine_asserts = asserts if asserts else [{"kind": "status"}]
     ```
     因编译产物为空 → fallback 为 `[{"kind": "status"}]`
  4. `[{"kind": "status"}]` 在 `assertion_engine.py` 第 140-143 行: 要求所有 job/step 为绿 (COMPLETED/SUCCESS)
  5. 但该 job 名称就是 "failing job for rerun probe" 且 step 执行 `exit 1` ——**设计上就应该失败**，失败后才能测试 rerun UI 功能

- **预期行为**（Phase 01 文本用例 USE-RUN-01-003，P1，usability）:
  - 操作步骤 1: "对同一失败运行连续重跑直至达到上限"
  - 操作步骤 2: "观察重跑按钮置灰时的悬停提示与运行详情页信息"
  - 操作步骤 3: "对超过 6 小时的运行观察按钮状态与提示"
  - 预期结果: "重跑不可用时按钮应有 tooltip 明示原因；运行详情页应显示已重跑次数与剩余次数"
  - 验证点: "[正向] 达到 3 次上限后按钮置灰且悬停提示已达最大重跑次数"、"[正向] 超过 6 小时的运行按钮置灰且悬停提示时限原因"、"[非功能] 运行详情页应显示当前已重跑次数"
  - **注意: 用例的操作步骤是关于 rerun UI 行为，不要求初始运行成功。`exit 1` 是有意为之的前置条件。**

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/running-pipelines/rerun-failed-jobs.md`:
  - 第 29-33 行「重新运行限制」表: "单条运行最多重新运行 3 次"、"超过 6 小时的运行不可重新运行"
  - 第 11-13 行「重新运行整条流水线」: "进入运行详情页，点击右上角 Re-run all jobs 按钮"
  - 第 16-19 行「重新运行失败 job」: "点击右上角 Re-run failed jobs 按钮"
  - **文档描述了限制规则和操作方式，但未承诺 UI 会提供 tooltip 或次数显示。** 用例的验证点（tooltip 明示原因、显示已重跑次数）超出了文档承诺，属于可用性启发式验证。

**置信度**: 高（编译链路可精确追溯：YAML → compile_asserts.py needs_review → fallback status → 假 FAIL。每条退化步骤在源码中有明确行号。）

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为正常，Job 按设计正确执行了 `exit 1` 并返回 FAILED。
- **静默性**: 🟡可察觉 — FAIL 判定会出现在报告中，用户可以看到这是 fallback 断言的结果；但根源（编译缺口）并非用户直接可见。
- **影响面**: 🟢单用例 — 当前仅影响 USE-RUN-01-003；但**所有使用 `eval: llm_assisted` + `target: ui`（或类似非确定性 target）的用例都面临同样的 fallback 退化风险**。
- **综合**: 无影响但假 FAIL——compiler 缺 `target: ui` 映射，导致 llm_assisted 断言被 fallback 为 status 检查，对故意失败的设计用例产生假阳性。
- **是否有规避手段**: 否 — 当前 harness 无机制将 llm_assisted UI 断言标记为"需人工判定"而非 fallback 为 status。需 compile_asserts.py 补映射或 assertion_engine 调整 fallback 策略。

**建议**:
- `compile_asserts.py` 的 `_NO_DATASOURCE_TARGETS`（第 42-44 行）应将 `"ui"` 加入列表，使 `target: ui` 的断言也进入 needs_review 而非被后续代码误处理。
- 或者：为 `eval: llm_assisted` 的断言新增编译规则，产出一个 `kind: ui_assisted` 断言，由 assertion_engine 统一判为 INCONCLUSIVE（标记为需人工辅助判定），而非 fallback 为 status。
- 相关用例: 所有使用 `target: ui` / `eval: llm_assisted` 的 P1 用例（`_NO_DATASOURCE_TARGETS` 列表已有 `run_ui`、`pr_ui`、`ui_layout`、`ui_visual` 但遗漏了裸 `ui`）。
- 由 Phase 02 确认 rerun UI 的实际 tooltip 行为并人工裁决：若 UI 确实显示 tooltip 和次数 → 用例通过（llm_assisted 人工判 PASS）；若 UI 无 tooltip → 平台可用性缺口。
