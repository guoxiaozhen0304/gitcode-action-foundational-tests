# Spec-Analyst 产出（Run 2026-07-27-01）：增量能力清单 + 新增规格缺口 + Intent 库（delta）

> 角色：phase01 spec-analyst（维度 = spec / 规范完备性）
> 输入版本：gitcode-spec/ 54 个文件（fetched 2026-07-20，本轮无内容刷新）；workflow-samples/ 12 文件（2026-07-22 新增 testorg/ 3 样本）；platform-config/ 2026-07-21；testing-focus.md 当前版本
> 分析日期：2026-07-27
> 与上轮关系：本轮为**增量（delta）模式**。上轮 2026-07-23-01 的 30 条 intent（INTENT-COMP-001~018 及跨维度 019~030）与 20 条 GAP 全部沿用，不重复产出；本轮仅产新增项。ID 续用 spec agent 自有号段，自 INTENT-COMP-019 起，不与上轮及回填的 INTENT-COMPAT-NEW-001~012 / INTENT-REL-067/068 冲突。

---

## 0. 本轮输入变化感知（rules.md §12）

| 输入 | 变化 | 对本轮发散的影响 |
|---|---|---|
| `inputs/gitcode-spec/` | 54 文件，文件头 fetched 时间均为 2026-07-20，**无内容刷新** | 上轮 GAP-001~020 全部仍然成立（本轮逐条抽验：默认 shell、Runner ephemeral、cache fork 隔离、artifact 大小上限、matrix 上限文档依旧未明） |
| `inputs/workflow-samples/` | 新增 `testorg/`（full_pr.yaml / build_job.yaml / ut_job.yaml，MindIE-SD 项目），补齐上轮标注的「缺 `pull_request`、`workflow_call` 入口样本」 | 新样本暴露多个**规范未文档化**字段/语法（`select`、`default()`、`manual_override`、`code-update`、`pr_comment` 别名、四段式 runs-on、`${gitcode_*}` 插值、pre-merge ref），是本轮 intent 的主要来源 |
| `inputs/business-context/` | 仍仅 README.md，无迁移摩擦实录 | 易用性向 intent 仍只能依据文档与样本推断 |

---

## 1. 增量结构化能力清单（仅列本轮新发现/需修正项；全量清单见 runs/2026-07-23-01/intents/spec.md §1）

