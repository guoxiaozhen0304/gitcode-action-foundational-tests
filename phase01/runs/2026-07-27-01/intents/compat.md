# compat-diff Agent 产出 · 兼容性差异 Intent 清单（增量）

> Run: 2026-07-27-01
> Agent: compat-diff
> 输入版本: phase01/inputs/gitcode-spec/（54 文件，抓取于 2026-07-20）; phase01/inputs/github-reference/（13 文件，抓取于 2026-07-20）; phase01/inputs/workflow-samples/（12 文件）; phase01/baseline/parity-matrix.md（2026-07-22）; phase01/baseline/risk-register.md（2026-07-21）; phase01/testing-focus.md（当前工作树）
> 基底: runs/2026-07-23-01/intents/compat.md（INTENT-COMPAT-001~035 + INTENT-COMPAT-NEW-001~012，已 delivered）; baseline/case-base-detail.md（2026-07-21）

---

## 一、与上一轮的关系（增量说明）

上一轮（2026-07-23-01）已按 testing-focus.md §10 的 7 大差异类别产出 35 条主系列 + 12 条回填 NEW 系列。本轮以**全集原则 + 基底加速**做增量发散，不重复已有覆盖：

- 本轮 18 条全部为**新增**（INTENT-COMPAT-036 ~ INTENT-COMPAT-053），ID 接续主系列，不与 001~035、NEW-001~012 冲突。
- 与旧 intent 存在邻近关系处，均在条目内显式注明（如 038↔011、041↔NEW-006、042↔NEW-009、046↔NEW-008、047↔NEW-011、048↔NEW-010、053↔030、040↔016/017）。
- 本轮新增发掘手段：(a) 对 GitCode spec 54 文件做**规格内部自相矛盾扫描**（发现 atomgit.actor、runs-on 自托管双形态、needs 上下文三处矛盾）；(b) 对 github-reference 13 文件逐节比对**未被上轮覆盖的章节**（workflow-commands 注解命令、events.md 全量事件表与平台限额、variables.md 的 RUNNER_* 系列）；(c) 函数级语义逐行 diff（发现 startsWith/endsWith 大小写敏感性**直接矛盾**——GitHub 不区分、GitCode 文档明写区分）。

### 差异类别增量覆盖

| 差异类别（§10） | 上轮覆盖 | 本轮增量 |
|---|---|---|
| 1. 默认值差异 | 001~003 | —（已足） |
| 2. 表达式函数差异 | 004~010 | 036、050 |
| 3. 触发过滤语义差异 | 011~015 | 037、038、039、051、052 |
| 4. 上下文对象差异 | 016~020 | 040、041、044 |
| 5. 不支持能力降级 | 021~023、NEW-001/002/010 | 037、042、045、048、049、053 |
| 6. 内置 action 差异 | 024~026 | 045、047、048 |
| 7. runner 标签/环境差异 | 027~028、NEW-008/011 | 044、046、047 |
| 8. 安全默认值/保护语义 | 002、030、032、033 | 043、053 |
| 9. 平台边界限额（新增子类） | 012（paths 300） | 051、052 |

---

## 二、输入退化标注

| 输入目录 | 退化状态 | 影响说明 |
|---|---|---|
| `inputs/workflow-samples/` | ⚠️ 仅 12 个 GitCode 项目样本（cann 7 + op-plugin 1 + testorg 3 + README），无真实 GitHub 侧开源 workflow 样本 | 「现实中常见」佐证仍以 GitHub 官方文档描述的生态惯例（如 labeled bot、`uses: actions/*` 引用）替代真实负载统计 |
| `inputs/business-context/` | ⚠️ 仅 README.md | 迁移摩擦类 intent 缺业务侧实证 |
| `runs/2026-07-27-01/intents/spec.md` | ⚠️ 本 run spec-analyst 产出尚未就绪（并行发散） | 能力项坐标以 baseline/parity-matrix.md（2026-07-22）为准 |

---

## 三、Intent 列表（全部为新增）

---

```
意图 ID:    INTENT-COMPAT-036
维度标签:   [compatibility]
标题:       startsWith/endsWith 大小写敏感性直接矛盾：GitHub 不区分 vs GitCode 文档明写「区分大小写」

风险点:     GitHub 官方语义明确 startsWith/endsWith「is not case sensitive」且 cast values to string；GitCode expressions.md 明确写「startsWith/endsWith：纯字符串操作，区分大小写」。这是两侧文档级直接矛盾，且属于「看起来一样、行为不一样」的最危险形态：迁移的 workflow 中 `if: startsWith(github.ref, 'Refs/Tags/')` 或 release 分支匹配（如 `startsWith(github.ref_name, 'Release-')`）在 GitHub 上为 true，在 GitCode 上静默翻转为 false，发布/部署步骤被跳过且无任何报错。分支/标签命名大小写在真实项目中极不统一（release/Release/RELEASE 并存），命中概率高。
预期系统行为: 确认为有意差异后：GitCode 维持区分大小写可实现，但必须在迁移指引中显著声明，并建议在差异确认后回写 Parity Matrix 作为该点权威 oracle；若实测结果为不区分大小写（与文档矛盾），则以实测为准并修正文档。
Oracle 来源: GitHub行为 | GitCode规格（文档已声明差异 → 差异确认后回写 Parity Matrix）

验证要点:
  - [正向] `startsWith('Hello World', 'hello')`：GitHub 语义为 true；GitCode 实测值需与自身文档（区分大小写 → false）一致
  - [正向] `endsWith(atomgit.ref_name, '.RC')` 对 `v1.0.rc` 的求值结果与文档声明一致
  - [负向] 不应出现文档声明与实际求值不一致（文档说区分、实测不区分，或反之）
  - [非功能] 差异确认后须在 Parity Matrix 回写，迁移指引中给出显式提示

对齐方向:   差异确认
优先级线索: RISK-COMPAT-01（P1：条件静默翻转，无报错，概率高）
破坏级别:   none
与旧 ID 关系: 新增；与 INTENT-COMPAT-006（contains 大小写）互补——006 是 GitCode 文档未明，本条是两侧文档直接矛盾
来源输入:   github-reference/reference/expressions.md（startsWith/endsWith: not case sensitive）; gitcode-spec/syntax-reference/expressions.md（「纯字符串操作，区分大小写」）
```

---

