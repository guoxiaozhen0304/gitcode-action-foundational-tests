# Failure Analyst — 故障注入 / 边界值用例归因报告

> 分析批次: 2026-07-25-01 | analyst: failure-analyst | 用例数: 4 FAIL

---

## 失败分诊 · REL-FAULT-01-033 · 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满

**判定结果**: FAIL

**失败断言**:
- assertions[0] (positive, run_status) — 期望 `FAILED`，实际 `COMPLETED`
- assertions[1] (positive, value, run_logs) — 期望 log 含 `No space left on device`，实际 absent

**根因初判**: 环境问题

**责任人**: Phase 02 — harness 的 fault_injection 机制（`disk_full` at pre_job）未产生预期磁盘满条件

**证据**:

- **Job 日志全量**（11 行）:
  ```
  [2026/07/25 15:09:01.199 GMT+08:00] [INFO] Job(1530592715697831936_1530592715664277511) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: …/_temp/17368304-d79a-4cd4-8451-de419c48c4b2.sh
  ::debug::Executing: bash -e …/_temp/17368304-d79a-4cd4-8451-de419c48c4b2.sh

  No shell specified, using platform default: default-bash
  ::debug::Script file created: …/_temp/1f5f754b-4acd-4151-98e0-f1dcfb91748c.sh
  ::debug::Executing: bash -e …/_temp/1f5f754b-4acd-4151-98e0-f1dcfb91748c.sh
  2048+0 records in
  2048+0 records out
  2147483648 bytes (2.1 GB, 2.0 GiB) copied, 0.836599 s, 2.6 GB/s
  ```
  两个 shell 步骤均成功执行。第一步 `fallocate`/`dd` 预填 49.5GB，第二步 `dd` 追加写入 2GB——**2GB 写入成功完成**（2048+0 records in，2.6 GB/s），未触发任何磁盘满错误。

- **预期行为**（用例 YAML `REL-FAULT-01-033`，维度 reliability，优先级 P1）:
  - `fault_injection`: `at: pre_job`, `action: disk_full`, `params: { pre_fill_gb: 49.5, append_gb: 2 }`
  - `recovery_expectation: explicit_error_and_user_retry`
  - 断言 1: `job_status == failure`
  - 断言 2: `run_logs contains "No space left on device"`

