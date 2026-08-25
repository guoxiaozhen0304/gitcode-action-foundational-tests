# Spec-Analyst Intents — Run 2026-08-25-02（增量）

> 本文件为 Run `2026-08-25-02` 的增量 test intent，由 spec-analyst 基于 `inputs/gitcode-spec/` 全部文档、`testing-focus.md`、`baseline/parity-matrix.md`、`baseline/risk-register.md` 及 `rules.md` 生成。
> 
> **增量原则**：上轮 Run `2026-08-25-01` 已交付 160 条 YAML（含 24 条 UI 用例），覆盖 Issue/MR/Repo/Search/User/Nav/Board/Code/Org 等通用页面。本轮重点填补 **Actions/Workflow 相关 UI 验证**、**Settings 治理页面**、以及 Parity Matrix 中标记为「部分/不支持/未知」的能力项。

---

## 1. Actions / Workflow 运行 UI（上轮零覆盖，本轮核心增量）

### INTENT-SPEC-001
- **id**: INTENT-SPEC-001
- **dimensions**: [completeness, usability]
- **scenario**: 在项目主页 Actions 标签页查看 workflow 列表与运行记录
- **capability**: 运行状态机 + 日志完整性（Parity Matrix: ✅，但 UI 验证缺失）
- **priority**: P0
- **oracle**: GitCode 规格（`view-run-results.md` §入口一）
- **ui_candidate**: true
- **rationale**: 规格声明运行状态包括 queued→in_progress→completed(success/failure/cancelled/skipped)，且 Actions 标签页是用户查看 workflow 的核心入口。上轮无 UI 用例覆盖 Actions 页面，存在重大场景遗漏。
- **expected_behavior**: Actions 标签页左侧列出所有 workflow 名称；右侧展示运行列表，每条记录显示触发事件、分支/标签、状态徽标、运行编号、触发人、耗时；点击状态筛选（成功/失败/运行中/取消/跳过）后列表即时刷新。

### INTENT-SPEC-002
- **id**: INTENT-SPEC-002
- **dimensions**: [completeness]
- **scenario**: 运行详情页按 stages 顺序渲染 Stage 侧栏、Job 卡片与 Step 时间线
- **capability**: `stages` 阶段机制 / `post` 后处理阶段（Parity Matrix: ❌ GitCode 特有）
- **priority**: P1
- **oracle**: GitCode 规格（`workflow-job-step-action.md`、`view-run-results.md`）
- **ui_candidate**: true
- **rationale**: `stages` 与 `post` 是 GitCode 特有机制（非 GitHub 兼容能力），文档声明阶段间串行、阶段内并行、`fail_fast` 可中断、`post` 默认 `run_always: true`。这些语义必须在 UI 上正确呈现，否则用户无法理解运行编排结构。
- **expected_behavior**: 详情页按 `stages` 定义顺序纵向排列；Stage 侧栏标注状态（成功/失败/跳过）；Job 卡片展示名称、Runner 标签、耗时、状态；展开 Job 后逐 step 显示执行耗时与结果；若定义了 `post` 阶段，在主流程后单独展示 Post 区域。

### INTENT-SPEC-003
- **id**: INTENT-SPEC-003
- **dimensions**: [completeness, usability]
- **scenario**: Job 日志面板中的折叠、搜索高亮与下载功能
- **capability**: 日志完整性、实时性、折叠分组（`testing-focus.md` §9）
- **priority**: P1
- **oracle**: GitCode 规格（`view-job-logs.md`）
- **ui_candidate**: true
- **rationale**: 日志是故障排查的唯一手段。规格声明日志支持折叠、搜索高亮、下载为 UTF-8 文本；长输出 step 默认折叠关键区间。需验证 UI 实际渲染质量。
- **expected_behavior**: 点击 Job 卡片展开 step 时间线；点击 step 行后右侧面板展示完整标准输出与标准错误；日志面板顶部支持关键词搜索并高亮匹配行；长输出 step 默认折叠，点击可展开；右上角「下载日志」按钮可获取完整日志文件。

### INTENT-SPEC-004
- **id**: INTENT-SPEC-004
- **dimensions**: [completeness, usability]
- **scenario**: 通过 UI 手动触发 workflow_dispatch 并填写 inputs 参数
- **capability**: `workflow_dispatch` 触发 + inputs 类型限制（Parity Matrix: 🟡 仅支持 string）
- **priority**: P1
- **oracle**: GitCode 规格（`manually-trigger-pipeline.md`）
- **ui_candidate**: true
- **rationale**: 手动触发是调试与发布的关键路径。文档声明 inputs 仅支持 `string` 类型，触发表单中有分支选择下拉框。需验证 UI 是否如实限制类型、是否展示 description/required/default，以及分支选择是否生效。
- **expected_behavior**: Actions 标签页中，仅 `on` 包含 `workflow_dispatch` 的 workflow 显示「Run workflow」按钮；点击后弹出表单，展示各 input 的 description、required 标记、default 值；类型仅提供文本输入（因规格仅支持 string）；分支选择下拉框默认为默认分支，可切换为任意分支；提交后触发新运行并跳转至运行详情页。