```
意图 ID:    INTENT-COMPAT-037
维度标签:   [compatibility, usability]
标题:       GitHub 全量事件集（release/issues/workflow_run/create/delete/label 等 20+ 种）在 GitCode 的降级方式

风险点:     GitHub 支持 25+ 触发事件（release、issues、workflow_run、create、delete、label、milestone、pull_request_review、registry_package、repository_dispatch、status、watch 等）；GitCode 仅支持 8 种（push/pull_request/pull_request_target/issue_comment/pull_request_comment/workflow_dispatch/workflow_call/schedule）。迁移含 `on: release: types: [published]` 的发布 workflow 时，GitCode 的降级方式未知：解析报错 / 静默保存但永不触发 / 部分映射。静默永不触发是最差形态——用户以为发布流水线已就位，实际发版时无任何运行且无提示。release 与 workflow_run 是 GitHub 生态发布与链式编排的主流机制，命中面广。
预期系统行为: GitCode 对不支持的事件名应在保存/解析阶段明确报错，报错信息列出受支持的 8 种事件及迁移建议（如 release 场景改用时 push tags 过滤 + 手动 dispatch）；不应静默接受后永不触发。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [负向] `on: release` / `on: workflow_run` / `on: issues` 的 workflow 不应被静默保存且永无触发记录
  - [正向] 解析/保存阶段的报错应包含「事件 X 不受支持」及受支持事件清单
  - [非功能] 报错可理解性：是否指明「GitCode 差异」而非泛化 YAML 错误；eval: llm_assisted

对齐方向:   差异确认
优先级线索: RISK-USE-01（P1：迁移核心路径静默失效）
破坏级别:   none
与旧 ID 关系: 新增；INTENT-COMPAT-011/NEW-004 覆盖的是「同名事件的 types 取值差异」，本条覆盖「事件本身不存在」的更大半径
来源输入:   github-reference/reference/events.md（Other events full list：25+ 事件）; gitcode-spec/syntax-reference/trigger-events.md（仅 8 种事件）
```

---

```
意图 ID:    INTENT-COMPAT-038
维度标签:   [compatibility]
标题:       pull_request 扩展 activity types 降级：GitHub 20+ 种（labeled/review_requested/ready_for_review…）vs GitCode 仅 4 种

风险点:     GitHub pull_request 支持 20+ activity types，其中 `labeled`/`unlabeled`（标签驱动自动化）、`ready_for_review`（draft 转正式触发 CI）、`review_requested`、`converted_to_draft` 是社区 bot 与质量门禁 workflow 的高频用法；GitCode 仅有 open/reopen/update/merge 四种。迁移的 workflow 写 `types: [labeled]` 时行为未知：解析报错 / 静默忽略该 type 导致全量触发 / 静默不触发。三者风险各异：全量触发浪费资源且可能误执行部署类 job；不触发则标签自动化整体失效。
预期系统行为: 对 GitCode 不支持的 pull_request types 值，应在解析阶段明确报错并列出合法值（open/reopen/update/merge）；不应静默忽略（导致 types 过滤失效全量触发），也不应静默接受后永不触发。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [负向] `types: [labeled]` 不应被静默忽略退化为「所有 PR 活动都触发」
  - [负向] `types: [ready_for_review]` 不应被静默接受后任何事件都不触发且无提示
  - [正向] 报错信息应列出 GitCode 合法的 4 种 types
  - [正向] 合法 4 种 types 的触发语义与命名映射（update≈synchronize）保持正确

对齐方向:   差异确认
优先级线索: RISK-COMPAT-01（P1）+ RISK-USE-01（迁移报错质量）
破坏级别:   none
与旧 ID 关系: 新增；INTENT-COMPAT-011 覆盖「同名 type 的命名差异」（opened vs open），本条覆盖「GitHub 有而 GitCode 完全无对应」的 type 类别，二者互补不重叠
来源输入:   github-reference/reference/events.md（pull_request activity types 全表 20+ 项）; gitcode-spec/syntax-reference/trigger-events.md（types 仅 4 种）; testing-focus.md §2
```

---

```
意图 ID:    INTENT-COMPAT-039
维度标签:   [compatibility]
标题:       pull_request 事件的 ref/sha/workflow 来源语义：GitHub merge commit 模型 vs GitCode 未明确

风险点:     GitHub pull_request 事件下：GITHUB_REF=refs/pull/<N>/merge、GITHUB_SHA=merge commit（head 与 base 的试合并结果）、workflow 文件取自 merge commit，且 **PR 存在合并冲突时不触发**。GitCode 文档未说明 atomgit.ref/atomgit.sha 在 pull_request 下的指向（head sha？试合并 sha？base sha？），也未说明冲突时是否触发。若 GitCode 直接以 head.sha 运行，CI 验证的是「源分支现状」而非「合并后的结果」，会出现「PR 上全绿、合并后主干即红」的静默语义降级；冲突时触发则会跑在一个无法合并的状态上。checkout 默认检出哪个 ref 与此强耦合。
预期系统行为: 确认 GitCode pull_request 下 atomgit.sha/ref 的确切语义；若与 GitHub merge commit 模型不同，属重大差异，必须文档化并回写 Parity Matrix；合并冲突时的触发策略应明确。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [正向] pull_request 触发时观测 atomgit.sha / atomgit.ref / ATOMGIT_SHA 的实际取值，与 PR head sha、base sha 逐一比对定位语义
  - [负向] 不应出现「checkout 检出的代码版本」与「atomgit.sha 指向的版本」不一致
  - [正向] 存在合并冲突的 PR：触发行为与 GitHub（不触发）对齐，或差异被明确文档化
  - [非功能] 语义确认后回写 Parity Matrix 作为该点 oracle

对齐方向:   一致性（GitCode 未声明差异，默认应与 GitHub merge commit 模型对齐；若实测不同则升级为差异确认并文档化）
优先级线索: RISK-COMPAT-01（P1：CI 验证对象错误属静默语义降级，影响所有 PR 流水线）
破坏级别:   fixture（需构造含合并冲突的 PR 夹具）
与旧 ID 关系: 新增；INTENT-COMPAT-032 覆盖 pull_request_target 的权限/secret 隔离面，本条覆盖 pull_request 的代码版本语义面，正交互补
来源输入:   github-reference/reference/events.md（pull_request: GITHUB_SHA=merge commit、merge conflict 不触发）; gitcode-spec/syntax-reference/context.md（atomgit.sha 仅「触发提交的 SHA」，未分事件说明）; gitcode-spec/syntax-reference/trigger-events.md
```

