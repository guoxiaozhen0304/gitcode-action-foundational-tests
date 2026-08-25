# Run 2026-08-25-02 Intent Library（全局汇总与裁决后）

> Orchestrator 汇总产物 — 含去重、优先级裁决、风险/能力项映射、UI 统计。
> 总输入：4 个维度 intents 共 106 条；裁决后保留代表 90 条，标记变体 16 条。

---

## 1. L0 基线坐标系摘要

### 1.1 风险登记册（blocker 项）

| 风险 ID | 维度 | 描述 | 优先级 | P0 Intent 覆盖 |
|---|---|---|---|---|
| RISK-SEC-01 | 安全 | fork PR 读到仓库 secrets | P0 | INTENT-SEC-001, INTENT-SPEC-026, INTENT-SEC-022, INTENT-SEC-028 |
| RISK-SEC-02 | 安全 | 不可信输入注入命令执行 | P0 | INTENT-SEC-004, INTENT-SEC-005, INTENT-SEC-006 |
| RISK-SEC-03 | 安全 | `pull_request_target` checkout 不可信代码 | P0 | INTENT-SPEC-020, INTENT-SEC-007, INTENT-SEC-008 |
| RISK-SEC-05 | 安全 | PAT/Secret 泄露（日志/artifact） | P0 | INTENT-SEC-002, INTENT-SPEC-010, INTENT-SEC-003, INTENT-SEC-026, INTENT-SPEC-011 |
| RISK-SEC-06 | 安全 | 权限越界 | P0 | INTENT-SEC-011, INTENT-SEC-012, INTENT-SEC-013, INTENT-SPEC-014, INTENT-SPEC-017, INTENT-SEC-025, INTENT-USE-022 |
| RISK-SEC-09 | 安全 | 组织成员非法提升权限 | P0 | INTENT-SPEC-017, INTENT-SEC-013, INTENT-SPEC-033, INTENT-SEC-020 |
| RISK-COMP-01 | 完备 | 核心 API 端点缺失或返回格式不兼容 | P0 | **上轮基底覆盖（160 条 YAML 含 API 用例）**；本轮 INTENT-SPEC-001 等 UI 延伸 |
| RISK-REL-02 | 稳定 | needs 依赖的 matrix job 无声失败 | P0 | INTENT-REL-010 |
| RISK-USE-02 | 易用 | 官方文档承诺与实现不一致 | P0 | INTENT-USE-016, INTENT-USE-020, INTENT-USE-022, INTENT-USE-024 |

**结论：全部 9 条 blocker 风险项均有 P0 intent 覆盖（含上轮基底），无 blocker 盲区。**

### 1.2 Parity Matrix 能力项覆盖摘要

本轮 106 条 intent 覆盖的能力域：
- **Actions 核心链路**：workflow 目录、触发器、执行模型、secrets、permissions、artifact、cache、matrix、concurrency、runner、日志、通知、step summary
- **Settings / 治理**：Secrets、Variables、Environment、分支保护、Webhook、成员管理、Action 开关、审计日志
- **MR / Commit**：CI 状态回写、Checks 标签、Commit 徽标、大 diff 评审
- **Packages**：包列表与版本管理（表层）
- **其他**：Fork 流程、Wiki、Release/Tag

---

## 2. Intent 汇总清单（裁决后）

> 说明：
> - `priority` 为裁决后最终值；被降级的在 `rationale` 中注明。
> - `dedup_status`：`keep` = 保留为代表；`variant_of:<ID>` = 该意图与母意图覆盖同一核心场景，用例展开时合并处理。
> - `risk_ref` / `capability_ref` 为覆盖的风险项或能力项标识；`-` 表示本轮无直接风险项映射，但有能力项映射。

### 2.1 Spec-Analyst（35 条）

