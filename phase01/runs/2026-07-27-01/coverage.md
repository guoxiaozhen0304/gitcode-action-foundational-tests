# Coverage Report — Run 2026-07-27-01

> 验收角色：验收 agent（STOP②）
> 评审日期：2026-07-27
> 用例全集：489 条（基底复用 369 + 本轮新增 120），text/yaml 一一对应 489/489
> 优先级分布：P0=97 / P1=355 / P2=37（脚本全量复扫确认，与 case-manifest.md 一致）
> 坐标系：baseline/parity-matrix.md（26 能力项）、baseline/risk-register.md（7 风险项，4 blocker）

---

## 1. 分维度用例分布

| 维度 | 用例数 | P0 | P1 | P2 |
|---|---|---|---|---|
| completeness（COMP） | 110 | 16 | 88 | 6 |
| compatibility（COMPAT） | 137 | 16 | 104 | 17 |
| reliability（REL） | 96 | 4 | 82 | 10 |
| security（SEC） | 67 | 50 | 16 | 1 |
| usability（USE） | 79 | 11 | 65 | 3 |
| **合计** | **489** | **97** | **355** | **37** |

---

## 2. Parity Matrix 能力项覆盖核对（26/26 全覆盖）

逐行核对 baseline/parity-matrix.md，每项均能反查到至少一条用例（溯源链：能力项 → INTENT → 用例 ID，全部闭合，脚本验证 489 条用例溯源意图 0 悬空）。

| # | 能力项 | 状态 | 覆盖用例（代表 ID 与数量） |
|---|---|---|---|
| 1 | 工作流目录 `.gitcode/workflows/` | 🟡 | COMP-DIR-01-001/002、COMPAT-DIR-01-001~003、USE-DIR-01-001/002（7 条） |
| 2 | 未知/不支持字段处理 | ❓ | COMP-UNKNOWN-01-001~005、COMPAT-FIELD-01-001~003、COMPAT-CONTAINER-01-001/002、COMPAT-ENVIRON-01-001/002、USE-UNKN-01-001~004（14 条） |
| 3 | `push` 触发 + branches/paths 过滤 | ✅ | COMP-PUSH-01-001~003、COMP-TRIG-01-072/078、COMP-BOUND-01-084、COMPAT-PATHS-01-001/002、REL-PATHS-01-014/015（10 条） |
| 4 | `pull_request` vs `pull_request_target` 隔离 | ✅ | COMP-PR-01-001~003、SEC-FORK-01-001/002、SEC-TOKEN-01-001/002、COMPAT-TARGET-01-001~003、SEC-BASE-01-001/002（12 条） |
| 5 | `schedule` cron 最短间隔 | 🟡 | COMP-SCHEDULE-01-001~003、COMPAT-SCHEDULE-01-001~004、REL-SCHED-01-058、USE-SCHED-01-001、COMP-BOUND-01-085（10 条） |
| 6 | `workflow_call` 嵌套层数 | 🟡 | COMP-CALL-01-001~004、COMPAT-NEST-01-001/002、REL-NEST-01-023/024、REL-CHILDSTATE-01-064(-V2)、USE-NEST-01-001/002（12 条） |
| 7 | `stages` 阶段机制 | ❌ | COMP-STAGES-01-001~005、REL-STAGES-01-029、COMP-WFLOW-01-064、USE-DOC-01-002（8 条） |
| 8 | `post` 后处理阶段 | ❌ | COMP-STAGES-01-003、REL-POST-01-001、COMP-WFLOW-01-065、COMP-ACT-01-003（4 条） |
| 9 | `timeout-minutes` 默认 360 | ✅ | COMP-TIMEOUT-01-001/002、REL-TIMEOUT-01-007~011、REL-LONG-01-043（8 条） |
| 10 | `rerun` 次数限制 | 🟡 | COMP-RERUN-01-001~003、REL-RERUN-01-011~013、USE-RUN-01-003（7 条） |
| 11 | `runs-on` 标签体系 | 🟡 | COMP-RUNNER-01-001~003、COMP-RUNNER-01-081/082、COMPAT-RUNSON-01-001~006、USE-RUN-01-001/002、USE-LBL-01-001~006、REL-RUNNER-01-050（20 条） |
| 12 | Runner 环境隔离 / 一次性 | ❓ | COMP-ISOLATION-01-001~004、COMPAT-ISOLATE-01-001/002、SEC-RUN-01-001~003（9 条） |
| 13 | `secrets` 日志脱敏 `***` | 🟡 | COMP-SECRET-01-001~003、COMPAT-MASK-01-001/002、SEC-MASK-01-001~006、SEC-LOG-01-002、USE-MASK-01-001/002（14 条） |
| 14 | `permissions` 默认权限 | ❓ | COMP-PERMS-01-001~003、COMPAT-PERM-01-001/002/005/006、SEC-PERM-01-003/004、SEC-DEFPERM-01-001/002（11 条） |
| 15 | `permissions` 权限域命名 | ❌ | COMPAT-PERM-01-003/004、COMPAT-MIGRATE-01-001、USE-PERM-01-001/002（5 条） |
| 16 | `pull_request_target` checkout head.sha 风险 | ✅ | COMP-PRTARGET-01-001~003、SEC-PRTGT-01-001/002、SEC-BASE-01-001/002（7 条） |
| 17 | `upload-artifact` / `download-artifact` | 🟡 | COMP-ARTIFACT-01-001~003、COMPAT-ARTIFACT-01-001/002、REL-ART-01-041/042、REL-ARTCONC-01-063、REL-RETAIN-01-047（10 条） |
| 18 | `cache` fork 场景隔离 | ❓ | COMP-CACHE-01-001~003、COMPAT-CACHE-01-001/002、SEC-CACHE-01-001/002、REL-CACHE-01-046~048（10 条） |
| 19 | 运行状态机 + 日志完整性 | ✅ | COMP-STATUS-01-001/002、REL-STATE-01-058/059、REL-LOGSTABLE-01-059、REL-LOG-01-040/041（7 条） |
| 20 | `ATOMGIT_STEP_SUMMARY` Markdown | 🟡 | COMP-SUMMARY-01-001/002、USE-MD-01-001（3 条） |
| 21 | 上下文对象命名 `github.*` → `atomgit.*` | ❌ | COMPAT-CTX-01-001~005、USE-CTX-01-001/002、COMP-ATOMGIT-01-047~049（10 条） |
| 22 | 状态函数括号语法 `success()` | ❌ | COMPAT-EXPR-01-001~003/013/014、USE-STAT-01-001/002（7 条） |
| 23 | 表达式函数边界（contains/hashFiles/toJson 等） | ❓ | COMP-EXPR-01-054~059、COMPAT-EXPR-01-004~012/015/016（17 条） |
| 24 | `workflow_dispatch.inputs` 类型 | 🟡 | COMPAT-INPUTS-01-001/002、USE-INPT-01-001/002、USE-DISP-01-001~003、COMP-CTX-01-054/055（9 条） |
| 25 | 迁移报错质量（GitHub→GitCode） | ❓ | COMPAT-MIGRATE-01-001/002、USE-DIR/ENV/CTX/STAT/TYPE/LBL/RUN/PERM/NEST/SECNAME/EXPR/YAML/UNKN/CONC/DISP/DEPR 系列（约 40 条易用性用例） |
| 26 | `concurrency.max` 1-5 + QUEUE/IGNORE | 🟡 | COMP-WFLOW-01-063、REL-CONC-01-001/002、REL-QUEUE-01-003、REL-IGNORE-01-004、REL-PREEMPT-01-005/006、REL-PRESSURE-01-055、COMPAT-CONCUR-01-001~004、USE-CONC-01-001/002（14 条） |
| 27（隐含） | `strategy.matrix` 组合数上限 | ❓ | REL-MATRIX-01-026/027/038~041、REL-MATRIXFAIR-01-056、COMP-BOUND-01-086、COMPAT-MATRIX-01-003~005（11 条） |

