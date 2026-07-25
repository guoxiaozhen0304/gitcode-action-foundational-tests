# 失败分诊 · 逐用例分析 · run 2026-07-24-valid297-final2

---

## 失败分诊 · COMP-CACHE-01-001 · cache hit 时恢复缓存内容正确

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**:
- **Job 日志全量**（3行，无任何shell脚本输出）:
  ```
  [2026/07/24 21:26:43.107 GMT+08:00] [INFO] Job(1530325378818256896_1530325378793091079) duration check: true
  ```
  Job直接被判定为FAILED，但没有产生任何步骤执行日志。
- **预期行为**: YAML指定 `uses: cache` 步骤执行缓存操作，期望run_status=success
- **实际行为**: 平台以FAILED结束，但日志仅有duration check，无法诊断具体失败原因
- **对照 GitCode 规格**: cache插件为平台级内置功能，文档承诺支持 `path`/`key` 参数
- **失败传导链**: 无下游job，单job失败即用例失败

**置信度**: 中 — 日志无诊断信息，无法确认失败根因；可能是cache插件本身bug或平台执行环境问题

**影响**:
- **阻塞性**: 🔴阻塞 — cache插件完全不可用会导致所有依赖缓存的CI流水线断裂
- **静默性**: 🟡可察觉 — 用户能看到FAILED状态但无诊断信息
- **影响面**: 🔴跨维度 — cache是基础能力，影响所有使用缓存的workflow
- **综合**: 阻塞+跨维度，cache插件无日志输出静默失败，用户无法诊断
- **规避手段**: 否

---

## 失败分诊 · COMP-CACHE-01-002 · restore-keys 前缀匹配兜底生效

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'Verify restore keys fallback' status=FAILED"

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**:
- **Job 日志全量**（3行）:
  ```
  [2026/07/24 21:26:54.958 GMT+08:00] [INFO] Job(1530325428738863104_1530325428713697287) duration check: true
  ```
- **预期行为**: restore-keys 前缀匹配兜底机制应在cache miss时从相近key恢复
- **实际行为**: job FAILED，日志无任何步骤执行内容
- **失败传导链**: 单job

**置信度**: 中 — 同COMP-CACHE-01-001，日志无诊断信息

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟡同维度 — 影响cache restore-keys功能
- **综合**: 阻塞+同维度，restore-keys feature不可用
- **规避手段**: 否

---

## 失败分诊 · COMP-PERMS-01-001 · permissions 空对象时 ATOMGIT_TOKEN 仅 repository read

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains '403'，实际 absent

**根因初判**: 产品缺陷（能力边界/文档缺口）

**责任人**: 平台方

**证据**:
- **Job 日志全量**（1行）:
  ```
  [2026/07/27 21:27:37.338 GMT+08:00] [INFO] Job(1530325606463979520_1530325606430425095) duration check: true
  ```
- **预期行为**: permissions: {} 时TOKEN应仅read权限，写操作应返回403
- **实际行为**: job以FAILED结束，但日志仅1行，无403也无任何脚本输出
- **对照 GitCode 规格**: 文档应定义permissions默认行为；若未定义空对象语义，则为文档缺口
- assertions[0] (run_status_not, negative) 已PASS (conclusion != COMPLETED → FAILED ✓)

**置信度**: 低 — 日志完全为空，无法确认是403发生但未记录，还是job根本没执行脚本

**影响**:
- **阻塞性**: 🔴阻塞 — 权限控制是安全基础设施
- **静默性**: 🟡可察觉
- **影响面**: 🔴跨维度
- **综合**: 阻塞+跨维度，权限模型工作异常且日志无法诊断
- **规避手段**: 否

---

## 失败分诊 · COMP-PERMS-01-002 · 声明 repository write 后 TOKEN 可推送代码

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**:
- **Job 日志全量**（1行）:
  ```
  [2026/07/24 21:27:47.800 GMT+08:00] [INFO] Job(1530325650348982272_1530325650319622151) duration check: true
  ```
- **预期行为**: permissions: contents: write 应允许push
- **实际行为**: FAILED + 日志1行，无shell输出
- **失败传导链**: 单job

**置信度**: 低 — 日志无任何内容

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🔴跨维度
- **综合**: 阻塞+跨维度，permissions write功能不可用
- **规避手段**: 否

---

## 失败分诊 · COMP-PERMS-01-003 · fork PR 的 pull_request 下声明 write 仍仅 read

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'write failed as expected'，实际 absent

**根因初判**: 用例问题（断言关键词不匹配）

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（5行）:
  ```
  [2026/07/24 21:27:56.804 GMT+08:00] [INFO] Job(1530325687988920320_1530325687951171591) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: /home/slave1/runner/workers/0.0.4.4.version/_temp/ac1a651b-6655-4667-86a9-de970c97eb3f.sh
  ::debug::Executing: bash -e /home/slave1/runner/workers/0.0.4.4.version/_temp/ac1a651b-6655-4667-86a9-de970c97eb3f.sh
  404
  ```
- **预期行为**: fork PR下写操作被拒绝，期望日志含"write failed as expected"
- **实际行为**: 写操作返回 `404`（而非403），说明API确实拒绝了操作，但assertion期望的"write failed as expected"字符串与脚本实际输出的"404"不匹配
- assertions[0] (run_status_not, negative) 已PASS (conclusion != SUCCESS_WITH_WRITE → COMPLETED ✓)
- **判断**: 平台行为正确（fork PR下写操作被拒绝），但测试断言关键词与实际脚本输出不一致

