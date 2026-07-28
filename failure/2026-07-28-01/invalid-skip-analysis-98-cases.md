# 98 条 Invalid/SKIP 用例分类分析

> 来源：目录 `phase02/agents/valid-classify/output/invalid/` (72 条) + `phase02/agents/valid-classify/output/SKIP/` (26 条)
> 日期：2026-07-24
> 参考规则：[VALIDATION-RULES.md](../../phase01/schema/VALIDATION-RULES.md)

---

## 一、Invalid (72 条) -- 平台 Schema 拒绝

### 1.1 分类统计

| 拒绝原因 | 数量 | 涉及规则 |
|----------|------|---------|
| `permissions` 不支持（Workflow 级或 Job 级） | 8 | Rule 13 |
| `environment` 不支持（Job 级） | 6 | Rule 16 |
| 表达式/函数不支持（`success()`, `failure()`, `vars`, `needs`, 未知函数, 裸关键字） | 8 | Rule 4, Rule 7 |
| `stages` 非法（数组格式或结构不被 platform 接受） | 4 | Rule 17 |
| `concurrency` 相关问题 | 6 | Rule 19 |
| `run-name` 不支持 | 4 | Rule 18 |
| `post` / `post.steps` 不支持 | 3 | Rule 20 |
| Runner 标签非法或不存在 | 8 | Rule 1 |
| 未知顶层字段（`unknown_field`, `custom_field`, `select`, `manual_override`, `inputs` 等） | 5 | Rule 22 |
| 不支持的触发事件（`release` 等）或 types（`opened`, `labeled`, `ready_for_review`） | 6 | Rule 12, Rule 22 |
| `services` 不支持 | 1 | Rule 20 |
| YAML 语法错误（缺少 `on`, 缩进错误） | 2 | Rule 8, Rule 10 |
| `uses:` 非法格式（市场名/typo squatting） | 2 | Rule 4b |
| Paths 超过限制（300/301） | 2 | Rule 11 (extended) |
| Steps 超过 16 个 | 1 | Rule 5 |
| WAF 拦截 (HTTP 418) 且不在白名单 | 2 | -- |

### 1.2 逐条明细

#### 1.2.1 permissions (Rule 13) -- 8 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMPAT-MIGRATE-01-001 | workflow 级 `permissions:` 块声明 `contents: read` | Rule 13 (`permissions` unknown property) | 是，删除 permissions 块 |
| 2 | COMPAT-PERM-01-003 | workflow 级 `permissions:` 含 GitHub `contents` 权限项 | Rule 13 | 是，删除 permissions 块 |
| 3 | COMPAT-PERM-01-006 | job 级 `permissions:` 字段 | Rule 13 (job 级 unknown property) | 是，删除 job 级 permissions |
| 4 | SEC-DEFPERM-01-001 | workflow 级 `permissions:` 声明 token 权限 | Rule 13 | 是，删除 permissions 块 |
| 5 | SEC-DEFPERM-01-002 | job 级 `permissions:` 收窄权限 | Rule 13 | 是，删除 job 级 permissions |
| 6 | SEC-PERM-01-001 | workflow 级 `permissions:` 显式声明 | Rule 13 | 是，删除 permissions 块 |
| 7 | SEC-PERM-01-002 | workflow 级 `permissions:` 声明 read | Rule 13 | 是，删除 permissions 块 |
| 8 | USE-PERM-01-002 | workflow 级 `permissions:` 使用 GitHub 权限域名 | Rule 13 | 是，删除 permissions 块 |

#### 1.2.2 environment (Rule 16) -- 6 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMPAT-ENVIRON-01-001 | job 含 `environment:` 字段 | Rule 16 | 是，删除 environment 块 |
| 2 | COMPAT-ENVIRON-01-002 | job 含 `environment:` 字段绑定 secrets | Rule 16 | 是，删除 environment 块 |
| 3 | COMPAT-SECRET-01-005 | job 含 `environment:` 绑定环境级 secrets | Rule 16 | 是，删除 environment 块 |
| 4 | SEC-ENV-01-001 | job 含 `environment:` 需审批访问 | Rule 16 | 是，删除 environment 块 |
| 5 | SEC-ENV-01-002 | job 含 `environment:` 审批前不可读取 | Rule 16 | 是，删除 environment 块 |
| 6 | USE-DOC-01-007 | job 含 `environment:` 字段 | Rule 16 | 是，删除 environment 块 |

