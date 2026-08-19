# compat-diff agent 产出 — 兼容性差异 intents

> Run: 2026-08-18-01
> Agent: compat-diff
> 输入版本: gitcode-spec/ (2026-07-20 抓取), parity-matrix.md (2026-08-18), testing-focus.md (2026-08-18)

---

## 缺失输入清单及退化影响

| 缺失输入 | 期望内容 | 实际状态 | 退化影响 |
|---|---|---|---|
| `phase01/inputs/github-reference/` | GitHub Actions 官方语法/语义文档、安全加固手册 | 目录不存在，零文件 | **重大退化**：兼容性 diff 失去权威 oracle。所有「GitHub 侧预期」只能基于 `testing-focus.md` 中列出的 GitHub 惯例、Parity Matrix 标注、以及业界通用 Actions 知识推断，无法逐字核对官方语义。 |
| `phase01/inputs/workflow-samples/` | 真实开源 `.github/workflows/*.yml` 样本 | 目录不存在 | 中度退化：无法引用真实开源 workflow 中的常见写法来佐证「这种构造现实中高频」。差异发现偏理论推导，缺真实负载验证。 |
| `phase01/inputs/business-context/` | 迁移改造点清单、历史踩坑记录 | 目录不存在 | 中度退化：无法获取用户侧已知的迁移摩擦点，迁移路径上的盲区可能未覆盖。 |

> **纪律声明**：以下所有 intent 中「GitHub 侧预期」均标为「基于行业惯例/GitHub 通用语义推断」，非直接引自官方文档。若后续 `github-reference/` 补充，需重新审校 oracle。

---

## 扫描骨架

以 `testing-focus.md` §10 兼容性差异高发区为骨架，逐类展开：
1. 默认值/隐式行为差异
2. 表达式函数差异
3. 触发过滤语义差异
4. 上下文对象差异
5. 不支持能力的降级方式
6. 内置 action 差异
7. runner 标签/环境差异
8. 迁移摩擦（§11）

---

## INTENTS

### INTENT-COMPAT-001
- **具体差异点**: workflow 文件存放目录。GitHub 使用 `.github/workflows/`，GitCode 使用 `.gitcode/workflows/`。
- **GitHub 侧预期**: 将 `.yml`/`.yaml` 文件放在 `.github/workflows/` 下即被识别为 workflow。
- **GitCode 侧疑似行为**: 仅识别 `.gitcode/workflows/` 目录下的 `.yml`/`.yaml` 文件；`.github/workflows/` 下的文件被静默忽略。
- **oracle 对齐方向**: 差异确认（GitCode 有意不同，已在文档明确声明）。
- **触发条件**: 用户直接复制 GitHub 仓库的 `.github/workflows/` 目录到 GitCode 仓库，未重命名为 `.gitcode/workflows/`。
- **为什么有风险**: 这是迁移第一摩擦点。用户「开箱即搬」时 workflow 完全不触发，且平台不会报错指明「请放到 .gitcode/workflows/」，造成「为什么我的 CI 不跑」的困惑。
- **dimensions**: [compatibility, usability]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-002
- **具体差异点**: YAML 中未知/不支持字段的处理方式。GitHub 对未知字段通常报错或静默忽略的行为有明确文档；GitCode 文档未明确降级方式。
- **GitHub 侧预期**: 对 schema 外字段通常在校验阶段给出明确报错（如 "Unexpected property"）。
- **GitCode 侧疑似行为**: 疑似部分报错、部分静默忽略（文档未声明）。例如 `container` 字段已知当前不可用，但报错形态未明确。
- **oracle 对齐方向**: 一致性（对「大部分兼容」的能力，降级方式应与 GitHub 对齐——至少不能静默忽略而不告知）。
- **触发条件**: 用户从 GitHub 迁移包含 GitCode 尚未支持字段的 workflow（如 `container`、`services`、`environment`）。
- **为什么有风险**: 静默忽略会导致「看起来一样、行为不一样」——用户以为配置了某能力，实际未生效，引发生产行为偏离预期。
- **dimensions**: [compatibility, usability]
- **优先级**: P1（关联 RISK-COMPAT-01、RISK-USE-01）