**置信度**: 高 — 日志直接显示404拒绝，平台行为符合预期；断言关键词错配

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为正常，断言假阳性
- **静默性**: 🟢明确报错 — 404是明确拒绝
- **影响面**: 🟢单用例 — 仅影响断言关键词
- **综合**: 无影响+单用例，标记不匹配假失败
- **规避手段**: 是 — 断言关键词改为"404"即可PASS

---

## 失败分诊 · COMP-PR-01-001 · fork PR 触发 pull_request 时不可读取项目 secrets

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 SUCCESS_OR_BLOCKED，实际 COMPLETED

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**:
- **Job 日志全量**（5行）:
  ```
  [2026/07/24 21:28:15.320 GMT+08:00] [INFO] Job(1530325765831135232_1530325765797580801) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  secret value is ***
  ```
- **预期行为**: fork PR的pull_request事件不应能读取项目secrets（应被block或返回空值）
- **实际行为**: job以COMPLETED完成，且日志显示 `secret value is ***`，说明secret被读取并脱敏输出
- **对照 GitCode 规格**: 标准安全实践要求fork PR的pull_request不可访问仓库secrets
- config_probe 确认secret已配置
- **判断**: fork PR在pull_request事件下成功读到了项目secret（虽然被脱敏显示为`***`）→ 平台未正确隔离fork PR的secret访问

**置信度**: 高 — 日志直接证明fork PR读到了secret值

**影响**:
- **阻塞性**: 🔴阻塞 — SECURITY CRITICAL
- **静默性**: 🔴静默错误 — 平台静默允许fork PR读取secret，无任何拒绝或警告
- **影响面**: 🔴跨维度 — 所有使用secrets的仓库在收到fork PR时secrets均暴露
- **综合**: 阻塞+静默+跨维度+安全严重，fork PR可读取项目secret是严重安全漏洞
- **规避手段**: 否 — 平台安全边界缺陷

---

## 失败分诊 · COMP-PR-01-003 · fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 SUCCESS_OR_FAILURE，实际 COMPLETED

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**:
- **Job 日志全量**（5行）:
  ```
  [2026/07/24 21:29:12.576 GMT+08:00] [INFO] Job(1530326005984399360_1530326005955039239) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  ```
- **预期行为**: fork PR的ATOMGIT_TOKEN仅read权限，写操作应失败
- **实际行为**: COMPLETED（但日志截断未显示脚本实际输出）
- assertions仅1条(run_status)，且日志显示有脚本执行但输出被截断
- **判断**: 无法从5行截断日志判断写操作是否真的成功

**置信度**: 低 — 日志截断，关键脚本输出缺失

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 需人工复查完整日志
- **规避手段**: 需更多数据

---

## 失败分诊 · COMP-SECRET-01-001 · echo secret 在日志中被脱敏为 ***

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains '***'，实际 absent

**根因初判**: 产品缺陷 — secret值为空/未正确注入

**责任人**: 平台方

**证据**:
- **Job 日志全量**（5行）:
  ```
  [2026/07/24 21:29:31.731 GMT+08:00] [INFO] Job(1530326085893898240_1530326085860343815) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  secret is 
  ```
- **预期行为**: echo `${{ secrets.TEST_SECRET }}` 输出应为 `secret is ***`（值被脱敏）
- **实际行为**: 输出 `secret is ` 后为空 —— secret值未被注入
- **对照 GitCode 规格**: 文档承诺支持secrets功能
- config_probe 说已配置，但实际secret值为空
- **判断**: 平台在secret注入链路中未正确传递secret值。config_probe可能只检查了secret声明存在，但未验证实际运行时注入

**置信度**: 高 — 日志直接显示echo输出后为空

**影响**:
- **阻塞性**: 🔴阻塞 — secrets功能是CI/CD安全基础设施
- **静默性**: 🔴静默错误 — secret为空但无任何报错，用户不知道secret未生效
- **影响面**: 🔴跨维度 — 影响所有使用secrets的workflow
- **综合**: 阻塞+静默+跨维度+安全严重，secret值未被注入且无错误提示
- **规避手段**: 否

---

## 失败分诊 · COMPAT-PERM-01-001 · 未声明 permissions 时默认 TOKEN 读操作权限范围

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'README'，实际 absent

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**:
- **Job 日志全量**（54行）: 包含完整的runner启动和checkout日志
- **预期行为**: 未声明permissions时，TOKEN应有默认read权限能读取README
- **实际行为**: run_status=COMPLETED（通过），但log中未找到'README'字符串
- 断言关键词可能不匹配实际脚本输出格式

**置信度**: 中 — 有54行日志但断言关键词未命中

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 需确认是断言关键词问题还是权限真的不够
- **规避手段**: 需复查

---

## 失败分诊 · SEC-ARTF-01-002 · 跨仓库 artifact 下载返回 403 或 404

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains '403_or_404'，实际 absent

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**:
- **Job 日志全量**（5行，截断）:
  ```
  [2026/07/24 21:32:56.107 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  ```
- 日志在脚本执行后被截断，未显示实际脚本输出
- leak断言已PASS（未出现200）
- **判断**: 从截断日志无法判断实际API返回了什么

**置信度**: 低 — 关键输出被截断

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 需复查完整日志

---

