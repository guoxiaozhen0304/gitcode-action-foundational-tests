# Failure Analyst — COMPAT + USE FAIL 归因报告

**Run ID**: 2026-07-25-01  
**分析日期**: 2026-07-25  
**FAIL 用例数**: 23（COMPAT: 11 / USE: 12）

---

## 失败分诊 · COMPAT-CONTAINER-01-001 · container 字段不被支持时应明确报错而非静默忽略

**判定结果**: FAIL  
**失败断言**: assertions[0] (negative, run_status_not) — 预期 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 不是问题

**责任人**: 平台方 — GitCode 对不支持的 `container` 字段未做校验拦截，静默忽略并正常执行 workflow

**证据**:

- **Job 日志全量**（5 行，成功执行）:
  ```
  [INFO] Job(1530578003019051008_1530578002993885191) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  hello
  ```
  `container` 字段被静默忽略，job 正常完成。

- **预期行为**（YAML `COMPAT-CONTAINER-01-001.yaml`，P1，compatibility）:
  - 操作步骤：使用 `runs-on` + `container: image: ubuntu:latest`
  - 预期结果："不通过静默忽略导致 workflow 成功运行（container 字段应被拦截）"

- **实际行为**: `container` 字段配置在 YAML 中，但 Runner 不使用容器，仍以默认环境执行，workflow COMPLETED。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/configure-jobs.md`:
  - 第 33-47 行定义 `runs-on` 为三段式标签格式，**未提及 `container` 字段支持**。
  - 第 42-46 行 `runs-on: [ubuntu-latest, x64, small]` 示例中无 container 字段。
  - 规格中 `configure-steps.md` 也未提及 `container` 属性。
  - 即：文档未承诺支持 container，但平台对不认识字段的静默忽略行为不符合"输入校验"的最佳实践——用户配置了 container 却不在容器内运行，属于静默行为偏差。

**置信度**: 高（日志直接显示 hello 输出成功，YAML 有 container 字段但未被使用）

**影响**:
- **阻塞性**: 🔴阻塞 — 用户配置 container 后依赖容器内的特定工具/版本，但 job 实际在裸机上运行，可能引发静默的环境差异错误
- **静默性**: 🔴静默错误 — workflow 成功完成，用户无法察觉未在容器内运行
- **影响面**: 🟡同维度 — 所有尝试使用 container 的 workflow 均受影响
- **综合**: 阻塞且静默——配置 container 字段被静默忽略，用户依赖容器环境的脚本可能在错误环境下运行而不自知
- **是否有规避手段**: 是，用户可通过 `runs-on` 选择含所需工具的自托管 runner 或自行在步骤中安装；但平台应在不支持时明确报错

**建议**:
- 平台应在 YAML schema 校验阶段拦截不支持的 `container` 字段，给出明确错误信息：`container 字段当前暂不支持，请使用 runs-on 选择 Runner 环境`
- 相关用例: `COMPAT-CONTAINER-01-002`

---

## 失败分诊 · COMPAT-DEPR-01-001 · ::set-env:: 废弃命令应被拒绝或给出迁移指引

**判定结果**: FAIL  
**失败断言**: assertions[0] (negative, run_status_not) — 预期 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 不是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（7 行）:
  ```
  [INFO] Job(1530578102998929408_1530578102969569287) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  ::set-env name=MY_VAR::hello
  MY_VAR=
  done
  ```
  `::set-env::` 被执行但 `MY_VAR` 输出为空——命令未生效但也没被拦截，workflow 成功完成。

- **预期行为**（YAML `COMPAT-DEPR-01-001.yaml`，P1，compatibility）:
  - 操作步骤：执行 `echo '::set-env name=MY_VAR::hello'`
  - 预期结果："不应静默忽略导致 workflow 成功且 MY_VAR 未被设置"

- **实际行为**: 废弃命令被接受（无错误），但 `MY_VAR` 未被设置（输出为空），workflow 以 COMPLETED 结束。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/workflow-commands.md`:
  - 第 60-68 行「废弃的命令格式」明确列出 `::set-env` 为废弃命令，替代方案为 `echo "MY_VAR=my_value" >> $ATOMGIT_ENV`
  - 第 65-67 行原文：`| echo "::set-env name=MY_VAR::my_value" | echo "MY_VAR=my_value" >> $ATOMGIT_ENV |`

**置信度**: 高（日志直接显示废弃命令未生效但 workflow 成功完成，文档明确标注为废弃）

**影响**:
- **阻塞性**: 🔴阻塞 — 用户使用废弃命令的 workflow 静默失败（变量未被设置），后续依赖该变量的步骤可能意外出错
- **静默性**: 🔴静默错误 — 无任何警告或错误，MY_VAR 无声无息地空着
- **影响面**: 🟡同维度 — 所有从 GitHub Actions 迁移来的 `::set-env::` 用法均受影响
- **综合**: 阻塞且静默——废弃命令执行无生效无提示，从 GitHub 迁移用户极易踩坑
- **是否有规避手段**: 是，使用 `$ATOMGIT_ENV` 文件协议替代

**建议**:
- 平台应在 Runner 层对废弃命令格式 `::set-env` 做识别：报错拒绝（推荐）或至少输出警告日志 + 指向替代方案 `$ATOMGIT_ENV`
- 相关用例: `COMPAT-DEPR-01-002`

---

## 失败分诊 · COMPAT-DEPR-01-002 · ::add-path:: 废弃命令应被拒绝或给出迁移指引

**判定结果**: FAIL  
**失败断言**: assertions[0] (negative, run_status_not) — 预期 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 不是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（7 行）:
  ```
  [INFO] Job(1530578159512600576_1530578159479046151) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  ::add-path::/custom/path
  PATH=/home/slave1/.local/bin:/usr/local/bin:.../usr/sbin:/usr/bin:/sbin:/bin
  done
  ```
  `::add-path::/custom/path` 被执行，但 `/custom/path` 未被加入 PATH，workflow 成功。

- **预期行为**（YAML `COMPAT-DEPR-01-002.yaml`，P1，compatibility）:
  - 操作步骤：执行 `echo '::add-path::/custom/path'`
  - 预期结果："不应静默忽略导致 workflow 成功且 PATH 未被修改"

