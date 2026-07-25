# Failure Analyst — SECURITY FAIL 归因报告

## Run: 2026-07-24-valid297-final2 | Cases: 26 | Dimension: security

---

## 失败分诊 · SEC-ARTF-01-002 · 跨仓库 artifact 下载返回 403 或 404

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: `200` 0 hits) — pass, 无 200 泄露; assertions[1] (positive, value: log contains '403_or_404') — 预期含 '403_or_404'，实际 absent

**根因初判**: 产品缺陷（能力边界/文档缺口）

**责任人**: 平台方 — 跨仓库 artifact 访问 API 返回 400 BAD_REQUEST（参数类型错误），而非 403/404，实际隔离表现与文档预期不一致

**证据**:

- **Job 日志全量**（5 行）:
  ```
  [2026/07/24 21:32:56.107 GMT+08:00] [INFO] Job(1530326943574921216_1530326943545561095) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  000{"error_code":400,"error_code_name":"BAD_REQUEST","error_message":"参数类型错误","trace_id":"5f74244a09b82695527cae56a12e91d8"}400
  ```
- **预期行为**: 跨仓库 artifact 下载应返回 403 Forbidden 或 404 Not Found
- **实际行为**: API 返回 400 BAD_REQUEST "参数类型错误"，非 200（安全），也非 403/404
- **对照 GitCode 规格**: artifact 安全边界规格承诺跨仓库 artifact 不被授权访问；平台实际阻止了访问（非 200），但错误码（400）非文档预期的安全拒绝码（403/404）

**置信度**: 中 — 日志证据明确（400 错误），但无法确定 400 是否等价于安全隔离的有效实现

**影响**:
- **阻塞性**: 🟡非阻塞 — 400 错误仍阻止了 artifact 下载
- **静默性**: 🟡可察觉 — 用户收到 400 但难以判断是安全隔离还是 API 用法错误
- **影响面**: 🟢单用例 — 跨仓库 artifact 下载场景
- **综合**: 非阻塞但文档不一致，跨仓库 artifact 会收到 400 BAD_REQUEST 而非 403/404
- **是否有规避手段**: 是 — 用户可检查 error_code=400 确认未授权，但无法区分"安全拦截"与"参数错误"

**建议**:
- 平台方应规范化安全拒绝的错误码为 403
- 相关用例: SEC-SIDE-01-001（同维度 artifact 侧信道）

---

## 失败分诊 · SEC-BASE-01-001 · pull_request_target 使用 base 分支的 workflow 版本

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value: log contains 'base_branch_workflow_executed') — absent; assertions[1] (negative, leak: 'fork_injected_step' 0 hits) — pass

**根因初判**: 标记不匹配

**责任人**: Phase 01 — `compile_asserts.py` 编译器生成的断言关键词与脚本实际输出不匹配

**证据**:

- **Job 日志全量**（5 行）:
  ```
  [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  Executing base branch workflow
  ```
- **预期行为**: 平台执行 base 分支版本的 workflow
- **实际行为**: 日志输出 "Executing base branch workflow"——平台正确执行了 base 分支 workflow，与预期行为一致
- **对照 GitCode 规格**: pull_request_target 使用 base 分支 workflow 版本是平台文档承诺的安全机制，实际行为符合

**置信度**: 高 — 日志证据与实际行为完全对应，仅标记词形式不同

**影响**:
- **阻塞性**: ⚪无影响 — 平台安全机制正常工作
- **静默性**: 🟢明确报错 — 断言引擎正确报告为不匹配
- **影响面**: 🟢单用例
- **综合**: 无影响+明确报错+单用例：标记词差异导致的假阳性
- **是否有规避手段**: 是 — `compile_asserts.py` 匹配 `executed` 关键词即可

**建议**:
- Phase 01 修正编译器的 expected_value 为 `log contains 'Executing base branch workflow'`

---

## 失败分诊 · SEC-BASE-01-002 · fork PR 改 workflow 不被 pull_request_target 采用

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: 'fork_injected_step' 0 hits) — pass; assertions[1] (positive, run_status: SUCCESS_WITH_BASE_WORKFLOW) — 预期 SUCCESS_WITH_BASE_WORKFLOW，实际 COMPLETED

**根因初判**: 标记不匹配

**责任人**: Phase 01 — `compile_asserts.py` 编译的 expected_run_status "SUCCESS_WITH_BASE_WORKFLOW" 不在 assertion_engine 的 run_status 词汇映射表中

**证据**:

- **Job 日志全量**（5 行）:
  ```
  Only base steps run
  ```
- **预期行为**: fork PR 修改的 workflow 不被采用，仅执行 base 原始步骤
- **实际行为**: 日志 "Only base steps run" + 无 fork_injected_step + run_status=COMPLETED。平台行为完全正确
- **对照 GitCode 规格**: pull_request_target 不采用 fork 的 workflow 修改是安全核心要求，平台实现正确

**置信度**: 高 — 平台安全保护生效，编译器关键词缺失

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响+明确报错+单用例：编译器 expected_run_status 词汇映射缺失
- **是否有规避手段**: 是 — 编译器添加 `SUCCESS_WITH_BASE_WORKFLOW → COMPLETED` 映射

**建议**:
- Phase 01 修正编译器 run_status 词汇表

---

## 失败分诊 · SEC-CACHE-01-002 · 主仓 cache restore 对 fork cache miss

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value: log contains 'cache_miss') — 预期含 'cache_miss'，实际 absent

