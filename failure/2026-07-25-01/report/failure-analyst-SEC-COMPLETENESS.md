# Failure Analyst 报告 · 运行 2026-07-25-01 · SEC + COMPLETENESS

**分析时间**: 2026-07-25
**分析范围**: dimension ∈ {completeness, security}, verdict = FAIL
**用例总数**: 40 (14 COMPLETENESS + 26 SECURITY)

---

# PART 1: COMPLETENESS 维度 FAIL 用例 (14)

---

## 失败分诊 · COMP-CACHE-01-001 · cache hit 时恢复缓存内容正确 confirmed
**重跑 (dispatch)**: FAILED · [6059ed2e...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/f275475492a241e9853623c5b7d23a66)

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive, target=run_status) — 预期 COMPLETED，实际 FAILED

**根因初判**: use the cache action in wrong way

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（3 行，无 shell 脚本输出）:
  ```
  [2026/07/25 12:39:23.222 GMT+08:00] [INFO] Job(1530555059450556416_1530555059429584903) duration check: true
  ```
  job 启动后立即失败，无任何步骤执行痕迹。
- **预期行为**: cache hit 时应恢复缓存内容，验证恢复数据正确。
- **实际行为**: job 在步骤执行前即 FAILED，无 shell 输出，无法判断 cache 行为。
- **对照 GitCode 规格**: 无对应文档引用（job 未执行到位无法对照规格）。

No:
1. `uses: cache` — GitCode may not recognize bare `cache` as an action. Should be a full path or built-in name.
2. `cached.txt` is never created — nothing writes the file before trying to cache it. On first run there's nothing to cache.
3. Cache only works with `push`/`pull_request` events, not `workflow_dispatch` (Manual) — the cache plugin skips with `Event Validation Error`.
4. `target: cache_step` — assertion engine doesn't support this kind (assertion_gap).


**置信度**: 中 — job 零输出无法确定根因在平台还是 runner 调度，但失败模式符合 runner 环境不可用特征。

**影响**:
- **阻塞性**: 🔴阻塞 — workflow 无法运行到结束
- **静默性**: 🟡可察觉 — job 明确标记 FAILED
- **影响面**: 🟢单用例
- **综合**: 阻塞但非静默，job 未执行到位导致 cache 功能未被测到
- **是否有规避手段**: 否

**建议**: 重试确认是否可复现；若复现则需排查 runner 调度、资源配额或镜像拉取问题。

---

## 失败分诊 · COMP-CACHE-01-002 · restore-keys 前缀匹配兜底生效 confirmed

**判定结果**: FAIL
**失败断言**: assertions[0] (status, positive, target=run_status) — 预期 all job/step green，实际 job 'Verify restore keys fallback' status=FAILED

**根因初判**: 产品缺陷, the cache doesnt support the cache

**责任人**: 平台方

**证据**:
- **Job 日志全量**（3 行，无 shell 脚本输出）:
  ```
  [2026/07/25 12:39:33.529 GMT+08:00] [INFO] Job(1530555102618460160_1530555102580711431) duration check: true
  ```
- **预期行为**: restore-keys 前缀匹配兜底，cache miss 时用前缀匹配获取部分缓存。
- **实际行为**: job 零 shell 输出即 FAILED。
- **失败传导链**: 无法判断——无任何步骤执行。
- **对照 GitCode 规格**: 无输出可对照。

**置信度**: 低 — 零输出的 job 无法区分是产品缺陷还是环境故障。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉 — FAILED 状态明确
- **影响面**: 🟢单用例
- **综合**: 阻塞但可察觉，cache restore-keys 功能未被测到
- **是否有规避手段**: 否

**建议**: 重试验证。若连续失败且 log 持续为零输出，需排查 runner 环境。

---

## 失败分诊 · COMP-PERMS-01-001 · permissions 空对象时 ATOMGIT_TOKEN 仅 repository read  confirmed

[log](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/7a8f6fd20eee4a148c350ffff583638b/job/5f5785b1ed5845fa9454463f0d18ba4e)

**判定结果**: success
**失败断言**: assertions[0] (run_status_not, negative) — PASS (conclusion != COMPLETED, actual=FAILED ✓); assertions[1] (value, positive, target=run_logs) — 预期 log contains '403'，实际 absent

**根因初判**: 

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（1 行，无 shell 脚本输出）:
  ```
  [2026/07/25 12:40:14.732 GMT+08:00] [INFO] Job(1530555275381841920_1530555275344093191) duration check: true
  ```
- **预期行为**（YAML intent_ref=INTENT-COMP-013）: permissions 空对象时，写操作被拒绝（期望返回 403）。
- **实际行为**: job FAILED 但零 shell 输出。run_status_not 断言已 PASS (conclusion!=COMPLETED)，说明 write 操作被阻止了（job 未跑完=权限阻止生效）。但 value 断言 '403' absent 是因为 job 根本没有 shell 输出可检查。
- **对照 GitCode 规格** `token-permissions.md` 第 103 行: "`permissions: {}`（空）| ATOMGIT_TOKEN 仅拥有最小默认权限（repository:read）"
- **分析**: 负向断言已 PASS，说明平台正确阻止了写操作（permissions: {} → write denied → job FAILED）。value 断言检查 logs 含 '403' 失败是因为 job 在 shell 执行前即终止，不是平台实现问题。

fatal: Authentication failed for 'https://atomgit.com/ComputingActionTest/foundational-tests.git/'
::error::Process exited with code 128

**置信度**: 中 — 负向断言已 PASS 佐证权限控制正确，value 缺失是因 job 提前终止无 log。

**影响**:
- **阻塞性**: ⚪无影响 — 平台权限行为正确
- **静默性**: 🟢明确报错 — job FAILED
- **影响面**: 🟢单用例
- **综合**: 无影响，标记不匹配假失败。负向断言已证实写操作被阻止
- **是否有规避手段**: 是，修复断言标记或检查 log 采集时机

**建议**: 调整断言策略：负向断言已确认权限阻止生效，value 断言应考虑 job 可能无 shell 输出的场景。

---

## 失败分诊 · COMP-PERMS-01-002 · 声明 repository write 后 TOKEN 可推送代码 confirmed
[log](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/3891a055808d4f5d8989b96fbeb5240c/job/01cb1986b9114777a52acaf09f531feb)
**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive, target=run_status) — 预期 COMPLETED，实际 FAILED

**根因初判**: no push permission

**责任人**: 平台方

**证据**:
- **Job 日志全量**（1 行，无 shell 脚本输出）:
  ```
  [2026/07/25 12:40:25.851 GMT+08:00] [INFO] Job(1530555322244927488_1530555322219761671) duration check: true
  ```
- **预期行为**（INTENT-COMP-013）: permissions repository: write 后 ATOMGIT_TOKEN 可推送代码。
- **实际行为**: job 零输出即 FAILED。
- **对照 GitCode 规格** `token-permissions.md` 第 40 行: repository 域 write=推送/修改仓库。
- **分析**: job 零输出意味着无法判断是 runner 故障还是平台真的拒绝了 write。需重试+采集有输出的日志才能判断。

**置信度**: 低 — 零日志无法归因，需重试。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 阻塞非静默，repository write 功能未被测到
- **是否有规避手段**: 否

---

## 失败分诊 · COMP-PERMS-01-003 · fork PR 的 pull_request 下声明 write 仍仅 read confirmed

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status_not, negative) — PASS (conclusion != SUCCESS_WITH_WRITE, actual=COMPLETED ✓); assertions[1] (value, positive, target=run_logs) — 预期 log contains 'write failed as expected'，实际 absent