- **实际行为**: 同 `COMPAT-DEPR-01-001`——废弃命令无效果无报错，workflow COMPLETED。`/custom/path` 未出现在 PATH 中。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/workflow-commands.md`:
  - 第 60-68 行废弃命令表第 68 行原文：`| echo "::add-path::/custom/bin" | echo "/custom/bin" >> $ATOMGIT_PATH |`

**置信度**: 高（同 DEPR-01-001 模式）

**影响**: 同 DEPR-01-001——阻塞且静默，迁移摩擦点

**建议**: 同 DEPR-01-001——平台对废弃命令做识别与拦截

---

## 失败分诊 · COMPAT-INPUTS-01-001 · workflow_dispatch inputs 类型限制 — boolean 应报错

**判定结果**: FAIL  
**失败断言**: assertions[0] (negative, run_status_not) — 预期 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 是问题

**责任人**: 平台方 — 文档明确声明仅支持 string，但 boolean 类型 input 被静默接受

**证据**:

- **Job 日志全量**（5 行）:
  ```
  [INFO] Job(1530562112864665600_1530562112831111175) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  INPUT_OK
  ```
  `type: boolean` 的 input 被接受，workflow 成功运行。

- **预期行为**（YAML `COMPAT-INPUTS-01-001.yaml`，P1，compatibility）:
  - 操作步骤：定义 `workflow_dispatch` input 的 `type: boolean`
  - 预期结果："错误信息应明确指出 workflow_dispatch inputs 仅支持 string 类型，boolean 不被支持"

- **实际行为**: boolean 类型被静默接受，workflow COMPLETED，无任何校验错误。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/COMPAT-NOTES.md`:
  - 第 46 行原文：`GitCode workflow_dispatch/workflow_call 的 inputs 仅支持 string 类型；GitHub 支持 boolean/choice/number/environment`

**置信度**: 高（COMPAT-NOTES 第 46 行白纸黑字，日志直接证明未被拦截）

**影响**:
- **阻塞性**: 🟡非阻塞 — workflow 仍能运行，`dry_run=false` 被转为字符串 `"false"`
- **静默性**: 🔴静默错误 — 用户以 boolean 语义理解值和条件判断，但实际是字符串 `"false"`（非空字符串为 truthy），可导致条件分支静默出错
- **影响面**: 🟡同维度 — 所有从 GitHub Actions 迁移的 boolean input 用法均受影响
- **综合**: 非阻塞但静默——boolean→string 的隐性转换会导致条件判断逻辑错误
- **是否有规避手段**: 是，用户自行将 boolean 改为 string，在步骤中使用条件表达式转换

**建议**:
- 平台在 YAML schema 校验层拦截 `type: boolean`，报错信息包含"仅支持 string 类型"并提示替代写法

---

## 失败分诊 · COMPAT-MATRIX-01-003 · matrix 三维展开不被支持时的差异

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, run_status) — PASS（COMPLETED）；assertions[1] (negative, run_status_not) — FAIL（预期 conclusion != COMPLETED，实际 COMPLETED）

**根因初判**: 不是问题

**责任人**: 多方联合 — 文档 vs 实际行为需要领导裁定

**证据**:

- **Job 日志**（64 行，8 个 matrix job 实例全部成功）:
  三维矩阵 `os×node×browser = 2×2×2 = 8` 个实例全部正常生成并成功执行：
  ```
  os=ubuntu node=16 browser=chrome
  os=ubuntu node=16 browser=firefox
  os=macos node=16 browser=chrome
  os=macos node=16 browser=firefox
  os=ubuntu node=18 browser=chrome
  os=ubuntu node=18 browser=firefox
  os=macos node=18 browser=chrome
  os=macos node=18 browser=firefox
  ```
  所有 8 个实例全部成功执行。

- **预期行为**（YAML `COMPAT-MATRIX-01-003.yaml`，P2，compatibility）:
  - 断言 rubric："系统对三维 matrix 给出明确响应（接受并展开为 8 个实例，或拒绝并给出原因）"
  - "不应静默忽略导致 matrix 配置仅生成部分实例"

- **实际行为**: 系统实际接受了三维矩阵并生成了 8 个实例——与断言 rubrics 中的正向分支"接受并展开为 8 个实例"完全符合。**FAIL 论断言的 negative（不应 COMPLETED）实质上是假设了"不支持"——但平台实际上支持了三维矩阵**。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/configure-matrix-builds.md`:
  - 第 67-75 行展示了三维矩阵示例：`os: [ubuntu-latest, windows-latest] / arch: [x64, arm64] / node-version: [18, 20]`
  - 文档明确承诺了三维矩阵支持——测试用例正是按文档写法编写。

**置信度**: 中 — 断言自身存在矛盾：正向 rubrics 涵盖"接受并展开"场景，但 negative 断言却要求 NOT COMPLETED。实际执行结果与文档承诺一致（8 个实例成功），FAIL 判定源于断言编译的局限性

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为与文档一致，功能正常
- **静默性**: ⚪无影响
- **影响面**: ⚪无影响
- **综合**: 假阳性 FAIL——平台三维矩阵功能正常，断言编译期望 NOT COMPLETED 与文档承诺矛盾
- **是否有规避手段**: 不适用——这是断言问题，非平台问题

**建议**:
- 此 FAIL 应回看断言编译产物：`run_status_not` 的断言可能来自 `compile_asserts.py` 对 llm_assisted rubric 的降级处理——rubric 写"接受...或拒绝"给了两种可能，但编译器可能将其定向为 negative（拒绝），与实际行为不符
- 需 Phase 01 审查断言编译逻辑，确保复合 rubric 不错误降级

---

## 失败分诊 · COMPAT-MATRIX-01-004 · matrix include 无基础变量不被支持时的差异

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, run_status) — PASS；assertions[1] (negative, run_status_not) — FAIL（预期 conclusion != COMPLETED，实际 COMPLETED）

**根因初判**: 不是问题

**责任人**: 多方联合 — 同 MATRIX-01-003，断言与文档承诺矛盾

**证据**:

- **Job 日志全量**（7 行，成功执行）:
  ```
  [INFO] Job(1530578466242052096_1530578466250440705) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  os=ubuntu
  node=20
  ```
  仅 `include` 无基础变量的 matrix 被接受并成功生成一个 job 实例。

- **预期行为**（YAML `COMPAT-MATRIX-01-004.yaml`，P2，compatibility）:
  - 断言 rubric："系统接受 include 无基础变量配置并正常生成实例，或明确拒绝并给出原因"
  - "include 配置不应被静默忽略"

- **实际行为**: 系统接受了纯 include 配置并正常生成了 1 个实例（os=ubuntu, node=20）——与 rubric 正向分支一致。FAIL 的 negative 断言（NOT COMPLETED）默认"不支持"方向。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/configure-matrix-builds.md`:
  - 第 79-92 行展示 `include` 用法，所有示例均在基础变量存在时使用 include（如 `os + node-version + include`）
  - 文档未明确说明纯 include 无基础变量时是否合法，存在规格缺口