### INTENT-SPEC-005
- **id**: INTENT-SPEC-005
- **dimensions**: [completeness, reliability]
- **scenario**: 运行详情页中重新运行按钮的可用性与限制提示
- **capability**: `rerun` 次数限制 / 超时运行不可 rerun（Parity Matrix: 🟡）
- **priority**: P1
- **oracle**: GitCode 规格（`rerun-failed-jobs.md`）
- **ui_candidate**: true
- **rationale**: 文档声明单条运行最多重新运行 3 次，超过 6 小时的运行不可重新运行。UI 需在按钮置灰时给出明确限制提示，否则用户会困惑为何无法 rerun。
- **expected_behavior**: 运行详情页右上角展示「Re-run all jobs」与「Re-run failed jobs」按钮； rerun 次数已达 3 次或运行超 6 小时，按钮置灰并提示具体限制原因；重新运行后创建新运行记录，运行编号递增。

### INTENT-SPEC-006
- **id**: INTENT-SPEC-006
- **dimensions**: [completeness, compatibility]
- **scenario**: Commit 记录页与 MR/PR 页的 CI 状态徽标渲染及点击跳转
- **capability**: CI 状态回写（Commit Status / Check Run）（Parity Matrix: ❓）
- **priority**: P1
- **oracle**: GitCode 规格（`view-run-results.md` §入口二/三）
- **ui_candidate**: true
- **rationale**: CI 状态回写是 MR 门禁的基础。规格声明 Commits 页面每条提交记录右侧显示精简状态徽标，PR 页面的 Checks 标签页汇总流水线运行结果。需验证徽标是否实时回写、状态是否与运行结果一致。
- **expected_behavior**: Commits 页面每条提交右侧显示状态徽标（成功/失败/运行中）；点击徽标跳转至对应运行详情；MR 详情页存在 Checks 标签页，汇总该 PR 触发的所有 workflow 运行结果及状态。

### INTENT-SPEC-007
- **id**: INTENT-SPEC-007
- **dimensions**: [completeness]
- **scenario**: README 中嵌入的流水线状态徽标（badge）在仓库首页正确渲染
- **capability**: 状态徽标嵌入（`view-run-results.md` §状态徽标嵌入）
- **priority**: P2
- **oracle**: GitCode 规格
- **ui_candidate**: true
- **rationale**: Badge 是项目质量可视化的常见手段。文档提供 badge URL 格式，需验证其在仓库 README 渲染页中是否正常显示 SVG 徽标。
- **expected_behavior**: 仓库首页 README 区域中，若包含 `![Build Status](https://atomgit.com/{owner}/{repo}/badges/{workflow_name}/pipeline.svg)` 语法，应渲染为对应状态的 SVG 徽标；运行状态变更后，刷新页面徽标同步更新。

### INTENT-SPEC-008
- **id**: INTENT-SPEC-008
- **dimensions**: [completeness, usability]
- **scenario**: 运行详情页中 Artifact 上传结果的下载入口与文件列表
- **capability**: `upload-artifact` / `download-artifact`（Parity Matrix: 🟡）
- **priority**: P1
- **oracle**: GitCode 规格（`upload-download-artifacts.md`）
- **ui_candidate**: true
- **rationale**: Artifact 跨 job 传递是 CI/CD 的核心能力。文档声明支持上传/下载制品，但保留期与大小上限未公开。UI 需提供明确的下载入口，否则用户无法获取构建产物。
- **expected_behavior**: 运行详情页（或关联 tab）展示本次运行产生的 Artifact 列表，包含名称、大小；提供下载按钮，点击可获取对应 artifact 压缩包；Artifact 保留期到达后列表自动清空或显示过期提示。

### INTENT-SPEC-009
- **id**: INTENT-SPEC-009
- **dimensions**: [completeness]
- **scenario**: 矩阵构建（matrix）在 UI 中展开为多个 Job 实例并各自展示状态
- **capability**: `strategy.matrix` 组合数上限（Parity Matrix: ❓ 未公开上限）
- **priority**: P1
- **oracle**: GitCode 规格（`configure-matrix-builds.md`）
- **ui_candidate**: true
- **rationale**: Matrix 展开正确性直接影响多环境测试的可观测性。文档说明 matrix 变量组合生成多个 job 实例，`fail-fast` 和 `max-parallel` 控制行为。UI 需清晰展示每个实例的状态与日志隔离。
- **expected_behavior**: 运行详情页中，matrix job 展开为多个子任务卡片，每个卡片标注具体矩阵变量值（如 os=ubuntu-latest, node-version=18）；任一实例失败时，若 `fail-fast: true`，其余实例显示「已取消」状态；各实例日志独立可展开。

### INTENT-SPEC-010
- **id**: INTENT-SPEC-010
- **dimensions**: [completeness, security]
- **scenario**: 日志面板中对 Secret 值的自动遮掩渲染为 `***`
- **capability**: `secrets` 日志脱敏 `***`（Parity Matrix: 🟡，文档自承可能绕过）
- **priority**: P0
- **oracle**: GitCode 规格（`using-secrets.md`、`view-job-logs.md`）
- **ui_candidate**: true
- **rationale**: 对应风险登记册 RISK-SEC-05（PAT 泄露日志/artifact）。文档声明 Secret 值在日志中自动替换为 `***`，且无法在界面查看原值。这是安全命脉，必须在 UI 层验证。
- **expected_behavior**: 日志面板中，任何包含 Secret 值的输出行均显示为 `***`；用户无法在 UI 中通过悬停、复制或下载日志绕过遮掩；Secret 名称可正常显示，仅值被替换。

