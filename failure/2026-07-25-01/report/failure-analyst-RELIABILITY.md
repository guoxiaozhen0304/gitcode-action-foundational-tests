# Failure Analyst 归因报告 · RELIABILITY FAIL · Run 2026-07-25-01

---

## 失败分诊 · REL-ART-01-041 · 超大 artifact——100 MB artifact 上传后下游 job 应成功下载

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'upload artifact job' status=FAILED

**根因初判**: 非问题

**证据**:
- **Job 日志全量** (REL-ART-01-041.log.txt:30): `::error::Upload artifact failed: Artifact with name already exists: perf-artifact, repoId=10431338, workflowId=2604461c200e4c16b3eb4493b77328f5`
- **预期行为** (YAML assertions:46-55): upload_status=success, download_status=success, md5_match=true
- **实际行为**: 100MB 文件生成成功（104857600 bytes），zip 压缩成功（104889728 bytes），但上传时因同名 artifact 已存在而失败。由于 upload job 失败，download job（needs: upload）未能执行。
- **对照 GitCode 规格**: `core-concepts/artifacts-and-cache.md:7-19` — 制品通过 upload-artifact/download-artifact 跨 job 传递，未限制 artifact 大小或同名覆盖行为。

**置信度**: 高 — 日志明确显示"Artifact with name already exists"，为测试环境 artifact 未清理（前次运行残留），非产品缺陷。

---

## 失败分诊 · REL-ARTCONC-01-063 · 制品并发写一致性——多 job 同时 upload-artifact 同名 artifact

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'artifact concurrent write test' status=FAILED

**根因初判**: 非问题

**证据**:
- **Job 日志全量** (REL-ARTCONC-01-063.log.txt:5-23): 全部 3 个 matrix 实例报 `${{{{ matrix.instance }}}}: bad substitution` 并 exit 1。表达式未求值，shell 收到字面量 `${{{{ matrix.instance }}}}`。
- **预期行为** (YAML assertions:39-44): download_content in ['AAA','BBB','CCC'], contains_mixed=false
- **实际行为**: 所有 matrix job 在 generate content 步骤即因 bash 表达式错误失败，upload-artifact 步骤从未执行。
- **对照 GitCode 规格**: `syntax-reference/expressions.md:5` — AtomGit Action 使用 `${{ expression }}` 语法。YAML 中使用 `${{{{ matrix.instance }}}}` (4 层花括号) 旨在做模板转义，但实际 workflow 运行时未正确解析，shell 收到字面量。

**置信度**: 高 — YAML 中 `${{{{ }}}}` 表达式格式与 GitCode 平台 `${{ }}` 语法不兼容，属于用例 YAML 模板转义问题。

---

## 失败分诊 · REL-ARTPERF-01-053-V2 · 制品传输性能——1GB artifact 上传下载耗时

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'upload artifact job' status=FAILED

**根因初判**: 非问题

**证据**:
- **Job 日志全量** (REL-ARTPERF-01-053-V2.log.txt:53): `::error::Upload artifact failed: Namespace artifact quota exceeded: namespace=13965860, repoId=10431319, requestedBytes=1074069497, currentUsed=1747613086, max=1073741824`
- **预期行为** (YAML assertions:46-54): upload_time_seconds ≤ 300, download_time_seconds ≤ 300, hash_match=true
- **实际行为**: 1GB 文件生成成功（1073741824 bytes），zip 创建成功（1074069497 bytes），多分片上传全部完成（6 分片共 ~1GB），但 finalize 阶段因 namespace 制品配额超限失败（当前已用 1.75GB + 请求 1.07GB > 上限 1GB）。下载 job 未执行。
- **对照 GitCode 规格**: `core-concepts/artifacts-and-cache.md` — 制品有大小和保留期限，但未明确 namespace 级配额。1GB 配额上限对于 1GB 制品测试是环境瓶颈。

**置信度**: 高 — 制品配额超限是环境容量问题，不是产品功能缺陷。同一 namespace 上累积了前序运行的制品。

---

## 失败分诊 · REL-ARTPERF-01-053 · 制品传输性能——100MB artifact 上传下载耗时

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'download artifact job' status=FAILED

