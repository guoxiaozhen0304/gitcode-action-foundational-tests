# Failure Analyst 根因初判 · run=2026-07-24-valid297-final2 · COMPATIBILITY + USABILITY

共 22 条 FAIL 用例，按 case_id 顺序排列。

---

## 失败分诊 · COMPAT-PERM-01-001 · 未声明 permissions 时默认 TOKEN 读操作权限范围

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 通过; assertions[1] (positive, run_logs) — 期望 log contains 'README'，实际 absent

**根因初判**: 用例问题

**责任人**: Phase 01 — 断言设计缺陷：expected 字符串 'README' 不在该 repo 的 README.md 文件内容中

**证据**:
- **Job 日志全量** (54 行): job 正常完成 (COMPLETED, duration=35s)，checkout 成功，`cat README.md` 输出文件内容为 "# gitcode-test-4" 和 "并发验证gitcodeactions的子仓库"——文件读取成功，未因权限不足被拒绝。日志中不存在 "README" 字符串。
- **预期行为**: 未声明 permissions 时默认 TOKEN 仅拥有读仓库权限，应能成功 `cat README.md`。
- **实际行为**: 文件读取成功，但断言匹配字符串 `"README"` 不存在于文件内容中，导致误判 FAIL。功能本身正常（读权限生效）。
- **对照 GitCode 规格** `token-permissions.md` 第 11-20 行：ATOMGIT_TOKEN 自动生成，权限由 permissions 字段控制；未声明时应有默认权限可读取仓库。

**置信度**: 高（日志证据直接，job 运行成功，断言匹配字符串不存在）

**影响**:
- **阻塞性**: ⚪无影响 — 功能正常，断言不匹配导致假失败
- **静默性**: ⚪无影响 — 只是标记问题
- **影响面**: 🟢单用例
- **综合**: 无影响，断言字符串选择不当（期望 repo 文件内包含 "README" 字面值但不含），需修正断言匹配内容
- **是否有规避手段**: 是 — 改用包含实际文件内容的匹配串，如 "test-4"

**建议**:
- 修正断言：将 contains: "README" 改为 contains: "gitcode-test" 或其他确定在文件中的内容
- 或改用更通用的断言：验证 exit code 0 即可证明读取成功

---

## 失败分诊 · COMPAT-ARTIFACT-01-001 · upload/download-artifact 跨 job 传递等价性

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED; assertions[1] (positive, run_logs) — 期望 log contains 'ARTIFACT_TRANSFER_OK'，实际 absent

**根因初判**: 环境问题

**责任人**: Phase 02 — 测试环境 artifact 名称残留冲突

**证据**:
- **Job 日志全量** (27 行):
  ```
  ::error::Upload artifact failed: Artifact with name already exists: cross-job-artifact, repoId=10431336, workflowId=75c8a55eb8704112af9e7a4acf79fb73
  ```
  job-upload 步骤失败，根因是 artifact 名称 "cross-job-artifact" 已存在。
- **预期行为**: upload artifact → download artifact → verify content → ARTIFACT_TRANSFER_OK
- **实际行为**: upload-artifact 因名称冲突失败，后续 download/verify 均未执行。
- **对照 GitCode 规格** `upload-download-artifacts.md`：正常应支持 upload/download 跨 job 传递。

**置信度**: 高（日志直接显示 "already exists"，典型的环境残留问题）

**影响**:
- **阻塞性**: ⚪无影响 — 非平台缺陷，环境需清理
- **静默性**: 🟡可察觉 — 错误信息明确
- **影响面**: 🟢单用例
- **综合**: 环境问题，需确保每次运行前清理同名 artifact 或使用唯一名称
- **是否有规避手段**: 是 — 使用带时间戳/run_id 的 artifact 名称或运行前清理

**建议**:
- harness 应在每次运行前清理同名 artifact，或为每个 run 使用唯一 artifact 名称
- 相关用例: COMPAT-ARTIFACT-01-002（同名问题）

---

## 失败分诊 · COMPAT-ARTIFACT-01-002 · upload-artifact 保留期行为等价性

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED; assertions[1] (positive, run_logs) — 期望 log contains 'ARTIFACT_UPLOADED_OK'，实际 absent

**根因初判**: 环境问题

**责任人**: Phase 02 — 测试环境 artifact 名称残留冲突

**证据**:
- **Job 日志全量** (28 行):
  ```
  ::error::Upload artifact failed: Artifact with name already exists: retention-test-artifact, repoId=10431338, workflowId=38558bd483024d28b5b46ce121cddc18
  ```
  与 COMPAT-ARTIFACT-01-001 同根因——artifact 名称冲突。
- **预期行为**: upload artifact with retention-days=1 → echo "ARTIFACT_UPLOADED_OK"
- **实际行为**: upload 因名称冲突失败
- **对照 GitCode 规格** 同上

**置信度**: 高（与 COMPAT-ARTIFACT-01-001 同根因）