### INTENT-COMPAT-003
- **具体差异点**: 核心上下文对象命名。GitHub 使用 `github.*`（如 `github.ref`、`github.sha`），GitCode 使用 `atomgit.*`。
- **GitHub 侧预期**: `${{ github.ref }}`、`${{ github.event_name }}`、`${{ github.sha }}` 等表达式可直接解析。
- **GitCode 侧疑似行为**: 上下文对象名为 `atomgit.*`；引用 `github.*` 可能解析为空字符串或报错。
- **oracle 对齐方向**: 差异确认（GitCode 有意不同，文档已声明）。需确认：若 workflow 中残留 `github.*`，平台是报错还是静默返回空值——后者更危险。
- **触发条件**: 直接迁移的 GitHub workflow 中仍包含 `${{ github.ref }}` 等表达式。
- **为什么有风险**: 直接搬运会导致所有 `github.*` 引用全线失效。若平台静默返回空字符串而非报错，用户可能在不知情的情况下执行错误逻辑（如空分支名导致部署到错误环境）。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01、RISK-COMPAT-02）

### INTENT-COMPAT-004
- **具体差异点**: 系统环境变量前缀。GitHub 使用 `GITHUB_*`（`GITHUB_SHA`、`GITHUB_REF`、`GITHUB_TOKEN` 等），GitCode 使用 `ATOMGIT_*`。
- **GitHub 侧预期**: Shell 脚本中 `$GITHUB_SHA`、`$GITHUB_REF`、`$GITHUB_TOKEN`、`$GITHUB_OUTPUT`、`$GITHUB_ENV`、`$GITHUB_PATH`、`$GITHUB_STEP_SUMMARY` 等可直接使用。
- **GitCode 侧疑似行为**: 对应变量为 `ATOMGIT_SHA`、`ATOMGIT_REF`、`ATOMGIT_TOKEN`、`ATOMGIT_OUTPUT`、`ATOMGIT_ENV`、`ATOMGIT_PATH`、`ATOMGIT_STEP_SUMMARY`。
- **oracle 对齐方向**: 差异确认（有意不同）。需确认：GitCode 是否同时提供 `GITHUB_*` 别名以兼容迁移——文档未提及。
- **触发条件**: 迁移的 shell 脚本或 action 代码中硬编码了 `GITHUB_*` 变量名。
- **为什么有风险**: 大量 GitHub action 和自定义脚本内部使用 `$GITHUB_OUTPUT` / `$GITHUB_ENV` 等文件协议。直接迁移会导致 step 输出传递、环境变量设置、PATH 追加全部失效。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-005
- **具体差异点**: 自动生成的 workflow token 名称。GitHub 使用 `secrets.GITHUB_TOKEN` / `env.GITHUB_TOKEN`，GitCode 使用 `secrets.ATOMGIT_TOKEN` / `env.ATOMGIT_TOKEN`。
- **GitHub 侧预期**: `${{ secrets.GITHUB_TOKEN }}` 在每个 workflow run 中自动注入。
- **GitCode 侧疑似行为**: 自动令牌为 `secrets.ATOMGIT_TOKEN`；文档未声明是否保留 `secrets.GITHUB_TOKEN` 别名。
- **oracle 对齐方向**: 差异确认（有意不同）。需确认是否有别名兼容。
- **触发条件**: 迁移 workflow 中引用 `${{ secrets.GITHUB_TOKEN }}` 进行 API 调用或 gh CLI 认证。
- **为什么有风险**: 几乎所有 GitHub workflow 都依赖 `GITHUB_TOKEN`。引用名错误会导致 API 调用 401/403，且报错信息可能不直观。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-006
- **具体差异点**: 状态函数的调用语法。GitHub 要求带括号 `success()` / `failure()` / `always()` / `cancelled()`；GitCode 使用无括号 `success` / `failed` / `always` / `cancelled`。
- **GitHub 侧预期**: `if: ${{ success() }}`、`if: ${{ failure() }}`、`if: ${{ always() }}` 是标准写法。
- **GitCode 侧疑似行为**: 需使用 `if: ${{ success }}`、`if: ${{ failed }}`、`if: ${{ always }}`。文档未明确：若用户写 `success()`，是兼容解析还是报错/忽略。
- **oracle 对齐方向**: 差异确认（有意不同）。需确认 GitCode 对带括号语法是「兼容解析」还是「拒绝/静默失败」——后者会导致条件 step 完全不执行。
- **触发条件**: 迁移 workflow 中仍使用 GitHub 风格的 `success()` / `failure()` 语法。
- **为什么有风险**: 条件执行是 workflow 核心控制流。若 `if: ${{ always() }}` 被静默忽略，清理 step 不会在失败时执行，导致资源泄漏。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-007
- **具体差异点**: 失败状态函数的名称。GitHub 使用 `failure()`，GitCode 使用 `failed`（无括号）。
- **GitHub 侧预期**: `if: ${{ failure() }}` 表示「任一前置步骤失败时执行」。
- **GitCode 侧疑似行为**: `if: ${{ failed }}`。若用户写 `failure()` 或 `failure`，行为未知。
- **oracle 对齐方向**: 差异确认（有意不同）。需验证 `failure` / `failure()` 在 GitCode 中的解析结果。
- **触发条件**: 迁移 workflow 中包含 `failure()` 的 step 条件。
- **为什么有风险**: 失败通知/回滚 step 是生产安全网。若条件解析失败导致通知 step 不执行，用户可能长时间不知道 CI 已失败。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-008
- **具体差异点**: 表达式函数 `contains`、`startsWith`、`endsWith`、`format`、`hashFiles`、`toJson` 的边界行为（空值处理、类型转换、大小写敏感）。
- **GitHub 侧预期**: 例如 `contains('', 'x')` 返回 `false`；`hashFiles('不存在的路径')` 返回空字符串；`toJson(null)` 返回 `'null'`。类型转换有明确规则。
- **GitCode 侧疑似行为**: 文档仅列出函数签名和简单示例，未描述边界行为。疑似部分边界与 GitHub 不一致。
- **oracle 对齐方向**: 一致性（对「大部分兼容」的能力，边界行为应与 GitHub 对齐；若有意不同需文档声明）。
- **触发条件**: workflow 中使用 `contains(atomgit.ref, 'release')`、`hashFiles('package-lock.json')` 等表达式，且输入处于边界状态（空字符串、文件不存在、null）。
- **为什么有风险**: 缓存 key 生成依赖 `hashFiles`。若文件不存在时返回行为与 GitHub 不同，会导致缓存命中/未命中策略偏离预期，影响构建正确性。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01、RISK-USE-02）