---

```
意图 ID:    INTENT-COMPAT-040
维度标签:   [compatibility]
标题:       atomgit 上下文字段级差距：actor 规格自相矛盾 + job/run_attempt/triggering_actor/ref_protected 缺位

风险点:     (a) GitHub `github.actor`（触发者）是最高频上下文字段之一，广泛用于 bot 过滤（`if: github.actor != 'dependabot[bot]'`）、部署审批条件、通知文案；GitCode context.md 的 atomgit 属性表**没有 actor**，但官方另两页文档（view-job-logs.md、configure-conditional-execution.md）的示例却使用 `${{ atomgit.actor }}`——规格自相矛盾，实测行为未知（有值 / 求值为空 / 解析报错）。(b) GitHub 还有 github.job（当前 job_id）、github.run_attempt、github.triggering_actor、github.ref_protected、github.retention_days 等字段，GitCode atomgit 表无对应（run_attempt 在 variables.md 的 ATOMGIT_RUN_ATTEMPT 有环境变量，但上下文侧未列）。迁移 workflow 引用这些字段会静默求值为空。
预期系统行为: atomgit.actor 应有明确定义与值（消除规格矛盾）；对 GitHub 有而 GitCode 无的上下文字段，引用时应给出可观测的行为（求值为空需文档列出缺失字段对照表）；回写 Parity Matrix。
Oracle 来源: GitHub行为 | GitCode规格（自相矛盾，需实测仲裁）

验证要点:
  - [正向] `echo "${{ atomgit.actor }}"` 应有确定行为：返回触发者用户名（与文档示例一致），或明确定义为不支持
  - [负向] atomgit.actor 不应在不同页面文档中一处有一处无（规格矛盾本身即缺陷）
  - [正向] 逐一探测 atomgit.job / atomgit.run_attempt / atomgit.triggering_actor / atomgit.ref_protected 的求值行为
  - [非功能] 缺失字段清单应进入迁移对照文档

对齐方向:   一致性（actor 应存在且等价）+ 差异确认（缺位字段的降级）
优先级线索: RISK-COMPAT-01（P1：actor 是 GitHub 生态 top-5 高频字段）
破坏级别:   none
与旧 ID 关系: 新增；INTENT-COMPAT-016/017 覆盖「前缀全局替换」，本条覆盖「替换前缀之后字段仍不存在」的字段级差距
来源输入:   github-reference/reference/contexts.md（github.actor/actor_id/job/triggering_actor/ref_protected）; gitcode-spec/syntax-reference/context.md（atomgit 属性表无 actor）; gitcode-spec/running-pipelines/view-job-logs.md:42 与 writing-pipelines/configure-conditional-execution.md:110（示例使用 atomgit.actor——规格矛盾证据）
```

---

```
意图 ID:    INTENT-COMPAT-041
维度标签:   [compatibility]
标题:       needs 上下文存在性与字段完备性：context.md 未列出 vs 官方输出传递文档实际使用

风险点:     GitHub `needs` 上下文（`needs.<job>.outputs.<key>`、`needs.<job>.result`）是跨 job 数据传递与结果判断的标准机制，GitHub 生态 workflow 普遍使用 `if: needs.build.result == 'success'`。GitCode context.md 的 12 上下文总览表**不含 needs**，但 pass-output-between-jobs.md 明确使用 `needs.<job_id>.outputs.<key>`——规格内部矛盾。未明点：(a) needs 上下文在 `if` 中是否可用；(b) `needs.<job>.result` 字段是否存在（GitHub 有 success/failure/cancelled/skipped）；(c) 上游为 matrix job 时 needs 聚合语义（GitHub：全部实例完成才算完成，outputs 取最后完成实例的值——该语义本身就常被踩坑）；(d) 上游 job 被 skip 时 needs.<job>.result 取值。
预期系统行为: needs 上下文应存在并与 GitHub 字段集（outputs/result）对齐；matrix 上游聚合与 skipped 上游的 result 语义应与 GitHub 一致或文档声明差异；消除规格矛盾（context.md 补列 needs）。
Oracle 来源: GitHub行为 | GitCode规格（自相矛盾，需实测仲裁）

验证要点:
  - [正向] `needs.build.outputs.version` 跨 job 取值正确（GitCode 文档已承诺）
  - [正向] `needs.build.result` 在上游 success/failure/cancelled/skipped 四种结局下的取值与 GitHub 对齐
  - [正向] matrix 上游 job 的 needs.outputs 聚合行为可观测且确定（明确取哪个实例的值）
  - [负向] 不应出现 needs 在 if 中不可用而文档未声明的情况

对齐方向:   一致性
优先级线索: RISK-COMPAT-01（P1：跨 job 编排是 CI 主干机制）
破坏级别:   none
与旧 ID 关系: 新增；INTENT-COMPAT-NEW-006 覆盖「引用未声明 output 返回空」单一边界，本条覆盖 needs 上下文整体存在性与 result/聚合语义，为其父集
来源输入:   github-reference/reference/contexts.md（needs context）; gitcode-spec/syntax-reference/context.md（12 上下文无 needs）; gitcode-spec/writing-pipelines/pass-output-between-jobs.md（使用 needs.<job_id>.outputs）
```

---