**影响**:
- **阻塞性**: ⚪无影响 — 环境残留
- **静默性**: 🟡可察觉 — 错误信息明确 "already exists"
- **影响面**: 🟢单用例
- **综合**: 与 COMPAT-ARTIFACT-01-001 同根因
- **是否有规避手段**: 是 — 唯一 artifact 名称

**建议**:
- 同 COMPAT-ARTIFACT-01-001

---

## 失败分诊 · COMPAT-CACHE-01-001 · cache 行为等价性——缓存命中场景

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_logs) — 期望 log contains 'CACHE_HIT'，实际 absent

**根因初判**: 产品缺陷（能力边界/文档缺口）

**责任人**: 平台方 — cache 插件不支持 workflow_dispatch 事件

**证据**:
- **Job 日志全量** (11 行):
  ```
  ::warning::Event Validation Error: The event type Manual (normalized: manual) is not supported because it's not tied to a branch or tag ref.
  ::warning::[cache eventValidation] normalized=manual allowlistMatch=false allowlist=[push|pull_request|merge_request] ATOMGIT_EVENT_NAME=Manual ...
  CACHE_MISS
  ```
  cache 插件明确拒绝：仅接受 push | pull_request | merge_request 事件，workflow_dispatch (Manual) 不在 allowlist。
- **预期行为**: 第二次运行（同 key）应命中 cache → CACHE_HIT
- **实际行为**: 每次都是 CACHE_MISS，cache 完全无法在 workflow_dispatch 下工作
- **对照 GitCode 规格** `COMPAT-NOTES.md` 第 49 行、`using-dependency-cache.md`：cache 插件文档未注明仅支持 push/PR 事件，但实际实现限制了事件范围。

**置信度**: 高（日志明确输出 allowlist 验证逻辑）

**影响**:
- **阻塞性**: 🟡非阻塞 — 仍可手动触发但 cache 不工作
- **静默性**: 🟡可察觉 — 日志有 warning 提示
- **影响面**: 🔴跨维度 — 所有通过 workflow_dispatch 触发的 CI/CD pipeline 无法使用 cache 加速
- **综合**: 非阻塞但跨维度——通过 UI 手动触发的所有 workflow 均无法利用 cache，严重影响开发体验和资源效率
- **是否有规避手段**: 部分 — 改用 push 事件触发可正常 cache，但失去了手动触发的灵活性

**建议**:
- 平台应将 cache allowlist 扩展至包含 workflow_dispatch / Manual 事件
- 或在文档中明确标注 cache 仅在 push/pull_request 事件下生效

---

## 失败分诊 · COMPAT-DIR-01-002 · 工作流目录差异——.github/workflows/ 不应被识别

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative, run_logs) — 期望 plaintext 'GITHUB_DIR_WORKFLOW_RAN' 0 hits，实际 FOUND

**根因初判**: 用例问题

**责任人**: Phase 01 — 断言设计无法区分触发来源（.gitcode/ vs .github/ directory）

**证据**:
- **Job 日志全量** (5 行): `GITHUB_DIR_WORKFLOW_RAN` 出现，run_status=COMPLETED
- **预期行为**: `.github/workflows/` 下的 workflow 不应被 GitCode 识别和触发；仅 `.gitcode/workflows/` 应生效
- **实际行为**: Workflow 由 Phase 02 部署到 `.gitcode/workflows/` 并因 push 事件触发执行——这是**正确行为**。`GITHUB_DIR_WORKFLOW_RAN` 从 `.gitcode/workflows/` 版本输出，但断言将其视为 `.github/workflows/` 被错误识别的证据。
- **失败传导链**: 无——这是一个假阳性；.gitcode/workflows/ 正确触发，断言缺乏区分 .gitcode/ vs .github/ 来源的能力。
- **对照 GitCode 规格** `configure-triggers.md` 第 9 行：明确 "workflow 文件已放在 `.gitcode/workflows/` 目录下"。`workflow-file-location-structure.md` 说明仅识别 `.gitcode/workflows/`。

**置信度**: 高（日志证据直接，断言逻辑缺陷明显）

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为可能正常，断言假阳性
- **静默性**: ⚪无影响 — 标记误判
- **影响面**: 🟢单用例
- **综合**: 断言设计问题——使用了无法区分触发来源的生产者标记。要证明 .github/ 被误识别，需设计两个内容不同的 workflow 分别放两目录
- **是否有规避手段**: 是 — 在两个目录放不同 marker 字符串，检查各自是否出现

**建议**:
- 重新设计：.gitcode/workflows/ 版本输出 "GITCODE_DIR_OK"，.github/workflows/ 版本（预置 fixture）输出 "GITHUB_DIR_WORKFLOW_RAN"——如仅前者出现 = 正确，后者出现 = .github/ 被误识别

---

## 失败分诊 · COMPAT-INPUTS-01-001 · workflow_dispatch inputs 类型限制 - boolean 应报错

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, run_status_not) — 期望 conclusion != COMPLETED（应被拒绝），实际 COMPLETED

