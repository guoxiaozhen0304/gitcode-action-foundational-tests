# GitCode Actions 产品缺陷清单（19 条）· run 2026-07-25-01

> 本文档只收录经 failure-analyst 归因 + 日志/规格交叉验证判定为**平台侧产品缺陷**的 19 条用例。
> 每条含完整失败分诊 + 复现 URL（GitCode Actions run 页面）。
> 门禁：5 条 P0 缺陷 → 整体 BLOCKED。
> ★ 保留项：SEC-INJ-01-005 置信度低（疑假阳性），进对外报告前须人工复核；全部 P0 安全缺陷建议二次拉 log 坐实。

---

# 一、security（5 条，全 P0）

---

## 失败分诊 · SEC-FORK-01-001 · fork PR 触发 pull_request 时不可读取项目 secrets

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-3/actions/runs/591484fed6364d0787f55a86a569923f

**判定结果**: FAIL（P0, security）
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (run_status, positive) — 预期 COMPLETED_OR_BLOCKED，实际 COMPLETED

**根因初判**: 产品缺陷 — fork PR secret 隔离缺口

**责任人**: 平台方 — fork PR 下 pull_request 事件中 secret 被注入（脱敏显示 `***` 而非空值），未按规格"不可访问"隔离

**证据**:
- Job 日志（11 行，关键部分）:
  ```
  ::debug::Executing: bash -e .../5a3e35b7-46cc-40ed-8932-430e93a9d9b2.sh
  secret value is ***
  ```
- `***` 意味着 secret **有值且被展开**（脱敏掩盖），而非空。若隔离生效，应如 COMP-SECRET-01-001 显示 `secret value is `（空）。
- 对照 GitCode 规格 `using-secrets.md` 第 68 行："Fork 隔离 | pull_request 来自 fork 的 workflow 不可访问项目级 Secret"。

**置信度**: 高（跨 COMP-PR-01-001 / SEC-FORK-01-002 三条交叉验证）

**影响**:
- 阻塞性: 🟡非阻塞 — workflow 仍 COMPLETED
- 静默性: 🔴静默错误 — 用户看到 `***` 会误以为 secret 被保护，实际值已注入
- 影响面: 🔴跨维度 — 所有 fork PR + pull_request + secret 场景
- 综合: 非阻塞但静默+跨维度，fork PR 安全隔离失效，存在信息泄露风险
- 是否有规避手段: 是，改用 pull_request_target 并避免 checkout 执行不可信代码

**建议**: 平台需确认 fork PR 下 pull_request 的 secret 注入行为——规格承诺"不可访问"意味着 secret 不应注入（应为空/undefined），而非注入后靠脱敏掩盖。
**相关用例**: COMP-PR-01-001, SEC-FORK-01-002

---

## 失败分诊 · SEC-FORK-01-002 · fork PR 中 secrets 引用返回空值且 job 不崩溃

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-4/actions/runs/ef61fd1b97f24f7aab0a94ec9d04256a

**判定结果**: FAIL（P0, security）
**失败断言**: assertions[0] (config_probe) — PASS; assertions[1] (run_status, positive) — 预期 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷 — secret 隔离不完整（secret 非空导致 job 崩溃）

**责任人**: 平台方 — fork PR 下 secret 被注入实际值，脚本检测到非空以 exit 1 主动失败

**证据**:
- Job 日志（6 行）:
  ```
  ::debug::Executing: bash -e .../6360f67c-75a5-455a-962f-38537f99c588.sh
  *** is not empty
  ::error::Process exited with code 1
  ```
- 脚本 `[ -z "$SECRET" ]` 预期 secret 为空（正常通过），实际 `*** is not empty` → secret 确被注入值。**这是 fork secret 隔离失效的直接证据。**
- 对照 GitCode 规格 `using-secrets.md` 第 68 行：fork 隔离。