### INTENT-COMPAT-009
- **具体差异点**: 数字字面量的类型处理。历史用例显示 GitCode 将整数 `42` 解析为浮点 `42.0`（TC-163/TC-539 NEEDS-UPDATE）。
- **GitHub 侧预期**: `${{ 42 }}` 解析为整数 `42`；类型严格区分整数与浮点。
- **GitCode 侧疑似行为**: 疑似所有数字字面量统一为浮点类型（`42` → `42.0`）。这会导致 `==` 比较、矩阵变量展开等行为与预期不符。
- **oracle 对齐方向**: 一致性（数字类型处理应与 GitHub 一致）。
- **触发条件**: workflow 中使用整数进行条件比较（如 `matrix.version > 12`）或输出传递时下游期望整数类型。
- **为什么有风险**: 类型差异是隐蔽 bug 源。若 `42 != 42.0` 在某些比较场景成立，或矩阵索引计算出错，会导致条件判断意外失败。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01、RISK-USE-02）

### INTENT-COMPAT-010
- **具体差异点**: `pull_request` 事件的 `types` 取值命名。GitHub 使用 `opened` / `synchronize` / `reopened` / `closed` 等；GitCode 使用 `open` / `update` / `reopen` / `merge`，且默认值为 `[open, reopen, update]`。
- **GitHub 侧预期**: `types: [opened, synchronize, reopened]` 可正常触发。
- **GitCode 侧疑似行为**: 若 workflow 中写 GitHub 风格的 `opened` / `synchronize`，可能不被识别，导致 PR 事件不触发 workflow。
- **oracle 对齐方向**: 差异确认（有意不同）。需确认：GitCode 是否兼容识别 GitHub 的 type 名称作为别名。
- **触发条件**: 迁移 workflow 中包含 `pull_request: types: [opened, synchronize]` 等 GitHub 标准命名。
- **为什么有风险**: PR 触发器是 CI 的核心入口。类型名称不兼容会导致「PR 提交了但 CI 不跑」，开发者误以为配置错误。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-011
- **具体差异点**: `paths` 路径过滤的匹配上限。GitCode 文档声明「匹配前 300 个变更文件，超出部分不参与匹配判断」。
- **GitHub 侧预期**: GitHub 对 paths 过滤的变更文件数量无公开的 300 文件上限（业界惯例认为可处理大量变更）。
- **GitCode 侧疑似行为**: 单次 push/PR 变更文件超过 300 个时，仅前 300 个文件参与 paths 匹配，其余被忽略。
- **oracle 对齐方向**: 差异确认（GitCode 有意限制）。需确认：超出 300 文件时的行为是「剩余文件不触发」还是「workflow 整体不触发」。
- **触发条件**: 大规模重构（如批量重命名、依赖升级）导致单次 push 变更文件数 > 300，且 workflow 配置了 `paths` 过滤。
- **为什么有风险**: 若关键路径的文件排在 300 名之后，workflow 本应触发却不触发，导致必要的 CI 检查被跳过，可能让有问题的代码合入主干。
- **dimensions**: [compatibility, reliability]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-012
- **具体差异点**: `schedule` cron 触发语义。GitCode 声明最短间隔 5 分钟、UTC 时区、仅默认分支生效。
- **GitHub 侧预期**: GitHub Actions 的 schedule 最短间隔 5 分钟、UTC、仅默认分支——表面一致，但调度延迟和 cron 解析边界行为可能不同。
- **GitCode 侧疑似行为**: 历史用例显示 Scheduler 当前不工作（TC-237 等 NEEDS-UPDATE）。即使修复后，调度延迟「数分钟」的边界、以及特殊 cron 符号（`,` `-` `/`）的解析行为待验证。
- **oracle 对齐方向**: 一致性（对标准 cron 语义应与 GitHub 一致）。
- **触发条件**: 配置 `schedule: cron: '*/5 * * * *'` 或包含特殊符号的 cron 表达式。
- **为什么有风险**: 定时任务是 nightly build、安全扫描等场景的基础设施。若调度不工作或 cron 解析与预期不符，会导致关键定时任务漏执行。
- **dimensions**: [compatibility, reliability]
- **优先级**: P1（关联 RISK-COMPAT-01、RISK-USE-02）