**根因初判**: 产品缺陷（能力边界/文档缺口）

**责任人**: 平台方 — 平台未校验 inputs type 字段，静默接受非 string 类型

**证据**:
- **Job 日志全量** (5 行): `INPUT_OK` — workflow 正常执行完成
- **预期行为**: 文档要求 workflow_dispatch inputs 仅支持 string 类型；type=boolean 应在 YAML 解析/校验阶段报错
- **实际行为**: 平台静默接受 `type: boolean` 并正常执行 workflow
- **对照 GitCode 规格** `COMPAT-NOTES.md` 第 46 行："GitCode workflow_dispatch/workflow_call 的 inputs 仅支持 string 类型"；但平台未实现此校验

**置信度**: 高（日志显示工作流成功执行，未因 boolean 类型被拒绝）

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为不阻塞 workflow
- **静默性**: 🔴静默错误 — 平台不报错，用户以为 boolean 类型可用，可能在逻辑中使用布尔值导致意外行为
- **影响面**: 🟡同维度 — 影响所有使用 workflow_dispatch inputs 的 workflow
- **综合**: 静默接受非 string 类型→用户可能误以为支持 boolean/number 等类型，写出平台实际不支持但未被拒绝的 YAML
- **是否有规避手段**: 否 — 用户无法得知类型限制未生效

**建议**:
- 平台应在 YAML 解析阶段验证 inputs type 字段，对非 string 类型给出明确错误并提示仅支持 string

---

## 失败分诊 · COMPAT-OUTCOME-01-002 · continue-on-error true 时 outcome 应为 failure 而 conclusion 应为 success

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 FAILED，实际 COMPLETED

**根因初判**: 标记不匹配

**责任人**: Phase 01 — compile_asserts.py 将 step-level outcome 概念错误映射为 job-level run_status=FAILED

**证据**:
- **Job 日志全量** (62 行):
  ```
  ::error::Process exited with code 1           # failing step exit
  This step should run                            # next step runs after continue-on-error
  Check step outcome and conclusion               # final step runs
  ```
  run_status=COMPLETED: 这是**正确行为**——continue-on-error:true 的步骤失败后，后续步骤继续执行，job 最终以 success 结束。
- **预期行为**: step outcome=failure, step conclusion=success (job continues), run_status=success
- **实际行为**: 与预期一致——step outcome 是 failure（exit 1），但 job conclusion 是 success（continue-on-error 容忍）
- **对照 GitCode 规格** `configure-steps.md`：continue-on-error 允许步骤失败后继续，job 状态不受影响

**置信度**: 高（断言编译器将 step outcome → job run_status 映射错误）

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为正确，假阳性
- **静默性**: ⚪无影响 — 标记误判
- **影响面**: 🟢单用例
- **综合**: 断言编译器 word-to-word 映射错误，step outcome = failure 不等于 job run_status = FAILED
- **是否有规避手段**: 是 — 修正 compile_asserts.py 中 step 级 target 到 job 级 verdict 的映射规则

**建议**:
- compile_asserts.py 需区分 step_status / step_conclusion / run_status 三个不同 target 的映射

---

## 失败分诊 · COMPAT-OUTCOME-01-003 · outcome 与 conclusion 在 job 条件判断中不应互换语义

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 FAILED，实际 COMPLETED

**根因初判**: 标记不匹配

**责任人**: Phase 01 — compile_asserts.py 同样将 step_status=failure 误映射为 run_status=FAILED

**证据**:
- **Job 日志全量** (58 行):
  ```
  ::error::Process exited with code 1           # job-a 的 failing step
  Job A conclusion should be success             # job-b 成功执行（needs 基于 conclusion 判断通过）
  ```
  run_status=COMPLETED: 所有 job 正确执行，job-b 的 needs 判定正确——job-a conclusion=success
- **预期行为**: job A conclusion=success 使 job B 继续；step outcome=failure 保持
- **实际行为**: 与预期完全一致——Job A conclusion 为 success（continue-on-error 容忍），Job B 正常执行
- **对照 GitCode 规格** `configure-dependencies-order.md`：needs 基于结论（conclusion）而非步骤结果（outcome）

**置信度**: 高（与 COMPAT-OUTCOME-01-002 同根因）

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为正确
- **静默性**: ⚪无影响 — 假阳性
- **影响面**: 🟢单用例
- **综合**: 同 COMPAT-OUTCOME-01-002——断言编译器映射错误
- **是否有规避手段**: 是 — 修正编译器

**建议**:
- 同 COMPAT-OUTCOME-01-002

---

## 失败分诊 · COMPAT-RUNSON-01-002 · runs-on 标签体系——单标签字符串应报错

**判定结果**: FAIL
**失败断言**: assertions[2] (leak, negative, run_logs) — 期望 plaintext 'RUNSON_STRING_ACCEPTED' 0 hits，实际 FOUND