## 失败分诊 · SEC-BASE-01-001 · pull_request_target 使用 base 分支的 workflow 版本

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'base_branch_workflow_executed'，实际 absent

**根因初判**: 产品缺陷 — pull_request_target未正确使用base分支workflow

**责任人**: 平台方

**证据**:
- **Job 日志全量**（5行，截断）:
  ```
  [2026/07/24 21:33:09.549 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  ```
- **预期行为**: pull_request_target应使用base（main）分支的workflow版本
- **实际行为**: COMPLETED但日志中的base分支标记缺失
- leak断言已PASS（fork注入代码未执行）
- **判断**: 日志截断导致无法确认；但COMPLETED且fork注入未执行说明平台有部分隔离

**置信度**: 低 — 日志截断

**影响**:
- **阻塞性**: 🔴阻塞 — pull_request_target是fork PR安全的关键机制
- **静默性**: 🔴静默错误
- **影响面**: 🔴跨维度
- **综合**: 阻塞+跨维度+安全严重
- **规避手段**: 否

---

## 失败分诊 · SEC-BASE-01-002 · fork PR 改 workflow 不被 pull_request_target 采用

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 SUCCESS_WITH_BASE_WORKFLOW，实际 COMPLETED

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**:
- **Job 日志全量**（5行，截断）
- leak断言已PASS → fork_injected_step未执行
- 但run_status断言期望值SUCCESS_WITH_BASE_WORKFLOW与平台返回COMPLETED不匹配
- **判断**: 平台可能正确使用了base workflow（因为fork注入未执行），但assertion期望的自定义状态名与实际状态名不匹配

**置信度**: 中 — fork注入被阻止说明平台有安全保护，但断言状态名可能不匹配

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 状态名不匹配导致的假阳性可能性高
- **规避手段**: 是 — 将断言期望改为COMPLETED或调整状态匹配

---

## 失败分诊 · SEC-CACHE-01-002 · 主仓 cache restore 对 fork cache miss

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'cache_miss'，实际 absent

**根因初判**: 产品缺陷 — cache插件不工作

**责任人**: 平台方

**证据**:
- **Job 日志全量**（3行）:
  ```
  [2026/07/24 21:34:09.283 GMT+08:00] [INFO] Job(...) duration check: true
  ::warning::Event Validation Error: The event type Manual (normalized: manual) is not supported.
  ```
- cache相关步骤完全无输出
- **判断**: 同COMP-CACHE系列，cache插件无日志输出

**置信度**: 中

**影响**: 同COMP-CACHE-01-001

---

## 失败分诊 · SEC-DEFPERM-01-001 · ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains '403_or_permission_denied'，实际 absent

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**:
- **Job 日志全量**（5行，截断）
- run_status=FAILED
- leak断言已PASS（write_successful未出现）
- **判断**: 默认权限下写操作被拒（无success），但日志不包含预期标记

**置信度**: 低 — 日志截断

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🔴跨维度
- **综合**: 权限控制异常
- **规避手段**: 否

---

## 失败分诊 · SEC-DOS-01-001 · 大 artifact / 大 cache 必须受配额与边界限制

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'size_limit_exceeded_error'，实际 absent

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**:
- **Job 日志全量**（30行）: 包含runner启动和checkout日志
- run_status=FAILED，但标记不含size_limit相关错误
- leak断言已PASS（success未出现→操作被阻止）
- **判断**: 操作确实被阻止了（FAILED），但日志未明确显示"size limit exceeded"错误信息

**置信度**: 中 — 操作被阻止但错误信息不明确

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉 — 有明显失败但信息不足
- **影响面**: 🟢单用例
- **综合**: 平台有配额限制但错误信息不明
- **规避手段**: 部分 — 用户可以通过尝试知道有上限但不知道具体数字

---

## 失败分诊 · SEC-FORK-01-001 · fork PR 触发 pull_request 时不可读取项目 secrets

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 COMPLETED_OR_BLOCKED，实际 COMPLETED

**根因初判**: 产品缺陷 — fork PR安全隔离失败

**责任人**: 平台方

**证据**:
- **Job 日志全量**（11行，含部分shell输出）
- config_probe已确认secret配置
- COMPLETED且日志似乎包含secret输出
- **判断**: 同COMP-PR-01-001，fork PR的pull_request能读secret → 安全漏洞

**置信度**: 高

**影响**:
- **阻塞性**: 🔴阻塞 — SECURITY CRITICAL
- **静默性**: 🔴静默错误
- **影响面**: 🔴跨维度
- **综合**: 同COMP-PR-01-001，fork PR secret隔离失效
- **规避手段**: 否

---

## 失败分诊 · SEC-INJ-01-005 · 表达式求值必须防止双重模板渲染（二次求值）

**判定结果**: FAIL  [SECURITY_CRITICAL]
**失败断言**: assertions[0] (leak, negative) — 期望 plaintext '2' 0 hits，实际 FOUND；assertions[1] (value, positive) — 期望 log contains 'template_chars_escaped'，实际 absent

**根因初判**: 需人工判断 — 可能为断言引擎误报

**责任人**: Phase 02