| 能力项 | 语义 | 约束与边界 | 默认值 | 出处 | 置信度 |
|---|---|---|---|---|---|
| `stages` 语法形式 | 阶段定义 | **同一文档给出两种形式**：map 形式（`stages: build_stage: jobs:`，workflow-file-location-structure.md L88）与 list 形式（`stages: - name: build-stage jobs:`，同文件 L115、manually-trigger-pipeline.md、configuring-images-toolchains.md）；真实样本均用 map 形式 | 未知（是否两种都接受） | workflow-file-location-structure.md; manually-trigger-pipeline.md | **未知（文档自相矛盾）** |
| `select` 字段（stage/job 级） | 选择性执行（`selected_by_default`） | 真实样本（testorg/full_pr.yaml）与 actions-market.md 示例使用；**规范文档零定义** | 未知 | actions-market.md L1317/1560/2496（仅示例）; workflow-samples/testorg | **未知（规格缺口）** |
| `default()` 表达式函数 | 疑似默认值回退函数 | actions-market.md 示例与 testorg 样本用于 `if: ${{ default() }}`；expressions.md **未列出** | 未知 | actions-market.md L1323/2511（仅示例） | **未知（规格缺口）** |
| `inputs` 上下文可用范围 | 触发输入参数访问 | **三方矛盾**：manually-trigger-pipeline.md L89 称「仅 workflow_dispatch 可用，其他事件引用会报错」；runtime-environment-variables.md L74 称「引用不存在属性计算为空字符串」；context.md L21/L291 称 inputs 在 workflow_dispatch/workflow_call 及多位置可用。真实样本在 `pull_request` 触发下使用 `${{ inputs.pr_id }}` | 矛盾 | manually-trigger-pipeline.md; runtime-environment-variables.md; context.md | **未知（规格自相矛盾）** |
| workflow 顶层 `inputs` + `manual_override` | 触发器之外的顶层输入声明 | testorg/full_pr.yaml 使用顶层 `inputs:`（12 个，含 `manual_override: true/false`）；规范仅定义 `on.workflow_dispatch.inputs` / `on.workflow_call.inputs`，顶层形式与 `manual_override` **未文档化** | 未知 | workflow-samples/testorg/full_pr.yaml（无规范出处） | **未知（规格缺口）** |
| 触发事件别名 `pr_comment` | PR 评论触发 | cann/sub_pipline_support.yaml 使用 `pr_comment`；规范仅定义 `pull_request_comment` | 未知 | workflow-samples/cann; core-concepts/trigger-events.md | **未知** |
| `runs-on` 标签形式 | Runner 选择 | **三种并存**：文档三段式 `{os,arch,flavor}`（selecting-runner-labels.md）；四段式 `[codearts-hosted, ubuntu-latest, x64, large]`（actions-market.md 示例、testorg 样本）；flow-mapping 写法 `runs-on: {ubuntu-24,x64,small}`（manually-trigger-pipeline.md、configuring-images-toolchains.md，YAML 语义上为 mapping 非数组） | 三段式 | selecting-runner-labels.md vs actions-market.md | **模糊（文档不一致）** |
| `container.volumes` / `container.options` | 容器挂载与 docker 参数 | configuring-images-toolchains.md 声明支持 `volumes`（**Host → Container 挂载**）与任意 `options`（如 `--memory 12g`、`--hostname`）；托管 Runner 上的隔离边界未声明 | 无 | configuring-images-toolchains.md | 明确（能力存在）/ **未知（隔离边界）** |
| action.yml `inputs.required` 强制力 | 必填输入校验 | top-level-fields.md 明确声明：「未指定输入时 required: true **不会自动返回错误**，需在代码中主动校验」 | 不强制 | action-development/top-level-fields.md L53 | 明确 |
| `INPUT_<VARIABLE_NAME>` 环境变量契约 | action 输入注入方式 | 输入名转大写、空格转 `_`；**连字符 `-` 的转换规则未声明**（GitHub 将 `-`→`_`） | 见左 | action-development/top-level-fields.md L41-43 | 模糊（边界未明） |
| action 级 `runs.post` 触发机制 | 插件清理钩子 | top-level-fields.md 声明两种触发：主动停止（用户取消，**调度服务调用 post**）/ 自然调用（需插件自行监听 SIGINT）；部分回答了上轮 GAP-008（取消语义） | 无 | action-development/top-level-fields.md L122-144 | 明确（声明）/ 待实测 |
| `workflow_call` 本地路径调用 | `uses: ./.gitcode/workflows/x.yml` | syntax-reference/trigger-events.md L228 声明本地路径调用 + `secrets:` 映射；被调方可声明 `secrets.required`；**调用方未传 required secret 的行为未声明**；路径解析基准（哪个分支/commit）未声明 | 未知 | syntax-reference/trigger-events.md | 模糊 |
| pre-merge ref | `refs/merge-requests/N/merge` | checkout 该 ref 获得合并预览代码；仅 actions-market.md 与 testorg 样本出现，**checkout 插件文档未定义**该 ref 的存在性与语义 | 无 | actions-market.md; workflow-samples/testorg | **未知（规格缺口）** |
| 非 `${{ }}` 插值风格 | `${gitcode_*}` / `${PIPELINE_*}` | testorg 样本 inputs default 使用；规范全文未提及该插值语法（疑似 CodeArts 遗留） | 未知 | workflow-samples/testorg/full_pr.yaml | **未知** |
| `pull_request.code-update` 字段 | 疑似代码更新过滤 | testorg 样本 `on.pull_request` 下出现 `code-update: false`；规范未定义 | 未知 | workflow-samples/testorg | **未知** |

---

## 2. 新增规格缺口/存疑清单（续上轮 GAP-001~020）

| 序号 | 缺口/存疑项 | 影响维度 | 置信度 | 下游消费方 | 说明 |
|---|---|---|---|---|---|
| GAP-021 | `stages` 双语法形式（map vs list）裁定 | completeness, usability | 未知 | case-writer, usability | 同一文档两种示例，平台接受哪种未明。 |
| GAP-022 | `inputs` 上下文可用范围三方矛盾 | completeness, compatibility | 未知 | compat-diff, case-writer | 报错 vs 空字符串 vs 多位置可用，三份文档互斥；真实样本依赖「非 dispatch 可用」。 |
| GAP-023 | `select` / `default()` / `manual_override` / `code-update` 未文档化字段群 | completeness, compatibility | 未知 | compat-diff, usability | 真实样本在用但规范零定义；若被静默忽略则衔接 GAP-007（未知字段降级方式）。 |
| GAP-024 | 「Fork 场景推荐使用 pull_request_target」与安全文档冲突 | security, usability | 明确（矛盾存在） | security, usability | core-concepts/trigger-events.md 的推荐与 pr-mr-pipeline-security.md 的警示直接冲突，误导风险高。 |
| GAP-025 | `container.volumes` 宿主挂载与 `options` 的隔离边界 | security, reliability | 未知 | security, reliability | 托管 Runner 是否真允许宿主路径挂载、特权 docker 参数是否被过滤，文档未声明。 |
| GAP-026 | 四段式 runs-on（`codearts-hosted` 首段）语义 | completeness, compatibility | 模糊 | case-writer, compat-diff | 首段疑似资源池标识，规范未定义；与三段式文档冲突。 |
| GAP-027 | `workflow_call` secrets required 未传的行为 + 本地路径解析基准 | completeness, security | 未知 | security, case-writer | required secret 缺失时报错还是空值；`uses: ./` 取调用方还是被调方 ref。 |
| GAP-028 | pre-merge ref `refs/merge-requests/N/merge` 语义与 `${gitcode_*}`/`${PIPELINE_*}` 插值 | completeness | 未知 | case-writer, compat-diff | PR 流水线核心模式无规范出处；插值风格疑似平台遗留。 |