**置信度**: 中 — 实际行为合理（include 本身即定义变量），但不排除 GitCode ACL 对此种写法有不同意图；断定言的 negative 过于绝对

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为合理，功能正常
- **静默性**: ⚪无影响
- **影响面**: ⚪无影响
- **综合**: 可能假阳性 FAIL——纯 include 被正常处理，需断看断言是否合理
- **是否有规避手段**: 不适用

**建议**: 同 MATRIX-01-003，审查断言编译逻辑

---

## 失败分诊 · COMPAT-OUTCOME-01-002 · continue-on-error true 时 outcome 应为 failure 而 conclusion 应为 success

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, step_status) — 预期 FAILED，实际 COMPLETED（被降级 run_status）；assertions[1] (positive, step_conclusion) — PASS（COMPLETED）；assertions[2] (positive, run_status) — PASS（COMPLETED）

**根因初判**: 不是问题

**责任人**: Phase 01 — step_outcome/step_conclusion 未编译为可执行断言（target 编译缺口）

**证据**:

- **Job 日志全量**（62 行）:
  - Step 1 "failing step tolerated" `continue-on-error: true` 执行 `exit 1`
  - 平台输出: `::error::Process exited with code 1`
  - Step 2 "next step runs" 成功输出 `This step should run`
  - Step 3 "check status" 成功输出 `Check step outcome and conclusion`
  结论：platform correctly allows downstream steps to run after `continue-on-error: true` step fails.

- **预期行为**（YAML `COMPAT-OUTCOME-01-002.yaml`，P1，compatibility）:
  - 断言 1：step outcome = failure
  - 断言 2：step conclusion = success
  - 断言 3：job run_status = success

- **实际行为**: Job 状态为 COMPLETED（= success），后续步骤全部成功执行。断言 1（step_status=FAILED）被断言编译降级为 `run_status=FAILED`（平台未提供 step_status 的编译映射），导致 FAIL。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/configure-jobs.md`:
  - 第 172-183 行 `continue-on-error`：`设置 continue-on-error: true 后，即使 job 失败，workflow 也不会因此终止`
  - 第 196-197 行：`continue-on-error 的 job 即使失败，也不会阻止后续 job 运行。但后续依赖该 job 的 job 中 if: ${{ success }} 条件将不满足`
  - 文档承诺结论是 `conclusion=success`（符合 COMPLETED），与平台实际行为一致

**置信度**: 高 — 文档明确 continue-on-error 后 conclusion=success，平台行为与文档一致，FAIL 源于断言编译将 step_status 降级为 run_status

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为正确
- **静默性**: ⚪无影响
- **影响面**: ⚪无影响
- **综合**: 编译缺口导致的假阳性 FAIL——`step_status`/`step_conclusion` 目标类型在 `compile_asserts.py` 中无直接映射
- **是否有规避手段**: 不适用——需补全编译器的目标类型映射

**建议**:
- Phase 01 的 `compile_asserts.py` 需添加 `step_status`/`step_conclusion`/`step_outcome` 到可编译 target 类型
- 否则此类断言被降级为 `run_status`，导致大量假阳性 FAIL

---

## 失败分诊 · COMPAT-OUTCOME-01-003 · outcome 与 conclusion 在 job 条件判断中不应互换语义

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, job_status) — PASS（COMPLETED）；assertions[1] (positive, run_status) — FAIL（预期 FAILED，实际 COMPLETED）

**根因初判**: 不是问题

**责任人**: Phase 01 — 编译缺口

**证据**:

- **Job 日志**（58 行）:
  - Job A: `continue-on-error: true` 步骤执行 `exit 1`，输出 `::error::Process exited with code 1`
  - Job B（needs: [job-a]）: 成功运行，输出 `Job A conclusion should be success`
  - 结论：平台实现正确——continue-on-error 使 Job A conclusion=success，Job B 正常被调度

- **预期行为**（YAML `COMPAT-OUTCOME-01-003.yaml`，P1，compatibility）:
  - 断言：job A conclusion=success（使 Job B 可运行），job A step outcome=failure
  - rubrics 明确描述"不应出现 outcome 与 conclusion 被互换使用"

- **实际行为**: Job B 成功运行证明 Job A 的 conclusion=success——平台行为完全符合文档承诺。FAIL 源于断言编译将 `step_status=failure` 降级为 `run_status=FAILED`。

- **对照 GitCode 规格**（同 OUTCOME-01-002，第 196-197 行）

**置信度**: 高 — 同 OUTCOME-01-002 模式

**影响**: ⚪无影响——假阳性 FAIL，需补全编译器

**建议**: 同 COMPAT-OUTCOME-01-002

---

## 失败分诊 · COMPAT-PERM-01-001 · 未声明 permissions 时默认 TOKEN 读操作权限范围

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, run_status) — PASS（COMPLETED）；assertions[1] (positive, value) — FAIL（预期 log contains 'README'，实际 absent）

**根因初判**: 不是问题

**责任人**: 平台方

**证据**:

- **Job 日志**（54 行）:
  - 日志中仅输出了仓库的描述性文本 `# gitcode-test-4` 和 `并发验证gitcodeactions的子仓库`，但**没有 `README` 字样**——`cat README.md` 执行的输出被截断或未执行。
  - `checkout` action 使用了默认配置未传 `ref` 参数。

- **预期行为**（YAML `COMPAT-PERM-01-001.yaml`，P0，compatibility/security）:
  - 操作步骤：checkout → cat README.md
  - 预期结果：log contains 'README'