**置信度**: 高（`*** is not empty` + exit 1 直接证明 secret 非空）

**影响**:
- 阻塞性: 🟡非阻塞
- 静默性: 🔴静默错误 — 若脚本不主动检查，用户不会发现 secret 可访问
- 影响面: 🔴跨维度 — 所有 fork PR + secret 场景
- 综合: 非阻塞但静默+跨维度，fork PR 安全隔离不完整
- 是否有规避手段: 是，使用 pull_request_target

**建议**: 同 SEC-FORK-01-001，平台需真正隔离 fork PR 的 secret 访问（不注入而非脱敏）。
**相关用例**: COMP-PR-01-001, SEC-FORK-01-001

---

## 失败分诊 · SEC-DEFPERM-01-001 · ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-2/actions/runs/701e3b05adb04ec393fa7c96e7313f4a

**判定结果**: FAIL（P0, security）
**失败断言**: assertions[0] (leak, negative) — PASS; assertions[1] (value, positive, run_logs) — 预期 log 含 '403_or_permission_denied'，实际缺

**根因初判**: 产品缺陷 — ATOMGIT_TOKEN 未注入

**责任人**: 平台方 — 未声明 permissions 时 token 未生成，违反"每次运行自动生成"承诺

**证据**:
- Job 日志（5 行）:
  ```
  ::debug::Executing: bash -e .../5533a9cf-a711-4989-a14b-31e97f86a322.sh
  000{"error_code":401,"error_code_name":"UNAUTHORIZED","error_message":"401, token not found","trace_id":"d46c89c1aac7994d7466a20f7c1b8c04"}401000000::error::Process exited with code 6
  ```
- 返回 `401 "token not found"` 而非 `403 permission denied` → token 根本没注入，不是权限不足。
- 对照 GitCode 规格 `token-permissions.md` 第 13 行："每次流水线运行时，AtomGit Action 自动生成 ATOMGIT_TOKEN"；第 101 行："未声明 permissions | 使用仓库设置中定义的权限"。

**置信度**: 高（401 token not found 与 403 权限拒绝本质不同；跨 SEC-PERM-01-003 验证）

**影响**:
- 阻塞性: 🔴阻塞 — token 缺失致所有认证操作失败
- 静默性: 🟡可察觉 — 401 明确报错
- 影响面: 🟡同维度 — 所有未声明 permissions 时依赖 ATOMGIT_TOKEN 的操作
- 综合: 阻塞但可察觉，ATOMGIT_TOKEN 未按承诺自动注入
- 是否有规避手段: 是，显式声明 permissions

**建议**: 平台需确认未声明 permissions 时 ATOMGIT_TOKEN 是否应自动注入；若应注入，此为平台缺陷。
**相关用例**: SEC-PERM-01-003

---

## 失败分诊 · SEC-PERM-01-003 · 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-1/actions/runs/02d4457c497d478990abd55e2d819a29

**判定结果**: FAIL（P0, security）
**失败断言**: assertions[0] (leak, negative) — PASS (无 'write_permission_granted'); assertions[1] (run_status, positive) — 预期 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷 — ATOMGIT_TOKEN 缺失（同 SEC-DEFPERM-01-001）

**责任人**: 平台方 — 同 token 未注入

**证据**:
- Job 日志（5 行）:
  ```
  ::debug::Executing: bash -e .../43cbedf8-cf08-46ef-a138-3dcd13db94fb.sh
  000{"error_code":401,"error_code_name":"UNAUTHORIZED","error_message":"401, token not found","trace_id":"714db08de2b9a8955538d6af92362e14"}401000000::error::Process exited with code 6
  ```
- `401 "token not found"` — 与 SEC-DEFPERM-01-001 相同错误模式，交叉验证 token 未注入。
- 对照 GitCode 规格 `token-permissions.md` 第 101 行。

**置信度**: 高（两例均 401 token not found，交叉验证）