#### 1.2.3 表达式/函数不支持 -- 8 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMPAT-EXPR-01-013 | `${{ success() }}`（GitHub 语法，平台拒绝） + `${{ success }}`（裸关键字，平台拒绝） | Rule 4 | 否，平台不支持 `success()` 也不支持裸 `success`；需等待平台支持或改写为 always() |
| 2 | COMPAT-EXPR-01-014 | `${{ always }}`（裸关键字，无括号，平台拒绝） | Rule 4 | 是，改为 `${{ always() }}`（带括号已实测通过） |
| 3 | COMPAT-VARS-01-005 | `if: ${{ vars.ENABLE_FEATURE == 'true' }}` | Rule 7 (`vars` 上下文不支持) | 是，改 `atomgit.*` 或其他上下文 |
| 4 | REL-RACE-01-048 | `if: failure()`（GitHub 语法，平台拒绝） | Rule 4 (`failure()` not supported) | 否，平台当前无确认可用的 failure 门控语法 |
| 5 | USE-EXPR-01-002 | `if: ${{ unknownFunc() }}` 调用平台不存在的函数 | Rule 4 (未知表达式函数) | 是，使用合法函数名 |
| 6 | USE-STAT-01-002 | `if: ${{ success() }}`（GitHub 语法） | Rule 4 | 否，平台不支持 `success()` |
| 7 | COMP-CTX-01-052 | `if: ${{ needs.verify.result == 'success' }}` + `if: ${{ env.ALWAYS_TRUE == 'yes' }}`（needs/env 复杂表达式上下文） | Rule 4 (platform refusal of specific expression patterns) | 部分可修复，简化表达式 |
| 8 | COMP-EXPR-01-058 | `${{ !false }}`, `${{ 5 > 3 }}`, `${{ 2 < 3 }}`, `${{ true && (false \|\| true) }}` 等运算符（部分被平台拒绝） | Rule 4 (部分运算符不支持) | 部分可修复，仅使用平台确认支持的运算符 |

#### 1.2.4 stages 非法 (Rule 17) -- 4 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMP-STAGES-01-002 | `stages:` 使用数组格式 `- name: test-stage` | Rule 17 (stages 必须是 map) | 是，改为 map 格式 `stages: {default: {jobs: {...}}}` |
| 2 | COMP-STAGES-01-004 | `stages:` 使用 map 格式但自定义名称 `build_stage`/`test_stage`（platform 可能仅识别 `default`） | Rule 17 (stages 结构被拒绝) | 部分可修复，尝试标准 `default` 名称 |
| 3 | COMP-STAGES-01-005 | `stages:` 数组格式 `- name: build-stage` | Rule 17 | 是，改为 map 格式 |
| 4 | REL-STAGES-01-029 | `stages:` 含 `fail_fast: true` + 自定义 stage 名称（`test_stage`, `next_stage`），platform 拒绝此 stages 结构 | Rule 17 | 部分可修复，简化为最小 stages 结构 |

#### 1.2.5 concurrency 问题 (Rule 19) -- 6 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMPAT-CONCUR-01-001 | `cancel-in-progress: false`（GitHub 风格字段名，platform 不支持） | Rule 19 (concurrency 字段不被识别) | 否，concurrency 整体不被 platform 接受 |
| 2 | COMPAT-CONCUR-01-002 | `concurrency.group: [invalid, array]`（group 值非法）+ `cancel-in-progress` | Rule 19 | 是，修正 group 为字符串 |
| 3 | COMPAT-CONCUR-01-003 | `concurrency` + `cancel-in-progress: true`（preemption 配置不被接受） | Rule 19 | 否，concurrency/preemption 未完全支持 |
| 4 | COMPAT-CONCUR-01-004 | `concurrency.preemption.enable: true` + `events: 11`（events 为整数非数组） | Rule 19a (preemption.events 格式非法) | 是，events 改为 `[mr_id]` |
| 5 | REL-PREEMPT-01-006 | `concurrency.preemption.events: [push, pull_request, ...]` 含 11 个值，含 `push`（不允许） | Rule 19a (events 仅允许 `[mr_id]`) | 是，events 改为 `[mr_id]` |
| 6 | USE-CONC-01-002 | `concurrency.max: -1` | Rule 19b (max 不得小于 1) | 是，max 改为 ≥1 |