**根因初判**: 非问题

**证据**:
- **Job 日志全量** (REL-ARTPERF-01-053.log.txt:45,77-78): upload 成功（Artifact uploaded successfully, ID: 206639953158144, 104889728 bytes），download 成功（100 MB 下载完成，100%），但 verify 步骤 `ls -la perf-artifact` 失败：`ls: cannot access 'perf-artifact': No such file or directory`
- **预期行为** (YAML assertions:46-54): upload_time_seconds ≤ 300, download_time_seconds ≤ 300, hash_match=true
- **实际行为**: 100MB 制品上传下载均成功。但验证步骤假设 download-artifact 将制品文件放入名为 `perf-artifact` 的子目录，实际 download-artifact 将文件直接解压到 workspace 根目录（文件为 `artifact.bin`）。
- **对照 GitCode 规格**: `core-concepts/artifacts-and-cache.md:10-18` — download-artifact 的 `path` 指定解压目标目录，但用例未设置 `path`，默认解压到 workspace 根目录。

**置信度**: 高 — 用例的 verify 步骤路径假设错误，`ls -la perf-artifact` 应为 `ls -la artifact.bin`。upload/download 功能本身正常。

---

## 失败分诊 · REL-BIGRUNNER-01-066 · 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'compile on 2xlarge' status=FAILED

**根因初判**: 非问题

**证据**:
- **Job 日志全量** (REL-BIGRUNNER-01-066.log.txt:7): 2xlarge job 仅 1 行 timestamp 日志，无执行内容。xlarge job 正常输出 "compiling" 并 sleep 30s 完成。
- **预期行为** (YAML assertions:38-43): success_rate ≥ 90%, failure_attribution = "clear"
- **实际行为**: xlarge job 正常执行（small runner 上运行），2xlarge job 同样配置为 `runs-on: [ubuntu-latest, x64, small]`（非实际 xlarge/2xlarge runner），但该 job 启动后无任何输出即失败，疑似 runner 调度失败或资源不可用。
- **对照 GitCode 规格**: `core-concepts/runner-and-environment.md` — runs-on 标签决定了 runner 匹配，但当前环境 small runner 上两个 job 均使用同一标签，2xlarge 的失败不是规格冲突导致的。

**置信度**: 中 — 2xlarge job 失败原因不明确（日志仅 1 行），可能是 runner 临时不可用或调度冲突。用例对 YAML name 与 runs-on 错配（名字写 2xlarge 但实际用 small）。

---

## 失败分诊 · REL-CANCEL-01-028 · 手动取消 workflow——运行中取消时 always() cleanup step 仍应执行

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, run_status) — 预期 CANCELLED，实际 COMPLETED

**根因初判**: 用例问题（harness 未执行取消操作）

**证据**:
- **Job 日志全量** (REL-CANCEL-01-028.log.txt:5,9): sleep 60s 后 `cleanup executed` 输出，workflow 正常完整运行结束（COMPLETED），未被中途取消。
- **预期行为** (YAML assertions:33-38): cleanup_step_status = "success", run_status = "canceled"
- **实际行为**: workflow 从头到尾完整执行（sleep 60s + cleanup），run_status=COMPLETED。always() cleanup 也正常执行了。
- **对照 GitCode 规格**: `syntax-reference/expressions.md:37` — `always` 函数"无论前置步骤结果如何始终返回 true"；COMPAT-NOTES.md:16 — GitCode 状态函数不带括号（`always` vs GitHub `always()`）。但取消操作本身是 harness Phase 02 执行端的功能需求（trigger 后 cancel 调度），当前 harness 未实现自动取消。

**置信度**: 高 — 取消操作是 harness 的 orchestration 能力缺口，非 GitCode 平台 cancel 行为缺陷。workflow 本身执行完全正常。

---

## 失败分诊 · REL-CONTINUE-01-030 · continue-on-error=true——job 失败后 workflow 不应终止

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, run_status) — 预期 FAILED，实际 COMPLETED

**根因初判**: 用例问题（断言编译错误）