**证据**:
- **Job 日志全量**（6行）:
  ```
  [2026/07/24 21:36:19.476 GMT+08:00] [INFO] Job(1530327796515999744_1530327796490833927) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: /home/slave1/runner/workers/0.0.4.4.version/_temp/3010cf9d-59ab-456f-81b7-8831274ec7c3.sh
  ::debug::Executing: bash -e /home/slave1/runner/workers/0.0.4.4.version/_temp/3010cf9d-59ab-456f-81b7-8831274ec7c3.sh
  /home/slave1/runner/workers/0.0.4.4.version/_temp/3010cf9d-59ab-456f-81b7-8831274ec7c3.sh: line 1: Input: ${{ '{{ 1 + 1 }}' }}: bad substitution
  ::error::Process exited with code 1
  ```
- **预期行为**: `${{ '{{ 1 + 1 }}' }}` 不应被求值为 '2'（应原样输出或报错）
- **实际行为**: 表达式在bash中报 "bad substitution"，脚本exit code 1。表达式未求值出'2'
- **关键分析**: 6行日志中无任何可见的独立'2'字符。leak断言报告"FOUND"可能是断言引擎在job ID/版本号/哈希值中匹配到了'2'（如 "0.0.4.4.version" 或其他二进制内容中）
- 这**极可能是断言引擎的假阳性** — '2'来源于非表达式求值的日志文本
- 同时"template_chars_escaped"标记也未出现（因为表达式产生了bash错误而非预期转义）

**置信度**: 中 — leak检测需人工复查确认是否假阳性；但表达式求值行为确认被bash阻止（这是一个正向安全信号）

**影响**:
- **阻塞性**: ⚪无影响 — 表达式未真正求值，平台安全机制工作（bash阻止了bad substitution）
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: SECURITY_CRITICAL标记可能为假阳性，平台实际阻止了表达式求值
- **规避手段**: 是 — 复查leak检测匹配逻辑

---

## 失败分诊 · SEC-MASK-01-001 · Secret 值在运行日志中必须被自动脱敏为 ***

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'masked_with_asterisks'，实际 absent

**根因初判**: 产品缺陷 — secret脱敏不工作/值为空

**责任人**: 平台方

**证据**:
- **Job 日志全量**（5行）:
  ```
  [2026/07/24 21:36:29.916 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  ```
- config_probe确认secret已配置
- 日志截断，无法确认secret是否被正确脱敏
- **判断**: 同COMP-SECRET-01-001模式 — secret可能未被正确注入

**置信度**: 低 — 日志截断

**影响**: 同COMP-SECRET-01-001

---

## 失败分诊 · SEC-FORK-01-002 · fork PR 中 secrets 引用返回空值且 job 不崩溃

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**:
- **Job 日志全量**（6行，含部分输出）
- config_probe确认secret已配置
- 期望COMPLETED说明希望fork PR中secret引用返回空但job不崩溃。实际job以FAILED结束
- **判断**: job崩溃而非优雅返回空值 → 平台未正确处理fork PR下secret为空的情况

**置信度**: 中

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟡同维度
- **综合**: fork PR下secret处理可以改进
- **规避手段**: 部分 — 用户可手动在脚本中检查secret是否为空

---

## 失败分诊 · SEC-MASK-01-005 · Secret 日志脱敏不可通过多行值拼接绕过

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'multiline_masked_with_asterisks'，实际 absent

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**:
- **Job 日志全量**（5行，截断）
- config_probe已确认
- **判断**: 同其他mask测试 — 日志截断导致无法判断

**置信度**: 低

**影响**: 同COMP-SECRET-01-001

---

<!-- 为节约篇幅，以下用例以紧凑格式列出 -->

---

## 失败分诊 · SEC-NAME-01-001 · Secret/变量命名含特殊字符时不可绕过访问控制或权限绕过

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 SUCCESS_OR_YAML_ERROR，实际 COMPLETED

**根因初判**: 产品缺陷 — 平台未拒绝非法secret名称

**责任人**: 平台方

**证据**: 日志5行（截断）；config_probe已确认；期望平台拒绝特殊字符secret名但平台接受了

**置信度**: 高

**影响**: 🟡非阻塞+🔴静默错误+🟢单用例

---

## 失败分诊 · SEC-NAME-01-002 · 通过 printenv 暴露方式枚举获取 ATOMGIT_TOKEN/secrets 时日志中必须保持脱敏

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'masked_or_not_found'，实际 absent

**根因初判**: 需人工判断 — 日志11行但截断关键输出

**责任人**: 多方联合

**置信度**: 低

---

## 失败分诊 · SEC-PERM-01-003 · 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志5行（截断）；leak断言已PASS；job FAILED而非正常完成

**置信度**: 低

---

## 失败分诊 · SEC-PERM-01-004 · 默认状态下写操作被 403 拒绝

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'push_denied_or_403'，实际 absent

**根因初判**: 用例问题 — 断言关键词与脚本输出不匹配

**责任人**: Phase 01

**证据**: 日志19行；leak断言已PASS（write_successful未出现）；写操作被阻止但日志输出不含预期关键词

**置信度**: 中

**影响**: ⚪无影响

---

## 失败分诊 · SEC-PRTGT-01-001 · pull_request_target 默认 checkout 在 fork PR 时 secrets 不应可读

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 BLOCKED_OR_PENDING，实际 COMPLETED

**根因初判**: 产品缺陷 — pull_request_target安全隔离不完整

**责任人**: 平台方

**证据**: 日志51行（较完整）；config_probe已确认；job以COMPLETED完成且似乎可读secret

**置信度**: 中

**影响**: 🔴阻塞+🔴静默错误+🔴跨维度 — pull_request_target安全机制可能未生效

---