**根因初判**: 用例问题

**责任人**: Phase 01 — YAML 工作流使用了合法的数组格式但测试标题/断言期望"单标签字符串"场景

**证据**:
- **Job 日志全量** (5 行): `RUNSON_STRING_ACCEPTED` — workflow 正常执行
- **预期行为**: 标题说"单标签字符串应报错"、断言说不应成功执行——但 YAML 中 `runs-on: [ubuntu-latest, x64, small]` 是正确的三段式数组格式
- **实际行为**: 平台接受并正确执行了数组格式的 runs-on（正确行为）
- **对照 GitCode 规格** `COMPAT-NOTES.md` 第 37 行：GitCode 用三段式标签 `{os-version},{arch},{flavor}`，正确格式已使用

**置信度**: 高（YAML 使用了合法格式，断言期望错误但没有制造错误条件）

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为正确
- **静默性**: ⚪无影响 — 假阳性
- **影响面**: 🟢单用例
- **综合**: 用例自相矛盾——标题说要测"单标签字符串应报错"但 YAML 使用了正确的数组格式
- **是否有规避手段**: 是 — 修正 YAML 为 `runs-on: ubuntu-latest`（单字符串）以测试实际的错误场景

**建议**:
- 修正 YAML：将 runs-on 改为单字符串 `ubuntu-latest`（而非数组）以触发预期错误
- 或修改标题/断言以匹配实际的数组格式测试内容

---

## 失败分诊 · COMPAT-VARS-01-006 · vars 在 Action 中的可用性差异

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷（能力边界）

**责任人**: 平台方 — vars 在 Action with 参数中的值解析失败

**证据**:
- **Job 日志全量** (6 行):
  ```
  [ERROR] 根因: Input required and not supplied: COMMIT_REF_NAME
  ::error::Input required and not supplied: COMMIT_REF_NAME
  ```
  使用 `${{ vars.ACTION_VAR }}` 作为 checkout action 的 ref 参数，但 vars 解析失败导致 ref 为空，checkout 报错。
- **预期行为**: `vars.ACTION_VAR` 应解析为 "action_value"，checkout 应能使用该 ref
- **实际行为**: vars 值未成功传递到 Action 的 with 参数中
- **对照 GitCode 规格** `syntax-reference/context.md` 第 13 行：vars 上下文定义为 "组织/项目级别配置变量"，应可在表达式中可用

**置信度**: 中（var 可能因未正确配置或平台不支持 vars 在 Action with 中传递；需确认环境是否已配置 vars.ACTION_VAR）

**影响**:
- **阻塞性**: 🔴阻塞 — workflow 因 checkout 失败中断
- **静默性**: 🟡可察觉 — checkout 报错 "Input required and not supplied"
- **影响面**: 🟡同维度 — 影响所有在 Action with 参数中使用 vars 的 workflow
- **综合**: vars 值未能传递到 Action 参数中，导致 workflow 中断
- **是否有规避手段**: 部分 — 可用 env 上下文替代 vars 设值到环境变量再在 step run 中引用；但损失了 vars 的跨 workflow 复用性

**建议**:
- 需验证 vars 是否已在环境配置，排除环境问题；若确认已配置则属平台缺陷

---

## 失败分诊 · USE-CONC-01-001 · concurrency.max 配置 0 或 10 时报错应提示有效范围 1-5

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, run_status_not) — 期望 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 产品缺陷（能力边界）

**责任人**: 平台方 — 平台未校验 concurrency.max 取值范围

**证据**:
- **Job 日志全量** (5 行): `hello` — workflow 正常执行完成
- **预期行为**: concurrency.max: 10（超出合理范围 1-5）应在解析阶段报错，workflow 不应执行
- **实际行为**: 平台静默接受 max: 10，workflow 正常执行
- **对照 GitCode 规格** `configure-jobs.md` / `concurrency` 章节：应定义有效范围，超出范围应拒绝

**置信度**: 中（需确认 GitCode 文档是否定义了 concurrency.max 的有效范围；若无文档定义则属于文档缺口而非实现缺陷）

**影响**:
- **阻塞性**: ⚪无影响 — workflow 正常执行
- **静默性**: 🔴静默错误 — 配置了超出合理范围的值但无任何反馈，后续行为不可预期
- **影响面**: 🟡同维度 — 所有使用 concurrency 的 workflow
- **综合**: 静默接受非法配置——用户以为限流生效实则不受限
- **是否有规避手段**: 否

**建议**:
- 平台应在解析阶段校验 concurrency.max 的合法取值范围并给出明确错误

---

## 失败分诊 · USE-CTX-01-001 · 使用 atomgit 上下文时表达式正常求值

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_logs) — 期望 log contains 'ref=refs/heads/'，实际 absent

**根因初判**: 产品缺陷

**责任人**: 平台方 — atomgit.ref 返回值与文档承诺不一致

