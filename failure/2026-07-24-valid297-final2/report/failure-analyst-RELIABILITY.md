# Failure Analyst · RELIABILITY FAIL 归因报告 · run 2026-07-24-valid297-final2

> 共 20 条 RELIABILITY 维度 FAIL 用例，按根因分组归因。

---

## 失败分诊 · REL-ARTCONC-01-063 · 制品并发写一致性——多 job 同时 upload-artifact 同名 artifact

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'artifact concurrent write test' status=FAILED

**根因初判**: 用例问题

**责任人**: Phase 01 — YAML 中 `${{{{ matrix.instance }}}}` 四括号语法错误，`${{ }}` 在合约生成阶段被重复模板渲染

**证据**:

- **Job 日志全量**（24 行，全部 job 实例同一错误）:
  ```
  /home/slave1/runner/workers/...: line 1: ${{{{ matrix.instance }}}: bad substitution
  ::error::Process exited with code 1
  ```
  3 个 matrix 实例（instance=1/2/3）全部因同一 bash 语法错误崩溃。

- **预期行为**（用例 REL-ARTCONC-01-063，P1，维度 reliability）:
  - 操作步骤: 3 个 matrix instance 各生成不同内容（A/B/C），upload-artifact 同名 "concurrent-artifact"
  - 预期结果: download_content ∈ [AAA, BBB, CCC]，且 contains_mixed=false

- **实际行为**:
  - 实际 workflow 脚本中 `${{ matrix.instance }}` 被错误渲染为 `${{{{ matrix.instance }}}}`
  - bash 将 `${{{{` 解析为 bad substitution，exit 1
  - 所有 matrix 实例均崩溃，无一成功执行

- **对照 GitCode 规格** `writing-pipelines/configure-matrix-builds.md`:
  - 第 24-37 行明确文档使用 `${{ matrix.<var> }}` 引用 matrix 变量（如 `${{ matrix.node-version }}`）
  - Phase 01 合约生成阶段将 `${{ }}` 错误 double-render 为 `${{{{ }}}}`

**置信度**: 高 — 日志直接显示 bash `bad substitution` 错误，4 个 `${{{{ }}}}` 用例（REL-ARTCONC-01-063、REL-MATRIX-01-038、REL-MATRIX-01-039、REL-OUTPUT-01-016）均为已知 Phase 01 语法 bug，证据链完整

**影响**:
- **阻塞性**: ⚪无影响 — 平台功能正常，纯用例侧 YAML 语法问题
- **静默性**: 🟢明确报错 — bash `bad substitution` 直接抛出，用户能立即定位
- **影响面**: 🟡同维度 — 所有使用 `${{ }}` 的 matrix/step output 用例均受影响
- **综合**: 无影响——已知 Phase 01 合约生成 double-template 渲染 bug，平台行为正常
- **是否有规避手段**: 是 — Phase 01 修复编译器的 YAML 模板渲染逻辑即可

**建议**:
- Phase 01 修复 `compile_asserts.py` 或 YAML 合约生成器中的模板渲染，确保 `${{ }}` 不被二次渲染
- 相关用例: REL-MATRIX-01-038、REL-MATRIX-01-039、REL-OUTPUT-01-016（同根因）

---

## 失败分诊 · REL-MATRIX-01-038 · 大规模 matrix——20 个组合应全部生成并正确调度

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 COMPLETED，实际 FAILED

**根因初判**: 用例问题

**责任人**: Phase 01 — YAML 中 `${{{{ }}}}` 四括号语法错误

**证据**:

- **Job 日志全量**（168 行，24 个 job 实例全部相同错误）:
  ```
  line 1: os=${{{{ matrix.os }}}: bad substitution
  ::error::Process exited with code 1
  ```
  24 个 matrix 组合（2×2×2×3=24，非声称的 20）全部因 `${{{{ }}}}` 语法错误崩溃。

- **预期行为**（用例 REL-MATRIX-01-038，P1，维度 reliability）:
  - strategy.matrix: os=[ubuntu,euler] × arch=[x64,arm64] × compiler=[gcc,clang] × mode=[debug,release,profile]
  - 预期: generated_jobs_count=20（实际组合数为 2×2×2×3=24，断言数有误），run_status=completed(success)

- **实际行为**:
  - YAML 第 28 行: `echo os=${{{{ matrix.os }}}} arch=${{{{ matrix.arch }}}} ...` — 四括号语法
  - 所有 24 个实例的 bash 脚本均被 `${{{{ }}}}` 语法错误阻塞

- **对照 GitCode 规格** `writing-pipelines/configure-matrix-builds.md`:
  - 第 24-39 行: 矩阵构建示例使用 `${{ matrix.<var> }}` 语法

**置信度**: 高 — 与 REL-ARTCONC-01-063 相同根因，日志证据直接

**影响**:
- **阻塞性**: ⚪无影响
- **静默性**: 🟢明确报错
- **影响面**: 🟡同维度 — 同 batch 4 个用例受影响
- **综合**: 无影响——已知 Phase 01 double-template 渲染 bug
- **是否有规避手段**: 是 — 修复 Phase 01 模板渲染

**建议**:
- 与 REL-ARTCONC-01-063 合并处理

---

## 失败分诊 · REL-MATRIX-01-039 · 大规模 matrix——50 个组合应全部生成并正确调度

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'matrix 50 combos test' status=FAILED

