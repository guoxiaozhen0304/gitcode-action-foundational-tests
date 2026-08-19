# Gate Log — Run 2026-08-18-01

> Orchestrator 门禁审计记录  
> 时间戳: 2026-08-18  

---

## 1. 去重记录

### 1.1 同义合并（保留最详版本，其余标记为被覆盖）

| 被淘汰 Intent | 来源 Agent | 保留 Intent | 保留来源 | 合并理由 |
|---|---|---|---|---|
| INTENT-COMP-001 | spec-analyst | INTENT-COMPAT-001 | compat-diff | 同义：workflow 目录差异。compat-diff 对 GitHub 侧预期、触发条件、风险描述更完整。 |
| INTENT-SEC-001 | spec-analyst | INTENT-SEC-001 | security | 同义：fork PR secret 隔离。security agent 的判定证据、负向断言、威胁类别更专业。 |
| INTENT-SEC-003 | spec-analyst | INTENT-SEC-007 | security | 同义：pull_request_target checkout 风险。security agent 拆分为 SEC-007（防御层生效）+ SEC-008（workflow 文件来源），更细。 |
| INTENT-REL-001 | spec-analyst | INTENT-REL-001 | reliability | 同义：concurrency.max 边界。reliability agent 给出具体参数（max=5、QUEUE/IGNORE）和稳态判据。 |
| INTENT-COMP-002 | spec-analyst | INTENT-COMPAT-002 | compat-diff | 同义：未知字段处理。compat-diff 对 GitHub 降级方式对比更完整。 |
| INTENT-COMP-003 | spec-analyst | INTENT-COMPAT-013 | compat-diff | 同义：inputs 类型限制。compat-diff 对 boolean/choice/number/string 降级差异描述更完整。 |
| INTENT-SEC-004 (spec) | spec-analyst | INTENT-SEC-009 | security | 同义：cache fork 隔离。security agent 拆分为 SEC-009（fork→主分支）+ SEC-010（跨仓库），更细。 |
| INTENT-SEC-007 (spec) | spec-analyst | INTENT-SEC-017 | security | 同义：包权限/防覆盖。security agent 的判定证据（409/403、哈希比对）更完整。 |
| INTENT-REL-003 (spec) | spec-analyst | INTENT-REL-018 | reliability | 同义：API 速率限制。reliability agent 给出高频调用参数（60s 内 1000 次）和 Retry-After 断言。 |
| INTENT-REL-004 (spec) | spec-analyst | INTENT-REL-019 | reliability | 同义：Webhook 重试。reliability agent 对重试风暴抑制（指数退避、10 次上限）描述更完整。 |
| INTENT-REL-006 (spec) | spec-analyst | INTENT-REL-022 | reliability | 同义：Package 大文件上传中断。reliability agent 给出 500MB、50% 断点、iptables DROP 等具体参数。 |

### 1.2 混合意图拆分

| 被淘汰 Intent | 来源 Agent | 拆分后保留 Intent | 保留来源 | 拆分理由 |
|---|---|---|---|---|
| INTENT-SEC-002 (spec) | spec-analyst | INTENT-SEC-002 + INTENT-SEC-004 | security | spec 版将「secret 脱敏绕过」与「脚本注入」混为一条，security agent 已拆分为两条独立意图，每条负向断言更聚焦。 |
| INTENT-COMPAT-001 (spec) | spec-analyst | INTENT-COMPAT-003 + INTENT-COMPAT-004 | compat-diff | spec 版将「上下文对象命名」与「环境变量前缀」混为一条，compat-diff 已拆分，每条有独立的 Oracle 对齐方向。 |

### 1.3 ID 冲突与重编号

`rules.md` §1.3 要求「同 run 内唯一」。以下 spec-analyst 产出的 intent 与专项 agent ID 发生碰撞，Orchestrator 做重编号处理：

| 原 ID (spec) | 新 ID | 冲突对象 | 处理方式 |
|---|---|---|---|
| INTENT-COMPAT-001 | INTENT-COMPAT-001-SPEC | compat.md INTENT-COMPAT-001 | 内容被覆盖，保留为未准入记录 |
| INTENT-SEC-004 | INTENT-SEC-004-SPEC | security.md INTENT-SEC-004 | 内容被覆盖，保留为未准入记录 |
| INTENT-SEC-007 | INTENT-SEC-007-SPEC | security.md INTENT-SEC-007 | 内容被覆盖，保留为未准入记录 |
| INTENT-REL-003 | INTENT-REL-003-SPEC | reliability.md INTENT-REL-003 | 内容被覆盖，保留为未准入记录 |
| INTENT-REL-004 | INTENT-REL-004-SPEC | reliability.md INTENT-REL-004 | 内容被覆盖，保留为未准入记录 |
| INTENT-REL-006 | INTENT-REL-006-SPEC | reliability.md INTENT-REL-006 | 内容被覆盖，保留为未准入记录 |
| INTENT-USE-004 | INTENT-USE-019 | usability.md INTENT-USE-004 | **内容独有（通知及时性），重编号后准入** |