---

## 3. Intent 列表（本轮 delta，共 15 条）

> 优先级线索均取自 baseline/risk-register.md 现有风险项；无法精确对齐处已诚实标注。
> spec 维度不直接产 P0（risk-register 的两个 P0 均为安全项，由 security 维度承接）；本维度 P1 集中于 RISK-COMPAT-01（默认/隐式行为差异）。

### INTENT-COMP-019
```
意图 ID:    INTENT-COMP-019
维度标签:   [completeness, usability]
标题:       裁定 stages 阶段定义的两种文档语法形式（map vs list）

风险点:     workflow-file-location-structure.md 同一文件给出 map 形式与 list 形式两种 stages 示例，
            manually-trigger-pipeline.md / configuring-images-toolchains.md 用 list 形式，
            真实样本（cann、op-plugin、testorg）全用 map 形式。若平台只接受其一，
            按另一形式编写的 workflow 会解析失败或被静默忽略（衔接 GAP-007）。
预期系统行为: 平台对 stages 的接受形式应有唯一确定语义：两种形式均被解析为等价的阶段结构，
            或拒绝其中一种并给出明确报错；不应出现「一种形式被静默忽略导致阶段串行语义丢失」。
Oracle 来源: GitCode规格（文档自相矛盾，需实测裁定哪份为真）

验证要点:
  - [正向] map 形式 stages 按定义顺序串行执行（样本路径，回归保护）
  - [正向/记录] list 形式 stages 的实际处理结果（接受并等价 / 报错 / 静默忽略），逐字记录
  - [负向] 不应出现 stages 被接受但阶段串行语义丢失（job 全部并行）而无任何告警

优先级线索: RISK-COMPAT-01（文档矛盾 → 隐式行为差异，发生概率高）→ 建议 P1
破坏级别:   none
来源输入:   workflow-file-location-structure.md L88/L115; manually-trigger-pipeline.md; configuring-images-toolchains.md; workflow-samples/testorg（2026-07-22）
```

### INTENT-COMP-020
```
意图 ID:    INTENT-COMP-020
维度标签:   [completeness, compatibility]
标题:       裁定 inputs 上下文在非 workflow_dispatch 触发下的可用性（三方文档矛盾）

风险点:     manually-trigger-pipeline.md 称「inputs 仅 workflow_dispatch 可用，其他事件引用会报错」；
            runtime-environment-variables.md 称「引用不存在的属性计算为空字符串」；
            context.md 称 inputs 在 workflow_dispatch/workflow_call 及多个位置可用。
            三份文档互斥，而 testorg 真实样本在 pull_request 触发下使用 ${{ inputs.pr_id }}——
            若按 manually-trigger-pipeline.md 应为报错，样本却在线上运行。迁移者无法预期行为。
预期系统行为: 平台对非 dispatch/call 触发下引用 inputs 的行为应唯一确定（报错 / 空字符串 / 取顶层 inputs 默认值），
            且与最终裁定的文档一致；若支持顶层 inputs 默认值注入（样本行为），则 manually-trigger-pipeline.md 的「会报错」声明应被证伪。
Oracle 来源: GitCode规格（矛盾，实测裁定）；对齐方向：差异确认（裁定后回写 Parity Matrix）

验证要点:
  - [正向] pull_request 触发 + 顶层 inputs 默认值场景下 ${{ inputs.x }} 的实际求值结果（逐字记录）
  - [正向] workflow_dispatch 触发下 inputs 正常求值（回归保护）
  - [负向] 同一引用不应在不同运行间给出不一致结果（求值确定性）
  - [非功能] 若报错，报错是否指明「inputs 不可用」而非泛化表达式错误

对齐方向:   差异确认
优先级线索: RISK-COMPAT-01（三方矛盾 + 真实样本依赖，概率高）→ 建议 P1
破坏级别:   none
来源输入:   manually-trigger-pipeline.md L89; runtime-environment-variables.md L74; syntax-reference/context.md L21/L265/L291; workflow-samples/testorg/full_pr.yaml（2026-07-22）
```