**根因初判**: 用例问题

**责任人**: Phase 01 — YAML 中 `${{{{ }}}}` 四括号语法错误

**证据**:

- **Job 日志全量**（350 行，50 个实例全部相同错误）:
  ```
  line 1: v1=${{{{ matrix.v1 }}}: bad substitution
  ::error::Process exited with code 1
  ```

- **预期行为**（用例 REL-MATRIX-01-039，P1）:
  - strategy.matrix: v1=[a,b,c,d,e] × v2=[1..10] = 50 组合
  - 预期: generated_jobs_count=50，scheduling_latency_seconds ≤ 300

- **实际行为**:
  - YAML 第 26 行: `echo v1=${{{{ matrix.v1 }}}} v2=${{{{ matrix.v2 }}}}` — 四括号语法
  - 50 个实例全部崩溃

- **对照 GitCode 规格** `writing-pipelines/configure-matrix-builds.md`: 第 24-39 行

**置信度**: 高

**影响**: 同 REL-MATRIX-01-038

**建议**: 与 REL-ARTCONC-01-063 合并处理

---

## 失败分诊 · REL-OUTPUT-01-016 · step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'output boundary test' status=FAILED

**根因初判**: 用例问题

**责任人**: Phase 01 — YAML 中 `${{{{ steps.writer.outputs.data }}}}` 四括号语法错误

**证据**:

- **Job 日志全量**（10 行）:
  ```
  line 1: ${{{{ steps.writer.outputs.data }}}: bad substitution
  ::error::Process exited with code 1
  ```

- **预期行为**（用例 REL-OUTPUT-01-016，P1）:
  - 步骤 1: writer 生成 1MB 数据写入 ATOMGIT_OUTPUT
  - 步骤 2: 读取 step output 并验证长度 ≥ 1048576
  - 预期: step_output_length=1048576

- **实际行为**:
  - YAML 第 27-28 行: `${{{{ steps.writer.outputs.data }}}}` — 四括号语法
  - read step 的 bash 脚本在解析阶段即崩溃

- **对照 GitCode 规格** `writing-pipelines/pass-output-between-jobs.md` 和 `configure-jobs.md` 第 139-150 行:
  - 文档承诺 `${{ steps.<id>.outputs.<name> }}` 语法

**置信度**: 高

**影响**: 同 REL-ARTCONC-01-063

**建议**: 与 REL-ARTCONC-01-063 合并处理

---

## 失败分诊 · REL-ART-01-041 · 超大 artifact——100 MB artifact 上传后下游 job 应成功下载

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'upload artifact job' status=FAILED

**根因初判**: 环境问题

**责任人**: Phase 02 — 前次运行 artifact 残留导致名称冲突

**证据**:

- **Job 日志全量**（31 行）:
  ```
  ::error::Upload artifact failed: Artifact with name already exists: perf-artifact, repoId=10431336, workflowId=a44a8dd05f9645c492c9807ee708990f
  ```

- **预期行为**（用例 REL-ART-01-041，P1）:
  - upload job: 生成 100MB 文件，upload-artifact(name=perf-artifact)
  - download job: download-artifact(name=perf-artifact)，验证文件存在
  - 预期: upload_status=success, download_status=success, md5_match=true

- **实际行为**:
  - 100MB 文件生成成功（0.369s），zip 打包成功（~100MB）
  - 上传时 Twirp 报错: "Artifact with name already exists: perf-artifact"
  - 这表明同一 workflow 或同一 repo 的前次运行残留了同名 artifact

- **失败传导链**: upload job FAILED → download job（needs: upload）未执行 → 下游验证全部未测试

- **对照 GitCode 规格** `writing-pipelines/upload-download-artifacts.md`:
  - 第 62 行: "`name` 是 制品名称，同一 workflow 中唯一" — 文档承诺 name 在同一 workflow 中唯一，未提及跨 run 残留问题

**置信度**: 高 — 错误消息直接指明冲突原因

**影响**:
- **阻塞性**: 🔴阻塞 — artifact 上传被拦，pipeline 断裂
- **静默性**: 🟡可察觉 — 平台报错但用户可能不理解为何残留
- **影响面**: 🟡同维度 — 同 batch 4 个 artifact 用例因名称冲突失败
- **综合**: 阻塞——环境残留（前次运行 artifact 未清理）导致上传失败，非平台 artifact 功能缺陷
- **是否有规避手段**: 是 — harness 在 run 前清理残留 artifact，或用例使用 UUID 后缀避免名称冲突

**建议**:
- Phase 02 harness 增加 pre-run cleanup 步骤（删除同名 artifact）
- 相关用例: REL-ARTPERF-01-053、REL-FAULT-01-032、REL-RETAIN-01-047

---

## 失败分诊 · REL-ARTPERF-01-053 · 制品传输性能——100MB artifact 上传下载耗时

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'upload artifact job' status=FAILED

**根因初判**: 环境问题

**责任人**: Phase 02 — 与 REL-ART-01-041 同名 artifact "perf-artifact" 冲突

**证据**:

- **Job 日志全量**（31 行）:
  ```
  ::error::Upload artifact failed: Artifact with name already exists: perf-artifact, repoId=10431338, workflowId=37377f8b2720406ca6780f11c1fe26ed
  ```