**证据**:
- **Job 日志全量** (5 行): `ref=main` — atomgit.ref 返回短格式 "main"
- **预期行为**: 断言期望 `ref=refs/heads/main`（完整引用格式）
- **实际行为**: atomgit.ref 返回 "main"（仅分支名，无 refs/heads/ 前缀）
- **对照 GitCode 规格** `syntax-reference/context.md` 第 31 行：明确文档承诺 `atomgit.ref` → "触发引用（分支或标签全名，如 `refs/heads/main`）"。实际返回 "main" 与文档承诺矛盾。

**置信度**: 高（日志证据 + 规格文档精确对应）

**影响**:
- **阻塞性**: 🟡非阻塞 — workflow 可完成，但 ref 格式不符
- **静默性**: 🔴静默错误 — user 脚本依赖完整 ref 格式（如 `refs/heads/` 前缀）时会静默出错
- **影响面**: 🔴跨维度 — 所有引用 `atomgit.ref` 的 workflow 均受影响
- **综合**: 非阻塞但静默且跨维度——atomgit.ref 返回短格式违背文档承诺，可导致所有依赖 `refs/heads/` 前缀的下游脚本静默失败
- **是否有规避手段**: 是 — 用户可用 `atomgit.ref_name` 获得相同短格式值，但需手动拼接 `refs/heads/` 前缀

**建议**:
- 平台应修正 atomgit.ref 返回完整格式（`refs/heads/main`）以符合文档承诺
- 或修正文档（若短格式是有意为之的设计选择）

---

## 失败分诊 · USE-CTX-01-002 · 使用 github 上下文时报错应提示 atomgit 替代

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, run_status_not) — 期望 conclusion != COMPLETED（应报错），实际 COMPLETED

**根因初判**: 产品缺陷

**责任人**: 平台方 — 平台静默将 github.ref 映射为占位符值，未给出迁移提示

**证据**:
- **Job 日志全量** (5 行): `ref=placeholder_ref` — 使用 `${{ github.ref }}` 未被拒绝，返回占位符值
- **预期行为**: 期望 workflow 报错，错误信息应包含 "github" 和 "atomgit" 字样并给出替换建议
- **实际行为**: 平台静默接受 github.ref 并返回 "placeholder_ref"，workflow 成功完成
- **对照 GitCode 规格** `COMPAT-NOTES.md` 第 10-12 行："直接搬 GitHub workflow 会全线失效"、"GitCode 核心上下文是 atomgit.*"

**置信度**: 高（日志直接证据）

**影响**:
- **阻塞性**: ⚪无影响 — workflow 成功但返回占位符
- **静默性**: 🔴静默错误 — 用户以为 github.ref 可用（因 workflow 成功），但得到虚假占位符值，业务逻辑可能出错
- **影响面**: 🔴跨维度 — 所有从 GitHub Actions 迁移且忘记改 github.* 为 atomgit.* 的 workflow
- **综合**: 极其危险的静默错误——迁移用户若漏改一处 github.* → 得到占位符而非明确报错，难以排查
- **是否有规避手段**: 否 — 用户无法自动发现此错误

**建议**:
- 平台应在使用 github 上下文时给出明确错误或 warning，提示应改用 atomgit 上下文
- 不应将 github.ref 静默替换为 placeholder_ref，这会产生误导性结果

---

## 失败分诊 · USE-ANNOT-01-002 · ::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转

**判定结果**: FAIL
**失败断言**: assertions[0] (status) — 期望 all job/step green，实际 job 'PR annotation test' status=FAILED

**根因初判**: 环境问题

**责任人**: Phase 02 — PR ref 解析失败（checkout 无法获取 refs/merge-requests/22/merge），annotations 功能本身未被测试到

**证据**:
- **Job 日志全量** (49 行):
  ```
  git -c protocol.version=2 fetch ... +refs/merge-requests/22/merge:refs/remotes/merge-requests/22/merge
  fatal: couldn't find remote ref refs/merge-requests/22/merge
  [ERROR] 根因: Git命令执行失败.
  ```
  checkout 步骤在 fetch PR merge ref 时失败，后续 ::error:: annotation 步骤未执行。
- **预期行为**: checkout PR → emit ::error:: annotation → 验证 annotation 在 PR 页面显示
- **实际行为**: checkout 失败 → job FAILED → annotation 步骤未执行
- **失败传导链**: checkout FAIL → annotation step 未执行 → PR annotation 功能未被测试到

**置信度**: 高（日志直接显示 PR ref 不存在）

**影响**:
- **阻塞性**: 🔴阻塞 — job 因 checkout 失败而中断
- **静默性**: 🟡可察觉 — 报错明确
- **影响面**: 🟡同维度 — 可能影响所有 PR 触发的 workflow
- **综合**: PR ref 获取失败，annotation 功能本身未被测试；需确认是 CI 环境 PR ref 问题还是平台缺陷
- **是否有规避手段**: 需排查 PR ref 格式是否正确