### INTENT-COMP-021
```
意图 ID:    INTENT-COMP-021
维度标签:   [completeness]
标题:       验证未文档化字段 select / selected_by_default 的真实语义与默认值

风险点:     testorg 样本在 stage 与 job 两级使用 select: selected_by_default，
            actions-market.md 示例同样使用，但规范文档零定义。
            该字段疑似控制「阶段/job 是否默认选中执行」，未声明时的默认行为未知——
            若默认不执行，按文档编写（无 select）的 workflow 与样本行为将出现静默分歧。
预期系统行为: 若平台支持 select，其语义（可选值、缺省默认、与 if 的交互）应被确定并文档化；
            未声明 select 的 stage/job 应默认执行（与全部官方示例一致）。
Oracle 来源: GitCode规格（缺口项，实测记录事实并回写规格缺口清单）

验证要点:
  - [正向] 未声明 select 的 stage/job 默认被执行
  - [正向/记录] 声明 select: selected_by_default 时的实际行为（与未声明是否等价）
  - [非功能] select 与 if 条件并存时的求值顺序（先 select 后 if / 反之 / 报错）

优先级线索: RISK-COMPAT-01（未文档化字段 + 默认行为未知）→ 建议 P1
破坏级别:   none
来源输入:   workflow-samples/testorg/full_pr.yaml（2026-07-22）; actions-market.md L1317/1560/2496; 规范全文检索确认无定义
```

### INTENT-COMP-022
```
意图 ID:    INTENT-COMP-022
维度标签:   [completeness]
标题:       验证未文档化表达式函数 default() 的存在性与语义

风险点:     actions-market.md 示例与 testorg 样本使用 if: ${{ default() }}，
            但 expressions.md 的函数清单未列出 default()。
            若函数不存在而表达式被静默求值为 falsy/truthy，job 执行与否将出现不可预期分歧。
预期系统行为: default() 若为平台函数，其返回语义（何场景 true/false）应确定；
            若不存在，引用处应报错而非静默求值。
Oracle 来源: GitCode规格（缺口项，实测记录事实）
与上轮关系:  新增；与 INTENT-COMPAT-021（同名函数对齐 GitHub 边界）互补——本条针对 GitCode 特有且未文档化的函数

验证要点:
  - [正向/记录] if: ${{ default() }} 在 job 与 stage 级的实际求值结果（逐字记录触发/跳过）
  - [负向] 未文档化函数不应被静默求值为常量而导致条件恒真/恒假且无提示
  - [非功能] default() 与手动触发表单（workflow_dispatch 选择执行项）是否存在联动（推测语义，需证伪/证实）

优先级线索: RISK-COMPAT-01 → 建议 P2（影响面限于使用 select/default 模式的流水线）
破坏级别:   none
来源输入:   actions-market.md L1323/2511/2564/2664/2790; workflow-samples/testorg/full_pr.yaml; syntax-reference/expressions.md（确认未列出）
```

### INTENT-COMP-023
```
意图 ID:    INTENT-COMP-023
维度标签:   [completeness, security]
标题:       裁定「Fork 场景推荐使用 pull_request_target」与安全警示的文档冲突

风险点:     core-concepts/trigger-events.md 明确写「Fork 场景推荐使用 pull_request_target」，
            而 pr-mr-pipeline-security.md 将 pull_request_target + checkout head.sha 列为高危模式。
            两份官方文档导向相反：按前者行事的用户会把 fork PR 放进高权限上下文，是直接的安全诱导。
预期系统行为: 文档层：两处表述应收敛为一致的安全导向（fork 场景默认 pull_request，
            pull_request_target 仅限确需 secrets/写权限且配合安全措施的场景）。
            平台层（与上轮 INTENT-COMP-004/014 联动）：pull_request_target 的防护
            （base 分支 workflow 版本、fork 不可改执行逻辑）必须在实测中成立，为文档收敛提供事实底座。
Oracle 来源: GitCode规格（文档间矛盾，以安全文档为权威方向）

验证要点:
  - [负向] 不应存在「按 trigger-events.md 推荐配置 fork PR 即获得 secrets 写权限且无平台警告」的默认路径
  - [正向] 平台对 pull_request_target 的 base 版本约束实测成立（复用 INTENT-COMP-014 证据链）
  - [非功能] 矛盾文档清单回写 Parity Matrix「差异/备注」，作为文档修复项跟踪

负向断言目标: fork PR 场景按「推荐」配置不应在无任何警示的情况下获得仓库 secrets 与写权限
优先级线索: RISK-SEC-01（文档误导直接抬升 fork PR 攻击面概率）→ 建议 P1
破坏级别:   fixture
来源输入:   core-concepts/trigger-events.md（"重要区别"段）; security-permissions/pr-mr-pipeline-security.md; 2026-07-20
```