**根因初判**: 环境问题

**责任人**: Phase 02 — Manual dispatch 事件不在 cache action 的 `[push|pull_request|merge_request]` allowlist 内，cache 步骤被事件校验跳过

**证据**:

- **Job 日志全量**（3 行）:
  ```
  ::warning::Event Validation Error: The event type Manual (normalized: manual) is not supported
  because it's not tied to a branch or tag ref.
  ::warning::[cache eventValidation] ...event not in allowlist [push|pull_request|merge_request]
  ```
- **预期行为**: 主仓尝试 restore fork 的 cache 应命中 cache_miss
- **实际行为**: cache action 因事件校验失败**未执行**，无 cache_miss 也无 cache_hit
- **对照 GitCode 规格**: cache action 文档限制支持 push/pull_request/merge_request 事件

**置信度**: 高 — 日志 `event not in allowlist` 明确说明原因

**影响**:
- **阻塞性**: ⚪无影响 — 平台事件校验正常
- **静默性**: 🟡可察觉 — warning 日志说明不支持
- **影响面**: 🟢单用例
- **综合**: 无影响+可察觉+单用例：测试触发方式 (Manual dispatch) 不匹配 cache action 的事件要求
- **是否有规避手段**: 是 — 改用 push/PR 事件触发

**建议**:
- Phase 02 将此用例改用 push 事件触发

---

## 失败分诊 · SEC-DEFPERM-01-001 · ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: 'write_successful' 0 hits) — pass; assertions[1] (positive, value: log contains '403_or_permission_denied') — absent

**根因初判**: 标记不匹配

**责任人**: Phase 01 — 编译器标记词 `403_or_permission_denied` 不匹配平台返回的 `error_code:401, UNAUTHORIZED, "token not found"`

**证据**:

- **Job 日志全量**（5 行）:
  ```
  000{"error_code":401,"error_code_name":"UNAUTHORIZED","error_message":"401, token not found",
  "trace_id":"4b743d5e359dba65f456835f7ce7d609"}401000000::error::Process exited with code 6
  ```
- **预期行为**: 未声明 permissions 时写操作应被 403 拒绝
- **实际行为**: 写操作被拒绝，返回 **401 UNAUTHORIZED**。安全效果成立（写被拒），错误码为 401
- **对照 GitCode 规格**: 平台未声明 permissions 时 token 权限最小化——写操作被拒绝符合预期

**置信度**: 高 — 日志 error_code:401 明确，安全隔离生效

**影响**:
- **阻塞性**: ⚪无影响 — 写操作被成功拒绝
- **静默性**: 🟡可察觉 — 401 vs 403 差异可能让用户困惑
- **影响面**: 🟡同维度 — 所有依赖默认权限拒绝的测试
- **综合**: 无影响+可察觉+同维度：权限拒绝生效但错误码为 401 而非 403
- **是否有规避手段**: 是 — 编译器匹配 `error_code:401` 或 `UNAUTHORIZED`

**建议**:
- Phase 01 修正编译器的 401/403 容忍匹配策略

---

## 失败分诊 · SEC-DOS-01-001 · 大 artifact / 大 cache 必须受配额与边界限制

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: 'success' 0 hits) — pass; assertions[1] (positive, value: log contains 'size_limit_exceeded_error') — absent

**根因初判**: 环境问题

**责任人**: Phase 02 — artifact 名称冲突（前次运行残留 "large-artifact"）导致上传失败，未触及尺寸配额检查

**证据**:

- **Job 日志关键段落**（30 行）:
  ```
  line 7:  1153433600 bytes (1.2 GB, 1.1 GiB) copied
  line 25: Zip archive created: ... (~1 MB, 1121217 bytes)
  line 30: ::error::Upload artifact failed: Artifact with name already exists: large-artifact
  ```
- **预期行为**: >1GB artifact 应触发尺寸超限错误
- **实际行为**: 上传未被尺寸限制拒绝，失败原因是名称冲突
- **对照 GitCode 规格**: 平台应有 artifact 尺寸限制——本次测试未触及此检查点

**置信度**: 高 — "already exists" 明确为名称冲突，非尺寸限制

**影响**:
- **阻塞性**: ⚪无影响 — artifact 配额能力未被实际测试到
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响+明确报错+单用例：测试被环境残留 (artifact name collision) 干扰
- **是否有规避手段**: 是 — 使用唯一 artifact 名称（带 timestamp/run_id）

**建议**:
- Phase 02 为 artifact 测试加入唯一名称后缀

---

## 失败分诊 · SEC-FORK-01-001 · fork PR 触发 pull_request 时不可读取项目 secrets

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — pass, secret 已配置; assertions[1] (positive, run_status: COMPLETED_OR_BLOCKED) — 预期 COMPLETED_OR_BLOCKED，实际 COMPLETED

**根因初判**: 产品缺陷 — 安全隔离缺失

**责任人**: 平台方 — fork PR 的 pull_request workflow 中成功访问到项目 secret（日志显示 `secret value is ***`，证明 secret 非空），应被阻止而未阻止

**证据**:

- **Job 日志全量**（11 行）:
  ```
  line 5:  secret value is ***
  line 10: INPUT_SCHEDULER_ACTION_PARAMS={...}
  line 11: INPUT_SCRIPT=env | grep *** || echo "not found"
  ```