**结论：26 个能力项（含全部 ❓/🟡/❌ 项）均有用例反查，无未覆盖能力项。**

### 2.1 门禁盲区 B1 闭环确认（Runner OS 多样性）

STOP① 裁决增补 INTENT-COMPAT-054，对应用例已生成并存在于本轮全集：

- `cases/text/COMPAT-RUNSON-01-005.md` + `cases/yaml/COMPAT-RUNSON-01-005.yaml`（windows-latest 调度结局，P1）
- `cases/text/COMPAT-RUNSON-01-006.md` + `cases/yaml/COMPAT-RUNSON-01-006.yaml`（macos-latest 调度结局，P1）

B1 已闭环；执行后需按 gate-log 建议回写 parity-matrix 增行（Runner OS 多样性）。

---

## 3. 风险登记册覆盖核对（7/7 全覆盖）

### 3.1 blocker 风险项（4 个，P0 强制覆盖）

| 风险 ID | 风险描述 | P0 覆盖用例 | 结论 |
|---|---|---|---|
| RISK-SEC-01 | fork PR 读到仓库 secrets | SEC-FORK-01-001/002、SEC-TOKEN-01-001/002、SEC-PRTGT-01-001/002、SEC-BASE-01-001/002、SEC-MASK-01-001~006、SEC-RUN-01-001~003、SEC-CACHE-01-001/002、SEC-ARTF-01-001/002、SEC-PERM-01-003/004、SEC-DEFPERM-01-001/002、SEC-ENV-01-001/002、SEC-SIDE-01-001/002、SEC-WCMD-01-001/002、SEC-NAME-01-002、COMP-PR-01-001/003、COMP-PRTARGET-01-001/002、COMP-PERMS-01-001~003、COMP-SECRET-01-001~003、COMP-CACHE-01-003、COMP-ISOLATION-01-001/002、COMPAT-MASK-01-001/002、COMPAT-PERM-01-001/002/005、COMPAT-TARGET-01-001~003、COMPAT-CACHE-01-002、USE-MASK-01-001/002（约 50 条 P0） | ✅ 足额 |
| RISK-SEC-02 | 不可信输入注入命令执行 | SEC-INJ-01-001~005、SEC-SUPPLY-01-001~003、SEC-TOCTOU-01-001/002、SEC-COMM-01-001、SEC-WCMD-01-003/004、SEC-NET-01-001、SEC-NAME-01-001、SEC-DOS-01-001（16 条 P0） | ✅ 足额 |
| RISK-REL-02 | needs 依赖的 matrix job 全成功但上游 job 初始化失败时无声失败（#101 ★，2026-07-27 STOP① 增补） | REL-NEEDS-01-026（成功路径）、REL-NEEDS-01-027（部分失败路径），均 P0，溯源 INTENT-REL-069 | ✅ 闭环（B4 已消除） |
| RISK-USE-02 | 官方文档承诺与实现不一致 / 核心迁移路径文档错误（2026-07-27 STOP① 增补） | USE-DOC-01-002/003/004/005（INTENT-USE-032/033）、USE-LBL-01-003/004（INTENT-USE-031）、USE-ENV-01-004（INTENT-USE-046）、USE-ONBD-01-001/002（INTENT-USE-050），共 9 条 P0 | ✅ 足额 |