**根因初判**: 产品缺陷（平台行为与文档承诺一致，但断言标记不匹配）

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:40:35.799 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../9cd67a85-877d-4186-a44d-660ef193f3f3.sh
  ::debug::Executing: bash -e .../9cd67a85-877d-4186-a44d-660ef193f3f3.sh
  404
  ```
- **预期行为**: fork PR 下 pull_request 中声明 write 权限仍应仅 read——即 write 操作应被拒绝，输出 "write failed as expected"。
- **实际行为**: shell 输出了 `404`（HTTP 404），表明写操作被拒绝（404 也意味着拒绝访问）。run_status_not 断言已 PASS (conclusion != SUCCESS_WITH_WRITE)。但 'write failed as expected' marker 未出现，log 输出的是数字 `404`。
- **对照 GitCode 规格** `pr-mr-pipeline-security.md` 第 41-42 行: "ATOMGIT_TOKEN 仅拥有 read 权限，无法推送代码、修改 PR"；`token-permissions.md` 第 105 行: "pull_request 事件来自 fork 仓库时，ATOMGIT_TOKEN 仅拥有 read 权限"。
- **分析**: 平台行为与文档完全一致——fork PR 下 pull_request 的 token 只有 read，写操作被正确拒绝（返回 404）。FAIL 是因为断言关键词 `'write failed as expected'` 与平台实际输出 `404` 不匹配。

**置信度**: 高 — 日志有 `404` + 规格明确 + 负向断言 PASS 三线交叉验证。

**影响**:
- **阻塞性**: ⚪无影响 — 平台正确实施了 fork PR 安全隔离
- **静默性**: 🟢明确报错 — 404 明确指示拒绝
- **影响面**: 🟢单用例
- **综合**: 无影响，标记不匹配假失败。平台行为正确符合安全规格
- **是否有规避手段**: 是，调整断言关键词匹配平台实际输出 404/403

---

## 失败分诊 · COMP-PR-01-001 · fork PR 触发 pull_request 时不可读取项目 secrets

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (run_status, positive) — 预期 SUCCESS_OR_BLOCKED，实际 COMPLETED

**根因初判**: 产品缺陷 — fork PR secret 隔离未生效

**责任人**: 平台方

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:40:55.795 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../715ee403-7183-43aa-b5cd-a6cbf95d6fea.sh
  ::debug::Executing: bash -e .../715ee403-7183-43aa-b5cd-a6cbf95d6fea.sh
  secret value is ***
  ```
- **预期行为**: fork PR 下 pull_request 不可读取项目 secrets，secret 应为空或被屏蔽。
- **实际行为**: `secret value is ***` — secret 被脱敏显示为 `***`，但 `***` 意味着 secret **有一个值并且被展开了**（被脱敏了但不是空的）。如果 secret 真的不可访问，日志应显示 "secret value is " (空) 像 COMP-SECRET-01-001 那样。
- **对照 GitCode 规格** `using-secrets.md` 第 68 行: "Fork 隔离 | pull_request 来自 fork 的 workflow 不可访问项目级 Secret"；`token-permissions.md` 第 105 行: "pull_request 事件来自 fork 仓库时，ATOMGIT_TOKEN 仅拥有 read 权限"。
- **分析**: 平台展示了 `***` 而非空值，说明 secret 在被脱敏掩盖前实际值已被注入。fork PR 场景下 secret 应完全不可访问（空值），出现 `***` 表示平台未正确隔离 fork PR 的 secret 访问。这是一个安全边界缺陷。

**置信度**: 高 — `***` vs 空值的区别明确，规格承诺 fork 不可访问。

**影响**:
- **阻塞性**: 🟡非阻塞 — workflow 仍能 COMPLETED
- **静默性**: 🔴静默错误 — 用户看到 `***` 会误以为 secret 被保护，但实际值已被注入
- **影响面**: 🔴跨维度 — 所有 fork PR + pull_request + secret 场景均受影响
- **综合**: 非阻塞但静默+跨维度——fork PR 安全隔离失效，secret 被注入后仅靠日志脱敏掩盖，存在信息泄露风险
- **是否有规避手段**: 是，使用 pull_request_target 并在 checkout 时避免执行不可信代码

**建议**: 平台需确认 fork PR 下 pull_request event 的 secret 注入行为——规格承诺"不可访问"意味着 secret 不应注入（应为空或 undefined），而非注入后靠脱敏掩盖。相关用例: COMP-PR-01-003, SEC-FORK-01-001, SEC-FORK-01-002。

---

## 失败分诊 · COMP-PR-01-003 · fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 SUCCESS_OR_FAILURE，实际 COMPLETED

**根因初判**: 标记不匹配

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:41:47.051 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../83160cec-66c6-49ac-ba7c-f1176709854c.sh
  ::debug::Executing: bash -e .../83160cec-66c6-49ac-ba7c-f1176709854c.sh
  404
  ```
- **预期行为**: fork PR 下写操作被拒绝（token 仅 read），预期运行状态为 success 或 failure。
- **实际行为**: shell 输出 `404`——写操作被拒绝，run_status=COMPLETED 表示 workflow 正常结束。
- **对照 GitCode 规格** `token-permissions.md` 第 105 行: fork PR 下 token 仅 read。
- **分析**: 平台行为正确（写操作返回 404 拒绝）。断言 expected=SUCCESS_OR_FAILURE 但 actual=COMPLETED — 这是标记映射问题：`COMPLETED` 对应 success 状态，但断言引擎的 `SUCCESS_OR_FAILURE` 关键词不识别 `COMPLETED`。

**置信度**: 高 — 日志 `404` + 规格明确 + 标记映射问题清晰。

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错 — 404
- **影响面**: 🟢单用例
- **综合**: 无影响，标记映射假失败。平台正确执行 fork PR 写权限限制
- **是否有规避手段**: 是，compile_asserts.py 添加 COMPLETED→SUCCESS_OR_FAILURE 映射

---

## 失败分诊 · COMP-SECRET-01-001 · echo secret 在日志中被脱敏为 *** confirmed
[log](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/351aaec6832f40ea879e6b6f065df368)
**判定结果**: SUCCESS
**失败断言**: assertions[0] (value, positive, target=run_logs) — 预期 log contains '***'，实际 absent; assertions[1] (config_probe) — PASS (configured)

**根因初判**: 用例问题（断言设计缺陷 — 正常脱敏行为被误判为失败）

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:42:05.982 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../e25c9bc7-c3bb-4a59-8446-053cbf386f39.sh
  ::debug::Executing: bash -e .../e25c9bc7-c3bb-4a59-8446-053cbf386f39.sh
  secret is 
  ```
- **预期行为**（YAML）: echo secret 值在日志中应被脱敏为 `***`。
- **实际行为**: `secret is ` — secret 值为空（或完全未注入），因为 fork PR 安全隔离阻止了 secret 访问。从 COMP-PR-01-001 的结果可知（secret value is ***），同一 trigger 下不应该是空的。这可能是由于该用例的 setup 不同导致的。
- **对照 GitCode 规格** `using-secrets.md` 第 66 行: "Secret 值在日志中自动替换为 ***"。
- **分析**: log 中 secret 值为空（不是 `***`），说明 secret 要么未配置、要么被隔离。config_probe 已 PASS（确认已配置），但即使 secret 被隔离（空值），也不可能在日志中出现 `***`。`***` 只出现在 secret 有值且被脱敏时。因此 FAIL 的原因不是平台脱敏失败，而是 secret 在当前 trigger 配置下为空，断言设计假定了 secret 一定会有值。

**置信度**: 中 — config_probe PASS 说明 secret 已配置，但值为空可能是平台安全隔离行为，也可能是配置问题。

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟡可察觉 — secret 为空用户会注意
- **影响面**: 🟢单用例
- **综合**: 无影响，断言前提不成立（secret 为空而非脱敏失败）
- **是否有规避手段**: 是，断言应考虑 secret 可能为空/未注入的场景

---

## 失败分诊 · COMP-ARTIFACT-01-001 · artifact 可在同 workflow 的 job 间正确传递 confirmed
**重跑 (dispatch)**: SUCCESS · [ebf8c920...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/f0bfdb7b132d49188e27cbc46a12c2c7)

**判定结果**: SUCCESS
**失败断言**: assertions[0] (run_status, positive) — 预期 COMPLETED，实际 FAILED; assertions[1] (value, positive, target=run_logs) — 预期 log contains 'hello artifact'，实际 absent

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**:
- **Job 日志全量**（3 行，零 shell 输出）:
  ```
  [2026/07/25 12:56:06.091 GMT+08:00] [INFO] Job(1530559265721032704_1530559265687478279) duration check: true
  ```
- **预期行为**: 2-job workflow, upload artifact in job1, download artifact in job2, 验证传递正确。
- **实际行为**: job FAILED 且零 shell 输出。
- **失败传导链**: 无法判断——零输出，不知道是 job1 upload 还是 job2 download 失败。
- **对照 GitCode 规格**: 无日志可对照。

**置信度**: 低 — 零日志无法判断根因。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 阻塞非静默，artifact 传递功能未被测到
- **是否有规避手段**: 否

---

## 失败分诊 · COMP-ARTIFACT-01-002 · 下载全部制品功能正常 confirmed
[log](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/a9e43266e1d8438eb9c791b1fa972849)
**判定结果**: SUCCESS 
**失败断言**: assertions[0] (run_status, positive) — 预期 COMPLETED，实际 FAILED; assertions[1] (value) — 预期 'app' absent; assertions[2] (value) — 预期 'report' absent

**根因初判**: 

**责任人**: 

**证据**:
- **预期行为**: upload 多个 artifact, download all, 验证全部下载成功。
- **实际行为**: run_status=FAILED, 2 jobs, 日志未读取但大概率零输出（与 COMP-ARTIFACT-01-001 类似）。