**影响**:
- 阻塞性: 🔴阻塞
- 静默性: 🟡可察觉
- 影响面: 🟡同维度 — 同 SEC-DEFPERM-01-001
- 综合: 阻塞可察觉，ATOMGIT_TOKEN 未注入
- 是否有规避手段: 是，显式声明 permissions

**建议**: 同 SEC-DEFPERM-01-001。
**相关用例**: SEC-DEFPERM-01-001

---

## 失败分诊 · SEC-INJ-01-005 · 表达式求值必须防止双重模板渲染（二次求值）

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-2/actions/runs/fda129b9ae7247c68bad2321ecad11c5

**判定结果**: FAIL（P0, security, **SECURITY_CRITICAL flag**）
**失败断言**: assertions[0] (leak, negative, run_logs) — FAIL, 预期明文 '2' 0 命中，实际 FOUND

**根因初判**: 产品缺陷（表达式注入）— ★但置信度低，疑假阳性，进对外报告前**必须人工复核**

**责任人**: 待定（平台方 or 断言引擎误报）

**证据**:
- Job 日志（6 行）:
  ```
  ::debug::Executing: bash -e .../7aff7eef-a088-4a5b-bffa-97a81036668f.sh
  .../7aff7eef-a088-4a5b-bffa-97a81036668f.sh: line 1: Input: ${{ '{{ 1 + 1 }}' }}: bad substitution
  ::error::Process exited with code 1
  ```
- ⚠️ **关键存疑**：日志实际是 bash `bad substitution` 错误（shell 解析 `${{ }}` 失败），**不是平台成功求值出 `2`**。leak 断言报"明文 '2' FOUND"，但 '2' 极可能来自日志时间戳（`12:49`）或版本号，而非表达式求值结果——**单字符 leak 检测高假阳性**。

**置信度**: 低/中（leak 匹配上下文未确认，bash 报错 ≠ 二次求值成功）

**影响**:
- 阻塞性: 🟡非阻塞 — bash 错误终止 job
- 静默性: 🟡可察觉
- 影响面: 🟡同维度（若真存在二次求值）
- 综合: 需人工复核——当前无明确证据支持"二次求值成功"，只有 bad substitution
- 是否有规避手段: 需确认

**建议**: ★首要确认 '2' 的匹配上下文——来自时间戳/版本号还是表达式输出。坐实前**不应对外称"表达式注入漏洞"**。此条列入 19 条是**按初判**，但为最弱一环。
**相关用例**: —

---

# 二、completeness（1 条，P0）

---

## 失败分诊 · COMP-PR-01-001 · fork PR 触发 pull_request 时不可读取项目 secrets

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-4/actions/runs/cd348d6bf11c455bb2eb731cc2d74660

**判定结果**: FAIL（P0, completeness）
**失败断言**: assertions[0] (config_probe) — PASS; assertions[1] (run_status, positive) — 预期 SUCCESS_OR_BLOCKED，实际 COMPLETED

**根因初判**: 产品缺陷 — fork PR secret 隔离缺口（与 SEC-FORK 同源）

**责任人**: 平台方 — fork PR 下 pull_request 中 secret 被注入（脱敏 `***` 非空值）

**证据**:
- Job 日志（5 行）:
  ```
  ::debug::Executing: bash -e .../715ee403-7183-43aa-b5cd-a6cbf95d6fea.sh
  secret value is ***
  ```
- `***` 表示 secret 有值且被展开脱敏；若隔离生效应为空值。
- 对照 GitCode 规格 `using-secrets.md` 第 68 行；`token-permissions.md` 第 105 行（fork pull_request 仅 read）。

**置信度**: 高（与 SEC-FORK-01-001/002 三条交叉验证）

**影响**:
- 阻塞性: 🟡非阻塞
- 静默性: 🔴静默错误 — 用户看到 `***` 误以为被保护
- 影响面: 🔴跨维度 — 所有 fork PR + pull_request + secret 场景
- 综合: 非阻塞但静默+跨维度，fork PR 安全隔离失效
- 是否有规避手段: 是，pull_request_target

