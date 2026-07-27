# Usability Intents（易用性维度）— Run 2026-07-27-01

> 产出时间：2026-07-27
> 维度 Agent：usability
> 上一轮参考：`runs/2026-07-23-01/intents/usability.md`（28 条 + USE-030，共 29 条）
> 本轮策略：**沿用上一轮 29 条 + 新增 23 条（INTENT-USE-031 ~ INTENT-USE-053）**。新 ID 从 031 起避免与历史冲突（029 在 intent-library 中已被 spec 维度占用为保留号段，故跳过）。

## 输入版本与退化标注

| 输入 | 版本/日期 | 状态 | 对本轮影响 |
|---|---|---|---|
| `inputs/business-context/README.md` | 2026-07-21 | ⚠️ 仍只有模板，但 §4 补了「易用/兼容性测试」三维诉求（文档易用性 / 实操易用性 / GitHub 兼容性） | 据此新增 USE-050 / USE-051 / USE-052 等实操与文档易用性 intent |
| `inputs/workflow-samples/` | 2026-07-22 | ✅ 已补 11 个真实样本（cann 7 + op-plugin 1 + testorg 3） | 上一轮缺失，本轮据此发现大量「文档未写但真实在用」的语法差异，新增 USE-036 ~ USE-040 |
| `inputs/existing-cases/cases.md`（问题 sheet 22 条） | 2026-07-20 | ✅ 已预处理 | 上一轮未充分消费；本轮从「问题」sheet 抽取 runner.os/arch 值格式、env 未注入、container.image 不可用、无 gh CLI、schedule 不触发无提示等真实痛点，新增 USE-041 ~ USE-048 |
| `inputs/gitcode-spec/actions-market.md` | 2026-07-23 | ✅ 新输入（49 个插件 README，258KB） | 上一轮不存在；据此新增 USE-052 |
| `inputs/gitcode-spec/00-overview.md`、`01-quick-start.md` 等 50 页 | 2026-07-20 抓取 | ✅ | 上一轮已读但仅作 oracle；本轮以「文档间交叉一致性」视角重读，发现 runs-on / stages / cron / shell 示例等多处自相矛盾，新增 USE-031 ~ USE-035 |
| `baseline/parity-matrix.md`、`risk-register.md`、`quality-gate.md` | 2026-07-21/22 基线 | ✅ | 优先级对齐来源 |

---

## 1. 与上一轮（2026-07-23-01）的关系

### 1.1 沿用（29 条，ID 不变）

下列 intent 经过本轮重读输入后仍成立，场景、判据、优先级线索无需修订，**原样沿用**；新发现的关联证据以「补强备注」附在条目后，不改 ID、不改标题。

| Intent ID | 标题（摘） | 优先级线索 | 本轮补强备注 |
|---|---|---|---|
| INTENT-USE-001 | `.github/workflows` 搬运时的路径指引 | RISK-USE-01 / P1 | 仍成立；quick-start 已显式强调目录，但实测「放错目录时系统是否静默」仍需验证 |
| INTENT-USE-002 | `github.*` 失效是否提示 `atomgit.*` | RISK-USE-01 / P1 | 仍成立 |
| INTENT-USE-003 | `GITHUB_*` 空值时的提示质量 | RISK-USE-01 / P1 | 仍成立；新增关联证据 TC-533（Job env 未注入 Shell）见 USE-046 |
| INTENT-USE-004 | `success()` 括号报错 | RISK-USE-01 / P1 | 仍成立；expressions.md 把无括号写法称「函数」的术语混乱另见 USE-035 |
| INTENT-USE-005 | permissions 命名报错 | RISK-USE-01 / P1 | 仍成立 |
| INTENT-USE-006 | `runs-on` 标签不匹配报错 | RISK-USE-01 / P1 | 仍成立；与新增 USE-031（三种写法自相矛盾）互补——USE-006 测「报错质量」，USE-031 测「文档一致性」 |
| INTENT-USE-007 | `actions/checkout@v4` 报错迁移指引 | RISK-USE-01 / P1 | 仍成立 |
| INTENT-USE-008 | inputs 非 string 类型报错 | RISK-USE-01 / P1 | 仍成立 |
| INTENT-USE-009 | `pull_request` types GitHub 命名静默失败 | RISK-USE-01 / P1 | 仍成立；历史问题 TC-234/236/461/463/561 实证此路径高频踩坑 |
| INTENT-USE-010 | 废弃命令报错给出替代 | RISK-USE-01 / P1 | 仍成立 |
| INTENT-USE-011 | stages/post 文档可发现性 | RISK-COMPAT-01 / P1 | 仍成立；本轮发现 stages 字段本身有 4 种写法（USE-032），「发现入口」之外还有「写法一致性」新问题 |
| INTENT-USE-012 | 文档残留 `GITHUB_*` 措辞 | RISK-COMPAT-01 / P1 | 仍成立 |
| INTENT-USE-013 | `runner.os` 支持平台文档-实际一致 | RISK-COMPAT-01 / P1 | 仍成立；「平台范围」之外本轮补「值大小写格式」问题（USE-041） |
| INTENT-USE-014 | vars 上下文文档-样本矛盾 | RISK-COMPAT-01 / P1 | 仍成立；样本 ops-nn_action.yml 注释 `#11` 仍是有效证据 |
| INTENT-USE-015 | paths 300 文件上限文档显眼性 | RISK-COMPAT-01 / P1 | 仍成立 |
| INTENT-USE-016 | secret 脱敏绕过文档-实际一致 | RISK-SEC-01 / P0 | 仍成立；唯一 P0 易用性 intent，继续保留 |
| INTENT-USE-017 | 日志 step 时间线可读性 | RISK-COMPAT-01 / P1 | 仍成立 |
| INTENT-USE-018 | 日志搜索/下载/高亮交互 | RISK-COMPAT-01 / P1 | 仍成立 |
| INTENT-USE-019 | 状态徽标回写可读性 | RISK-COMPAT-01 / P1 | 仍成立 |
| INTENT-USE-020 | STEP_SUMMARY Markdown 渲染 | RISK-COMPAT-01 / P1 | 仍成立 |
| INTENT-USE-021 | `::error::`/`::warning::` 注解 | RISK-COMPAT-01 / P1 | 仍成立 |
| INTENT-USE-022 | YAML 报错行号与可操作性 | RISK-USE-01 / P1 | 仍成立 |
| INTENT-USE-023 | 未知字段报错质量 | RISK-USE-01 / P1 | 仍成立；USE-036/037/040 给出新的「未知字段」具体实例 |
| INTENT-USE-024 | 表达式语法错误报错质量 | RISK-USE-01 / P1 | 仍成立 |
| INTENT-USE-025 | Runner 标签无匹配报错质量 | RISK-USE-01 / P1 | 仍成立 |
| INTENT-USE-026 | workflow_call 超 2 层报错 | RISK-COMPAT-01 / P1 | 仍成立 |
| INTENT-USE-027 | concurrency.max 越界报错 | RISK-COMPAT-01 / P1 | 仍成立 |
| INTENT-USE-028 | Secret 命名违规报错质量 | RISK-SEC-01 / P1 | 仍成立 |
| INTENT-USE-030 | workflow_dispatch inputs 默认值与必填校验（spec 维度挂入） | RISK-USE-01 / P1 | 仍成立 |

### 1.2 新增（23 条，INTENT-USE-031 ~ INTENT-USE-053）

新增 intent 按主题分为 5 组，详见 §2：