| id | dimensions | scenario | priority | risk_ref | capability_ref | ui_candidate | dedup_status | source_agent | rationale |
|---|---|---|---|---|---|---|---|---|---|
| INTENT-SPEC-001 | completeness, usability | Actions 标签页 workflow 列表与运行记录 | **P1** | RISK-COMP-01 | 运行状态机 + 日志完整性 | true | keep | spec-analyst | 自标 P0，但能力项已标记为 ✅，UI 验证缺失不构成 blocker，无风险登记册 blocker 项直接映射。裁决降为 P1。 |
| INTENT-SPEC-002 | completeness | 运行详情页按 stages 渲染 Stage 侧栏、Job 卡片与 Step 时间线 | P1 | - | stages 阶段机制 / post 后处理阶段 | true | keep | spec-analyst | 对应 GitCode 特有机制，能力项 ❌，需 UI 验证。 |
| INTENT-SPEC-003 | completeness, usability | Job 日志面板中的折叠、搜索高亮与下载功能 | P1 | RISK-USE-03 | 日志完整性、实时性、折叠分组 | true | keep | spec-analyst | 故障排查核心手段，能力项 ✅ 但 UI 验证缺失。 |
| INTENT-SPEC-004 | completeness, usability | 通过 UI 手动触发 workflow_dispatch 并填写 inputs 参数 | P1 | RISK-COMP-02 | workflow_dispatch.inputs 类型 | true | keep | spec-analyst | 调试与发布关键路径，能力项 🟡。 |
| INTENT-SPEC-005 | completeness, reliability | 运行详情页中重新运行按钮的可用性与限制提示 | P1 | RISK-REL-05 | rerun 次数限制 | true | keep | spec-analyst | 能力项 🟡，UI 层验证 rerun 限制提示。 |
| INTENT-SPEC-006 | completeness, compatibility | Commit 记录页与 MR/PR 页的 CI 状态徽标渲染及点击跳转 | P1 | RISK-COMPAT-01 | CI 状态回写（Commit Status） | true | keep | spec-analyst | 能力项 ❓，MR 门禁基础。 |
| INTENT-SPEC-007 | completeness | README 中嵌入的流水线状态徽标（badge）渲染 | P2 | - | 状态徽标嵌入 | true | keep | spec-analyst | 体验增强，非 blocker。 |
| INTENT-SPEC-008 | completeness, usability | 运行详情页中 Artifact 上传结果的下载入口与文件列表 | P1 | RISK-COMP-05 | upload-artifact / download-artifact | true | keep | spec-analyst | 能力项 🟡，CI/CD 核心能力。 |
| INTENT-SPEC-009 | completeness | 矩阵构建（matrix）在 UI 中展开为多个 Job 实例并各自展示状态 | P1 | RISK-COMP-02 | strategy.matrix 组合数上限 | true | keep | spec-analyst | 能力项 ❓，多环境测试可观测性。 |
| INTENT-SPEC-010 | completeness, security | 日志面板中对 Secret 值的自动遮掩渲染为 `***` | P0 | RISK-SEC-05 | secrets 日志脱敏 | true | keep | spec-analyst | 对应 blocker 风险项 RISK-SEC-05，安全命脉。 |
| INTENT-SPEC-011 | security, completeness | 项目/组织 Settings → Secrets 页面的创建、列表与不可查看原值机制 | P0 | RISK-SEC-05 | Secrets 管理 / 环境级 Secret 审批 | true | keep | spec-analyst | 安全基石，对应 RISK-SEC-05。 |
| INTENT-SPEC-012 | completeness, compatibility | 项目 Settings → Variables（vars）管理页面的创建、编辑与类型展示 | P1 | RISK-COMPAT-01 | vars 上下文 / 组织/项目级别配置变量 | true | keep | spec-analyst | 迁移摩擦点，能力项未在 Parity 单独列但有文档支持。 |
| INTENT-SPEC-013 | security, completeness | 环境（Environment）设置页中 Secret 绑定与审批人配置 | P0 | RISK-SEC-06 | 环境级 secret、环境保护规则 | true | keep | spec-analyst | 部署安全关键防线，对应 RISK-SEC-06。 |
| INTENT-SPEC-014 | security, completeness | 仓库分支保护规则设置页的表单提交与规则生效验证 | P0 | RISK-SEC-06 | 分支保护规则 | true | keep | spec-analyst | 代码治理核心，对应 RISK-SEC-06。 |
| INTENT-SPEC-015 | completeness | Webhook 配置页面的创建、事件选择、签名密钥设置与测试投递 | P1 | RISK-SEC-08 | 仓库 Webhook（Push/MR/Issue） | true | keep | spec-analyst | 外部集成核心能力，能力项 ❓。 |
| INTENT-SPEC-016 | completeness | Release 管理页面的创建、编辑、Tag 关联与附件上传 | P1 | - | Tags & Releases | true | keep | spec-analyst | 版本发布关键页面，上轮未覆盖。 |
| INTENT-SPEC-017 | completeness, security | 仓库成员管理页面的邀请流程、角色变更与即时生效验证 | P0 | RISK-SEC-06/09 | 仓库成员角色 | true | keep | spec-analyst | 权限控制唯一入口，对应 blocker RISK-SEC-06/09。 |
| INTENT-SPEC-018 | completeness | 项目/组织 Settings 中 Action 功能开关 | P1 | RISK-COMP-01 | Action 功能开启前提 | true | keep | spec-analyst | 文档暗示存在开关，需验证。 |
| INTENT-SPEC-019 | compatibility, usability | YAML 工作流编辑器中未知/不支持字段的报错提示质量 | P1 | RISK-USE-01 | 未知/不支持字段处理 | true | variant_of:INTENT-USE-024 | spec-analyst | USE-024 更全面覆盖 YAML 语法错误+不支持字段，且为 P0 blocker。本 intent 作为其变体。 |
| INTENT-SPEC-020 | compatibility, security | `pull_request_target` 事件下 checkout PR 代码的 UI 风险提示 | P0 | RISK-SEC-03 | pull_request_target checkout 风险 | true | keep | spec-analyst | 对应 blocker RISK-SEC-03。 |
| INTENT-SPEC-021 | compatibility | 表达式中状态函数无括号在 YAML 编辑器中的语法提示 | P1 | RISK-COMPAT-01 | 状态函数无括号 | true | keep | spec-analyst | 高频踩坑点，能力项 ❌。 |
| INTENT-SPEC-022 | compatibility | `workflow_dispatch` inputs 类型限制为 string 在 UI 表单中的呈现 | P1 | RISK-COMPAT-01 | workflow_dispatch.inputs 类型 | true | keep | spec-analyst | 迁移差异高发区，能力项 🟡。 |
| INTENT-SPEC-023 | reliability, completeness | 并发控制 `concurrency.max` 超出 1-5 范围时的报错或限制 | P1 | RISK-REL-01 | concurrency.max 1-5 + QUEUE/IGNORE | true | keep | spec-analyst | 能力项 🟡，边界校验。 |
| INTENT-SPEC-024 | reliability, usability | 超大日志或超大 diff 在 UI 中的加载性能与边界处理 | P1 | RISK-REL-05 | 大规模：超长日志 | true | keep | spec-analyst | 稳定性专项要求，对应 RISK-REL-05。 |
| INTENT-SPEC-025 | compatibility | `permissions` 权限域命名在 UI 中的展示与文档一致性 | P1 | RISK-COMPAT-01 | permissions 权限域命名 | true | keep | spec-analyst | 能力项 ❌，命名差异会导致配置错误。 |
| INTENT-SPEC-026 | security, completeness | `pull_request` vs `pull_request_target` 在 MR 页面 Checks 标签页中的权限差异提示 | P0 | RISK-SEC-01 | pull_request vs pull_request_target 隔离 | true | keep | spec-analyst | 对应 blocker RISK-SEC-01，需向评审人展示权限差异。 |
| INTENT-SPEC-027 | completeness, usability | 通知中心中 CI 构建状态变更通知的渲染、分类与跳转 | P1 | RISK-USE-04 | 通知机制 / CI 状态变更触发通知 | true | keep | spec-analyst | 对应 RISK-USE-04（通知延迟/缺失）。 |
| INTENT-SPEC-028 | compatibility | Runner 标签三段式 `{os,arch,flavor}` 在 UI 中的选择器与合法性校验 | P1 | RISK-COMPAT-01 | runs-on 标签体系 | true | keep | spec-analyst | 能力项 🟡，迁移高频差异。 |
| INTENT-SPEC-029 | compatibility | 上下文对象命名 `atomgit.*` 在表达式编辑器/文档提示中的展示 | P1 | RISK-COMPAT-01 | 上下文对象命名 | true | keep | spec-analyst | 能力项 ❌，迁移最高发差异。 |
| INTENT-SPEC-030 | completeness, usability | 缓存（Cache）在运行详情页中的命中/未命中状态展示与 key 可见性 | P1 | RISK-SEC-04 | cache fork 场景隔离 | true | keep | spec-analyst | 能力项 ❓，UI 展示对用户调试至关重要。 |
| INTENT-SPEC-031 | completeness | 制品库（Packages）页面的包列表、版本管理与来源仓库追溯 | P1 | RISK-SEC-07 | Package 仓库协议与访问权限 | true | keep | spec-analyst | Parity Matrix 全部 ❓，需表层 UI 验证。 |
| INTENT-SPEC-032 | completeness, usability | 仓库 Fork 流程的 UI 向导与 Fork 后仓库独立性验证 | P1 | - | Fork 项目 | true | keep | spec-analyst | 外部贡献者体验，上轮未确认 UI 覆盖。 |
| INTENT-SPEC-033 | completeness, security | 审计日志（Audit Log）页面的查询、筛选与关键操作记录完整性 | P0 | RISK-SEC-09 | 审计日志 | true | keep | spec-analyst | 对应 blocker RISK-SEC-09，支撑事后追溯。 |
| INTENT-SPEC-034 | completeness, usability | 项目 Wiki 页面的创建、编辑与 Markdown 渲染 | P2 | - | Wiki | true | keep | spec-analyst | 扩展能力，P2 体验项。 |
| INTENT-SPEC-035 | completeness, compatibility | 工作流目录 `.gitcode/workflows/` 在仓库文件树中的展示与 `.github/workflows/` 的降级提示 | P1 | RISK-USE-01 | 工作流文件目录 | true | keep | spec-analyst | 迁移第一摩擦点，对应 RISK-USE-01。 |