**建议**: 平台需真正隔离 fork PR secret（不注入而非脱敏）。
**相关用例**: SEC-FORK-01-001, SEC-FORK-01-002

---

# 三、compatibility（1 条 P0 + 4 条 P1）

---

## 失败分诊 · COMPAT-PERM-01-001 · 未声明 permissions 时默认 TOKEN 读操作权限范围

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-4/actions/runs/6dcbfd9a8ffc44a999f777a4d8d0c6e0

**判定结果**: FAIL（P0, compatibility）
**失败断言**: assertions[0] (value, positive, run_logs) — 预期 log 含 README 内容，实际缺失

**根因初判**: 产品缺陷 — 未声明 permissions 时 repository:read 未默认授予

**责任人**: 平台方

**证据**:
- cat README.md 的输出在日志中缺失，README 未出现。
- 对照 GitCode 规格 `token-permissions.md` 第 101 行："未声明 permissions | 使用仓库设置中定义的权限"。

**置信度**: 中（job 未执行到位、缺 403 明证；此条较弱，建议二次拉 log）

**影响**:
- 阻塞性: 🔴阻塞 — 默认读权限缺失可致基础 CI 中断
- 静默性: 🟡可察觉
- 影响面: 🟡同维度
- 综合: 阻塞且默认权限不明
- 是否有规避手段: 是，显式声明 permissions

**建议**: 平台需明确未声明 permissions 时的默认权限集。
**相关用例**: SEC-DEFPERM-01-001

---

## 失败分诊 · COMPAT-CONTAINER-01-001 · container 字段不被支持时应明确报错而非静默忽略

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-1/actions/runs/f1bdbb5f59134248b3b68a0def2438b3

**判定结果**: FAIL（P1, compatibility）
**失败断言**: assertions[0] (negative, run_status_not) — 预期 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 产品缺陷（静默忽略）

**责任人**: 平台方 — GitCode 对不支持的 container 字段未做校验拦截，静默忽略并正常执行 workflow

**证据**:
- Job 日志（5 行，成功执行）:
  ```
  [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e ...
  hello
  ```
- container 字段被静默忽略，Runner 未使用容器，仍以默认环境执行，workflow COMPLETED。
- 对照 GitCode 规格 `configure-jobs.md` 第 33-47 行：runs-on 为三段式标签格式，未提及 container 支持；`configure-steps.md` 亦未提及 container。文档未承诺支持，但静默忽略不符合输入校验最佳实践。

**置信度**: 高（日志显示 hello 输出成功，YAML 有 container 字段但未被使用）

**影响**:
- 阻塞性: 🔴阻塞 — 用户依赖容器内工具/版本，job 实际裸机运行，引发静默环境差异
- 静默性: 🔴静默错误 — workflow 成功，用户无法察觉未在容器内运行
- 影响面: 🟡同维度 — 所有使用 container 的 workflow
- 综合: 阻塞且静默，依赖容器环境的脚本可能在错误环境下运行而不自知
- 是否有规避手段: 是，用 runs-on 选含所需工具的 runner 或步骤内自装；但平台应报错

**建议**: 平台应在 YAML schema 校验阶段拦截不支持的 container 字段，明确报错「container 字段暂不支持，请使用 runs-on 选择 Runner 环境」。
**相关用例**: COMPAT-CONTAINER-01-002

---

## 失败分诊 · COMPAT-DEPR-01-001 · ::set-env:: 废弃命令应被拒绝或给出迁移指引

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-2/actions/runs/858c995ff79b4deebf128508d699ab00

**判定结果**: FAIL（P1, compatibility）

**根因初判**: 产品缺陷（静默接受废弃命令）

**责任人**: 平台方 — `::set-env::` 被执行但未生效也未拦截