- **预期行为**（用例 REL-ARTPERF-01-053，P1）:
  - 100MB artifact 上传/下载，测量耗时
  - 预期: upload_time_seconds ≤ 30, download_time_seconds ≤ 30, hash_match=true

- **实际行为**: 与 REL-ART-01-041 完全相同的名称冲突错误

**置信度**: 高

**影响**: 同 REL-ART-01-041

**建议**: 同 REL-ART-01-041

---

## 失败分诊 · REL-ARTPERF-01-053-V2 · 制品传输性能——1GB artifact 上传下载耗时

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'upload artifact job' status=FAILED

**根因初判**: 环境问题

**责任人**: Phase 02 — Namespace artifact quota 超限

**证据**:

- **Job 日志全量**（55 行）:
  1. 1GB 文件生成成功（3.39s）
  2. zip 压缩完成（~1024MB）
  3. multipart 上传全部 6 个分片成功
  4. 上传完成，SHA-256 校验通过
  5. **最终错误**:
  ```
  ::error::Upload artifact failed: Namespace artifact quota exceeded: namespace=13965860, repoId=10431319, requestedBytes=1074069497, currentUsed=1642723372, max=1073741824
  ```
  - 当前已用 1.64GB，请求 1.07GB，配额上限 1.07GB（1GB）
  - 此次上传前配额已耗尽

- **预期行为**（用例 REL-ARTPERF-01-053-V2，P1）:
  - 1GB artifact 上传/下载，测量耗时
  - 预期: upload_time_seconds ≤ 300, download_time_seconds ≤ 300, hash_match=true

- **实际行为**:
  - 上传机制本身工作正常（6 分片并发、SHA-256 校验均通过）
  - 但在 finalization 阶段被命名空间配额限流拒绝
  - 注意：quota "max=1073741824"（1GB），而 artifact 大小 = 1074069497（~1.07GB）也已超限

- **对照 GitCode 规格** `writing-pipelines/upload-download-artifacts.md`:
  - 文档未明确列出 artifact 大小上限；第 9 行仅提及"已确认制品大小不超过限制"

**置信度**: 中 — 上传功能正常但因配额超限失败，无法区分是环境残留导致的配额耗尽还是平台硬限制

**影响**:
- **阻塞性**: 🔴阻塞 — artifact 上传因 quota 被拒
- **静默性**: 🟡可察觉 — 错误消息明确指出 quota exceeded
- **影响面**: 🟡同维度 — 同一 namespace 下所有 artifact 用例受影响
- **综合**: 阻塞+可察觉——命名空间 artifact 配额耗尽（1GB limit），非 artifact 插件自身缺陷
- **是否有规避手段**: 是 — 清理 namespace 下残留 artifact 释放配额

**建议**:
- Phase 02 harness 增加 pre-run artifact 清理步骤
- 若该配额是平台的硬上限（1GB/namespace），则标记为平台能力边界

---

## 失败分诊 · REL-FAULT-01-032 · 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 FAILED，实际 FAILED（pass）；assertions[1] (value, run_logs) — 预期 log contains 'network'，实际 absent

**根因初判**: 环境问题

**责任人**: Phase 02 — "Artifact with name already exists" 阻断有效测试

**证据**:

- **Job 日志全量**（29 行）:
  ```
  ::error::Upload artifact failed: Artifact with name already exists: net-fault-artifact, repoId=10431335, workflowId=7303592c5f7849e59f49fed684ebb95e
  ```

- **预期行为**（用例 REL-FAULT-01-032，P1）:
  - fault_injection: network_partition 30s，target_step=2
  - 预期: step_status=failure，run_logs 含 'network'

- **实际行为**:
  - artifact 上传因名称冲突在 fault injection 触发前即失败
  - network_partition 故障注入未执行到
  - 因此 run_logs 不含 'network'（value 断言失败）

- **对照 GitCode 规格**: 同上 artifact 规范

**置信度**: 高 — artifact 名称冲突阻断了故障注入测试

**影响**:
- **阻塞性**: 🔴阻塞 — 前置 artifact 冲突导致故障注入测试未执行
- **静默性**: 🟡可察觉 — 错误消息明确
- **影响面**: 🟢单用例 — 仅影响此用例的故障注入路径
- **综合**: 阻塞——artifact 名称冲突导致故障注入测试被跳过
- **是否有规避手段**: 是 — 清理残留 artifact

**建议**: 同 REL-ART-01-041

---

## 失败分诊 · REL-RETAIN-01-047 · artifact 保留期 90 天边界——第 91 天应不可下载

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'artifact retention test' status=FAILED

**根因初判**: 环境问题

**责任人**: Phase 02 — "Artifact with name already exists: retention-artifact"

**证据**:

- **Job 日志全量**（26 行）:
  ```
  ::error::Upload artifact failed: Artifact with name already exists: retention-artifact, repoId=10431336, workflowId=c2b738ae9da948c29bcad64ac9226d5a
  ```

- **预期行为**（用例 REL-RETAIN-01-047，P1）:
  - upload-artifact(name=retention-artifact, retention-days=90)
  - 预期: download_day90_status=200, download_day91_status=404

- **实际行为**: 上传阶段即失败，retention 测试完全未执行

**置信度**: 高

**影响**:
- **阻塞性**: 🔴阻塞 — retention 测试完全未执行
- **静默性**: 🟡可察觉
- **影响面**: 🟢单用例
- **综合**: 阻塞——artifact 名称冲突阻断测试
- **是否有规避手段**: 是 — 清理残留 artifact