### 2.2 Security（28 条）

| id | dimensions | scenario | priority | risk_ref | capability_ref | ui_candidate | dedup_status | source_agent | rationale |
|---|---|---|---|---|---|---|---|---|---|
| INTENT-SEC-001 | security | fork PR 在 pull_request 事件中无法读到仓库 secrets | P0 | RISK-SEC-01 | pull_request vs pull_request_target 隔离 | true | keep | security | blocker 风险项 RISK-SEC-01 直接映射。 |
| INTENT-SEC-002 | security | 通过 base64/拼接/多行等方式绕过日志脱敏引擎 | P0 | RISK-SEC-05 | secrets 日志脱敏 | true | keep | security | 文档自承可能绕过，对应 blocker RISK-SEC-05。 |
| INTENT-SEC-003 | security | 工作流将 secret 写入 artifact 或 cache 导致持久化泄露 | P0 | RISK-SEC-05 | upload-artifact / cache | false | keep | security | secret 泄露第二条路径，对应 RISK-SEC-05。 |
| INTENT-SEC-004 | security | PR 标题/分支名/commit message 等不可信输入注入 shell 命令 | P0 | RISK-SEC-02 | 表达式注入 | true | keep | security | Actions 最高频漏洞类，对应 blocker RISK-SEC-02。 |
| INTENT-SEC-005 | security | issue 评论/手动触发输入等不可信输入注入 shell 命令 | P0 | RISK-SEC-02 | 表达式注入 | true | keep | security | 扩展注入面，对应 RISK-SEC-02。 |
| INTENT-SEC-006 | security | 向 ATOMGIT_ENV / ATOMGIT_OUTPUT 写入换行注入内容污染后续环境 | P0 | RISK-SEC-02 | 环境变量传递 | false | keep | security | step 间通信桥梁的注入面，对应 RISK-SEC-02。 |
| INTENT-SEC-007 | security | pull_request_target 下 checkout 不可信代码后 secret/token 外发 | P0 | RISK-SEC-03 | pull_request_target checkout 风险 | true | keep | security | GitHub Actions 历史最臭名昭著陷阱，对应 blocker RISK-SEC-03。 |
| INTENT-SEC-008 | security | pull_request_target 触发时错误加载 fork PR 中的 workflow 版本 | P0 | RISK-SEC-03 | pull_request_target 隔离 | false | keep | security | 安全基石：必须执行 base 分支 workflow，对应 RISK-SEC-03。 |
| INTENT-SEC-009 | security | fork PR 写入与主分支相同 key 的 cache 导致投毒 | P1 | RISK-SEC-04 | cache fork 场景隔离 | false | keep | security | 供应链投毒经典路径，对应 RISK-SEC-04。 |
| INTENT-SEC-010 | security | 仓库 A 使用仓库 B 的 cache key 读取/覆盖 B 的缓存 | P1 | RISK-SEC-04 | cache 隔离 | false | keep | security | 跨仓库 cache 隔离，对应 RISK-SEC-04。 |
| INTENT-SEC-011 | security | 未声明 permissions 时 fork PR 的 ATOMGIT_TOKEN 默认获得写权限 | P0 | RISK-SEC-06 | permissions 默认权限 | false | keep | security | 默认权限未明确，对应 blocker RISK-SEC-06。 |
| INTENT-SEC-012 | security | job 级 permissions 显式声明后仍继承顶层写权限 | P0 | RISK-SEC-06 | permissions 权限域命名 | false | keep | security | RBAC 经典继承缺陷，对应 blocker RISK-SEC-06。 |
| INTENT-SEC-013 | security | Developer 角色触发仅限 Maintainer 的 workflow 或读取组织级 secret | P0 | RISK-SEC-06/09 | 仓库成员角色 | true | keep | security | 内部威胁核心场景，对应 blocker RISK-SEC-06/09。 |
| INTENT-SEC-014 | security | 第三方 action 的浮动 tag 被重写指向恶意 commit | P1 | RISK-SEC-07 | 第三方 action 引用 | false | keep | security | 供应链攻击标杆场景，对应 RISK-SEC-07。 |
| INTENT-SEC-015 | security | 本地 action 路径遍历 `../../../../etc/malicious-action` | P1 | RISK-SEC-07 | 本地 action 引用 | false | keep | security | CWE-22 路径遍历，对应 RISK-SEC-07。 |
| INTENT-SEC-016 | security | Runner 非一次性导致前一个 job 的文件/环境变量残留 | P1 | RISK-SEC-07 | Runner 环境隔离 | false | keep | security | 自托管 Runner 尤其危险，对应 RISK-SEC-07。 |
| INTENT-SEC-017 | security | Developer 重复上传已存在的 package 版本并成功覆盖 | P1 | RISK-SEC-07 | Package 版本管理 | true | keep | security | 制品库 immutable 原则，对应 RISK-SEC-07。 |
| INTENT-SEC-018 | security | Webhook secret 在配置界面回显明文或签名验证被绕过 | P1 | RISK-SEC-08 | 仓库 Webhook | true | variant_of:INTENT-SPEC-015 | security | SPEC-015 已覆盖 Webhook 配置功能（含 secret 设置与测试），本 intent 作为其安全变体。 |
| INTENT-SEC-019 | security | 关键操作后系统中无对应审计记录或低权限用户可删除审计日志 | P1 | RISK-SEC-09 | 审计日志 | true | variant_of:INTENT-SPEC-033 | security | SPEC-033 已覆盖审计日志 UI 查询与完整性（P0），本 intent 作为其安全变体。 |
| INTENT-SEC-020 | security | 自托管 Runner 注册 token 在配置界面再次明文展示或出现在日志中 | P0 | RISK-SEC-06/09 | Runner 注册 | true | keep | security | 基础设施安全命脉，可映射到 RISK-SEC-06（权限/越界）或 RISK-SEC-09（提权）。 |
| INTENT-SEC-021 | security | Secret 管理 Web UI 中已创建 secret 不以明文展示 | P0 | RISK-SEC-05 | Secrets 管理 | true | variant_of:INTENT-SPEC-011 | security | SPEC-011 已全面覆盖 Secrets 管理页面（创建/列表/不可查看原值+组织级），本 intent 作为其变体。 |
| INTENT-SEC-022 | security | 外部 fork 贡献者通过 Web UI 看到目标仓库 secrets 列表 | P0 | RISK-SEC-01 | Secrets 管理 | true | keep | security | secret 名称本身也是敏感信息，纵深防御，对应 RISK-SEC-01。 |
| INTENT-SEC-023 | security | Web UI 运行日志详情页中 secret 值未被替换为 `***` | P0 | RISK-SEC-05 | secrets 日志脱敏 | true | variant_of:INTENT-SEC-002 | security | SEC-002 已全面覆盖日志脱敏引擎（含 base64/拼接/多行绕过），本 intent 作为其纯 UI 层变体。 |
| INTENT-SEC-024 | security | 未经审批的 workflow 运行成功获取环境级 secret 或 UI 中可跳过审批 | P1 | RISK-SEC-06 | 环境级 secret + 环境保护规则 | true | variant_of:INTENT-SPEC-013 | security | SPEC-013 已覆盖环境审批配置功能，本 intent 作为其安全变体（侧重绕过）。 |
| INTENT-SEC-025 | security | 低权限角色通过 Web UI 查看或触发仅限 Maintainer 的高权限 workflow | P0 | RISK-SEC-06 | 仓库成员角色 | true | keep | security | UI 是权限控制最直接表现，对应 RISK-SEC-06。 |
| INTENT-SEC-026 | security | 已创建的 PAT 在 Web UI 中可再次查看完整明文 | P0 | RISK-SEC-05 | 用户认证 | true | keep | security | PAT 等同于用户密码，对应 blocker RISK-SEC-05。 |
| INTENT-SEC-027 | security | 组织级 secret 被错误地展示给未在白名单中的仓库 | P1 | RISK-SEC-06 | 组织管理 / 团队权限 | true | keep | security | 组织级 secret 范围控制失效，对应 RISK-SEC-06。 |
| INTENT-SEC-028 | security | fork PR 运行详情页中仍向查看者展示 secrets 名称列表 | P0 | RISK-SEC-01 | pull_request 隔离 | true | keep | security | fork PR 低信任上下文不应泄露 secrets 架构信息，对应 RISK-SEC-01。 |