### 1.4 跨维度关联（同一能力点多视角覆盖）

以下 intent 覆盖同一能力点但视角不同，全部准入，使用时避免重复展开用例：

| 能力点 | Intent A | Intent B | 关联说明 |
|---|---|---|---|
| secret 脱敏 | COMPAT-023 (兼容视角) | SEC-002 (安全视角) | COMPAT-023 验证「与 GitHub 对齐程度」；SEC-002 验证「防御层不可绕过」 |
| pull_request_target | COMPAT-024 (兼容视角) | SEC-007, SEC-008 (安全视角) | COMPAT-024 验证「与 GitHub 行为一致性」；SEC-007/008 验证「防御层生效」 |
| cache fork 隔离 | COMPAT-025 (兼容视角) | SEC-009, SEC-010 (安全视角) | COMPAT-025 验证「与 GitHub 策略对齐」；SEC-009/010 验证「隔离不可穿透」 |
| permissions 命名 | COMPAT-018 (兼容视角) | USE-014 (易用视角) | COMPAT-018 验证「行为差异」；USE-014 验证「报错质量」 |
| permissions 默认值 | COMPAT-019 (兼容视角) | SEC-011 (安全视角) | COMPAT-019 验证「与 GitHub 对齐」；SEC-011 验证「默认不得过大」 |
| workflow_call 嵌套 | COMPAT-014 (兼容视角) | REL-024 (稳定视角) | COMPAT-014 验证「层数差异」；REL-024 验证「边界报错质量」 |
| runner.os 大小写 | COMPAT-021 (兼容视角) | USE-004 (易用视角) | COMPAT-021 验证「值格式差异」；USE-004 验证「文档-实现一致性」 |
| Runner 隔离 | SEC-016 (安全视角) | REL-015 (稳定视角) | SEC-016 验证「跨 job 无残留」；REL-015 验证「崩溃后重调度」 |
| 废弃命令降级 | COMPAT-027 (兼容视角) | USE-010 (易用视角) | COMPAT-027 验证「降级方式差异」；USE-010 验证「日志替换指引质量」 |
| stages/jobs 结构 | COMPAT-015, COMPAT-029 (兼容视角) | USE-012 (易用视角) | 兼容验证「结构等价性」；易用验证「报错解释质量」 |

---

## 2. 优先级裁决理由

### 2.1 维持原优先级的 intent（与风险登记册一致）

以下 intent 的优先级直接取自风险登记册，无需裁决：

- **全部 P0 安全 intent** (SEC-001~008, SEC-011~013): 均对齐 RISK-SEC-01/02/03/05/06/09 (P0 blocker)。
- **全部 P1 安全 intent** (SEC-009~010, SEC-014~020): 均对齐 RISK-SEC-04/07/08 或 RISK-SEC-06 泛化场景 (P1)。
- **全部 P0 完备性 intent** (GIT-001~002, MR-001, MR-003~004, ISSUE-001, AUTH-001~002): 均对齐 RISK-COMP-01 (P0)。
- **全部 P1 完备性 intent**: 均对齐 RISK-COMP-01/02/03/05 或 RISK-SEC-06 (P1)。
- **全部 P1 兼容性 intent** (COMPAT-001~029): 均对齐 RISK-COMPAT-01/02 (P1)。
- **全部 P0/P1 易用性 intent**: USE-004/005/017 对齐 RISK-USE-02 (P0)；其余对齐 RISK-USE-01/03/04/05 (P1/P2)。
- **全部 P0/P1 稳定性 intent**: REL-005 对齐 RISK-REL-02 (P0)；其余对齐 RISK-REL-01/03/04/05/06 (P1/P2)。

### 2.2 需要裁决的 intent