#### 1.2.6 run-name (Rule 18) -- 4 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMPAT-FIELD-01-001 | `run-name: Test Run Name` 顶层字段 | Rule 18 (`run-name` unknown property) | 是，删除 run-name |
| 2 | COMPAT-MIGRATE-01-002 | `run-name: "Build by ${{ github.actor }}"` | Rule 18 + Rule 4 (`github.actor` 上下文不存在) | 是，删除 run-name |
| 3 | USE-UNKN-01-001 | `run-name: Build by ${{ atomgit.actor }}` | Rule 18 | 是，删除 run-name |
| 4 | COMPAT-FIELD-01-001 | 同上 | Rule 18 | 是 |

#### 1.2.7 post/post.steps (Rule 20) -- 3 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMP-STAGES-01-003 | `post:` + `post.run_always: true` + `post.steps` | Rule 20 (`post.steps` unknown property) | 是，移除 post 块 |
| 2 | COMP-WFLOW-01-065 | `post:` + `post.run_always: true` + `post.steps` | Rule 20 | 是，移除 post 块 |
| 3 | REL-POST-01-001 | `post:` + `post.run_always: true` + `post.steps` | Rule 20 | 是，移除 post 块 |

#### 1.2.8 Runner 标签问题 (Rule 1) -- 8 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMP-RUNNER-01-003 | `runs-on: [nonexistent-os, x64, small]` | Rule 1 (runner 标签组合不存在) | 是，使用合法标签如 `[ubuntu-latest, x64, small]` |
| 2 | COMP-RUNNER-01-082 | `runs-on: {ubuntu-24, x64, small}`（对象格式，非数组） | Rule 1 (对象格式禁止) | 是，改为 `[ubuntu-24, x64, small]` |
| 3 | COMPAT-RUNNER-01-004 | `runs-on: [gpu, nvidia]`（自定义特征标签不存在） | Rule 1 | 是，使用已注册标签 |
| 4 | COMPAT-RUNNER-01-005 | `runs-on: [intranet, x64]`（不完整/不存在的标签） | Rule 1 | 是，使用合法标签 |
| 5 | COMPAT-RUNSON-01-003 | `runs-on: {}`（对象格式） | Rule 1 (对象格式禁止) | 是，改为数组格式 |
| 6 | COMPAT-RUNSON-01-005 | `runs-on: [windows-latest, x64, small]`（windows runner 不支持） | Rule 1 (windows 标签不存在) | 是，改为 `[ubuntu-latest, x64, small]` |
| 7 | COMPAT-RUNSON-01-006 | `runs-on: [macos-latest, x64, small]`（macos runner 不支持） | Rule 1 (macos 标签不存在) | 是，改为 `[ubuntu-latest, x64, small]` |
| 8 | COMPAT-SHELL-01-003 | `runs-on: [windows-latest, x64, small]`（windows runner 不支持） | Rule 1 | 是，改为 `[ubuntu-latest, x64, small]` |

#### 1.2.9 未知字段 (Rule 22) -- 5 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMP-UNKNOWN-01-001 | `unknown_field: true` 顶层字段 | Rule 22 | 是，删除 unknown_field |
| 2 | COMP-UNKNOWN-01-004 | `stages.gated_stage.select: selected_by_default` + `jobs.beta.select: selected_by_default` | Rule 22 (`select` unknown property) | 是，删除 select 字段 |
| 3 | COMP-UNKNOWN-01-005 | 顶层 `inputs:` + `manual_override: true` | Rule 22 (顶层 `inputs` 不被识别，`manual_override` unknown) | 是，删除这些字段或移动到 `on.workflow_dispatch.inputs` |
| 4 | COMPAT-FIELD-01-003 | `custom_field: value` 顶层未知字段 | Rule 22 | 是，删除 custom_field |
| 5 | COMPAT-FIELD-01-001 | `run-name:` 也是 Rule 18，但还使用了未记录的 `name:` 顶层字段（`name: unknown field test`） | Rule 22 | 是，删除未知顶层字段 |