### INTENT-COMPAT-013
- **具体差异点**: `workflow_dispatch` 与 `workflow_call` 的 `inputs` 类型支持。GitCode 仅支持 `string` 类型；GitHub 支持 `boolean`、`choice`、`number`、`environment`。
- **GitHub 侧预期**: `type: boolean` 可渲染为勾选框，`type: choice` 可渲染为下拉框，`type: number` 限制为数字输入。
- **GitCode 侧疑似行为**: 所有 inputs 均为 string。若 workflow 写 `type: boolean`，可能报错或被降级为 string。
- **oracle 对齐方向**: 差异确认（GitCode 有意限制）。需确认降级方式：是解析报错，还是静默按 string 处理。
- **触发条件**: 迁移 workflow 中包含 `type: boolean` / `choice` / `number` 的 `workflow_dispatch.inputs`。
- **为什么有风险**: 若静默降级为 string，`true` / `false` 变成字符串后在表达式中 `${{ inputs.dry_run == true }}` 会恒为 `false`，导致部署逻辑被错误执行。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-014
- **具体差异点**: `workflow_call`（可重用 workflow）的嵌套层数上限。GitCode 最多 2 层；GitHub 最多 4 层。
- **GitHub 侧预期**: 可重用 workflow A 调用 B，B 调用 C，C 调用 D（共 4 层嵌套）可正常执行。
- **GitCode 侧疑似行为**: 嵌套超过 2 层时报错或拒绝执行。
- **oracle 对齐方向**: 差异确认（GitCode 有意限制）。
- **触发条件**: 组织内存在分层抽象的可重用 workflow（如「基础构建」→「语言特定构建」→「项目特定构建」→「项目子模块构建」）。
- **为什么有风险**: 大型企业通常有多层复用抽象。层数限制会导致现有 GitHub 可重用 workflow 架构在迁移时需扁平化重构，增加迁移成本。
- **dimensions**: [compatibility]
- **优先级**: P2（关联 RISK-COMPAT-01）