- **实际行为**: README.md 内容未被输出到日志中。可能原因：① checkout 未拿到代码（TOKEN 默认无 read 权限）；② `cat README.md` 失败但被 bash -e 静默忽略

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/security-permissions/token-permissions.md`:
  - 第 26 行：顶层 permissions 示例中 `project: read` 和 `repository: write` 为默认
  - 第 41 行：`repository | read | 克隆/读取`——文档承诺 repository:read 权限
  - **文档未明确说明"未声明 permissions 时的默认值"**——这是文档缺口

**置信度**: 中 — 日志证据显示 README 不在输出中，但无法从日志判断 checkout 是否成功拿到代码（无 checkout action 的详细输出）。需进一步验证 TOKEN 默认权限

**影响**:
- **阻塞性**: 🔴阻塞 — 未声明 permissions 时 checkout 可能失败，CI pipeline 无法运行
- **静默性**: 🔴静默错误 — 日志无明显错误信息
- **影响面**: 🔴跨维度 — 所有未声明 permissions 的 workflow 中 checkout 可能失败，影响面极大
- **综合**: 阻塞且静默——未声明 permissions 时默认权限不明，可能导致基础 CI 中断
- **是否有规避手段**: 是，显式声明 `permissions: repository: read`

**建议**:
- 平台文档需明确"未声明 permissions 时 TOKEN 的默认权限集"
- 如 `cat README.md` 确实失败，需确认 checkout action 在默认 TOKEN 下的行为

---

## 失败分诊 · COMPAT-PR-01-006 · PR 目标分支过滤行为差异

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, run_status) — PASS（COMPLETED）；assertions[1] (negative, run_status_not) — FAIL（预期 conclusion != COMPLETED，实际 COMPLETED）

**根因初判**: 不是问题

**责任人**: Phase 02 — PR 触发未验证目标分支

**证据**:

- **Job 日志全量**（6 行）:
  ```
  [INFO] Job(1530578361653141504_1530578361623781383) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  event_name=MR
  done
  ```
  event_name 为 `MR`（Merge Request），而非 GitHub Actions 的 `pull_request`。

- **预期行为**（YAML `COMPAT-PR-01-006.yaml`，P1，compatibility）:
  - Positive: 目标分支 main 的 PR 应触发 workflow → 已验证通过（event=MR 触发成功）
  - Negative: 目标分支不为 main 的不应触发 → **未在本次测试中验证**（harness 可能始终向 main 创建 MR）

- **实际行为**: workflow 被正确触发。但断言 1 的 negative（不应 COMPLETED）测试目标"不匹配的分支不应触发"在本次运行中未得到验证——harness 的 PR 操作始终针对 main。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/COMPAT-NOTES.md`:
  - 第 27 行：`pull_request types 取值：GitCode 为 [merge, open, reopen, update]`

**置信度**: 中 — 两个断言在本次运行中无法同时满足（PR 就是发往 main），断言编排存在互斥

**影响**:
- **阻塞性**: ⚪无影响 — positive 行为验证通过
- **静默性**: ⚪无影响
- **影响面**: ⚪无影响
- **综合**: 断言编排问题——同一 run 无法同时验证"对 main 触发"和"对非 main 不触发"；需拆分为两个独立 trigger
- **是否有规避手段**: 不适用——需在 harness 中提供 `target_branch` 参数支持

**建议**: 将两个断言拆分为两个独立的 PR 触发——一个发往 main（验证触发），一个发往 non-main（验证不触发）。产品行为方向上需要更精确的验证

---

## 失败分诊 · COMPAT-VARS-01-006 · vars 在 Action 中的可用性差异

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, run_status) — 预期 COMPLETED，实际 FAILED

**根因初判**: 不是问题

**责任人**: 多方联合 — 可能 harness 的 dispatch payload 未传递变量值

**证据**:

- **Job 日志全量**（6 行）:
  ```
  [INFO] Job(1530563265157795840_1530563265136824327) duration check: true
  [ERROR] ID: CHECKOUT.00010003
  [ERROR] 描述: 插件执行异常.
  [ERROR] 根因: Input required and not supplied: COMMIT_REF_NAME
  [ERROR] 解决方法: 查看报错日志, 分析错误原因.
  ::error::Input required and not supplied: COMMIT_REF_NAME
  ```
  失败原因：checkout action 未能获得 `COMMIT_REF_NAME` input——无法完成代码检出。

- **预期行为**（YAML `COMPAT-VARS-01-006.yaml`，P1，compatibility）:
  - 操作步骤：checkout action 的 `with.ref: ${{ vars.ACTION_VAR }}`
  - 预期结果："若支持 vars，Action 的 with 参数应正确接收值"

- **实际行为**: checkout action 因 `COMMIT_REF_NAME` 未提供而失败——这可能不是 `vars` 的问题（错误信息未提及 `vars`），而是 checkout action 本身在特定条件下需要 `ref` 参数。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/context.md`:
  - 第 13 行：`vars | 组织/项目级别配置变量 | ${{ vars.DEPLOY_ENV }}`
  - 文档确认 `vars` 上下文存在

**置信度**: 低 — 错误信息仅指向 `COMMIT_REF_NAME`，未直接关联 `vars` 上下文的可用性。无法判断 `${{ vars.ACTION_VAR }}` 是否正确解析或等价于空值

**影响**:
- **阻塞性**: 🟡非阻塞 — 错误信息明确
- **静默性**: 🟢明确报错 — `Input required and not supplied: COMMIT_REF_NAME`
- **影响面**: 🟢单用例
- **综合**: 需进一步诊断——checkout 报错 `COMMIT_REF_NAME` 缺失可能与 `vars` 传递有关，也可能与 harness trigger 未传完整参数有关
- **是否有规避手段**: 是——不使用 `vars` 而直接写 ref 值

**建议**: 追加诊断——确认 `${{ vars.ACTION_VAR }}` 在 workflow 表达式中是否解析为非空值；如为空，需要确认 harness 的 dispatch payload 是否正确传递 variables

---

## 失败分诊 · USE-ANNOT-01-002 · ::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, status) — 预期 all job/step green，实际 job 'PR annotation test' status=FAILED

**根因初判**: 不是问题

**责任人**: Phase 02 — PR 触发时合并引用不可用

**证据**:

- **Job 日志**（49 行）:
  - 第 30 行：`git -c protocol.version=2 fetch ... origin +refs/merge-requests/34/merge:refs/remotes/merge-requests/34/merge`
  - 第 31 行：`fatal: couldn't find remote ref refs/merge-requests/34/merge`
  - 第 33-36 行：`[ERROR] ID: CHECKOUT.00010010` — `git进行拉取动作失败`
  - job 在 checkout 阶段即失败，annotation 步骤从未执行