#### 1.2.10 不支持的触发事件/types (Rule 12 + Rule 22) -- 6 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMPAT-EVENT-01-001 | `on.release.types: [published]`（`release` 事件不支持） | Rule 22 (unsupported event) | 是，改为 `workflow_dispatch` 或 `push` |
| 2 | COMPAT-PR-01-002 | `on.pull_request.types: [opened, closed, reopened]`（GitHub 风格 types） | Rule 12 (GitHub types naming) | 是，改为 `[open, close, reopen]` 或使用 `merge_requests` |
| 3 | COMPAT-PR-01-004 | `on.pull_request.types: [open, merge]` | Rule 12 (pull_request 可能不支持 merge type) | 是，改用 `merge_requests` 事件 |
| 4 | COMPAT-PR-01-007 | `on.pull_request.types: [labeled]`（`labeled` 不是合法 type） | Rule 12 | 是，删除此 type |
| 5 | COMPAT-PR-01-008 | `on.pull_request.types: [ready_for_review]`（不合法 type） | Rule 12 | 是，删除此 type |
| 6 | USE-TYPE-01-002 | `on.pull_request.types: [opened, synchronize]`（GitHub 命名） | Rule 12 | 是，改为 `[open, update]` |

#### 1.2.11 其他规则 -- 8 条

| # | case_id | 原因 | 违反的规则 | 可修复? |
|---|---------|------|-----------|--------|
| 1 | COMPAT-FIELD-01-002 | `jobs.test.services:` 含 `services` 字段 | Rule 20 (`services` unknown property) | 是，删除 services 块 |
| 2 | USE-YAML-01-001 | workflow 缺少 `on:` 字段 | Rule 8/Rule 22 (缺失必填字段) | 是，添加 `on: workflow_dispatch:` |
| 3 | USE-YAML-01-002 | steps 缩进不一致：第一个 step 6 空格，第二个 step 7 空格 | Rule 10 (YAML 缩进错误) | 是，修正缩进为统一空格数 |
| 4 | USE-ACT-01-004 | `uses: AtomgitCache`（市场名格式，非短名，platform step uses 仅接受官方短名或 `owner/repo@ref`） | Rule 4b (illegal uses format) | 是，改为 `uses: cache` 或 `owner/repo@ref` |
| 5 | SEC-SUPPLY-01-003 | `uses: checkout-action@v1`（typosquatting，非官方 Action 名） | Rule 4b (non-official action name) | 是，改为 `uses: checkout` |
| 6 | COMP-TRIG-01-079 | `on.pull_request.types: [open, merge]`（platform 拒绝此组合） | Rule 12 | 是，改用合法事件/type 组合 |
| 7 | COMPAT-PATHS-01-001 | 300 条 paths（边界值，platform 可能拒绝 >= 300） | Rule 11 (extended: paths 上限) | 是，减少 paths 数量到 < 300 或验证实际限制 |
| 8 | COMPAT-PATHS-01-002 | 301 条 paths（明确越界，预期被拒绝） | Rule 11 (extended: paths 上限) | 是，减少到 ≤300 或标记为负向用例 |

#### 1.2.12 平台语义拒绝（非 schema 直接违规） -- 5 条

以下用例 workload 语法上可能合规，但 platform validator 仍拒绝：

| # | case_id | 原因 | 判定 | 可修复? |
|---|---------|------|------|--------|
| 1 | COMP-RUNNER-01-003 | `runs-on: [nonexistent-os, x64, small]` -- 标签组合在平台 runner 池中不存在 | 平台调度层拒绝（非 schema 层） | 是，使用已注册标签 |
| 2 | USE-LBL-01-001 | `runs-on: [nonexistent-os, x64, small]` -- 同上 | 平台调度层拒绝 | 是，使用已注册标签 |
| 3 | USE-RUN-01-002 | `runs-on: [ubuntu-latest]` -- 单标签不完整，缺少 x64/small | Rule 1 (标签数量不足) | 是，改为 `[ubuntu-latest, x64, small]` |
| 4 | COMPAT-PR-01-003 | `on.pull_request.types: [open, reopen, update]` -- 平台拒绝此 type 组合（实际语义不匹配） | Rule 12 (语义拒绝) | 部分可修复 |
| 5 | COMPAT-PR-01-005 | `on.pull_request.paths: ['api/**']` -- pull_request 事件不支持 paths 过滤 | Rule 12 (paths filter on unsupported event) | 是，改用 push 事件 |
| 6 | COMPAT-ACTIONDEV-01-001 | `uses: ./.github/actions/my-action` -- 本地 Action 路径在 validation 时文件不存在 | Rule 4b (action resolution failure) | 是，验证时确保 action.yml 存在 |
| 7 | REL-STEPS-01-042 | 单 job 含 50 个 step | Rule 5 (steps > 16 超过平台限制) | 是，拆分为多个 job |
| 8 | SEC-WCMD-01-003 | shell 注入安全测试，workflow 语法本身可能合法但被安全校验拒绝 | 安全校验 (WAF-like) | 否，安全设计意图 |
| 9 | SEC-WCMD-01-004 | 同上，output 注入测试 | 安全校验 | 否，安全设计意图 |