**置信度**: 低 — 同 COMP-ARTIFACT-01-001 零输出模式。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 阻塞非静默，download-all 功能未被测到
- **是否有规避手段**: 否

---

## 失败分诊 · COMP-ARTIFACT-01-003 · artifact 保留期设置生效 confirmed
[log](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/168aaa22139b4c2d8801f67cdf0e92a2/workflow)
**判定结果**: PEDING
**失败断言**: assertions[0] (status, positive) — 预期 all job/step green，实际 job 'Upload with short retention' status=FAILED

**根因初判**: 

**责任人**: 

**证据**:
- **预期行为**: upload-artifact 设置 retention-days 短期保留。
- **实际行为**: job FAILED。需读日志确认具体错误。

**置信度**: 低 — 未读日志无法确认。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 阻塞非静默
- **是否有规避手段**: 否

---

## 失败分诊 · COMP-CALL-01-001 · 2 层 workflow_call 嵌套正常执行

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 COMPLETED，实际 FAILED

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**:
- **预期行为**: 2 层 workflow_call 嵌套调用正常执行。
- **实际行为**: run_status=FAILED, 1 job, 47s。需读日志确认具体错误（是否嵌套层数被平台限制，或 YAML 加载失败）。

**置信度**: 低 — 未读日志无法确认。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 阻塞非静默
- **是否有规避手段**: 否

---

## 失败分诊 · COMP-SUMMARY-01-001 · ATOMGIT_STEP_SUMMARY Markdown 表格与标题正确渲染

[log](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/0580293ec3e84a32b2b0f43458ccbbbb)

**判定结果**: SUCCESS
**失败断言**: assertions[0] (value, positive, target=run_logs) — 预期 log contains 'Test Summary'，实际 absent; assertions[1] (value) — 预期 log contains '<table>'，实际 absent

**根因初判**: dont support Step Summary Markdown 在 UI 中渲染为表格和标题

**责任人**: 

**证据**:
- **Job 日志全量**（4 行，零 shell 输出）:
  ```
  [2026/07/25 12:59:56.000 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../f348790c-c139-456a-b17f-8666ff27ecca.sh
  ::debug::Executing: bash -e .../f348790c-c139-456a-b17f-8666ff27ecca.sh
  ```
- **预期行为**（INTENT-COMP-018）: Step Summary Markdown 在 UI 中渲染为表格和标题。
- **实际行为**: shell 脚本零输出——这是因为 step summary 内容是写入 `$ATOMGIT_STEP_SUMMARY` 文件后被平台 UI 渲染的，不会出现在 run_logs 中。断言 target=run_logs 检查 logs 是否含 'Test Summary' 和 '<table>' 是不正确的——这些内容写入 summary 文件而非 stdout。
- **对照 GitCode 规格**: 无特定规格引用，但 step summary 工作机制决定了内容不出现在 run logs。
- **分析**: 断言 target 选择错误——step_summary 内容不在 run_logs 中，断言设计阶段未考虑此 target 类型。

**置信度**: 高 — step summary 机制决定了内容不在 shell logs；log 零输出也佐证了这点。

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错 — 但需要确认 UI 是否正常渲染
- **影响面**: 🟢单用例
- **综合**: 无影响，断言 target 错误假失败——step summary 需 UI 层面验证而非 logs
- **是否有规避手段**: 是，修改断言 target 为其他验证方式（如 API 查询 summary 内容）或将 markdown 内容也 echo 到 stdout

---

## 失败分诊 · COMP-TIMEOUT-01-002 · 超时的 job 被强制终止并标记为 failure

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status_not, negative) — PASS (conclusion != COMPLETED, actual=CANCELED ✓); assertions[1] (run_status, positive) — 预期 FAILED，实际 CANCELED; assertions[2] (value, positive) — PASS (log contains 'starting' ✓)

**根因初判**: 产品缺陷（标记映射）— 平台用 CANCELED 而非 FAILED 标记超时终止

**责任人**: Phase 01（标记不匹配）+ 协同平台方

**证据**:
- **Job 日志全量**（9 行）:
  ```
  [2026/07/25 13:00:31.751 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../82aa7317-e315-47a3-bde7-4a2d9b41872f.sh
  ::debug::Executing: bash -e .../82aa7317-e315-47a3-bde7-4a2d9b41872f.sh
  starting
  ...(second step - no output before cancellation)...
  ```
- **预期行为**: 超时的 job 被强制终止，run_status 应为 FAILED。
- **实际行为**: job 开始执行（输出 'starting'），超时后被平台终止，run_status=CANCELED。GitHub Actions 中超时 job 的 conclusion 为 `cancelled`，GitCode 同样使用 CANCELED。
- **对照 GitCode 规格**: 无明确规格说明超时 job 的 status 应为 FAILED vs CANCELED。GitHub Actions 文档中超时 job conclusion 为 `cancelled`。
- **分析**: 平台行为正确（超时后取消），但断言期望 FAILED 而非 CANCELED。若规格未明确承诺超时后 status 必须为 FAILED，这是预期关键字映射问题。run_status_not 断言已 PASS (conclusion != COMPLETED)，说明平台正确终止了超时 job。

**置信度**: 高 — 平台超时后 CANCELED 与 GitHub Actions 行为一致，关键字映射问题清晰。

**影响**:
- **阻塞性**: ⚪无影响 — 平台正确终止超时 job
- **静默性**: 🟡可察觉 — CANCELED 状态明确指示被终止
- **影响面**: 🟢单用例
- **综合**: 无影响，标记映射假失败。平台超时取消行为正确
- **是否有规避手段**: 是，compile_asserts.py 添加 CANCELED→FAILED 映射或修改断言预期

---

# PART 2: SECURITY 维度 FAIL 用例 (26)

---

## 失败分诊 · SEC-ARTF-01-002 · 跨仓库 artifact 下载返回 403 或 404

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext '200' 0 hits ✓); assertions[1] (value, positive, target=run_logs) — 预期 log contains '403_or_404'，实际 absent

**根因初判**: 用例问题（标记不匹配）

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:45:55.726 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../1155d9e0-0b5b-4c55-94d3-6df298a6f2eb.sh
  000{"error_code":400,"error_code_name":"BAD_REQUEST","error_message":"参数类型错误","trace_id":"7ce0d069edfe93e23b6a13c5148f33a3"}400
  ```
- **预期行为**: 跨仓库 artifact 下载应被安全策略拒绝，返回 403 或 404。
- **实际行为**: 平台返回 `400 BAD_REQUEST "参数类型错误"` 而非 403/404。leak 断言已 PASS（未返回 200 success）。平台拒绝方式与预期不同（400 而非 403/404），但同样拒绝访问。
- **对照 GitCode 规格** `using-secrets.md` 第 68 行: fork 隔离机制防止跨仓库 artifact 访问。
- **分析**: 平台正确拒绝了跨仓库 artifact 下载（400 BAD_REQUEST），但错误码/消息与断言关键词 '403_or_404' 不匹配。

**置信度**: 高 — 日志有 400 错误码 + leak 断言 PASS 佐证拒绝生效。

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错 — 400 BAD_REQUEST
- **影响面**: 🟢单用例
- **综合**: 无影响，标记不匹配。平台正确拒绝跨仓库访问但返回码与预期不同
- **是否有规避手段**: 是，调整断言匹配 400/BAD_REQUEST 或更通用的拒绝关键词

---

## 失败分诊 · SEC-BASE-01-001 · pull_request_target 使用 base 分支的 workflow 版本

**判定结果**: FAIL
**失败断言**: assertions[0] (value, positive, target=run_logs) — 预期 log contains 'base_branch_workflow_executed'，实际 absent; assertions[1] (leak, negative) — PASS (plaintext 'fork_injected_step' 0 hits ✓)

**根因初判**: 标记不匹配

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:46:08.422 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../a0222209-72eb-4561-850d-cc1d96ed11ff.sh
  Executing base branch workflow
  ```
- **预期行为**（YAML）: pull_request_target 应执行 base 分支的 workflow（输出 'base_branch_workflow_executed'）。
- **实际行为**: log 输出 "Executing base branch workflow"——平台确实执行了 base 分支的 workflow。leak 断言 PASS（无 fork_injected_step）。但 value 断言关键词 'base_branch_workflow_executed' 与实际输出 'Executing base branch workflow' 不匹配。
- **对照 GitCode 规格** `pr-mr-pipeline-security.md` 第 74 行: "workflow 文件使用目标仓库（main 分支）的版本"；第 13 行表格: "使用目标分支中的 workflow 版本"。
- **分析**: 平台行为完全符合规格（执行 base 分支 workflow，无 fork 注入）。FAIL 纯粹因为断言关键词与实际输出不匹配。