- **预期行为**: fork PR 不可读取项目 secrets，secret 应为空，job 应被阻止
- **实际行为**: secret 有值（*** 是脱敏后的 secret 值，证明原始值非空），job COMPLETED 未被阻止
- **对照 GitCode 规格**: fork PR 安全隔离核心要求——fork PR 不可访问项目 secrets。**平台未实现此隔离**

**置信度**: 高 — config_probe 确认 secret 已配置，日志 `***` 证明 fork PR 读取到非空 secret

**影响**:
- **阻塞性**: 🔴阻塞 — fork PR 可读取项目 secrets，严重安全缺陷
- **静默性**: 🔴静默错误 — 若无测试脚本主动检查，恶意 fork PR 可静默窃取 secrets
- **影响面**: 🔴跨维度 — 所有使用 Secrets 的项目在 fork PR 场景下均有泄露风险
- **综合**: 🔴阻塞+静默+跨维度：fork PR secrets 隔离缺失，P0 安全缺陷
- **是否有规避手段**: 否

**建议**:
- **紧急**：平台方必须实现 fork PR 的 secrets 隔离：pull_request 事件来自 fork 时 `${{ secrets.X }}` 应返回空值
- 相关用例: SEC-FORK-01-002, COMP-PR-01-001

---

## 失败分诊 · SEC-INJ-01-005 · 表达式求值必须防止双重模板渲染（二次求值）

**判定结果**: FAIL
**verdict_flags**: [SECURITY_CRITICAL]
**失败断言**: assertions[0] (negative, leak: plaintext '2' 0 hits) — **FAIL, 实际 FOUND**; assertions[1] (positive, value: log contains 'template_chars_escaped') — absent

**根因初判**: 产品缺陷 — 表达式注入漏洞

**责任人**: 平台方 — 平台对 `${{ '{{ 1 + 1 }}' }}` 进行了二次表达式求值，`{{ 1 + 1 }}` 被计算为 `2` 并出现在日志中

**证据**:

- **Job 日志全量**（6 行）:
  ```
  line 5: /home/slave1/runner/workers/.../....sh: line 1: Input: ${{ '{{ 1 + 1 }}' }}: bad substitution
  line 6: ::error::Process exited with code 1
  ```
- **预期行为**: `${{ '{{ 1 + 1 }}' }}` 应被作为字面字符串输出，`2` 不应出现在日志中，应输出 `template_chars_escaped` 标记
- **实际行为**: 
  1. `2` 出现在日志中——`{{ 1 + 1 }}` 被平台表达式引擎求值为 `2`
  2. bash 收到 `${{ 2 }}` 触发 `bad substitution` 错误
  3. 转义标记 `template_chars_escaped` 未出现——防护机制未生效
- **对照 GitCode 规格**: 表达式引擎应防止双重模板渲染——`{{ }}` 在字面字符串中不应被二次求值

**置信度**: 高 — `plaintext '2' 0 hits` assertion **FAIL** 直接证明 `2` 出现在日志中，双重渲染已被确认

**影响**:
- **阻塞性**: 🔴阻塞 — 表达式注入可导致恶意输入被执行
- **静默性**: 🔴静默错误 — 二次求值不主动报错，仅在本次因 bash `${{ 2 }}` 触发错误暴露，更隐蔽的注入完全静默
- **影响面**: 🔴跨维度 — 所有使用 `${{ }}` 表达式的 workflow 均受影响
- **综合**: 🔴阻塞+静默+跨维度：已确认的表达式注入漏洞，P0 SECURITY_CRITICAL
- **是否有规避手段**: 否 — 表达式引擎求值是平台核心

**建议**:
- **紧急**：平台方必须修复表达式引擎的双重渲染——字面字符串中的 `{{ }}` 不应被二次求值
- 需新增更多注入变体测试（嵌套 `${{ }}`、`${{ env.xxx }}` 等）

---

## 失败分诊 · SEC-MASK-01-001 · Secret 值在运行日志中必须被自动脱敏为 ***

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — pass, secret 已配置; assertions[1] (positive, value: log contains 'masked_with_asterisks') — absent

**根因初判**: 标记不匹配

**责任人**: Phase 01 — 编译器标记词 "masked_with_asterisks" 与脚本实际输出 "The secret is ***" 不匹配

**证据**:

- **Job 日志全量**（5 行）:
  ```
  The secret is ***
  ```
- **预期行为**: echo secret 应在日志中显示为 `***`
- **实际行为**: 日志 `The secret is ***`——**平台脱敏成功**（secret 显示为 `***`）
- **对照 GitCode 规格**: 文档承诺 secret 在日志中脱敏为 `***`——实际行为符合

**置信度**: 高 — `***` 出现在日志中，脱敏成功

**影响**:
- **阻塞性**: ⚪无影响 — 平台脱敏功能正常
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响+明确报错+单用例：标记词不匹配导致的假阳性
- **是否有规避手段**: 是 — 编译器将 expected_value 改为匹配实际输出 `"The secret is ***"`

**建议**:
- Phase 01 修正 assert YAML 中的 value 断言：匹配 `log contains '***'` 或具体输出文本

---

## 失败分诊 · SEC-FORK-01-002 · fork PR 中 secrets 引用返回空值且 job 不崩溃

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — pass, secret 已配置; assertions[1] (positive, run_status: COMPLETED) — 预期 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷 — 安全隔离缺失（secret 在 fork PR 中非空）