- **实际行为**:
  - 两个 shell 步骤均成功执行完毕，job 状态为 `COMPLETED`（非 FAILED）
  - 写入操作成功，无磁盘满错误
  - runner 实际磁盘容量 > 51.5GB（预填 49.5GB + 追加 2GB 后仍有余量），超出官方资源池 `small` 规格声明的 50GB

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/core-concepts/runner-and-environment.md`:
  - 第 24 行: `small` 规格磁盘声明为 50GB。而 runner 实际容量足以容纳 51.5GB+ 无错误，实际磁盘容量与文档存在偏差（实际容量 > 文档承诺容量）。这不构成产品缺陷（多给磁盘是利好而非缺陷），但使得基于 50GB 边界设计的故障注入测试失效。

**置信度**: 高 — 日志直接证明两步 shell 均成功执行，2GB 写入无报错；fault_injection 的 `disk_full` 机制未能制造磁盘满条件（runner 磁盘实际 > 51.5GB）。

**影响**:
- **阻塞性**: ⚪无影响 — 此失败暴露的是 harness 故障注入能力缺口，非平台功能缺陷
- **静默性**: 🟡可察觉 — test 设计预期 FAILED 但实际 COMPLETED，断言明确报告异常
- **影响面**: 🟡同维度 — 所有依赖 `disk_full` 故障注入的可靠性测试均受影响
- **综合**: harness 的 disk_full 注入对 small runner（实际磁盘 > 50GB）无法生效，需升级注入策略（如使用 `dd` 填写更大比例或改用 loop device）
- **是否有规避手段**: 是 — 可将 `pre_fill_gb` 从 49.5 提升至接近 runner 实际容量的值（需先探测实际容量），或换用更大磁盘规格的 runner

**建议**:
- harness 需实现磁盘容量探针：注入前先 `df` 获取实际可用空间，按比例填充（如填至 99%），不依赖固定 50GB 假设
- 相关用例: 所有启用 `fault_injection.action: disk_full` 的用例

---

## 失败分诊 · REL-FAULT-01-034 · 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss

**判定结果**: FAIL

**失败断言**:
- assertions[0] (positive, run_status) — 期望 `COMPLETED`，实际 `FAILED`
- assertions[1] (positive, value, run_logs) — 期望 log 含 `cache miss`，实际 absent

**根因初判**: 环境问题

**责任人**: Phase 02 — harness 的 `concurrent_flood` 故障注入（cache 503 at mid_job target_step:1）未能产生可控的 503 降级场景，反而导致 job 直接失败且无任何 shell 步骤输出

**证据**:

- **Job 日志全量**（3 行）:
  ```
  [2026/07/25 15:09:27.830 GMT+08:00] [INFO] Job(1530592827400790016_1530592827367235591) duration check: true

  ```
  仅 3 行输出，**零 shell 步骤执行痕迹**。无 "No shell specified"、无 "Script file created"、无任何步骤的 stdout/stderr。job 在步骤调度阶段即失败（docker 容器/shell 初始化阶段），cache 插件根本没有被调用。

- **预期行为**（用例 YAML `REL-FAULT-01-034`，维度 reliability，优先级 P1）:
  - `fault_injection`: `at: mid_job`, `action: concurrent_flood`, `params: { service: cache, response: 503, target_step: 1 }`
  - `recovery_expectation: graceful_degradation_cache_miss`
  - 断言 1: `job_status == success` — job 应整体成功
  - 断言 2: `run_logs contains "cache miss"` — cache 步骤应输出 cache miss

- **实际行为**:
  - job 在步骤执行前即 FAILED，无任何步骤被执行
  - 无法判断是 cache 插件返回了 503 还是 job 初始化阶段即崩溃
  - 与预期 "cache 步骤优雅降级为 miss、后续步骤继续执行" 完全不符
  - **失败传导链**: job 初始化阶段崩溃 → 所有步骤（cache + subsequent step）均未执行

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/using-dependency-cache.md`:
  - 第 54-58 行: cache 插件参数说明——`path`/`key` 必填，`restore-keys` 可选
  - 第 62-65 行: 缓存匹配机制——精确匹配 `key` → 前缀匹配 `restore-keys` → 全失败则执行后保存新缓存
  - **文档未提及 cache 服务 503 时的降级行为**。平台文档未承诺"cache 服务不可用时的优雅降级"——此预期来自测试设计者的健壮性假设，非平台文档承诺。但这不影响根因判定：**harness 的 fault_injection 应在 cache 步骤处注入 503，而非导致 job 在初始化阶段崩溃**。

**置信度**: 中 — 日志只有 3 行（无 shell 步骤输出），无法确定是 harness 注入触发了 job 初始化崩溃还是 runner 环境瞬时故障；但**零 shell 输出 100% 确认**故障注入未产生"cache 步骤返回 503 → 降级为 miss → 继续执行后续步骤"的目标行为

**影响**:
- **阻塞性**: 🟡非阻塞 — 此失败暴露 harness 注入能力缺口，非平台功能缺陷
- **静默性**: 🟡可察觉 — job FAILED 明确可见，但原因不透明（零 shell 输出无诊断线索）
- **影响面**: 🟡同维度 — 所有使用 `concurrent_flood` 注入的用例均可能受影响
- **综合**: harness 的 concurrent_flood 注入（cache 503 at mid_job）导致 job 初始化阶段崩溃而非在 cache 步骤产生可控 503——注入粒度过粗/实现缺陷
- **是否有规避手段**: 否 — 若 harness 的 concurrent_flood 机制本身不工作，没有测试侧规避手段；若仅此用例环境波动，重跑可验证