**建议**: 同 REL-ART-01-041

---

## 失败分诊 · REL-CONTINUE-01-030 · continue-on-error=true——job 失败后 workflow 不应终止

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 FAILED，实际 COMPLETED

**根因初判**: 标记不匹配

**责任人**: Phase 01 — `compile_asserts.py` 将 YAML `workflow_status=success` 错误映射为 run_status assertion `expected=FAILED`

**证据**:

- **Job 日志全量**（11 行）:
  ```
  [job_a] ::error::Process exited with code 1
  [job_b] job_b executed
  ```

- **预期行为**（用例 REL-CONTINUE-01-030，P1）:
  - job_a: continue-on-error=true，执行 exit 1 → 预期 status=failure
  - job_b: 无 needs 依赖 → 预期 status=success
  - 整体: 预期 workflow_status=success

- **实际行为**:
  - job_a 失败（exit 1），job_b 正常执行（"job_b executed"）
  - workflow 整体状态 COMPLETED（即 success）——**平台行为与 YAML 预期完全一致**
  - 但 assertion_engine 编译出的断言为：run_status expected=FAILED → 与实际 COMPLETED 冲突
  - 这正是 continue-on-error 的正确行为：job 失败但 workflow 不应终止

- **对照 GitCode 规格**:
  - `configure-dependencies-order.md` 第 83 行: "依赖的 job 失败时，当前 job 默认不执行"
  - 但 job_b 没有 `needs: job_a`，所以 continue-on-error 应让 workflow 继续

- **标记根因**:
  - 原始断言 `job_a_status=failure` 和 `workflow_status=success` 语义不同
  - 编译器将 `workflow_status=success` 错误映射为 `run_status FAILED`
  - 实际 workflow 因 continue-on-error=true 而 COMPLETED（正确），但断言期望 FAILED

**置信度**: 高 — 平台行为与 YAML 设计意图一致，FAIL 来源于编译层的 status 词汇映射错误

**影响**:
- **阻塞性**: ⚪无影响 — 平台 continue-on-error 功能正常
- **静默性**: 🟢明确报错 — 断言失败提示清晰
- **影响面**: 🟢单用例
- **综合**: 无影响——测试断言编译层的 status 关键词映射问题，平台功能正常
- **是否有规避手段**: 是 — 修复 compile_asserts.py 中的 positive/negative status 词汇映射

**建议**:
- Phase 01 compile_asserts.py 审查 `workflow_status=success` 到 `run_status expected=FAILED` 的映射逻辑

---

## 失败分诊 · REL-DISK-01-019 · Runner 磁盘越界——small runner 写入 51 GB 应失败并报磁盘满

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 FAILED，实际 COMPLETED；assertions[1] (value, run_logs) — 预期 log contains 'No space left on device'，实际 absent

**根因初判**: 环境问题 / 需人工判断

**责任人**: 多方联合 — runner 环境磁盘充足（94GB available）导致 51GB 写入成功，无法触发磁盘满错误

**证据**:

- **Job 日志全量**（9 行）:
  ```
  expecting failure above
  ```

- **预期行为**（用例 REL-DISK-01-019，P1）:
  - 步骤 1: `fallocate -l 51G testfile || dd if=/dev/zero of=testfile bs=1M count=52224`（continue-on-error: true）
  - 步骤 2: echo "expecting failure above"
  - 预期: job_status=failure, run_logs 含 'No space left on device'

- **实际行为**:
  - 51GB 写入**成功完成**（无任何错误）
  - "expecting failure above" 被输出
  - 从 REL-RUNNER-01-049-V2 日志可知 runner 有 ~94GB 可用磁盘空间
  - 51GB << 94GB available → 写入不会失败

- **对照 GitCode 规格**:
  - `selecting-runner-labels.md` 第 14 行: small runner 规格未明确标注磁盘空间
  - runner 环境实际情况: 94GB available（从 REL-RUNNER-01-049-V2 探针日志确认）

**置信度**: 中 — runner 磁盘空间足够导致磁盘满测试无法触发，但 GitCode 文档未明确承诺 small runner 的磁盘限制

**影响**:
- **阻塞性**: ⚪无影响 — 非平台缺陷，运行环境磁盘充足
- **静默性**: 🟡可察觉 — 测试断言明确报告 "No space left on device" 缺失
- **影响面**: 🟢单用例
- **综合**: 无影响——small runner 实际磁盘空间（94GB）远超测试写量（51GB），环境不满足测试前置条件
- **是否有规避手段**: 是 — 使用更小磁盘的 runner 或增加写量至超出可用空间

**建议**:
- 用例需根据实际 runner 磁盘容量调整写入量（如 94GB+ 才能触发 ENOSPC）
- 或 Phase 02 确认 runner 规格中 small 的磁盘上限承诺

---

## 失败分诊 · REL-CANCEL-01-028 · 手动取消 workflow——运行中取消时 always() cleanup step 仍应执行

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 CANCELLED，实际 COMPLETED

**根因初判**: 环境问题 / 需人工判断

**责任人**: Phase 02 — harness 未执行 workflow cancel 操作；workflow 自然完成（sleep 60 秒 → cleanup 执行）

**证据**:

- **Job 日志全量**（9 行）:
  ```
  cleanup executed
  ```