### 3.2 非 blocker 风险项（覆盖计数）

| 风险 ID | 优先级 | 覆盖计数（按维度前缀归集） | 结论 |
|---|---|---|---|
| RISK-COMPAT-01 | P1 | COMP 110 条 + COMPAT 137 条 = 247 条（含表达式边界、默认值差异、命名差异、触发语义差异全谱系） | ✅ 无盲区 |
| RISK-REL-01 | P1 | REL 96 条（并发/洪泛/故障注入 9 条/恢复/状态机/调度公平性/超时/rerun 全谱系） | ✅ 无盲区 |
| RISK-USE-01 | P1 | USE 79 条（报错质量/文档一致性/迁移指引/onboarding 全谱系） | ✅ 无盲区 |

---

## 4. 已知输入退化项及影响面（如实标注）

| 项 | 退化内容 | 影响面 | 状态 |
|---|---|---|---|
| B2 | `inputs/business-context/` 为空模板（无部署模型、内网拓扑、历史安全台账） | 依赖部署拓扑/内网信息的 intent 证据不足，对应用例：SEC-RUN-01-003（自托管 Runner 跨项目残留）、SEC-NET-01-001（出站受控/SSRF）、SEC-LOG-01-001/002（日志访问控制）、COMPAT-RUNNER-01-005（内网 Runner）。这些用例的前置假设基于通用 CI/CD 威胁模型而非实测部署事实，执行期可能需按真实拓扑调整断言阈值 | 用户 STOP① 知悉，不阻塞本轮，安排后续补输入后重审 |
| B3 | 无真实 GitHub 侧 workflow 样本（`inputs/workflow-samples/` 缺真实负载） | COMPAT 维度 137 条用例的「现实命中率」论证依赖 GitHub 官方文档语义而非真实开源项目负载统计；差异优先级排序可能与真实迁移流量分布有偏差 | 用户 STOP① 知悉，不阻塞本轮，安排后续补 3~5 个真实样本 |
| B5 | 风险登记册「覆盖意图」列部分仍为占位 | 不影响本轮溯源链闭合（用例侧全部可反查），属基线维护债 | 安排本轮后统一回写基线 |

---

## 5. 覆盖盲区结论

- **能力项盲区：无。** 26/26 Parity 项有用例反查；原盲区 B1（Runner OS 多样性）已由 INTENT-COMPAT-054 → COMPAT-RUNSON-01-005/006 闭环（文件已核实存在）。
- **blocker 盲区：无。** 4 个 blocker（RISK-SEC-01/02、RISK-REL-02、RISK-USE-02）均有 P0 用例覆盖，用例文件已逐一核实存在且优先级字段为 P0（REL-NEEDS-01-026/027、USE-DOC-01-002 等已抽验）。
- **残留风险：B2/B3 两项输入退化**（非用例覆盖盲区，属证据强度降级），用户已知悉并安排后续补输入。
- **质量遗留（详见 dod-checklist.md）**：① COMPAT-SECRET-01-005.yaml schema 校验失败且 text/yaml 溯源意图不一致；② SEC-DEFPERM-01-001.md 文本层缺 [负向] 验证点。两项均为基底遗留个案，不影响覆盖结论，但影响 DoD 第 3/5 项判定。