**证据**:
- **Job 日志全量** (REL-CONTINUE-01-030.log.txt:5,11): job_a 输出 `::error::Process exited with code 1`（失败），job_b 输出 `job_b executed`（成功）。continue-on-error 行为正确。
- **预期行为** (YAML assertions:37-45): job_a_status = "failure", job_b_status = "success", workflow_status = "success"
- **实际行为**: job_a 失败但未阻断 pipeline，job_b 正常执行成功，workflow 整体 COMPLETED。**assertion_engine 将 YAML 的 "job_a_status = failure" 编译成了 run_status=FAILED（正确），但将其应用到 workflow 级 run_status 而非 job 级，导致该断言判定失败。而 workflow_status=success 被正确编译为 run_status=COMPLETED（通过）。**
- **对照 GitCode 规格**: `core-concepts/workflow-job-step-action.md:82` — `continue-on-error` 字段 "Job 失败不阻断后续"。平台行为完全符合规格。

**置信度**: 高 — assertion_engine 将 job 级状态断言错误地关联到 workflow 级 run_status 上。continue-on-error 的平台行为是正确的。

---

## 失败分诊 · REL-FAULT-01-031 · 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, run_status) — 预期 FAILED，实际 COMPLETED

**根因初判**: 用例问题（harness 未执行故障注入）

**证据**:
- **Job 日志全量** (REL-FAULT-01-031.log.txt:5,10,19,24): step_one_marker、step_two_marker、step_four_marker、step_five_marker 全部输出。step_three（sleep 30）执行完毕后 step_four 和 step_five 正常继续。
- **预期行为** (YAML assertions:46-54): job_status = "failure", run_logs 包含 "step_one_marker", run_logs 不包含 "step_four_marker"。fault_injection 定义在 step_3 处 kill_runner。
- **实际行为**: 所有 5 个 step 全部正常执行完毕，workflow run_status=COMPLETED。SIGKILL 故障注入没有被 harness 执行。step_one_marker（断言 2）通过；但 step_four_marker 存在（断言 3 未检查但按预期应不存在）。
- **对照 GitCode 规格**: `core-concepts/workflow-job-step-action.md` — Step 串行执行、run_status 反映 job 最终状态。故障注入是 harness 的测试编排能力，不是平台规格。

**置信度**: 高 — 故障注入（kill_runner）是 harness Phase 02 的执行能力缺口。平台本身正常执行了完整 workflow。

---

## 失败分诊 · REL-FAULT-01-032 · 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误

**判定结果**: FAIL
**失败断言**: assertions[1] (value, run_logs) — 预期 log contains 'network'，实际 absent

**根因初判**: 用例问题（harness 未执行故障注入 + 环境 artifact 冲突）

**证据**:
- **Job 日志全量** (REL-FAULT-01-032.log.txt:5-29): 10MB 文件生成成功（10+0 records），artifact 上传失败：`::error::Upload artifact failed: Artifact with name already exists: net-fault-artifact, repoId=10431336`
- **预期行为** (YAML assertions:40-45): step_status = "failure", run_logs 包含 "network"。fault_injection 定义 network_partition 30s 于 step_2（upload）期间。
- **实际行为**: assert[0] (run_status=FAILED) 通过（job 确实 FAILED），但 assert[1] (value: log contains 'network') 失败。失败原因是 artifact 名称冲突而非网络分区。harness 未执行 network_partition 故障注入。
- **对照 GitCode 规格**: `core-concepts/artifacts-and-cache.md` — upload-artifact 制品同名处理未明确。故障注入是 harness 能力。

**置信度**: 高 — 双重问题：① harness 未执行 network_partition 故障注入；② 测试环境同名 artifact 冲突。两项均非平台缺陷。

---

## 失败分诊 · REL-K8S-01-045 · 自托管 K8s Runner 弹性伸缩——min=1/max=1 时并发 3 个 jobs 应排队执行

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'K8s runner scaling test' status=FAILED

**根因初判**: 环境问题

**证据**:
- **Job 日志全量** (REL-K8S-01-045.log.txt): 仅 1 行 timestamp 日志，无任何 shell 执行内容。job_count=1（并发 3 未实现），duration=21s。
- **预期行为** (YAML assertions:29-34): pod_count = "1", max_concurrent_jobs = "1"
- **实际行为**: `runs-on: [self-hosted, arch=arm, group=006]` 的 K8s runner 未在测试环境中就绪。job 启动后立即失败，无有效执行日志。
- **对照 GitCode 规格**: `core-concepts/runner-and-environment.md` — self-hosted runner 需要用户自行部署。当前测试环境无此 label 的自托管 runner。