**证据**:
- Job 日志：`::set-env::` 被执行，但 MY_VAR 输出为空，workflow COMPLETED。命令未生效、无报错、无迁移提示。
- 对照 GitHub 行为：`::set-env::` 已废弃，应改用 `$ATOMGIT_ENV` 文件写法，且平台应明确拒绝或提示。

**置信度**: 高

**影响**:
- 阻塞性: 🔴阻塞 — 废弃命令无声失效，依赖它的后续步骤取到空值
- 静默性: 🔴静默错误 — 无生效无提示
- 影响面: 🟡同维度 — GitHub 迁移用户高频踩坑
- 综合: 阻塞且静默，迁移摩擦点
- 是否有规避手段: 是，改用 `echo "K=V" >> $ATOMGIT_ENV`

**建议**: 平台应拒绝废弃命令并提示迁移到 `$ATOMGIT_ENV`。
**相关用例**: COMPAT-DEPR-01-002

---

## 失败分诊 · COMPAT-DEPR-01-002 · ::add-path:: 废弃命令应被拒绝或给出迁移指引

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-3/actions/runs/aa0233e8aa984a5ab9d5c5bd87550358

**判定结果**: FAIL（P1, compatibility）

**根因初判**: 产品缺陷（静默接受废弃命令）

**责任人**: 平台方 — `::add-path::/custom/path` 被执行但未生效

**证据**:
- Job 日志：`::add-path::/custom/path` 被执行，但 /custom/path 未被加入 PATH，workflow COMPLETED。
- 对照 GitHub 行为：应改用 `$ATOMGIT_PATH`，平台应拒绝或提示。

**置信度**: 高

**影响**:
- 阻塞性: 🔴阻塞 — 同 DEPR-01-001
- 静默性: 🔴静默错误
- 影响面: 🟡同维度
- 综合: 阻塞且静默，迁移摩擦点
- 是否有规避手段: 是，改用 `echo "/custom/path" >> $ATOMGIT_PATH`

**建议**: 平台应拒绝废弃命令并提示迁移到 `$ATOMGIT_PATH`。
**相关用例**: COMPAT-DEPR-01-001

---

## 失败分诊 · COMPAT-INPUTS-01-001 · workflow_dispatch inputs 类型限制 — boolean 应报错

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-4/actions/runs/0e732c6244bf4086a6399c73561a4ca7

**判定结果**: FAIL（P1, compatibility）

**根因初判**: 产品缺陷（boolean 类型未被拦截）

**责任人**: 平台方 — type: boolean 的 input 被接受，无校验错误

**证据**:
- Job 日志：`type: boolean` 的 input 被接受，workflow COMPLETED，无任何校验错误。
- 对照 GitCode 规格：workflow_dispatch inputs 类型支持范围未明确承诺 boolean，boolean→string 隐性转换会致条件判断错误。

**置信度**: 高

**影响**:
- 阻塞性: 🟡非阻塞
- 静默性: 🔴静默错误 — boolean 被隐性当 string，条件逻辑静默出错
- 影响面: 🟡同维度 — 所有用 boolean input 的 dispatch
- 综合: 非阻塞但静默，类型混淆
- 是否有规避手段: 是，input 用 string 并在脚本内比较字符串

**建议**: 平台应在 input 类型校验阶段拦截不支持的类型并报错。
**相关用例**: USE-INPT-01-002

---

# 四、usability（8 条，全 P1）

---

## 失败分诊 · USE-CTX-01-001 · 使用 atomgit 上下文时表达式正常求值

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-3/actions/runs/296c72cb31f14133ad1807a5d3c0da94

**判定结果**: FAIL（P1, usability）

**根因初判**: 产品缺陷（atomgit.ref 返回短格式而非文档承诺全格式）

**责任人**: 平台方