---

## 二、SKIP (26 条) -- 无法脚本化

### 2.1 分类统计

| SKIP 原因 | 数量 |
|-----------|------|
| `workflow: null`（无 workflow 定义） | 26 |

### 2.2 按主题细分

| 主题 | 数量 | case_ids |
|------|------|---------|
| K8s/Karmada 集群调度 | 6 | REL-K8S-01-046 ~ REL-K8S-01-051 |
| Volcano Job (vcjob) | 2 | REL-VCJOB-01-001, REL-VCJOB-01-002 |
| 安全审计/Secret 管理 | 3 | SEC-AUDIT-01-001, SEC-NAME-01-003, SEC-SECMGMT-01-002 |
| 安全运行链/权限 | 1 | SEC-WFRUN-01-001 |
| Action/插件目录/API 一致性 | 2 | USE-ACT-01-003, USE-API-01-001 |
| 文档扫描/一致性 | 8 | USE-DOC-01-001, USE-DOC-01-002, USE-DOC-01-006, USE-DIR-01-002, USE-EXPR-01-003, USE-LBL-01-003, USE-LBL-01-005, USE-PATH-01-001 |
| 环境变量/Runtime 文档 | 1 | USE-RES-01-001 |
| 新手引导/未知字段 | 2 | USE-ONBD-01-001, USE-UNKN-01-004 |
| 变量上下文文档 | 1 | USE-VARS-01-001 |

### 2.3 逐条明细

| # | case_id | title | SKIP 原因 |
|---|---------|-------|----------|
| 1 | REL-K8S-01-046 | K8s 单集群接入与 NPU 资源发现正确性 | `workflow: null` -- 需要直接操作 K8s 集群，无法通过 workflow 描述 |
| 2 | REL-K8S-01-047 | Karmada 多集群接入、聚合资源发现与指定成员集群调度 | `workflow: null` |
| 3 | REL-K8S-01-048 | Karmada 按卡型号/数量自动分发与成员资源不足时的终态语义 | `workflow: null` |
| 4 | REL-K8S-01-049 | pod NPU 单卡/多卡调度正确性与非法请求 Pending 语义 | `workflow: null` |
| 5 | REL-K8S-01-050 | pod 多副本任务（Worker）指定 NPU 调度 | `workflow: null` |
| 6 | REL-K8S-01-051 | 同一集群重复接入的幂等性 | `workflow: null` |
| 7 | REL-VCJOB-01-001 | vcjob（volcano job）格式任务解析与运行 | `workflow: null` -- Volcano Job 非标准 workflow 格式 |
| 8 | REL-VCJOB-01-002 | 大规模 vcjob 并发提交 | `workflow: null` |
| 9 | SEC-AUDIT-01-001 | 敏感操作审计记录 | `workflow: null` -- 审计查询而非 workflow 执行 |
| 10 | SEC-NAME-01-003 | 可遮蔽系统变量的 secret 命名（ATOMGIT_ 前缀等）创建时被拒 | `workflow: null` -- API 调用测试 |
| 11 | SEC-SECMGMT-01-002 | 无权限角色对 secret 的 CRUD 被拒 | `workflow: null` -- API 权限测试 |
| 12 | SEC-WFRUN-01-001 | 不可信运行不应存在隐式拉起高权限后续运行的链式路径 | `workflow: null` -- 系统级安全测试 |
| 13 | USE-ACT-01-003 | 官方短名 Action 清单与 actions-market 插件目录映射一致性 | `workflow: null` -- 文档/目录对比 |
| 14 | USE-API-01-001 | API 字段值与事件类型命名同一概念分裂的对照检查 | `workflow: null` -- API 文档测试 |
| 15 | USE-DIR-01-002 | .github/workflows/ 下 workflow 未被识别时的目录差异提示 | `workflow: null` -- 目录/文档测试 |
| 16 | USE-DOC-01-001 | stages 与 post 概念在迁移文档中具备可发现性 | `workflow: null` -- 文档扫描 |
| 17 | USE-DOC-01-002 | stages 与 stages 内 jobs 字段语法跨文档四种形态互相矛盾扫描 | `workflow: null` -- 文档扫描 |
| 18 | USE-DOC-01-006 | syntax-reference 章节编号连续性扫描 | `workflow: null` -- 文档扫描 |
| 19 | USE-EXPR-01-003 | expressions 函数表语法标记可解析性与状态关键字术语区分 | `workflow: null` -- 文档扫描 |
| 20 | USE-LBL-01-003 | runs-on 标签写法跨文档形态扫描 | `workflow: null` -- 文档扫描 |
| 21 | USE-LBL-01-005 | runs-on 含资源池名写法的文档资源池清单 diff | `workflow: null` -- 文档扫描 |
| 22 | USE-ONBD-01-001 | 新手快速开始路径端到端可复刻走查 | `workflow: null` -- 手工走查 |
| 23 | USE-PATH-01-001 | paths 300 文件上限在文档与行为中一致且明示 | `workflow: null` -- 文档验证 |
| 24 | USE-RES-01-001 | runtime-environment-variables.md 中不应出现未标注的 GitHub 专属变量名 | `workflow: null` -- 文档扫描 |
| 25 | USE-UNKN-01-004 | 未文档化字段 select/manual_override/code-update/顶层 inputs 的文档集合 | `workflow: null` -- 文档扫描 |
| 26 | USE-VARS-01-001 | vars 上下文在文档与样本中的声明必须一致 | `workflow: null` -- 文档验证 |