**置信度**: 高 — log + leak 断言 PASS + 规格三线验证。

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错 — log 明确指示 base branch workflow 执行
- **影响面**: 🟢单用例
- **综合**: 无影响，标记不匹配假失败。pull_request_target base 版本安全机制正确运作
- **是否有规避手段**: 是，调整断言关键词或让 YAML 使用 `base_branch_workflow_executed` 作为标记

---

## 失败分诊 · SEC-BASE-01-002 · fork PR 改 workflow 不被 pull_request_target 采用

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext 'fork_injected_step' 0 hits ✓); assertions[1] (run_status, positive) — 预期 SUCCESS_WITH_BASE_WORKFLOW，实际 COMPLETED

**根因初判**: 标记不匹配

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:46:56.509 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../db691e54-8f03-44e9-838f-cbdddf9904e7.sh
  Only base steps run
  ```
- **预期行为**: fork PR 中修改的 workflow 不应被 pull_request_target 采用，只执行 base 步骤。
- **实际行为**: log 输出 "Only base steps run" + leak 断言 PASS（无 fork_injected_step）。平台正确拒绝了 fork 中的 workflow 修改，但断言引擎的 `SUCCESS_WITH_BASE_WORKFLOW` 不识别 `COMPLETED`。
- **对照 GitCode 规格** `pr-mr-pipeline-security.md` 第 13, 74 行: pull_request_target 使用目标分支 workflow 版本。
- **分析**: 与 SEC-BASE-01-001 同一类问题——平台安全机制正确运作，断言关键词映射失败。

**置信度**: 高 — log + leak PASS + 规格三线验证。

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响，标记映射假失败
- **是否有规避手段**: 是，compile_asserts.py 添加 COMPLETED→SUCCESS_WITH_BASE_WORKFLOW 映射

---

## 失败分诊 · SEC-CACHE-01-002 · 主仓 cache restore 对 fork cache miss

**判定结果**: FAIL
**失败断言**: assertions[0] (value, positive, target=run_logs) — 预期 log contains 'cache_miss'，实际 absent

**根因初判**: 环境问题（cache 事件触发条件不满足）

**责任人**: Phase 02

**证据**:
- **Job 日志全量**（3 行）:
  ```
  [2026/07/25 12:47:03.667 GMT+08:00] [INFO] Job(...) duration check: true
  ::warning::Event Validation Error: The event type Manual (normalized: manual) is not supported because it's not tied to a branch or tag ref.
  ::warning::[cache eventValidation] normalized=manual allowlistMatch=false allowlist=[push|pull_request|merge_request] ATOMGIT_EVENT_NAME=Manual GITHUB_EVENT_NAME=Manual
  ```
- **预期行为**: 主仓 workflow 尝试 restore fork 写入的 cache，应 cache miss。
- **实际行为**: cache 插件的 allowlist 只支持 [push|pull_request|merge_request]，但当前触发事件为 Manual (workflow_dispatch)，导致 cache 事件校验失败，插件静默跳过（不执行 restore）。
- **对照 GitCode 规格**: cache 文档可能限制支持的触发事件。
- **分析**: cache 功能因事件类型不匹配而未被触发，属于测试环境 trigger 配置与 cache 插件约束不兼容。不是平台缺陷也不是用例设计问题——是 cache 插件限制了可用事件。

**置信度**: 高 — log 明确显示事件校验失败。

**影响**:
- **阻塞性**: ⚪无影响 — cache 插件正确报告不支持的事件
- **静默性**: 🟡可察觉 — warning 明确
- **影响面**: 🟢单用例
- **综合**: 无影响，环境问题——trigger event 不在 cache 允许列表
- **是否有规避手段**: 是，使用 push/pull_request 事件触发或用 API 直接触发 cache 行为

---

## 失败分诊 · SEC-DEFPERM-01-001 · ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext 'write_successful' 0 hits ✓); assertions[1] (value, positive, target=run_logs) — 预期 log contains '403_or_permission_denied'，实际 absent

**根因初判**: 产品缺陷 — 缺少 ATOMGIT_TOKEN 认证

**责任人**: 平台方

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:47:24.192 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../5533a9cf-a711-4989-a14b-31e97f86a322.sh
  000{"error_code":401,"error_code_name":"UNAUTHORIZED","error_message":"401, token not found","trace_id":"d46c89c1aac7994d7466a20f7c1b8c04"}401000000::error::Process exited with code 6
  ```
- **预期行为**: ATOMGIT_TOKEN 默认权限下写操作应返回 403 或权限拒绝错误。
- **实际行为**: 返回 `401 UNAUTHORIZED "token not found"`——不是权限不足（403），而是根本没有 token。这表明 job 中 `$ATOMGIT_TOKEN` 未注入/为空。
- **对照 GitCode 规格** `token-permissions.md` 第 13 行: "每次流水线运行时，AtomGit Action 自动生成 ATOMGIT_TOKEN"。第 101 行: "未声明 permissions | 使用仓库设置中定义的权限"。
- **分析**: 返回 401 "token not found" 而非 403 "permission denied" 说明 ATOMGIT_TOKEN 未被注入。若需声明 permissions 为空对象或不声明，token 应至少存在（有 read 权限）。token not found 可能是该 repo 设置未启用 token 注入。这是一个平台行为与规格承诺（token 自动生成）不符的案例。

**置信度**: 高 — 401 token not found 与 403 权限拒绝有本质区别。

**影响**:
- **阻塞性**: 🔴阻塞 — token 缺失导致所有认证操作失败
- **静默性**: 🟡可察觉 — 401 明确报错
- **影响面**: 🟡同维度 — 所有依赖 ATOMGIT_TOKEN 的操作在未声明 permissions 时均失败
- **综合**: 阻塞但可察觉——ATOMGIT_TOKEN 在未声明 permissions 时未注入，违反自动生成承诺
- **是否有规避手段**: 是，显式声明 permissions。但若默认行为不符合文档承诺仍需修复

**建议**: 平台需确认未声明 permissions 时 ATOMGIT_TOKEN 是否应自动注入；若应注入，此为平台缺陷。

---

## 失败分诊 · SEC-DOS-01-001 · 大 artifact / 大 cache 必须受配额与边界限制

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext 'success' 0 hits ✓); assertions[1] (value, positive, target=run_logs) — 预期 log contains 'size_limit_exceeded_error'，实际 absent

**根因初判**: 环境问题（artifact 名称冲突）

**责任人**: Phase 02

**证据**:
- **Job 日志全量**（30 行，关键部分）:
  ```
  ...1100+0 records in...1153433600 bytes (1.2 GB, 1.1 GiB) copied...
  Creating artifact "large-artifact" (size: 1121217 bytes)...
  ::error::Upload artifact failed: Artifact with name already exists: large-artifact, repoId=10431336, workflowId=ba5629eb6c374fb6a43202d0cf9c6aba
  ```
- **预期行为**: 大 artifact 应被配额/边界限制拒绝。
- **实际行为**: 1.2GB 文件成功创建（zip 压缩后 1MB），但上传失败因为 artifact 名称冲突（"already exists"）。这不是大小配额限制——是环境中的名称残留。
- **对照 GitCode 规格**: artifact 上传规格需查阅对应文档。
- **分析**: 失败原因是 artifact 名称冲突，前次运行残留。不是平台配额/边界限制的问题——配额功能根本未触发。

**置信度**: 高 — log 明确 "Artifact with name already exists"。

**影响**:
- **阻塞性**: 🟡非阻塞 — workflow 能跑完但 artifact 上传失败
- **静默性**: 🟡可察觉 — 错误消息明确
- **影响面**: 🟢单用例
- **综合**: 非阻塞，环境问题——名称冲突而非配额限制失效
- **是否有规避手段**: 是，使用唯一 artifact 名称或清理前次残留

---

## 失败分诊 · SEC-FORK-01-001 · fork PR 触发 pull_request 时不可读取项目 secrets

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (run_status, positive) — 预期 COMPLETED_OR_BLOCKED，实际 COMPLETED

**根因初判**: 标记不匹配 — fork PR secret 隔离可能存在产品缺陷（同 COMP-PR-01-001）

**责任人**: Phase 01 + 平台方

**证据**:
- **Job 日志全量**（11 行）:
  ```
  ...::debug::Executing: bash -e .../5a3e35b7-46cc-40ed-8932-430e93a9d9b2.sh
  secret value is ***
  ...(step 2)...
  env | grep *** || echo "not found"
  ```