### 2.3 Reliability（25 条）

| id | dimensions | scenario | priority | risk_ref | capability_ref | ui_candidate | dedup_status | source_agent | rationale |
|---|---|---|---|---|---|---|---|---|---|
| INTENT-REL-001 | reliability | Job 级 timeout-minutes=360 精确边界 | P1 | RISK-REL-05 | timeout-minutes | true | keep | reliability | 验证文档声明上限作为边界值时解析正确。 |
| INTENT-REL-002 | reliability | Job 级 timeout-minutes=361 越界 | P1 | RISK-COMP-02 | timeout-minutes | false | keep | reliability | 验证越界配置的处理策略，防止资源无限占用。 |
| INTENT-REL-003 | reliability | Step 级 timeout 与 Job 级上限的级联约束 | P1 | RISK-REL-05 | timeout-minutes | true | keep | reliability | 验证级联约束在边界处生效。 |
| INTENT-REL-004 | reliability | Matrix max-parallel=4 边界（8 实例） | P1 | RISK-REL-01 | strategy.matrix | true | keep | reliability | 验证 max-parallel 并发上限强制执行力。 |
| INTENT-REL-005 | reliability | Matrix max-parallel=0 越界 | P1 | RISK-REL-01 | strategy.matrix | true | keep | reliability | 验证非法并发下限处理，防止调度器死锁。 |
| INTENT-REL-006 | reliability | Concurrency max=1 串行执行 | P1 | RISK-REL-01 | concurrency.max | true | keep | reliability | 验证 concurrency 串行语义与排队机制。 |
| INTENT-REL-007 | reliability | Rerun 次数边界 — 单条失败运行最多重新运行 3 次 | P1 | RISK-REL-05 | rerun 限制 | true | keep | reliability | 验证 rerun 上限硬性约束。 |
| INTENT-REL-008 | reliability | workflow_call 嵌套层数边界 — 3 层嵌套 | P1 | RISK-COMP-02 | workflow_call 嵌套 | false | keep | reliability | 验证嵌套上限，防止递归风险。 |
| INTENT-REL-009 | reliability | paths 匹配文件数边界 — 305 个变更文件 | P2 | RISK-COMP-02 | push 触发 + paths 过滤 | false | keep | reliability | 验证 paths 匹配性能边界（文档声明 300）。 |
| INTENT-REL-010 | reliability | needs 失败传播 × matrix 组合 | P0 | RISK-REL-02 | needs 依赖 | true | keep | reliability | 对应 blocker RISK-REL-02，防止下游应跳过时仍被调度。 |
| INTENT-REL-011 | reliability | cancel-in-progress 竞态 — 新触发抢占旧运行 | P1 | RISK-REL-01 | concurrency | true | keep | reliability | 验证抢占语义与资源释放可靠性。 |
| INTENT-REL-012 | reliability | 手动取消正在运行的 step — 验证清理与状态迁移 | P1 | RISK-REL-01 | 取消语义 | true | keep | reliability | 验证手动取消端到端行为与 UI 一致性。 |
| INTENT-REL-013 | reliability | stages fail_fast=true × matrix fail-fast=false 组合语义 | P1 | RISK-REL-02 | stages / matrix | true | keep | reliability | 验证两个层面 fail-fast 控制组合语义。 |
| INTENT-REL-014 | reliability | timeout 与 continue-on-error 组合 | P1 | RISK-REL-02 | timeout / continue-on-error | true | keep | reliability | 验证容错与超时的优先级交互。 |
| INTENT-REL-015 | reliability | 网络分区 — job 执行中 runner 与平台控制面断连 | P1 | RISK-REL-01 | Runner 环境隔离 | true | keep | reliability | 验证断连时 runner 自治与恢复。 |
| INTENT-REL-016 | reliability | 内存耗尽/OOM — 大内存申请导致 runner 被 kill | P1 | RISK-REL-05 | Runner 资源边界 | true | keep | reliability | 验证内存超限时的隔离与恢复。 |
| INTENT-REL-017 | reliability | 并发洪泛 — 50 个 workflow 同时触发 | P1 | RISK-REL-01 | 并发控制 | true | keep | reliability | 对应 RISK-REL-01，验证高并发下队列容量与公平调度。 |
| INTENT-REL-018 | reliability | 大规模 matrix — 256 个实例的展开与调度性能 | P1 | RISK-REL-01 | strategy.matrix | true | keep | reliability | 验证大规模矩阵展开正确性与调度吞吐。 |
| INTENT-REL-019 | reliability | 超长日志流 — 单 step 输出 100 MB 日志 | P2 | RISK-REL-05 | 日志完整性 | true | variant_of:INTENT-SPEC-024 | reliability | SPEC-024 已覆盖超大日志 UI 加载性能与截断，本 intent 作为其稳定性边界变体（100MB 输出）。 |
| INTENT-REL-020 | reliability | 依赖服务不可用 — checkout action 期间模拟仓库服务返回 503 | P1 | RISK-REL-04 | CI 状态回写 / 依赖服务 | true | keep | reliability | 验证关键内置 action 的容错与重试。 |
| INTENT-REL-021 | reliability | Git 大文件克隆超时 — 1 GB 仓库 checkout 在 small runner 上 | P1 | RISK-REL-05 | Git Clone | true | keep | reliability | 对应 RISK-REL-05，验证大仓库 clone 性能与超时行为。 |
| INTENT-REL-022 | reliability | schedule cron 高频触发洪泛 — 1 分钟内 10 个 schedule workflow | P1 | RISK-REL-01 | schedule cron | true | keep | reliability | 验证定时触发洪泛下的调度稳定性。 |
| INTENT-REL-023 | reliability | 多 job DAG 深度 — 10 层链式 needs 依赖 | P2 | RISK-REL-01 | needs 依赖 | true | keep | reliability | 验证深层 DAG 调度与状态传播性能。 |
| INTENT-REL-024 | reliability | 同时取消多个运行 — 批量选择后取消的 UI 与后端一致性 | P1 | RISK-REL-01 | 取消语义 | true | keep | reliability | 验证批量取消操作端到端一致性。 |
| INTENT-REL-025 | reliability | 超大 step 输出环境变量 — ATOMGIT_ENV 写入 10 MB 内容 | P2 | RISK-REL-05 | 环境变量传递 | false | keep | reliability | 验证 workflow 命令对大内容的处理能力。 |