```
意图 ID:    INTENT-COMPAT-042
维度标签:   [compatibility]
标题:       注解命令 `::error::`/`::warning::`/`::notice::`/`::debug::` 支持度与 debug 门控机制差异

风险点:     GitHub 的 `::error::`/`::warning::`/`::notice::` 会生成落在 PR/commit 文件行的注解（annotation），`::debug::` 仅在 secret `ACTIONS_STEP_DEBUG=true` 且 RUNNER_DEBUG=1 时输出。GitHub 生态几乎所有第三方 action（toolkit core.error/core.warning）都输出这些命令。GitCode workflow-commands.md 未列这四个命令；base 用例 TC-247~250（debug/error/warning/notice）全部 FAIL，TC-099（runner.debug 值不符）FAIL。疑似行为未知：静默忽略 / 原样输出到日志 / 部分解析。若原样输出，日志被 `::error file=...::` 噪声污染；若静默忽略，action 的失败标注能力丧失（`core.setFailed` 依赖 ::error + exit 1）。
预期系统行为: 不支持的注解命令至少应「不中断 workflow 且日志保留可见原文」（与 NEW-009 同策略）；更进一步确认是否有注解 UI 等价物；debug 门控应明确（GitCode 无 ACTIONS_STEP_DEBUG 对应机制时，`::debug::` 输出行为需定义）。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [正向] 输出 `::error::msg` / `::warning::msg` 不应导致 step/workflow 失败（setFailed 场景 exit code 仍由脚本控制）
  - [负向] 注解命令不应被解析执行出非预期副作用（如错误截断后续日志）
  - [正向] `::debug::` 在无任何门控配置时的默认可见性行为确定且文档化
  - [非功能] 与 GitHub 注解能力的差距应在差异清单中声明

对齐方向:   一致性（不中断降级）+ 差异确认（注解 UI 能力缺失）
优先级线索: RISK-COMPAT-01（P1：第三方 action 生态普遍依赖）
破坏级别:   none
与旧 ID 关系: 新增；INTENT-COMPAT-NEW-009 覆盖 add-mask/group/stop-commands，本条覆盖其余四个 message 类命令 + debug 门控，互补成完整 workflow-commands 面
来源输入:   github-reference/reference/workflow-commands.md（Setting messages 四命令 + ACTIONS_STEP_DEBUG 门控）; gitcode-spec/syntax-reference/workflow-commands.md（未列）; baseline/case-base-detail.md（TC-247~250、TC-099 FAIL）
```

---

```
意图 ID:    INTENT-COMPAT-043
维度标签:   [compatibility, security]
标题:       ATOMGIT_ENV 环境文件是否禁止覆写系统默认变量（GitHub 明确禁止覆写 GITHUB_*/RUNNER_*）

风险点:     GitHub 明确规定「You can't overwrite the value of the default environment variables named GITHUB_* and RUNNER_*」——通过 GITHUB_ENV 写入同名变量会被拒绝/忽略，防止 step 污染平台注入的关键变量（如 GITHUB_TOKEN 路径、GITHUB_WORKSPACE）。GitCode 文档对 ATOMGIT_ENV 无任何同名保护说明。若 `echo "ATOMGIT_WORKSPACE=/tmp/evil" >> $ATOMGIT_ENV` 生效，后续 step 的工作区、甚至 ATOMGIT_TOKEN 相关变量被污染，既是兼容差异（GitHub 上该写法无效）也是安全面（步骤间变量污染的信任边界）。真实场景中误用也常见（用户自定义变量恰好命名 ATOMGIT_XXX）。
预期系统行为: 与 GitHub 对齐：通过 ATOMGIT_ENV 写入 ATOMGIT_* 前缀的默认系统变量应被拒绝或忽略，并在日志中留下可观测提示；文档应声明保护名单。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [负向] 通过 ATOMGIT_ENV 覆写 ATOMGIT_WORKSPACE / ATOMGIT_SHA 后，后续 step 读到的不应是被污染值
  - [正向] 覆写尝试应在日志中产生警告或拒绝痕迹（而非静默成功）
  - [正向] 普通自定义变量（非 ATOMGIT_ 前缀）写入不受影响的正常工作

对齐方向:   一致性
优先级线索: RISK-COMPAT-01（P1；安全面与 RISK-SEC-02 注入面相邻，但不构成新 blocker——secret 隔离主线已由 032/033 覆盖）
破坏级别:   none
与旧 ID 关系: 新增；与 INTENT-COMPAT-017（ATOMGIT_* 变量清单差异）互补——017 是「有没有」，本条是「能不能被覆写」
来源输入:   github-reference/reference/workflow-commands.md（GITHUB_ENV 覆写禁止条款）; github-reference/reference/variables.md（同名禁止）; gitcode-spec/syntax-reference/workflow-commands.md（无保护说明）
```

---

```
意图 ID:    INTENT-COMPAT-044
维度标签:   [compatibility]
标题:       RUNNER_* 环境变量缺位：GitHub 注入 RUNNER_OS/ARCH/NAME/TEMP/TOOL_CACHE/ENVIRONMENT，GitCode 无对应

风险点:     GitHub Runner 注入 RUNNER_OS/RUNNER_ARCH/RUNNER_NAME/RUNNER_TEMP/RUNNER_TOOL_CACHE/RUNNER_DEBUG/RUNNER_ENVIRONMENT 系列环境变量，第三方 action 与构建脚本大量直接读取（如 `$RUNNER_OS` 做平台分支、`$RUNNER_TEMP` 放临时文件、`$RUNNER_TOOL_CACHE` 找缓存工具）。GitCode variables.md 的 ATOMGIT_* 清单中没有 RUNNER 系列对应变量（仅有 runner.* 上下文对象）。迁移的脚本/第三方 action 内 `echo $RUNNER_OS` 得空值，平台分支逻辑静默走错路径。base 用例 TC-441/442（ATOMGIT_RUNNER_OS/ARCH）FAIL，佐证该面已有实测问题。
预期系统行为: 确认 GitCode 是否注入 ATOMGIT_RUNNER_* 或兼容 RUNNER_* 变量；若不注入，差异须文档化并给出 runner 上下文替代写法对照表；TOOL_CACHE/ENVIRONMENT 等无 runner 上下文对应物的字段需单独声明缺失。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [正向] 逐一探测 RUNNER_OS/RUNNER_ARCH/RUNNER_TEMP/RUNNER_TOOL_CACHE/RUNNER_ENVIRONMENT 在 GitCode Runner 上的取值
  - [负向] 不应出现「文档未声明、实际部分注入」的不一致（如 RUNNER_TEMP 有值而 RUNNER_OS 为空）——半套兼容比完全不兼容更难排查
  - [非功能] 缺失变量清单进入迁移对照表；TC-441/442 修复后复验

对齐方向:   差异确认
优先级线索: RISK-COMPAT-01（P1：第三方 action 内部依赖，用户不可控；有 runner.* 上下文作 workaround 故不至 P0）
破坏级别:   none
与旧 ID 关系: 新增；与 INTENT-COMPAT-018/019（runner.os/arch 上下文值格式）互补——那两条是上下文对象，本条是环境变量面
来源输入:   github-reference/reference/variables.md（RUNNER_* 系列）; gitcode-spec/syntax-reference/variables.md（ATOMGIT_* 清单无 RUNNER 系列）; baseline/case-base-detail.md（TC-441/442 FAIL）
```

---