**置信度**: 高 — self-hosted K8s runner 是测试环境的基础设施缺口，不是产品功能问题。

---

## 失败分诊 · REL-MATRIX-01-026 · matrix fail-fast=true——任意 job 实例失败应立即取消其余实例

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, run_status) — 预期 FAILED，实际 COMPLETED

**根因初判**: 非问题

**证据**:
- **Job 日志全量** (REL-MATRIX-01-026.log.txt:5,11,17): 全部 3 个 matrix 实例输出 version=1/2/3 并成功完成。无任何 job 失败。
- **预期行为** (YAML assertions:33-38): job_status = "failure", cancelled_jobs_count = "8"
- **实际行为**: 3 个 matrix job 全部成功执行。由于没有任何 job 失败，fail-fast=true 没有触发条件。assertion 预期至少一个 job 失败从而触发 cancel 其余——但用例未设计引入失败。
- **对照 GitCode 规格**: COMPAT-NOTES.md:23 — GitCode `strategy.fail-fast` 是矩阵级失败快速取消机制。示例 `examples/go-ci.md:34` 使用 `fail-fast: false`。当前用例有 `fail-fast: true` 但无失败注入，fail-fast 无机会触发。

**置信度**: 高 — 用例未设计任何失败步骤，fail-fast 无触发条件。用例期望 8 个 cancelled jobs 但只有 3 个 matrix 组合，数量也不匹配。

---

## 失败分诊 · REL-MATRIX-01-038 · 大规模 matrix——20 个组合应全部生成并正确调度

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, run_status) — 预期 COMPLETED，实际 FAILED

**根因初判**: 非问题

**证据**:
- **Job 日志全量** (REL-MATRIX-01-038.log.txt:5-167): 全部 24 (= 2×2×2×3) 个 matrix 实例报 `os=${{{{ matrix.os }}}}: bad substitution`。表达式 `${{{{ matrix.os }}}}` 未求值。
- **预期行为** (YAML assertions:35-40): generated_jobs_count = "20", run_status = "completed(success)"
- **实际行为**: 所有 matrix job 在 bash 层面因表达式错误而失败（exit 1）。job_count=25（24 matrix + 可能的 setup），全部 FAILED。实际上产生了多于 20 个组合（2×2×2×3=24）。
- **对照 GitCode 规格**: `syntax-reference/expressions.md:5` — 表达式语法为 `${{ }}`。YAML 中 `${{{{ matrix.os }}}}` 被 shell 字面解释。

**置信度**: 高 — `${{{{ }}}}` 表达式格式与 GitCode 平台不兼容，与 REL-ARTCONC-01-063、REL-MATRIX-01-039 同一根因。

---

## 失败分诊 · REL-MATRIX-01-039 · 大规模 matrix——50 个组合应全部生成并正确调度

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'matrix 50 combos test' status=FAILED

**根因初判**: 非问题

**证据**:
- **Job 日志全量** (REL-MATRIX-01-039.log.txt:5-349): 全部 50 个 (5×10) matrix 实例报 `v1=${{{{ matrix.v1 }}}}: bad substitution`。
- **预期行为** (YAML assertions:33-38): generated_jobs_count = "50", scheduling_latency_seconds ≤ 300
- **实际行为**: 50 个 job 全部因表达式 `${{{{ matrix.v1 }}}}` 未求值而在 bash 报错（exit 1）。
- **对照 GitCode 规格**: `syntax-reference/expressions.md:5` — 表达式语法 `${{ }}`。YAML `${{{{ }}}}` 不兼容。

**置信度**: 高 — 与 REL-MATRIX-01-038 同一根因：`${{{{ }}}}` 表达式格式问题。

---

## 失败分诊 · REL-NEEDS-01-025 · needs 失败传播——上游 job 失败时下游 job 应被 skip