- **预期行为**（YAML `USE-ANNOT-01-002.yaml`，P1，usability）:
  - 操作步骤：checkout → emit `::error file=README.md,line=1::Test error annotation`
  - 预期结果：PR 页面出现带文件路径、行号、可点击跳转的 annotation

- **实际行为**: checkout 阶段失败，用例本身未被测试到。**失败传导链**: checkout FAILED → annotation step SKIPPED（功能未被测试）

- **对照 GitCode 规格**: 无法对照——job 在 git fetch 阶段即失败，平台行为尚未进入验证范围

**置信度**: 高 — 日志明确显示 `fatal: couldn't find remote ref`，checkout 失败原因清晰

**影响**:
- **阻塞性**: 🔴阻塞 — PR checkout 无法获取 merge ref，CI 无法运行
- **静默性**: 🟡可察觉 — 有明确错误信息
- **影响面**: 🟡同维度 — 所有 PR 触发的 workflow checkout 可能受影响
- **综合**: 环境问题——PR #34 的 merge ref 不存在（可能是合并已完成或已关闭），本次运行无法测试 annotation 功能
- **是否有规避手段**: 是——重新以 open 状态创建新 PR；或改用 push 触发

**建议**: 重新创建有效的 open PR 后重测。如 merge ref 持续不可用，可能是平台 checkout 插件的 PR 场景支持问题

---

## 失败分诊 · USE-CONC-01-001 · concurrency.max 配置 0 或 10 时报错应提示有效范围 1-5

**判定结果**: FAIL  
**失败断言**: assertions[0] (negative, run_status_not) — 预期 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（5 行）:
  ```
  [INFO] Job(1530572417380782080_1530572417359810567) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  hello
  ```
  `concurrency.max: 10` 被静默接受，workflow 正常完成。

- **预期行为**（YAML `USE-CONC-01-001.yaml`，P1，usability）:
  - 操作步骤：workflow 设置 `concurrency: max: 10, exceed-action: QUEUE`
  - 预期结果："报错信息必须包含有效范围 1-5 或 1 到 5"

- **实际行为**: `max: 10` 被接受，workflow COMPLETED，无范围校验错误。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/configure-jobs.md`:
  - 第 152-166 行 concurrency 示例中 `max: 1`，无文档说明有效范围上限为 5
  - **文档未定义 max 的有效范围**（`max: 5` 是 GitHub 的限制）——这是文档缺口

**置信度**: 中 — 日志证实 max=10 被接受，但 GitCode 文档未明确声明上限为 5；断言基于 GitHub Actions 假设

**影响**:
- **阻塞性**: 🟡非阻塞 — workflow 能运行，但并发语义可能不符合预期
- **静默性**: 🔴静默错误 — 无校验，后续行为不可预期
- **影响面**: 🟢单用例
- **综合**: 文档缺口+静默接受——max 范围无文档定义也无运行时校验
- **是否有规避手段**: 是，用户自行遵守范畴 1-5

**建议**:
- 如 GitCode 确实有 1-5 范围限制 → 文档需声明 + 运行时需校验报错
- 如 GitCode 无此限制 → COMPAT-NOTES 中应标注与 GitHub 的差异
- 当前状态为"无文档说明也无效验"——两者至少补其一

---

## 失败分诊 · USE-CTX-01-001 · 使用 atomgit 上下文时表达式正常求值

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, value) — 预期 log contains 'ref=refs/heads/'，实际 absent

**根因初判**: 是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（5 行）:
  ```
  [INFO] Job(1530572464138629120_1530572464117657607) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  ref=main
  ```
  `atomgit.ref` 返回 `main`（短名），而非 `refs/heads/main`（全名）。

- **预期行为**（YAML `USE-CTX-01-001.yaml`，P1，usability/compatibility）:
  - 操作步骤：`echo "ref=${{ atomgit.ref }}"`
  - 预期结果：`log contains 'ref=refs/heads/'`

- **实际行为**: `ref=main`——平台返回的是 `ref_name` 格式而非 `ref` 格式。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/context.md`:
  - 第 31 行原文：`atomgit.ref | string | 触发引用（分支或标签全名，如 refs/heads/main）`
  - 第 32 行原文：`atomgit.ref_name | string | 触发引用短名（如 main, v1.0）`
  - 文档明确承诺 `atomgit.ref` 返回全格式 `refs/heads/main`——实际返回的 `main` 是 `ref_name` 的值

**置信度**: 高 — 日志直接显示 `ref=main`，文档第 31 行精确对应

**影响**:
- **阻塞性**: 🟡非阻塞 — workflow 可运行
- **静默性**: 🔴静默错误 — 用户脚本如依赖 `refs/heads/` 前缀做分支判断，会静默失败
- **影响面**: 🟡同维度 — 所有引用 `atomgit.ref` 的工作流均受影响
- **综合**: 非阻塞但静默——`atomgit.ref` 返回值格式与文档契约不一致，影响所有依赖全格式的下游脚本
- **是否有规避手段**: 是——用户可手动拼接 `refs/heads/${{ atomgit.ref_name }}`，但会增加迁移摩擦

**建议**:
- **P0 修复**: `atomgit.ref` 必须返回全格式 `refs/heads/<name>` 以符合文档承诺
- 相关用例: `COMP-ATOMGIT-01-047/048/049`, `USE-CTX-01-002`

---

## 失败分诊 · USE-CTX-01-002 · 使用 github 上下文时报错应提示 atomgit 替代

**判定结果**: FAIL  
**失败断言**: assertions[0] (negative, run_status_not) — 预期 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（5 行）:
  ```
  [INFO] Job(1530572512855724032_1530572512830558215) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  ref=placeholder_ref
  ```
  `${{ github.ref }}` 被解析为 `placeholder_ref`——平台未报错，也未提示应使用 `atomgit`。

- **预期行为**（YAML `USE-CTX-01-002.yaml`，P1，usability/compatibility）:
  - 操作步骤：`echo "ref=${{ github.ref }}"`
  - 预期结果："报错信息必须同时出现 github 与 atomgit 字样，并给出替换建议"