### INTENT-COMP-024
```
意图 ID:    INTENT-COMP-024
维度标签:   [completeness, compatibility]
标题:       验证触发事件别名 pr_comment 的有效性与等价性

风险点:     cann/sub_pipline_support.yaml 使用 on: pr_comment，规范仅定义 pull_request_comment。
            别名是否真实有效、两者是否完全等价（含 comments 正则过滤）、
            无效事件名是否被静默忽略（workflow 不触发且无提示），均未明。
预期系统行为: pr_comment 若为合法别名，其行为应与 pull_request_comment 逐点等价；
            若为非法字段，应在 workflow 校验期报错，而非静默不触发。
Oracle 来源: GitCode规格（缺口项）；对齐方向：差异确认（与 GAP-007 未知字段降级方式联动）

验证要点:
  - [正向/记录] on: pr_comment 的实际处理（触发成功 / 校验报错 / 静默忽略），逐字记录
  - [正向] pull_request_comment 的 comments 正则过滤行为（回归保护）
  - [负向] 非法事件名不应静默导致 workflow 永不触发且无任何可见提示

对齐方向:   差异确认
优先级线索: RISK-COMPAT-01 → 建议 P2
破坏级别:   fixture（需布置评论触发夹具）
来源输入:   workflow-samples/cann/sub_pipline_support.yaml; core-concepts/trigger-events.md; syntax-reference/trigger-events.md
```

### INTENT-COMP-025
```
意图 ID:    INTENT-COMP-025
维度标签:   [completeness, security]
标题:       验证 container.volumes 宿主机挂载与 container.options 在托管 Runner 上的真实边界

风险点:     configuring-images-toolchains.md 声明 container 支持 volumes（Host → Container 挂载）
            与任意 docker options（--memory、--hostname 等）。
            在官方托管 Runner 上允许挂载宿主路径、传入任意 docker 参数，直接触及执行环境隔离边界
            （文档未声明任何限制/过滤）；同时与「Runner 是否一次性」（GAP-003）叠加放大残留污染风险。
预期系统行为: 规格声明的能力边界应被确定：托管 Runner 上 volumes 可挂载的路径范围、
            options 中被禁止/过滤的特权参数（如 --privileged、--network=host、挂载 / 根目录）
            应有确定性行为（拒绝 / 报错 / 允许），且结果回写规格缺口清单。
Oracle 来源: GitCode规格（能力存在性明确，边界未知——实测记录事实）

验证要点:
  - [正向] 常规 volumes 挂载（如构建缓存目录）按声明工作
  - [负向] 托管 Runner 上不应能无限制挂载宿主敏感路径或传入提权类 docker options（记录实际拒绝/放行行为）
  - [非功能] credentials/env/options 组合下的行为一致性

负向断言目标: 在官方托管 Runner 上，job 不应能通过 container 配置获得超出文档声明的宿主机访问面；
            若平台选择放行，必须以事实记录形式回写风险登记册
优先级线索: RISK-SEC-01（隔离边界）→ 建议 P1；安全利用面深测由 security 维度承接
破坏级别:   fixture
来源输入:   runner-management/configuring-images-toolchains.md; core-concepts/runner-and-environment.md; 2026-07-20
```

### INTENT-COMP-026
```
意图 ID:    INTENT-COMP-026
维度标签:   [completeness, compatibility]
标题:       验证 action.yml inputs.required: true 不自动校验的声明行为

风险点:     top-level-fields.md 明确声明「未指定输入时 required: true 不会自动返回错误，需在代码中主动校验」。
            用户直觉（与 GitHub 一致也是不强制，但大量 action 依赖平台报错心智）相反；
            若平台实际会校验，文档为假；若不校验，缺失必填输入的 action 收到空值后的失败模式不可预期。
预期系统行为: 与文档声明一致：平台不因 required: true 缺参而失败；
            action 侧收到的对应环境变量为空值；失败与否由 action 自身校验决定。
Oracle 来源: GitCode规格（明确声明，验证为真）；对齐方向：差异确认（声明与直觉相反，需固化事实）

验证要点:
  - [正向] 调用声明 required: true 的本地 action 且未传该参数时，workflow 不在调度层失败
  - [正向] action 内读取到该输入对应的环境变量为空值
  - [非功能] 若平台后续加入校验，文档与行为需同步（回写差异声明）

对齐方向:   差异确认
优先级线索: RISK-COMPAT-01 → 建议 P2
破坏级别:   fixture（需布置自定义本地 action 夹具）
来源输入:   action-development/top-level-fields.md L53; 2026-07-20
```