---

## 2. Settings / Governance UI（上轮部分覆盖，增量补齐）

### INTENT-SPEC-011
- **id**: INTENT-SPEC-011
- **dimensions**: [security, completeness]
- **scenario**: 项目/组织 Settings → Secrets 页面的创建、列表与不可查看原值机制
- **capability**: Secrets 管理 / 环境级 Secret 审批（Parity Matrix: 🟡）
- **priority**: P0
- **oracle**: GitCode 规格（`using-secrets.md`）
- **ui_candidate**: true
- **rationale**: Secret 管理是安全基石。文档声明创建后无法在界面查看原值，只能更新覆盖；支持项目级与组织级 Secret。需验证 UI 是否严格禁止回显 Secret 值。
- **expected_behavior**: Secrets 设置页列出所有 Secret 名称，但 Value 列仅显示为 `***` 或空，不提供「查看」按钮；编辑 Secret 时表单不提供原值回显，仅允许输入新值覆盖；组织级 Secret 与项目级 Secret 分开展示或标注来源。

### INTENT-SPEC-012
- **id**: INTENT-SPEC-012
- **dimensions**: [completeness, compatibility]
- **scenario**: 项目 Settings → Variables（vars）管理页面的创建、编辑与类型展示
- **capability**: `vars` 上下文 / 组织/项目级别配置变量（`context.md`）
- **priority**: P1
- **oracle**: GitCode 规格（`syntax-reference/context.md`）
- **ui_candidate**: true
- **rationale**: `vars` 是除 `secrets` 外另一关键配置变量机制，用于非敏感配置。文档声明支持组织、仓库和环境级别设置，但 UI 管理页面的可达性与功能完整性未验证。
- **expected_behavior**: 项目设置中存在「变量」或「Variables」标签页；支持创建、编辑、删除变量；变量值在 UI 中可明文查看（区别于 Secret）；变量按作用域（仓库/环境）分组展示。

### INTENT-SPEC-013
- **id**: INTENT-SPEC-013
- **dimensions**: [security, completeness]
- **scenario**: 环境（Environment）设置页中 Secret 绑定与审批人（reviewers/wait timer）配置
- **capability**: 环境级 secret、环境保护规则（`testing-focus.md` §5）
- **priority**: P0
- **oracle**: GitCode 规格（`using-secrets.md` §环境审批）
- **ui_candidate**: true
- **rationale**: 环境级 Secret + 审批规则是部署安全的关键防线。文档提到「环境级 Secret 可配置审批人，未经审批 job 不可访问」。需验证 UI 是否支持配置审批人及等待时间。
- **expected_behavior**: 环境设置页支持创建环境（如 production/staging）；可为环境绑定 Secret 和变量；支持配置审批人列表（用户名/团队）；支持配置 wait timer（等待时间）；未通过审批的运行在 UI 中显示「等待审批」状态。

### INTENT-SPEC-014
- **id**: INTENT-SPEC-014
- **dimensions**: [security, completeness]
- **scenario**: 仓库分支保护规则设置页的表单提交与规则生效验证
- **capability**: 分支保护规则（Parity Matrix: ❓）
- **priority**: P0
- **oracle**: GitCode 规格（`repository-spec.md` §1.2）
- **ui_candidate**: true
- **rationale**: 分支保护是代码治理核心。文档声明可配置 force_push、allow_push、allow_merge、require_ci_pass、require_review。上轮用例未覆盖分支保护规则的 UI 设置流程。
- **expected_behavior**: 仓库设置中存在「保护分支」标签页；可选择分支并启用保护规则；表单包含 force_push 开关、允许推送/合并的角色下拉框、require_ci_pass 开关、require_review_count 数字输入；保存后规则即时生效，无权限用户 push 时 UI 给出明确拒绝提示。

### INTENT-SPEC-015
- **id**: INTENT-SPEC-015
- **dimensions**: [completeness]
- **scenario**: Webhook 配置页面的创建、事件选择、签名密钥设置与测试投递
- **capability**: 仓库 Webhook（Push/MR/Issue）（Parity Matrix: ❓）
- **priority**: P1
- **oracle**: GitCode 规格（`discussion-notification-spec.md` §2.3）
- **ui_candidate**: true
- **rationale**: Webhook 是外部集成的核心能力。文档声明支持签名验证、SSL 验证、自定义 Content-Type、失败重试。需验证 UI 配置页是否完整支持这些能力。
- **expected_behavior**: 仓库设置中存在「Webhooks」标签页；支持新增 Webhook，表单包含 URL、Content-Type（json/form）、Secret、SSL 验证开关、事件多选列表（push/pull_request/issues 等）；支持点击「测试」按钮模拟投递并显示响应状态码；支持启用/禁用开关。