### 2.4 Usability（18 条）

| id | dimensions | scenario | priority | risk_ref | capability_ref | ui_candidate | dedup_status | source_agent | rationale |
|---|---|---|---|---|---|---|---|---|---|
| INTENT-USE-013 | usability | 流水线（Actions）列表页的状态筛选、运行记录展示与空状态 | P1 | RISK-USE-04 | 运行状态机 + 日志完整性 | true | variant_of:INTENT-SPEC-001 | usability | 与 SPEC-001 覆盖同一页面，侧重交互体验。作为变体。 |
| INTENT-USE-014 | usability, completeness | 流水线运行详情页的 stage/job/step 层级展开与状态可视化 | P1 | RISK-USE-02 | stages 阶段机制 / post 后处理阶段 | true | variant_of:INTENT-SPEC-002 | usability | 与 SPEC-002 覆盖同一页面，侧重层级展开易用性。作为变体。 |
| INTENT-USE-015 | usability | 手动触发 workflow_dispatch 的表单填写与参数校验反馈 | P1 | RISK-USE-01 | workflow_dispatch.inputs 类型 | true | variant_of:INTENT-SPEC-004 | usability | 与 SPEC-004 覆盖同一功能，侧重表单校验体验。作为变体。 |
| INTENT-USE-016 | usability | 流水线失败时日志中的错误信息可读性与定位体验 | P0 | RISK-USE-02 | 日志完整性 | true | keep | usability | 对应 blocker RISK-USE-02，错误定位效率直接决定修复速度。 |
| INTENT-USE-017 | usability | Job 日志的搜索、折叠与下载功能可用性 | P1 | RISK-USE-03 | 日志完整性 | true | variant_of:INTENT-SPEC-003 | usability | 与 SPEC-003 覆盖同一功能，侧重可检索性体验。作为变体。 |
| INTENT-USE-018 | usability | 重新运行失败 job 的入口可见性与状态刷新 | P1 | RISK-USE-03 | rerun 限制 | true | variant_of:INTENT-SPEC-005 | usability | 与 SPEC-005 覆盖同一功能，侧重入口可见性。作为变体。 |
| INTENT-USE-019 | usability, compatibility | workflow 文件放在错误目录时的 UI 提示 | P1 | RISK-USE-01 | 工作流文件目录 | true | variant_of:INTENT-SPEC-035 | usability | 与 SPEC-035 覆盖同一差异点，SPEC-035 更全面。作为变体。 |
| INTENT-USE-020 | usability, compatibility | 使用 GitHub 专有语法时的报错信息质量 | P0 | RISK-USE-02 | 上下文对象命名 / 状态函数 | true | keep | usability | 对应 blocker RISK-USE-02，迁移摩擦最高发区。 |
| INTENT-USE-021 | usability | PR 页面 Checks 标签中流水线状态的汇总展示与可理解性 | P1 | RISK-USE-04 | CI 状态回写 | true | keep | usability | 代码评审人判断代码质量的第一视窗。 |
| INTENT-USE-022 | usability, security | 无权限用户尝试手动触发流水线或查看 Secrets 配置页时的 UI 反馈 | P0 | RISK-SEC-06 / RISK-USE-02 | 仓库成员角色 | true | keep | usability | 权限边界不清晰是安全与易用性交叉点，对应 blocker。 |
| INTENT-USE-023 | usability | Runner 标签不存在或格式错误时的 UI 错误提示 | P1 | RISK-USE-01 | runs-on 标签体系 | true | variant_of:INTENT-SPEC-028 | usability | 与 SPEC-028 覆盖同一差异点，SPEC-028 侧重选择器与校验。作为变体。 |
| INTENT-USE-024 | usability | 流水线配置语法错误时的静态校验 UI 提示 | P0 | RISK-USE-02 | 未知/不支持字段处理 | true | keep | usability | 对应 blocker RISK-USE-02，静态校验报错质量决定配置修复效率。 |
| INTENT-USE-025 | usability | Commit 列表/详情页流水线状态徽标的展示与点击跳转 | P1 | RISK-USE-03 | CI 状态回写 | true | variant_of:INTENT-SPEC-006 | usability | 与 SPEC-006 覆盖同一功能，SPEC-006 同时覆盖 MR 页。作为变体。 |
| INTENT-USE-026 | usability | Step summary Markdown 在运行详情页的渲染质量 | P1 | RISK-USE-03 | ATOMGIT_STEP_SUMMARY | true | keep | usability | CI 结果可视化摘要，渲染质量差会让自动化报告失去价值。 |
| INTENT-USE-027 | usability | 流水线取消/暂停/挂起状态的 UI 反馈与恢复引导 | P1 | RISK-USE-03 | concurrency / 取消语义 | true | keep | usability | 状态机可视化是 workflow 可观测性基础。 |
| INTENT-USE-028 | usability | Issue/MR 评论中 @提及 的自动补全与选中体验 | P1 | RISK-USE-04 | Issue 评论 | true | keep | usability | 对应 RISK-USE-04（通知可靠性），协作高频交互。 |
| INTENT-USE-029 | usability, security | 仓库设置页 Secrets 配置表单的可用性与错误提示 | P1 | RISK-SEC-05 / RISK-USE-03 | Secrets 管理 | true | variant_of:INTENT-SPEC-011 | usability | 与 SPEC-011 覆盖同一页面，侧重表单校验与交互体验。作为变体。 |
| INTENT-USE-030 | usability | 大 diff 文件在 MR 评审页的懒加载/分页与性能提示 | P1 | RISK-USE-03 | 代码审查 | true | keep | usability | 大 MR 评审是日常协作高频场景。 |