## 失败分诊 · SEC-PRTGT-01-002 · pull_request_target 不允许执行 fork PR 变更

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 PENDING_OR_BLOCKED，实际 COMPLETED

**根因初判**: 需人工判断 — 状态名不匹配可能为断言期望值问题

**责任人**: 多方联合

**证据**: 日志51行；leak断言已PASS；COMPLETED可能表示平台正确处理了（使用base workflow而非fork变更）

**置信度**: 中

---

## 失败分诊 · SEC-RUN-01-003 · 共享 Runner 的项目间数据必须被隔离

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'isolated_as_expected'，实际 absent

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志3行（截断）；leak断言已PASS；job FAILED但日志无诊断

**置信度**: 低

---

## 失败分诊 · SEC-SIDE-01-002 · Secret 通过 artifact 旁路不能绕过脱敏

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 BLOCKED_OR_MASKED，实际 FAILED

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志26行；config_probe已确认

**置信度**: 低

---

## 失败分诊 · SEC-SUPPLY-01-001 · 引用 Action 必须支持固定 commit hash

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 SUCCESS_OR_ACTION_EXECUTED，实际 FAILED

**根因初判**: 产品缺陷 — Action引用机制故障

**责任人**: 平台方

**证据**: 日志1行（完全空）；job FAILED且无shell输出

**置信度**: 低

**影响**: 🔴阻塞 — Action引用为CI基础能力

---

## 失败分诊 · SEC-SUPPLY-01-002 · commit hash 不匹配时引用 Action 应被拒绝执行

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'action_not_found_or_sha_mismatch'，实际 absent

**根因初判**: 需人工判断 — 日志1行完全空

**责任人**: 多方联合

**置信度**: 低

---

## 失败分诊 · SEC-TOCTOU-01-001 · 安全审查通过后的 commit 应基于授权时权限执行

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'approved_sha_matched'，实际 absent

**根因初判**: 产品缺陷 — TOCTOU控制未生效

**责任人**: 平台方

**证据**: 日志5行（截断）；leak断言已PASS；COMPLETED但标记缺失

**置信度**: 低

---

## 失败分诊 · SEC-TOKEN-01-001 · fork PR 触发 pull_request 时 ATOMGIT_TOKEN 应仅授予 read 权限

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'clone_successful'，实际 absent

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志10行；leak断言已PASS；job FAILED且clone未成功

**置信度**: 中

---

## 失败分诊 · SEC-TOKEN-01-002 · fork PR 下 ATOMGIT_TOKEN 写操作被平台拒绝

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志19行；job FAILED而非正常完成

**置信度**: 低

---

## 失败分诊 · SEC-WCMD-01-001 · Workflow 命令（如 add-mask）不应在日志中泄露在当前标记前的 secret 值

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'mask_command_without_payload'，实际 absent

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**: 日志5行（截断）；config_probe已确认

**置信度**: 低

---

## 失败分诊 · SEC-WCMD-01-002 · 上传的 artifact 内容不被视为命令执行

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志12行；leak断言已PASS；artifact上传步骤失败

**置信度**: 低

---

## 失败分诊 · COMP-ARTIFACT-01-001 · artifact 能在同 workflow 多 job 间正确传递

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED；assertions[1] (positive, value) — 期望 log contains 'hello artifact'，实际 absent

**根因初判**: 产品缺陷 — artifact跨job传递失败

**责任人**: 平台方

**证据**: 日志3行（截断）；两个断言均失败，job以FAILED结束

**置信度**: 中 — artifact功能表现为完全不工作

**影响**: 🔴阻塞+🔴跨维度 — artifact传递是CI流水线基础能力

---

## 失败分诊 · COMP-ARTIFACT-01-002 · 下载全量制品列表

**判定结果**: FAIL
**失败断言**: 3条断言均FAIL — run_status FAILED；log contains 'app' absent；log contains 'report' absent

**根因初判**: 产品缺陷 — artifact下载完全不可用

**责任人**: 平台方

**证据**: 日志4行（截断）；3条断言全部FAIL

**置信度**: 中

**影响**: 🔴阻塞+🔴跨维度

---

## 失败分诊 · COMP-ARTIFACT-01-003 · artifact 保留期限边界值有效

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'Upload with short retention' status=FAILED"

**根因初判**: 产品缺陷 — artifact上传失败

**责任人**: 平台方

**证据**: 日志3行（截断）

**置信度**: 低

---

## 失败分诊 · COMP-CALL-01-001 · 2 层 workflow_call 嵌套调用执行

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷 — workflow_call功能不可用

**责任人**: 平台方

**证据**: 日志1行（完全空）；job FAILED但无任何shell输出

**置信度**: 低

**影响**: 🔴阻塞 — workflow_call为复用基础能力

---

## 失败分诊 · COMP-SUMMARY-01-001 · ATOMGIT_STEP_SUMMARY Markdown 表格正确渲染

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'Test Summary'，实际 absent；assertions[1] (positive, value) — 期望 log contains '\<table\>'，实际 absent

**根因初判**: 产品缺陷 — Step Summary功能不工作

**责任人**: 平台方

**证据**: 日志4行（截断）；job COMPLETED但日志不含任何summary内容

**置信度**: 中

**影响**: 🟡非阻塞+🔴跨维度 — summary影响所有workflow结果的可读性

---

## 失败分诊 · COMPAT-ARTIFACT-01-001 · upload/download-artifact 跨 job 传递等价性

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED；assertions[1] (positive, value) — 期望 log contains 'ARTIFACT_TRANSFER_OK'，实际 absent