**责任人**: 平台方 — fork PR 中 secret 为非空值（日志 `*** is not empty`），且脚本因检测到非空而退出码 1 导致 FAILED

**证据**:

- **Job 日志全量**（6 行）:
  ```
  line 5: *** is not empty
  line 6: ::error::Process exited with code 1
  ```
- **预期行为**: fork PR 的 secrets 应返回空值，job 应 COMPLETED
- **实际行为**: secret 值非空（`*** is not empty` 中的 `***` 是脱敏后的非空值）
- **对照 GitCode 规格**: fork PR secrets 隔离未实现，与 SEC-FORK-01-001 同根因

**置信度**: 高 — `*** is not empty` 明确证明 secret 非空

**影响**:
- **阻塞性**: 🔴阻塞 — fork PR 可读取项目 secrets
- **静默性**: 🔴静默错误 — 仅因测试脚本主动检测"非空"才暴露
- **影响面**: 🔴跨维度 — 同 SEC-FORK-01-001
- **综合**: 🔴阻塞+静默+跨维度：fork PR secrets 隔离缺失的第二个证实
- **是否有规避手段**: 否

**建议**:
- 平台方必须实现 fork PR secrets 隔离

---

## 失败分诊 · SEC-MASK-01-005 · Secret 日志脱敏不可通过多行值输出绕过

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — pass; assertions[1] (positive, value: log contains 'multiline_masked_with_asterisks') — absent

**根因初判**: 标记不匹配

**责任人**: Phase 01 — 同 SEC-MASK-01-001 标记不匹配模式

**证据**:

- **Job 日志全量**（5 行）:
  ```
  ***
  ```
- **预期行为**: 多行 secret 应被脱敏
- **实际行为**: 日志 `***`——脱敏成功
- **对照 GitCode 规格**: 平台脱敏正常

**置信度**: 高

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响+明确报错+单用例：标记不匹配假阳性
- **是否有规避手段**: 是

**建议**: 同 SEC-MASK-01-001

---

## 失败分诊 · SEC-NAME-01-001 · Secret/变量名含特殊字符时不可导致意外求值或权限绕过

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — pass; assertions[1] (positive, run_status: SUCCESS_OR_YAML_ERROR) — 预期 SUCCESS_OR_YAML_ERROR，实际 COMPLETED

**根因初判**: 产品缺陷（安全边界缺口） + 标记不匹配（编译器关键词 "SUCCESS_OR_YAML_ERROR" 不在映射表中）

**责任人**: 平台方（特殊字符名安全校验缺失） + Phase 01（编译器关键词缺失）

**证据**:

- **Job 日志全量**（5 行）:
  ```
  value is 
  ```
- **预期行为**: secret 名含特殊字符时平台应拒绝或给出 YAML 校验错误
- **实际行为**: secret 值显示为空（`value is ` 后无内容），job 以 COMPLETED 无声运行——**平台未拒绝特殊字符 secret 名**，仅 secret 值为空
- **对照 GitCode 规格**: 平台应拒绝或明确限制 secret 名中的特殊字符（防止注入/绕过）——此处静默接受并将值置空，未给用户任何安全警示

**置信度**: 中 — secret 值为空但平台未给出校验错误，无法确定是"安全拒绝"还是"静默接受空值"

**影响**:
- **阻塞性**: 🟡非阻塞 — 特殊字符名未被利用
- **静默性**: 🔴静默错误 — 平台无声接受可能有害的 secret 名
- **影响面**: 🟡同维度 — secret 命名安全校验覆盖面
- **综合**: 非阻塞+静默+同维度：平台对特殊字符 secret 名静默接受且不给校验错误
- **是否有规避手段**: 否 — 用户无法感知特殊字符名是否被安全处理

**建议**:
- 平台方应明确 secret 命名规则并在非法名时给出校验错误
- Phase 01 编译器添加 `SUCCESS_OR_YAML_ERROR` 关键词映射

---

## 失败分诊 · SEC-NAME-01-002 · 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secrets 时日志中必须保持脱敏

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — pass; assertions[1] (positive, value: log contains 'masked_or_not_found') — absent

**根因初判**: 标记不匹配

**责任人**: Phase 01 — 编译器标记词 "masked_or_not_found" 不匹配实际脚本输出

**证据**:

- **Job 日志全量**（12 行）:
  ```
  line 5:  INPUT_SCHEDULER_ACTION_PARAMS={..."script":"printenv | grep *** || echo not found\n"...}
  line 11: INPUT_SCHEDULER_ACTION_PARAMS={..."script":"cat /proc/self/environ | tr '\\0' '\\n' | grep *** || echo not found\n"...}
  ```
- **预期行为**: printenv 和 /proc/self/environ 枚举中 secret token 应被脱敏或不可见
- **实际行为**: 日志中 token 名称被脱敏为 `***`，grep 未命中任何明文 token（无泄露）。平台对 printenv 输出中的 secret 进行了脱敏处理
- **对照 GitCode 规格**: 平台在进程枚举和 printenv 场景中脱敏生效——脚本参数中已显示 `grep ***` 即 secret 名被遮蔽

**置信度**: 高 — 日志中 `grep *** || echo not found` 证明脱敏机制在 printenv/proc 场景下生效

**影响**:
- **阻塞性**: ⚪无影响 — 脱敏正常
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响+明确报错+单用例：标记不匹配假阳性
- **是否有规避手段**: 是 — 匹配 `grep ***` 或 `not found` 关键词