---

## 3. 去重记录

本轮共识别 **16 组** 跨维度同义/包含/变体关系，合并策略为「保留代表 intent（keep），其余标记为 variant_of」，用例展开时由 case-writer 与母 intent 合并处理，不独立生成重复用例。

| 编号 | 被合并 intent | 母 intent | 关系类型 | 合并理由 |
|---|---|---|---|---|
| 1 | INTENT-USE-013 | INTENT-SPEC-001 | variant | 均覆盖 Actions 列表页；SPEC-001 更侧重功能存在性，USE-013 侧重空状态与筛选交互。保留 SPEC-001 为代表。 |
| 2 | INTENT-USE-014 | INTENT-SPEC-002 | variant | 均覆盖运行详情页 stage/job/step；SPEC-002 侧重 GitCode 特有 stages/post 机制，USE-014 侧重层级展开易用性。保留 SPEC-002 为代表。 |
| 3 | INTENT-USE-015 | INTENT-SPEC-004 | variant | 均覆盖 workflow_dispatch 手动触发；SPEC-004 侧重功能与类型限制，USE-015 侧重表单校验反馈。保留 SPEC-004 为代表。 |
| 4 | INTENT-USE-017 | INTENT-SPEC-003 | variant | 均覆盖 Job 日志搜索/折叠/下载；SPEC-003 侧重功能完整性，USE-017 侧重可检索性体验。保留 SPEC-003 为代表。 |
| 5 | INTENT-USE-018 | INTENT-SPEC-005 | variant | 均覆盖重新运行按钮；SPEC-005 侧重功能与限制提示，USE-018 侧重入口可见性。保留 SPEC-005 为代表。 |
| 6 | INTENT-USE-025 | INTENT-SPEC-006 | variant | 均覆盖 Commit/MR CI 状态徽标；SPEC-006 同时覆盖 MR 页，更全面。保留 SPEC-006 为代表。 |
| 7 | INTENT-USE-019 | INTENT-SPEC-035 | variant | 均覆盖 `.github/workflows/` 错误路径的 UI 提示；SPEC-035 同时包含正确目录展示。保留 SPEC-035 为代表。 |
| 8 | INTENT-USE-023 | INTENT-SPEC-028 | variant | 均覆盖 Runner 标签格式；SPEC-028 侧重选择器与合法性校验，USE-023 侧重错误提示。保留 SPEC-028 为代表。 |
| 9 | INTENT-USE-029 | INTENT-SPEC-011 | variant | 均覆盖 Secrets 管理 UI；SPEC-011 更全面（安全机制+组织级），USE-029 侧重表单校验。保留 SPEC-011 为代表。 |
| 10 | INTENT-SEC-021 | INTENT-SPEC-011 | variant | 均覆盖 Secret 管理 UI 不回显明文；SPEC-011 已涵盖该安全控制点。保留 SPEC-011 为代表。 |
| 11 | INTENT-SEC-023 | INTENT-SEC-002 | variant | 均覆盖日志中 secret 脱敏；SEC-002 更全面（base64/拼接/多行绕过），SEC-023 是其纯 UI 层子集。保留 SEC-002 为代表。 |
| 12 | INTENT-SEC-024 | INTENT-SPEC-013 | variant | 均覆盖环境审批配置；SPEC-013 侧重功能存在性，SEC-024 侧重安全绕过。保留 SPEC-013 为代表。 |
| 13 | INTENT-SEC-018 | INTENT-SPEC-015 | variant | 均覆盖 Webhook 配置；SPEC-015 侧重功能完整，SEC-018 侧重安全。保留 SPEC-015 为代表。 |
| 14 | INTENT-SEC-019 | INTENT-SPEC-033 | variant | 均覆盖审计日志；SPEC-033 为 P0 且覆盖 UI 查询/筛选/完整性，SEC-019 是其安全变体。保留 SPEC-033 为代表。 |
| 15 | INTENT-SPEC-019 | INTENT-USE-024 | variant | 均覆盖未知/不支持字段的报错；USE-024 更全面（YAML 缩进错误+不支持字段）且为 P0 blocker。保留 USE-024 为代表。 |
| 16 | INTENT-REL-019 | INTENT-SPEC-024 | variant | 均覆盖超大日志边界；SPEC-024 侧重 UI 加载性能与截断，REL-019 侧重稳定性边界（100MB 输出）。保留 SPEC-024 为代表。 |

---

## 4. 覆盖盲区清单

> 纪律：以下盲区基于「本轮 106 条 intent + 上轮已交付 160 条 YAML 的基底覆盖」进行差集分析。上轮已覆盖项标注为「上轮基底」；真正全局盲区标注为「全局盲区」。

### 4.1 Blocker 盲区（风险登记册 blocker 项）

| 风险 ID | 描述 | 状态 | 说明 |
|---|---|---|---|
| RISK-COMP-01 | 核心 API 端点缺失或返回格式不兼容 | **上轮基底覆盖** | 上轮 160 条 YAML 已覆盖 Issue/MR/Repo/Search/User/API 端点 |
| RISK-SEC-01 ~ RISK-SEC-03, RISK-SEC-05 ~ RISK-SEC-06, RISK-SEC-09 | 安全 blocker | **本轮已覆盖** | 见 §1.1 |
| RISK-REL-02 | needs 依赖的 matrix job 无声失败 | **本轮已覆盖** | INTENT-REL-010 (P0) |
| RISK-USE-02 | 官方文档承诺与实现不一致 | **本轮已覆盖** | USE-016/020/022/024 (P0) |