### INTENT-COMPAT-015
- **具体差异点**: `stages` 阶段机制。GitCode 特有「阶段间串行、阶段内并行、fail_fast」的顶层 `stages` 字段；GitHub 无此概念，仅通过 `needs` 构建 DAG。
- **GitHub 侧预期**: 不存在 `stages` 字段；所有 job 默认并行，依赖通过 `needs` 显式声明。
- **GitCode 侧疑似行为**: 支持 `stages` 作为可选顶层字段。当 workflow 包含 `stages` 时，job 需嵌套在 stage 内；无 `stages` 时所有 job 默认并行（与 GitHub 类似）。
- **oracle 对齐方向**: 差异确认（GitCode 扩展能力）。需验证：GitHub 风格的纯 `jobs` 顶层结构在 GitCode 中是否 100% 等价执行——尤其是 `needs` 跨 stage 的行为。
- **触发条件**: 用户在 GitCode 中混合使用 `stages` 和 `needs`，或从 GitHub 迁移纯 `jobs` 结构。
- **为什么有风险**: 若 `needs` 引用了跨 stage 的 job，GitCode 的串行约束可能与 GitHub 的纯 DAG 调度产生时序差异，导致执行顺序偏离预期。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-016
- **具体差异点**: `post` 后处理阶段。GitCode 特有顶层 `post` 字段，默认 `run_always: true`；GitHub 无等价顶层字段（仅在 action 内定义 `post`）。
- **GitHub 侧预期**: 不存在 workflow 级别的 `post`；全局清理/通知需通过 `if: always()` 在最后 job 中实现。
- **GitCode 侧疑似行为**: `post` 在 workflow 终态后执行，无论成功失败默认都执行。
- **oracle 对齐方向**: 差异确认（GitCode 扩展能力）。需验证：GitHub 迁移来的 workflow 若包含自定义 action 的 `post` step，该 `post` 是在 action 级别执行（与 GitHub 一致）还是在 workflow 级别被重新解释。
- **触发条件**: 使用包含 `post` 的自定义 action，或在 GitCode 中显式使用顶层 `post`。
- **为什么有风险**: 若 action 内 `post` 的行为被平台重新解释（如执行时机、环境变量可见性变化），可能导致自定义 action 的清理逻辑异常。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-017
- **具体差异点**: `concurrency` 并发控制语法与语义。GitHub 使用 `concurrency: group: ... cancel-in-progress: true`；GitCode 使用 `concurrency: enable: true max: 3 exceed-action: QUEUE preemption: ...`。
- **GitHub 侧预期**: 通过 `group` 字符串标识并发组，`cancel-in-progress` 控制是否取消同组旧运行。
- **GitCode 侧疑似行为**: 通过 `max` 数值限制并发数（1-5），`exceed-action` 控制超出时排队或忽略，`preemption.events` 控制抢占事件。
- **oracle 对齐方向**: 差异确认（语法完全不同）。需验证：功能覆盖度是否等价——GitHub 的「同 branch + workflow 名」group 语义在 GitCode 中如何表达。
- **触发条件**: 迁移 workflow 中包含 `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` 等 GitHub 标准写法。
- **为什么有风险**: 并发控制是部署安全的关键（防止并行部署冲突）。语法不兼容且语义可能不等价，直接迁移可能导致并发控制失效。
- **dimensions**: [compatibility, reliability]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-018
- **具体差异点**: `permissions` 权限域命名。GitHub 使用 `contents`、`pull-requests`、`issues`、`actions`、`checks`、`deployments` 等；GitCode 使用 `repository`、`pr`、`issue`、`note`、`project`、`hook`。
- **GitHub 侧预期**: `permissions: contents: read`、`permissions: pull-requests: write` 等标准命名可被解析。
- **GitCode 侧疑似行为**: 仅识别 `repository`/`pr`/`issue`/`note`/`project`/`hook`。使用 GitHub 命名可能报错或静默无效。
- **oracle 对齐方向**: 差异确认（有意不同）。需确认：GitCode 是否提供 GitHub 命名的别名映射。
- **触发条件**: 迁移 workflow 中包含 `permissions: contents: read` 或 `permissions: pull-requests: write`。
- **为什么有风险**: 权限声明是安全最小授权的核心。若 `permissions` 字段被静默忽略，TOKEN 会回退到仓库默认权限（可能过宽），导致最小授权原则被破坏。
- **dimensions**: [compatibility, security]
- **优先级**: P1（关联 RISK-COMPAT-01、RISK-SEC-06）

### INTENT-COMPAT-019
- **具体差异点**: `permissions` 默认权限范围。GitHub 默认权限可由仓库/组织设置控制，且默认趋向于受限；GitCode 文档称「使用仓库设置中定义的权限」，但未明确默认值。
- **GitHub 侧预期**: 新仓库默认 `permissions` 趋向 `read` 或更严格；未声明 `permissions` 时的行为有明确文档。
- **GitCode 侧疑似行为**: 默认值未在公开文档中明确。可能默认较宽（如 `write-all`），或继承仓库设置的未知默认值。
- **oracle 对齐方向**: 一致性（默认权限语义应与 GitHub 对齐，或至少文档明确声明）。
- **触发条件**: workflow 未声明 `permissions` 字段，依赖默认值运行。
- **为什么有风险**: 默认值差异是「静默行为变更」的典型场景。若 GitCode 默认权限比 GitHub 更宽，迁移后同一 workflow 会获得超出预期的写权限，增加安全风险。
- **dimensions**: [compatibility, security]
- **优先级**: P1（关联 RISK-COMP-02、RISK-SEC-06）