**证据**:
- Job 日志：`ref=main`。
- 对照 GitCode 规格 context.md 第 31 行："atomgit.ref | 触发引用（分支或标签全名，如 refs/heads/main）"。实际返回短格式 `main`。

**置信度**: 高

**影响**:
- 阻塞性: 🟡非阻塞
- 静默性: 🔴静默错误
- 影响面: 🟡同维度 — 所有引用 atomgit.ref 的 workflow
- 综合: 非阻塞但静默，返回值与文档不符
- 是否有规避手段: 是，脚本内自行补 refs/heads/ 前缀

**建议**: 平台修正 atomgit.ref 返回全格式，或更新文档说明实际为短格式。
**相关用例**: USE-CTX-01-002

---

## 失败分诊 · USE-CTX-01-002 · 使用 github 上下文时报错应提示 atomgit 替代

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-4/actions/runs/07faabc52d364cd5889414aa63c128da

**判定结果**: FAIL（P1, usability）

**根因初判**: 产品缺陷（github 上下文静默替换为占位值而非报错/警告）

**责任人**: 平台方

**证据**:
- Job 日志：`ref=placeholder_ref` — github.ref 被解析为 placeholder_ref，无任何警告或迁移提示。

**置信度**: 高

**影响**:
- 阻塞性: 🔴阻塞 — github 上下文返回垃圾值
- 静默性: 🔴静默错误 — 无警告
- 影响面: 🟡同维度 — 所有含 github.* 上下文的迁移 workflow
- 综合: 严重迁移阻塞+静默错误
- 是否有规避手段: 是，全量替换 github.* → atomgit.*

**建议**: 平台应对 github.* 上下文报错并提示迁移到 atomgit.*，而非返回占位值。
**相关用例**: USE-CTX-01-001

---

## 失败分诊 · USE-ENV-01-002 · 引用 GITHUB_SHA 时日志应给出环境变量映射提示

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-3/actions/runs/ee53fda663814e08907afddb2e2e7807

**判定结果**: FAIL（P1, usability）

**根因初判**: 产品缺陷（bash set -u 下 GITHUB_SHA 未定义，无迁移提示）

**责任人**: 平台方 — Runner 不识别 GITHUB_*，也不给迁移提示

**证据**:
- Job 日志：`/home/slave1/runner/...sh: line 2: GITHUB_SHA: unbound variable`

**置信度**: 高

**影响**:
- 阻塞性: 🔴阻塞 — 迁移场景直接崩溃
- 静默性: 🟡可察觉 — unbound variable 明确
- 影响面: 🟡同维度 — 所有引用 GITHUB_* 的迁移 workflow
- 综合: 高摩擦迁移阻塞，Runner 层不识别 GITHUB_* 也不提示
- 是否有规避手段: 是，改用 ATOMGIT_* 对应变量

**建议**: Runner 层对 GITHUB_* 变量给出迁移提示或映射到 ATOMGIT_*。
**相关用例**: USE-CTX-01-002

---

## 失败分诊 · USE-EXPR-01-001 · 引用不存在的上下文属性时报错应包含原始表达式与错误类型

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-3/actions/runs/70811c7c35554d3a990a9e0ed2aff57c

**判定结果**: FAIL（P1, usability）

**根因初判**: 产品缺陷（不存在的上下文属性 atomgit.nonexistent_property 被静默解析为空字符串）

**责任人**: 平台方

**证据**:
- Job 日志：`val=`，无任何错误提示。

**置信度**: 高

**影响**:
- 阻塞性: 🟡非阻塞
- 静默性: 🔴静默错误 — 无报错致调试困难
- 影响面: 🟡同维度
- 综合: 非阻塞但静默，不存在属性静默返空
- 是否有规避手段: 无直接规避，依赖用户自查

**建议**: 平台对不存在的上下文属性应报错并包含原始表达式与错误类型。
**相关用例**: —

---