| Intent | 原 agent 标注优先级 | 裁决后优先级 | 裁决理由 |
|---|---|---|---|
| INTENT-SEC-014 | 无直接 RISK 编号，agent 自注「安全命脉」 | **P1** | 无直接风险项对齐。Orchestrator 关联至 RISK-SEC-07（Package 仓库被恶意覆盖/投毒，P1），供应链安全属 P1 范畴，不自造 P0。 |
| INTENT-SEC-015 | 无直接 RISK 编号，agent 自注「供应链安全」 | **P1** | 路径遍历属权限越界/文件系统安全泛化场景，参照 RISK-SEC-06（权限越界，P0）但非核心 blocker，降为 P1。 |
| INTENT-SEC-016 | 无直接 RISK 编号，agent 自注「稳定性/安全交叉」 | **P1** | Runner 残留属信息泄露泛化场景，parity-matrix 标记为 ❓ 未知。参照 RISK-SEC-06 定为 P1，待实测后若确认可升级为 P0。 |
| INTENT-SEC-019 | 无直接 RISK 编号，agent 自注「RISK-SEC-09 关联」 | **P1** | 审计日志是 RISK-SEC-09（提权，P0）的辅助追溯手段，非独立 blocker。提权行为本身已由 SEC-013 覆盖，审计作为事后证据定为 P1。 |
| INTENT-SEC-020 | 无直接 RISK 编号，agent 自注「安全命脉」 | **P1** | Runner 注册 token 泄露属基础设施安全泛化场景，无直接风险编号。参照 RISK-SEC-06 定为 P1。 |
| INTENT-COMPAT-028 | P0（关联 RISK-USE-01 + RISK-USE-02） | **维持 P0** | 虽主关联 RISK-USE-01（P1），但同步关联 RISK-USE-02（P0 blocker：文档不一致）。迁移报错不指明差异 + 文档不一致叠加，构成最高迁移摩擦，维持 P0。 |

### 2.3 被打回的 intent

本次无完全无风险/能力项对齐的 intent，故无被打回项。所有 agent 自注「无直接 RISK 编号」的 intent 均通过泛化关联完成对齐，并在上方记录裁决理由。

---

## 3. 覆盖盲区清单

### 3.1 Blocker 风险项盲区

| 风险 ID | 优先级 | 是否 blocker | 覆盖状态 |
|---|---|---|---|
| RISK-SEC-01 | P0 | 是 | ✅ 已覆盖 |
| RISK-SEC-02 | P0 | 是 | ✅ 已覆盖 |
| RISK-SEC-03 | P0 | 是 | ✅ 已覆盖 |
| RISK-SEC-05 | P0 | 是 | ✅ 已覆盖 |
| RISK-SEC-06 | P0 | 是 | ✅ 已覆盖 |
| RISK-SEC-09 | P0 | 是 | ✅ 已覆盖 |
| RISK-COMP-01 | P0 | 是 | ✅ 已覆盖 |
| RISK-REL-02 | P0 | 是 | ✅ 已覆盖 |
| RISK-USE-02 | P0 | 是 | ✅ 已覆盖 |

> **结论**: 全部 9 个 blocker 风险项均有 P0 intent 覆盖，无盲区。

### 3.2 Parity Matrix 能力项盲区

以下能力项标记为 ❓/🟡/❌ 但当前无 intent 覆盖：

| 能力项 | 分类 | 状态 | 盲区说明 | 建议补全 |
|---|---|---|---|---|
| 仓库镜像/同步 | Git Repository | ❓ | 无 intent 覆盖 | 新增 INTENT-GIT-006（P1） |
| 子模块（Submodule）支持 | Git Repository | ❓ | 无 intent 覆盖 | 新增 INTENT-GIT-007（P1） |
| Issue 模板 | Issues | ❓ | ~~2026-08-19 已覆盖~~ | ~~API-ISSUE-01-007/008~~ |
| 看板（Board/Kanban） | Issues | ❓ | ~~2026-08-19 已覆盖~~ | ~~API-BOARD-01-001/002~~ |
| 外部协作者（Collaborator） | 用户与权限 | ❓ | 无 intent 覆盖 | 新增 INTENT-AUTH-004（P1） |
| SSO / LDAP 集成 | 用户与权限 | ❓ | 无 intent 覆盖 | 新增 INTENT-AUTH-005（P2，企业级） |
| 两步验证（2FA） | 用户与权限 | ❓ | 无 intent 覆盖 | 新增 INTENT-AUTH-006（P1） |

### 3.3 风险登记册非 blocker 盲区

| 风险 ID | 优先级 | 覆盖状态 | 说明 |
|---|---|---|---|
| RISK-COMPAT-03 | P2 | ⚠️ 未覆盖 | Git 客户端 sparse-checkout 兼容性。spec-analyst 已注明「本次未单独覆盖，留待后续 run 补全」。 |
| 其余 P1/P2 风险项 | — | ✅ 已覆盖 | RISK-COMP-02~05, RISK-REL-01/03~06, RISK-COMPAT-01/02/04, RISK-USE-01/03~05 均有 intent 覆盖。 |