### INTENT-COMPAT-020
- **具体差异点**: `runs-on` Runner 标签体系。GitHub 使用单标签或标签数组（`ubuntu-latest`、`windows-latest`、`macos-latest`、[self-hosted, linux, x64]）；GitCode 使用三段式 `{os-version,arch,flavor}` 或数组形式。
- **GitHub 侧预期**: `runs-on: ubuntu-latest` 或 `runs-on: [self-hosted, linux, x64]` 可直接匹配 Runner。
- **GitCode 侧疑似行为**: 官方 Runner 需 `{ubuntu-24,x64,small}` 或 `[ubuntu-latest, x64, small]`；`ubuntu-latest` 单标签疑似不被识别为完整匹配。
- **oracle 对齐方向**: 差异确认（有意不同）。需确认：GitHub 风格的 `runs-on: ubuntu-latest` 在 GitCode 中是报错、降级为 `default`，还是尝试匹配。
- **触发条件**: 迁移 workflow 中写 `runs-on: ubuntu-latest` 或 `runs-on: windows-latest`。
- **为什么有风险**: 几乎所有 GitHub workflow 都使用 `ubuntu-latest`。若该写法在 GitCode 中报错，意味着 100% 的迁移 workflow 都需要修改此字段。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01）

### INTENT-COMPAT-021
- **具体差异点**: `runner` 上下文字段值格式。历史用例显示 GitCode `runner.os` 返回 `linux`（小写），`runner.arch` 返回 `x86_64`；GitHub 返回 `Linux`（首字母大写）和 `X64`。
- **GitHub 侧预期**: `runner.os` = `Linux` / `Windows` / `macOS`；`runner.arch` = `X64` / `ARM64` / `ARM`。
- **GitCode 侧疑似行为**: `runner.os` = `linux` / `windows` / `macos`（小写）；`runner.arch` = `x86_64` / `arm64`（小写或下划线分隔）。
- **oracle 对齐方向**: 一致性（值格式应与 GitHub 对齐，或文档明确声明差异）。
- **触发条件**: workflow 中通过 `runner.os == 'Linux'` 或 `runner.arch == 'X64'` 做条件分支。
- **为什么有风险**: 大小写敏感的字符串比较会导致条件恒为 `false`。若某 step 仅在 Linux 下执行安全加固脚本，条件误判会导致该脚本在所有 OS 上被跳过或错误执行。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-02、RISK-USE-02）

### INTENT-COMPAT-022
- **具体差异点**: 默认 shell 选择。GitHub 有明确的按 OS 默认 shell 规则（Linux/macOS 默认 `bash`，Windows 默认 `pwsh`）；GitCode 文档未明确 `run` 步骤的默认 shell。
- **GitHub 侧预期**: 未声明 `shell` 时，Linux/macOS 使用 `bash -e {0}`，Windows 使用 `pwsh -command ". '{0}'"`。
- **GitCode 侧疑似行为**: 文档未声明默认值。可能默认 `bash`，也可能因 Runner 镜像配置而不同。
- **oracle 对齐方向**: 一致性（默认 shell 应与 GitHub 对齐）。
- **触发条件**: `run` 步骤未显式声明 `shell`，依赖默认值执行脚本。
- **为什么有风险**: 默认 shell 差异是差异高发区。若 Windows Runner 默认使用 `cmd` 而非 `pwsh`，PowerShell 语法会报错；若默认不带 `-e`（errexit），脚本出错不会中断 step，导致「失败被静默忽略」。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMP-02）

### INTENT-COMPAT-023
- **具体差异点**: `secrets` 日志脱敏（masking）强度。GitCode 文档自承 `echo "${{ secrets.X }}"` 可能绕过脱敏机制。
- **GitHub 侧预期**: GitHub 对 secret 脱敏有多层机制，包括值匹配、base64 变形检测、多行 secret 处理；直接 `echo ${{ secrets.X }}` 通常也会被遮蔽。
- **GitCode 侧疑似行为**: 疑似仅对直接 secret 值进行简单字符串替换，对拼接、base64、多行变形的遮蔽可能不完整。
- **oracle 对齐方向**: 一致性（secret 脱敏是安全基线，应与 GitHub 对齐）。
- **触发条件**: step 中意外执行 `echo "${{ secrets.MY_TOKEN }}"`、`echo "prefix-${{ secrets.MY_TOKEN }}-suffix"`、或 `echo $MY_TOKEN`（从 env 注入）。
- **为什么有风险**: Secret 泄露是 P0 级安全命脉。若脱敏机制可被轻易绕过，任何打印环境变量或调试输出的 step 都可能将部署密钥泄露到公开日志中。
- **dimensions**: [compatibility, security]
- **优先级**: P0（关联 RISK-SEC-05）