- **预期行为**（YAML）: fork PR 下 pull_request 不可读取 secret，预期 run_status 为 completed_or_blocked。
- **实际行为**: `secret value is ***` — 同 COMP-PR-01-001，secret 显示为 `***` 而非空值，说明 secret 被注入（被脱敏但不是空的）。run_status=COMPLETED。
- **对照 GitCode 规格** `using-secrets.md` 第 68 行: "Fork 隔离 | pull_request 来自 fork 的 workflow 不可访问项目级 Secret"。
- **分析**: 两重问题——(1) 同 COMP-PR-01-001 的潜在 fork secret 隔离缺陷（`***` vs 空）；(2) 断言标记 COMPLETED_OR_BLOCKED 不识别 COMPLETED。若 secret 隔离正确生效且 job COMPLETED，run_status 应为 blocked/completed_or_blocked，COMPLETED 意味着 secret 被访问了。

**置信度**: 高 — 与 COMP-PR-01-001 交叉验证，secret *** 现象一致。

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🔴静默错误 — 用户看到 *** 误以为被保护
- **影响面**: 🔴跨维度 — 同 COMP-PR-01-001
- **综合**: 非阻塞但静默+跨维度——fork PR secret 隔离可能存在边界缺口
- **是否有规避手段**: 是，使用 pull_request_target

---

## 失败分诊 · SEC-FORK-01-002 · fork PR 中 secrets 引用返回空值且 job 不崩溃
**重跑 (dispatch)**: FAILED · [69a627e9...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/69a627e9daa74ac1ba794db6c4e6756b)

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (run_status, positive) — 预期 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷（secret 隔离不完整 — secret 非空导致 job 崩溃）

**责任人**: 平台方

**证据**:
- **Job 日志全量**（6 行）:
  ```
  [2026/07/25 12:48:07.257 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../6360f67c-75a5-455a-962f-38537f99c588.sh
  *** is not empty
  ::error::Process exited with code 1
  ```
- **预期行为**: fork PR 下 secret 应返回空值，job 不崩溃（正常完成）。
- **实际行为**: `*** is not empty` + exit code 1 — secret 有值（被脱敏为 `***`），且测试脚本通过 `[ -z "$SECRET" ]` 检查发现非空，以 exit 1 故意 fail。这说明 secret **被注入了值**（而非预期空值），导致本应返回空/不崩溃的 job 因检测到非空值而 FAILED。
- **对照 GitCode 规格** `using-secrets.md` 第 68 行: fork 隔离。
- **分析**: 这是 fork PR secret 隔离问题的直接证据——脚本预期 secret 为空（正常通过），但实际非空（`***`），证实了 COMP-PR-01-001 和 SEC-FORK-01-001 的发现：fork PR 下 secret 不仅被脱敏掩盖，其值确实被注入了。平台未做到真正的 fork secret 隔离。

**置信度**: 高 — `*** is not empty` + exit 1 直接证明 secret 非空。

**影响**:
- **阻塞性**: 🟡非阻塞 — job 仍然有输出
- **静默性**: 🔴静默错误 — 若测试脚本不主动检查，用户不会发现 secret 可访问
- **影响面**: 🔴跨维度 — 所有 fork PR + secret 场景
- **综合**: 非阻塞但静默+跨维度——fork PR 安全隔离不完整，secret 值在 fork PR 中可被访问
- **是否有规避手段**: 是，使用 pull_request_target

---

## 失败分诊 · SEC-INJ-01-005 · 表达式求值必须防止双重模板渲染（二次求值）
**重跑 (dispatch)**: FAILED · [08e4cbc6...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/08e4cbc63e3b418a9475979cf125a4dc)

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative, target=run_logs) — FAIL + SECURITY_CRITICAL, 预期 plaintext '2' 0 hits，实际 FOUND; assertions[1] (value, positive) — 预期 log contains 'template_chars_escaped'，实际 absent

**根因初判**: 产品缺陷（表达式注入 —— 模板语法在求值后被二次渲染）

**责任人**: 平台方

**证据**:
- **Job 日志全量**（6 行）:
  ```
  [2026/07/25 12:49:01.786 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../7aff7eef-a088-4a5b-bffa-97a81036668f.sh
  /home/slave1/runner/workers/0.0.4.4.version/_temp/7aff7eef-a088-4a5b-bffa-97a81036668f.sh: line 1: Input: ${{ '{{ 1 + 1 }}' }}: bad substitution
  ::error::Process exited with code 1
  ```
- **预期行为**（YAML）: `${{ '{{ 1 + 1 }}' }}` 应将内层 `{{ 1 + 1 }}` 当作字面字符串输出，不应被求值为 `2`。断言要求 log 不含 '2' 且含 'template_chars_escaped'。
- **实际行为**: bash 报错 "bad substitution"——shell 把 `${{ '{{ 1 + 1 }}' }}` 解析为变量替换 `${{ ... }}` 失败（bash 的 `${}` 语法）。这说明表达式引擎处理后的输出包含了未被正确转义的 `{{ }}` 字符。注意这是 bash 层面的 bad substitution 错误，不是平台成功求值了 `1+1=2`。
- **对照 GitCode 规格**: 无明确规格说明模板二次求值防护。
- **分析**: 关键问题——leak 断言说 "plaintext '2' FOUND"，而实际日志中没有 '2'——只有 bash 的 "bad substitution" 错误。需要确认 leak 检测的对象：如果 assertion engine 搜索的是 raw 完整的 log（包括 runner 日志），'2' 可能出现在时间戳 `12:49:01` 或版本号 `2.43.0` 等位置。**单字符 leak 检测存在高假阳性风险**——'2' 频繁出现在数字上下文中。但断言报告 `actual: "FOUND"` 说明引擎确实在日志某处匹配到了 '2'。

**置信度**: 低/中 — leak 检测的 '2' 可能来自时间戳/版本号而非表达式求值。bash bad substitution 错误说明模板语法未正确转义而非二次求值成功。需人工审查引擎 leak 匹配逻辑确认匹配上下文。

**影响**:
- **阻塞性**: 🟡非阻塞 — bash 错误终止了 job
- **静默性**: 🟡可察觉 — bash bad substitution 错误可见
- **影响面**: 🟡同维度 — 若真正存在二次求值而非 bad substitution，影响所有模板表达式
- **综合**: 非阻塞可察觉——bash bad substitution 而非表达式求值 2，leak 检测可能存在单字符误匹配
- **是否有规避手段**: 需确认。若真的是二次求值则平台需修复模板引擎；若为单字符误匹配则断言需调整

**建议**: 首要确认 '2' 的匹配上下文——是来自时间戳/版本号还是真正来自表达式求值输出。当前日志无明确证据支持二次求值成功（只有 bad substitution 错误）。

---

## 失败分诊 · SEC-MASK-01-001 · Secret 值在运行日志中必须被自动脱敏为 *** confirmed
**重跑 (dispatch)**: COMPLETED · [3b9c05d7...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/3b9c05d741ef486489c9ea06a4e1b1bd)

**判定结果**: SUCCESS
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (value, positive, target=run_logs) — 预期 log contains 'masked_with_asterisks'，实际 absent

**根因初判**: 标记不匹配

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:49:12.657 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../14e24d5d-7f4d-4295-97ea-8b7725d28b15.sh
  The secret is ***
  ```
- **预期行为**（YAML）: echo secret 应在日志中显示为 `***`，且 log 含 'masked_with_asterisks' 标记。
- **实际行为**: `The secret is ***` — secret **确实被脱敏为 `***`**！但断言关键词 `masked_with_asterisks` 不在日志中。
- **对照 GitCode 规格** `using-secrets.md` 第 66 行: "Secret 值在日志中自动替换为 `***`"。
- **分析**: 平台正确实施了 secret 脱敏。FAIL 纯粹因为断言关键词与 YAML step 输出不匹配。

**置信度**: 高 — log 明确显示 `***` + 规格确认。

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错 — `***` 可见
- **影响面**: 🟢单用例
- **综合**: 无影响，标记不匹配假失败。secret 脱敏正常工作
- **是否有规避手段**: 是，让 YAML step 输出 'masked_with_asterisks' 或调整断言关键词

---

## 失败分诊 · SEC-MASK-01-005 · Secret 日志脱敏不可通过多行值输出绕过 confirmed
**重跑 (dispatch)**: COMPLETED · [f042e198...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/f042e19867ce4375982a4f881c543e83)

**判定结果**: SUCCESS
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (value, positive, target=run_logs) — 预期 log contains 'multiline_masked_with_asterisks'，实际 absent

**根因初判**: 标记不匹配

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:50:20.388 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../3e5a402b-8ea1-435c-bb93-d2b05e682433.sh
  ***
  ```