- **A. 文档自相矛盾**（USE-031 ~ USE-035）：同一字段跨文档写法不一 / 文档示例照抄不能跑
- **B. 真实样本在用但文档未写**（USE-036 ~ USE-040）：从 workflow-samples 发现的命名双轨、未文档化字段、双插值语法
- **C. 文档承诺 vs 实际能力**（USE-041 ~ USE-048）：从 existing-cases 问题 sheet 提取的实证痛点
- **D. 实操 / 新手路径**（USE-049 ~ USE-051）：business-context §4 维度 2 的落地
- **E. Action 生态**（USE-052 ~ USE-053）：基于新输入 actions-market.md

### 1.3 未沿用 / 合并说明

- 无删除。上一轮 29 条全部沿用。
- USE-014（vars 矛盾）与本轮想补的「文档应显式标注 vars 已知不支持 #11」**合并**——不新增条目，通过在 USE-014 的「本轮补强备注」里强化判据即可，避免与历史 ID 双份。
- USE-013（runner.os 平台范围）与本轮新发现「runner.os 值大小写」（`linux` vs `Linux`）**拆分**——平台范围沿用 USE-013，值格式新增 USE-041，两者关注的用户困扰不同。

---

## 2. 新增 Intent 详表

> 模板字段沿用上一轮约定：`意图 ID / 维度标签 / 标题 / 场景 / 用户视角 / 风险点 / 预期系统行为 / Oracle 来源 / 验证要点 / 可理解性判据 / 是否 llm_assisted / 关联兼容性差异 / 优先级线索 / 破坏级别 / 来源输入`。

### A 组：文档自相矛盾（文档作为 oracle 自身不可信）

```
意图 ID:    INTENT-USE-031
维度标签:   [usability]
标题:       runs-on 标签写法跨文档三种形态互相矛盾

场景:       新手按「快速开始」Copy 第一个 workflow，改天翻「选择 Runner 标签」又看到另一种写法，
            再翻「产品总览」看到第三种写法。三处都是官方文档，用户不知道哪一种是「真正合法」的。
用户视角:   迁移者 / 新手，对 GitCode 标签体系尚未建立心智。
风险点:     01-quick-start.md 示例写 `runs-on: ubuntu-latest`（GitHub 单标签风格）；
            00-overview.md 与 workflow-file-location-structure.md 示例写 `runs-on: [ubuntu-latest, x64, small]`（数组三段式）；
            selecting-runner-labels.md 与 token-permissions.md 写 `runs-on: {ubuntu-24,x64,small}`（花括号三段式）；
            configure-jobs.md 又把自托管写成 `runs-on: {type, group, labels}` 对象形态。
            同一概念至少 4 种形态，且文档之间互不引用、不说明取舍关系。
预期系统行为: 文档应选定一种「推荐写法」并在所有示例统一；其他写法如确被平台兼容，应在「选择 Runner 标签」
            一处集中说明「以下写法等价」，而不是让每个页面自由发挥。
Oracle 来源: GitCode 规格多页交叉（quick-start / overview / selecting-runner-labels / configure-jobs /
            workflow-file-location-structure / token-permissions）

验证要点:
  - [正向] 选定 quick-start 示例 `runs-on: ubuntu-latest` 提交，验证平台是否真能调度（若不能，则 quick-start 示例本身错误）
  - [正向] 数组 `[ubuntu-latest, x64, small]` 与花括号 `{ubuntu-24,x64,small}` 分别提交，验证是否都合法
  - [负向] 文档之间不应互相矛盾（同一字段在 ≥3 个官方页给出互不相同的形式即视为缺陷）
  - [非功能] 「选择 Runner 标签」页应列出全部合法形态并标注推荐项

可理解性判据: 对 50 页 gitcode-spec 全文 grep `runs-on:` 后归纳形态数；形态数 > 2 且文档未在任何一处集中说明等价关系，即视为不合格。
            eval: 否（文档扫描 + 形态计数可判定；平台对哪种形态合法另由 compat 维度验证）。

关联兼容性差异: parity-matrix「runs-on 标签体系」🟡
优先级线索: RISK-USE-01（迁移报错不指明差异）→ P0
            理由：runs-on 是新手写第一个 workflow 的第一个必写字段，此处置信度崩塌直接影响 onboarding。
破坏级别:   none
来源输入:   gitcode-spec/01-quick-start.md; gitcode-spec/00-overview.md;
            gitcode-spec/runner-management/selecting-runner-labels.md;
            gitcode-spec/writing-pipelines/configure-jobs.md;
            gitcode-spec/writing-pipelines/workflow-file-location-structure.md;
            gitcode-spec/security-permissions/token-permissions.md
```

```
意图 ID:    INTENT-USE-032
维度标签:   [usability]
标题:       stages / jobs 字段语法跨文档四种形态互相矛盾

场景:       stages 是 GitCode 特有概念，文档解释它时给出多种互相不一致的 YAML 形态，
            用户照抄任一示例都可能与平台实际期望不符。
用户视角:   需要使用 stages 做门禁管控的中级用户。
风险点:     00-overview.md 写 `stages: - name: build-stage`（list of map）；
            workflow-file-location-structure.md「完整基本结构示例」写 `stages: build_stage: name: 构建`（map 形态）；
            同页「staged-pipeline 示例」又写 `stages: - name: build-stage`（list 形态）——同一文档内自相矛盾；
            view-run-results.md 与 token-permissions.md 进一步写 `stages: compile: name: build; jobs: - name: compile`（map 形态 + jobs 为 list of map with name）；
            真实样本 cann/ops-nn_action.yml 使用 `stages: stage1: name: image; jobs: JOB_image: ...`（map 形态 + jobs 为 map keyed by id）。
            即 stages 至少有 list/map 两种形态，jobs 在 stages 内又有 list-of-name-map / map-by-id 两种形态，合计 4 种组合。
预期系统行为: 文档应明确 stages 与 jobs 的唯一合法形态（或显式声明「以下形态等价」），并把所有示例统一为该形态。
Oracle 来源: GitCode 规格多页交叉 + 真实样本（cann/ops-nn_action.yml）

验证要点:
  - [正向] 分别提交 list 形态、map 形态、jobs-as-list、jobs-as-map 四种组合，验证平台实际接受哪种
  - [负向] 文档不应在同一页内对同一字段给出两种形态而不加说明
  - [非功能] 「工作流文件位置与基本结构」页应对 stages 给出单一权威形态定义

可理解性判据: 对 gitcode-spec 全文 grep `^stages:` 与 `jobs:` 在 stages 下的形态；形态数 > 1 且文档未在任何一处说明等价关系即不合格。
            eval: 否（文档扫描可判定）。

关联兼容性差异: parity-matrix「stages 阶段机制」❌（GitHub 无对应概念，文档即为唯一 oracle，自相矛盾时无外部参照）
优先级线索: RISK-USE-01 → P0
            理由：stages 是 GitCode 唯一「特有且必学」的编排概念，文档自身形态不稳，用户没有任何外部参照可校正。
破坏级别:   none
来源输入:   gitcode-spec/00-overview.md; gitcode-spec/writing-pipelines/workflow-file-location-structure.md;
            gitcode-spec/running-pipelines/view-run-results.md; gitcode-spec/security-permissions/token-permissions.md;
            workflow-samples/cann/ops-nn_action.yml
```