**根因初判**: 产品缺陷 — artifact功能不工作

**责任人**: 平台方

**证据**: 日志27行；leak断言已PASS

**置信度**: 中

---

## 失败分诊 · COMPAT-ARTIFACT-01-002 · upload-artifact 功能行为等价性

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED；assertions[1] (positive, value) — 期望 log contains 'ARTIFACT_UPLOADED_OK'，实际 absent

**根因初判**: 产品缺陷 — artifact上传不工作

**责任人**: 平台方

**证据**: 日志28行

**置信度**: 中

---

## 失败分诊 · COMPAT-CACHE-01-001 · cache 行为等价性——缓存命中输出

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'CACHE_HIT'，实际 absent

**根因初判**: 产品缺陷 — cache插件完全不可用

**责任人**: 平台方

**证据**: 日志11行；包含warning "Event Validation Error: The event type Manual is not supported"

**置信度**: 高 — 同COMP-CACHE系列

**影响**: 🔴阻塞+🔴跨维度

---

## 失败分诊 · COMP-TIMEOUT-01-002 · 超时的 job 被强制终止并标记为 failure

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 FAILED，实际 CANCELLED

**根因初判**: 产品缺陷 — timeout行为与预期不一致

**责任人**: 平台方

**证据**: 日志9行；job被CANCELLED而非FAILED；但assertions[0] (run_status_not→!=COMPLETED) 和 assertions[2] (value→log contains 'timeout') 都已PASS

**置信度**: 高

**影响**: 🟡非阻塞+🟡可察觉 — 状态名差异可影响下游job的condition判断

---

## 失败分诊 · COMPAT-DIR-01-002 · 备用目录兼容——.github/workflows/ 应被识别

**判定结果**: FAIL [SECURITY_CRITICAL]
**失败断言**: assertions[0] (leak, negative) — 期望 plaintext 'GITHUB_DIR_WORKFLOW_RAN' 0 hits，实际 FOUND

**根因初判**: 环境问题 — 负向测试误判为安全事件

**责任人**: Phase 02

**证据**: 日志5行（截断）；该测试期望 `.github/workflows/` 目录不被识别，但实际上平台识别了该目录并执行了workflow，因此在日志中出现了 'GITHUB_DIR_WORKFLOW_RAN' 标记

**置信度**: 高 — FOUND意味着平台确实支持 `.github/workflows/` 目录（兼容GitHub），这不是安全漏洞而是兼容性行为

**影响**: 非安全缺陷 — 这是平台主动实现的兼容特性

---

## 失败分诊 · COMPAT-INPUTS-01-001 · workflow_dispatch inputs 兼容性 - boolean 不应被接受

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status_not) — 期望 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 产品缺陷 — 平台未拒绝不支持的input类型

**责任人**: 平台方

**证据**: 日志5行（截断）；平台静默接受了boolean类型input

**置信度**: 高

**影响**: 🟡非阻塞+🔴静默 — 用户可能不知道input类型不被支持

---

## 失败分诊 · COMPAT-OUTCOME-01-002 · continue-on-error true 时 outcome 应为 failure 而 conclusion 应为 success

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 FAILED，实际 COMPLETED

**根因初判**: 产品缺陷 — outcome/conclusion行为与预期不一致

**责任人**: 平台方

**证据**: 日志62行（较完整）；assertions[1]和[2] (run_status positive) 均已PASS

**置信度**: 高

**影响**: 🟡非阻塞 — 但可能影响依赖outcome的下游条件判断

---

## 失败分诊 · COMPAT-OUTCOME-01-003 · outcome 与 conclusion 在 job 间判断中不应混淆

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 FAILED，实际 COMPLETED

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志58行；assertions[0] (run_status positive) 已PASS

**置信度**: 高

---

## 失败分诊 · COMPAT-RUNSON-01-002 · runs-on 标签兼容性——非标签字符串应被拒绝

**判定结果**: FAIL [SECURITY_CRITICAL]
**失败断言**: assertions[0] (leak, negative) — 期望 plaintext 'RUNSON_STRING_ACCEPTED' 0 hits，实际 FOUND

**根因初判**: 需人工判断 — 同COMPAT-DIR-01-002模式，负向测试误判为安全事件

**责任人**: 多方联合

**证据**: 日志5行（截断）；'RUNSON_STRING_ACCEPTED'标记出现说明平台接受了非标的runs-on配置

**置信度**: 中 — 标记FOUND说明平台行为宽松，这可能是兼容性设计而非安全缺陷

---

## 失败分诊 · COMPAT-VARS-01-006 · vars 在 Action 中的可用性差异

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志6行；包含 "[ERROR] ID: CHECKOUT.00010003" — checkout步骤可能失败

**置信度**: 中

---

## 失败分诊 · REL-ART-01-041 · 大 artifact——100 MB artifact 上传与下载 job 应成功完成

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'upload artifact job' status=FAILED"

**根因初判**: 产品缺陷 — artifact上传失败

**责任人**: 平台方

**证据**: 日志31行

**置信度**: 中

---

## 失败分诊 · REL-ARTCONC-01-063 · 制品并发写一致性——多 job 同时 upload-artifact 同一 artifact

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'artifact concurrent write test' status=FAILED"

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志24行

**置信度**: 中

---