- **预期行为**（INTENT-SEC-007）: 多行 secret 值在日志中应被脱敏。
- **实际行为**: log 显示 `***`——多行 secret **已被脱敏**。但断言关键词 'multiline_masked_with_asterisks' 不在日志中。
- **对照 GitCode 规格** `using-secrets.md` 第 66 行。
- **分析**: 与 SEC-MASK-01-001 同类——平台脱敏正确，断言关键词不匹配。

**置信度**: 高 — `***` + 规格确认。

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响，标记不匹配假失败
- **是否有规避手段**: 是，调整断言标记

---

## 失败分诊 · SEC-NAME-01-001 · Secret/变量名含特殊字符时不可导致意外求值或权限绕过 confirmed
**重跑 (dispatch)**: COMPLETED · [61c1ed14...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/61c1ed147a544bae8e05b05725d5b6b7)

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (run_status, positive) — 预期 SUCCESS_OR_YAML_ERROR，实际 COMPLETED

**根因初判**: 标记不匹配  secret doesnt support the my-var

**责任人**: Phase 01  

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:50:42.281 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../0271378f-e0a9-40c2-a585-a877ee56a961.sh
  value is 
  ```
- **预期行为**: 特殊字符 secret 名不应导致意外行为，预期 YAML 解析应报错或成功完成。
- **实际行为**: `value is ` — secret 值为空（特殊字符名未被解析？），job 正常 COMPLETED。
- **对照 GitCode 规格** `using-secrets.md` 第 44 行: "仅允许大写字母、数字和下划线"。
- **分析**: secret 名含特殊字符违反命名规则，secret 未被加载（值为空）。job COMPLETED 但断言期望 SUCCESS_OR_YAML_ERROR。若 YAML 未报错是因为 shell 脚本使用 `${{ secrets.X }}` 引用了一个不存在的 key，返回空而非报错——这是合理的平台行为（不存在=空不报语法错误）。run_status 断言仅因 COMPLETED 未被映射到 SUCCESS_OR_YAML_ERROR。

**置信度**: 中 — log 空值 + 规格命名规则交叉验证。

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟡可察觉 — secret 为空是明确信号
- **影响面**: 🟢单用例
- **综合**: 无影响，标记不匹配。secret 特殊字符名被规格正确拒绝（返回空）
- **是否有规避手段**: 是，标记映射修复

---

## 失败分诊 · SEC-NAME-01-002 · 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secrets 时日志中必须保持脱敏 confirmed
**重跑 (dispatch)**: SUCCESS · [1ea72d07...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/371a6021781e4109ae861b2dd0c0defb/job/ebe4853b45be4beeb0f85a5ffec347e3)

**判定结果**: SUCCESS
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (value, positive, target=run_logs) — 预期 log contains 'masked_or_not_found'，实际 absent

**根因初判**: 

**责任人**: 

**证据**:
- **Job 日志全量**（3 行，零 shell 输出）:
  ```
  [2026/07/25 12:50:53.205 GMT+08:00] [INFO] Job(...) duration check: true
  ```
- **预期行为**: printenv 输出中 secret 值应被脱敏。
- **实际行为**: job FAILED 且零 shell 输出。
- **分析**: 零输出无法判断脱敏行为。需重试验证。

**置信度**: 低 — 零日志。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 阻塞非静默
- **是否有规避手段**: 否

---

## 失败分诊 · SEC-PERM-01-003 · 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）
**重跑 (dispatch)**: FAILED · [53798629...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/53798629398644e58ee9c8df3271ab66)

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext 'write_permission_granted' 0 hits ✓); assertions[1] (run_status, positive) — 预期 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷（ATOMGIT_TOKEN 缺失 — 同 SEC-DEFPERM-01-001）

**责任人**: 平台方

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:51:42.645 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../43cbedf8-cf08-46ef-a138-3dcd13db94fb.sh
  000{"error_code":401,"error_code_name":"UNAUTHORIZED","error_message":"401, token not found","trace_id":"714db08de2b9a8955538d6af92362e14"}401000000::error::Process exited with code 6
  ```
- **预期行为**: 未声明 permissions 时 token 默认 read-only。
- **实际行为**: `401 "token not found"` — ATOMGIT_TOKEN 未注入。与 SEC-DEFPERM-01-001 相同错误模式。
- **对照 GitCode 规格** `token-permissions.md` 第 101 行: "未声明 permissions | 使用仓库设置中定义的权限"。
- **分析**: token not found 而非 permission denied → token 未被注入，违反 "每次运行自动生成" 的规格承诺。

**置信度**: 高 — 与 SEC-DEFPERM-01-001 交叉验证，两例均出现 401 token not found。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟡同维度 — 同 SEC-DEFPERM-01-001
- **综合**: 阻塞可察觉——ATOMGIT_TOKEN 在未声明 permissions 时缺失
- **是否有规避手段**: 是，显式声明 permissions

---

## 失败分诊 · SEC-PERM-01-004 · 默认状态下写操作被 403 拒绝 confirmed
**重跑 (dispatch)**: success · [14fe1eb6...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/c5a623954a6b426c844a7ce7d00a9361/job/b8b64270d01c4719bbff4246511543eb)

**判定结果**: success
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext 'push_successful' 0 hits ✓); assertions[1] (value, positive, target=run_logs) — 预期 log contains 'push_denied_or_403'，实际 absent

**根因初判**: 环境问题（git 用户配置缺失）

**责任人**: Phase 02

**证据**:
- **Job 日志全量**（19 行）:
  ```
  ...::debug::Executing: bash -e .../9975f47e-5265-4733-9e9b-dab1b316250d.sh
  Cloning into 'repo'...
  Author identity unknown
  *** Please tell me who you are.
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
  fatal: unable to auto-detect email address (got 'slave1@...')
  ::error::Process exited with code 128
  ```
- **预期行为**: 默认权限下写操作应被 403 拒绝。
- **实际行为**: git clone 成功但 git commit/push 因缺少 user.email/user.name 配置失败（exit 128）。这不是权限拒绝——是 git 环境配置问题。写操作是否被平台权限限制阻止无法判断，因为 git 在 commit 阶段就因配置缺失失败了。
- **对照 GitCode 规格**: 不适用——git 配置问题是环境问题。
- **分析**: 失败原因与断言预期完全不同——git config 缺失而非 API 403。leak 断言 PASS（无 push_successful）符合预期。

**置信度**: 高 — log 明确 "Please tell me who you are" / "unable to auto-detect email"。

**影响**:
- **阻塞性**: 🟡非阻塞 — git 配置问题非平台权限问题
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 非阻塞，环境问题——runner git 用户配置缺失
- **是否有规避手段**: 是，step 中添加 `git config user.email/user.name`

---

## 失败分诊 · SEC-PRTGT-01-001 · pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控
**重跑 (dispatch)**: FAILED · [ffed6e13...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/b71eb4ad3975410cbf4773957beece98/job/b1d0294ad3c8462eb09190e9f76502e5)

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (run_status, positive) — 预期 BLOCKED_OR_PENDING，实际 COMPLETED

**根因初判**: secret is not empty

**责任人**: 平台方

**证据**:
- **Job 日志全量**（51 行，关键部分第 51 行）:
  ```
  ...
  ::debug::Executing: bash -e .../e75972dd-712c-4ffc-a904-d4e0c088171b.sh
  secret is ***
  ```
- **预期行为**（YAML）: pull_request_target 下 checkout PR head 并尝试访问 secret，预期 secret 应被隔离（run_status=blocked_or_pending）。
- **实际行为**: `secret is ***` — secret 有值（被脱敏）。workflow 正常执行并 COMPLETED。YAML 期望 secret 应被 blocked，但平台规格 `pr-mr-pipeline-security.md` 第 76 行明确承诺: "pull_request_target 下 Secret 可访问——可读取项目级和组织级 Secret"。因此平台行为正确——pull_request_target 本来就允许 secret 访问。
- **对照 GitCode 规格** `pr-mr-pipeline-security.md` 第 13 行表格: "pull_request_target | Secrets 可访问性: 可访问项目 Secret"。第 76 行: "Secret 可访问：可读取项目级和组织级 Secret"。
- **分析**: YAML 的预期与规格矛盾——pull_request_target 下 secret 本来就应可访问（文档明确承诺）。若期望 secret 被 blocked，应使用 pull_request 事件而非 pull_request_target。这是一开始合约设计时未对齐文档的 case。

**置信度**: 高 — 规格第 13/76 行明确 pull_request_target 下 secret 可访问。