```
意图 ID:    INTENT-COMPAT-045
维度标签:   [compatibility, usability]
标题:       GitHub 风格第三方 action 引用（`uses: actions/checkout@v4`、`docker/build-push-action@v6`）的解析域

风险点:     GitHub 生态 workflow 几乎必含 `uses: actions/checkout@v4`、`actions/setup-node@v4`、`docker/build-push-action@v6` 等 GitHub 源引用。GitCode using-actions.md 定义三种引用方式（官方短名 / 开源插件 owner/repo/path@ref / 本仓路径），其中「开源插件」指向 **AtomGit 公开仓库**；但同页示例又出现 `uses: docker/build-push-action@v6`——若 GitCode 实际无法解析 GitHub 源 action，该示例构成文档误导，且迁移 workflow 的 uses 行将全线失败；若可解析（代理/镜像机制），则 ref 语义、可用版本集、供应链来源声明都需验证。这是迁移通过率的第一决定因素。
预期系统行为: 明确 GitCode 对 GitHub 风格 owner/repo@ref 引用的解析策略：可解析则应保证常见 action（actions/* 系列）的版本可用性与行为等价；不可解析则保存/解析阶段报错并提示官方短名替代（checkout/setup-node 等），官方文档示例不得出现实际不可用的引用写法。
Oracle 来源: GitCode规格（承诺三种引用方式）| 差异声明

验证要点:
  - [正向] `uses: actions/checkout@v4` 的解析结果明确：成功执行 或 保存期明确报错（二选一，不得排队期卡死）
  - [负向] 不可解析时不应表现为 job 无限 queued 或运行到该 step 才报模糊错误
  - [正向] `uses: docker/build-push-action@v6`（官方文档自带示例）必须可用，或文档勘误
  - [非功能] 报错/文档应给出 GitHub 引用 → GitCode 短名的映射指引

对齐方向:   差异确认
优先级线索: RISK-USE-01（P1：迁移核心路径）+ RISK-COMPAT-01
破坏级别:   none
与旧 ID 关系: 新增；INTENT-COMPAT-024 覆盖「短名 checkout 与 actions/checkout@v4 的行为等价性」（假定短名可用），本条覆盖「GitHub 风格全名引用本身能否被解析」的前置问题
来源输入:   gitcode-spec/writing-pipelines/using-actions.md（三种引用方式 + docker/build-push-action@v6 示例）; testing-focus.md §7/§11
```

---

```
意图 ID:    INTENT-COMPAT-046
维度标签:   [compatibility, usability]
标题:       自托管 runs-on 写法规格自相矛盾：对象式 {type,group,labels} vs 数组式 [self-hosted, linux, x64]

风险点:     GitCode 两份官方文档给出两种自托管 runs-on 写法：configure-jobs.md 用对象式（`runs-on: {type: self-hosted, group: ..., labels: [...]}`）；runner-images-tools.md 用数组式（`runs-on: [self-hosted, linux, x64, my-group, gpu]`，并给出「标签列表必须是 Runner 注册标签的子集」匹配规则）。GitHub 侧只有数组式。规格矛盾导致：用户无法确定哪种写法被真正接受；两种写法若都被接受，匹配语义（group 字段 vs 数组元素中的分组名位置约定）是否一致未明；数组式中「分组名」与「标签」无语法区分，与对象式的 group 字段如何对应是隐式约定。自托管是企业落地的必经路径，写法歧义直接阻塞接入。
预期系统行为: 两种写法中被实际接受的形式应唯一确定并统一文档；若兼容两种，匹配语义必须等价且文档声明；不接受的形式应在解析期报错而非排队。
Oracle 来源: GitCode规格（自相矛盾，需实测仲裁）| GitHub行为

验证要点:
  - [正向] 对象式写法在已注册自托管 Runner 的实例上调度成功（或明确报错）
  - [正向] 数组式写法同样得到确定响应
  - [负向] 不被接受的写法不应表现为 job 无限 queued 无提示
  - [非功能] 两种写法的匹配语义（子集规则、group 对应关系）文档统一

对齐方向:   一致性（对自身规格自洽）+ 差异确认（与 GitHub 数组式的关系）
优先级线索: RISK-USE-01（P1：自托管接入阻塞点）
破坏级别:   fixture（需自托管 Runner 夹具）
与旧 ID 关系: 新增；INTENT-COMPAT-NEW-008 覆盖「不支持的标签应报错而非无限排队」，本条覆盖「两种合法形态之间的规格矛盾」，互补
来源输入:   gitcode-spec/writing-pipelines/configure-jobs.md（对象式）; gitcode-spec/syntax-reference/runner-images-tools.md（数组式 + 子集匹配规则）
```

---

```
意图 ID:    INTENT-COMPAT-047
维度标签:   [compatibility]
标题:       预装工具链规格 vs 实测一致性，以及与 GitHub hosted image 的能力差距

风险点:     GitCode runner-images-tools.md 声称 ubuntu-24 镜像预装 Java 8/11/17/21、Maven、Gradle、Node 18/20/22、Go、kubectl、aws-cli 等完整清单；但 base 用例显示实测矛盾：TC-310（setup-java 插件不存在）与 NEW-011（Runner 未预装 Java、java -version 即失败）——规格承诺与实测直接冲突。此外 GitHub hosted runner 预装清单远更大（docker 守护进程、浏览器/驱动、Android SDK、多语言多版本并存），迁移 workflow 中 `docker build`、浏览器 E2E 测试等隐含依赖在 GitCode 上是否可用未明。工具链「文档说有、实际没有」比「文档说没有」危害更大（用户不会准备 fallback）。
预期系统行为: 预装清单逐条与实测对齐：实际存在的工具版本与文档一致；不存在的从文档移除或补齐；与 GitHub image 的关键差距（docker-in-docker、浏览器）显式声明。setup-* 系列插件与预装工具的关系（有预装还需不需要 setup）文档化。
Oracle 来源: GitCode规格（对自身承诺的一致性）| GitHub行为（能力差距对照）

验证要点:
  - [正向] 规格清单逐项实测：java/mvn/gradle/node/go/kubectl/aws-cli 的版本存在性与文档一致
  - [负向] 不应出现文档列出但实测缺失的工具（当前疑似 Java 即为此类）
  - [正向] docker、浏览器（chrome/firefox）等 GitHub 常见预装能力的可用性得到确定结论
  - [非功能] 与 GitHub image 的差距清单进入迁移文档

对齐方向:   一致性（对 GitCode 自身规格）
优先级线索: RISK-COMPAT-01（P1：构建环境是 CI 第一依赖）
破坏级别:   none
与旧 ID 关系: 新增；INTENT-COMPAT-NEW-011 是「Java 缺失单点 + 报错提示」，本条是「预装清单全面对账 + 与 GitHub image 系统差距」，为其父集
来源输入:   gitcode-spec/syntax-reference/runner-images-tools.md（预装清单）; baseline/case-base-detail.md（TC-310、TC-499 FAIL）; github-reference（hosted runner 能力基线）
```