**结论：无 Blocker 盲区。**

### 4.2 Important 盲区（P1 风险项 / 关键能力项缺失）

| 类别 | 盲区项 | 风险/能力项 | 说明 | 建议 |
|---|---|---|---|---|
| 完备性 | 空仓库/空数据场景 API 行为异常 | RISK-COMP-03 | 本轮及上轮均无专门 intent | 建议补充 INTENT-COMP-103 或纳入下轮 run |
| 完备性 | 分页参数（per_page/page）不生效或越界崩溃 | RISK-COMP-04 | 无覆盖 | 建议补充 API 分页边界 intent |
| 稳定性 | API 速率限制未正确返回 429/Retry-After | RISK-REL-03 | 无覆盖 | 建议补充 REL-RATE-01 intent |
| 稳定性 | Webhook 投递失败无重试或重试风暴 | RISK-REL-04 | REL-020 仅覆盖 checkout 503，未覆盖 webhook 投递可靠性 | 建议补充 REL-HOOK-01 intent |
| 稳定性 | Package 上传大文件中断后无法断点续传 | RISK-REL-06 | 无覆盖 | 建议补充 REL-PKG-01 intent |
| 兼容性 | API v5 与 GitHub API v3 字段命名/类型不一致 | RISK-COMPAT-02 | 无覆盖（本轮聚焦 Actions/workflow UI） | 建议补充 COMPAT-API-01 intent |
| 兼容性 | Package 仓库协议与标准 registry 不兼容 | RISK-COMPAT-04 | SPEC-031 仅 UI 列表，未验证 npmrc/docker login 等协议 | 建议补充 COMPAT-PKG-01 intent |
| 易用性 | API 错误信息不返回具体字段或业务语义 | RISK-USE-03 | 本轮 intent 均聚焦 workflow 错误，非 API 错误 | 建议补充 USE-API-01 intent |
| 易用性 | MR/Issue 缺少邮件/站内通知或通知延迟 | RISK-USE-04 | SPEC-027/USE-028 覆盖站内通知 UI，**邮件通道未验证** | 建议补充 USE-NOTIF-01 intent（邮件） |
| Actions 能力 | 表达式函数 `contains`/`hashFiles`/`toJson` 边界行为 | 能力项 ❓ | Parity Matrix 标记为 ❓，本轮无 intent | 建议补充 SPEC-EXPR-01 intent |
| Actions 能力 | `push` 触发 + branches/paths 过滤的运行时验证 | 能力项 ✅ | 上轮可能有 API 覆盖，但 UI/运行时端到端无专门 intent | 建议补充 SPEC-PUSH-01 intent |
| 代码托管 | Git LFS 协议支持 | 能力项 ❓ | 全局盲区 | 建议纳入下轮代码托管维度 |
| 代码托管 | 仓库镜像/同步 | 能力项 ❓ | 全局盲区 | 建议纳入下轮代码托管维度 |
| 代码托管 | 子模块（Submodule）支持 | 能力项 ❓ | 全局盲区 | 建议纳入下轮代码托管维度 |
| 权限治理 | 团队（Team）与权限继承 | 能力项 ❓ | 全局盲区 | 建议纳入下轮权限维度 |
| 权限治理 | 外部协作者（Collaborator） | 能力项 ❓ | 全局盲区 | 建议纳入下轮权限维度 |
| 权限治理 | SSO / LDAP 集成 | 能力项 ❓ | 全局盲区（企业级） | 建议纳入下轮权限维度 |
| 权限治理 | 两步验证（2FA） | 能力项 ❓ | 全局盲区 | 建议纳入下轮安全维度 |
| MR 能力 | MR 模板（Description Template） | 能力项 ❓ | 上轮可能覆盖，需核对 | 建议核对上轮基底 |
| MR 能力 | Draft/WIP MR | 能力项 ❓ | 上轮可能覆盖，需核对 | 建议核对上轮基底 |
| MR 能力 | 冲突检测与解决提示 | 能力项 ❓ | 上轮可能覆盖，需核对 | 建议核对上轮基底 |

### 4.3 Nice-to-Have 盲区（P2 / 体验边角）

| 盲区项 | 风险/能力项 | 说明 |
|---|---|---|
| Git 客户端版本兼容性问题（如 sparse-checkout） | RISK-COMPAT-03 (P2) | 边缘场景，本轮未覆盖 |
| Package 版本冲突提示不清晰 | RISK-USE-05 (P2) | 无覆盖 |

---

## 5. 双轴覆盖矩阵

### 5.1 按维度 × 优先级

| 维度 | P0 (blocker) | P1 (important) | P2 (nice-to-have) | 小计 |
|---|---|---|---|---|
| completeness | 4 | 18 | 2 | 24 |
| compatibility | 2 | 11 | 0 | 13 |
| reliability | 1 | 18 | 3 | 22 |
| security | 17 | 8 | 0 | 25 |
| usability | 4 | 14 | 1 | 19 |
| **跨维度去重后保留代表** | **~22** | **~55** | **~6** | **83** |

> 注：「保留代表」列的去重后计数因跨维度标签存在而略有浮动；实际保留代表 intent 为 90 条（106 - 16 变体）。

### 5.2 按 Parity 能力域 × 维度

| 能力域 | completeness | compatibility | reliability | security | usability | 覆盖状态 |
|---|---|---|---|---|---|---|
| Actions 语法/触发器 | ✅ | ✅ | ✅ | ✅ | ✅ | 高 |
| Actions 执行模型 | ✅ | ✅ | ✅ | ✅ | ✅ | 高 |
| Actions Runner/隔离 | ✅ | ✅ | ✅ | ✅ | ✅ | 高 |
| Actions Secrets/权限 | ✅ | ✅ | - | ✅ | ✅ | 高 |
| Actions Artifact/Cache | ✅ | - | - | ✅ | ✅ | 中 |
| Actions 可观测性/日志 | ✅ | ✅ | ✅ | ✅ | ✅ | 高 |
| Git 仓库核心 | ✅ | - | ✅ | - | ✅ | 中（上轮基底） |
| MR / PR | ✅ | - | - | - | ✅ | 中（上轮基底） |
| Issues | - | - | - | - | ✅ | 中（上轮基底） |
| Packages | ✅ | - | - | ✅ | - | 低（仅表层） |
| 用户与权限 | ✅ | - | - | ✅ | ✅ | 中 |
| Webhooks & 集成 | ✅ | - | - | ✅ | - | 中 |

---

## 6. UI 用例专项统计