**建议**:
- 检查 MR #22 是否存在、ref 格式是否正确（GitCode 用 merge-requests 而非 pull-requests）
- annotation 功能应设计为不依赖 checkout 成功的测试用例

---

## 失败分诊 · USE-DISP-01-002 · workflow_dispatch 未提供参数但存在 default 时应使用默认值运行

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_logs) — 期望 log contains 'env=staging'，实际 absent

**根因初判**: 产品缺陷

**责任人**: 平台方 — workflow_dispatch 默认 input 值未生效或 dispatch 触发失败

**证据**:
- **Job 日志全量** (1 行): 仅 duration check 行，无任何 shell 脚本执行输出
- **预期行为**: 不提供 inputs.environment → 使用 default 值 "staging" → echo "env=staging"
- **实际行为**: job 执行了但日志为空（仅 1 行 runner metadata），job 状态 FAILED，没有默认值生效的证据
- **对照 GitCode 规格** `configure-triggers.md` 第 75-80 行：workflow_dispatch 支持 inputs 定义，含 default 字段

**置信度**: 中（日志极短仅有 1 行；可能是 dispatch 触发方式有问题或平台未设置默认值）

**影响**:
- **阻塞性**: 🔴阻塞 — workflow 未产出预期结果
- **静默性**: 🟡可察觉 — job FAILED，但原因不透明
- **影响面**: 🟡同维度 — workflow_dispatch default 值功能不工作
- **综合**: default 输入值未生效，workflow 未能完成验证
- **是否有规避手段**: 否

**建议**:
- 需进一步排查：dispatch 触发是否成功、input 默认值是否在 YAML 解析阶段已被正确读取

---

## 失败分诊 · USE-ENV-01-002 · 引用 GITHUB_SHA 时日志应给出环境变量映射提示

**判定结果**: FAIL
**失败断言**: assertions[0] (status) — 期望 all job/step green，实际 job 'test GITHUB env var hint' status=FAILED

**根因初判**: 产品缺陷

**责任人**: 平台方 — GITHUB_* 环境变量不存在且未给出 ATOMGIT_* 迁移提示

**证据**:
- **Job 日志全量** (6 行):
  ```
  /home/slave1/...sh: line 2: GITHUB_SHA: unbound variable
  ::error::Process exited with code 1
  ```
  `GITHUB_SHA` 环境变量未定义（而非静默为空），set -u 触发 "unbound variable" 错误。但错误信息仅是 shell 级别的，无 GitCode 平台级提示（如"GITHUB_SHA 在 GitCode 中对应 ATOMGIT_SHA"）。
- **预期行为**: 日志应给出迁移指引，提示 GITHUB_* → ATOMGIT_* 映射
- **实际行为**: 仅有 shell unbound variable 错误，无平台级迁移提示
- **对照 GitCode 规格** `COMPAT-NOTES.md` 第 11 行："系统环境变量前缀：GitCode 为 ATOMGIT_*"

**置信度**: 高（日志证据直接）

**影响**:
- **阻塞性**: 🔴阻塞 — job 因未定义变量而失败
- **静默性**: 🟡可察觉 — 有明确 shell 错误但缺少迁移指引
- **影响面**: 🔴跨维度 — 所有从 GitHub Actions 迁移、使用 GITHUB_* 环境变量的 workflow
- **综合**: 阻塞且跨维度——用户收到 shell 错误而非平台级迁移提示，增加迁移排查成本
- **是否有规避手段**: 是 — 用户需自行查找 COMPAT-NOTES 文档

**建议**:
- 平台应在 runner 中预定义 GITHUB_* → ATOMGIT_* 的映射变量（或至少给出 warning）
- 或在 runner 启动阶段检测到 GITHUB_* 引用时输出迁移提示

---

## 失败分诊 · USE-EXPR-01-001 · 引用不存在的上下文属性时报错应包含原始表达式与错误类型

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, run_status_not) — 期望 conclusion != COMPLETED（应报错），实际 COMPLETED

**根因初判**: 产品缺陷

**责任人**: 平台方 — 不存在的上下文属性被静默解析为空字符串

**证据**:
- **Job 日志全量** (5 行): `val=` — `${{ atomgit.nonexistent_property }}` 静默解析为空字符串
- **预期行为**: 引用不存在的上下文属性应报错，错误信息包含原始表达式和错误类型
- **实际行为**: 平台静默将未知上下文属性解析为空字符串，workflow 成功完成
- **对照 GitCode 规格** `expressions.md`：文档未说明未知上下文属性的行为

**置信度**: 高（日志直接证据）

**影响**:
- **阻塞性**: ⚪无影响 — workflow 成功完成但值异常
- **静默性**: 🔴静默错误 — 用户拼错属性名 → 得到空字符串而非错误 → 后续逻辑可能做出错误判断
- **影响面**: 🔴跨维度 — 所有使用上下文表达式的 workflow
- **综合**: 极度危险的静默行为——用户某处拼错 atomgit 属性名，得到空值但平台不报错，很难排查
- **是否有规避手段**: 否 — 没有防御手段