### INTENT-COMP-027
```
意图 ID:    INTENT-COMP-027
维度标签:   [completeness]
标题:       验证 INPUT_<VARIABLE_NAME> 环境变量命名契约的边界（连字符转换规则未声明）

风险点:     top-level-fields.md 声明输入名「转大写、空格替换为 _」生成 INPUT_<NAME> 环境变量，
            但对 inputs.<input_id> 合法字符集中允许的连字符 `-` 如何转换只字未提
            （GitHub 惯例为 `-`→`_`）。action 开发者按文档拼环境变量名将取不到值。
预期系统行为: 命名转换规则应对全部合法字符确定：大写化、空格→_、连字符的转换行为被实测确定；
            文档未声明部分以事实回写。
Oracle 来源: GitCode规格（边界未明，实测记录事实）

验证要点:
  - [正向] 含连字符的 input_id（如 dry-run）注入的环境变量名被确定（INPUT_DRY-RUN / INPUT_DRY_RUN / 其他）
  - [正向] 大写化与空格转换与文档一致
  - [非功能] 同一 input_id 经 `with` 传参与环境变量两条路径取值一致

优先级线索: RISK-COMPAT-01 → 建议 P2
破坏级别:   fixture（需布置自定义本地 action 夹具）
来源输入:   action-development/top-level-fields.md L41-57; 2026-07-20
```

### INTENT-COMP-028
```
意图 ID:    INTENT-COMP-028
维度标签:   [completeness, reliability]
标题:       验证 action 级 runs.post 的两种触发机制（取消时调度服务调用 / 自然调用靠插件自监听）

风险点:     top-level-fields.md 声明：用户取消流水线时由调度服务主动调用 action 的 post；
            正常结束时需插件自行监听 SIGINT 调用 post。这是上轮 GAP-008（取消语义）的
            部分文档化回答，但「调度服务调用 post」的时限、失败处理、
            以及插件未监听信号时清理逻辑被跳过的后果均未明。
预期系统行为: 手动取消运行中的 workflow 时，声明了 runs.post 的 action 的 post 入口被调用
            （清理副作用发生）；正常完成时 post 行为符合「插件自监听」的责任划分；
            post 执行失败/超时对 workflow 终态的影响确定。
Oracle 来源: GitCode规格（明确声明，验证为真 + 记录边界事实）

验证要点:
  - [正向] 取消运行后，action 的 post 逻辑被执行（以其清理副作用为证据）
  - [正向] 正常完成后 post 的行为符合文档责任划分
  - [非功能] 取消到 post 被调用的时延有上界（记录实测值）；post 失败不改变 workflow 已取消的终态
  - [负向] 取消后不应出现 post 未执行且无痕迹可查（日志应留有 post 调用记录）

故障/压力参数: 注入时机: job 运行中（step 执行至 50% 进度）手动取消；恢复预期: post 完成清理后运行进入 cancelled 终态，无残留副作用
优先级线索: RISK-REL-01（取消/恢复语义，部分对齐；GAP-008 衍生）→ 建议 P1
破坏级别:   fixture
来源输入:   action-development/top-level-fields.md L111-144; 2026-07-20；关联上轮 GAP-008
```

### INTENT-COMP-029
```
意图 ID:    INTENT-COMP-029
维度标签:   [completeness, compatibility]
标题:       裁定 runs-on 标签的三种并存形式（三段式 / 四段式 codearts-hosted / flow-mapping 写法）

风险点:     selecting-runner-labels.md 定义三段式 {os,arch,flavor}；
            actions-market.md 示例与 testorg 样本使用四段式 [codearts-hosted, ubuntu-latest, x64, large]
            （首段疑似资源池标识，规范未定义）；
            manually-trigger-pipeline.md 与 configuring-images-toolchains.md 使用
            runs-on: {ubuntu-24,x64,small}——YAML 语义为 mapping 而非数组。
            三种形式何者合法、四段式首段语义、mapping 写法是否被特判，全部未明；
            而真实生产流水线（MindIE-SD）直接依赖四段式。
预期系统行为: 平台对 runs-on 的合法形式应有确定语法：三段式与四段式的匹配语义明确、
            首段资源池标识的合法取值集合明确、mapping 写法要么被解析为等价数组要么校验报错；
            不应出现「语法被接受但调度到非预期 Runner」。
Oracle 来源: GitCode规格（文档不一致，实测裁定）

验证要点:
  - [正向] 三段式调度行为（回归保护，复用上轮 INTENT-COMP-010 证据）
  - [正向/记录] 四段式（含 codearts-hosted 首段）的调度结果与首段语义（逐字记录实际 Runner）
  - [正向/记录] flow-mapping 写法的处理结果（等价解析 / 报错 / 排队不匹配）
  - [负向] 任一形式被接受后不应调度到与标签声明不符的 Runner 且无提示

对齐方向:   差异确认
优先级线索: RISK-COMPAT-01（真实样本强依赖 + 文档不一致）→ 建议 P1
破坏级别:   none
来源输入:   runner-management/selecting-runner-labels.md; actions-market.md L215 等; manually-trigger-pipeline.md L42; configuring-images-toolchains.md; workflow-samples/testorg（2026-07-22）
```