### INTENT-SPEC-016
- **id**: INTENT-SPEC-016
- **dimensions**: [completeness]
- **scenario**: Release 管理页面的创建、编辑、Tag 关联与附件上传
- **capability**: Tags & Releases（`repository-spec.md` §2.5）
- **priority**: P1
- **oracle**: GitCode 规格
- **ui_candidate**: true
- **rationale**: Release 是版本发布的关键页面。上轮用例未覆盖 Release 管理 UI。需验证 Release 列表、创建表单、Tag 关联及 Draft/Prerelease 状态的页面渲染。
- **expected_behavior**: 仓库存在「Releases」标签页；列表页按时间倒序展示 Release，包含 Tag 名、标题、发布时间；创建 Release 表单支持选择 Tag 或新建 Tag、填写标题/正文、标记 Draft/Prerelease；支持上传附件（二进制文件）。

### INTENT-SPEC-017
- **id**: INTENT-SPEC-017
- **dimensions**: [completeness, security]
- **scenario**: 仓库成员管理页面的邀请流程、角色变更与即时生效验证
- **capability**: 仓库成员角色（Owner/Maintainer/Developer）（Parity Matrix: ❓）
- **priority**: P0
- **oracle**: GitCode 规格（`repository-spec.md` §1.1、§2.4）
- **ui_candidate**: true
- **rationale**: 对应风险登记册 RISK-SEC-06（权限越界）与 RISK-SEC-09（提权漏洞）。成员管理是权限控制的唯一入口。上轮 UI-ORG-25-001 仅覆盖组织设置，未深入仓库级成员邀请与角色变更。
- **expected_behavior**: 仓库设置中存在「成员」标签页；展示当前成员列表及角色；支持通过用户名/邮箱邀请新成员；角色下拉框包含 Owner/Maintainer/Developer/Reporter；变更角色后保存即时生效，被降权用户刷新页面后不再看到高权限菜单。

### INTENT-SPEC-018
- **id**: INTENT-SPEC-018
- **dimensions**: [completeness]
- **scenario**: 项目/组织 Settings 中 Action 功能开关（启用/禁用 Actions）
- **capability**: Action 功能开启前提（`workflow-file-location-structure.md` §前提条件）
- **priority**: P1
- **oracle**: GitCode 规格
- **ui_candidate**: true
- **rationale**: 文档提到「AtomGit Action 功能已开启」是前提条件，暗示存在开关。若 UI 中开关缺失或状态不同步，会导致 workflow 不被触发而用户无从排查。
- **expected_behavior**: 项目/组织设置中存在「Actions」或「CI/CD」模块；提供启用/禁用 Action 的总开关；禁用后仓库的 `.gitcode/workflows/` 不再触发运行，且 UI 给出明确提示「Action 已禁用」。

---

## 3. 规格声明验证点（Parity Matrix 中 ❓/🟡/❌ 的能力项）

### INTENT-SPEC-019
- **id**: INTENT-SPEC-019
- **dimensions**: [compatibility, usability]
- **scenario**: YAML 工作流编辑器中未知/不支持字段的报错提示质量
- **capability**: 未知/不支持字段处理（Parity Matrix: ❓）
- **priority**: P1
- **oracle**: GitCode 规格缺失（文档未明确降级方式）+ GitHub 语义（通常报错）
- **ui_candidate**: true
- **rationale**: Parity Matrix 明确标记「未知/不支持字段处理」为 ❓，文档未说明是报错还是静默忽略。这是兼容性差异高发区。若通过 Web IDE 或 YAML 编辑器编辑 workflow，报错质量直接影响迁移体验。
- **expected_behavior**: 在 Web 编辑器中保存包含未知顶层字段（如 GitHub 特有的 `concurrency.cancel-in-progress` 写法差异）的 workflow 时，系统应在保存前或触发时给出明确报错，指出不支持的字段名及位置；不应静默忽略导致行为与预期不符。

### INTENT-SPEC-020
- **id**: INTENT-SPEC-020
- **dimensions**: [compatibility, security]
- **scenario**: `pull_request_target` 事件下 checkout PR 代码的 UI 风险提示
- **capability**: `pull_request_target` checkout 风险（Parity Matrix: ✅，但风险登记册 RISK-SEC-03 为 P0 blocker）
- **priority**: P0
- **oracle**: GitCode 规格（`pr-mr-pipeline-security.md`）
- **ui_candidate**: true
- **rationale**: 文档明确警告「`pull_request_target` 下若显式 checkout 了 PR 源分支代码并执行其脚本，等于在高权限上下文中运行不可信代码」。平台应在 UI 层对此类高风险 workflow 配置给出安全提示。
- **expected_behavior**: 当 workflow 使用 `pull_request_target` 且包含 `uses: checkout` + `ref: ${{ atomgit.event.pull_request.head.sha }}` 时，编辑器或运行详情页应展示安全警告横幅，提示「此 workflow 在高权限上下文中运行不可信代码，请谨慎评审」；MR 页面 Checks 标签页中对该类运行标注风险标识。