**建议**:
- 平台应在表达式求值阶段校验上下文属性是否存在，对不存在的属性给出报错并指明属性名

---

## 失败分诊 · USE-INPT-01-002 · 使用 boolean 类型 input 时报错应提示仅支持 string

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, run_status_not) — 期望 conclusion != COMPLETED（应报错），实际 COMPLETED

**根因初判**: 产品缺陷（能力边界）

**责任人**: 平台方 — 同 COMPAT-INPUTS-01-001，平台未校验 inputs type

**证据**:
- **Job 日志全量** (5 行): `dry_run=false` — workflow 正常执行
- **预期行为**: type=boolean 应在 YAML 校验阶段报错
- **实际行为**: 平台静默接受并使用 boolean 类型输入
- **对照 GitCode 规格** `COMPAT-NOTES.md` 第 46 行：inputs 仅支持 string 类型

**置信度**: 高（与 COMPAT-INPUTS-01-001 同根因）

**影响**:
- **阻塞性**: ⚪无影响 — workflow 正常
- **静默性**: 🔴静默错误 — 同 COMPAT-INPUTS-01-001
- **影响面**: 🟡同维度
- **综合**: 与 COMPAT-INPUTS-01-001 同根因
- **是否有规避手段**: 否

**建议**:
- 同 COMPAT-INPUTS-01-001

---

## 失败分诊 · USE-LOG-01-001 · 多 step 日志按时间线组织且边界清晰

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_logs) — 期望 log contains 'step one prepare'，实际 absent

**根因初判**: 用例问题

**责任人**: Phase 01 — 断言期望 step name 出现在 stdout 日志中，但 step name 是 UI 层元数据不输出到 shell stdout

**证据**:
- **Job 日志全量** (25 行): 所有 5 步正常执行，输出 "prepare done" / "build done" / "test done" / "package done" / "summary done"。每步之间有明确分隔，时间线清晰。
- **预期行为**: 断言期望日志包含 step name "step one prepare"
- **实际行为**: stdout 日志只包含 shell 脚本的输出内容（"prepare done"），不包含 step name（step name 在 UI 层级显示而非 shell输出）
- **对照 GitCode 规格** `view-job-logs.md`：日志 UI 应按步骤分组显示，step name 在 UI 层级而非 shell stdout

**置信度**: 高（step name 是 runner orchestrator 层面的标签，不经过 shell）

**影响**:
- **阻塞性**: ⚪无影响 — 功能正常，多步日志清晰
- **静默性**: ⚪无影响 — 假阳性
- **影响面**: 🟢单用例
- **综合**: 断言错误地期望 UI 层元数据（step name）出现在 shell stdout 中
- **是否有规避手段**: 是 — 断言改为匹配每个步骤的 shell 输出内容（如 "prepare done"）

**建议**:
- 修正断言：contains 改为各步骤实际输出的 marker 字符串（如 "prepare done" / "build done"）
- 或使用多段 contains 验证每个 step 的输出均在日志中出现

---

## 失败分诊 · USE-MD-01-001 · ATOMGIT_STEP_SUMMARY 写入的 Markdown 正确渲染为 HTML

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, step_summary) — 期望 log contains 'Test Report'，实际 absent

**根因初判**: 用例问题

**责任人**: Phase 01 — 断言在 stdout 日志中寻找 step summary 内容，但 summary 内容写入专门的 summary 文件/页面，不出现在 stdout log 中

**证据**:
- **Job 日志全量** (4 行): job 成功执行（COMPLETED, duration=105s），写入 `$ATOMGIT_STEP_SUMMARY` 的 Markdown 内容不显示在 stdout 日志中。stdout 日志仅有 runner 级别的 debug 行且无 shell 输出（echo 全部被重定向到 summary 文件）。
- **预期行为**: Markdown 应渲染在 step summary 页面
- **实际行为**: 平台正常完成了 summary 写入（job COMPLETED），但断言在错误的 channel（stdout log）搜索 summary 内容
- **对照 GitCode 规格**: `$ATOMGIT_STEP_SUMMARY` 写入到独立的 summary 文件，不经过 stdout

**置信度**: 高（summary 文件和 stdout log 是不同的输出 channel）

**影响**:
- **阻塞性**: ⚪无影响 — 功能可能正常，假阳性
- **静默性**: ⚪无影响 — 假阳性
- **影响面**: 🟢单用例
- **综合**: 断言在错误的 channel（stdout log）搜索 summary 内容
- **是否有规避手段**: 是 — 需要在 summary 页面（而非 log）验证内容；或先 echo 到 stdout 再 tee 到 summary

**建议**:
- assertion_engine 需支持 `step_summary` target 类型（从 summary 文件中验证内容，而非从 stdout log）
- 当前架构下可考虑先用 `cat $ATOMGIT_STEP_SUMMARY` 输出到 stdout 再验证