## 失败分诊 · USE-OS-01-001 · runner.os 返回值与文档声明的平台支持一致

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-2/actions/runs/ef8a65b9e5fa4048a4283ec54588d3b4

**判定结果**: FAIL（P1, usability）

**根因初判**: 产品缺陷（runner.os 返回小写 linux 而非大写 Linux）

**责任人**: 平台方

**证据**:
- Job 日志：`os=linux`。GitHub 约定为 `Linux`（首字母大写）。

**置信度**: 高

**影响**:
- 阻塞性: 🟡非阻塞
- 静默性: 🔴静默错误 — `runner.os == 'Linux'` 条件静默失败
- 影响面: 🟡同维度 — 所有含 runner.os 判断的迁移 workflow
- 综合: 非阻塞但静默，格式与 GitHub 约定不一致
- 是否有规避手段: 是，改用小写比较或 lower()

**建议**: 平台让 runner.os 与 GitHub 约定一致（Linux），或文档明确格式。
**相关用例**: —

---

## 失败分诊 · USE-CONC-01-001 · concurrency.max 配置 0 或 10 时报错应提示有效范围

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-2/actions/runs/15552376b5f24894814689e0ade2dbe7

**判定结果**: FAIL（P1, usability）

**根因初判**: 产品缺陷（超范围 concurrency.max 值被静默接受）

**责任人**: 平台方

**证据**:
- Job 日志：`concurrency.max: 10` 被静默接受，workflow COMPLETED，无范围校验错误。

**置信度**: 中（文档未定义 max 范围，断言基于 GitHub 假设——★此条较弱，若平台文档确未限制范围则属用例问题）

**影响**:
- 阻塞性: 🟡非阻塞
- 静默性: 🔴静默错误 — 超范围值无提示
- 影响面: 🟢单用例
- 综合: 非阻塞但静默，无范围校验
- 是否有规避手段: 是，用文档允许范围内的值

**建议**: 平台应定义 concurrency.max 有效范围并对超范围报错；或文档明确无范围限制（则此条转用例问题）。
**相关用例**: —

---

## 失败分诊 · USE-DISP-01-002 · workflow_dispatch 未提供参数但存在 default 时应使用默认值运行

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-2/actions/runs/c4104a7164e14c8abbd643dbe35d8ba1

**判定结果**: FAIL（P1, usability）

**根因初判**: 产品缺陷（dispatch 未传参时 default 值未被使用）

**责任人**: 平台方

**证据**:
- Job 日志：job 运行但无任何 shell 脚本输出，run_status=FAILED。

**置信度**: 中（零输出，也可能是 harness dispatch 传参或 runner 调度问题）

**影响**:
- 阻塞性: 🟡非阻塞
- 静默性: 🟡可察觉
- 影响面: 🟡同维度 — 所有依赖 input default 的 dispatch
- 综合: 非阻塞，default 值疑未生效
- 是否有规避手段: 是，dispatch 时显式传参

**建议**: 平台确认 dispatch 未传参时是否应用 input default；harness 侧同步排查零输出根因。
**相关用例**: USE-INPT-01-002

---

## 失败分诊 · USE-INPT-01-002 · 使用 boolean 类型 input 时报错应提示仅支持 string

**复现 URL**: https://gitcode.com/ComputingActionTest/gitcode-test-4/actions/runs/9c1bd8bc0411437eae3932ab9ce0ba17

**判定结果**: FAIL（P1, usability）

**根因初判**: 产品缺陷（同 COMPAT-INPUTS-01-001，boolean 未拦截）

**责任人**: 平台方

**证据**:
- Job 日志：`type: boolean` 的 input dry_run 被接受并输出 false（字符串）。

**置信度**: 高

**影响**:
- 阻塞性: 🟡非阻塞
- 静默性: 🔴静默错误 — boolean 被隐性当 string
- 影响面: 🟡同维度
- 综合: 非阻塞但静默，类型混淆
- 是否有规避手段: 是，input 用 string