### INTENT-SPEC-021
- **id**: INTENT-SPEC-021
- **dimensions**: [compatibility]
- **scenario**: 表达式中状态函数无括号（`success`/`failed`）在 YAML 编辑器中的语法提示
- **capability**: 状态函数无括号 `success`/`failed`（Parity Matrix: ❌ GitCode 特有差异）
- **priority**: P1
- **oracle**: GitCode 规格（`expressions.md`、`COMPAT-NOTES.md`）
- **ui_candidate**: true
- **rationale**: GitCode 使用无括号语法 `success`/`failed`，而 GitHub 使用 `success()`/`failure()`。这是高频踩坑点。若 Web YAML 编辑器能给出语法提示或自动补全，可显著降低迁移摩擦。
- **expected_behavior**: Web 编辑器中输入 `${{ success }}` 时不标红报错（视为合法）；输入 `${{ success() }}` 时给出警告提示「AtomGit Action 中状态函数无需括号」；自动补全列表中状态函数展示为无括号形式。

### INTENT-SPEC-022
- **id**: INTENT-SPEC-022
- **dimensions**: [compatibility]
- **scenario**: `workflow_dispatch` inputs 类型限制为 string 在 UI 表单中的呈现
- **capability**: `workflow_dispatch.inputs` 类型（Parity Matrix: 🟡 仅支持 string）
- **priority**: P1
- **oracle**: GitCode 规格（`manually-trigger-pipeline.md`）
- **ui_candidate**: true
- **rationale**: GitHub 支持 boolean/choice/number/environment，GitCode 仅支持 string。若用户迁移 GitHub workflow 到 GitCode，UI 表单应如实反映此限制，避免用户误以为支持其他类型。
- **expected_behavior**: 手动触发弹窗中，所有 inputs 均渲染为文本输入框，无复选框、下拉选择或数字步进器；若 workflow YAML 中错误声明了非 string 类型（如 `type: boolean`），编辑器给出警告「AtomGit Action 仅支持 string 类型 inputs」。

### INTENT-SPEC-023
- **id**: INTENT-SPEC-023
- **dimensions**: [reliability, completeness]
- **scenario**: 并发控制 `concurrency.max` 超出 1-5 范围时的报错或限制
- **capability**: `concurrency.max` 1-5 + QUEUE/IGNORE（Parity Matrix: 🟡）
- **priority**: P1
- **oracle**: GitCode 规格（`workflow-file-location-structure.md`）
- **ui_candidate**: true
- **rationale**: 文档声明 `concurrency.max` 范围为 1-5，超出此范围的配置行为未说明。UI 编辑器应在保存时校验此边界，避免无效配置进入仓库。
- **expected_behavior**: Web 编辑器中保存 `concurrency.max: 10` 时，保存前或 YAML 校验阶段给出明确错误提示「并发数最大为 5」；运行列表中，处于 QUEUE 状态的运行展示排队位置或预估等待时间；被 IGNORE 策略忽略的运行在历史列表中显示「已忽略」状态。

### INTENT-SPEC-024
- **id**: INTENT-SPEC-024
- **dimensions**: [reliability, usability]
- **scenario**: 超大日志或超大 diff 在 UI 中的加载性能与边界处理
- **capability**: 大规模：超大 matrix、超多 step、超长日志（`testing-focus.md` §12）
- **priority**: P1
- **oracle**: GitHub 语义（通常截断并提供下载）+ GitCode 规格（`view-job-logs.md` 提到下载）
- **ui_candidate**: true
- **rationale**: 稳定性专项要求验证「超长日志」的边界行为。若日志过大导致浏览器卡死或 UI 无法渲染，将严重影响调试体验。
- **expected_behavior**: 当日志大小超过某阈值（如 10MB 或 50,000 行），UI 自动截断在线展示部分，提示「日志过大，请下载完整日志」；下载功能正常返回完整文件；日志面板滚动流畅，无显著卡顿。

### INTENT-SPEC-025
- **id**: INTENT-SPEC-025
- **dimensions**: [completeness, compatibility]
- **scenario**: `permissions` 权限域命名（project/pr/issue/note/repository/hook）在 UI 中的展示与文档一致性
- **capability**: `permissions` 权限域命名（Parity Matrix: ❌ 与 GitHub 完全不同）
- **priority**: P1
- **oracle**: GitCode 规格（`token-permissions.md`）
- **ui_candidate**: true
- **rationale**: GitCode 权限域命名与 GitHub 完全不同（GitHub 用 `contents`/`pull-requests`/`issues`…）。若 UI 中帮助文案或自动补全沿用 GitHub 命名，将直接导致用户配置错误。
- **expected_behavior**: 编辑器自动补全 `permissions:` 时提示的域名为 `project`、`pr`、`issue`、`note`、`repository`、`hook`；设置页或文档悬浮提示中不混入 GitHub 命名（如 `contents`、`pull-requests`）；快捷语法 `read-all`/`write-all`/`{}` 在编辑器中支持自动补全。