### INTENT-COMP-030
```
意图 ID:    INTENT-COMP-030
维度标签:   [completeness, security]
标题:       验证 workflow_call 本地路径调用与 secrets required 契约（调用方缺参行为）

风险点:     syntax-reference/trigger-events.md 声明 uses: ./.gitcode/workflows/x.yml 本地路径调用
            与被调方 secrets.required 声明，但未声明：调用方未传 required secret 时的行为
            （校验报错 / 运行期空值 / 静默通过——三种失败模式安全后果截然不同）；
            本地路径的解析基准（调用方当前 ref？被调用 workflow 所在 commit？fork PR 场景取哪侧）
            也未明。testorg 全部构建 job 依赖此模式传递 OBS_AK/OBS_SK。
预期系统行为: 调用方未传 required secret 时，应在校验/调度期明确失败并指明缺失项，
            不应以空值进入被调 workflow 执行；本地路径解析基准确定且与文档/样本行为一致；
            fork PR 场景下路径解析不产生跨信任边界的意外代码加载。
Oracle 来源: GitCode规格（契约边界未明，实测记录事实）

验证要点:
  - [正向] 完整传参（含 secrets 映射）的本地路径调用正常执行（样本路径回归）
  - [负向] 未传 required secret 时不应以空 secret 静默进入执行（记录实际：报错 / 空值 / 其他）
  - [负向] fork PR 修改本地被调 workflow 内容时，执行版本应符合平台声明的信任边界
  - [非功能] 缺参报错信息指明缺失的 secret 名

负向断言目标: required secret 缺失时不应在被调 workflow 内以空值使用 secret（如以空 OBS_AK 执行上传）
优先级线索: RISK-SEC-01（secret 契约边界）→ 建议 P1
破坏级别:   fixture
来源输入:   syntax-reference/trigger-events.md L204-233; workflow-samples/testorg/build_job.yaml（2026-07-22）
```

### INTENT-COMP-031
```
意图 ID:    INTENT-COMP-031
维度标签:   [completeness]
标题:       验证 workflow 顶层 inputs 与 manual_override 字段（未文档化）的实际处理

风险点:     testorg/full_pr.yaml 使用顶层 inputs（12 个，含 manual_override: true/false），
            规范仅定义 on.workflow_dispatch.inputs / on.workflow_call.inputs 两种挂载位置。
            顶层形式是被识别为 workflow 级输入（并与 ${{ inputs.* }} 联动，见 INTENT-COMP-020）、
            还是被当作未知字段静默忽略（GAP-007），直接决定该样本流水线参数是否生效。
预期系统行为: 顶层 inputs 的处理方式确定：被识别则其与触发器 inputs 的合并/覆盖规则明确；
            被忽略则应有校验提示；manual_override 的语义（若生效）被确定。
Oracle 来源: GitCode规格（缺口项，实测记录事实）

验证要点:
  - [正向/记录] 顶层 inputs 的 default 值是否注入 ${{ inputs.* }} 上下文（与 INTENT-COMP-020 互证）
  - [正向/记录] manual_override: true/false 对手动触发表单/参数覆盖的实际影响
  - [负向] 不应出现「参数看似声明实则无效」的静默忽略且无提示

优先级线索: RISK-COMPAT-01 → 建议 P2
破坏级别:   none
来源输入:   workflow-samples/testorg/full_pr.yaml L24-86（2026-07-22）; 规范全文检索确认无定义
```