- **预期行为**（用例 REL-CANCEL-01-028，P1）:
  - 步骤 1: sleep 60
  - 步骤 2: if always() → echo cleanup executed
  - 预期: cleanup_step_status=success, run_status=canceled（在 sleep 期间被主动取消）

- **实际行为**:
  - sleep 60 正常执行完毕
  - always() cleanup step 正常执行（"cleanup executed"）
  - workflow 以 COMPLETED 结束——**未被取消**
  - harness 未在 sleep 期间发送 cancel API 调用

- **对照 GitCode 规格**: 文档未明确记录 cancel API 能力

- **环境前提验证**: 无 cancel API 调用证据。测试 YAML 依赖 harness 在执行中主动 cancel workflow，但日志无取消痕迹

**置信度**: 中 — harness 未执行 cancel 操作是明确事实，但无法确定是 harness 未实现 cancel 功能还是 cancel API 不可用

**影响**:
- **阻塞性**: ⚪无影响 — workflow 正常完成，只是测试场景不满足
- **静默性**: 🟡可察觉 — 断言报告 expected CANCELLED got COMPLETED
- **影响面**: 🟢单用例
- **综合**: 无影响——harness cancel 功能缺失或未触发，非平台 workflow 缺陷
- **是否有规避手段**: 是 — harness 实现 cancel API 调用后重跑

**建议**:
- Phase 02 harness 实现 workflow cancel 触发机制
- 确认 GitCode API 是否支持 cancel workflow

---

## 失败分诊 · REL-FAULT-01-031 · 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 FAILED，实际 COMPLETED

**根因初判**: 环境问题

**责任人**: Phase 02 — harness 未执行 fault_injection kill_runner 动作；SIGKILL 未发送，所有步骤正常完成

**证据**:

- **Job 日志全量**（24 行）:
  ```
  step_one_marker
  step_two_marker
  step_four_marker
  step_five_marker
  ```

- **预期行为**（用例 REL-FAULT-01-031，P1）:
  - fault_injection: at=mid_job, action=kill_runner, target_step=3
  - 预期: job_status=failure, run_logs 含 step_one_marker, run_logs 不含 step_four_marker

- **实际行为**:
  - 5 个步骤**全部执行完毕**（step_one 到 step_five 均有输出）
  - step_three（sleep 30）完成——未被 SIGKILL 中断
  - 无任何 runner 被杀或异常终止的证据

- **对照 GitCode 规格**: 故障注入非 GitCode 平台承诺行为，是 harness 层面的测试机制

**置信度**: 中 — 所有步骤均完成证明 kill_runner 未生效，但无法确定是 harness fault_injection 引擎 bug 还是平台阻止了 kill

**影响**:
- **阻塞性**: ⚪无影响 — harness fault_injection 未触发，非平台缺陷
- **静默性**: 🟡可察觉 — 断言 FAILED vs COMPLETED 明确
- **影响面**: 🟢单用例
- **综合**: 无影响——harness fault_injection 引擎未执行 kill_runner，平台功能无异常
- **是否有规避手段**: 是 — Phase 02 审查 fault_injection 引擎的 runner kill 实现

**建议**:
- Phase 02 检查 fault_injection 的 kill_runner action 是否正确连接 runner API

---

## 失败分诊 · REL-K8S-01-045 · 自托管 K8s Runner 弹性伸缩——min=1/max=1 时并发 3 个 jobs 应排队执行

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'K8s runner scaling test' status=FAILED

**根因初判**: 需人工判断

**责任人**: 多方联合 — 自托管 runner（runs-on: [self-hosted, arch=arm, group=006]）无可用实例，job 调度后无执行

**证据**:

- **Job 日志全量**（1 行）:
  ```
  [INFO] Job(1530334955945209856_1530334955920044039) duration check: true
  ```
  无任何 shell 脚本执行、无 runner 调度日志

- **预期行为**（用例 REL-K8S-01-045，P1）:
  - runs-on: [self-hosted, arch=arm, group=006]
  - 预期: pod_count=1, max_concurrent_jobs=1（3 个 jobs 排队串行执行）

- **实际行为**:
  - job 被调度但无 runner 拾取
  - 无 shell 输出、无步骤执行痕迹
  - "duration check: true" 仅一行——可能是 job 超时/取消后的残留日志

- **对照 GitCode 规格** `runner-management/selecting-runner-labels.md`:
  - 第 9-15 行: 自托管 runner 使用 `[self-hosted, <custom-labels>]` 格式
  - 第 19-31 行: "runs-on 中的所有标签必须同时存在于 Runner 的标签集合中"
  - 测试用例要求 arch=arm + group=006 —— 若有这样的 runner 注册且在线，则应匹配

**置信度**: 低 — 单行日志缺乏诊断信息；可能是 runner 不在线/标签不匹配/未注册，也可能是 harness 未等待足够长

**影响**:
- **阻塞性**: 🔴阻塞 — job 完全未执行
- **静默性**: 🔴静默错误 — 无任何报错，仅一行 "duration check"
- **影响面**: 🟢单用例 — 仅自托管 K8s runner 场景
- **综合**: 阻塞+静默——自托管 runner 不可达但无明确报错
- **是否有规避手段**: 是 — 确认 group=006 的 arm runner 在线并正确注册标签

**建议**:
- Phase 02 确认 runner group=006 的 arm 实例是否在线
- 若 runner 不在线，为环境问题；若在线但未匹配，为平台标签匹配缺陷