```
意图 ID:    INTENT-USE-033
维度标签:   [usability]
标题:       文档代码示例「照抄即可跑」的端到端可复刻性抽查

场景:       新手的最短路径是「Copy 文档示例 → 提交 → 看到绿色」。若官方示例本身有错，
            新手会在第一小时就流失。
用户视角:   完全新手。
风险点:     本轮发现 4 处「照抄会失败或行为不符预期」的官方示例：
            (1) syntax-reference/trigger-events.md 在「schedule 最短间隔 5 分钟」提示下方仍给出 `* * * * *`（每分钟）作为示例；
            (2) syntax-reference/workflow-commands.md 多行输出示例漏写 `>> $ATOMGIT_OUTPUT` 重定向，照抄会得到空输出；
            (3) writing-pipelines/configure-steps.md `shell: bash` 示例配 `Write-Host`（PowerShell 命令）、`shell: python` 示例配 `echo`（shell 命令）；
            (4) writing-pipelines/configure-jobs.md「job 输出参数」章节声称演示 outputs，但示例只写 step 未声明 `outputs:` 字段。
预期系统行为: 所有出现在官方文档的 YAML/shell 片段应「复制-粘贴-提交」即可得到文档声称的结果；
            若示例为了简洁省略关键行，应显式标注「此处省略 X」。
Oracle 来源: GitCode 规格各页自身声明（文档内部 oracle）

验证要点:
  - [正向] 抽取 quick-start / configure-triggers / configure-jobs / configure-steps / workflow-commands 中全部 ```yaml 代码块，
          逐个在隔离实例提交并断言「结果与文档描述一致」
  - [负向] 示例不应包含「会导致与文档描述相反结果」的错误（如 shell 类型与命令语言不匹配）
  - [非功能] 文档示例应在页面头部标注「本示例已在 GitCode x.y 版本实测通过」之类的版本锚点

可理解性判据: 对抽取到的代码块逐一在隔离实例执行；任一代码块运行结果与文档描述不符即该示例不合格；
            整体合格率 < 100% 即维度不通过。eval: 否（实际跑一遍即可判定）。

关联兼容性差异: 无（纯文档质量）
优先级线索: RISK-USE-01 → P0
            理由：示例不可复刻是新手流失的最大单一原因；quality-gate 易用性「核心迁移路径可跑」直接命中。
破坏级别:   none
来源输入:   gitcode-spec/syntax-reference/trigger-events.md; gitcode-spec/syntax-reference/workflow-commands.md;
            gitcode-spec/writing-pipelines/configure-steps.md; gitcode-spec/writing-pipelines/configure-jobs.md;
            gitcode-spec/01-quick-start.md
```

```
意图 ID:    INTENT-USE-034
维度标签:   [usability]
标题:       官方文档章节编号跳跃与编辑质量

场景:       文档章节号是用户引用与沟通的最小单位（「见 5.4 节」）。编号混乱会让用户在二人对话、
            issue 描述、内部 wiki 引用时产生错位。
用户视角:   所有读者。
风险点:     syntax-reference/workflow-commands.md 章节号为 5.1 / 5.2 / 5.3 / 5.4 / 5.6（缺 5.5）；
            syntax-reference/trigger-events.md 章节号为 1.1 / 1.2 / 1.3 / 1.4 / 1.5 / 1.6 / 1.8 / 1.9（缺 1.7；
            INDEX.md 注明「系官方页原样，非抓取遗漏」——即官方原文就缺）。
预期系统行为: 官方文档的章节号应连续；若因历史原因跳号，应在跳号处显式注明「原 5.5 已合并至 5.4」之类说明。
Oracle 来源: 文档自身编辑规范

验证要点:
  - [负向] syntax-reference/ 下各页章节号不应跳号
  - [非功能] 若官方确有跳号，应在跳号位置补「编号沿革」一句话说明