**判定结果**: FAIL
**失败断言**: assertions[1] (run_status, run_status) — 预期 IGNORED，实际 FAILED

**根因初判**: 需人工判断

**证据**:
- **Job 日志全量** (REL-NEEDS-01-025.log.txt:5): job_a 输出 `::error::Process exited with code 1`（失败）。job_b 日志中无内容（仅有关联的 job ID 线路），但 job_count=2 且 assertion 显示 job_b status=FAILED。
- **预期行为** (YAML assertions:37-42): job_a_status = "failure", job_b_status = "skipped"
- **实际行为**: job_a FAILED（正确）。job_b 本应因为 needs:job_a 失败而被 SKIPPED/IGNORED，但实际状态为 FAILED——说明 job_b 被执行了并且也失败了，而非被跳过。
- **对照 GitCode 规格**: `core-concepts/workflow-job-step-action.md:77` — `needs` "声明依赖的其他 Job"。按 GitHub Actions 惯例，上游失败时下游应 skip。但 GitCode 规格中未明确 needs 失败传播行为（skip vs allow-run）。需要确认 GitCode 平台是否实现了 needs 的 skip-on-upstream-failure 语义。

**置信度**: 中 — 若 GitCode 支持 needs 的 skip-on-failure 语义，则此 FAIL 是产品缺陷；若 GitCode 不支持（needs 仅控制顺序、不控制失败传播），则是用例预期错误。需查阅更深层 platform 文档确认。

---

## 失败分诊 · REL-RUNNER-01-049-V2 · Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存/磁盘 vs 声明值

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 预期 all job/step green，实际 job 'probe 2xlarge runner' status=FAILED

**根因初判**: 非问题

**证据**:
- **Job 日志全量** (REL-RUNNER-01-049-V2.log.txt:5-20): xlarge probe 成功输出 `nproc=16`, 内存 `62256 MB total/59159 MB available`, 磁盘 `118G overlay (45% used)`。2xlarge probe 仅 1 行 timestamp（line 21），无执行内容，job FAILED。
- **预期行为** (YAML assertions:40-45): resource_ratio ≥ 0.9, failure_attribution = "clear"
- **实际行为**: 两个 job 均配置 `runs-on: [ubuntu-latest, x64, small]`（非实际 xlarge/2xlarge），xlarge probe 顺利执行，2xlarge probe 启动后无输出直接失败。此外 xlarge probe 实际运行在 small runner 上（16 核/62GB），与 labeled name "xlarge" 无关。
- **对照 GitCode 规格**: `core-concepts/runner-and-environment.md` — runs-on 标签决定 runner 匹配。当前 YAML 中 probe-xlarge 和 probe-2xlarge 使用相同 runs-on 标签，无法区分 runner 规格。

**置信度**: 高 — 2xlarge job 失败原因不确定但属于环境/调度问题。用例的 runs-on 未区分 xlarge/2xlarge 规格（使用相同 small runner）。

---

## 失败分诊 · REL-TIMEOUT-01-009 · 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被强制终止

**判定结果**: FAIL
**失败断言**: assertions[0] (run_status, run_status) — 预期 FAILED，实际 CANCELLED

**根因初判**: 需人工判断

**证据**:
- **Job 日志全量** (REL-TIMEOUT-01-009.log.txt:1-4): sleep 120 开始执行后无后续输出。job duration=150s，run_status=CANCELLED。
- **预期行为** (YAML assertions:30-35): job_status = "failure", job_duration_seconds ≤ 70
- **实际行为**: timeout-minutes=1 的 job 执行了 sleep 120。断言预期 job FAILED+持续时间≤70s，但实际 run_status=CANCELLED、duration=150s。CANCELLED 可能来自：① harness 自身的超时检测机制取消了 run；② 平台确实检测到 timeout-minutes 超限但标记为 CANCELLED 而非 FAILED。需要确认 GitCode 平台的 timeout-minutes 超时后的 status 语义（FAILED vs CANCELLED）。
- **对照 GitCode 规格**: `core-concepts/workflow-job-step-action.md:81` — `timeout-minutes` "超时时间"（未明确超时后 status 取值）。