---

## 失败分诊 · REL-MATRIX-01-026 · matrix fail-fast=true——任意 job 实例失败应立即取消其余实例

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 FAILED，实际 COMPLETED

**根因初判**: 用例问题

**责任人**: Phase 01 — 测试 workflow 中无任何步骤会失败，fail-fast 行为未被触发；且断言 cancelled_jobs_count=8 与 matrix 只有 3 个组合矛盾

**证据**:

- **Job 日志全量**（18 行）:
  ```
  version=1
  version=2
  version=3
  ```
  3 个矩阵实例全部输出 version 号并成功完成

- **预期行为**（用例 REL-MATRIX-01-026，P1）:
  - strategy.matrix: version=[1,2,3], fail-fast=true
  - 预期: job_status=failure（需要至少一个实例失败），cancelled_jobs_count=8

- **实际行为**:
  - 唯一步骤: `echo version=${{ matrix.version }}` —— 全部成功
  - 无任何故意失败逻辑
  - fail-fast=true 无法触发（没有实例失败）
  - 断言 cancelled_jobs_count=8 与 matrix 仅有 3 个组合严重矛盾

- **对照 GitCode 规格** `writing-pipelines/configure-matrix-builds.md`:
  - 第 22-31 行: `fail-fast` 配置——当设为 true 时"任意 job 实例失败，取消其余未完成实例"

**置信度**: 高 — workflow 设计无失败路径，断言数与实际 matrix 大小矛盾

**影响**:
- **阻塞性**: ⚪无影响 — 用例设计缺陷，非平台问题
- **静默性**: 🟢明确报错 — 断言失败
- **影响面**: 🟢单用例
- **综合**: 无影响——用例需要加入条件性失败步骤（如 version=2 时 exit 1）才能测试 fail-fast
- **是否有规避手段**: 是 — 用例加入条件性失败逻辑，修正 cancelled_jobs_count

**建议**:
- Phase 01 重新设计此用例：加入 `if: ${{ matrix.version == 2 }}` 的故意失败步骤
- 修正断言：cancelled_jobs_count 应为 2（3 个实例中 1 个失败后取消其余 2 个）

---

## 失败分诊 · REL-NEEDS-01-025 · needs 失败传播——上游 job 失败时下游 job 应被 skip

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 FAILED，实际 FAILED（pass）；assertions[1] (run_status, positive) — 预期 IGNORED，实际 FAILED（不 pass）

**根因初判**: 产品缺陷

**责任人**: 平台方 — `needs: job_a` 且 job_a 失败时，job_b 应被 skipped/ignored，但实际 job_b 同样 FAILED（被执行了）

**证据**:

- **Job 日志全量**（6 行）:
  ```
  ::error::Process exited with code 1
  ```

- **预期行为**（用例 REL-NEEDS-01-025，P1）:
  - job_a: exit 1 → status=failure
  - job_b: needs job_a → 因上游失败应被 skipped
  - 预期: job_a_status=failure, job_b_status=skipped

- **实际行为**:
  - job_a 失败（exit 1）——正确
  - job_b **也被执行且失败**——违反了 `needs` 的 downstream skip 语义
  - 日志中 job_b 也有 "Process exited with code 1" 虽然没有实际步骤输出

- **对照 GitCode 规格** `writing-pipelines/configure-dependencies-order.md`:
  - 第 79-83 行: "needs 配置 job 间的依赖关系：被依赖的 job 完成后才执行当前 job...依赖的 job 失败时，当前 job 默认不执行"

- **精确定位**: 文档第 83 行确凿承诺 "依赖的 job 失败时，当前 job 默认不执行"。测试 YAML 的 job_b 设置了 `needs: job_a`，与文档示例一致。实际行为与文档承诺矛盾。

**置信度**: 高 — GitCode 文档明确承诺 needs 失败 skip，日志证据确凿显示 job_b 被执行

**影响**:
- **阻塞性**: 🔴阻塞 — needs 依赖语义出错可导致整个 CI pipeline 行为不可预期
- **静默性**: 🔴静默错误 — 用户可能未察觉下游 job 在上游失败时仍被执行
- **影响面**: 🔴跨维度 — needs 是 workflow 基础件，影响所有使用 needs 依赖的 pipeline
- **综合**: 阻塞+静默+跨维度——needs 失败传播与文档承诺矛盾，上游失败时下游 job 未被 skip
- **是否有规避手段**: 否 — 除非用户改用 stages 机制或手动 `if: ${{ always() && ... }}`

**建议**:
- 平台方审查 needs 依赖在 upstream job FAILED 时的 downstream skip 逻辑
- 相关用例: 所有依赖 needs 传播语义的其他用例

---

## 失败分诊 · REL-TIMEOUT-01-009 · 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被强制终止

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, positive) — 预期 FAILED，实际 CANCELLED

**根因初判**: 标记不匹配

**责任人**: Phase 01 — 超时后的平台状态为 CANCELLED，但 YAML 断言 `job_status=failure`，编译器未将 timeout→CANCELLED 正确映射

**证据**:

- **Job 日志全量**（4 行）:
  ```
  [INFO] Job(...) duration check: true
  ```
  无 shell 步骤输出——job 被 timeout 机制终止