---

```
意图 ID:    INTENT-COMPAT-048
维度标签:   [compatibility]
标题:       action 运行时 runs.using 类型覆盖：GitCode 仅见 node16 vs GitHub node20/docker/composite

风险点:     GitHub action 元数据支持 runs.using: node16/node20/docker/composite 四类运行时，其中 **composite action 是 GitHub 生态复用逻辑的绝对主力**（大量组织内部 action 与 marketplace action 都是 composite），docker action 在发布类流程常见。GitCode 文档示例与元数据说明中 runs.using 仅出现 node16（COMPAT-NOTES §10 已标记）。若 composite/docker 不支持，引用这类第三方 action 的迁移 workflow 会在加载 action 时失败；降级方式（明确报错 vs 模糊失败）与是否有替代机制（如把 composite 展开为 run 步骤）未明。
预期系统行为: 明确 GitCode 支持的 runs.using 取值全集；对不支持的类型（composite/docker/node20）在 action 加载阶段给出明确报错与替代指引；node16 运行时的 Node 实际版本与 GitHub node16 语义对齐。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [正向] runs.using: node16 的本地 action 正常执行
  - [正向] runs.using: composite / docker / node20 的 action 得到确定响应（支持执行 或 加载期明确报错）
  - [负向] 不支持的 using 类型不应表现为 step 运行期模糊失败（如 node: command not found）
  - [非功能] 支持的运行时清单进入差异文档

对齐方向:   差异确认
优先级线索: RISK-COMPAT-01（P1：composite 不支持则 GitHub 生态 action 大面积不可复用）
破坏级别:   fixture（需构造各类型本地 action 夹具）
与旧 ID 关系: 新增；INTENT-COMPAT-NEW-010 覆盖 action.yml 的展示性字段（branding）兼容性，本条覆盖 runs 运行时类型，互补成完整 action 元数据面
来源输入:   gitcode-spec/action-development/action-yml-metadata-syntax.md（using: node16）; gitcode-spec/COMPAT-NOTES.md §10; github-reference（GitHub action 运行时类型）
```

---

```
意图 ID:    INTENT-COMPAT-049
维度标签:   [compatibility, usability]
标题:       YAML 1.1 `on:` 键被解析为布尔 true 的经典陷阱在 GitCode 解析器中的处理

风险点:     YAML 1.1 规范中 `on`/`off`/`yes`/`no` 是布尔值，`on:` 作为顶层键会被标准 YAML 1.1 解析器读成 `true:`。GitHub 对此有显式处理（文档亦提醒）。GitCode 解析器的 YAML 版本与对该陷阱的处理未明：若按 YAML 1.1 严格解析，整个 workflow 的触发配置键名变为 `true`，可能整体不触发且无明显报错——这是 GitHub 社区最经典的 workflow「静默失效」坑之一，迁移用户会在 GitCode 上重新踩一遍。同理 `env` 中值为 yes/no/on/off 的字符串未加引号时的类型翻转。
预期系统行为: GitCode 应与 GitHub 一致，对顶层 `on:` 键做显式兼容处理；若解析器行为不同（如要求写 `"on":`），必须在快速入门显著位置声明。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [正向] 标准 `on: [push]` / `on: push:` 写法被正确识别为触发配置（非布尔键）
  - [负向] workflow 不应因 `on:` 键被解析为布尔而静默不触发且无任何告警
  - [正向] `env: {DEBUG: on}`（未加引号）的取值类型行为确定且与 GitHub 对齐

对齐方向:   一致性
优先级线索: RISK-USE-01（P1 线索；自评 P2：写法普遍但平台通常已处理，实测确认即可）
破坏级别:   none
与旧 ID 关系: 新增；无旧 ID 覆盖 YAML 解析器层的字面陷阱
来源输入:   github-reference/reference/workflow-syntax.md（on 键说明）; gitcode-spec/writing-pipelines/workflow-file-location-structure.md（on 为必填字段，未提解析陷阱）
```

---

```
意图 ID:    INTENT-COMPAT-050
维度标签:   [compatibility]
标题:       format() 花括号转义与字符串字面量引号规则的边界差异

风险点:     GitHub format() 支持双花括号转义（`format('{{Hello {0}}}', x)` 输出 `{Hello x}`），且字符串字面量规则严格：单引号包裹、字面单引号用 `''` 转义、双引号直接报错。GitCode expressions.md 对 format 仅描述「{0},{1}... 占位符依次替换」，未声明转义能力；字面量一节也未声明引号转义与双引号行为。迁移 workflow 中含字面花括号的 format 模板（如生成 JSON 片段 `format('{{"tag": "{0}"}}', ver)`——这在动态构造矩阵/配置时是真实用法）或带撇号的字符串（`it's`），求值结果可能与 GitHub 不一致或报错形态不同。
预期系统行为: format 的转义语义与 GitHub 对齐（支持 {{ }}），或文档声明不支持及替代写法；字符串字面量引号规则（'' 转义、双引号报错）与 GitHub 一致。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [正向] `format('{{{0}}}', 'x')` 的转义求值结果与 GitHub 对齐
  - [正向] 字符串中 `''` 转义为字面单引号的行为与 GitHub 一致
  - [负向] 双引号字符串不应被静默接受却求值异常（应与 GitHub 一样明确报错，或差异文档化）
  - [非功能] 转义能力差异进入表达式差异清单

对齐方向:   一致性
优先级线索: RISK-COMPAT-01（P1 线索；自评 P2：边界用法，概率中低）
破坏级别:   none
与旧 ID 关系: 新增；INTENT-COMPAT-009 覆盖运算符类型强转，本条覆盖函数/字面量语法层边界，互补
来源输入:   github-reference/reference/expressions.md（format 转义示例、字面量引号规则）; gitcode-spec/syntax-reference/expressions.md（format 简述，无转义说明）
```

---

```
意图 ID:    INTENT-COMPAT-051
维度标签:   [compatibility, reliability]
标题:       schedule 生命周期语义差异：GitHub 公开仓库 60 天无活动自动停用 vs GitCode 未声明