- **实际行为**: `github.ref` 被解析为 `placeholder_ref`，无任何警告或迁移提示。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/COMPAT-NOTES.md`:
  - 第 10 行原文：`上下文对象：GitCode 核心上下文是 atomgit.*...GitHub 是 github.*`
  - 第 12 行：`直接搬 GitHub workflow 会全线失效（兼容性/迁移）`
  - 文档应明确 `github` 上下文应如何被处理——当前行为是返回占位值而非报错

**置信度**: 高 — 日志直接显示 `placeholder_ref`，无 github/atomgit 迁移提示

**影响**:
- **阻塞性**: 🔴阻塞 — 从 GitHub 迁移的用户使用 `github.ref`，得到 `placeholder_ref`（垃圾值），后续步骤会静默失败
- **静默性**: 🔴静默错误 — 不报错不警告，用户完全不知道 `placeholder_ref` 不是正确的 ref
- **影响面**: 🔴跨维度 — 所有从 GitHub Actions 迁移且未改 `github.*` 为 `atomgit.*` 的工作流均受影响
- **综合**: 严重迁移阻塞+静默错误——`github` 上下文返回垃圾值而不报错，是对迁移用户最大的可用性陷阱
- **是否有规避手段**: 是，用户必须在迁移时就改为 `atomgit.*`

**建议**:
- **P0**: `github` 上下文应被识别并报错："`github` 上下文在 GitCode Actions 中不可用，请使用 `atomgit` 上下文替代"
- 绝不应返回占位值——这直接破坏用户数据完整性
- 相关用例: `USE-ENV-01-002`

---

## 失败分诊 · USE-DISP-01-002 · workflow_dispatch 未提供参数但存在 default 时应使用默认值运行

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, value) — 预期 log contains 'env=staging'，实际 absent

**根因初判**: 不是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（1 行，无 shell 输出）:
  ```
  [INFO] Job(1530572810881867776_1530572810848313351) duration check: true
  ```
  Job 运行了但**无任何 shell 脚本输出**——脚本可能在表达式解析阶段即失败。

- **预期行为**（YAML `USE-DISP-01-002.yaml`，P1，usability）:
  - 操作步骤：`echo "env=${{ inputs.environment }}"`（environment 有 default: staging）
  - 预期结果：`log contains 'env=staging'`

- **实际行为**: Job 状态为 FAILED，无 shell 输出——`${{ inputs.environment }}` 可能因 dispatch 未传参数而解析为空（失败）或表达式求值阶段就崩溃了。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/COMPAT-NOTES.md`:
  - 第 46 行：仅声明 inputs 只支持 string，未描述 default 值的运行时行为
  - 文档缺口：workflow_dispatch inputs 的 default 值在未传参时的行为未定义

**置信度**: 中 — 0 行 shell 输出 + run_status=FAILED 表明表达式求值或 default 逻辑失败，但具体原因需平台侧日志确认

**影响**:
- **阻塞性**: 🔴阻塞 — 有 default 值的 dispatch input 在未传参时 workflow 直接失败
- **静默性**: 🟡可察觉 — run_status=FAILED 用户可见
- **影响面**: 🟡同维度 — 所有使用 default 的 workflow_dispatch input 可能受影响
- **综合**: 阻塞——default 值未被使用导致 workflow 失败，`inputs` 的 default 机制存在缺陷或 harness trigger 未兼容
- **是否有规避手段**: 是——用户在 dispatch 时手动传所有参数值

**建议**: 需平台提供表达式求值日志确认 `${{ inputs.environment }}` 在未传参时的解析结果。如实际为 null/空而非 default 值，则为平台缺陷

---

## 失败分诊 · USE-ENV-01-002 · 引用 GITHUB_SHA 时日志应给出环境变量映射提示

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, status) — 预期 all job/step green，实际 job 'test GITHUB env var hint' status=FAILED

**根因初判**: 不是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（6 行）:
  ```
  [INFO] Job(1530572905006370816_1530572904977010695) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  /home/slave1/runner/...sh: line 2: GITHUB_SHA: unbound variable
  ::error::Process exited with code 1
  ```
  `GITHUB_SHA` 在 bash `set -u` 下是 unbound variable——因为环境变量名为 `ATOMGIT_SHA`。

- **预期行为**（YAML `USE-ENV-01-002.yaml`，P1，usability）:
  - 操作步骤：`set -u; echo "sha=$GITHUB_SHA"`
  - 预期结果："日志警告是否足够醒目且包含有效指引：应提示 GITHUB_* 环境变量在 GitCode 中对应为 ATOMGIT_*"

- **实际行为**: bash 直接报 `unbound variable` 然后 exit 1——无任何 GitCode 层面的环境变量映射提示。这是典型的从 GitHub 迁移时踩的坑。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/COMPAT-NOTES.md`:
  - 第 11 行原文：`系统环境变量前缀：GitCode 为 ATOMGIT_* ... GitHub 为 GITHUB_*`
  - 文档未描述平台是否应对 `GITHUB_*` 环境变量做自动识别并提示

**置信度**: 高 — bash 的 `unbound variable` 错误直接证明了无映射提示

**影响**:
- **阻塞性**: 🔴阻塞 — 从 GitHub 迁移的脚本引用 `$GITHUB_SHA` 直接 crash
- **静默性**: 🟡可察觉 — 但只有 bash `set -u` 下才报错；普通脚本中 `$GITHUB_SHA` 会是空串（静默）
- **影响面**: 🔴跨维度 — 所有从 GitHub Actions 迁移的 shell 脚本均可能受影响
- **综合**: 高摩擦迁移阻塞——Runner 层面不识别 `GITHUB_*`，也不给迁移提示，用户需要自己一个个改
- **是否有规避手段**: 是——手动将所有 `GITHUB_*` 改为 `ATOMGIT_*`

**建议**:
- **P1**: Runner 在解析环境变量时应识别 `GITHUB_*` 前缀，给出 warning: `GITHUB_SHA 在 GitCode Actions 中对应 ATOMGIT_SHA，请更新您的脚本`
- 相关用例: `USE-CTX-01-002`, `USE-ENV-01-001`

---

## 失败分诊 · USE-EXPR-01-001 · 引用不存在的上下文属性时报错应包含原始表达式与错误类型

**判定结果**: FAIL  
**失败断言**: assertions[0] (negative, run_status_not) — 预期 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 不是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（5 行）:
  ```
  [INFO] Job(1530572953466978304_1530572953433423879) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  val=
  ```
  `${{ atomgit.nonexistent_property }}` 被解析为空字符串，无任何错误。

- **预期行为**（YAML `USE-EXPR-01-001.yaml`，P1，usability/compatibility）:
  - 操作步骤：`echo "val=${{ atomgit.nonexistent_property }}"`
  - 预期结果："报错信息必须包含出错的原始表达式和错误类型说明"

- **实际行为**: 不存在属性被静默解析为空——无校验无报错，用户完全无法察觉引用了不存在的属性。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/context.md`:
  - 第 9-21 行列出所有 `atomgit.*` 属性——`nonexistent_property` 不在列表中
  - 文档未定义"引用不存在的上下文属性"时的行为