- **预期行为**（用例 REL-TIMEOUT-01-009，P1）:
  - timeout-minutes: 1，sleep 120（2 分钟）
  - 预期: job_status=failure, job_duration_seconds ≤ 70

- **实际行为**:
  - sleep 120 远超 timeout-minutes=1
  - 平台在 ~60s 后终止 job，状态设为 CANCELLED（而非 FAILED）
  - timeout 机制**功能正常**
  - 但 assertion_engine 编译出 expected=FAILED vs actual=CANCELLED

- **对照 GitCode 规格** `writing-pipelines/configure-jobs.md`:
  - 第 110-121 行: "timeout-minutes: 30...默认超时时间为 360 分钟（6 小时）。超时后 job 将被强制终止"
  - 文档承诺 "强制终止"，但未承诺终止后状态词汇是 "failed" 还是 "cancelled"

- **根因**: assertion_engine 将 YAML `job_status=failure` 编译为 `run_status expected=FAILED`，但平台 timeout 后 status 实际为 CANCELLED。这是 CANCELLED↔FAILED 状态词汇映射问题。

**置信度**: 高 — timeout 功能有效，问题是状态词汇映射

**影响**:
- **阻塞性**: ⚪无影响 — timeout 功能正常
- **静默性**: 🟢明确报错 — 断言报告 expected FAILED got CANCELLED
- **影响面**: 🟢单用例
- **综合**: 无影响——timeout 机制正常，只需平台明确文档承诺超时终止的状态词汇 → 修正断言映射
- **是否有规避手段**: 是 — compile_asserts.py 将 timeout→CANCELLED 映射或 YAML 改用 equals: "cancelled"

**建议**:
- Phase 01 在 `compile_asserts.py` 中处理 CANCELLED 状态词汇
- 建议 GitCode 文档明确 timeout 后的 job status 词汇（CANCELLED vs FAILED）

---

## 失败分诊 · REL-BIGRUNNER-01-066 · 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'compile on 2xlarge' status=FAILED

**根因初判**: 需人工判断

**责任人**: 多方联合 — YAML 中所有 job 均使用 `runs-on: [ubuntu-latest, x64, small]`（非 xlarge/2xlarge）；2xlarge job 仅有 1 行日志无任何 shell 输出

**证据**:

- **Job 日志全量**（7 行）:
  ```
  [compile on xlarge] compiling
  [compile on 2xlarge] [INFO] Job(...) duration check: true  （仅 1 行）
  ```

- **预期行为**（用例 REL-BIGRUNNER-01-066，P1）:
  - 两个 job 反复编译 30s
  - 预期: success_rate ≥ 90%, failure_attribution=clear

- **实际行为**:
  - compile_xlarge 正常（echo compiling, sleep 30）
  - compile_2xlarge 仅有 1 行 duration check，无 shell 脚本执行
  - YAML 中两个 job 的 runs-on 均为 `[ubuntu-latest, x64, small]`——与"xlarge/2xlarge"标题不符
  - 2xlarge job 失败原因不明（可能是 runner 资源耗尽、schedule 超时等）

- **对照 GitCode 规格**: `selecting-runner-labels.md` 第 14 行指定 small flavor；xlarge/2xlarge 规格未在测试用的 runs-on 中请求

**置信度**: 低 — 2xlarge job 无任何诊断信息输出；YAML 中 runs-on 与测试标题不一致

**影响**:
- **阻塞性**: 🔴阻塞 — 2xlarge job 完全未执行
- **静默性**: 🔴静默错误 — 1 行日志无任何错误信息
- **影响面**: 🟢单用例
- **综合**: 阻塞+静默——2xlarge job 静默失败无诊断信息，需确认是 runner 不可用还是平台调度缺陷
- **是否有规避手段**: 否 — 需平台提供至少 error 消息

**建议**:
- 确认测试 YAML 是否应使用 `[ubuntu-latest, x64, xlarge]` / `[ubuntu-latest, x64, 2xlarge]`
- 若 xlarge/2xlarge 规格不存在于 runner 池，为环境问题
- 若存在但调度失败而无报错，为平台缺陷

---

## 失败分诊 · REL-RUNNER-01-049-V2 · Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存/磁盘 vs 声明值

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'probe 2xlarge runner' status=FAILED

**根因初判**: 需人工判断

**责任人**: 多方联合 — 与 REL-BIGRUNNER-01-066 相同模式；所有 job 使用 `runs-on: [ubuntu-latest, x64, small]`

**证据**:

- **Job 日志全量**（21 行）:
  ```
  [probe xlarge runner] 16 cores, 62256MB RAM, 118GB disk, 94GB available
  [probe 2xlarge runner] [INFO] Job(...) duration check: true  （仅 1 行）
  ```

- **预期行为**（用例 REL-RUNNER-01-049-V2，P1）:
  - 探针: nproc, free -m, df -BG
  - 预期: resource_ratio ≥ 0.9, failure_attribution=clear

- **实际行为**:
  - probe-xlarge job 正常输出系统资源信息（16 核 CPU, 62GB RAM, 94GB 可用磁盘）
  - probe-2xlarge job 仅有 1 行 duration check
  - 两个 job 的 runs-on 均为 `[ubuntu-latest, x64, small]`
  - xlarge job 的实际规格是 "16 核 + 62GB RAM + 94GB disk"——这更接近 medium/large 而非 xlarge

- **对照 GitCode 规格**: `selecting-runner-labels.md` 第 14 行指定 small/large 等 flavor