### INTENT-COMPAT-024
- **具体差异点**: `pull_request_target` 事件下 `checkout` action 的默认代码来源。GitCode 文档声明「checkout 默认代码来源为 base 分支」；GitHub 的 `actions/checkout@v4` 在 `pull_request_target` 下默认也检出 base 分支，但参数和行为细节可能不同。
- **GitHub 侧预期**: `pull_request_target` 下 `actions/checkout` 默认检出 base 分支；若显式设置 `ref: ${{ github.event.pull_request.head.sha }}` 则检出 PR 代码。
- **GitCode 侧疑似行为**: 文档同样声明默认检出 base 分支，且可通过 `ref: ${{ atomgit.event.pull_request.head.sha }}` 切换。但隔离强度、TOKEN 权限范围、以及 checkout 后环境变量的注入是否与 GitHub 一致待验证。
- **oracle 对齐方向**: 一致性（安全隔离语义应与 GitHub 一致）。
- **触发条件**: 使用 `pull_request_target` 事件并在 workflow 中调用 checkout，随后执行构建/测试脚本。
- **为什么有风险**: `pull_request_target` 是最危险的 Actions 特性之一。若隔离强度弱于 GitHub（如 TOKEN 权限未正确降级、secret 未隔离），恶意 PR 可窃取凭证或修改仓库。
- **dimensions**: [compatibility, security]
- **优先级**: P0（关联 RISK-SEC-01、RISK-SEC-03）

### INTENT-COMPAT-025
- **具体差异点**: `cache` action 在 fork PR 场景下的隔离策略。GitHub 明确 fork PR 只能读取 cache、不能写入，防止 cache 投毒；GitCode 文档未明确 cache 隔离策略。
- **GitHub 侧预期**: fork 来源的 `pull_request` 触发可读取主分支 cache，但写入的 cache 仅对该 fork 可见，不会污染主分支 cache。
- **GitCode 侧疑似行为**: 文档未声明。疑似可能允许 fork PR 写入主分支可见的 cache，或完全不允许 fork PR 使用 cache。
- **oracle 对齐方向**: 一致性（cache 隔离是供应链安全基线，应与 GitHub 对齐）。
- **触发条件**: 来自 fork 的 PR 触发 workflow，且 workflow 中包含 `uses: cache` step。
- **为什么有风险**: 若 fork PR 可写入主分支 cache，攻击者可通过构造恶意依赖缓存（如替换 npm 包为恶意版本）污染后续主分支构建，构成供应链攻击。
- **dimensions**: [compatibility, security]
- **优先级**: P1（关联 RISK-SEC-04）

### INTENT-COMPAT-026
- **具体差异点**: 内置 action 的引用写法。GitHub 使用 `actions/checkout@v4`、`actions/setup-node@v4` 等带 owner+版本；GitCode 使用无 owner 短名 `checkout`、`setup-node`，且未明确版本机制。
- **GitHub 侧预期**: `uses: actions/checkout@v4` 锁定到具体版本；`@main` 或 `@v4` 为浮动引用。
- **GitCode 侧疑似行为**: `uses: checkout` 为短名引用，文档未说明版本锁定机制。可能始终使用平台内置的最新版本，或版本不可控。
- **oracle 对齐方向**: 差异确认（有意不同）。需验证：GitHub 风格的 `actions/checkout@v4` 在 GitCode 中是报错、忽略，还是通过别名映射。
- **触发条件**: 迁移 workflow 中包含 `uses: actions/checkout@v4`、`uses: actions/cache@v4` 等标准写法。
- **为什么有风险**: 版本锁定是供应链安全的关键实践。若无法锁定 action 版本，平台 action 的升级可能引入破坏性变更，导致原有 workflow 突然失败。
- **dimensions**: [compatibility, security]
- **优先级**: P1（关联 RISK-COMPAT-01、RISK-SEC-07）

### INTENT-COMPAT-027
- **具体差异点**: 废弃 workflow 命令的降级方式。GitHub 已废弃 `::set-output`、`::set-env`、`::add-path`，推荐文件写入协议；GitCode 同样声明废弃。但历史用例显示 `::set-output` 在 GitCode 中「已知 FAIL」。
- **GitHub 侧预期**: 废弃命令在 GitHub 中仍可向后兼容执行一段时间，并打印 deprecation warning。
- **GitCode 侧疑似行为**: 疑似直接拒绝执行（FAIL），无向后兼容期。文档未明确降级方式。
- **oracle 对齐方向**: 一致性（若 GitCode 宣称「大部分兼容」，废弃命令至少应给出可操作的错误提示，而非静默失败）。
- **触发条件**: 迁移的旧版 workflow 或第三方 action 中仍使用 `::set-output`、`::set-env`、`::add-path`。
- **为什么有风险**: 大量存量 GitHub workflow 和旧版第三方 action 仍使用这些命令。若 GitCode 直接拒绝且无明确报错，用户难以定位失败原因。
- **dimensions**: [compatibility, usability]
- **优先级**: P1（关联 RISK-COMPAT-01、RISK-USE-01）