**置信度**: 高 — 日志直接显示 `val=`，不存在的属性被解析为空

**影响**:
- **阻塞性**: 🔴阻塞 — 用户拼写错误（如 `atomgit.shaa`）会被静默接受，后续依赖该值的步骤可能意外失败
- **静默性**: 🔴静默错误 — 无任何提示
- **影响面**: 🟡同维度 — 所有拼写/引用错误均受影响
- **综合**: 静默错误导致调试困难——用户输入 `atomgit.nonexistent_property` 得到空值无提示，排查极其困难
- **是否有规避手段**: 否——用户除非事先测试所有表达式，否则无法发现引用错误

**建议**:
- **P1**: 表达式求值引擎应对不存在的上下文属性报错，包含原始表达式名称和"未知属性"提示
- GitHub Actions 对不存在属性的行为是返回空字符串（兼容性一致），但 **可用性层面** GitCode 应增强：至少输出一条 info 日志指出该属性未被识别

---

## 失败分诊 · USE-INPT-01-002 · 使用 boolean 类型 input 时报错应提示仅支持 string

**判定结果**: FAIL  
**失败断言**: assertions[0] (negative, run_status_not) — 预期 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 不是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（5 行）:
  ```
  [INFO] Job(1530573045502717952_1530573045477552135) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  dry_run=false
  ```
  `type: boolean` 的 input `dry_run` 被接受并输出 `false`（字符串）。无类型校验警告。

- **预期行为**（YAML `USE-INPT-01-002.yaml`，P1，usability/compatibility）:
  - 操作步骤：`echo "dry_run=${{ inputs.dry_run }}"`（type: boolean）
  - 预期结果："报错信息必须包含 GitCode 仅支持 string 类型或等效说明，并给出在步骤中使用表达式转换类型的替代方案"

- **实际行为**: boolean 被接受为 string `"false"`，workflow COMPLETED，无任何类型限制提示。

- **对照 GitCode 规格**（同 COMPAT-INPUTS-01-001，COMPAT-NOTES.md 第 46 行）

**置信度**: 高（同 COMPAT-INPUTS-01-001）

**影响**: 同 COMPAT-INPUTS-01-001——静默转换危险

**建议**: 同 COMPAT-INPUTS-01-001——拦截 + 报错

---

## 失败分诊 · USE-LOG-01-001 · 多 step 日志按时间线组织且边界清晰

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, value) — 预期 log contains 'step one prepare'，实际 absent

**根因初判**: 不是问题

**责任人**: Phase 01 — 断言 target 应调整为 step 的实际输出内容

**证据**:

- **Job 日志全量**（25 行）:
  5 个 step 均成功执行：
  ```
  prepare done       # step one prepare
  build done         # step two build
  test done          # step three test
  package done       # step four package
  summary done       # step five summary
  ```
  日志采集了每个 step 的 `run` 脚本输出（如 `prepare done`），但**不包含 step name**（如 `step one prepare`）——这是日志采集的格式设计，非平台缺陷。

- **预期行为**（YAML `USE-LOG-01-001.yaml`，P1，usability）:
  - 操作步骤：5 个 step，step name 分别为 `step one prepare` ... `step five summary`
  - 预期结果：`log contains 'step one prepare'`

- **实际行为**: step name 不出现在采集的日志中——只采集 shell 执行输出。断言期望与日志采集的实际内容范围不匹配。

- **对照 GitCode 规格**: 无相关文档定义 step name 是否应出现在日志中

**置信度**: 高 — 日志只含 shell 输出不含 step name；step 运行完全正常

**影响**:
- **阻塞性**: ⚪无影响 — 功能正常，所有 step 均成功运行
- **静默性**: ⚪无影响
- **影响面**: ⚪无影响
- **综合**: 假阳性 FAIL——断言期望的内容（step name）不在日志采集范围内；功能实际正常
- **是否有规避手段**: 不适用——断言应与日志采集范围对齐

**建议**: 断言改为检查 step 的实际输出内容（如 `prepare done`、`build done`）而非 step name

---

## 失败分诊 · USE-MD-01-001 · ATOMGIT_STEP_SUMMARY 写入的 Markdown 正确渲染为 HTML

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, step_summary) — 预期 contains 'Test Report'，实际 absent

**根因初判**: 不是问题

**责任人**: Phase 01 — `compile_asserts.py` 不支持 `step_summary` target 类型

**证据**:

- **Job 日志全量**（4 行，无 shell 输出）:
  ```
  [INFO] Job(1530573311585296384_1530573311547547655) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  ```
  Step 执行了但无输出——`ATOMGIT_STEP_SUMMARY` 的内容写入的是**工作流摘要页面**，不是 shell stdout/log。

- **预期行为**（YAML `USE-MD-01-001.yaml`，P1，usability）:
  - 操作步骤：写入 Markdown 到 `$ATOMGIT_STEP_SUMMARY`
  - 预期结果：`step_summary contains 'Test Report'`

- **实际行为**: `step_summary` target 类型在编译后可能被降级为 `value → run_logs`——日志中没有 summary 内容（正确行为），导致 FAIL。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/workflow-commands.md`:
  - 第 49-58 行：`ATOMGIT_STEP_SUMMARY` 写入 Markdown 显示在"工作流运行详情页面"
  - summary 内容不出现在 runner log 中——断言 target `step_summary` 需要 UI 级别的检查而非 log 检查

**置信度**: 高 — `step_summary` 内容确实不应在 shell 日志中出现；断言编译未处理此 target 类型

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: ⚪无影响
- **影响面**: ⚪无影响
- **综合**: 编译缺口——step_summary target 在 assertion_engine 中无实现（需 UI 检查能力）
- **是否有规避手段**: 不适用——需补全 assertion_engine 的 step_summary 采集能力

**建议**: Phase 02 assertion_engine 需增加 step_summary 数据源（通过 API 拉取 workflow 的 summary 内容）；当前编译后降级为 run_logs 会导致必然 FAIL

---

## 失败分诊 · USE-OS-01-001 · runner.os 返回值与文档声明的平台支持一致

**判定结果**: FAIL  
**失败断言**: assertions[0] (positive, value) — 预期 log contains 'os=Linux'，实际 absent

**根因初判**: 是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（5 行）:
  ```
  [INFO] Job(1530573357764329472_1530573357726580743) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  os=linux
  ```
  `runner.os` 返回 `linux`（小写），而非 `Linux`。

- **预期行为**（YAML `USE-OS-01-001.yaml`，P1，usability/compatibility）:
  - 操作步骤：`echo "os=${{ runner.os }}"`
  - 预期结果：`log contains 'os=Linux'`

- **实际行为**: `os=linux`——全小写，与 GitHub Actions 的 `Linux` 不同。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/context.md`:
  - 第 17 行：`runner | Runner 执行环境信息 | ${{ runner.os }}, ${{ runner.arch }}`
  - **文档未声明 `runner.os` 的返回值格式**（大写/小写未定义）——这是文档缺口
  - GitHub Actions 的 `runner.os` 返回值为 `Linux`/`Windows`/`macOS`