**建议**:
- 确认 harness 的 `concurrent_flood` 注入实现：是否能在 target_step 层面注入，还是粗粒度注入导致整个 job 崩溃
- 若注入机制尚未实现，此用例属于"预期功能不存在"——标记为 FAIL 是合理的（测试目标未达成），但根因是 harness gap 非平台缺陷
- 相关用例: 所有启用 `fault_injection.action: concurrent_flood` 的用例

---

## 失败分诊 · REL-FAULT-01-035 · 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误

**判定结果**: FAIL

**失败断言**:
- assertions[0] (positive, run_status) — 期望 `FAILED`，实际 `FAILED` — **PASS**（断言通过）
- assertions[1] (positive, value, run_logs) — 期望 log 含 `503`，实际 **absent** — FAIL
- assertions[2] (positive, run_status) — 期望 `FAILED`，实际 `FAILED` — **PASS**（断言通过）

> 注: 两条 run_status 断言均 PASS，仅 run_logs 断言因 503 未出现而 FAIL。

**根因初判**: 环境问题

**责任人**: Phase 02 — harness 的 `concurrent_flood` 故障注入（artifact_download 503 at mid_job target_step:1）未产生 503 响应；平台按正常逻辑返回了 "artifact not found" 错误

**证据**:

- **Job 日志全量**（10 行）:
  ```
  [2026/07/25 15:09:39.272 GMT+08:00] [INFO] Job(1530592875219922944_1530592875194757127) duration check: true
  ::debug::run-id input: '' (length: 0)
  ::debug::Resolved path is /home/slave1/runner/workers/0.0.4.4.version/worker_dir/ComputingActionTest/gitcode-test-2
  ::debug::Artifact client initialized for https://actions-results.atomgit.com
  ::debug::Resolved workflow id 762a8390a7434c5db06dfdfdf12b2e8c
  Downloading single artifact
  ::debug::Listing artifacts for workflow 762a8390a7434c5db06dfdfdf12b2e8c with name filter "missing-artifact"
  [Twirp] trace-id: 03bd072f3f8ce23a47b8f1648feced7c
  ::debug::Found 0 artifact(s)
  ::error::Unable to download artifact(s): Artifact 'missing-artifact' not found. Available artifacts: (none)
  ```
  download-artifact 插件正常执行：向 `https://actions-results.atomgit.com` 查询制品，返回 0 条结果。错误信息为 **"Artifact 'missing-artifact' not found"**——这是制品不存在的正常错误响应，**不是 503（Service Unavailable）**。

- **预期行为**（用例 YAML `REL-FAULT-01-035`，维度 reliability，优先级 P1）:
  - `fault_injection`: `at: mid_job`, `action: concurrent_flood`, `params: { service: artifact_download, response: 503, target_step: 1 }`
  - `recovery_expectation: explicit_error_and_rerun_success`
  - 断言 1: `step_status == failure` — download 步骤应失败
  - 断言 2: `run_logs contains "503"` — 日志应出现 503 状态码
  - 断言 3: `job_status == failure` — job 应整体失败