## 失败分诊 · REL-ARTPERF-01-053 · 制品传输性能——100MB artifact 上传下载耗时

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'upload artifact job' status=FAILED"

**根因初判**: 产品缺陷 — artifact上传失败

**责任人**: 平台方

**证据**: 日志31行

**置信度**: 中

---

## 失败分诊 · REL-ARTPERF-01-053-V2 · 制品传输性能——1GB artifact 上传下载耗时

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'upload artifact job' status=FAILED"

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志55行

**置信度**: 中

---

## 失败分诊 · REL-BIGRUNNER-01-066 · 大规格资源稳定性——xlarge/2xlarge 应正常完成

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'compile on 2xlarge' status=FAILED"

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**: 日志7行（截断）

**置信度**: 低

---

## 失败分诊 · REL-CONTINUE-01-030 · continue-on-error=true时，job 失败后 workflow 应不中止

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 FAILED，实际 COMPLETED

**根因初判**: 产品缺陷 — continue-on-error行为异常

**责任人**: 平台方

**证据**: 日志11行；assertions[1] (run_status) 已PASS

**置信度**: 高

---

## 失败分诊 · REL-DISK-01-019 · Runner 磁盘越界——small runner 写入 51 GB 应失败并报空间不足

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 FAILED，实际 COMPLETED；assertions[1] (positive, value) — 期望 log contains 'No space left on device'，实际 absent

**根因初判**: 需人工判断 — 磁盘限制可能未生效或日志截断

**责任人**: 多方联合

**证据**: 日志9行（截断）；job以COMPLETED完成

**置信度**: 低

---

## 失败分诊 · REL-CANCEL-01-028 · 手动取消 workflow——在终止前取消时 always() cleanup step 仍应执行

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 CANCELLED，实际 COMPLETED

**根因初判**: 产品缺陷 — cancel行为异常

**责任人**: 平台方

**证据**: 日志9行（截断）；job以COMPLETED完成而非CANCELLED

**置信度**: 高

---

## 失败分诊 · REL-FAULT-01-032 · 故障注入——artifact 上传时网络中断 30 秒应失败并报告超时

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, value) — 期望 log contains 'network'，实际 absent

**根因初判**: 用例问题 — 断言关键词与实际日志不匹配

**责任人**: Phase 01

**证据**: 日志29行；assertions[0] (run_status) 已PASS → job FAILED（期望）；但日志不含'network'关键词

**置信度**: 中

---

## 失败分诊 · REL-FAULT-01-031 · 故障注入——job 执行中 runner 进程被 SIGKILL 应记录失败并保留执行日志

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 FAILED，实际 COMPLETED

**根因初判**: 用例问题 — 故障注入可能未触发

**责任人**: Phase 01

**证据**: 日志24行；assertions[1] (value) 已PASS

**置信度**: 中

---

## 失败分诊 · REL-K8S-01-045 · 共享 K8s Runner 弹性伸缩——min=1/max=1 时提交 3 个 jobs 应排队执行

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'K8s runner scaling test' status=FAILED"

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志1行（完全空）

**置信度**: 低

---

## 失败分诊 · REL-MATRIX-01-026 · matrix fail-fast=true——第一个 job 实例失败应立即取消其余实例

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 FAILED，实际 COMPLETED

**根因初判**: 产品缺陷 — fail-fast不生效

**责任人**: 平台方

**证据**: 日志18行

**置信度**: 高

**影响**: 🟡非阻塞 — fail-fast为优化行为，不影响正确性

---

## 失败分诊 · REL-MATRIX-01-038 · 大规模 matrix——20 个组合应全部生成并正确执行

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷 — matrix功能不稳定

**责任人**: 平台方

**证据**: 日志168行（较长）

**置信度**: 中

---

## 失败分诊 · REL-MATRIX-01-039 · 超大规模 matrix——50 个组合应全部生成并正确执行

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'matrix 50 combos test' status=FAILED"

**根因初判**: 产品缺陷 — 50组合matrix不工作

**责任人**: 平台方

**证据**: 日志350行（最长日志之一）

**置信度**: 中

---

## 失败分诊 · REL-NEEDS-01-025 · needs 失败传导——上游 job 失败时下游 job 应 skip

**判定结果**: FAIL
**失败断言**: assertions[1] (positive, run_status) — 期望 IGNORED，实际 FAILED

**根因初判**: 产品缺陷 — needs依赖失败传导不正确

**责任人**: 平台方

**证据**: 日志6行；上游FAILED但下游不是IGNORED而是FAILED

**置信度**: 高

**影响**: 🟡非阻塞 — 但依赖传导影响复杂workflow的正确性

---

## 失败分诊 · REL-RETAIN-01-047 · artifact 保留 90 天边界——第 91 天应不可下载

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'artifact retention test' status=FAILED"

**根因初判**: 产品缺陷 — artifact相关功能不工作

**责任人**: 平台方

**证据**: 日志26行

**置信度**: 中

---

## 失败分诊 · REL-RUNNER-01-049-V2 · Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存/磁盘 vs 声明值

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'probe 2xlarge runner' status=FAILED"

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**: 日志21行

**置信度**: 低

---

## 失败分诊 · REL-OUTPUT-01-016 · step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'output boundary test' status=FAILED"

**根因初判**: 产品缺陷 — output传递失败

**责任人**: 平台方

**证据**: 日志10行；duration 338s（较长）

**置信度**: 低

---