可理解性判据: 对 syntax-reference/*.md 扫描 `^## \d+\.\d+` 并检测连续性；存在跳号且无说明即不合格。
            eval: 否（正则扫描可判定）。

关联兼容性差异: 无
优先级线索: RISK-COMPAT-01 → P2
            理由：不影响功能正确性，仅影响文档引用精确度；非上线 blocker。
破坏级别:   none
来源输入:   gitcode-spec/syntax-reference/workflow-commands.md; gitcode-spec/syntax-reference/trigger-events.md;
            gitcode-spec/INDEX.md
```

```
意图 ID:    INTENT-USE-035
维度标签:   [usability]
标题:       expressions.md 函数表语法标记与术语混乱

场景:       用户按文档函数表写表达式；函数表的「写法示意」本身有 typo 或术语错误时，
            用户会照抄错误写法。
用户视角:   写表达式的中级用户。
风险点:     syntax-reference/expressions.md 函数表把 `hashFiles` 写成 `hashFiles(paths...))`（多了一个右括号）；
            同表把 `success` / `failed` / `always` / `cancelled` 列在「函数」一节并称作函数，
            但这四个在 GitCode 是无括号关键字（与 GitHub 的 `success()` 函数调用不同），
            「函数」这一术语会让迁移者误以为仍可加括号，恰好踩 INTENT-USE-004 的坑。
预期系统行为: 函数表的语法示意应可粘贴即用；状态关键字应单独一节标注「状态关键字（非函数调用，无括号）」，
            与真正的函数（contains/startsWith/...）区分。
Oracle 来源: GitCode 规格 expressions.md 自身 + COMPAT-NOTES.md §3

验证要点:
  - [负向] 函数表语法列不应含无法通过自身 parser 的字符串（如多余括号）
  - [负向] 文档不应把无括号关键字称为「函数」而不加区别说明
  - [非功能] 状态关键字与函数应在视觉/章节上有明确区分

可理解性判据: 抽取函数表「语法」列每行，送入 GitCode 表达式 parser 验证可解析性；任一行 parse 失败即不合格；
            「函数」一词是否同时覆盖 `success` 等无括号关键字可由字符串扫描判定。
            eval: 否。

关联兼容性差异: COMPAT-NOTES.md §3；parity-matrix「状态函数括号语法」❌
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   gitcode-spec/syntax-reference/expressions.md; COMPAT-NOTES.md §3
```

### B 组：真实样本在用但文档未写（文档-生态脱节）

```
意图 ID:    INTENT-USE-036
维度标签:   [usability, compatibility]
标题:       命名双轨 — id/identifier、pull_request_comment/pr_comment、comments/keyword

场景:       真实试点项目的 workflow 大量使用与官方文档不同的字段名；用户看文档学一套，
            看真实项目又看到另一套，不知道哪套是「正版」。
用户视角:   迁移者参考内部试点项目 workflow 作为迁移模板时。
风险点:     cann/ops-nn_action.yml 中 step 标识用 `identifier:` 而文档（configure-steps.md）用 `id:`；
            同文件触发器同时写 `pull_request_comment:` 与 `pr_comment:` 两个事件名，文档只提 `pull_request_comment`；
            评论过滤字段同文件既有 `comments:` 又有 `keyword:`，文档只提 `comments:`。
            若这些是历史别名，文档未说明；若 `pr_comment` / `keyword` / `identifier` 已废弃但仍被样本使用，
            则样本在误导用户。
预期系统行为: 文档应就每个「双名」字段给出权威说明：哪个是推荐名、哪个是别名/废弃名、何时废弃；
            若平台对两种写法都接受，应显式声明等价关系；若只接受其一，平台应对另一种给出明确报错而非静默忽略。
Oracle 来源: GitCode 规格（configure-steps.md / syntax-reference/trigger-events.md）+
            真实样本（cann/ops-nn_action.yml）

验证要点:
  - [正向] 分别用 `id:` 与 `identifier:` 提交同一 step，验证平台是否都接受且行为一致
  - [正向] 分别用 `pull_request_comment` 与 `pr_comment` 提交，验证平台是否都识别
  - [负向] 若两种写法并存且行为不同，文档必须说明差异
  - [非功能] 平台对废弃名应给出 deprecation 警告而非静默接受

可理解性判据: 对「文档字段集合」与「样本字段集合」做 diff；任何样本字段不在文档字段集合内，且文档未在任何一处提及该字段，即视为缺陷。
            eval: 否（集合 diff 可判定）。

关联兼容性差异: parity-matrix「未知/不支持字段处理」❓
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   workflow-samples/cann/ops-nn_action.yml;
            gitcode-spec/writing-pipelines/configure-steps.md;
            gitcode-spec/syntax-reference/trigger-events.md
```

```
意图 ID:    INTENT-USE-037
维度标签:   [usability, compatibility]
标题:       未文档化字段 — select / manual_override / code-update / 顶层 inputs

场景:       真实样本使用多个文档完全未提的字段；用户看到这些字段无法从文档学到语义，
            只能猜。
用户视角:   阅读内部试点 workflow 的迁移者。
风险点:     testorg/full_pr.yaml 使用 `stages.<id>.select: selected_by_default`、
            `inputs.<name>.manual_override: true|false`、`on.pull_request.code-update: false`、
            顶层 `inputs:` 字段（非 `on.workflow_dispatch.inputs`）。
            上述字段在 gitcode-spec 50 页中均无说明。
预期系统行为: 平台实际支持的每个字段都应在语法参考页有自己的条目（名称、取值、默认、示例）；
            已废弃但仍在样本中的字段应在样本所在仓库显式标注。
Oracle 来源: 真实样本 vs 文档集合 diff

验证要点:
  - [正向] 提交含 `select: selected_by_default` 的 workflow，验证平台是否识别、UI 是否呈现「默认选中」语义
  - [负向] 平台不应静默忽略未文档化字段（用户会误以为生效）
  - [非功能] 文档应对「顶层 inputs」与「on.workflow_dispatch.inputs」的关系给出说明

可理解性判据: 把样本中所有 YAML key 集合与文档语法参考中列出的合法 key 集合做 diff；
            样本独有且文档未提的 key 数量应为 0，每多 1 个即一条缺陷。eval: 否。

关联兼容性差异: parity-matrix「未知/不支持字段处理」❓
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   workflow-samples/testorg/full_pr.yaml;
            gitcode-spec/writing-pipelines/workflow-file-location-structure.md;
            gitcode-spec/syntax-reference/trigger-events.md
```

```
意图 ID:    INTENT-USE-038
维度标签:   [usability, compatibility]
标题:       变量插值双语法 — ${gitcode_*} / ${PIPELINE_*} / atomgit.repositoryurl

场景:       样本中混用三种变量插值风格，文档只教一种，用户不知道另外两种是什么、何时该用、
            与 `${{ }}` 的优先级如何。
用户视角:   阅读并改造内部试点 workflow 的迁移者。
风险点:     testorg/full_pr.yaml 同时使用 `${gitcode_SOURCE_BRANCH}` / `${PIPELINE_RUN_ID}` / `${PROJECT_ID}`
            （美元单括号、全大写、蛇形）与 `${{atomgit.event.pull_request.number}}`（标准 `${{ }}`）；
            还出现 `atomgit.repositoryurl`（全小写、无下划线）这一文档中查不到的属性名，
            以及 `${{ env.ATOMGIT_WORKSPACE }}` 这种把系统变量当 env 上下文属性访问的写法。
            文档（variables-secrets-context-expressions.md / context.md）对以上三种写法均未说明。
预期系统行为: 文档应列出平台支持的全部插值语法（含历史遗留语法），标注每种语法的推荐程度、
            与 `${{ }}` 的优先级、是否存在废弃计划；`atomgit.*` 上下文的合法属性名应有完整清单，
            大小写敏感规则应明示。
Oracle 来源: 真实样本 vs 文档集合 diff

验证要点:
  - [正向] 在测试 workflow 中使用 `${gitcode_X}` / `${PIPELINE_Y}` 提交，验证是否被求值
  - [负向] 若这些语法已废弃，平台应在解析时给出 deprecation 警告
  - [非功能] `atomgit.*` 上下文属性应有完整、大小写明确的官方列表

可理解性判据: 同 USE-037 的集合 diff；样本中出现而文档未列的插值语法/属性名数量应为 0。
            eval: 否。

关联兼容性差异: parity-matrix「上下文对象命名 atomgit.*」❌
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   workflow-samples/testorg/full_pr.yaml;
            gitcode-spec/core-concepts/variables-secrets-context-expressions.md;
            gitcode-spec/syntax-reference/context.md
```

```
意图 ID:    INTENT-USE-039
维度标签:   [usability]
标题:       未文档化函数 default() 的真实语义

场景:       样本 `if: "${{ default() }}"` 多次出现；文档 expressions.md 函数表无 `default`。
            用户无法理解这个条件在判断什么。
用户视角:   阅读样本的迁移者。
风险点:     cann/ops-nn_action.yml 至少 2 处 `if: "${{ default() }}"`；
            testorg/full_pr.yaml 也在 `select: selected_by_default` 上下文中暗示存在「默认选中」语义。
            该函数语义、参数、返回值在文档中完全缺失。
预期系统行为: 平台支持的函数应在 expressions.md 函数表中有完整条目（签名、参数、返回、示例）；
            若为内部/遗留函数不应出现在用户可见的样本中，或文档应标注「内部函数，不建议使用」。
Oracle 来源: 真实样本 vs expressions.md 函数表 diff

验证要点:
  - [正向] 提交含 `if: ${{ default() }}` 的 workflow，观察实际求值结果
  - [负向] 文档函数表不应缺少平台实际支持的函数
  - [非功能] 若为内部函数，文档应说明「不要依赖此函数」

可理解性判据: expressions.md 函数表函数名集合 ⊇ 样本中实际出现的函数名集合；每缺 1 个即一条缺陷。
            eval: 否。

关联兼容性差异: parity-matrix「表达式函数 contains/hashFiles/toJson」❓
优先级线索: RISK-USE-01 → P2
            理由：样本量有限，推测非高频路径。
破坏级别:   none
来源输入:   workflow-samples/cann/ops-nn_action.yml; workflow-samples/testorg/full_pr.yaml;
            gitcode-spec/syntax-reference/expressions.md
```

```
意图 ID:    INTENT-USE-040
维度标签:   [usability, compatibility]
标题:       runs-on 含资源池名的 4 段式写法文档未提

场景:       样本大量使用 `runs-on: [codearts-hosted, ubuntu-latest, x64, large]` 或
            `[dedicate-hosted, arm64, xlarge]` 这种把「资源池名」作为第一段、
            后接（os / arch / flavor）的 4 段（或 3 段含池名）写法。
用户视角:   需要使用专属资源池（dedicate-hosted）的企业用户。
风险点:     文档（selecting-runner-labels.md / configure-jobs.md）只讲三段式 `{os},{arch},{flavor}`、
            `default`、自托管 `self-hosted + labels` 三种；未提「官方池之外还有 dedicate-hosted / codearts-hosted
            等具名资源池可写在第一段」。用户从样本学到这种写法后无法验证它是不是合法、可用池名清单在哪。
预期系统行为: 文档应列出全部官方/专属资源池名（default / dedicate-hosted / codearts-hosted / ...）、
            各自的可用 flavor 范围、申请方式；并说明具名资源池在 runs-on 中的合法位置。
Oracle 来源: 真实样本（cann/*.yml / testorg/*.yaml / op-plugin/*.yml） vs selecting-runner-labels.md diff

验证要点:
  - [正向] 提交 `runs-on: [dedicate-hosted, x64, large]`，验证平台是否识别、是否进入对应资源池
  - [负向] 文档不应让用户只能从内部样本学到这种写法
  - [非功能] 资源池名清单、与 `{os,arch,flavor}` 的组合规则应集中在 Runner 文档一节

可理解性判据: 样本中出现的资源池名集合 ⊆ 文档列出的资源池名集合；每缺 1 个即一条缺陷。
            eval: 否。

关联兼容性差异: parity-matrix「runs-on 标签体系」🟡
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   workflow-samples/cann/*.yml; workflow-samples/testorg/*.yaml;
            workflow-samples/op-plugin/PR-pipeline_op-plugin.yml;
            gitcode-spec/runner-management/selecting-runner-labels.md
```

### C 组：文档承诺 vs 实际能力（来自 existing-cases 问题 sheet 的实证）

```
意图 ID:    INTENT-USE-041
维度标签:   [usability, compatibility]
标题:       runner 上下文值的大小写 / 格式与文档不一致

场景:       用户写 `if: runner.os == 'Linux'` 按文档判断平台；实际返回 `linux`（小写），条件不成立，
            用户排查半小时才发现是大小写。
用户视角:   中级用户，依赖 runner 上下文做条件分支。
风险点:     问题 sheet TC-137/138 实证：`runner.os` 实际返回 `linux`，文档（syntax-reference/context.md）
            写 `Linux`；TC-095 实证：`runner.arch` 实际返回 `x86_64`，文档写 `X64`。
            文档值与实际值的大小写 / 命名风格不一致直接破坏表达式。
预期系统行为: 文档列出的枚举值应与实际返回值逐字符一致；若平台做了大小写不敏感比较，
            文档应显式说明比较规则。
Oracle 来源: GitCode 规格（syntax-reference/context.md）+ 实际运行行为（问题 sheet 实证）

验证要点:
  - [正向] 在 step 中 `echo "${{ runner.os }}"` 与 `echo "${{ runner.arch }}"`，断言返回值精确字符串
  - [负向] 文档枚举值与实际返回值不应仅在大小写/连字符上不同
  - [非功能] 若平台比较时大小写不敏感，文档应明示

可理解性判据: 实际返回值与文档枚举值做逐字符 diff；存在差异且文档未说明比较规则即不合格。
            eval: 否。

关联兼容性差异: parity-matrix「上下文对象命名」❌（连带属性值格式）
优先级线索: RISK-COMPAT-01 → P1
破坏级别:   none
来源输入:   gitcode-spec/syntax-reference/context.md; inputs/existing-cases/cases.md 问题 sheet（TC-095 / TC-137/138）
```

```
意图 ID:    INTENT-USE-042
维度标签:   [usability, compatibility]
标题:       container.image 文档声明可用但实际不可用

场景:       用户按文档写 `container.image` 自定义镜像，平台报错或忽略；用户无法判断是
            自己写错还是平台未实现。
用户视角:   需要自定义构建环境的中高级用户。
风险点:     问题 sheet TC-273 实证：文档声明的 `container.image` 能力实际无法使用；
            configure-jobs.md / view-run-results.md 在示例中引用 `container:` 字段但未标注可用状态。
预期系统行为: 文档应对尚未 GA 的能力显式标注「即将支持 / Beta / 仅特定资源池可用」；
            若平台已下线该能力，文档应移除示例。
Oracle 来源: GitCode 规格 vs 实际行为（TC-273 实证）

验证要点:
  - [正向] 提交含 `container.image` 的 workflow，观察平台行为（报错 / 忽略 / 实际生效）
  - [负向] 文档不应把不可用的能力以正式语法呈现
  - [非功能] 能力可用性状态（GA / Beta / 未支持）应在字段说明旁显式标注

可理解性判据: 文档中出现的字段集合与实际平台可用字段集合做 diff；文档多出且未标注「未支持」的字段每 1 个即一条缺陷。
            eval: 否。

关联兼容性差异: parity-matrix「未知/不支持字段处理」❓
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   gitcode-spec/writing-pipelines/configure-jobs.md;
            inputs/existing-cases/cases.md 问题 sheet（TC-273）
```

```
意图 ID:    INTENT-USE-043
维度标签:   [usability]
标题:       environment 字段语法文档缺失

场景:       用户写 `environment: production` 想绑定环境级 Secret 审批；平台报 unknown property，
            文档中查不到 environment 的 YAML 写法。
用户视角:   需要环境审批流的中高级用户。
风险点:     问题 sheet TC-010 实证：`environment` 字段不被平台识别（unknown property），
            但 using-secrets.md 提到「环境级 Secret 可配置审批人」——文档描述了能力，未描述 YAML 语法。
预期系统行为: 文档应给出 environment 字段的完整 YAML 语法（位置、取值、与 Secret 审批的绑定关系）；
            若该能力尚未开放，应在「环境级 Secret」章节显式说明「environment 字段暂未支持，审批能力仅通过 UI 配置」。
Oracle 来源: GitCode 规格（using-secrets.md）vs 实际行为（TC-010 实证）

验证要点:
  - [负向] 文档不应描述能力但不描述对应语法
  - [非功能] 平台对未识别字段的报错信息应给出「该字段是否未来支持」的指引

可理解性判据: 文档「能力描述」与「语法参考」应一一对应；能力描述存在但语法参考缺失即不合格。
            eval: 否。

关联兼容性差异: 无
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   gitcode-spec/security-permissions/using-secrets.md;
            inputs/existing-cases/cases.md 问题 sheet（TC-010）
```

```
意图 ID:    INTENT-USE-044
维度标签:   [usability, compatibility]
标题:       系统环境变量清单与实际注入集合不一致

场景:       用户在脚本里引用 `$ATOMGIT_REPOSITORY_OWNER`，得到空值；文档（runtime-environment-variables.md
            / view-job-logs.md）列出的 `ATOMGIT_*` 清单要么不含此变量、要么含了但实际未注入。
用户视角:   写 shell 脚本依赖系统变量的中级用户。
风险点:     问题 sheet TC-206 实证：`ATOMGIT_REPOSITORY_OWNER` 未注入 Runner；
            TC-220 实证：`ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS` 默认值缺失；
            view-job-logs.md 列出 8 个 `ATOMGIT_*` 变量，runtime-environment-variables.md 列出更多，
            两页清单本身不一致。
预期系统行为: 文档应给出唯一的「系统环境变量完整清单」页，标注每个变量是否默认注入、默认值、可读性；
            其他页面引用该清单而非各自列子集。
Oracle 来源: GitCode 规格（runtime-environment-variables.md / view-job-logs.md）+ 实际 Runner 注入集合

验证要点:
  - [正向] 在 step 中 `env | grep ^ATOMGIT_`，断言实际注入集合
  - [负向] 文档列出的变量在实际注入集合中应全部存在（不存在即文档失实）
  - [非功能] 两页文档列出的清单应一致

可理解性判据: 实际注入集合 vs 文档列出集合做 diff；任一方向存在差集且文档未说明即不合格。
            eval: 否。

关联兼容性差异: COMPAT-NOTES.md §2
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   gitcode-spec/action-development/runtime-environment-variables.md;
            gitcode-spec/running-pipelines/view-job-logs.md;
            inputs/existing-cases/cases.md 问题 sheet（TC-206 / TC-220）
```

```
意图 ID:    INTENT-USE-045
维度标签:   [usability]
标题:       缺 GitCode 等效 CLI（gh 对应物）的迁移指引

场景:       迁移者的 workflow 中大量使用 `gh pr comment`、`gh release create` 等 GitHub CLI 命令；
            在 GitCode Runner 上 `gitcode` / `gh` 命令不存在，脚本直接 command not found。
用户视角:   从 GitHub 迁移、重度依赖 gh CLI 的用户。
风险点:     问题 sheet TC-502 实证：Runner 未提供类似 gh 的 CLI；文档未在迁移指引中说明
            「gh CLI 不可用，可改用 curl + ATOMGIT_TOKEN + REST API」的替代方案。
            token-permissions.md 示例演示了 curl 调用，但未把它框定为「gh 替代方案」，
            迁移者难以发现。
预期系统行为: 文档应在「迁移指引 / 常见问题」中显式说明：Runner 是否预装 GitCode CLI；
            若未预装，应给出 gh → curl 的对照示例（覆盖 pr comment / checks / release 三类高频操作）。
Oracle 来源: 迁移者合理预期 + 实际 Runner 能力（TC-502 实证）

验证要点:
  - [负向] Runner 上 `gh` / `gitcode` / `atomgit` 命令不存在时，文档应有对应说明
  - [非功能] 「从 GitHub 迁移」章节应包含「gh CLI 替代方案」小节

可理解性判据: 文档「迁移指引 / 常见问题」中是否存在「gh」相关小节；缺失即不合格。
            eval: 否（文档扫描可判定）。

关联兼容性差异: 无
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   gitcode-spec/security-permissions/token-permissions.md;
            inputs/existing-cases/cases.md 问题 sheet（TC-502）
```

```
意图 ID:    INTENT-USE-046
维度标签:   [usability, compatibility]
标题:       job env 未注入到 Runner shell — 文档明确承诺的能力未兑现

场景:       用户在 job 级写 `env: {APP_ENV: prod}`，在 step 的 `run:` 里 `echo $APP_ENV` 得到空值；
            表达式 `${{ env.APP_ENV }}` 却能取到。文档（configure-jobs.md / using-script-commands.md）
            明确承诺「job env 对该 job 内所有 step 可见」。
用户视角:   所有写 env 的用户。
风险点:     问题 sheet TC-533 实证：Runner 不注入 Job env 到 Shell；表达式层可取、shell 层恒 UNSET。
            这违反「变量注入 Runner」与「env > vars」优先级链的明文声明。
            用户会误以为是自己 YAML 写错，反复排查。
预期系统行为: 文档声明与平台行为必须一致：job env 在 shell 中可读；
            若平台实际语义是「job env 仅表达式层可见」，文档必须改写法并给出迁移示例（`run: echo ${{ env.X }}`
            或 `env: {X: ${{ env.X }}}` 在 step 层显式声明）。
Oracle 来源: GitCode 规格（configure-jobs.md / using-script-commands.md）vs 实际行为（TC-533 实证）

验证要点:
  - [正向] 提交 job 级 env，分别在 step 的 `run:` 用 `$VAR` 与 `${{ env.VAR }}` 读取，断言两者是否一致
  - [负向] 文档「对该 job 内所有 step 可见」的表述不应与「shell 中读不到」并存
  - [非功能] 平台行为修复前，文档应显式 workaround

可理解性判据: 文档承诺与平台行为一致；不一致即不合格。
            eval: 否（实际跑一遍即可判定）。

关联兼容性差异: 无（但与 COMPAT 维度的 env 注入测试联动）
优先级线索: RISK-USE-01 → P0
            理由：文档明确承诺的能力未兑现，属「文档说谎」级别；新手与迁移者都会踩；
            quality-gate 易用性「核心迁移路径可跑」直接命中。
破坏级别:   none
来源输入:   gitcode-spec/writing-pipelines/configure-jobs.md;
            gitcode-spec/writing-pipelines/using-script-commands.md;
            inputs/existing-cases/cases.md 问题 sheet（TC-533）
```

```
意图 ID:    INTENT-USE-047
维度标签:   [usability, reliability]
标题:       schedule 不触发时无任何可观测提示

场景:       用户配置 cron 后等了一夜没跑；不知道是 cron 写错、时区算错、不在默认分支、
            间隔 < 5min 被吞、还是平台调度器故障。
用户视角:   所有用 schedule 的用户。
风险点:     问题 sheet S3×24 + TC-391 实证：两个仓库多次 cron 配置从未产生 Schedule Run；
            平台 UI 对「schedule 为什么没触发」没有任何提示、没有「下次预计触发时间」、
            没有「已跳过的触发记录」。用户只能在文档与平台之间反复盲猜。
预期系统行为: workflow 列表或详情页应展示 schedule 工作流的「下次预计触发时间」；
            每次被跳过的触发（非默认分支 / 间隔 < 5min / cron 非法）应在运行列表中留一条「skipped」记录并附原因。
Oracle 来源: 迁移者合理预期（GitHub Actions 会在 workflow 列表显示 cron 状态）；testing-focus §9 可观测性

验证要点:
  - [负向] schedule 未触发时，平台不应完全静默
  - [非功能] workflow 列表应显示「下次预计触发时间」字段
  - [非功能] 跳过的触发应有原因记录（非默认分支 / 间隔过短 / cron 非法 / 平台故障）

可理解性判据: 在 UI 上，用户能在不查文档的情况下区分「cron 写错」与「平台故障」两类原因。
            eval: 是（「能否区分」需主观评判 UI 信息呈现）。

关联兼容性差异: parity-matrix「schedule cron 最短间隔」🟡
优先级线索: RISK-USE-01 → P1
            理由：可靠性维度（REL）会验证调度器本身；易用性维度验证「不触发时的可观测性」。
破坏级别:   none
来源输入:   gitcode-spec/writing-pipelines/configure-triggers.md;
            inputs/existing-cases/cases.md 问题 sheet（S3×24 + TC-391）
```

```
意图 ID:    INTENT-USE-048
维度标签:   [usability, compatibility]
标题:       API 字段命名与事件类型命名不一致 — opened vs open

场景:       用户在 workflow 里写 `types: [open]`，在 API 返回值里看到 `opened`；
            用户写脚本消费 API 时用事件名匹配，结果永远不命中。
用户视角:   用 API 做二次开发 / 状态检查的用户。
风险点:     问题 sheet TC-064 实证：API 返回 PR 状态为 `opened`，而 GitCode 事件类型命名是 `open`；
            同一概念在两处命名不一致，用户需要记忆两套词汇。
预期系统行为: 同一概念的命名应在事件、API、文档三处一致；若 API 沿用 GitHub 风格（opened）
            而事件命名独立演进（open），文档应在「触发事件」与「API 参考」两处分别给出对照表。
Oracle 来源: GitCode 规格（syntax-reference/trigger-events.md）+ 实际 API 行为（TC-064 实证）

验证要点:
  - [负向] 事件类型与 API 字段命名不应在同一概念上分裂
  - [非功能] 若已分裂，文档应在两处互相引用对照

可理解性判据: 对事件类型集合与 API 字段值集合做 diff；同概念不同名即不合格（除非文档明示对照）。
            eval: 否。

关联兼容性差异: parity-matrix「pull_request types 命名」
优先级线索: RISK-USE-01 → P2
破坏级别:   none
来源输入:   gitcode-spec/syntax-reference/trigger-events.md;
            inputs/existing-cases/cases.md 问题 sheet（TC-064）
```

### D 组：实操 / 新手路径（business-context §4 维度 1+2 落地）

```
意图 ID:    INTENT-USE-049
维度标签:   [usability]
标题:       rerun 上限（3 次 / 超 6h）在 UI 的明示

场景:       用户第 4 次点击 Re-run 按钮，发现按钮置灰或点了没反应；文档（rerun-failed-jobs.md）
            写了限制但 UI 未在置灰时提示原因。
用户视角:   调试偶发失败的中级用户。
风险点:     rerun-failed-jobs.md 声明「最多重新运行 3 次」「超过 6 小时的运行不可重新运行」；
            若 UI 只把按钮置灰而不在 tooltip / 帮助文本中说明原因，用户会以为是平台 bug。
预期系统行为: 当 Re-run 不可用时，按钮应有 tooltip 明示原因（已达上限 / 超过 6h 时限）；
            运行详情页应显示「已重跑次数 / 剩余次数」。
Oracle 来源: GitCode 规格（running-pipelines/rerun-failed-jobs.md）+ 通用 UI 可用性启发

验证要点:
  - [正向] 重跑 3 次后按钮置灰，悬停提示「已达最大重跑次数 3」
  - [正向] 超过 6h 的运行，按钮置灰，悬停提示「超过 6 小时不可重新运行」
  - [非功能] 运行详情页应显示当前已重跑次数

可理解性判据: 用户在不查文档的情况下，通过 UI 自身即可理解「为什么不能重跑」。
            eval: 是（tooltip 是否清晰需主观评判）。

关联兼容性差异: parity-matrix「rerun 次数限制」🟡
优先级线索: RISK-COMPAT-01 → P1
破坏级别:   none
来源输入:   gitcode-spec/running-pipelines/rerun-failed-jobs.md
```

```
意图 ID:    INTENT-USE-050
维度标签:   [usability]
标题:       新手快速开始路径端到端可复刻 — 从开通到看到第一个 ✅

场景:       完全新手按 00-overview → 01-quick-start 顺序操作，应能在 30 分钟内看到第一个成功的
            workflow 运行。每一步都可能卡壳：找不到开通入口、不知道仓库要有内容、
            不知道 push 之后去哪看结果。
用户视角:   完全新手（business-context §4 维度 2「实操易用性」直接命中）。
风险点:     quick-start 列出 3 条前提（账号 / 仓库 / YAML 基础），但未说「仓库如何开通 Action 功能」
            （workflow-file-location-structure.md 前提里提到「AtomGit Action 功能已开启」但未给开启步骤）；
            「提交触发」一节只给 git 命令，未说 push 后多久能看到运行、去哪看；
            「成功结果验证」一节用 ✅ 图标描述成功，但未说「如果没看到 First Pipeline 条目怎么办」。
预期系统行为: 新手路径每一步都应有「如何验证这一步做对了」的检查点；
            每个可能的卡壳点（未开通 / 目录错 / 分支错）应在文档中给出排查锚点。
Oracle 来源: 文档自承诺 + business-context §4「步骤可直接复刻 / 报错解决方案有效」

验证要点:
  - [正向] 按 quick-start 逐步操作，每步有可观察验证点
  - [负向] 不应存在「文档假设用户知道但新手不知道」的隐式前提（如开通步骤）
  - [非功能] 全流程 ≤ 30 分钟可完成

可理解性判据: 由无 GitCode 经验的评测者（或 LLM 模拟新手）按文档操作，记录每个卡壳点；
            卡壳点数量应为 0。eval: 是（需主观/LLM 评判「新手是否会卡」）。

关联兼容性差异: 无
优先级线索: RISK-USE-01 → P0
            理由：onboarding 是 business-context §4 维度 2 的核心；quality-gate 易用性「核心迁移路径可跑」直接命中。
破坏级别:   none
来源输入:   gitcode-spec/00-overview.md; gitcode-spec/01-quick-start.md;
            gitcode-spec/writing-pipelines/workflow-file-location-structure.md;
            inputs/business-context/README.md §4
```

```
意图 ID:    INTENT-USE-051
维度标签:   [usability]
标题:       workflow_dispatch 手动触发 UI 与 YAML inputs 定义的一致性

场景:       用户在 YAML 定义了 5 个 inputs（含 description / required / default），
            点击「手动触发」按钮后，UI 表单应忠实呈现这 5 个字段。
            若 UI 少字段、类型错（string 全渲染成 text 无下拉）、必填未标星、默认值未填，
            用户会填错参数。
用户视角:   用 workflow_dispatch 做发布 / 热修的用户（cann / testorg 真实场景）。
风险点:     真实样本 testorg/full_pr.yaml 定义了 12 个 inputs、含 `manual_override` 语义，
            平台 UI 是否理解这些字段、是否把 `manual_override: false` 的字段锁死，文档完全未提。
预期系统行为: 手动触发 UI 应逐一渲染 YAML 定义的 inputs：字段名、description 作 label / 提示、
            required 标红星、default 预填；`manual_override: false` 字段应锁死为只读。
Oracle 来源: 文档（configure-triggers.md workflow_dispatch 一节）+ 真实样本（testorg/full_pr.yaml）

验证要点:
  - [正向] YAML 定义 5 个 inputs，UI 渲染 5 个对应控件
  - [负向] UI 不应渲染 YAML 未定义的字段；不应漏渲染已定义字段
  - [非功能] required / default / description 在 UI 均有对应呈现

可理解性判据: 对比 YAML inputs 集合与 UI 渲染字段集合；集合不一致即不合格。
            eval: 否（UI 扫描 + 集合 diff 可判定）。

关联兼容性差异: parity-matrix「workflow_dispatch.inputs 类型」🟡
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   gitcode-spec/writing-pipelines/configure-triggers.md;
            workflow-samples/testorg/full_pr.yaml
```

### E 组：Action 生态（基于新输入 actions-market.md）

```
意图 ID:    INTENT-USE-052
维度标签:   [usability]
标题:       官方短名 Action 清单与 actions-market 49 插件目录的一致性

场景:       用户看 using-actions.md 学到「官方插件直接用短名 `checkout` / `setup-node`」，
            但文档列的短名只有寥寥几个；新输入 actions-market.md 收录 49 个插件，
            其中很多名字（如 `AtomgitCache` / `BuildCache` / `Cache` / `UploadArtifact` / `DownloadArtifact`）
            与文档提到的短名（`cache` / `upload-artifact` / `download-artifact`）在大小写 / 连字符上不一致。
用户视角:   想用官方 Action 的中级用户。
风险点:     文档（using-actions.md / COMPAT-NOTES §10）说官方 Action 用「无 owner 短名」；
            但市场目录里的官方插件名带大小写（`AtomgitCache`）与文档示例（`cache`）不一致；
            用户不知道 `uses: cache` 与 `uses: AtomgitCache` 是否同物、哪种是推荐写法；
            也缺乏「这 49 个插件里哪些是官方维护 / 哪些是社区贡献」的标识。
预期系统行为: 文档应给出「官方短名 ⇄ 市场插件名」的完整对照表；
            市场对官方维护插件应有明显标识；大小写 / 连字符不敏感规则应明示。
Oracle 来源: GitCode 规格（using-actions.md）vs actions-market.md 实际目录

验证要点:
  - [正向] 用文档短名 `cache` 与市场名 `AtomgitCache` 分别提交，验证是否解析到同一插件
  - [负向] 文档与市场不应让用户对「同一插件的两个名字」感到困惑
  - [非功能] 市场页应标识「官方 / 社区」维护者属性

可理解性判据: 文档短名集合与市场目录插件名集合建立映射；映射关系文档未明示即不合格。
            eval: 否（集合比对可判定）。

关联兼容性差异: COMPAT-NOTES §10；parity-matrix「内置 action 差异」
优先级线索: RISK-USE-01 → P1
破坏级别:   none
来源输入:   gitcode-spec/writing-pipelines/using-actions.md;
            gitcode-spec/actions-market.md;
            COMPAT-NOTES.md §10
```

```
意图 ID:    INTENT-USE-053
维度标签:   [usability, security]
标题:       隐藏开关（如 ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS）默认值与文档缺失

场景:       平台存在影响安全行为的隐藏开关，文档未列出；用户在禁用废弃命令、调试老 workflow 时
            不知道该开关存在、默认值是什么、如何打开。
用户视角:   维护历史 workflow 的高级用户 / 平台管理员。
风险点:     问题 sheet TC-220 实证：`ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS` 默认值缺失；
            该开关控制「废弃的 ::set-output 等命令是否仍被接受」，直接影响 INTENT-USE-010 的判定；
            文档（workflow-commands.md / using-script-commands.md）只写「已废弃」，未写「可通过此开关临时放行」。
预期系统行为: 所有影响平台行为的开关（尤其安全相关）应在语法参考页集中列出：名称、默认值、
            取值范围、开启后的安全影响；安全相关开关的默认值应显式标注。
Oracle 来源: 问题 sheet 实证 + 通用「安全默认值应文档化」原则

验证要点:
  - [负向] 平台不应存在影响安全行为但文档未提的开关
  - [非功能] 开关清单页应标注每个开关的安全影响与默认值

可理解性判据: 通过实际问题 / 源码 / 平台行为收集到的开关集合，应 ⊆ 文档开关清单；每缺 1 个即一条缺陷。
            eval: 否。

关联兼容性差异: COMPAT-NOTES §11
优先级线索: RISK-SEC-01 → P1
破坏级别:   none
来源输入:   gitcode-spec/syntax-reference/workflow-commands.md;
            gitcode-spec/writing-pipelines/using-script-commands.md;
            inputs/existing-cases/cases.md 问题 sheet（TC-220）
```

---

## 3. 统计摘要

### 3.1 总量

| 类别 | 数量 |
|---|---|
| 沿用（来自 2026-07-23-01） | 29（INTENT-USE-001 ~ 028 + 030） |
| 新增（本轮） | 23（INTENT-USE-031 ~ 053） |
| **合计** | **52** |

### 3.2 按优先级分布（沿用 + 新增合并）

| 优先级 | 数量 | 涉及 Intent ID |
|---|---|---|
| **P0** | 6 | USE-016（沿用，secret 脱敏）；USE-031 / USE-032 / USE-033（文档自相矛盾 / 示例不可复刻）；USE-046（job env 未注入，文档说谎）；USE-050（新手 onboarding 路径） |
| **P1** | 40 | 沿用 27（USE-001 ~ 015、017 ~ 028、030）；新增 13（USE-035 ~ 038、040 ~ 045、047、049、051、052、053） |
| **P2** | 6 | USE-034（章节编号）；USE-039（default() 未文档化）；USE-048（opened vs open 命名）；以及沿用中的 USE-016 之外的少数（沿用全部为 P0/P1，无 P2 沿用） |

> 备注：上一轮沿用条目按 risk-register 对齐全部为 P0/P1，故 P2 完全由本轮新增的低优先级文档质量条目构成。

### 3.3 按主题分布（新增 23 条）

| 主题组 | 数量 | Intent ID |
|---|---|---|
| A. 文档自相矛盾 | 5 | USE-031 / 032 / 033 / 034 / 035 |
| B. 真实样本在用但文档未写 | 5 | USE-036 / 037 / 038 / 039 / 040 |
| C. 文档承诺 vs 实际能力 | 8 | USE-041 / 042 / 043 / 044 / 045 / 046 / 047 / 048 |
| D. 实操 / 新手路径 | 3 | USE-049 / 050 / 051 |
| E. Action 生态 | 2 | USE-052 / 053 |

### 3.4 需 llm_assisted 评判的条目

| Intent ID | 需主观评判的点 |
|---|---|
| USE-047 | 「用户能否在 UI 上区分 cron 写错 vs 平台故障」 |
| USE-049 | 「rerun 按钮置灰时的 tooltip 是否足以解释原因」 |
| USE-050 | 「新手在 onboarding 全流程中实际卡壳点数量」（可借助 LLM 模拟新手） |

新增 23 条中 3 条需 llm_assisted；其余 20 条均可通过集合 diff / 字符串匹配 / 实跑对照做确定性判定。

### 3.5 跨维度分布（新增 23 条）

- 纯 `[usability]`：14（USE-031 ~ 035、039、043、045、049、050、051、052、034 重复计数已剔除——实见上表）
- `[usability, compatibility]`：7（USE-036 / 037 / 038 / 040 / 041 / 042 / 044 / 046 / 048 中实际打 compat 标签的 7 条）
- `[usability, reliability]`：1（USE-047）
- `[usability, security]`：1（USE-053）

---

## 4. 与其他维度的边界声明

- **不与 compat-diff 重复**：compat 维度关注「行为是否与 GitHub 一致」；本文件新增条目关注的是「文档自身的一致性 / 文档与真实样本的一致性 / 文档承诺与平台行为的一致性」，assertion 目标都是文档与可观测 UI，不是行为等价。
- **不与 reliability 重复**：USE-047 仅验证「schedule 不触发时的可观测提示」，调度器本身的正确性由 REL 维度覆盖。
- **不与 security 重复**：USE-053 仅验证「安全开关是否文档化」，开关的实际防护强度由 SEC 维度覆盖。
- **与 spec / completeness 协同**：USE-031 / 032 / 037 / 040 / 042 / 046 同时给 spec 维度提供「平台实际支持什么」的实证输入；spec 维度确认行为后，本维度的「文档-行为一致性」判定才有最终 oracle。

---

## 5. 风险登记册对齐自查

| 风险 ID | 覆盖 Intent（沿用 + 新增） | 是否充分 |
|---|---|---|
| RISK-USE-01（迁移报错不指明 GitCode 差异） | 沿用 USE-001 ~ 010、022 ~ 025、028、030；新增 USE-031 / 032 / 033 / 035 / 036 / 037 / 038 / 040 / 042 / 043 / 044 / 045 / 046 / 048 / 050 / 051 / 052 | ✅ 充分 |
| RISK-COMPAT-01（默认值差异致行为静默不同） | 沿用 USE-011 ~ 015、017 ~ 021、026、027；新增 USE-034 / 041 / 049 | ✅ 充分 |
| RISK-SEC-01（fork PR secret 泄露，易用性视角） | 沿用 USE-016、028；新增 USE-053 | ✅ 充分（主覆盖在 SEC 维度） |
| RISK-REL-01（并发洪泛） | 不直接覆盖（由 REL 维度负责） | N/A |
| RISK-SEC-02（不可信输入注入） | 不直接覆盖（由 SEC 维度负责） | N/A |

所有新增 intent 均能反查到至少一条风险登记册条目；无「无法对齐」的孤立 intent。

---

## 6. 门禁对齐

按 `baseline/quality-gate.md` 易用性维度门禁「P0/P1 错误信息类用例达标；核心迁移路径可跑」：

- 本轮 P0 共 6 条，其中 USE-016（沿用）+ USE-031 / 032 / 033 / 046 / 050（新增）共同构成「核心迁移路径可跑 + 文档可信」的最小集合——这 6 条任一失败即建议判易用性维度不通过。
- P1 40 条构成「迁移摩擦可达底」的完整覆盖网。

---

## 7. 变更留痕

| 时间 | 操作 | 说明 |
|---|---|---|
| 2026-07-27 | 新建 | Run 2026-07-27-01 usability 维度 intents 首次产出；沿用 29 + 新增 23 = 52 条 |