**置信度**: 低 — 2xlarge job 无输出，无法判断失败原因

**影响**:
- **阻塞性**: 🔴阻塞 — 2xlarge 探针完全未执行
- **静默性**: 🔴静默错误 — 无任何错误信息
- **影响面**: 🟢单用例
- **综合**: 阻塞+静默——2xlarge job 静默失败
- **是否有规避手段**: 否 — 需平台提供 runner 调度错误信息

**建议**:
- 确认 GitCode 是否提供 xlarge/2xlarge flavor runner
- 测试 YAML runs-on 应改为对应规格标签
- 若 2xlarge 不可用且平台不报错，为产品缺陷（静默调度失败）

---

## 失败分诊 · REL-YAMLCACHE-01-060 · Workflow YAML 缓存失效——修改后无旧代码残留

**判定结果**: FAIL
**失败断言**: assertions[0] (value, run_logs) — 预期 log contains 'marker_v2'，实际 absent

**根因初判**: 用例问题 / 需人工判断

**责任人**: Phase 01 / 多方联合 — YAML 中 workflow 的 run 步骤输出 `marker_v1`，但断言要求 `marker_v2`

**证据**:

- **Job 日志全量**（5 行）:
  ```
  marker_v1
  ```

- **预期行为**（用例 REL-YAMLCACHE-01-060，P1）:
  - 第一次运行：workflow 含 `echo marker_v1`
  - 修改 workflow → 第二次运行：`echo marker_v2`（验证缓存失效）
  - 预期: run_logs 含 marker_v2，不含 marker_v1

- **实际行为**:
  - 日志仅输出 marker_v1
  - YAML 文件本身含 `echo marker_v1`（第 22 行）
  - 断言 `contains: "marker_v2"` 的 marker 在当前 YAML 中并不存在

- **测试设计问题**:
  - 此用例要求在**两次 workflow 触发之间**修改 YAML（从 marker_v1 改为 marker_v2）
  - 当前单次执行的 harness 无法模拟此场景——workflow YAML 只提交了一次
  - 因此断言 marker_v2 永远不会满足（除非 harness 在第一次触发后修改并重新触发）

- **对照 GitCode 规格**: 无明确 YAML 缓存行为文档承诺

**置信度**: 高 — 测试机制缺陷：YAML 中含 marker_v1 但断言 marker_v2，且 harness 不支持两阶段触发

**影响**:
- **阻塞性**: ⚪无影响 — 测试设计缺陷
- **静默性**: 🟢明确报错 — 断言报告 marker_v2 absent
- **影响面**: 🟢单用例
- **综合**: 无影响——用例需要两阶段交互（修改→重触发），当前 harness 不支持
- **是否有规避手段**: 是 — 设计为两阶段用例，或 phase02 支持 workflow YAML 更新后重触发

**建议**:
- Phase 02 harness 支持"修改 workflow YAML → 重触发 → 验证结果"两阶段流程
- 或重新设计为先用含 marker_v1 的 YAML 跑一次，再修改跑第二次

---

## 失败分诊 · REL-ARTPERF-01-053-V2 · 制品传输性能——1GB artifact 上传下载耗时（补充说明）

> 已在上述条目中分析，此处补充未覆盖的断言细节。

**失败断言补充**: 除 status 断言外，hash_match 和 upload/download time 均因 upload 阶段失败而未测量

**建议**: 与其他 artifact 名称冲突/配额问题的用例一并处理

---

# 总览

| 根因分类 | 数量 | 用例 |
|---------|------|------|
| **用例问题** (quadruple-brace `${{{{ }}}}`) | 4 | REL-ARTCONC-01-063, REL-MATRIX-01-038, REL-MATRIX-01-039, REL-OUTPUT-01-016 |
| **环境问题** (artifact 名称冲突) | 4 | REL-ART-01-041, REL-ARTPERF-01-053, REL-FAULT-01-032, REL-RETAIN-01-047 |
| **环境问题** (artifact quota 超限) | 1 | REL-ARTPERF-01-053-V2 |
| **环境问题** (fault_injection 未触发) | 2 | REL-FAULT-01-031, REL-CANCEL-01-028 |
| **标记不匹配** (status 词汇映射) | 2 | REL-CONTINUE-01-030, REL-TIMEOUT-01-009 |
| **用例问题** (测试设计缺陷) | 2 | REL-MATRIX-01-026, REL-YAMLCACHE-01-060 |
| **产品缺陷** (needs 失败传播) | 1 | REL-NEEDS-01-025 |
| **需人工判断** (runner 不可达/静默失败) | 3 | REL-K8S-01-045, REL-BIGRUNNER-01-066, REL-RUNNER-01-049-V2 |
| **环境问题** (磁盘充足) | 1 | REL-DISK-01-019 |

**关键发现**:
1. **P0 产品缺陷**: REL-NEEDS-01-025 — needs 上游失败时下游未 skip，与 GitCode 文档第 83 行承诺矛盾
2. **批量用例问题**: 4 个 `${{{{ }}}}` 四括号语法 bug（Phase 01 已知问题）
3. **批量环境问题**: 5 个 artifact 相关用例因残留名称冲突/配额耗尽失败
4. **静默失败模式**: 3 个用例（K8s runner、bigrunner、runner probe）job 完全无输出就失败——需平台提供至少错误信息