### INTENT-COMP-032
```
意图 ID:    INTENT-COMP-032
维度标签:   [completeness]
标题:       验证 ${gitcode_*} / ${PIPELINE_*} 非标准插值风格的求值行为

风险点:     testorg 样本 inputs default 混用三种变量风格：${{ atomgit.* }}（规范内）、
            ${gitcode_SOURCE_BRANCH} 与 ${PIPELINE_RUN_ID}（规范全文未提及，疑似 CodeArts 遗留）。
            若后两者被原样保留为字面字符串，依赖其取值的下游参数将静默获得错误值。
预期系统行为: 平台对 ${...} 风格占位符的处理确定：求值（其来源上下文明确）/ 原样保留 / 报错；
            三种风格混用时的求值顺序与优先级确定。
Oracle 来源: GitCode规格（缺口项，实测记录事实）

验证要点:
  - [正向/记录] ${gitcode_*} 与 ${PIPELINE_*} 在 inputs default 中的实际求值结果（逐字记录运行时值）
  - [负向] 未求值的占位符不应以字面量形态静默流入下游 job 参数且无任何提示
  - [非功能] 与 ${{ env.* }} / ${{ atomgit.* }} 混用时的行为一致性

优先级线索: RISK-COMPAT-01 → 建议 P2
破坏级别:   none
来源输入:   workflow-samples/testorg/full_pr.yaml L28-86（2026-07-22）; 规范全文检索确认无定义
```

### INTENT-COMP-033
```
意图 ID:    INTENT-COMP-033
维度标签:   [completeness]
标题:       验证 pre-merge ref（refs/merge-requests/N/merge）的存在性与语义

风险点:     actions-market.md 示例与 testorg 全部 job 通过 checkout ref: refs/merge-requests/<N>/merge
            获取「合并预览」代码，这是 PR 流水线的核心模式；但 checkout 插件文档
            未定义该 ref 的存在性、语义（合并结果提交 vs 源分支头）、
            以及在 PR 源分支强推/目标分支漂移后该 ref 的刷新时机。
            语义不明会导致「测的不是将要合入的代码」这一静默正确性风险。
预期系统行为: 该 ref 在 PR 存续期内可解析；其指向（merge commit / 源分支头）被实测确定；
            源分支更新后 ref 指向刷新；PR 关闭后行为确定（失效/保留）。
Oracle 来源: GitCode规格（缺口项，实测记录事实并回写规格缺口清单）

验证要点:
  - [正向] PR 打开状态下 checkout 该 ref 成功，且取到的代码内容符合实测裁定的语义
  - [正向] 源分支新增提交后该 ref 内容刷新
  - [非功能] PR 合并/关闭后再次解析该 ref 的行为（报错 / 保留快照）被确定
  - [负向] 不应出现 ref 解析成功但内容为陈旧合并结果而无任何标识

优先级线索: RISK-COMPAT-01（正确性相关的隐式语义，概率高）→ 建议 P1
破坏级别:   fixture（需布置 PR 夹具）
来源输入:   actions-market.md; workflow-samples/testorg（2026-07-22）; checkout 插件文档（确认未定义）
```

---

## 4. 统计摘要

| 指标 | 数量 |
|---|---|
| 本轮增量能力项 | **15 条**（其中规格自相矛盾 3 项、规格缺口/未文档化 9 项、边界未明 3 项） |
| 新增规格缺口 | **8 条**（GAP-021 ~ GAP-028），上轮 GAP-001~020 经抽验全部仍成立 |
| 本轮 Intent 总数 | **15 条**（INTENT-COMP-019 ~ INTENT-COMP-033），全部为**新增 delta**，无沿用/合并/改号 |
| 优先级分布（线索，待门禁拍板） | **P1 ×9**（019/020/021/023/025/028/029/030/033）；**P2 ×6**（022/024/026/027/031/032）；**P0 ×0**（risk-register 的 P0 均为安全项，由 security 维度承接；本维度 023/025/030 为安全相关 P1，提供事实底座） |
| 维度标签分布 | completeness 15（全部）；compatibility 5；security 4；usability 2；reliability 1（多标签） |
| 与上轮关系 | 沿用：上轮 30 条 intent 与 20 条 GAP 不重复产出；新增：15 条，主要驱动为 testorg 新样本（2026-07-22）暴露的未文档化行为 + 上轮未覆盖文档（top-level-fields / manually-trigger-pipeline / configuring-images-toolchains / selecting-runner-labels / plugin-security-specification）的声明项；无 ID 冲突（本轮用 spec agent 自有号段 COMP-019+，回填号段 COMPAT-NEW-001~012、REL-067/068 未触碰） |

## 5. 质量清单自检

- [x] 每条能力项/缺口均有出处（文件+位置），无凭空条目；未文档化项明确标注「规范全文检索确认无定义」。
- [x] 默认值/边界显式记录，未知项标 `未知` 并指明下游消费方。
- [x] intent 只写意图层，不含执行细节与 GitCode 具体语法示例。
- [x] 每条 intent 标注 dimensions、Oracle 来源、优先级线索（对齐 risk-register 现有项，无自造级别）。
- [x] 输入版本与样本增量（testorg，2026-07-22）已在 §0 标注。
- [x] 新 ID 与上轮及回填号段无冲突（自有号段 INTENT-COMP-019 起）。