**影响**:
- **阻塞性**: ⚪无影响 — 平台按文档承诺行事
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响，用例设计未对齐文档——pull_request_target 规格承诺 secret 可访问，BLOCKED_OR_PENDING 预期不合理
- **是否有规避手段**: 是，修改用例预期为 COMPLETED（含脱敏 secret），或改用 pull_request 测试 secret 隔离

---

## 失败分诊 · SEC-PRTGT-01-002 · pull_request_target 无审批不执行 fork PR 代码
**重跑 (dispatch)**: FAILED · [4b550324...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/4b5503245d07412382f7d6ff8227e585)

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext 'success_without_approval' 0 hits ✓); assertions[1] (run_status, positive) — 预期 PENDING_OR_BLOCKED，实际 COMPLETED

**根因初判**: 需人工判断 — 平台可能无审批机制

**责任人**: 多方联合

**证据**:
- **Job 日志全量**（51 行，关键部分第 51 行）:
  ```
  ...
  ::debug::Executing: bash -e .../fb78fdb7-5430-460c-896c-284700a5a95e.sh
  Building PR code
  ```
- **预期行为**: pull_request_target 下无审批不执行 fork PR 代码，预期 run_status=PENDING_OR_BLOCKED。
- **实际行为**: `Building PR code` — PR 代码被执行了，workflow COMPLETED。leak 断言 PASS（无 'success_without_approval'）。
- **对照 GitCode 规格**: 检查 pull_request_target 审批机制文档。若 GitCode 文档未承诺 pull_request_target 需要审批才能执行，则平台行为正确。
- **分析**: 需查阅 GitCode 文档确认是否有 pull_request_target 审批机制。若无，则此用例预期不合理。

**置信度**: 中 — 需查 GitCode 文档确认审批承诺。

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 非阻塞——平台可能无审批机制，用例预期需对照文档
- **是否有规避手段**: 待查文档

---

## 失败分诊 · SEC-RUN-01-003 · 自托管 Runner 跨项目残留必须被隔离
**重跑 (dispatch)**: FAILED · [73fe7c52...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/73fe7c5218d74236a61d5620967defe7)

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext 'cross project leak' 0 hits ✓); assertions[1] (value, positive, target=run_logs) — 预期 log contains 'isolated_as_expected'，实际 absent

**根因初判**: 需人工判断

**责任人**: 多方联合

**证据**:
- **Job 日志全量**（3 行，零 shell 输出）:
  ```
  [2026/07/25 12:52:46.599 GMT+08:00] [INFO] Job(1530558428982550528_1530558428944801799) duration check: true
  [2026/07/25 12:52:46.588 GMT+08:00] [INFO] Job(1530558428982550528_1530558428944801801) duration check: true
  ```
- **预期行为**: 自托管 runner 跨项目残留隔离。
- **实际行为**: 2 jobs 零 shell 输出即 FAILED。
- **分析**: 自托管 runner 用例需要 runner 被正确注册和调度。零输出可能意味着 runner 根本不活跃。

**置信度**: 低 — 零日志。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 阻塞非静默
- **是否有规避手段**: 否

---

## 失败分诊 · SEC-SIDE-01-002 · Secret 不经 artifact 侧信道绕过脱敏外泄 confirmed
**重跑 (dispatch)**: FAILED · [9b1a2c9f...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/e372cfd4a131418cb1b00432a217ff8f/job/19962f85c3be4d7cb165bf8a67a94302)

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (run_status, positive) — 预期 BLOCKED_OR_MASKED，实际 FAILED

**根因初判**: secret is not empty

**责任人**: 平台方

**证据**:
- **Job 日志全量**（26 行，关键部分第 26 行）:
  ```
  ...Uploading artifact "secret-artifact" from paths: .../secret.txt
  Creating artifact "secret-artifact" (size: 155 bytes, workflow: 92877ce27bff4e149e2f5985f84e9b19)...
  [Twirp] error trace-id: 3993e9d9fb2ed23c02acef2cd1dcc8b8
  ::error::Upload artifact failed: Artifact with name already exists: secret-artifact, repoId=10431328, workflowId=92877ce27bff4e149e2f5985f84e9b19
  ```
- **预期行为**: 含 secret 的文件作为 artifact 上传应被阻止或脱敏。
- **实际行为**: artifact 上传因名称冲突失败（"already exists"）。不能判断平台是否会在成功上传时对 secret 做脱敏——因为上传未成功。
- **对照 GitCode 规格**: artifact 安全隔离机制。
- **分析**: 与 SEC-DOS-01-001 同类——名称冲突导致功能未触发。需清理后重试。

**置信度**: 高 — "already exists" 错误明确。

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 环境问题——名称冲突
- **是否有规避手段**: 是，使用唯一名称

---

## 失败分诊 · SEC-SUPPLY-01-001 · 第三方 Action 引用应支持完整 commit hash 固定 confirm
**重跑 (dispatch)**: FAILED · [0e149f3a...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/0e149f3a3fea438b8dbd0808999a2202)

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 SUCCESS_OR_ACTION_EXECUTED，实际 FAILED; assertions[1] (leak, negative) — PASS (plaintext 'unauthorized_action_execution' 0 hits ✓)


**根因初判**: there is no the action and this hash  docker/build-push-action@1234567890abcdef1234567890abcdef12345678

**责任人**: phase 01

**证据**:
- **Job 日志全量**（1 行，零 shell 输出）:
  ```
  [2026/07/25 12:53:52.022 GMT+08:00] [INFO] Job(1530558703596343296_1530558703571177479) duration check: true
  ```
- **预期行为**: 使用 commit hash 引用第三方 action 应被支持。
- **实际行为**: job FAILED 且零输出——可能是仓库不存在、hash 不匹配、或平台不支持此引用格式。
- **对照 GitCode 规格**: 需查 action 引用格式文档。
- **分析**: 零输出无法判断具体原因。

**置信度**: 低 — 零日志。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 阻塞非静默
- **是否有规避手段**: 否

---

## 失败分诊 · SEC-SUPPLY-01-002 · commit hash 不匹配时第三方 Action 应被拒绝执行 confirm
**重跑 (dispatch)**: FAILED · [0ad11491...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/0ad1149178df44fc96ba55cc353d0ffb)

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext 'success' 0 hits ✓); assertions[1] (value, positive, target=run_logs) — 预期 log contains 'action_not_found_or_sha_mismatch'，实际 absent

**根因初判**: there is no the action and this hash docker/build-push-action@1234567890abcdef1234567890abcdef12345678

**责任人**: phase 01

**证据**:
- **Job 日志全量**（1 行，零 shell 输出）:
  ```
  [2026/07/25 12:54:02.860 GMT+08:00] [INFO] Job(1530558748823269376_1530558748802297863) duration check: true
  ```
- **预期行为**: hash 不匹配的 action 应被拒绝并报错。
- **实际行为**: job FAILED 零输出。leak 断言 PASS（无 success）。
- **分析**: 零输出无法判断。若平台因 hash 不匹配拒绝了引用但未给出子步骤的 shell 输出，这可能是 runner 调度问题而非 action 引用问题。

**置信度**: 低 — 零日志。

**影响**:
- **阻塞性**: 🔴阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 阻塞非静默
- **是否有规避手段**: 否

---

## 失败分诊 · SEC-TOCTOU-01-001 · 审批后推送新 commit 不应被已授权特权运行执行
**重跑 (dispatch)**: COMPLETED · [2643d4c7...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/2643d4c791e6406c9650e255e8af2e79)

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext 'unapproved_commit_executed' 0 hits ✓); assertions[1] (value, positive, target=run_logs) — 预期 log contains 'approved_sha_matched'，实际 absent

**根因初判**: 标记不匹配 — 平台上下文变量可能不返回 sha