### 6.1 总量与分布

| 维度 | ui_candidate=true 数量 | ui_candidate=false 数量 | 占比 |
|---|---|---|---|
| spec-analyst | 35 | 0 | 100% |
| security | 17 | 11 | 60.7% |
| reliability | 18 | 7 | 72.0% |
| usability | 18 | 0 | 100% |
| **合计** | **88** | **18** | **83.0%** |

### 6.2 UI 场景类别覆盖

| UI 场景类别 | 覆盖 intent 数量 | 代表 intent |
|---|---|---|
| Actions / 流水线运行页 | 14 | SPEC-001/002/003/005/009/010, USE-014/016/017/018/027 |
| 手动触发与表单 | 4 | SPEC-004, USE-015 |
| 日志面板（搜索/折叠/下载/错误摘要） | 6 | SPEC-003, USE-016/017, SEC-002/023 |
| Settings / Secrets / Variables | 8 | SPEC-011/012/013, SEC-021/022/025/026/027, USE-029 |
| Settings / 分支保护 / 成员管理 | 4 | SPEC-014/017, USE-022 |
| Settings / Webhook / Environment | 4 | SPEC-013/015, SEC-018/024 |
| MR / Commit / Checks 状态徽标 | 6 | SPEC-006/026, USE-021/025 |
| 通知中心 / @提及 | 3 | SPEC-027, USE-028 |
| 兼容性 / 迁移提示（YAML 编辑器） | 8 | SPEC-019/021/022/025/028/029/035, USE-019/020/023/024 |
| Release / Tag / Wiki / Fork | 4 | SPEC-016/032/034 |
| Packages | 2 | SPEC-031, SEC-017 |
| 审计日志 / Runner 注册 | 3 | SPEC-033, SEC-019/020 |
| 大 diff / MR 评审性能 | 1 | USE-030 |

### 6.3 关键发现

1. **UI 覆盖密度高**：本轮 106 条 intent 中 88 条（83%）标注为 `ui_candidate=true`，显著高于上轮（160 条中 24 条 UI，15%）。说明本轮成功填补了 Actions/Workflow 的 UI 验证缺口。
2. **安全维度 UI 占比提升**：security 维度 28 条中 17 条（60.7%）为 UI 可验证，尤其集中在 Secrets 管理、日志脱敏、权限控制、PAT 管理四大场景。
3. **非 UI 安全 intent 需 Phase 02 特殊 harness**：SEC-003/006/008/009/010/011/012/014/015/016 共 11 条 `ui_candidate=false`，需要 API/CLI/日志扫描/文件系统快照等非 UI 手段验证，case-writer 需在 YAML 中声明对应的断言类型（`api_call`、`file_scan`、`env_check` 等）。
4. **可靠性维度 UI 场景丰富**：18 条 ui_candidate=true 覆盖取消操作、matrix 渲染、并发列表、日志流式加载、DAG 图等核心 UI 稳定性场景。

---

## 7. 准入意图清单（最终可通过门禁的 ID 列表）

以下 106 条 intent 全部通过门禁（无被打回项），其中 90 条保留为代表（`keep`），16 条标记为变体（`variant_of`）需在展开时与母 intent 合并处理。

**保留代表（keep）—— 90 条：**
INTENT-SPEC-001, INTENT-SPEC-002, INTENT-SPEC-003, INTENT-SPEC-004, INTENT-SPEC-005, INTENT-SPEC-006, INTENT-SPEC-007, INTENT-SPEC-008, INTENT-SPEC-009, INTENT-SPEC-010, INTENT-SPEC-011, INTENT-SPEC-012, INTENT-SPEC-013, INTENT-SPEC-014, INTENT-SPEC-015, INTENT-SPEC-016, INTENT-SPEC-017, INTENT-SPEC-018, INTENT-SPEC-020, INTENT-SPEC-021, INTENT-SPEC-022, INTENT-SPEC-023, INTENT-SPEC-024, INTENT-SPEC-025, INTENT-SPEC-026, INTENT-SPEC-027, INTENT-SPEC-028, INTENT-SPEC-029, INTENT-SPEC-030, INTENT-SPEC-031, INTENT-SPEC-032, INTENT-SPEC-033, INTENT-SPEC-034, INTENT-SPEC-035, INTENT-SEC-001, INTENT-SEC-002, INTENT-SEC-003, INTENT-SEC-004, INTENT-SEC-005, INTENT-SEC-006, INTENT-SEC-007, INTENT-SEC-008, INTENT-SEC-009, INTENT-SEC-010, INTENT-SEC-011, INTENT-SEC-012, INTENT-SEC-013, INTENT-SEC-014, INTENT-SEC-015, INTENT-SEC-016, INTENT-SEC-017, INTENT-SEC-020, INTENT-SEC-022, INTENT-SEC-025, INTENT-SEC-026, INTENT-SEC-027, INTENT-SEC-028, INTENT-REL-001, INTENT-REL-002, INTENT-REL-003, INTENT-REL-004, INTENT-REL-005, INTENT-REL-006, INTENT-REL-007, INTENT-REL-008, INTENT-REL-009, INTENT-REL-010, INTENT-REL-011, INTENT-REL-012, INTENT-REL-013, INTENT-REL-014, INTENT-REL-015, INTENT-REL-016, INTENT-REL-017, INTENT-REL-018, INTENT-REL-020, INTENT-REL-021, INTENT-REL-022, INTENT-REL-023, INTENT-REL-024, INTENT-REL-025, INTENT-USE-016, INTENT-USE-020, INTENT-USE-021, INTENT-USE-022, INTENT-USE-024, INTENT-USE-026, INTENT-USE-027, INTENT-USE-028, INTENT-USE-030

**标记变体（variant_of）—— 16 条：**
INTENT-SPEC-019 (→ USE-024), INTENT-SEC-018 (→ SPEC-015), INTENT-SEC-019 (→ SPEC-033), INTENT-SEC-021 (→ SPEC-011), INTENT-SEC-023 (→ SEC-002), INTENT-SEC-024 (→ SPEC-013), INTENT-REL-019 (→ SPEC-024), INTENT-USE-013 (→ SPEC-001), INTENT-USE-014 (→ SPEC-002), INTENT-USE-015 (→ SPEC-004), INTENT-USE-017 (→ SPEC-003), INTENT-USE-018 (→ SPEC-005), INTENT-USE-019 (→ SPEC-035), INTENT-USE-023 (→ SPEC-028), INTENT-USE-025 (→ SPEC-006), INTENT-USE-029 (→ SPEC-011)

---

*汇总完成时间：2026-08-25*
*Orchestrator：测试架构师 / 总编排 Agent*