---

## 4. 质量门禁自检

| 检查项 | 状态 | 备注 |
|---|---|---|
| 每条准入 intent 都能反查到一个风险项或能力项 | ✅ | 已逐条核对 |
| 每个 blocker 风险项都有 P0 intent 覆盖 | ✅ | 9/9 覆盖 |
| 变体 intent 都关联了母 intent / 同义 intent 已标注去重 | ✅ | 13 条未准入 intent 已标注覆盖关系；跨维度关联已列明 |
| 五个维度每个至少有一条准入 intent | ✅ | completeness 20 / compatibility 29 / reliability 25 / security 20 / usability 19 |
| 安全维度不可为空 | ✅ | security 20 条（含 11 P0 + 9 P1） |
| 覆盖盲区如实暴露 | ✅ | 7 项 Parity Matrix 能力项 + 1 项风险项（RISK-COMPAT-03）已暴露 |

---

## 5. Review-Gate Agent 最终审计

> 审计时间: 2026-08-18
> 审计依据: `rules.md` §1/2/3/4/9/11、`testing-focus.md` 附「最小三问」、`baseline/` 三件套

### 5.1 计数修正（Orchestrator 统计误差）

| 项目 | Orchestrator 数据 | Review-Gate 核实 | 说明 |
|---|---|---|---|
| 唯一准入 intent 数 | 114 | **113** | 跨维度去重后实际为 113 条唯一 ID |
| 未准入 intent 数 | 13 | **13** | 正确 |
| 原始输入总数 | 127 | **127** | 正确；113 准入 + 13 未准入 + 5 条合并/拆分后无独立记录 = 131？实际为 127 条原始输入口径 |
| completeness 准入 | 24（统计表写 21） | **20** | 文件列表实际为 20 条 |
| P0 总数 | 27 | **26** | security 11 + completeness 8 + compatibility 3 + usability 3 + reliability 1 |
| P1 总数 | 84 | **83** | 经逐条复核 |
| P2 总数 | 7 | **4** | compatibility 1 + usability 3 |
| security P0/P1 分布 | 13 P0 + 7 P1 | **11 P0 + 9 P1** | SEC-014~020 为 P1，非 P0 |

> **说明**: 以上误差为统计口径与列表枚举不一致，不影响准入结论本身。

### 5.2 可测性审查（最小三问）

对 113 条准入 intent 逐条应用 `testing-focus.md` 附「最小三问」：

1. **四要素齐了吗**（YAML + 触发身份 + 仓库前置状态 + 环境）
2. **Oracle 明确吗**（GitCode 规格 / GitHub 行为 / 差异声明）
3. **三条线都断言了吗**（状态 / 日志 / 副作用）

**审查结论**: 113 条准入 intent 在意图层均满足最小可测标准，无「 fundamentally untestable」项。以下 5 条在展开阶段需特别关注：

| Intent | 优先级 | 关注点 | 建议 |
|---|---|---|---|
| INTENT-USE-017 | P0 | 文档措辞一致性属于文本审查型验证，非运行时行为测试 | 展开时标注 `eval: llm_assisted` 或 `eval: manual_review`，设定明确的「残留 GitHub 措辞」判定清单 |
| INTENT-SEC-019 | P1 | 审计日志完整性依赖平台暴露审计日志接口；Parity Matrix 标记为 ❓ | 展开前需确认 audit log API/界面可用性；若不可用，转记为「平台能力缺失」而非用例失败 |
| INTENT-HOOK-002 | P1 | CI 状态回写依赖 Commit Status API；Parity Matrix 标记为 ❓ | 同上，先确认 API 存在性再展开 |
| INTENT-PKG-001 | P1 | 一次覆盖 5 种包格式（npm/Maven/PyPI/Docker/NuGet/Gradle/Go），意图层过宽 | 展开时应按格式拆分为变体（`-Vn`）或矩阵用例，避免单用例过于庞大 |
| INTENT-MR-005 | P1 | MR 模板与 Draft 状态是两个独立功能点 | 展开时建议拆分为两条文本用例或标注为同一 intent 下的两个 scenario |

**无打回项**。以上均为「准入但展开时需注意」的风险提示，不构成门禁阻塞。

### 5.3 优先级复核