风险点:     GitHub 对公开仓库的定时 workflow 有「60 天无仓库活动自动停用」的平台行为（并有邮件通知）；GitCode 文档对 schedule 仅声明最短 5 分钟、UTC、仅默认分支，未声明任何自动停用/保活策略。差异双向：若 GitCode 有类似的未声明停用策略，低活动仓库的定时任务（如每周依赖巡检）会静默停摆；若 GitCode 无停用策略，则是与 GitHub 的有意差异（对迁移用户反而是行为改进），但仍需文档化以免用户按 GitHub 经验做「保活提交」等多余动作。另：schedule 在高负载下的触发延迟容忍（GitHub 文档提示可能延迟）GitCode 未声明，base 用例 TC-563（调度延迟）FAIL 佐证。
预期系统行为: GitCode 的 schedule 自动停用/保活策略与延迟容忍应明确文档化；若存在自动停用，停用前应有可观测通知且 UI 可见状态。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [正向] 确认 GitCode 是否存在 schedule 自动停用策略（文档/实测任一途径）
  - [负向] 不应存在「未文档化的静默停用」
  - [正向] schedule 触发延迟的可观测性（计划时间 vs 实际入队时间可见）
  - [非功能] TC-563 修复后复验调度延迟

对齐方向:   差异确认
优先级线索: RISK-COMPAT-01（P1 线索；自评 P2：长尾场景）+ RISK-REL-01（调度可靠性邻接）
破坏级别:   none
与旧 ID 关系: 新增；INTENT-COMPAT-013 覆盖 timezone 差异，本条覆盖 schedule 生命周期/延迟语义，互补
来源输入:   github-reference/reference/events.md（schedule: 60 天自动停用、延迟提示）; gitcode-spec/syntax-reference/trigger-events.md（schedule 三节无生命周期说明）; baseline/case-base-detail.md（TC-563 FAIL）
```

---

```
意图 ID:    INTENT-COMPAT-052
维度标签:   [compatibility]
标题:       触发器平台限额差异：push 批量上限（>5000 分支/>3 tags）与 workflow_dispatch 输入上限（25 个/65535 字符）

风险点:     GitHub 明确了两组平台限额：(a) 单次推送超过 5,000 个分支或超过 3 个 tag 时不生成事件（monorepo 批量同步、镜像仓库全量推 tag 场景会命中）；(b) workflow_dispatch 最多 25 个顶层 inputs、payload 最大 65,535 字符，且被触发的 workflow 文件必须在默认分支。GitCode 文档未声明对应限额。若 GitCode 限额更紧（如 dispatch inputs 上限更低），迁移的复杂参数化 workflow 会在保存或触发时被截断/拒绝；若无限额，批量推送下的事件风暴可能冲击调度（稳定性邻接）。「必须在默认分支才可 dispatch」这条若 GitCode 不同（可在任意分支 dispatch），反而是迁移便利差异，也需确认。
预期系统行为: GitCode 的对应限额（或明确无限额）应文档化；超限时的拒绝/截断行为应有明确报错而非静默丢弃事件。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [正向] 单次推送 4 个 tags：触发行为确定（全部触发 / 部分触发 / 不触发）且与文档一致
  - [正向] workflow_dispatch 配置 26 个 inputs：保存期明确报错或截断行为确定
  - [负向] 超限场景不应静默丢事件且无任何记录
  - [正向] 非默认分支上的 workflow_dispatch 可用性结论确定

对齐方向:   差异确认
优先级线索: RISK-COMPAT-01（P1 线索；自评 P2：批量/超限为长尾场景）
破坏级别:   none
与旧 ID 关系: 新增；INTENT-COMPAT-012 覆盖 paths 300 文件上限（同类「平台限额」子类），本条补齐其余限额项
来源输入:   github-reference/reference/events.md（push 批量上限、dispatch 25 inputs/65535 chars、默认分支要求）; gitcode-spec/syntax-reference/trigger-events.md（无限额声明）
```

---

```
意图 ID:    INTENT-COMPAT-053
维度标签:   [compatibility, security]
标题:       job 级 permissions 字段支持度：GitHub jobs.<id>.permissions 覆盖语法在 GitCode 的降级

风险点:     GitHub 支持 workflow 级与 job 级双层 permissions，job 级覆盖 workflow 级——最小权限实践（一个 workflow 里 build job 只读、release job 写）高度依赖 job 级覆盖，GitHub 安全加固文档将其列为推荐姿势。GitCode 文档仅在 workflow 顶层示例 permissions，configure-jobs.md 的 job 属性说明中未列 permissions 字段。迁移的加固版 workflow 含 `jobs.<id>.permissions:` 时降级方式未知：静默忽略（job 退回 workflow 级权限——可能过宽，安全语义降级）/ 解析报错 / 正确支持。静默忽略是最差形态：用户以为已按最小权限收窄，实际 TOKEN 权限比预期宽。
预期系统行为: job 级 permissions 若支持，覆盖语义与 GitHub 对齐（job 级替换 workflow 级，而非合并）；若不支持，解析期明确报错提示仅支持 workflow 级，不应静默忽略导致权限比声明更宽。
Oracle 来源: GitHub行为 | 差异声明

验证要点:
  - [负向] 含 job 级 permissions 的 workflow 不应被静默接受后该 job 实际获得 workflow 级（更宽）权限
  - [正向] 若支持：job 级 permissions 的实际 TOKEN 权限与声明一致（覆盖而非并集）
  - [正向] 若不支持：解析期报错指明「job 级 permissions 不支持，请提升到 workflow 级」
  - [非功能] 覆盖语义（替换 vs 合并）文档化