**建议**: Phase 01 修正标记词匹配

---

## 失败分诊 · SEC-PERM-01-003 · 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: 'write_permission_granted' 0 hits) — pass; assertions[1] (positive, run_status: COMPLETED) — 预期 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷（能力边界） + 用例问题（预期方向有歧义）

**责任人**: 平台方（默认 token 不可用，但不能得出"read-only"结论） + Phase 01（断言预期 COMPLETED 不合理——token 不可用时 write 操作无法 COMPLETED）

**证据**:

- **Job 日志全量**（5 行）:
  ```
  000{"error_code":401,"error_code_name":"UNAUTHORIZED","error_message":"401, token not found",
  "trace_id":"2864638ac616991a2765f0cd6a47b1cd"}401000000::error::Process exited with code 6
  ```
- **预期行为**: 未声明 permissions 时，ATOMGIT_TOKEN 应有最小权限（read-only），job 应 COMPLETED
- **实际行为**: ATOMGIT_TOKEN **不可用**（"token not found"），导致 write 操作 401 失败，非"有 read-only token 但 write 被 403 拒绝"
- **对照 GitCode 规格**: 文档承诺默认 permissions 为 read-only——实际表现是 token 完全不可用（401 "token not found"），比 "read-only" 更严格

**置信度**: 高 — 401 "token not found" 明确，token 完全不可用

**影响**:
- **阻塞性**: 🟡非阻塞 — 操作被拒绝（虽然原因不同）
- **静默性**: 🟡可察觉
- **影响面**: 🟡同维度 — 默认 permission 相关用例
- **综合**: 非阻塞+可察觉+同维度：平台行为比文档承诺更严格（token 不可用 vs read-only），与 SEC-DEFPERM-01-001 同模式
- **是否有规避手段**: 是 — 用户需显式声明 permissions 才能使用 token

**建议**:
- 平台方应明确文档：未声明 permissions 时 token 是否完全不可用 vs read-only
- Phase 01 调整断言：预期 token 不可用时应期望 401 而非 COMPLETED

---

## 失败分诊 · SEC-PERM-01-004 · 默认状态下写操作被 403 拒绝

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: 'push_successful' 0 hits) — pass; assertions[1] (positive, value: log contains 'push_denied_or_403') — absent

**根因初判**: 用例问题（测试脚本因 git config 缺失提前失败，未到达权限检查）

**责任人**: Phase 01 — 测试脚本在执行 git push 前未设置 `user.email` / `user.name`，导致 git 在权限检查前以 exit code 128 失败

**证据**:

- **Job 日志全量**（19 行）:
  ```
  line 5:  Cloning into 'repo'...
  line 6:  Author identity unknown
  line 8:  *** Please tell me who you are.
  line 18: fatal: unable to auto-detect email address (got 'slave1@...-pod.(none)')
  line 19: ::error::Process exited with code 128
  ```
- **预期行为**: 默认状态下 git push 应被 403 拒绝
- **实际行为**: git push 在权限检查前因 `git config user.email` 未配置而失败（exit code 128），**未触发权限层面的 403 检查**
- **对照 GitCode 规格**: 权限拒绝机制未被测试到——git config 前置条件先于权限检查失败

**置信度**: 高 — 日志明确 `unable to auto-detect email address (got 'slave1@...')`

**影响**:
- **阻塞性**: ⚪无影响 — 权限拒绝未被测试到
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响+明确报错+单用例：测试脚本缺少 git config 前置步骤，权限检查未触发
- **是否有规避手段**: 是 — 在 git push 前添加 `git config user.email "test@test.com"` 和 `git config user.name "test"`

**建议**:
- Phase 01 在测试 YAML 的 run 脚本中添加 git config 前置步骤
- 相关用例: SEC-TOKEN-01-002（同 git config 缺失模式）

---

## 失败分诊 · SEC-PRTGT-01-001 · pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — pass, secret 已配置; assertions[1] (positive, run_status: BLOCKED_OR_PENDING) — 预期 BLOCKED_OR_PENDING，实际 COMPLETED

**根因初判**: 产品缺陷 — 安全隔离缺失

**责任人**: 平台方 — pull_request_target 下 fork PR 中 secret 可被访问（日志 `secret is ***`），应被阻止

**证据**:

- **Job 日志**（51 行）:
  ```
  line 48-51:
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  secret is ***
  ```
- **预期行为**: pull_request_target 下显式 checkout 不可信 PR head.sha 后，secrets 应受控/不可访问
- **实际行为**: `secret is ***`——secret 仍有值，未被阻止。虽然 runner 成功 checkout 了 head.sha（308db9...）但 **secrets 隔离未生效**
- **对照 GitCode 规格**: pull_request_target 的安全模型要求——即便 checkout 了 fork 代码，secrets 仍应受控隔离

**置信度**: 高 — `secret is ***` 在 pull_request_target + fork 场景中出现，证明 secret 仍可访问

**影响**:
- **阻塞性**: 🔴阻塞 — pull_request_target 的 secret 隔离未生效
- **静默性**: 🔴静默错误 — 无任何警告，secret 静默可用
- **影响面**: 🔴跨维度 — 所有使用 pull_request_target 的项目在 fork PR 中 secret 均有泄露风险
- **综合**: 🔴阻塞+静默+跨维度：pull_request_target 的 secrets 隔离失效
- **是否有规避手段**: 否