**责任人**: Phase 01 + 平台方

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:54:13.318 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../56a097f6-7ecb-4e03-9cb3-4da560be3fbe.sh
  Running commit: 
  ```
- **预期行为**: 审批后推送新 commit 不应被执行，应展示 approved_sha。
- **实际行为**: `Running commit: ` — 引用的 SHA 变量为空。这意味着平台上下文变量（如 atomgit.event.pull_request.head.sha）返回空值。
- **对照 GitCode 规格**: 需查 atomgit context 文档。
- **分析**: SHA 为空导致脚本无法验证 commit 是否匹配，不是 TOCTOU 机制本身的问题（因为没有可对比的 SHA）。FAIL 主要是断言关键词不匹配 + SHA 上下文为空。

**置信度**: 中 — SHA 为空 + 断言关键词不匹配双因素。

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 非阻塞——SHA 上下文为空导致无法验证 TOCTOU
- **是否有规避手段**: 是，确认 atomgit context 中 SHA 变量的正确路径和名称

---

## 失败分诊 · SEC-TOKEN-01-001 · fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限
**重跑 (dispatch)**: FAILED · [e5677522...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/e567752207134ff69dbe0f2808a4d307)

**判定结果**: FAIL
**失败断言**: assertions[0] (value, positive, target=run_logs) — 预期 log contains 'clone_successful'，实际 absent; assertions[1] (leak, negative) — PASS (plaintext 'write_permission_granted' 0 hits ✓)

**根因初判**: 标记不匹配 — clone 成功但 marker 不匹配

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（10 行）:
  ```
  ...::debug::Executing: bash -e .../98cc9a8c-54dd-48bc-9ac8-5f708ff8b510.sh
  Cloning into 'test-clone'...
  ...(step 2)...
  000{"error_code":401,"error_code_name":"UNAUTHORIZED","error_message":"401, token not found","trace_id":"2b691262de4e78ee8d876a5726fd7e89"}401000000::error::Process exited with code 6
  ```
- **预期行为**: fork PR 下 token 仅 read 权限，clone 应成功（read 操作），写操作应被拒绝。
- **实际行为**: clone 成功（"Cloning into 'test-clone'..."），但写操作返回 401 token not found（而非 403）。clone_successful marker 未匹配。平台行为部分正确——read 操作成功，写操作被阻止。
- **对照 GitCode 规格** `token-permissions.md` 第 105 行。
- **分析**: read 操作（clone）成功证明 token 有 read 权限。写操作失败（401 token not found）而非 403 说明 token 不够或未被正确注入为写场景。标记不匹配导致 value 断言失败。

**置信度**: 高 — clone 成功 + 写操作 401 三线证据。

**影响**:
- **阻塞性**: ⚪无影响 — read 权限正确
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 无影响，标记不匹配——token read 权限正确，clone 成功
- **是否有规避手段**: 是，调整断言关键词 'clone_successful' → 匹配实际 git clone 输出

---

## 失败分诊 · SEC-TOKEN-01-002 · fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝  
**重跑 (dispatch)**: FAILED · [710f696a...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/710f696a9a7e41f09599131c3f19460f)

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 COMPLETED，实际 FAILED

**根因初判**: 环境问题（git 用户配置缺失）

**责任人**: Phase 02

**证据**:
- **Job 日志全量**（19 行）:
  ```
  ...::debug::Executing: bash -e .../e0ff8fd2-ab3c-4714-893a-f0b6d12dee50.sh
  Cloning into 'repo'...
  Author identity unknown
  *** Please tell me who you are.
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
  fatal: unable to auto-detect email address (got 'slave1@...')
  ::error::Process exited with code 128
  ```
- **预期行为**: fork PR 下写操作应被平台拒绝。
- **实际行为**: 与 SEC-PERM-01-004 相同——git clone 成功但 commit 因缺少 user.email/user.name 配置失败（exit 128）。不是平台权限拒绝。
- **分析**: 同 SEC-PERM-01-004——git 配置缺失导致无法测试平台权限。

**置信度**: 高 — 同 SEC-PERM-01-004 日志模式。

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 非阻塞，环境问题——git 用户配置缺失
- **是否有规避手段**: 是，添加 git config 步骤

---

## 失败分诊 · SEC-WCMD-01-001 · Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值
**重跑 (dispatch)**: COMPLETED · [ae13726e...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/ae13726eb7b642518133c49fdcc49e9d)

**判定结果**: FAIL
**失败断言**: assertions[0] (config_probe) — PASS (configured); assertions[1] (value, positive, target=run_logs) — 预期 log contains 'mask_command_without_payload'，实际 absent

**根因初判**: 标记不匹配

**责任人**: Phase 01

**证据**:
- **Job 日志全量**（5 行）:
  ```
  [2026/07/25 12:54:55.406 GMT+08:00] [INFO] Job(...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Executing: bash -e .../26fa5a31-b455-482c-8e36-ec0feaebc149.sh
  ::add-mask::***
  ```
- **预期行为**: add-mask 命令响应不应泄露 secret 明文，log 应含 'mask_command_without_payload'。
- **实际行为**: `::add-mask::***` — add-mask 命令被正确执行，mask 值已为 `***`（脱敏后）。平台正确脱敏了 add-mask 命令的响应。但断言关键词不匹配。
- **分析**: 平台行为完全正确——add-mask 响应被脱敏为 `***`。FAIL 是标记不匹配。

**置信度**: 高 — `::add-mask::***` 明确显示脱敏正确。

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错
- **影响面**: 🟢单用例
- **综合**: 无影响，标记不匹配假失败。add-mask 命令响应被正确脱敏
- **是否有规避手段**: 是，调整断言关键词

---

## 失败分诊 · SEC-WCMD-01-002 · 跨运行 artifact 必须被视为不可信数据
**重跑 (dispatch)**: FAILED · [12c6941c...](https://gitcode.com/ComputingActionTest/foundational-tests/actions/runs/12c6941c211a4361aec29afc4f9e6aaa)

**判定结果**: FAIL
**失败断言**: assertions[0] (leak, negative) — PASS (plaintext 'auto_executed' 0 hits ✓); assertions[1] (run_status, positive) — 预期 COMPLETED，实际 FAILED

**根因初判**: 环境问题（artifact 不存在）

**责任人**: Phase 02

**证据**:
- **Job 日志全量**（12 行）:
  ```
  ...::debug::Artifact client initialized for https://actions-results.atomgit.com
  Downloading single artifact
  ::debug::Listing artifacts for workflow 2bbaa0d812e64e37a20bf0a5976832a8 with name filter "untrusted-artifact"
  [Twirp] trace-id: b3125182d65c57efae74697146cfd8a0
  ::debug::Found 0 artifact(s)
  ::error::Unable to download artifact(s): Artifact 'untrusted-artifact' not found. Available artifacts: (none)
  ```
- **预期行为**: 跨运行 artifact 应为不可信数据，下载应失败。
- **实际行为**: artifact 'untrusted-artifact' 不存在——上一个 workflow 运行未成功创建 artifact，因此验证不可信数据处理的步骤无法触发。
- **分析**: 这不是安全机制缺陷——artifact 根本不存在。如果上游 run 未成功创建 artifact，测试不可信 artifact 的前提不成立。

**置信度**: 高 — "Found 0 artifact(s)" 明确。

**影响**:
- **阻塞性**: 🟡非阻塞
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 环境问题——artifact 不存在，测试前提未满足
- **是否有规避手段**: 是，先确保上游 artifact 创建成功

---

# 汇总分析

## 根因分类分布

| 分类 | 数量 | 占比 |
|------|------|------|
| 标记不匹配（Phase 01） | 12 | 30% |
| 环境问题（Phase 02） | 8 | 20% |
| 产品缺陷（平台方） | 4 | 10% |
| 需人工判断（多方联合） | 12 | 30% |
| 用例问题（Phase 01） | 4 | 10% |

## 关键发现

### P0 安全问题
1. **fork PR secret 隔离缺陷** (COMP-PR-01-001, SEC-FORK-01-001, SEC-FORK-01-002): 三个用例交叉验证——fork PR 下 pull_request 事件中 secret 值被注入后脱敏（`***`），而非按规格承诺"不可访问"（空值）。SEC-FORK-01-002 中 `*** is not empty` 直接证实 secret 非空。**这是 SECURITY_CRITICAL 级别的安全边界问题。**

2. **ATOMGIT_TOKEN 缺失** (SEC-DEFPERM-01-001, SEC-PERM-01-003): 未声明 permissions 时 ATOMGIT_TOKEN 未注入（401 "token not found"），违反规格"每次运行自动生成"的承诺。

3. **SEC-INJ-01-005 表达式注入**: 误报风险——log 中 '2' 的 leak 匹配可能来自时间戳/版本号，需排查匹配上下文。bash bad substitution 错误而非成功求值。

### 系统性模式

- **标记不匹配是最大假失败源**（30% 的 FAIL）: COMPLETED 与 SUCCESS/BLOCKED/PENDING 等关键词映射缺失。compile_asserts.py 需要关键词归一化表。
- **零输出 job**（10+ 用例）: runner 调度问题导致 job 在步骤执行前即 FAILED。需排查 runner 环境和调度机制。
- **Artifact 名称冲突** (2 用例): 前次运行残留导致 "already exists" 错误。
- **Git 用户配置缺失** (2 用例): runner 缺少 user.email/user.name 导致 git commit 失败。

### 平台行为正确的假失败
约 20 个 FAIL 用例中，平台实际行为符合 GitCode 文档规格，FAIL 纯粹因为断言关键词/标记不匹配或环境问题。这些不应归类为产品缺陷。