- **实际行为**:
  - download-artifact 步骤按正常逻辑执行，向 artifact 服务查询 `missing-artifact`
  - artifact 服务正常响应（未返回 503），正确返回 "0 artifact(s) found"
  - 步骤因制品不存在而失败，符合 download-artifact 的正常语义
  - **503 从未出现**——harness 的 503 注入未生效

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/upload-download-artifacts.md`:
  - 第 90-93 行: download-artifact 参数——`name`（必填，要下载的制品名称），`path`（可选，下载目标路径）
  - 第 100-103 行: 下载当前 workflow 所有制品示例。此处测试 YAML 传 `name: missing-artifact`，合法写法
  - **文档未提下载不存在的制品时的错误格式**，也**未提 artifact 服务 503 时的行为**——平台文档对服务不可用场景无承诺
  - 实际平台行为：制品不存在时返回 `::error::Unable to download artifact(s): Artifact 'X' not found.`——这是合理的用户可见错误

**置信度**: **高** — 日志完整展示了 download-artifact 的完整执行链路（初始化 → 查询 → 0 results → not found error），全程无 503 状态码；harness 的 503 注入明确未生效

**影响**:
- **阻塞性**: ⚪无影响 — 平台 artifact 查询功能正常工作，harness 注入未生效导致断言 FAIL
- **静默性**: 🟢明确报错 — 平台给出了清晰的 "Artifact not found" 错误信息
- **影响面**: 🟡同维度 — 所有使用 `concurrent_flood` 注入 artifact 503 的用例均受影响
- **综合**: harness 的 concurrent_flood 注入（artifact_download 503）对平台 artifact 服务完全未生效，平台按正常逻辑完成了制品查询并返回 not found
- **是否有规避手段**: 否 — 需要 harness 实现真实的 artifact 服务 503 注入或使用服务端 mock

**建议**:
- 此用例实际测试了 "下载不存在的制品时的平台行为"——平台行为正确（返回清晰错误、job FAILED）
- 503 注入未生效使得原测试目标（服务不可用时的容错）未达成
- 相关用例: 同批次 REL-FAULT-01-034（cache 503 注入同样未产生目标效果）

---

## 失败分诊 · REL-OUTPUT-01-016 · step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递

**判定结果**: FAIL

**失败断言**:
- assertions[0] (positive, status) — 期望 `all job/step green`，实际 `job 'output boundary test' status=FAILED`

> 注: 断言编译为 `kind: status`（退化断言），未编译出 `step_output_length` 类型的值断言。原始 YAML 要求 `step_output_length == 1048576`，但 compile_asserts 可能不支持此 target 类型。

**根因初判**: 用例问题

**责任人**: Phase 01 — YAML 生成器产出了无效语法 `${{{{ steps.writer.outputs.data }}}}`（四重花括号），导致 bash 解析失败

**证据**:

- **Job 日志全量**（10 行）:
  ```
  [2026/07/25 15:11:07.539 GMT+08:00] [INFO] Job(1530593245681823744_1530593245660852231) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: …/_temp/77f3602c-bbfa-480d-9ddb-f405849be468.sh
  ::debug::Executing: bash -e …/_temp/77f3602c-bbfa-480d-9ddb-f405849be468.sh

  No shell specified, using platform default: default-bash
  ::debug::Script file created: …/_temp/247db17e-a76d-48b7-b11c-ef755b1dfd7c.sh
  ::debug::Executing: bash -e …/_temp/247db17e-a76d-48b7-b11c-ef755b1dfd7c.sh
  /home/slave1/runner/workers/0.0.4.4.version/_temp/247db17e-a76d-48b7-b11c-ef755b1dfd7c.sh: line 1: ${{{{ steps.writer.outputs.data }}}}: bad substitution
  ::error::Process exited with code 1
  ```
  第一个步骤（write 1MB output）成功执行（无错误输出）。第二个步骤（read 1MB output）在第 1 行即报错：**`${{{{ steps.writer.outputs.data }}}}: bad substitution`**——bash 无法解析四重花括号语法。

- **预期行为**（用例 YAML `REL-OUTPUT-01-016`，维度 reliability，优先级 P1）:
  - `fault_injection: null` — 无故障注入，纯功能边界测试
  - Step 1: 用 python3 生成 1MB 数据，通过 `echo "data=…" >> $ATOMGIT_OUTPUT` 写入 step output
  - Step 2: 通过 `${{{{ steps.writer.outputs.data }}}}` 读取输出，校验长度 ≥ 1048576
  - 断言: `step_output_length == 1048576`

- **实际行为**:
  - Step 1 执行成功（output 已写入）
  - Step 2 在 bash 解析阶段即失败——`${{{{ }}}}` 不是合法的 context 表达式语法
  - **失败传导链**: Step 2 bash 语法错误 → step FAILED → job FAILED

- **对照 GitCode 规格**:
  - `phase01/inputs/gitcode-spec/writing-pipelines/pass-output-between-jobs.md` 第 27 行:
    ```yaml
    run: echo "version=1.0.0" >> "$ATOMGIT_OUTPUT"
    ```
    写入输出使用 `$ATOMGIT_OUTPUT` 环境变量（无花括号）。
  - 同文件第 35 行:
    ```yaml
    version: ${{ steps.version.outputs.version }}
    ```
    读取步骤输出使用 **`${{ }}`（双花括号）**，例如 `${{ steps.version.outputs.version }}`。
  - `phase01/inputs/gitcode-spec/syntax-reference/context.md` 第 16 行:
    `${{ steps.build.outputs.result }}`——所有 context 表达式统一使用 `${{ }}` 双花括号。
  - **结论**: GitCode 文档约定的 context 表达式语法为 `${{ context.property }}`（双花括号）。测试 YAML 中的 `${{{{ steps.writer.outputs.data }}}}`（四花括号）**不符合任何已知的 GitCode/AtomGit Action 语法**，是 YAML 生成的语法缺陷。

**置信度**: **高** — 日志第 9 行明确报 `bad substitution`，bash 对 `${{{{ }}` 的拒绝是确定的；GitCode 文档多处明确使用双花括号。语法错误与文档对照一致。

**影响**:
- **阻塞性**: ⚪无影响 — 此为测试用例自身的语法缺陷，非平台功能问题
- **静默性**: 🟢明确报错 — bash 直接报 "bad substitution"，错误信息清晰
- **影响面**: 🟡同维度 — 所有 Phase 01 生成的使用 `${{{{ }}}}` 四花括号的用例均受影响（这是一个已知的系统性 YAML 生成缺陷模式）
- **综合**: 测试 YAML 的四花括号语法错误导致 step 2 在 bash 解析阶段即失败，1MB output 传递功能本身未被测试到
- **是否有规避手段**: 是 — 将 `${{{{ steps.writer.outputs.data }}}}` 改为 `${{ steps.writer.outputs.data }}` 即可修复

**建议**:
- Phase 01 的 YAML 生成器需修复 `${{{{ }}}}` → `${{ }}` 的系统性语法错误（此为已知模式，非孤立个案）
- compile_asserts 对 `step_output_length` target 类型退化为 `kind: status`（仅检查 job/step 是否 green），未能做长度值断言——这本身也是一个编译缺口，但与当前 FAIL 的根因（语法错误）独立
- 修复语法后重新跑，验证 1MB output 传递是否真正工作

---

## 汇总

| 用例 | 根因分类 | 责任人 | 置信度 |
|------|---------|--------|--------|
| REL-FAULT-01-033 | 环境问题 | Phase 02 | 高 |
| REL-FAULT-01-034 | 环境问题 | Phase 02 | 中 |
| REL-FAULT-01-035 | 环境问题 | Phase 02 | 高 |
| REL-OUTPUT-01-016 | 用例问题 | Phase 01 | 高 |

**模式总结**:
- **3/4 为 harness 故障注入机制缺口**（REL-FAULT-01-033/034/035）：harness 的 `fault_injection` 声明未转化为实际的故障条件（disk_full 填充量不足 + concurrent_flood 完全未生效）。故障注入是 Phase 02 harness 的核心能力，当前处于"YAML 声明了但执行层未实现或未生效"状态——系统性缺口。
- **1/4 为 YAML 生成语法缺陷**（REL-OUTPUT-01-016）：`${{{{ }}}}` 四花括号是 Phase 01 的已知系统性 bug，非平台问题。
- **零产品缺陷**：本轮 4 个 FAIL 中无一是 GitCode Action 平台的实际功能缺陷——3 个是 harness 注入能力缺口，1 个是用例生成 bug。