### INTENT-COMPAT-028
- **具体差异点**: 迁移报错质量。用户直接搬运 GitHub workflow 到 GitCode 时，平台报错是否能指明「这是 GitCode 不支持/需改写」而非泛化报错。
- **GitHub 侧预期**: 不适用（这里是 GitCode 的易用性 oracle）。
- **GitCode 侧疑似行为**: 疑似对不兼容语法给出泛化 YAML 解析错误（如 "Unknown property"），而不指明「GitCode 使用 atomgit.* 而非 github.*」或「GitCode 使用 .gitcode/workflows/ 目录」。
- **oracle 对齐方向**: 差异确认（GitCode 的易用性能力）。
- **触发条件**: 将包含 `github.*` 上下文、`.github/workflows/` 目录、`success()` 语法、`permissions: contents: read` 的 GitHub workflow 直接放入 GitCode 仓库。
- **为什么有风险**: 报错质量直接决定迁移成本。若报错无法指向具体差异点，用户需要逐行对比文档排查，迁移摩擦极高。
- **dimensions**: [compatibility, usability]
- **优先级**: P0（关联 RISK-USE-01、RISK-USE-02）

### INTENT-COMPAT-029
- **具体差异点**: `jobs` 顶层字段与 `stages` 嵌套的结构兼容性。GitHub 仅有顶层 `jobs`；GitCode 可选顶层 `stages`，`jobs` 可嵌套在 `stages` 内，也可作为顶层字段（无 stages 时）。
- **GitHub 侧预期**: `jobs:` 必须作为 workflow 的顶层字段，所有 job 定义在 `jobs` 下。
- **GitCode 侧疑似行为**: 无 `stages` 时支持顶层 `jobs`（与 GitHub 兼容）；有 `stages` 时 `jobs` 需嵌套在 stage 内。
- **oracle 对齐方向**: 一致性（无 stages 时，顶层 jobs 结构应与 GitHub 100% 等价）。
- **触发条件**: 迁移的 GitHub workflow 不含 `stages`，直接使用顶层 `jobs`。
- **为什么有风险**: 这是迁移的「最小兼容面」。若最简单的「无 stages、纯 jobs」结构都不能与 GitHub 等价执行，意味着任何迁移都需要改写 workflow 结构。
- **dimensions**: [compatibility]
- **优先级**: P1（关联 RISK-COMPAT-01）

---

## 覆盖度自检

| 差异类别 | §10 骨架项 | 覆盖 intent | 备注 |
|---|---|---|---|
| 默认值差异 | 默认 shell、默认 permissions、默认并发 | 019, 022, 017 | |
| 表达式函数差异 | 同名函数边界、类型转换、空值处理 | 006, 007, 008, 009 | |
| 触发过滤语义差异 | paths/branches 通配、事件负载字段命名 | 010, 011, 012 | |
| 上下文对象差异 | `github.*` 字段是否齐全、值格式 | 003, 004, 005, 021 | |
| 不支持能力的降级方式 | 报错 vs 静默忽略 vs 部分支持 | 002, 013, 014, 027 | |
| 内置 action 差异 | checkout、cache 等对应实现 | 024, 025, 026 | |
| runner 标签/环境差异 | `runs-on` 取值、预装软件版本 | 020, 021, 022 | |
| 迁移摩擦（§11） | 开箱能跑多少、报错指引、文档差异 | 001, 028, 029 | |
| 编排模型差异 | stages、post、concurrency | 015, 016, 017 | |
| 权限模型差异 | permissions 命名、默认值 | 018, 019 | |

**总计**: 29 条 intents，符合 20-35 条控制要求。

**按优先级分布**:
- P0: 3 条（023, 024, 028）
- P1: 25 条
- P2: 1 条（014）

**风险登记册覆盖检查**:
- RISK-COMPAT-01 (P1): 覆盖 001~029 中绝大多数
- RISK-COMPAT-02 (P1): 覆盖 003, 004, 005, 021
- RISK-COMP-02 (P1): 覆盖 019, 022
- RISK-USE-01 (P1): 覆盖 002, 028
- RISK-USE-02 (P0): 覆盖 008, 009, 021, 023, 028
- RISK-SEC-01 (P0): 覆盖 024
- RISK-SEC-03 (P0): 覆盖 024
- RISK-SEC-04 (P1): 覆盖 025
- RISK-SEC-05 (P0): 覆盖 023
- RISK-SEC-06 (P0): 覆盖 018, 019
- RISK-SEC-07 (P1): 覆盖 026

**溯源链闭合**: 每条 intent 均可追溯到 Parity Matrix 的 🟡/❌/❓ 项 或 COMPAT-NOTES.md 的具体条目 或 testing-focus.md 的章节。