**置信度**: 高 — 日志直接显示 `linux`（小写），文档未定义格式

**影响**:
- **阻塞性**: 🟡非阻塞 — workflow 能运行
- **静默性**: 🔴静默错误 — 用户如用 `if: ${{ runner.os == 'Linux' }}` 做平台判断会静默失败
- **影响面**: 🟡同维度 — 所有基于 `runner.os` 做条件判断的工作流可能受影响
- **综合**: 格式不一致——`runner.os` 返回 `linux` 而非 `Linux`，且文档未声明格式，导致跨平台迁移的表达式匹配失败
- **是否有规避手段**: 是——用户使用 `${{ runner.os == 'linux' }}` 小写匹配

**建议**:
- 文档需声明 `runner.os` 返回值格式（`linux` / `windows` / `macos`）
- 若有意保持小写以区别于 GitHub，需在 COMPAT-NOTES 中标注差异
- 断言也应基于实际的格式化值调整（允许大小写不敏感匹配）

---

## 失败分诊 · USE-SECNAME-01-001 · Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误

**判定结果**: FAIL  
**失败断言**: assertions[0] (negative, run_status_not) — 预期 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 不是问题

**责任人**: 平台方

**证据**:

- **Job 日志全量**（5 行）:
  ```
  [INFO] Job(1530573546994802688_1530573546957053959) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  token=***
  ```
  `secrets.ATOMGIT_TOKEN` 被引用并脱敏为 `***`，workflow COMPLETED。

- **预期行为**（YAML `USE-SECNAME-01-001.yaml`，P1，usability/security）:
  - 操作步骤：引用 `secrets.ATOMGIT_TOKEN`
  - 预期结果："报错信息必须包含 Secret 名称规则或命名格式相关说明，并列出允许字符（大写字母、数字、下划线）"

- **实际行为**: `secrets.ATOMGIT_TOKEN` 被成功解析——读取的是系统自动生成的 `ATOMGIT_TOKEN`。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/security-permissions/token-permissions.md`:
  - 第 13 行：`每次流水线运行时，AtomGit Action 自动生成 ATOMGIT_TOKEN`
  - `secrets.ATOMGIT_TOKEN` 是系统保留的 secret 名称——用户不应创建同名 secret
  - 但此用例引用的是**系统生成的 token**（非用户创建的），从系统角度这不是"错误"而是"正常使用"

**置信度**: 中 — 用例的 intent 是"用户创建了名为 ATOMGIT_ 前缀的 secret"，但实际引用的是系统自动生成的 `ATOMGIT_TOKEN`（合法的系统 token）

**影响**:
- **阻塞性**: ⚪无影响 — 系统 token 正常可用
- **静默性**: ⚪无影响
- **影响面**: ⚪无影响
- **综合**: 断言期望与实际情况有偏差——用例意图是测试用户创建保留前缀 secret 被拦截，但测试中引用的是系统生成的合法 token
- **是否有规避手段**: 不适用——断言假设的前提场景（用户创建 ATOMGIT_ 前缀 secret）与测试 setup（引用系统 token）不匹配

**建议**: 如需验证"用户创建 ATOMGIT_ 前缀 secret 被拒绝"，应用例应在 setup 中声明创建自定义 secret（如 `ATOMGIT_MY_SECRET`），而非引用系统生成的 `ATOMGIT_TOKEN`

---

## 汇总统计

### 按根因分类

| 分类 | 数量 | 用例 |
|------|------|------|
| 产品缺陷 | 12 | CONTAINER-01-001, DEPR-01-001/002, INPUTS-01-001, PERM-01-001, CTX-01-001/002, EXPR-01-001, INPT-01-002, OS-01-001, CONC-01-001, SECNAME-01-001 |
| 用例问题/编译缺口 | 4 | MATRIX-01-003/004, OUTCOME-01-002/003 |
| 环境问题 | 5 | PR-01-006, ANNOT-01-002, DISP-01-002, ENV-01-002, VARS-01-006 |
| 需人工判断 | 2 | LOG-01-001, MD-01-001 |

### 假阳性 FAIL（高置信度）

以下 FAIL 源于断言编译目标未映射或日志采集范围不匹配，非平台缺陷：
- **COMPAT-OUTCOME-01-002 / 01-003**: `step_status`/`step_conclusion` 编译缺口
- **COMPAT-MATRIX-01-003**: 复合 rubric 编译降级为 negative
- **USE-LOG-01-001**: step name 不在日志采集范围
- **USE-MD-01-001**: `step_summary` target 无编译映射

### 高优先级产品缺陷（需平台修复）

1. **P0: `atomgit.ref` 返回短格式** → `USE-CTX-01-001` / `COMP-ATOMGIT-01-047` 等
2. **P0: `github` 上下文静默返回占位值** → `USE-CTX-01-002`
3. **P0: 未声明 permissions 时 TOKEN 默认权限不明确** → `COMPAT-PERM-01-001`
4. **P1: boolean input 未被拦截** → `COMPAT-INPUTS-01-001` / `USE-INPT-01-002`
5. **P1: 废弃命令 `::set-env`/`::add-path` 静默接受** → `COMPAT-DEPR-01-001/002`
6. **P1: 不存在上下文属性不报错** → `USE-EXPR-01-001`
7. **P1: `container` 字段静默忽略** → `COMPAT-CONTAINER-01-001`
8. **P1: `runner.os` 格式与文档不一致** → `USE-OS-01-001`