对齐方向:   一致性（权限不得宽于声明——安全底线）+ 差异确认（字段支持度）
优先级线索: RISK-SEC-01（权限越界面，P1；不构成新 blocker——默认权限与 fork 隔离主线已由 002/032 覆盖）+ RISK-COMPAT-01
破坏级别:   fixture（需不同权限声明的 job 组合夹具）
与旧 ID 关系: 新增；INTENT-COMPAT-030 覆盖 permissions「权限域命名」差异，本条覆盖「job 级字段存在性与覆盖语义」，正交互补；与 INTENT-COMPAT-002（默认权限）构成完整 permissions 三面
来源输入:   github-reference/reference/workflow-syntax.md（jobs.<job_id>.permissions）; github-reference/security/github-token.md（最小权限推荐）; gitcode-spec/writing-pipelines/configure-jobs.md（job 属性未列 permissions）; gitcode-spec/writing-pipelines/workflow-file-location-structure.md（仅顶层 permissions）
```

```
意图 ID:    INTENT-COMPAT-054
维度标签:   [compatibility, usability]
标题:       Runner OS 多样性：平台是否提供 Windows/macOS Runner，不支持 OS 的明确报错而非无限排队

风险点:     GitHub hosted runner 提供 ubuntu-latest / windows-latest / macos-latest 三大 OS 生态，
            大量迁移 workflow 含 Windows 构建（.NET/MSBuild）与 macOS 构建（iOS 签名）。
            GitCode selecting-runner-labels.md 三段式 {os,arch,flavor} 的 os 合法取值全集未公开，
            官方示例仅见 ubuntu 系；parity-matrix 对 Runner OS 多样性无对应能力行（盲区 B1）。
            迁移含 runs-on: windows-latest 的 workflow 时降级方式未知：明确报错（最好）/
            排队永不匹配（最差，用户无法区分「无此 OS」与「资源繁忙」）。
预期系统行为: GitCode 支持的 OS 取值全集应确定并文档化；指定不支持的 OS（如 windows-latest /
            macos-latest 或三段式中 os=windows）时，应在校验/调度期明确报错并列出受支持 OS，
            不应表现为 job 无限 queued 且无任何提示。
Oracle 来源: GitHub行为（hosted runner OS 矩阵）| 差异声明（GitCode OS 取值全集待实测）

验证要点:
  - [正向/记录] 逐一探测 os 取值（ubuntu 系各版本、windows、macos）的调度结果，逐字记录受支持全集
  - [负向] 指定不支持 OS 的 job 不应无限 queued 无提示（与 NEW-008 标签不匹配同策略）
  - [正向] 若仅支持 Linux，文档与迁移指引应显式声明「Windows/macOS 构建需自托管 Runner」
  - [非功能] OS 取值全集回写 parity-matrix（新增「Runner OS 多样性」能力行）与迁移对照表

对齐方向:   差异确认
优先级线索: RISK-USE-01（P1：迁移核心路径；有自托管 workaround 故不至 P0）
破坏级别:   none
与旧 ID 关系: 2026-07-27 STOP① 用户裁决增补（盲区 B1 闭环）；关联 INTENT-COMPAT-NEW-008（不支持标签报错）、INTENT-COMP-029（runs-on 形态裁定）
来源输入:   github-reference（hosted runner OS 矩阵）; gitcode-spec/runner-management/selecting-runner-labels.md; baseline/parity-matrix.md（缺行）
```

---

## 四、统计汇总

| 指标 | 数值 |
|---|---|
| **本轮新增 Intent 总数** | 19（INTENT-COMPAT-036 ~ 054；其中 054 为 2026-07-27 STOP① 用户裁决增补，覆盖门禁盲区 B1「Runner OS 多样性」） |
| **P0** | 0 |
| **P1** | 15（036~048、053、054；其中 049~052 为 P1 线索自评 P2 的除外项见下） |
| **P2（自评）** | 4（049、050、051、052——风险登记册无 P2 项，按「影响面长尾 + 有 workaround」自评降档，风险册线索仍为 RISK-COMPAT-01/RISK-USE-01，待门禁裁定） |
| **对齐方向 = 一致性** | 6（039、040、041、043、049、050；043/053 含差异确认成分） |
| **对齐方向 = 差异确认** | 8（036、037、038、044、045、048、051、052） |
| **对齐方向 = 混合（一致性+差异确认）** | 4（042、046、047、053） |
| **单维度 [compatibility]** | 9 |
| **跨 [compatibility, security]** | 2（043、053） |
| **跨 [compatibility, usability]** | 4（037、045、046、049） |
| **跨 [compatibility, reliability]** | 1（051） |
| **破坏级别 = fixture** | 3（039、046、048、053——共 4 条，039/046/048/053） |
| **破坏级别 = none** | 14 |

### P0 为空的原因说明
按 rules.md §2，P0 必须逐条对应风险登记册 blocker 项（RISK-SEC-01/02）。本轮新增差异点中，secret 隔离/注入的主攻击面已由上轮 032、033 及 NEW-002 覆盖；043/053 与 SEC-01/02 相邻但不构成新的独立 blocker 面，故保守标 P1。若门禁认为 053（权限静默宽于声明）应升级，请回指。

### 与上一轮关系总览
- **新增 19 条**（036~054，054 为 STOP① 增补）；**沿用 0 条**（上轮 47 条全部保持有效，本轮不重复产出）；**合并 0 条**（与旧 ID 的邻近关系均以「父集/互补/正交」注明，未做合并改写）。

---

## 五、溯源链闭合检查（本轮增量部分）

| 风险项 / Parity 能力项 | 覆盖 Intent（本轮新增） | 状态 |
|---|---|---|
| RISK-COMPAT-01（默认值/静默差异） | 036、038、039、040、041、042、043、044、047、048、050、051、052 | ✅ |
| RISK-USE-01（迁移报错质量） | 037、045、046、049 | ✅ |
| RISK-SEC-01（权限越界邻接） | 043、053 | ✅（P1 邻接覆盖） |
| Parity：表达式函数 `contains`/`hashFiles`/`toJson`（❓） | 036、050（补充 startsWith/endsWith/format 边界） | ✅ 增量 |
| Parity：未知/不支持字段处理（❓） | 037、045、048、053 | ✅ 增量 |
| Parity：Runner 环境/标签（🟡/❓） | 044、046、047 | ✅ 增量 |
| Parity：迁移报错质量（❓） | 037、045、049 | ✅ 增量 |
| GitHub events.md 全量事件表 | 037、038、039、051、052 | ✅ 新增覆盖 |
| GitHub workflow-commands.md 注解命令节 | 042 | ✅ 新增覆盖 |
| GitHub variables.md RUNNER_* 节 | 044 | ✅ 新增覆盖 |
| GitCode 规格内部矛盾（actor / runs-on 双形态 / needs 缺列 / 预装清单） | 040、046、041、047 | ✅ 本轮特有发现 |

---

*产出完毕。待门禁评审。*