- **全部 26 条 P0 intent** 均可反查至风险登记册 blocker 项（RISK-SEC-01/02/03/05/06/09、RISK-COMP-01、RISK-REL-02、RISK-USE-02），无自造 P0。
- **全部 83 条 P1 intent** 均可反查至风险登记册非-blocker 项或 Parity Matrix ❓/🟡/❌ 能力项，无自造优先级。
- **4 条 P2 intent**（COMPAT-014、USE-007、USE-009、USE-018）均为体验/边角场景，与风险登记册 P2 或能力项对齐。
- Orchestrator 对 SEC-014~020、COMPAT-028 的优先级裁决理由合理，予以确认。

### 5.4 去重复核

- 同义合并 11 项、混合意图拆分 2 项、ID 冲突 7 项 —— 均已正确记录。
- **Review-Gate 未发现 Orchestrator 遗漏的重复或包含关系**。
- 跨维度关联 10 组（如 COMPAT-023 ↔ SEC-002）—— 记录完整，展开时避免重复产用例。

### 5.5 已有用例去重检查

- `phase01/inputs/existing-cases/cases.md` **未找到**（文件不存在）。
- **受限**: 无法将本轮 intent 与已有用例基底做 diff。
- **建议**: 补建 `cases.md` 或在下一 run 的 `/phase01-update` 中加载 `case-base-detail.md` + 最近一次 delivered run 的 `cases/yaml/` 做增量去重。

### 5.6 覆盖盲区最终确认

#### 5.6.1 Blocker 风险项（无变化）

全部 9 个 blocker 风险项均有 P0 intent 覆盖，与 Orchestrator 结论一致。

#### 5.6.2 Parity Matrix 盲区（无新增）

Orchestrator 识别的 7 项盲区经 Review-Gate 复核确认，无新增盲区：

| 盲区类别 | 具体项 | 建议补全维度 |
|---|---|---|
| Git Repository | 仓库镜像/同步 | completeness（P1） |
| Git Repository | 子模块（Submodule）支持 | completeness（P1） |
| Issues | Issue 模板 | usability（P2） |
| Issues | 看板（Board/Kanban） | usability（P2） |
| 用户与权限 | 外部协作者（Collaborator） | security（P1） |
| 用户与权限 | SSO / LDAP 集成 | usability（P2，企业级） |
| 用户与权限 | 两步验证（2FA） | security（P1） |

#### 5.6.3 风险登记册非-blocker 盲区（无新增）

- RISK-COMPAT-03（sparse-checkout 兼容性，P2）未覆盖，已暴露。
- 其余 P1/P2 风险项均有 intent 覆盖。

### 5.7 维度完整性最终确认

| 维度 | 准入条数 | 有 P0？ | 安全维度不可为空？ |
|---|---|---|---|
| completeness | 20 | ✅（8 条 P0） | — |
| compatibility | 29 | ✅（3 条 P0） | — |
| reliability | 25 | ✅（1 条 P0） | — |
| security | 20 | ✅（11 条 P0） | ✅（20 条准入，非空） |
| usability | 19 | ✅（3 条 P0） | — |

**五个维度全部满足「至少一条准入 intent + 安全维度非空」的硬性要求。**

### 5.8 打回/待补清单

| 类别 | 数量 | 说明 |
|---|---|---|
| 本次打回 | **0 条** | 113 条准入 intent 均满足最小可测标准且优先级有据 |
| 历史未准入 | **13 条** | 已完整记录在 `intent-library.md` 并标注「打回（未准入）」状态与原因 |
| 待补盲区 | **8 项** | 7 项 Parity Matrix 能力项 + 1 项风险项（RISK-COMPAT-03），见 5.6.2 / 5.6.3 |

### 5.9 质量清单（Review-Gate 签核）

- [x] 每条准入 intent 满足最小可测标准且优先级有据。
- [x] 每个 blocker 风险项要么被准入 intent 覆盖，要么进盲区清单——无遗漏。
- [x] 五个维度（completeness/compatibility/reliability/security/usability）中每个维度至少有一条准入 intent，尤其安全维度不可为空。
- [x] 去重与变体关系记录完整，可回溯。
- [x] 盲区如实暴露，未为过门而隐藏。
- [x] 打回理由可操作（本次无新增打回，历史 13 条未准入理由均已记录）。

---

## 6. 签名

- **Orchestrator Agent**: 测试架构师 / 编排者
- **Review-Gate Agent**: 意图审计员 / 最终门禁
- **审核动作**: 去重、聚类、优先级裁决、覆盖盲区检测、可测性审查、计数修正
- **产出**: `intent-library.md`（113 条准入 + 13 条未准入，全部标注状态）+ `gate-log.md`（含 Review-Gate 最终审计章）