### INTENT-SPEC-026
- **id**: INTENT-SPEC-026
- **dimensions**: [security, completeness]
- **scenario**: `pull_request` vs `pull_request_target` 在 MR 页面 Checks 标签页中的权限差异提示
- **capability**: `pull_request` vs `pull_request_target` 隔离（Parity Matrix: ✅，但风险登记册 RISK-SEC-01 为 P0）
- **priority**: P0
- **oracle**: GitCode 规格（`pr-mr-pipeline-security.md`）
- **ui_candidate**: true
- **rationale**: 对应风险登记册 RISK-SEC-01（fork PR 读到 secrets，P0 blocker）。虽然文档声明隔离机制存在，但 UI 层是否向 MR 评审人清晰展示「此 Checks 来自 fork PR，Token 为只读」至关重要。
- **expected_behavior**: MR 页面 Checks 标签页中，来自 `pull_request` 事件的运行标注「Fork PR 检查，只读权限」；来自 `pull_request_target` 事件的运行标注「目标分支检查，拥有写权限」；评审人可通过悬停或图标区分两者。

### INTENT-SPEC-027
- **id**: INTENT-SPEC-027
- **dimensions**: [completeness, usability]
- **scenario**: 通知中心中 CI 构建状态变更通知的渲染、分类与跳转
- **capability**: 通知机制 / CI 状态变更触发通知（`discussion-notification-spec.md`）
- **priority**: P1
- **oracle**: GitCode 规格
- **ui_candidate**: true
- **rationale**: 风险登记册 RISK-USE-04 关注「MR/Issue 缺少邮件/站内通知或通知延迟」。CI 状态变更是高频通知源，通知中心需正确分类并支持一键跳转至运行详情。
- **expected_behavior**: 通知中心收到 CI 失败/成功通知时，展示仓库名、workflow 名、运行编号、状态徽标；点击通知跳转至对应运行详情页；通知 reason 标记为 `ci_status_change` 或类似值；支持按通知类型筛选。

### INTENT-SPEC-028
- **id**: INTENT-SPEC-028
- **dimensions**: [completeness, compatibility]
- **scenario**: Runner 标签三段式 `{os,arch,flavor}` 在 UI 中的选择器与合法性校验
- **capability**: `runs-on` 标签体系（Parity Matrix: 🟡）
- **priority**: P1
- **oracle**: GitCode 规格（`using-hosted-runners.md`、`runner-and-environment.md`）
- **ui_candidate**: true
- **rationale**: 三段式标签是 GitCode 特有格式，与 GitHub 的单标签差异显著。若 UI 提供 Runner 选择器，应引导用户正确填写三段式，避免迁移用户直接填入 `ubuntu-latest` 导致匹配失败。
- **expected_behavior**: 若 UI 存在 Runner 选择器（如新建 workflow 的向导），应分三列展示 OS、Arch、Flavor 选项；直接输入 `runs-on: ubuntu-latest` 时编辑器给出警告「建议使用三段式格式，如 {ubuntu-latest,x64,small}」；非法 flavor（如未申请的 `xlarge`）在保存或触发时报错。

### INTENT-SPEC-029
- **id**: INTENT-SPEC-029
- **dimensions**: [completeness, compatibility]
- **scenario**: 上下文对象命名 `atomgit.*` 在表达式编辑器/文档提示中的展示
- **capability**: 上下文对象命名 `atomgit.*`（Parity Matrix: ❌ 替代 `github.*`）
- **priority**: P1
- **oracle**: GitCode 规格（`context.md`、`COMPAT-NOTES.md`）
- **ui_candidate**: true
- **rationale**: 上下文对象从 `github.*` 变为 `atomgit.*` 是迁移最高发差异。若 Web 编辑器或帮助文档中仍残留 `github.*` 提示，将直接导致 workflow 触发失败。
- **expected_behavior**: Web 编辑器的表达式自动补全提示 `atomgit.ref`、`atomgit.sha` 等，不出现 `github.ref`；文档悬浮窗或侧边栏帮助中所有示例均使用 `atomgit.*` 前缀；输入 `${{ github.ref }}` 时编辑器标红并提示「请使用 atomgit 上下文」。

### INTENT-SPEC-030
- **id**: INTENT-SPEC-030
- **dimensions**: [completeness, usability]
- **scenario**: 缓存（Cache）在运行详情页中的命中/未命中状态展示与 key 可见性
- **capability**: `cache` fork 场景隔离（Parity Matrix: ❓ 文档未明确 cache 隔离策略）
- **priority**: P1
- **oracle**: GitCode 规格（`core-concepts/artifacts-and-cache.md`、`using-dependency-cache.md`）
- **ui_candidate**: true
- **rationale**: Parity Matrix 标记 cache 隔离策略为 ❓。虽然底层隔离机制需通过 API/运行日志验证，但 UI 上是否展示 cache 命中状态、key 信息，对用户调试缓存行为至关重要。
- **expected_behavior**: 运行详情页中，使用 `uses: cache` 的 step 显示「Cache Hit」或「Cache Miss」状态；命中时展示匹配的 key；未命中时展示尝试的 `restore-keys` 列表；若存在 fork 场景，UI 中应明确标注「Fork PR 使用独立缓存命名空间」或类似提示（若规格支持）。

---

## 4. Packages / 其他未覆盖能力项