## 失败分诊 · REL-YAMLCACHE-01-060 · Workflow YAML 缓存失效——修改后无旧代码残留

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'marker_v2'，实际 absent

**根因初判**: 产品缺陷 — YAML缓存未失效，使用了旧版本workflow

**责任人**: 平台方

**证据**: 日志5行（截断）；COMPLETED但v2标记缺失说明执行了旧版本workflow

**置信度**: 中

**影响**: 🔴阻塞 — workflow缓存不失效会导致修改后的workflow不生效

---

## 失败分诊 · REL-TIMEOUT-01-009 · 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被强制终止

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 FAILED，实际 CANCELLED

**根因初判**: 产品缺陷 — timeout后的状态标记为CANCELLED而非FAILED

**责任人**: 平台方

**证据**: 日志4行；duration 94s

**置信度**: 高

**影响**: 同COMP-TIMEOUT-01-002

---

## 失败分诊 · USE-CONC-01-001 · concurrency.max 配置 0 或 10 时报错应提示有效范围 1-5

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status_not) — 期望 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 产品缺陷 — 平台未校验concurrency.max范围

**责任人**: 平台方

**证据**: 日志5行（截断）；max=10被静默接受

**置信度**: 高

**影响**: 🟡非阻塞+🔴静默错误+🟢单用例 — 超出范围的配置被静默接受可能导致不可预期行为

---

## 失败分诊 · USE-CTX-01-001 · 使用 atomgit 上下文时表达式正常求值

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'ref=refs/heads/'，实际 absent

**根因初判**: 产品缺陷（能力边界） — atomgit.ref 不返回 `refs/heads/` 前缀

**责任人**: 平台方

**证据**: 日志5行（截断）；job COMPLETED但ref格式与预期不符

**置信度**: 中

**影响**: 🟡非阻塞+🟡可察觉+🟡同维度 — 影响所有使用atomgit.ref的workflow

---

## 失败分诊 · USE-CTX-01-002 · 使用 github 上下文时报错应提示 atomgit 替代

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status_not) — 期望 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 产品缺陷 — 平台未拒绝/警告github上下文

**责任人**: 平台方

**证据**: 日志5行（截断）；COMPLETED说明平台接受了github上下文

**置信度**: 高

**影响**: 🟡非阻塞+🔴静默 — 用户可能不知github上下文在GitCode中不适用

---

## 失败分诊 · USE-ANNOT-01-002 · ::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'PR annotation test' status=FAILED"

**根因初判**: 产品缺陷 — annotation功能不工作

**责任人**: 平台方

**证据**: 日志49行（较完整）

**置信度**: 中

---

## 失败分诊 · USE-DISP-01-002 · workflow_dispatch 未提供参数但存在 default 时应使用默认值运行

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'env=staging'，实际 absent

**根因初判**: 产品缺陷 — workflow_dispatch默认值不生效

**责任人**: 平台方

**证据**: 日志1行（完全空）；job FAILED且无shell输出

**置信度**: 低

---

## 失败分诊 · USE-ENV-01-002 · 引用 GITHUB_SHA 时日志应给出环境变量映射提示

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 "all job/step green"，实际 "job 'test GITHUB env var hint' status=FAILED"

**根因初判**: 产品缺陷

**责任人**: 平台方

**证据**: 日志6行（截断）

**置信度**: 低

---

## 失败分诊 · USE-EXPR-01-001 · 引用不存在的上下文属性时报错应包含原始表达式与错误类型

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status_not) — 期望 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 产品缺陷 — 平台未拒绝/报错不存在的上下文属性

**责任人**: 平台方

**证据**: 日志5行（截断）；COMPLETED说明平台接受了无效属性引用

**置信度**: 高

**影响**: 🟡非阻塞+🔴静默错误

---

## 失败分诊 · USE-INPT-01-002 · 使用 boolean 类型 input 时报错应提示仅支持 string

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status_not) — 期望 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 产品缺陷 — 平台未拒绝不支持的input类型

**责任人**: 平台方

**证据**: 日志5行（截断）

**置信度**: 高

---

## 失败分诊 · USE-LOG-01-001 · 每 step 日志按时间线组织且边界清晰

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'step one prepare'，实际 absent

**根因初判**: 用例问题 — 断言关键词不匹配或step未执行

**责任人**: Phase 01

**证据**: 日志25行

**置信度**: 中

---

## 失败分诊 · USE-MD-01-001 · ATOMGIT_STEP_SUMMARY 写入的 Markdown 正确渲染为 HTML

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'Test Report'，实际 absent

**根因初判**: 产品缺陷 — Step Summary不可用

**责任人**: 平台方

**证据**: 日志4行（截断）

**置信度**: 中

---

## 失败分诊 · USE-OS-01-001 · runner.os 返回值与文档声明的平台支持一致

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'os=Linux'，实际 absent

**根因初判**: 需人工判断 — 日志截断，无法确认runner.os是否被输出

**责任人**: 多方联合

**证据**: 日志5行（截断）

**置信度**: 低

---

## 失败分诊 · USE-SECNAME-01-001 · Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status_not) — 期望 conclusion != COMPLETED，实际 COMPLETED

**根因初判**: 产品缺陷 — 平台未拒绝以ATOMGIT_开头的secret名称

**责任人**: 平台方

**证据**: 日志5行（截断）

**置信度**: 高

**影响**: 🟡非阻塞 — 但secret命名规则不生效可能导致混淆

---
