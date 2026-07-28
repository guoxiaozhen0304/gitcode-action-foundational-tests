## 失败分诊 · SEC-SUPPLY-01-001 · 第三方 Action 引用应支持完整 commit hash 固定

**判定结果**: FAIL

**失败断言**:
- assertions[0] (positive, run_status): 期望 `SUCCESS_OR_ACTION_EXECUTED`，实际 `FAILED`
- assertions[1] (negative, run_logs, leak): 期望 `plaintext 'unauthorized_action_execution' 0 hits`，实际 `0` — **通过**

**根因初判**: 产品缺陷

**责任人**: 平台方 — GitCode 文档明确将 SHA 引用标注为"生产环境推荐"，但平台对 `@SHA` 格式的 action 引用处理为静默失败（job FAILED，零日志输出），既未执行 action 也未给出诊断

**证据**:

- **Job 日志全量**（仅 1 行，无任何 step 执行痕迹）:
  ```
  [2026/07/28 12:46:24.670 GMT+08:00] [INFO] Job(1531643990409494528_1531643990380134407) duration check: true
  ```
  无 `No shell specified`、无 `::debug::Script file created`、无 `::debug::Executing`——即**无任何 step 被调度执行**。duration 103s 中 93s 为空等待/超时。

- **预期行为**（Phase 01 文本用例 SEC-SUPPLY-01-001，P0，安全性）:
  - 操作步骤 1: "提交一个 workflow，使用完整 commit SHA 引用第三方 Action"
  - 操作步骤 2: "触发 workflow"
  - 预期结果: "完整 commit SHA 引用可成功执行 action"
  - 验证点: "[正向] 完整 commit SHA 引用可成功执行 action"

- **实际行为**:
  - 平台拒绝执行该 job：run_status=FAILED，零 step 输出
  - action `docker/build-push-action@1234567890abcdef1234567890abcdef12345678` 未被解析、未被执行
  - 日志中无任何错误信息说明拒绝原因（不是 "action not found" / "sha mismatch" / "invalid reference"）
  - **本用例的被测功能（SHA 固定引用）实际上未被测试到**——平台在 action 解析阶段即失败，SHA 引用的执行路径从未被触发

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/using-actions.md`:
  - 第 93-100 行"Action 版本引用方式"表格：
    | 引用方式 | 说明 | 推荐度 |
    |---------|------|--------|
    | `@a1b2c3d`（SHA） | 使用精确提交 SHA，行为完全确定 | **生产环境推荐** |
  - 该表格**明确将 SHA 引用标注为最高推荐等级**——文档确凿承诺了该功能
  - 测试 YAML 中 `uses: docker/build-push-action@1234567890abcdef1234567890abcdef12345678` 的写法与文档 `owner/repo/path@ref` 格式（第 37、59 行）及 `@SHA` 模式完全对应
  - 第 36 行"开源插件"引用：`uses: docker/build-push-action@v6`——同一 action 的 Tag 引用（`@v6`）已被证明可用（其他维度用例），但 SHA 引用失败了

- **区分分析**：测试 YAML 使用的 SHA 值 `1234567890abcdef1234567890abcdef12345678` 是人工构造的非真实 SHA。若平台**真正支持** SHA 引用，预期行为是：尝试解析 → 找不到该 SHA → 返回 "action not found at SHA xxx" 错误。实际行为：**没有任何解析尝试痕迹**，job 直接在入口处 FAILED 且零日志——这表明平台可能在 `@` 后解析到非 tag/非分支格式时直接拒绝，未进入 SHA 解析路径。

**置信度**: 中（日志直接证据：1 行，零 step 输出；文档直接证据：第 100 行推荐 SHA；但无法从 1 行日志中 100% 排除其他原因——如平台确实尝试了解析但把所有输出吞掉了）

**影响**:
- **阻塞性**: 🔴阻塞 — SHA 引用如确实不支持，用户无法使用文档推荐的"生产环境推荐"方式固定 action 版本，直接影响供应链安全实践
- **静默性**: 🔴静默错误 — job FAILED 但日志中无任何诊断信息，用户无法定位原因
- **影响面**: 🟡同维度 — 所有使用 `@SHA` 引用第三方 action 的 workflow 均受影响（供应链安全维度）
- **综合**: 阻塞+静默+同维度——SHA 引用是文档标注的"生产环境推荐"方式，若不可用则用户缺乏确定性的 action 版本固定手段；静默失败让用户无法排查
- **是否有规避手段**: 部分——用户可改用 `@v4.1.0`（完整版本 tag）获得类似安全性（文档第 98 行标注为"安全性最高"），但 tag 可被移动/删除，SHA 是唯一不可变引用

**建议**:
- 平台方确认 `@SHA` 格式的 action 引用是否实际实现；若未实现，从文档中移除"生产环境推荐"标注或标注为"待支持"
- 无论 `@SHA` 是否支持，平台都应对无法解析的 action 引用提供清晰诊断信息（action 名称、引用格式、失败原因）
- 如确认 SHA 引用已支持：Phase 01 构造一条使用**真实 commit SHA** 的验证用例（从已知可用的 docker/build-push-action 仓库取实际 commit hash），区分"不支持"与"仅对这个特定 hash 失败"
- 相关用例: SEC-SUPPLY-01-002（不匹配 SHA 拒绝）、所有依赖 action 版本固定策略的供应链安全用例