**建议**: 平台应统一对不支持的 input 类型校验并报错。
**相关用例**: COMPAT-INPUTS-01-001

---

# 附：19 条速查表

| # | 用例 | 维度 | 优先级 | 复现 URL |
|---|---|---|---|---|
| 1 | SEC-FORK-01-001 | security | P0 | .../gitcode-test-3/actions/runs/591484fed6364d0787f55a86a569923f |
| 2 | SEC-FORK-01-002 | security | P0 | .../gitcode-test-4/actions/runs/ef61fd1b97f24f7aab0a94ec9d04256a |
| 3 | SEC-DEFPERM-01-001 | security | P0 | .../gitcode-test-2/actions/runs/701e3b05adb04ec393fa7c96e7313f4a |
| 4 | SEC-PERM-01-003 | security | P0 | .../gitcode-test-1/actions/runs/02d4457c497d478990abd55e2d819a29 |
| 5 | SEC-INJ-01-005 ⚠️ | security | P0 | .../gitcode-test-2/actions/runs/fda129b9ae7247c68bad2321ecad11c5 |
| 6 | COMP-PR-01-001 | completeness | P0 | .../gitcode-test-4/actions/runs/cd348d6bf11c455bb2eb731cc2d74660 |
| 7 | COMPAT-PERM-01-001 | compatibility | P0 | .../gitcode-test-4/actions/runs/6dcbfd9a8ffc44a999f777a4d8d0c6e0 |
| 8 | COMPAT-CONTAINER-01-001 | compatibility | P1 | .../gitcode-test-1/actions/runs/f1bdbb5f59134248b3b68a0def2438b3 |
| 9 | COMPAT-DEPR-01-001 | compatibility | P1 | .../gitcode-test-2/actions/runs/858c995ff79b4deebf128508d699ab00 |
| 10 | COMPAT-DEPR-01-002 | compatibility | P1 | .../gitcode-test-3/actions/runs/aa0233e8aa984a5ab9d5c5bd87550358 |
| 11 | COMPAT-INPUTS-01-001 | compatibility | P1 | .../gitcode-test-4/actions/runs/0e732c6244bf4086a6399c73561a4ca7 |
| 12 | USE-CTX-01-001 | usability | P1 | .../gitcode-test-3/actions/runs/296c72cb31f14133ad1807a5d3c0da94 |
| 13 | USE-CTX-01-002 | usability | P1 | .../gitcode-test-4/actions/runs/07faabc52d364cd5889414aa63c128da |
| 14 | USE-ENV-01-002 | usability | P1 | .../gitcode-test-3/actions/runs/ee53fda663814e08907afddb2e2e7807 |
| 15 | USE-EXPR-01-001 | usability | P1 | .../gitcode-test-3/actions/runs/70811c7c35554d3a990a9e0ed2aff57c |
| 16 | USE-OS-01-001 | usability | P1 | .../gitcode-test-2/actions/runs/ef8a65b9e5fa4048a4283ec54588d3b4 |
| 17 | USE-CONC-01-001 | usability | P1 | .../gitcode-test-2/actions/runs/15552376b5f24894814689e0ade2dbe7 |
| 18 | USE-DISP-01-002 | usability | P1 | .../gitcode-test-2/actions/runs/c4104a7164e14c8abbd643dbe35d8ba1 |
| 19 | USE-INPT-01-002 | usability | P1 | .../gitcode-test-4/actions/runs/9c1bd8bc0411437eae3932ab9ce0ba17 |

> ⚠️ SEC-INJ-01-005 置信度低（疑假阳性，明文 '2' 或来自时间戳）——进对外报告前须人工复核。
> ★ 全部 P0 安全缺陷（尤其 fork secret 三条）对外前建议二次拉 log 坐实。

---

*数据源：failure/2026-07-25-01/{report,result} · 生成 2026-07-25*