### INTENT-SPEC-031
- **id**: INTENT-SPEC-031
- **dimensions**: [completeness]
- **scenario**: 制品库（Packages）页面的包列表、版本管理与来源仓库追溯
- **capability**: Package 仓库协议与访问权限（Parity Matrix: 全部 ❓）
- **priority**: P1
- **oracle**: GitCode 规格（`parity-matrix.md` §五）
- **ui_candidate**: true
- **rationale**: Parity Matrix 中 Packages 全部能力项均为 ❓，是本轮未覆盖的整块领域。制品库页面是包治理的核心 UI，需验证其存在性与基础功能。
- **expected_behavior**: 仓库或组织存在「Packages」标签页；支持按包类型（npm/maven/docker 等）筛选；包详情页展示版本列表、上传时间、大小、来源仓库/CI 构建信息；支持删除特定版本（若权限允许）。

### INTENT-SPEC-032
- **id**: INTENT-SPEC-032
- **dimensions**: [completeness, usability]
- **scenario**: 仓库 Fork 流程的 UI 向导与 Fork 后仓库独立性验证
- **capability**: Fork 项目（`repository-spec.md` §2.1）
- **priority**: P1
- **oracle**: GitCode 规格
- **ui_candidate**: true
- **rationale**: 上轮 INTENT-COMP-009 已覆盖 Fork 流程，但 YAML 用例层是否有对应 UI 用例需确认。本轮补充 intent 以确保 UI 层有明确追溯。Fork 后导航独立性直接影响外部贡献者体验。
- **expected_behavior**: 公开仓库首页展示「Fork」按钮；点击后弹出向导，支持选择目标命名空间（个人/组织）并修改仓库名；Fork 完成后自动跳转至新仓库首页；新仓库的 Issues/MR/Actions 标签页导航均指向 Fork 仓库自身，不回指原仓库。

### INTENT-SPEC-033
- **id**: INTENT-SPEC-033
- **dimensions**: [completeness, security]
- **scenario**: 审计日志（Audit Log）页面的查询、筛选与关键操作记录完整性
- **capability**: 审计日志（Parity Matrix: ❓）
- **priority**: P0
- **oracle**: GitCode 规格（`user-org-spec.md` §1.1 提到审计，但 `parity-matrix.md` §六标记为 ❓）
- **ui_candidate**: true
- **rationale**: 风险登记册 RISK-SEC-09（组织成员非法提升权限，P0 blocker）要求有审计能力支撑事后追溯。若审计日志页面缺失或记录不完整，将无法支撑安全事件调查。
- **expected_behavior**: 组织/仓库设置中存在「审计日志」标签页；记录关键操作（成员角色变更、仓库删除、Secret 更新、保护规则修改、Webhook 增删）；支持按操作者、时间范围、操作类型筛选；日志不可被普通成员删除或篡改。

### INTENT-SPEC-034
- **id**: INTENT-SPEC-034
- **dimensions**: [completeness, usability]
- **scenario**: 项目 Wiki 页面的创建、编辑与 Markdown 渲染
- **capability**: Wiki（`repository-spec.md` §1 功能概述提到 Wiki）
- **priority**: P2
- **oracle**: GitCode 规格
- **ui_candidate**: true
- **rationale**: Wiki 是项目文档协作的扩展能力。文档提到支持 Wiki，但 UI 可达性与编辑体验未验证。
- **expected_behavior**: 仓库存在「Wiki」标签页；支持创建首页、新增子页面；编辑器支持 Markdown 语法与实时预览；保存后页面内容正确渲染；支持查看修订历史。

### INTENT-SPEC-035
- **id**: INTENT-SPEC-035
- **dimensions**: [completeness, compatibility]
- **scenario**: 工作流目录 `.gitcode/workflows/` 在仓库文件树中的展示与 `.github/workflows/` 的降级提示
- **capability**: 工作流文件目录 `.gitcode/workflows/`（Parity Matrix: 🟡）
- **priority**: P1
- **oracle**: GitCode 规格（`workflow-file-location-structure.md`、`COMPAT-NOTES.md`）
- **ui_candidate**: true
- **rationale**: 迁移第一摩擦点是目录名差异。若用户保留 `.github/workflows/` 而 GitCode 仅识别 `.gitcode/workflows/`，UI 应在适当位置给出提示，避免用户误以为 workflow 已配置但不被触发。
- **expected_behavior**: 仓库文件树中 `.gitcode/workflows/` 目录正常展示，文件可点击编辑；若仓库存在 `.github/workflows/` 但不存在 `.gitcode/workflows/`，在 Actions 标签页显示提示「请将 workflow 文件移至 `.gitcode/workflows/` 目录」；`.github/workflows/` 中的文件在 GitCode 中不被识别为 workflow。

---

## 附录：本轮增量 intent 汇总