---

## 失败分诊 · USE-OS-01-001 · runner.os 返回值与文档声明的平台支持一致

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_logs) — 期望 log contains 'os=Linux'，实际 absent

**根因初判**: 产品缺陷（文档不一致）

**责任人**: 平台方 — runner.os 返回 "linux"（小写）而非 "Linux"（首字母大写）

**证据**:
- **Job 日志全量** (5 行): `os=linux` — runner.os 返回小写 "linux"
- **预期行为**: 断言期望 `os=Linux`（首字母大写，与 GitHub Actions 行为一致）
- **实际行为**: 返回 `linux`（全小写）
- **对照 GitCode 规格** `syntax-reference/context.md` 第 17 行：列出 `runner.os` 但未说明具体返回值格式。`COMPAT-NOTES.md` 未提及此差异。

**置信度**: 中（日志证据直接，但需确认 GitCode 文档对 runner.os 返回值的大小写约定）

**影响**:
- **阻塞性**: ⚪无影响 — workflow 正常
- **静默性**: 🔴静默错误 — 用户脚本中做 `runner.os == 'Linux'` 大小写敏感比较会静默失败
- **影响面**: 🔴跨维度 — 所有使用 runner.os 做条件判断的 workflow
- **综合**: 大小写差异需在文档中明确标注，避免用户迁移踩坑
- **是否有规避手段**: 是 — 用户可用 `startsWith(runner.os, 'L')` 或转小写比较

**建议**:
- 若平台有意返回小写，需在文档中明确标注
- 或统一为 "Linux"（与 GitHub Actions 一致以降低迁移摩擦）

---

## 失败分诊 · USE-SECNAME-01-001 · Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, run_status_not) — 期望 conclusion != COMPLETED（应报命名规则错误），实际 COMPLETED

**根因初判**: 产品缺陷

**责任人**: 平台方 — 平台未校验 secret 命名规则，`secrets.ATOMGIT_TOKEN` 被静默接受

**证据**:
- **Job 日志全量** (5 行): `token=***` — workflow 成功执行，ATOMGIT_TOKEN 被引用且脱敏输出
- **预期行为**: Secret 名称以 `ATOMGIT_` 开头的应被视为保留前缀，应在解析/校验阶段报错
- **实际行为**: 平台静默接受 `${{ secrets.ATOMGIT_TOKEN }}` 并正常返回脱敏后的 token 值——但这实际上是系统的 ATOMGIT_TOKEN，不是用户自建的 secret；请求系统保留前缀的 secret 名未被拒绝
- **对照 GitCode 规格** `using-secrets.md`：ATOMGIT_ 前缀为系统保留

**置信度**: 中（需要对照确认 GitCode 是否确实保留 ATOMGIT_ 前缀——若文档未明确声明保留前缀，则属于文档缺口）

**影响**:
- **阻塞性**: ⚪无影响 — workflow 正常
- **静默性**: 🟡可察觉 — 用户使用 ATOMGIT_TOKEN 实际上拿到了系统 token
- **影响面**: 🟢单用例
- **综合**: 需确认——若文档未声明 ATOMGIT_ 前缀保留规则，归因应转为「文档缺口」
- **是否有规避手段**: 否

**建议**:
- 若平台有意保留 ATOMGIT_ 前缀，应在文档和 YAML 校验中明确声明

---

## 汇总

| 根因分类 | 计数 | 用例 |
|---------|------|------|
| **产品缺陷** | 12 | COMPAT-CACHE-01-001, COMPAT-INPUTS-01-001, COMPAT-VARS-01-006, USE-CONC-01-001, USE-CTX-01-001, USE-CTX-01-002, USE-DISP-01-002, USE-ENV-01-002, USE-EXPR-01-001, USE-INPT-01-002, USE-OS-01-001, USE-SECNAME-01-001 |
| **用例问题** | 5 | COMPAT-PERM-01-001, COMPAT-DIR-01-002, COMPAT-RUNSON-01-002, USE-LOG-01-001, USE-MD-01-001 |
| **环境问题** | 3 | COMPAT-ARTIFACT-01-001, COMPAT-ARTIFACT-01-002, USE-ANNOT-01-002 |
| **标记不匹配** | 2 | COMPAT-OUTCOME-01-002, COMPAT-OUTCOME-01-003 |
| **需人工判断** | 0 | — |

**关键发现**:
1. **产品缺陷高发**: 12/22 (55%) 为平台侧缺陷，集中于 inputs 类型校验缺失、atomgit.ref 格式不符文档、未知属性静默为空、GITHUB_* 缺少迁移提示
2. **静默错误模式突出**: 多个缺陷表现为"平台不报错但给出错误/占位符结果"——用户极难发现，潜在影响大
3. **断言设计缺陷**: 5 条用例因断言/编译器问题产生假阳性，需 Phase 01 修
4. **环境残留**: 2 条 artifact 用例因名称冲突失败，harness 需改进清理逻辑