---

## 三、可修复建议

### 3.1 批量可修复：直接删除不支持字段 (约 30 条)

以下案例仅因使用了平台不支持的字段，删除对应字段即可通过 schema 校验：

| 不支持字段 | 涉及案例数 | case_ids | 修复方案 |
|-----------|-----------|---------|---------|
| `permissions` | 8 | 见 §1.2.1 | 删除所有 `permissions:` 块（workflow 级和 job 级） |
| `environment` | 6 | 见 §1.2.2 | 删除所有 job 级 `environment:` 块 |
| `run-name` | 4 | 见 §1.2.6 | 删除 `run-name:` 行 |
| `post` + `post.steps` | 3 | 见 §1.2.7 | 删除 `post:` 块 |
| `services` | 1 | COMPAT-FIELD-01-002 | 删除 `services:` 块 |
| `unknown_field`/`custom_field` | 2 | COMP-UNKNOWN-01-001, COMPAT-FIELD-01-003 | 删除未知顶层字段 |
| `select` | 1 | COMP-UNKNOWN-01-004 | 删除 `select:` 字段 |
| `manual_override` | 1 | COMP-UNKNOWN-01-005 | 删除 `manual_override:` 字段 |

### 3.2 批量可修复：修正格式 (约 12 条)

| 问题 | 涉及案例数 | case_ids | 修复方案 |
|------|-----------|---------|---------|
| `runs-on` 对象格式 | 2 | COMP-RUNNER-01-082, COMPAT-RUNSON-01-003 | 改为数组 `[tag1, tag2, ...]` |
| `runs-on` 单标签 | 1 | USE-RUN-01-002 | 补充为三段式 `[ubuntu-latest, x64, small]` |
| `runs-on` 不存在标签 | 6 | COMP-RUNNER-01-003, COMPAT-RUNNER-01-004, COMPAT-RUNNER-01-005, COMPAT-RUNSON-01-005, COMPAT-RUNSON-01-006, USE-LBL-01-001 | 改为平台支持的标签组合 |
| `stages` 数组格式 | 2 | COMP-STAGES-01-002, COMP-STAGES-01-005 | 改为 map 格式 |
| `on.schedule` 对象格式 | 0 | (本次未出现) | -- |
| YAML 缩进/缺失字段 | 2 | USE-YAML-01-001, USE-YAML-01-002 | 补充 `on:` / 修正缩进 |