| 序号 | ID | 维度 | 能力项 | 优先级 | ui_candidate | 对应 Parity Matrix / 风险登记册 |
|------|-----|------|--------|--------|--------------|-------------------------------|
| 1 | INTENT-SPEC-001 | completeness, usability | Actions 标签页 workflow 列表 | P0 | true | 运行状态机（✅，UI 缺） |
| 2 | INTENT-SPEC-002 | completeness | 运行详情页 stages/job/step 渲染 | P1 | true | stages（❌）/ post（❌） |
| 3 | INTENT-SPEC-003 | completeness, usability | Job 日志折叠/搜索/下载 | P1 | true | 日志完整性（✅，UI 缺） |
| 4 | INTENT-SPEC-004 | completeness, usability | 手动触发 workflow_dispatch | P1 | true | inputs 仅 string（🟡） |
| 5 | INTENT-SPEC-005 | completeness, reliability | 重新运行按钮与限制提示 | P1 | true | rerun 限制（🟡） |
| 6 | INTENT-SPEC-006 | completeness, compatibility | Commit/MR CI 状态徽标 | P1 | true | CI 状态回写（❓） |
| 7 | INTENT-SPEC-007 | completeness | README badge 渲染 | P2 | true | 状态徽标嵌入 |
| 8 | INTENT-SPEC-008 | completeness, usability | Artifact 下载入口 | P1 | true | upload-artifact（🟡） |
| 9 | INTENT-SPEC-009 | completeness | Matrix job UI 展开展示 | P1 | true | matrix 组合上限（❓） |
| 10 | INTENT-SPEC-010 | completeness, security | Secret 日志脱敏 `***` | P0 | true | secrets 脱敏（🟡）/ RISK-SEC-05 |
| 11 | INTENT-SPEC-011 | security, completeness | Secrets 管理页面 | P0 | true | secrets 管理 |
| 12 | INTENT-SPEC-012 | completeness, compatibility | Variables 管理页面 | P1 | true | vars 上下文 |
| 13 | INTENT-SPEC-013 | security, completeness | Environment 审批配置 | P0 | true | 环境级 Secret + 审批 |
| 14 | INTENT-SPEC-014 | security, completeness | 分支保护规则设置页 | P0 | true | 分支保护规则（❓） |
| 15 | INTENT-SPEC-015 | completeness | Webhook 配置与测试 | P1 | true | Webhook（❓） |
| 16 | INTENT-SPEC-016 | completeness | Release/Tag 管理页面 | P1 | true | Release（未在 Parity 单独列） |
| 17 | INTENT-SPEC-017 | completeness, security | 仓库成员邀请与角色变更 | P0 | true | 仓库角色（❓）/ RISK-SEC-06/09 |
| 18 | INTENT-SPEC-018 | completeness | Action 功能开关 | P1 | true | Action 开启前提 |
| 19 | INTENT-SPEC-019 | compatibility, usability | 未知字段 YAML 报错质量 | P1 | true | 未知/不支持字段（❓） |
| 20 | INTENT-SPEC-020 | compatibility, security | `pull_request_target` checkout 风险提示 | P0 | true | RISK-SEC-03 |
| 21 | INTENT-SPEC-021 | compatibility | 状态函数无括号语法提示 | P1 | true | 状态函数无括号（❌） |
| 22 | INTENT-SPEC-022 | compatibility | `workflow_dispatch` inputs string 限制 | P1 | true | inputs 类型（🟡） |
| 23 | INTENT-SPEC-023 | reliability, completeness | `concurrency.max` 边界与 QUEUE/IGNORE 展示 | P1 | true | concurrency（🟡） |
| 24 | INTENT-SPEC-024 | reliability, usability | 超大日志/diff 加载与截断 | P1 | true | 超长日志（§12） |
| 25 | INTENT-SPEC-025 | compatibility | `permissions` 域命名 UI 一致性 | P1 | true | permissions 命名（❌） |
| 26 | INTENT-SPEC-026 | security, completeness | PR Checks 标签页权限差异提示 | P0 | true | RISK-SEC-01 |
| 27 | INTENT-SPEC-027 | completeness, usability | 通知中心 CI 状态通知渲染 | P1 | true | RISK-USE-04 |
| 28 | INTENT-SPEC-028 | compatibility | Runner 三段式标签选择器 | P1 | true | runs-on（🟡） |
| 29 | INTENT-SPEC-029 | compatibility | `atomgit.*` 上下文命名提示 | P1 | true | atomgit.*（❌） |
| 30 | INTENT-SPEC-030 | completeness, usability | Cache 命中状态与 key 展示 | P1 | true | cache 隔离（❓） |
| 31 | INTENT-SPEC-031 | completeness | Packages 页面列表与追溯 | P1 | true | Packages（全部 ❓） |
| 32 | INTENT-SPEC-032 | completeness, usability | Fork 流程 UI 向导 | P1 | true | Fork |
| 33 | INTENT-SPEC-033 | completeness, security | 审计日志查询与完整性 | P0 | true | 审计日志（❓）/ RISK-SEC-09 |
| 34 | INTENT-SPEC-034 | completeness, usability | Wiki 创建与渲染 | P2 | true | Wiki |
| 35 | INTENT-SPEC-035 | completeness, compatibility | `.gitcode/workflows/` 目录展示与迁移提示 | P1 | true | 工作流目录（🟡） |

> **统计**：本轮共生成 35 条增量 intent，其中 **ui_candidate: true 35 条**（100%），覆盖 Actions UI（10 条）、Settings/Governance（8 条）、规格声明验证（12 条）、Packages/其他（5 条）。P0 共 7 条，P1 共 26 条，P2 共 2 条。