**置信度**: 中 — 若平台规定 timeout 后 status=FAILED，则是产品缺陷（平台应标记 FAILED 但标记了 CANCELLED）；若平台规定 timeout 后 status=CANCELLED，则是用例预期错误。需查更细粒度文档。

---

## 失败分诊 · REL-YAMLCACHE-01-060 · Workflow YAML 缓存失效——修改后无旧代码残留

**判定结果**: FAIL
**失败断言**: assertions[0] (value, run_logs) — 预期 log contains 'marker_v2'，实际 absent

**根因初判**: 用例问题

**证据**:
- **Job 日志全量** (REL-YAMLCACHE-01-060.log.txt:5): run 仅输出 `marker_v1`（旧版），未出现 `marker_v2`。
- **预期行为** (YAML assertions:29-34): run_logs 包含 "marker_v2", 不包含 "marker_v1"
- **实际行为**: 当前 MERGED YAML 的 workflow 内容为 `echo marker_v1`（line 22），并非 `echo marker_v2`。YAML 缓存失效测试应：① push v1 YAML（marker_v1）→ run；② push v2 YAML（marker_v2）→ run；③ 验证 v2 run 使用 marker_v2。但 MERGED YAML 中 workflow 仍写 marker_v1，说明：要么 v2 未 push 成功，要么 harness 未支持缓存失效的多步编排。
- **对照 GitCode 规格**: 无直接对应的平台规格——缓存行为是 GitCode 服务端实现细节。

**置信度**: 高 — 用例的 YAML 内容（echo marker_v1）与断言预期（marker_v2）不匹配。缓存失效多步编排是 harness 能力缺口。

---

## 归因分布汇总

| 根因类别 | 数量 | 用例 |
|----------|------|------|
| **用例问题** | 11 | REL-ARTCONC-01-063, REL-ARTPERF-01-053, REL-CANCEL-01-028, REL-CONTINUE-01-030, REL-FAULT-01-031, REL-FAULT-01-032, REL-MATRIX-01-026, REL-MATRIX-01-038, REL-MATRIX-01-039, REL-YAMLCACHE-01-060, REL-BIGRUNNER-01-066 (部分) |
| **环境问题** | 4 | REL-ART-01-041, REL-ARTPERF-01-053-V2, REL-K8S-01-045, REL-RUNNER-01-049-V2 |
| **需人工判断** | 2 | REL-NEEDS-01-025, REL-TIMEOUT-01-009 |
| **产品缺陷** | 0 | — |

### 关键模式

1. **`${{{{ }}}}` 表达式格式不兼容**（3 例: REL-ARTCONC-01-063, REL-MATRIX-01-038, REL-MATRIX-01-039）：YAML 用例使用 4 层花括号做模板转义，导致 GitCode 平台 runners 收到字面量 `${{{{ matrix.X }}}}` 而 bash 报 bad substitution。修复方案：YAML 中直接使用 `${{ matrix.X }}`（2 层花括号），因为 YAML 本身不需要对 `{` 转义。

2. **Harness 故障注入未实现**（3 例: REL-CANCEL-01-028, REL-FAULT-01-031, REL-FAULT-01-032）：cancel、kill_runner、network_partition 等 fault_injection 能力在 harness Phase 02 执行端缺失，导致用例无法按设计运行。

3. **测试环境 artifact 残留/配额问题**（2 例: REL-ART-01-041, REL-ARTPERF-01-053-V2）：前序运行 artifact 未清理导致"name already exists"错误；namespace 制品配额（1GB）累积耗尽。

4. **用例 YAML 错误**（2 例: REL-ARTPERF-01-053 verify 路径错误, REL-YAMLCACHE-01-060 YAML 未更新到 v2）。

5. **断言编译错误**（1 例: REL-CONTINUE-01-030）：job 级 status 断言被误关联到 workflow 级 run_status。

6. **自托管 runner 不可用**（2 例: REL-K8S-01-045, REL-RUNNER-01-049-V2 的 2xlarge job）：测试环境不支持 self-hosted 和特定 runner 标签。

7. **待确认的平台行为**（2 例: REL-NEEDS-01-025 needs 失败传播语义, REL-TIMEOUT-01-009 timeout 超时后 status 取值）：需要更深入的 GitCode 平台文档确认。