### 3.3 批量可修复：修正触发事件/types (约 7 条)

| 问题 | 涉及案例数 | case_ids | 修复方案 |
|------|-----------|---------|---------|
| `on.release` 不支持事件 | 1 | COMPAT-EVENT-01-001 | 改为 `workflow_dispatch` |
| `pull_request.types` GitHub 命名 | 4 | COMPAT-PR-01-002, COMPAT-PR-01-007, COMPAT-PR-01-008, USE-TYPE-01-002 | 改为 GitCode 命名 (`opened→open`, `closed→close`, `synchronize→update`) |
| `pull_request.types` 不合法值 | 1 | COMPAT-PR-01-004 | 改用 `merge_requests` 事件 |

### 3.4 批量可修复：修正 uses 格式 (约 2 条)

| 问题 | 涉及案例数 | case_ids | 修复方案 |
|------|-----------|---------|---------|
| 市场名格式 | 1 | USE-ACT-01-004 | 改为官方短名 (`cache`) |
| typo squatting | 1 | SEC-SUPPLY-01-003 | 改为正确短名 (`checkout`) |

### 3.5 不可修复或需平台支持 (约 14 条)

以下案例因平台功能缺失或语义限制，即使修正 schema 也无法通过：

| case_id | 问题 | 根本原因 |
|---------|------|---------|
| COMPAT-EXPR-01-013 | `success()` 不识别 | 平台不支持 `success()` 函数和裸 `success` 关键字 |
| COMPAT-EXPR-01-014 | 裸 `always` 关键字 | 平台只支持 `always()` 带括号 |
| COMPAT-VARS-01-005 | `vars.*` 上下文 | 平台不支持 `vars` 上下文 (Rule 7) |
| REL-RACE-01-048 | `failure()` 不识别 | 平台不支持 `failure()` 函数 |
| USE-STAT-01-002 | `success()` 不识别 | 平台不支持此函数 |
| COMP-CTX-01-052 | `needs.verify.result` 复杂上下文 | 平台不支持 needs 上下文中的 status check 函数 |
| COMP-EXPR-01-058 | `!false`, `>`, `<`, `&&` 等运算符 | 部分运算符平台不支持 |
| USE-EXPR-01-002 | 未知函数调用 | 平台拒绝不存在的表达式函数 |
| COMPAT-CONCUR-01-001 | `cancel-in-progress` | concurrency 字段整体被平台拒绝 |
| COMPAT-CONCUR-01-003 | `cancel-in-progress` | 同上 |
| REL-PREEMPT-01-006 | preemption events 含 `push` | events 仅允许 `[mr_id]` |
| USE-CONC-01-002 | `max: -1` | max 须 ≥1 |
| REL-STEPS-01-042 | 50 steps | 平台限制 steps ≤ 16 |
| SEC-WCMD-01-003/004 | workflow 安全测试 | 安全校验层拒绝 |

### 3.6 修复率估算

| 类别 | 数量 | 百分比 |
|------|------|-------|
| 可直接修复（删除字段/修正格式） | ~50 | 69% |
| 需修正触发事件/types | ~7 | 10% |
| 不可修复（平台功能缺失） | ~15 | 21% |
| **总计 Invalid** | **72** | **100%** |

---

## 四、SKIP 案例建议

26 条 SKIP 案例全部因 `workflow: null` 导致无法脚本化，可分为两类：

### 4.1 需外部操作（非 workflow 系统测试）— 13 条

K8s 集群 (6)、Volcano Job (2)、安全审计/secret API 测试 (4)、新手走查 (1) -- 这些案例验证的是平台的管理面 API、K8s 对接、审计系统等，天然不适合用 workflow 自动化。建议维持 SKIP 状态，通过流水线 API 测试或手工验证。

### 4.2 文档验证测试 — 13 条

文档扫描/一致性测试（USE-DOC/EXPR/LBL/PATH/RES/UNKN/VARS/API/DIR 等）验证的是文档内容本身。这些可以通过独立的文档 Link Checker / Markdown Parser 自动化完成，无需通过 workflow 提交。建议维持 SKIP 状态，并用独立文档测试工具覆盖。

---

*生成日期: 2026-07-24 · 分析文件数: 98 (72 invalid + 26 SKIP)*