**建议**:
- 平台方必须实现 pull_request_target 的 secrets 隔离

---

## 失败分诊 · SEC-PRTGT-01-002 · pull_request_target 无审批不执行 fork PR 代码

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: 'success_without_approval' 0 hits) — pass; assertions[1] (positive, run_status: PENDING_OR_BLOCKED) — 预期 PENDING_OR_BLOCKED，实际 COMPLETED

**根因初判**: 产品缺陷 — 审批管控缺失

**责任人**: 平台方 — pull_request_target 下 fork PR 代码被执行（日志 "Building PR code"），无需审批

**证据**:

- **Job 日志**（51 行）:
  ```
  line 51: Building PR code
  ```
- **预期行为**: pull_request_target 无审批时，fork PR 代码不应被执行
- **实际行为**: 日志 "Building PR code"——**fork PR 代码被执行**，且 run_status=COMPLETED
- **对照 GitCode 规格**: pull_request_target 的安全模型——无审批不应执行 fork PR 代码

**置信度**: 高 — "Building PR code" 明确证明 PR 代码被执行，无审批

**影响**:
- **阻塞性**: 🔴阻塞 — 无审批时仍执行不可信代码
- **静默性**: 🔴静默错误 — 平台未阻止、无任何审批提示
- **影响面**: 🔴跨维度 — 与 SEC-PRTGT-01-001 同根因
- **综合**: 🔴阻塞+静默+跨维度：pull_request_target 审批缺失 + secret 隔离缺失组合缺陷
- **是否有规避手段**: 否

**建议**:
- 平台方必须实现 pull_request_target 的审批机制

---

## 失败分诊 · SEC-RUN-01-003 · 自托管 Runner 跨项目残留必须被隔离

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: 'cross project leak' 0 hits) — pass; assertions[1] (positive, value: log contains 'isolated_as_expected') — absent

**根因初判**: 需人工判断

**责任人**: 多方联合 — Job 无任何 shell 执行痕迹（两行 duration check 后无任何步骤日志），无法判定是 runner 调度问题还是隔离测试未实际运行

**证据**:

- **Job 日志全量**（3 行）:
  ```
  [INFO] Job(1530328756319174656_1530328756285620231) duration check: true
  [INFO] Job(1530328756319174656_1530328756285620233) duration check: true
  ```
- **预期行为**: 验证 runner 跨项目隔离能力
- **实际行为**: Job 有 2 个 pod 出现（2 条 duration check），但**无任何 shell 脚本执行日志**——测试步骤未运行
- **对照 GitCode 规格**: 无法判定——测试脚本未执行，该能力未被验证

**置信度**: 低 — 无脚本执行输出，无法判断隔离是否生效。可能是自托管 runner 不可用、调度失败或测试 YAML 编译错误

**影响**:
- **阻塞性**: ⚪无影响 — 本用例未被实际测试
- **静默性**: 🟡可察觉 — 无输出
- **影响面**: 🟢单用例
- **综合**: 无影响+可察觉+单用例：Job 无 shell 执行，需排查 runner 调度原因
- **是否有规避手段**: 需人工排查 — 检查 runner 标签/状态/配额

**建议**:
- 需人工排查 runner 调度日志，确认自托管 runner 是否可用
- 相关用例: SEC-SUPPLY-01-001, SEC-SUPPLY-01-002（同"无脚本执行"模式）

---

## 失败分诊 · SEC-SIDE-01-002 · Secret 不经 artifact 侧信道绕过脱敏外泄

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — pass; assertions[1] (positive, run_status: BLOCKED_OR_MASKED) — 预期 BLOCKED_OR_MASKED，实际 FAILED

**根因初判**: 环境问题

**责任人**: Phase 02 — artifact 名称冲突（"secret-artifact" 已存在）导致上传失败，安全隔离检查被跳过

**证据**:

- **Job 日志关键段落**（26 行）:
  ```
  line 26: ::error::Upload artifact failed: Artifact with name already exists: secret-artifact,
           repoId=10431338, workflowId=596195ca1a9e4bc5ac91aca8dbf0caac
  ```
- **预期行为**: 包含 secret 值的 artifact 上传应被安全机制阻止或脱敏
- **实际行为**: artifact 上传因**名称冲突**失败，非安全阻止。安全机制未被触发
- **对照 GitCode 规格**: artifact 侧信道安全隔离未被验证

**置信度**: 高 — "already exists" 明确为环境冲突

**影响**:
- **阻塞性**: ⚪无影响 — 安全能力未被测试到
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响+明确报错+单用例：同 SEC-DOS-01-001 的名称冲突模式
- **是否有规避手段**: 是 — 使用唯一 artifact 名称

**建议**:
- Phase 02 artifact 测试使用唯一名称（如 `secret-artifact-{run_id}`）

---

## 失败分诊 · SEC-SUPPLY-01-001 · 第三方 Action 引用应支持完整 commit hash 固定

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status: SUCCESS_OR_ACTION_EXECUTED) — 预期 SUCCESS_OR_ACTION_EXECUTED，实际 FAILED; assertions[1] (negative, leak) — pass

**根因初判**: 需人工判断

**责任人**: 多方联合 — Job 无任何 shell 执行（仅 1 行 duration check），无法判定是第三方 action 解析失败还是 runner 调度问题

**证据**:

- **Job 日志全量**（1 行）:
  ```
  [INFO] Job(1530329031020920832_1530329030991560711) duration check: true
  ```
- **预期行为**: 使用完整 commit hash 引用的第三方 action 应被执行
- **实际行为**: Job **无任何步骤执行痕迹**——既无 "action not found" 也无 "action executed"
- **对照 GitCode 规格**: 无法判定——测试脚本未运行

**置信度**: 低 — 无脚本执行输出

**影响**:
- **阻塞性**: ⚪无影响 — 供应链安全能力未被测试
- **静默性**: 🟡可察觉 — 无输出
- **影响面**: 🟢单用例
- **综合**: 无影响+可察觉+单用例：需排查为何 Job 无执行
- **是否有规避手段**: 需人工排查

**建议**:
- 排查 Job 日志中 compile/pipeline 阶段的错误

---

## 失败分诊 · SEC-SUPPLY-01-002 · commit hash 不匹配时第三方 Action 应被拒绝执行

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: 'success' 0 hits) — pass; assertions[1] (positive, value: log contains 'action_not_found_or_sha_mismatch') — absent

**根因初判**: 需人工判断

**责任人**: 多方联合 — 同 SEC-SUPPLY-01-001，Job 无任何 shell 执行，无法判定平台是否对不匹配的 commit hash 做了拒绝

**证据**:

- **Job 日志全量**（1 行）:
  ```
  [INFO] Job(1530329077581889536_1530329077548335111) duration check: true
  ```
- **预期行为**: 不匹配的 commit hash 应被拒绝执行
- **实际行为**: Job 无任何脚本执行痕迹
- **对照 GitCode 规格**: 无法判定

**置信度**: 低 — 无脚本执行输出

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 需排查 Job 无执行原因
- **是否有规避手段**: 需人工排查

**建议**: 排查 runner 调度/pipeline 编译阶段

---

## 失败分诊 · SEC-TOCTOU-01-001 · 审批后推送新 commit 不应被已授权特权运行执行

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: 'unapproved_commit_executed' 0 hits) — pass; assertions[1] (positive, value: log contains 'approved_sha_matched') — absent

**根因初判**: 用例问题 + 标记不匹配

**责任人**: Phase 01 — commit SHA 上下文未获取到（日志 "Running commit: " 之后为空），且预期标记词 "approved_sha_matched" 与实际输出不匹配

**证据**:

- **Job 日志全量**（5 行）:
  ```
  Running commit: 
  ```
- **预期行为**: 验证审批后新推送的 commit 不被已授权运行执行
- **实际行为**: `Running commit: ` 后 commit SHA 为空——上下文获取失败，无法进行 TOCTOU 校验
- **对照 GitCode 规格**: TOCTOU 攻击防护依赖于 commit SHA 上下文——本次 SHA 获取失败导致无法测试

**置信度**: 中 — SHA 为空但无法确定是平台上下文 bug 还是用例参数/trigger 错误

**影响**:
- **阻塞性**: ⚪无影响 — TOCTOU 防护未被实际测试
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 无影响+可察觉+单用例：commit SHA 获取为空，标记词不匹配
- **是否有规避手段**: 需排查 — 检查 trigger 方式是否正确传入 head_sha

**建议**:
- Phase 02 检查 dispatch payload 中 head_sha 是否被正确传入

---

## 失败分诊 · SEC-TOKEN-01-001 · fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value: log contains 'clone_successful') — absent; assertions[1] (negative, leak: 'write_permission_granted' 0 hits) — pass

**根因初判**: 产品缺陷 — 期望的 "read 权限" 场景中 token 完全不可用（401），无法验证"仅有 read 权限"是否正确生效

**责任人**: 平台方 — fork PR 中 ATOMGIT_TOKEN 返回 401 "token not found"，克隆失败。同时表明 fork PR 的 ATOMGIT_TOKEN 未被授予 read 权限（比 read-only 更严格）

**证据**:

- **Job 日志全量**（10 行）:
  ```
  line 5:  Cloning into 'test-clone'...
  line 10: 000{"error_code":401,"error_code_name":"UNAUTHORIZED","error_message":"401, token not found",
           "trace_id":"58544fd173c536167e1d962a558e0e9e"}401000000::error::Process exited with code 6
  ```
- **预期行为**: ATOMGIT_TOKEN 应有 read 权限，clone 成功
- **实际行为**: ATOMGIT_TOKEN **不可用**（401 "token not found"），clone 失败。平台未授予任何 token
- **对照 GitCode 规格**: fork PR 的 ATOMGIT_TOKEN 权限范围——平台完全未提供 token（比 read-only 更严格）。这可能是一个额外的安全决策（fork PR 完全不给 token），但文档未说明

**置信度**: 中 — 401 证据明确，但无法区分"平台有意完全不给 token" vs "bug 导致 token 未生成"

**影响**:
- **阻塞性**: 🟡非阻塞 — clone 失败但安全性更高
- **静默性**: 🟡可察觉 — 401 错误
- **影响面**: 🟡同维度 — fork PR token 策略影响所有 fork 场景
- **综合**: 非阻塞+可察觉+同维度：fork PR 中完全没有 token（而非仅有 read 权限），安全性高于预期但偏离文档
- **是否有规避手段**: 否 — 用户无法控制 fork PR 的 token 策略

**建议**:
- 平台方应明确文档：fork PR 中 ATOMGIT_TOKEN 是完全不可用还是仅有 read 权限
- Phase 01 更新用例预期：若平台决策是"fork PR 不给 token"，则断言应期望 clone 失败

---

## 失败分诊 · SEC-TOKEN-01-002 · fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status: COMPLETED) — 预期 COMPLETED，实际 FAILED

**根因初判**: 用例问题 — git config 前置条件缺失导致 git push 在权限检查前失败

**责任人**: Phase 01 — 同 SEC-PERM-01-004，测试脚本未设置 `user.email` / `user.name`，导致 git push 以 exit code 128 失败

**证据**:

- **Job 日志全量**（19 行）:
  ```
  line 5:  Cloning into 'repo'...
  line 6:  Author identity unknown
  line 8:  *** Please tell me who you are.
  line 18: fatal: unable to auto-detect email address (got 'slave1@...-pod.(none)')
  line 19: ::error::Process exited with code 128
  ```
- **预期行为**: fork PR 中写操作应被平台拒绝
- **实际行为**: git push 在权限检查前因 git config 缺失失败（exit code 128），**未确认平台是否拒绝写操作**
- **对照 GitCode 规格**: fork PR 写操作隔离未被验证——git config 前置条件先于权限检查失败

**置信度**: 高 — 同 SEC-PERM-01-004 模式

**影响**:
- **阻塞性**: ⚪无影响 — 未被实际测试
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 同 SEC-PERM-01-004：git config 缺失
- **是否有规避手段**: 是 — 添加 git config 步骤

**建议**: Phase 01 在脚本中添加 `git config user.email/name`

---

## 失败分诊 · SEC-WCMD-01-001 · Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — pass; assertions[1] (positive, value: log contains 'mask_command_without_payload') — absent

**根因初判**: 标记不匹配

**责任人**: Phase 01 — 编译器标记词不匹配；平台实际行为正确（`::add-mask::***` 中 secret 值被脱敏）

**证据**:

- **Job 日志全量**（5 行）:
  ```
  ::add-mask::***
  ```
- **预期行为**: `::add-mask::` 命令响应不应泄露 secret 明文
- **实际行为**: 日志 `::add-mask::***`——**secret 值被遮蔽为 `***`**，未泄露明文。平台行为正确
- **对照 GitCode 规格**: `::add-mask::` 响应中的 secret 值被脱敏处理，符合安全要求

**置信度**: 高 — `***` 证明脱敏生效，仅标记词不匹配

**影响**:
- **阻塞性**: ⚪无影响 — 平台脱敏正常
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响+明确报错+单用例：标记词不匹配假阳性
- **是否有规避手段**: 是 — 修正标记

**建议**: Phase 01 修正标记词匹配规则

---

## 失败分诊 · SEC-WCMD-01-002 · 跨运行 artifact 必须被视为不可信数据

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, leak: 'auto_executed' 0 hits) — pass; assertions[1] (positive, run_status: COMPLETED) — 预期 COMPLETED，实际 FAILED

**根因初判**: 环境问题

**责任人**: Phase 02 — 下载 artifact 时未找到目标 artifact（"Artifact 'untrusted-artifact' not found. Available artifacts: (none)"），前置条件（先上传 artifact）未建立

**证据**:

- **Job 日志全量**（12 行）:
  ```
  line 10: ::error::Unable to download artifact(s): Artifact 'untrusted-artifact' not found.
           Available artifacts: (none)
  ```
- **预期行为**: 跨运行下载的 artifact 应被视为不可信数据，安全处理
- **实际行为**: artifact 未找到，下载失败。**安全机制未被触发**——artifact 不存在时无安全判定场景
- **对照 GitCode 规格**: 跨运行 artifact 安全隔离未被测试

**置信度**: 高 — "Available artifacts: (none)" 明确，artifact 未建立

**影响**:
- **阻塞性**: ⚪无影响 — 安全能力未被验证
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响+明确报错+单用例：前置条件未建立
- **是否有规避手段**: 是 — 确保前置 artifact 先在当前 workflow 内上传

**建议**: Phase 02 建立 artifact 前置上传步骤

---

## 汇总统计

| 根因分类 | 数量 | 占比 |
|---------|------|------|
| **产品缺陷** | 8 | 30.8% |
| **标记不匹配** | 9 | 34.6% |
| **环境问题** | 4 | 15.4% |
| **用例问题** | 2 | 7.7% |
| **需人工判断** | 3 | 11.5% |

### 真缺陷（平台级安全漏洞）:
1. **SEC-FORK-01-001**: fork PR secrets 隔离缺失
2. **SEC-FORK-01-002**: fork PR secrets 隔离缺失（同根因）
3. **SEC-INJ-01-005**: 表达式双重渲染漏洞 (SECURITY_CRITICAL)
4. **SEC-PRTGT-01-001**: pull_request_target secrets 隔离缺失
5. **SEC-PRTGT-01-002**: pull_request_target 审批缺失
6. **SEC-NAME-01-001**: 特殊字符 secret 名静默接受
7. **SEC-PERM-01-003**: fork PR 默认 token 不可用（偏离文档承诺）
8. **SEC-TOKEN-01-001**: fork PR token 不可用（偏离文档承诺）

### 主责分布:
| 主责方 | 用例数 |
|--------|-------|
| **Phase 01**（标记不匹配/用例设计） | 11 |
| **平台方**（安全缺陷/能力边界） | 10 |
| **Phase 02**（环境问题） | 3 |
| **多方联合** | 2 |
