# Intent Library（汇总意图库）

> Run: 2026-07-27-01
> 评审角色: orchestrator + review-gate（串行）
> 评审日期: 2026-07-27
> 意图总数: 282 条（沿用上轮已准入 198 + 本轮新增 84，含 STOP① 增补 COMPAT-054）
> 准入: 282 条 | 打回: 0 条 | STOP① 用户裁决（2026-07-27）已落实: REL-069 升 P0（登记册增补 RISK-REL-02）、USE-031/032/033/046/050 恢复 P0（登记册增补 RISK-USE-02）、19 条 P2 降档接受、COMPAT-054 增补闭环盲区 B1
> 过程记录: 见 `gate-log.md`

---

## 统计摘要

| 维度 | 沿用（上轮已准入） | 本轮新增 | 合计准入 | P0 | P1 | P2 | 打回 |
|---|---|---|---|---|---|---|---|
| completeness | 18 | 15 | 33 | 6 | 21 | 6 | 0 |
| compatibility | 47（035 系列 35 + NEW 系列 12） | 19（含 STOP① 增补 054） | 66 | 7 | 55 | 4 | 0 |
| security | 36 | 10 | 46 | 35 | 10 | 1 | 0 |
| reliability | 68 | 17 | 85 | 1 | 76 | 8 | 0 |
| usability | 29 | 23 | 52 | 6 | 43 | 3 | 0 |
| **合计** | **198** | **84** | **282** | **55** | **205** | **22** | **0** |

> 注 1：REL-069 P0 已经 STOP① 用户裁决确认（2026-07-27），risk-register.md 已增补 blocker 项 RISK-REL-02（matrix×needs 聚合判定无声失败，依据 #101 ★）。
> 注 2：USE-031/032/033/046/050 门禁初审降为 P1，STOP① 用户裁决增补 RISK-USE-02（文档承诺未兑现/核心迁移路径文档错误，blocker）后**恢复 P0**。
> 注 3：本轮 agent 自评降档 P2 共 19 条（COMPAT-049~052、COMP-022/024/026/027/031/032、SEC-045、REL-075~079、USE-034/039/048），门禁复核接受，STOP① 用户确认无异议。
> 注 4：COMPAT-054（Runner OS 多样性）为 STOP① 用户裁决增补，闭环盲区 B1，准入 P1。

### 分维度 P0 覆盖检查（rules.md §11）

| 维度 | P0 条数 | 结论 |
|---|---|---|
| completeness | 6（COMP-004/011/012/013/014/016） | ✅ |
| compatibility | 7（COMPAT-002/025/028/030/032/033 + NEW-002） | ✅ |
| security | 35 | ✅ 非空且为主力 |
| reliability | 1（REL-069，STOP① 确认 + RISK-REL-02） | ✅ |
| usability | 6（USE-016 + USE-031/032/033/046/050，STOP① 确认 + RISK-USE-02） | ✅ |

---

## 准入意图清单

### 维度：completeness（33 条）

#### 沿用（18 条，2026-07-23-01 已准入，本轮不重复展开）

| 意图 ID | 标题 | 优先级 | 覆盖风险/能力项 | 去重关系 | 已有覆盖 |
|---|---|---|---|---|---|
| INTENT-COMP-001 | 工作流目录 `.gitcode/workflows/` 识别 | P1 | RISK-COMPAT-01 / 目录识别 | 沿用 | TC-366, TC-383 |
| INTENT-COMP-002 | 未知/不支持字段的 YAML 校验行为 | P1 | RISK-COMPAT-01 / 未知字段降级 | 沿用 | TC-274, TC-336 |
| INTENT-COMP-003 | push 触发 + branches/paths/tags 过滤 | P1 | RISK-REL-01 / 触发器核心 | 沿用 | TC-223, TC-229~233 |
| INTENT-COMP-004 | pull_request vs pull_request_target 隔离强度 | P0 | RISK-SEC-01 / 安全命脉 | 沿用 | TC-445, TC-461~463 |
| INTENT-COMP-005 | schedule cron 语义（5 分钟/UTC/默认分支） | P1 | RISK-COMPAT-01 / 定时触发 | 沿用 | TC-427~430 |
| INTENT-COMP-006 | workflow_call 嵌套层数（≤2 层） | P1 | RISK-REL-01 / 可重用工作流 | 沿用 | TC-426, TC-564 |
| INTENT-COMP-007 | stages 阶段机制与 post 后处理阶段语义 | P1 | RISK-REL-01 / 执行模型 | 沿用 | TC-402~404, 406~407 |
| INTENT-COMP-008 | timeout-minutes 默认 360 与强制终止 | P1 | RISK-REL-01 / 超时机制 | 沿用 | TC-270 |
| INTENT-COMP-009 | rerun 次数限制与上下文保持 | P1 | RISK-REL-01 / 可观测性 | 沿用 | TC-350 |
| INTENT-COMP-010 | runs-on 三段式标签体系与 default 标签 | P1 | RISK-COMPAT-01 / Runner 基础 | 沿用 | TC-363/365, TC-446~457 |
| INTENT-COMP-011 | Runner 环境隔离强度（ephemeral） | P0 | RISK-SEC-01 / 安全与稳定性 | 沿用 | — |
| INTENT-COMP-012 | secrets 日志脱敏与绕过场景 | P0 | RISK-SEC-01 / 安全命脉 | 沿用 | TC-011, TC-354 |
| INTENT-COMP-013 | permissions 默认权限与声明语义 | P0 | RISK-SEC-01 / 安全命脉 | 沿用 | TC-351~416 |
| INTENT-COMP-014 | pull_request_target checkout head.sha 注入风险 | P0 | RISK-SEC-01 / 安全命脉 | 沿用 | TC-461~463 |
| INTENT-COMP-015 | artifact 跨 job 传递与保留期 | P1 | RISK-REL-01 / Artifact 基础 | 沿用 | TC-294~300, 378~380 |
| INTENT-COMP-016 | cache 作用域与 fork 隔离策略 | P0 | RISK-SEC-01 / 安全与稳定性 | 沿用 | TC-301~303 |
| INTENT-COMP-017 | 运行状态机与日志完整性 | P1 | RISK-USE-01 / 可观测性 | 沿用 | TC-347, TC-348 |
| INTENT-COMP-018 | ATOMGIT_STEP_SUMMARY Markdown 渲染 | P1 | RISK-USE-01 / 可观测性 | 沿用 | TC-219, TC-246, TC-497 |

#### 本轮新增（15 条，门禁全部准入）

| 意图 ID | 标题 | 优先级（裁决） | 覆盖风险/能力项 | 去重关系 | 已有覆盖 | 门禁结论 |
|---|---|---|---|---|---|---|
| INTENT-COMP-019 | 裁定 stages 两种文档语法形式（map vs list） | P1 | RISK-COMPAT-01 / stages ❌项 | 关联 USE-032（同主题：本条=平台行为裁定，USE-032=文档一致性） | — | 准入 |
| INTENT-COMP-020 | 裁定 inputs 上下文非 dispatch 触发可用性（三方文档矛盾） | P1 | RISK-COMPAT-01 / inputs 上下文 | 关联 COMP-031、USE-051（inputs 主题簇） | — | 准入 |
| INTENT-COMP-021 | 未文档化字段 select/selected_by_default 语义与默认值 | P1 | RISK-COMPAT-01 / 未知字段 ❓ | 关联 USE-037（本条=行为，USE-037=文档缺失面） | — | 准入 |
| INTENT-COMP-022 | 未文档化函数 default() 存在性与语义 | P2（自评，门禁接受） | RISK-COMPAT-01 / 表达式函数 ❓ | 关联 USE-039、COMPAT-021 | — | 准入 |
| INTENT-COMP-023 | 裁定「Fork 推荐 pull_request_target」与安全警示文档冲突 | P1 | RISK-SEC-01（邻接）/ 文档安全导向 | 关联 SEC-002/035、COMP-004/014（pull_request_target 簇） | — | 准入 |
| INTENT-COMP-024 | 触发事件别名 pr_comment 有效性与等价性 | P2（自评，门禁接受） | RISK-COMPAT-01 / 触发事件 | 关联 USE-036（命名双轨）、COMPAT-037 | — | 准入 |
| INTENT-COMP-025 | container.volumes 宿主挂载与 options 在托管 Runner 的边界 | P1 | RISK-SEC-01（邻接）/ Runner 隔离 ❓ | 关联 SEC-020~023（隔离边界簇，深测由 SEC 承接） | — | 准入 |
| INTENT-COMP-026 | action.yml inputs.required:true 不自动校验的声明行为 | P2（自评，门禁接受） | RISK-COMPAT-01 / action 元数据 | 独立 | — | 准入 |
| INTENT-COMP-027 | INPUT_<NAME> 环境变量命名契约边界（连字符转换） | P2（自评，门禁接受） | RISK-COMPAT-01 / action 输入注入 | 关联 SEC-024/041（命名面） | TC-531（相邻） | 准入 |
| INTENT-COMP-028 | action 级 runs.post 两种触发机制（取消时调度调用） | P1 | RISK-REL-01 / 取消语义（GAP-008 衍生） | 关联 REL-028/061、REL-083 | — | 准入 |
| INTENT-COMP-029 | 裁定 runs-on 三种并存形式（三段/四段/flow-mapping） | P1 | RISK-COMPAT-01 / runs-on 🟡 | runs-on 主题簇：关联 COMPAT-046、USE-031、USE-040 | TC-363/365 等 | 准入 |
| INTENT-COMP-030 | workflow_call 本地路径调用与 secrets required 契约 | P1 | RISK-SEC-01（邻接）/ workflow_call | 独立（安全深测面由 SEC 维度承接） | — | 准入 |
| INTENT-COMP-031 | workflow 顶层 inputs 与 manual_override（未文档化）处理 | P2（自评，门禁接受） | RISK-COMPAT-01 / inputs | 关联 COMP-020、USE-037、USE-051 | — | 准入 |
| INTENT-COMP-032 | ${gitcode_*} / ${PIPELINE_*} 非标准插值求值行为 | P2（自评，门禁接受） | RISK-COMPAT-01 / 插值语法 | 关联 USE-038 | — | 准入 |
| INTENT-COMP-033 | pre-merge ref（refs/merge-requests/N/merge）存在性与语义 | P1 | RISK-COMPAT-01 / PR 代码版本语义 | 关联 COMPAT-039（同主题两面，展开时共享 PR 夹具与证据链） | — | 准入 |

### 维度：compatibility（65 条）

#### 沿用（47 条 = 主系列 35 + NEW 回填 12，2026-07-23-01 已准入）

| 意图 ID | 标题 | 优先级 | 去重关系 | 已有覆盖 |
|---|---|---|---|---|
| INTENT-COMPAT-001 | 默认 shell 与默认工作目录隐式行为差异 | P1 | 沿用 | TC-288 |
| INTENT-COMPAT-002 | 未声明 permissions 默认 TOKEN 权限差异 | P0 | 沿用 | TC-351~416 |
| INTENT-COMPAT-003 | if 未声明时默认状态检查差异 | P1 | 沿用 | TC-176~179 |
| INTENT-COMPAT-004 | 状态函数括号语法差异 success() vs success | P1 | 沿用 | TC-176~179, 317~321 |
| INTENT-COMPAT-005 | 失败状态函数命名差异 failure() vs failed | P1 | 沿用（变体自 004） | TC-178, TC-320 |
| INTENT-COMPAT-006 | contains 函数边界行为差异 | P1 | 沿用 | TC-180, TC-543~544 |
| INTENT-COMPAT-007 | hashFiles 函数边界行为差异 | P1 | 沿用 | TC-186, TC-550 |
| INTENT-COMPAT-008 | toJson 输出格式差异 | P1 | 沿用 | TC-187, TC-549 |
| INTENT-COMPAT-009 | 表达式 loose equality 与类型强转差异 | P1 | 沿用 | TC-160~175 |
| INTENT-COMPAT-010 | 缺失函数 join/fromJSON/case 降级行为 | P1 | 沿用 | — |
| INTENT-COMPAT-011 | pull_request types 命名与取值差异 | P1 | 沿用 | TC-234, TC-560 |
| INTENT-COMPAT-012 | paths 上限差异 GitHub 3000 vs GitCode 300 | P1 | 沿用 | TC-422, TC-514~515 |
| INTENT-COMPAT-013 | schedule timezone 差异 IANA vs UTC | P1 | 沿用 | TC-427~430 |
| INTENT-COMPAT-014 | dispatch/call inputs 仅支持 string | P1 | 沿用 | TC-014, TC-193, TC-581 |
| INTENT-COMPAT-015 | workflow_call 嵌套 2 层差异 | P1 | 沿用 | TC-426, TC-564 |
| INTENT-COMPAT-016 | 上下文前缀 github.* vs atomgit.* | P1 | 沿用 | TC-017~018 |
| INTENT-COMPAT-017 | 环境变量前缀 GITHUB_* vs ATOMGIT_* | P1 | 沿用 | TC-197~218 |
| INTENT-COMPAT-018 | runner.os 值格式差异 Linux vs linux | P1 | 沿用 | TC-023/094, 136~139 |
| INTENT-COMPAT-019 | runner.arch 值格式差异 X64 vs x86_64 | P1 | 沿用 | TC-095, TC-442 |
| INTENT-COMPAT-020 | 自动令牌命名 GITHUB_TOKEN vs ATOMGIT_TOKEN | P1 | 沿用 | TC-036, TC-196 |
| INTENT-COMPAT-021 | 未知/不支持字段降级方式 | P1 | 沿用（关联 COMP-002） | TC-274, TC-336 |
| INTENT-COMPAT-022 | vars 上下文不支持时降级行为 | P1 | 沿用 | TC-019, TC-115~119 |
| INTENT-COMPAT-023 | jobs.<id>.environment 支持与降级 | P1 | 沿用 | TC-010, TC-274 |
| INTENT-COMPAT-024 | 内置 action 短名引用等价性 | P1 | 沿用 | TC-304, TC-354 |
| INTENT-COMPAT-025 | 内置 cache 行为等价性与 fork 隔离 | P0 | 沿用（关联 SEC-018） | TC-301~303 |
| INTENT-COMPAT-026 | 内置 upload/download-artifact 等价性 | P1 | 沿用（关联 COMP-015） | TC-294~300 |
| INTENT-COMPAT-027 | runs-on 标签体系差异 | P1 | 沿用（关联 COMP-010） | TC-363/365, 571~573 |
| INTENT-COMPAT-028 | Runner 环境隔离与复用策略未明 | P0 | 沿用（关联 SEC-020） | — |
| INTENT-COMPAT-029 | 工作流目录差异 | P1 | 沿用（关联 COMP-001） | TC-366, TC-383 |
| INTENT-COMPAT-030 | permissions 权限域命名完全差异 | P0 | 沿用（关联 USE-005） | TC-351~416 |
| INTENT-COMPAT-031 | 迁移报错质量（是否指明 GitCode 差异） | P1 | 沿用 | — |
| INTENT-COMPAT-032 | pull_request_target 语义一致性 | P0 | 沿用（关联 SEC-035） | TC-461~463 |
| INTENT-COMPAT-033 | Secret 日志脱敏绕过风险 | P0 | 沿用（关联 SEC-004~008） | TC-011 |
| INTENT-COMPAT-034 | concurrency 字段结构与语义差异 | P1 | 沿用（关联 REL-001~006） | TC-289~293, 518~523 |
| INTENT-COMPAT-035 | steps 上下文 outcome/conclusion 语义差异 | P1 | 沿用 | TC-090~092 |
| INTENT-COMPAT-NEW-001 | container 字段不支持时报错质量与替代指引 | P1 | 沿用（回填） | — |
| INTENT-COMPAT-NEW-002 | 环境级 secrets 不支持不应静默降级 | P0 | 沿用（回填） | — |
| INTENT-COMPAT-NEW-003 | pull_request types/paths/branches 过滤不触发差异 | P1 | 沿用（回填） | — |
| INTENT-COMPAT-NEW-004 | issue_comment types 命名差异与降级指引 | P1 | 沿用（回填） | — |
| INTENT-COMPAT-NEW-005 | concurrency.preemption 配置差异 | P1 | 沿用（回填，关联 REL-001~006） | — |
| INTENT-COMPAT-NEW-006 | 跨 Job 引用未声明 output 返回值差异 | P1 | 沿用（回填）；本轮裁决：**变体/子集于 COMPAT-041**，展开时并入 041 证据链 | — |
| INTENT-COMPAT-NEW-007 | strategy.matrix 高级用法差异 | P1 | 沿用（回填） | — |
| INTENT-COMPAT-NEW-008 | runs-on 不支持标签报错与排队行为 | P1 | 沿用（回填） | — |
| INTENT-COMPAT-NEW-009 | workflow 命令 add-mask/group/stop-commands 静默降级 | P1 | 沿用（回填） | — |
| INTENT-COMPAT-NEW-010 | action.yml 元数据校验差异（branding 等） | P1 | 沿用（回填） | — |
| INTENT-COMPAT-NEW-011 | Runner 未预装 Java 工具链差异 | P1 | 沿用（回填）；本轮裁决：**变体/子集于 COMPAT-047** | — |
| INTENT-COMPAT-NEW-012 | 废弃命令 set-env/add-path 拒绝或迁移指引 | P1 | 沿用（回填） | — |

#### 本轮新增（19 条，门禁全部准入；054 为 STOP① 用户裁决增补）

| 意图 ID | 标题 | 优先级（裁决） | 覆盖风险/能力项 | 去重关系 | 已有覆盖 | 门禁结论 |
|---|---|---|---|---|---|---|
| INTENT-COMPAT-036 | startsWith/endsWith 大小写敏感性两侧文档直接矛盾 | P1 | RISK-COMPAT-01 / 表达式函数 ❓ | 关联 COMPAT-006（互补：006=文档未明，本条=直接矛盾） | — | 准入 |
| INTENT-COMPAT-037 | GitHub 全量事件集在 GitCode 的降级方式（事件本身不存在） | P1 | RISK-USE-01 / 触发事件 | 关联 011/NEW-004（父集：事件不存在 > types 差异）；关联 SEC-044（workflow_run 面） | — | 准入 |
| INTENT-COMPAT-038 | pull_request 扩展 activity types 降级（labeled 等 20+ 种） | P1 | RISK-COMPAT-01+RISK-USE-01 / 触发过滤 | 关联 011（互补不重叠，裁决认可 agent 标注） | — | 准入 |
| INTENT-COMPAT-039 | pull_request 的 ref/sha/workflow 来源语义（merge commit 模型） | P1 | RISK-COMPAT-01 / PR 代码版本语义 | 关联 032（正交）；关联 COMP-033（同主题两面，共享夹具） | — | 准入 |
| INTENT-COMPAT-040 | atomgit 字段级差距：actor 规格矛盾 + 字段缺位 | P1 | RISK-COMPAT-01 / 上下文对象 ❌ | 关联 016/017（互补：字段级差距） | — | 准入 |
| INTENT-COMPAT-041 | needs 上下文存在性与字段完备性（规格自相矛盾） | P1 | RISK-COMPAT-01 / needs 上下文 | **父集于 NEW-006**（裁决确认 agent 标注）；关联 REL-069（matrix 聚合面） | — | 准入 |
| INTENT-COMPAT-042 | 注解命令 ::error/::warning/::notice/::debug 支持度与 debug 门控 | P1 | RISK-COMPAT-01 / workflow 命令 | 关联 NEW-009（互补成完整命令面）；关联 USE-021（注解可读性） | TC-247~250、TC-099（FAIL） | 准入 |
| INTENT-COMPAT-043 | ATOMGIT_ENV 是否禁止覆写系统默认变量 | P1 | RISK-COMPAT-01（SEC-02 邻接）/ 写协议 | 关联 017（「有没有」vs「能不能覆写」）；关联 SEC-030 | — | 准入 |
| INTENT-COMPAT-044 | RUNNER_* 环境变量缺位 | P1 | RISK-COMPAT-01 / Runner 环境 | 关联 018/019（上下文 vs 环境变量两面）；关联 USE-044 | TC-441/442（FAIL） | 准入 |
| INTENT-COMPAT-045 | GitHub 风格 action 引用（owner/repo@ref）解析域 | P1 | RISK-USE-01+RISK-COMPAT-01 / action 引用 | 关联 024（前置问题 vs 等价性）、USE-007/052 | — | 准入 |
| INTENT-COMPAT-046 | 自托管 runs-on 写法规格矛盾（对象式 vs 数组式） | P1 | RISK-USE-01 / 自托管接入 | 关联 NEW-008（互补）；runs-on 主题簇（COMP-029/USE-031/040） | — | 准入 |
| INTENT-COMPAT-047 | 预装工具链规格 vs 实测一致性 + 与 GitHub image 差距 | P1 | RISK-COMPAT-01 / Runner 环境 | **父集于 NEW-011**（裁决确认） | TC-310、TC-499（FAIL） | 准入 |
| INTENT-COMPAT-048 | action 运行时 runs.using 类型覆盖（node16 vs composite/docker） | P1 | RISK-COMPAT-01 / action 生态 | 关联 NEW-010（互补成完整元数据面） | — | 准入 |
| INTENT-COMPAT-049 | YAML 1.1 `on:` 布尔陷阱在 GitCode 解析器的处理 | P2（自评降档，门禁接受） | RISK-USE-01 / 解析器行为 | 独立 | — | 准入 |
| INTENT-COMPAT-050 | format() 转义与字符串字面量引号规则边界 | P2（自评降档，门禁接受） | RISK-COMPAT-01 / 表达式边界 | 关联 009（互补） | — | 准入 |
| INTENT-COMPAT-051 | schedule 生命周期语义（60 天停用/延迟容忍） | P2（自评降档，门禁接受） | RISK-COMPAT-01（REL 邻接）/ schedule 🟡 | schedule 主题簇：关联 013、REL-085、USE-047 | TC-563（FAIL） | 准入 |
| INTENT-COMPAT-052 | 触发器平台限额（push 批量/dispatch 输入上限） | P2（自评降档，门禁接受） | RISK-COMPAT-01 / 平台限额 | 关联 012（同「平台限额」子类） | — | 准入 |
| INTENT-COMPAT-053 | job 级 permissions 字段支持度与覆盖语义 | P1 | RISK-SEC-01（邻接）+RISK-COMPAT-01 / 权限 | 关联 030（正交）、002、SEC-016/036（permissions 簇） | — | 准入（注：若实测为静默忽略→权限宽于声明，执行期升 blocker 缺陷，见 gate-log §3.4） |
| INTENT-COMPAT-054 | Runner OS 多样性：Windows/macOS Runner 有无与不支持 OS 的明确报错 | P1 | RISK-USE-01 / Runner OS 多样性（parity 增行） | 关联 NEW-008（标签不匹配报错）、COMP-029；**2026-07-27 STOP① 用户裁决增补，闭环盲区 B1** | — | 准入 |

### 维度：security（46 条）

#### 沿用（36 条，2026-07-23-01 已准入；本轮实证刷新 #51/#66 已回注备注）

| 意图 ID | 标题 | 优先级 | 去重关系 | 已有覆盖 |
|---|---|---|---|---|
| INTENT-SEC-001 | fork PR 触发 pull_request 不可读 secrets | P0 | 沿用（#51 实证强化，回归命脉） | TC-445 |
| INTENT-SEC-002 | pull_request_target checkout 不可信代码时受控 | P0 | 沿用（变体自 035；#66 实证刷新） | TC-461~463 |
| INTENT-SEC-003 | fork PR 的 ATOMGIT_TOKEN 仅 read | P0 | 沿用（#51 实证） | TC-445 |
| INTENT-SEC-004 | secret 日志/summary/堆栈脱敏 *** | P0 | 沿用 | TC-011, TC-354 |
| INTENT-SEC-005 | 脱敏不可被 base64 绕过 | P0 | 沿用（变体自 004） | — |
| INTENT-SEC-006 | 脱敏不可被拼接/插值绕过 | P0 | 沿用（变体自 004） | — |
| INTENT-SEC-007 | 脱敏不可被多行值绕过 | P0 | 沿用（变体自 004） | — |
| INTENT-SEC-008 | 脱敏不可被分片输出绕过 | P0 | 沿用（变体自 004） | — |
| INTENT-SEC-009 | PR 标题/正文不可注入 run 脚本 | P0 | 沿用 | — |
| INTENT-SEC-010 | 分支名/标签名不可注入 run 脚本 | P0 | 沿用（变体自 009） | — |
| INTENT-SEC-011 | 评论内容不可注入 run 脚本 | P0 | 沿用（变体自 009；关联 SEC-042/043） | — |
| INTENT-SEC-012 | commit message/author email 不可注入 | P0 | 沿用（变体自 009） | — |
| INTENT-SEC-013 | 防双重模板渲染 | P0 | 沿用 | — |
| INTENT-SEC-014 | 第三方 action 支持完整 commit SHA 固定 | P0 | 沿用 | TC-628 |
| INTENT-SEC-015 | 第三方 action 来源信任边界 | P0 | 沿用 | — |
| INTENT-SEC-016 | 显式 permissions 在 job 级实际生效 | P0 | 沿用（关联 COMPAT-053） | TC-351~416 |
| INTENT-SEC-017 | 未声明 permissions 默认最小化 | P0 | 沿用 | TC-351~416 |
| INTENT-SEC-018 | fork PR 写 cache 不可被主仓读取 | P0 | 沿用 | TC-301~303 |
| INTENT-SEC-019 | fork PR artifact 不可被主仓下载/执行 | P0 | 沿用 | — |
| INTENT-SEC-020 | job 结束 workspace/临时文件彻底清理 | P0 | 沿用 | — |
| INTENT-SEC-021 | runner 环境变量与 /tmp 跨 job 隔离 | P0 | 沿用（变体自 020） | — |
| INTENT-SEC-022 | 自托管 runner 跨项目残留隔离 | P0 | 沿用（变体自 020） | — |
| INTENT-SEC-023 | runner 网络出站受控（SSRF/内网跳板） | P0 | 沿用 | — |
| INTENT-SEC-024 | 变量名特殊字符不导致意外求值/泄露 | P0 | 沿用（关联 SEC-041） | TC-531 |
| INTENT-SEC-025 | printenv/进程枚举输出仍保持脱敏 | P0 | 沿用（变体自 004） | TC-011 |
| INTENT-SEC-026 | 评论触发关键字过滤不可被绕过 | P0 | 沿用（本轮新增变体 SEC-042） | TC-464~470 |
| INTENT-SEC-027 | 环境级 secret 审批前不可访问 | P0 | 沿用（关联 COMPAT-NEW-002） | TC-010 |
| INTENT-SEC-028 | workflow 命令 add-mask 响应不泄露原值 | P0 | 沿用（变体自 004） | TC-436 |
| INTENT-SEC-029 | 跨运行 artifact 视为不可信数据 | P0 | 沿用（变体自 019；关联 SEC-044） | — |
| INTENT-SEC-030 | ATOMGIT_ENV/OUTPUT/PATH 写协议防污染 | P0 | 沿用（关联 COMPAT-043） | TC-243~245, 434~435 |
| INTENT-SEC-031 | TOCTOU：审批后推新 commit 不被采用 | P0 | 沿用（本轮新增变体 SEC-043） | — |
| INTENT-SEC-032 | secret 不经 output/artifact/summary 侧信道外泄 | P0 | 沿用（变体自 004） | TC-246, TC-497 |
| INTENT-SEC-033 | 大 artifact/cache 配额与边界限制 | P0 | 沿用 | — |
| INTENT-SEC-034 | OIDC/短时凭据缺失需明示并提供替代 | P1 | 沿用 | — |
| INTENT-SEC-035 | pull_request_target 使用 base 分支 workflow 版本 | P0 | 沿用（#66 实证刷新） | TC-461~463 |
| INTENT-SEC-036 | token 默认权限范围与 job 级覆盖生效 | P0 | 沿用（变体自 016） | TC-351~416 |

#### 本轮新增（10 条，门禁全部准入）

| 意图 ID | 标题 | 优先级（裁决） | 覆盖风险/能力项 | 去重关系 | 已有覆盖 | 门禁结论 |
|---|---|---|---|---|---|---|
| INTENT-SEC-037 | ATOMGIT_TOKEN 生命周期与 run 绑定，结束失效不可复活 | P1 | RISK-SEC-01 / token 生命周期 | 独立 | — | 准入 |
| INTENT-SEC-038 | Secret 写后不可回读，管理操作鉴权+审计 | P1 | RISK-SEC-01 / secret 管理面 | 独立（关联 SEC-046 审计面） | — | 准入 |
| INTENT-SEC-039 | 组织级 Secret 仓库可见性边界生效 | P1 | RISK-SEC-01 / 组织级边界 | 独立 | — | 准入 |
| INTENT-SEC-040 | 运行日志访问控制、保留期与历史日志脱敏一致性 | P1 | RISK-SEC-01 / 日志读取面 | 独立（关联 SEC-046） | — | 准入 |
| INTENT-SEC-041 | Secret/变量命名约束实际生效，防遮蔽系统变量 | P1 | RISK-SEC-02 / 命名遮蔽 | 关联 SEC-024（互补）、USE-028（报错质量） | TC-531（相邻） | 准入 |
| INTENT-SEC-042 | pull_request_comment 的 comments 正则过滤语义安全（GitCode 特有） | P1 | RISK-SEC-02 / 评论触发 | **变体自 SEC-026**（显式关联，裁决确认） | TC-464~470（相邻） | 准入 |
| INTENT-SEC-043 | 评论 edited/deleted 事件 TOCTOU 面 | P1 | RISK-SEC-02 / TOCTOU | **变体自 SEC-031**（显式关联，裁决确认） | — | 准入 |
| INTENT-SEC-044 | 缺 workflow_run 等价特权分离机制的补偿防护 | P1 | RISK-SEC-01/02 / 机制缺失 | 关联 COMPAT-037（事件降级面）、SEC-029 | — | 准入 |
| INTENT-SEC-045 | Artifact/Cache 打包不意外夹带敏感文件 | P2（自评，门禁接受） | RISK-SEC-01 / 数据卫生 | 独立 | — | 准入 |
| INTENT-SEC-046 | 敏感操作可审计（secret/权限/rerun/审批/评论触发） | P1 | RISK-SEC-01/02 / 审计 | 独立（038/040/042 的审计断言挂靠本条） | — | 准入 |

### 维度：reliability（85 条）

#### 沿用（68 条，2026-07-23-01 已准入，含回填 REL-067/068）

| 意图 ID | 标题 | 优先级 | 去重关系 | 已有覆盖 |
|---|---|---|---|---|
| INTENT-REL-001~006 | concurrency.max 边界/越界、QUEUE/IGNORE、preemption 边界/越界 | P1 | 沿用 | TC-289~293, 518~523 |
| INTENT-REL-007~010 | job timeout 边界/越界/短超时/默认超时 | P1 | 沿用 | TC-270 |
| INTENT-REL-011~013 | rerun 边界/越界/6h 限制 | P1 | 沿用 | TC-350 |
| INTENT-REL-014~015 | paths 300 边界/越界 | P1 | 沿用 | TC-422, 514~515 |
| INTENT-REL-016~017 | step output 1MB 边界/越界 | P1 | 沿用 | TC-331/434, 554~555 |
| INTENT-REL-018~022 | Runner 磁盘/内存/CPU 边界与饱和 | P1 | 沿用 | TC-447~455 |
| INTENT-REL-023~024 | workflow_call 嵌套 2 层边界/3 层越界 | P1 | 沿用 | TC-426, TC-564 |
| INTENT-REL-025 | needs 失败传播（上游失败下游 skip） | P1 | 沿用（关联本轮 REL-069 成功路径） | TC-313~316 |
| INTENT-REL-026~027 | matrix fail-fast / max-parallel | P1 | 沿用 | TC-277/329, 278/330 |
| INTENT-REL-028 | 手动取消时 always() cleanup 执行 | P1 | 沿用（关联 COMP-028、REL-083） | TC-350 |
| INTENT-REL-029 | stages fail_fast 机制 | P1 | 沿用 | TC-403~404 |
| INTENT-REL-030 | continue-on-error=true 容错 | P1 | 沿用 | TC-272 |
| INTENT-REL-031~035 | 故障注入：SIGKILL/网络分区/磁盘满/cache 503/artifact 503 | P1 | 沿用（本轮 REL-080/081 为其补全变体） | TC-301~303, 294~300 |
| INTENT-REL-036~037 | 并发洪泛 10/50 push | P1 | 沿用 | — |
| INTENT-REL-038~039 | 大规模 matrix 20/50 组合 | P1 | 沿用（本轮 REL-076 补 256/300 上限） | TC-325~328 |
| INTENT-REL-040~043 | 超长日志/超大 artifact/超多 step/长时运行 | P1 | 沿用（本轮 REL-077/078 补上限探测） | TC-348, 378~380, 279~288, 270 |
| INTENT-REL-044~048 | 调度公平性/K8s 弹性/缓存 LRU/保留期边界/取消竞态 | P1 | 沿用 | TC-450, 301~303, 296/380, 350 |
| INTENT-REL-049~053 | Runner 规格真实性/调度延迟/日志性能/镜像性能/制品性能 | P1 | 沿用 | TC-447~455, 348, 262~263/458~460, 294~300 |
| INTENT-REL-054 | 缓存加速比 | P2 | 沿用 | TC-301~303 |
| INTENT-REL-055~061 | 并发压测/矩阵公平/调度一致性/Runner 状态机/日志稳定性/YAML 缓存/取消可靠性 | P1 | 沿用（REL-057 关联本轮 REL-082） | TC-289~293, 325~328, 348, 350 |
| INTENT-REL-062 | 网络依赖容错有界超时 | P2 | 沿用 | — |
| INTENT-REL-063~064 | 制品并发写一致性/子任务状态传播 | P1 | 沿用 | TC-294~300, 426/564 |
| INTENT-REL-065 | API 限流一致性 10 QPS | P2 | 沿用 | — |
| INTENT-REL-066 | 大规格资源调度稳定性 | P1 | 沿用 | TC-447~455 |
| INTENT-REL-067~068 | 项目级并发上限 200 边界/201 越界 | P1 | 沿用（2026-07-27 回填） | — |

#### 本轮新增（17 条，门禁全部准入）

| 意图 ID | 标题 | 优先级（裁决） | 覆盖风险/能力项 | 去重关系 | 已有覆盖 | 门禁结论 |
|---|---|---|---|---|---|---|
| INTENT-REL-069 | needs 依赖 matrix job 成功路径（历史 #101 ★） | **P0（STOP① 用户裁决确认）** | RISK-REL-02（新增 blocker）+ RISK-REL-01 / 执行模型 | 关联 REL-025（失败路径互补）、COMPAT-041（needs 聚合语义） | —（#101 实证） | 准入（P0 已确认） |
| INTENT-REL-070 | 多并发 run 中取消指定 run 目标正确性（#10） | P1 | RISK-REL-01 / 取消语义 | 关联 REL-061 | —（#10 实证） | 准入 |
| INTENT-REL-071 | run 状态收敛有界性（#55/#19） | P1 | RISK-REL-01 / 状态机 | 关联 COMP-017 | TC-347/348（相邻） | 准入 |
| INTENT-REL-072 | 新仓库 workflow 注册延迟（#17） | P1 | RISK-REL-01 / 触发注册 | 独立 | —（#17 实证） | 准入 |
| INTENT-REL-073 | 触发幂等与去抖（#67） | P1 | RISK-REL-01 / 触发语义 | 关联 REL-036/037 | —（#67 实证） | 准入 |
| INTENT-REL-074 | 架构标签调度正确性 x64/arm64（#48/#96） | P1 | RISK-REL-01 / 调度正确性 | 关联 COMP-029/REL-049 | —（#48/#96 实证） | 准入 |
| INTENT-REL-075 | timeout-minutes=720 超默认值接受/拒绝探测 | P2（自评，门禁接受；发现静默截断升 P1） | RISK-REL-01 / 未公开配额 | 关联 COMP-008、REL-007~010 | — | 准入 |
| INTENT-REL-076 | matrix 组合数上限 256/300 探测 | P2（同上升级条款） | RISK-REL-01 / matrix 上限 ❓ | 关联 REL-038/039、COMPAT-NEW-007 | — | 准入 |
| INTENT-REL-077 | 单 job 日志上限 500MB/1GB 截断语义探测 | P2（同上升级条款） | RISK-REL-01 / 日志上限 | 关联 REL-040/051/059 | — | 准入 |
| INTENT-REL-078 | artifact 上限 2GB/5GB 接受/拒绝探测 | P2（自评，门禁接受） | RISK-REL-01 / artifact 上限 | 关联 REL-041/053、COMP-015 | — | 准入 |
| INTENT-REL-079 | cache 容量上限与同 key 并发写一致性探测 | P2（自评，门禁接受） | RISK-REL-01 / cache 上限+竞态 | 关联 REL-046/063 | — | 准入 |
| INTENT-REL-080 | 故障注入：心跳分区 60s 恢复后续跑 | P1 | RISK-REL-01 / 混沌注入 | **变体/补全自 REL-031**（临时分区 vs 永久失联） | — | 准入 |
| INTENT-REL-081 | 故障注入：artifact 上传中断半成品不得可下载 | P1 | RISK-REL-01 / 数据完整性 | **变体/补全自 REL-032**（进程被杀 vs 网络分区） | — | 准入 |
| INTENT-REL-082 | 故障注入：排队期 runner 下线重调度（#12/#54） | P1 | RISK-REL-01 / 调度可用性 | 关联 REL-057 | —（#12/#54 实证） | 准入 |
| INTENT-REL-083 | post 后处理阶段失败语义（run_always=true） | P1 | RISK-REL-01 / post ❌特有项 | 关联 COMP-007、COMP-028、REL-028 | — | 准入 |
| INTENT-REL-084 | 日志实时性：运行中流式可见延迟有界（#14/#81） | P1 | RISK-REL-01 / 日志链路 | 关联 REL-059、USE-017/018 | TC-348（相邻） | 准入 |
| INTENT-REL-085 | schedule 触发准点性与丢失率 | P1 | RISK-REL-01 / schedule 🟡 | schedule 主题簇：关联 COMP-005、COMPAT-013/051、USE-047 | — | 准入 |
| INTENT-REL-086 | K8s 单集群接入与 NPU 资源发现 | P1 | RISK-REL-01 / NPU 调度（盲区 GAP-019/020 闭环） | 独立（2026-07-27 NPU 增补） | —（xlsx NPU sheet #1） | 准入（用户裁决） |
| INTENT-REL-087 | Karmada 多集群接入、聚合资源发现与分发调度 | P1 | RISK-REL-01 / NPU 调度 | 独立（2026-07-27 NPU 增补） | —（xlsx #2/6/7/10） | 准入（用户裁决） |
| INTENT-REL-088 | pod NPU 请求调度正确性与非法请求 Pending（多副本 Worker 已知失败回归） | P1（回归优先） | RISK-REL-01 / NPU 调度 | 独立（2026-07-27 NPU 增补） | —（xlsx #3/4/5/8/9，#5 实测不通过） | 准入（用户裁决） |
| INTENT-REL-089 | vcjob 格式兼容与大规模并发提交（vcjob 已知失败回归） | P1（回归优先） | RISK-REL-01 / NPU 调度 | 独立（2026-07-27 NPU 增补） | —（xlsx #11/14，#11 实测不通过） | 准入（用户裁决） |
| INTENT-REL-090 | 同一集群重复接入幂等性 | P2 | RISK-REL-01 / NPU 调度 | 独立（2026-07-27 NPU 增补） | —（xlsx #12） | 准入（用户裁决） |
| INTENT-REL-091 | 集群断连恢复后的任务日志同步 | P1 | RISK-REL-01 / NPU 调度 | 独立（2026-07-27 NPU 增补） | —（xlsx #13） | 准入（用户裁决） |

### 维度：usability（52 条）

#### 沿用（29 条，2026-07-23-01 已准入）

| 意图 ID | 标题 | 优先级 | 去重关系 | 已有覆盖 |
|---|---|---|---|---|
| INTENT-USE-001 | 工作流目录搬运路径指引 | P1 | 沿用（关联 COMP-001） | TC-366, TC-383 |
| INTENT-USE-002 | github.* 失效提示 atomgit.* | P1 | 沿用（关联 COMPAT-016） | TC-017~018 |
| INTENT-USE-003 | GITHUB_* 空值提示质量 | P1 | 沿用（关联 COMPAT-017；补强证据 TC-533→USE-046） | TC-197~218 |
| INTENT-USE-004 | success() 括号报错 | P1 | 沿用（关联 COMPAT-004、USE-035） | TC-176~179 |
| INTENT-USE-005 | permissions 命名报错 | P1 | 沿用（关联 COMPAT-030） | TC-351~416 |
| INTENT-USE-006 | runs-on 标签不匹配报错 | P1 | 沿用（关联 COMP-010；与 USE-031 互补） | TC-571~573 |
| INTENT-USE-007 | actions/checkout@v4 报错迁移指引 | P1 | 沿用（关联 COMPAT-024/045） | TC-304 |
| INTENT-USE-008 | inputs 非 string 类型报错 | P1 | 沿用（关联 COMPAT-014） | TC-014, TC-193 |
| INTENT-USE-009 | pull_request types GitHub 命名静默失败 | P1 | 沿用（关联 COMPAT-011/038） | TC-234, TC-560 |
| INTENT-USE-010 | 废弃命令报错给出替代 | P1 | 沿用（关联 USE-053、COMPAT-NEW-012） | TC-239~241, 552~553 |
| INTENT-USE-011 | stages/post 文档可发现性 | P1 | 沿用（关联 COMP-007、USE-032） | TC-402~404 |
| INTENT-USE-012 | 文档残留 GITHUB_* 措辞 | P1 | 沿用 | TC-206, TC-220 |
| INTENT-USE-013 | runner.os 支持平台文档-实际一致 | P1 | 沿用（关联 COMPAT-018；值格式拆分至 USE-041） | TC-023, TC-094 |
| INTENT-USE-014 | vars 上下文文档-样本矛盾 | P1 | 沿用（关联 COMPAT-022） | TC-019, 115~119 |
| INTENT-USE-015 | paths 300 上限文档显眼性 | P1 | 沿用（关联 COMPAT-012） | TC-422, 514~515 |
| INTENT-USE-016 | secret 脱敏绕过文档-实际一致 | P0 | 沿用（关联 SEC-004~008） | TC-011 |
| INTENT-USE-017 | 日志 step 时间线可读性 | P1 | 沿用（关联 REL-084） | TC-348 |
| INTENT-USE-018 | 日志搜索/下载/高亮交互 | P1 | 沿用 | TC-348 |
| INTENT-USE-019 | 状态徽标回写可读性 | P1 | 沿用 | TC-347 |
| INTENT-USE-020 | STEP_SUMMARY Markdown 渲染 | P1 | 沿用（关联 COMP-018） | TC-246, TC-497 |
| INTENT-USE-021 | ::error::/::warning:: 注解可读性 | P1 | 沿用（关联 COMPAT-042） | TC-248~250 |
| INTENT-USE-022 | YAML 报错行号与可操作性 | P1 | 沿用 | TC-393~401 |
| INTENT-USE-023 | 未知字段报错质量 | P1 | 沿用（关联 COMP-002、USE-036/037/040） | TC-274, TC-336 |
| INTENT-USE-024 | 表达式语法错误报错质量 | P1 | 沿用 | TC-160~187 |
| INTENT-USE-025 | Runner 标签无匹配报错质量 | P1 | 沿用（关联 COMP-010、COMPAT-NEW-008） | TC-571~573 |
| INTENT-USE-026 | workflow_call 超 2 层报错 | P1 | 沿用（关联 REL-024） | TC-564 |
| INTENT-USE-027 | concurrency.max 越界报错 | P1 | 沿用（关联 REL-002） | TC-522 |
| INTENT-USE-028 | Secret 命名违规报错质量 | P1 | 沿用（关联 SEC-041） | TC-531 |
| INTENT-USE-030 | workflow_dispatch inputs 默认值与必填校验 | P1 | 沿用 | TC-012~016, 581~583 |

#### 本轮新增（23 条，门禁全部准入）

| 意图 ID | 标题 | 优先级（裁决） | 覆盖风险/能力项 | 去重关系 | 已有覆盖 | 门禁结论 |
|---|---|---|---|---|---|---|
| INTENT-USE-031 | runs-on 标签写法跨文档三种形态互相矛盾 | **P0（STOP① 恢复，RISK-USE-02）** | RISK-USE-02 + RISK-USE-01 / runs-on 🟡 | runs-on 主题簇（COMP-029=平台行为、COMPAT-046=自托管、本条=文档一致性）；与 USE-006 互补 | — | 准入 |
| INTENT-USE-032 | stages/jobs 字段语法跨文档四种形态矛盾 | **P0（STOP① 恢复，RISK-USE-02）** | RISK-USE-02 + RISK-USE-01 / stages ❌ | 关联 COMP-019（平台行为 vs 文档一致性两面） | — | 准入 |
| INTENT-USE-033 | 文档代码示例「照抄即可跑」端到端可复刻抽查 | **P0（STOP① 恢复，RISK-USE-02）** | RISK-USE-02 + RISK-USE-01 / 文档可信度 | 独立 | — | 准入 |
| INTENT-USE-034 | 官方文档章节编号跳跃与编辑质量 | P2 | RISK-COMPAT-01 / 文档编辑质量 | 独立 | — | 准入 |
| INTENT-USE-035 | expressions.md 函数表语法标记与术语混乱 | P1 | RISK-USE-01 / 表达式文档 | 关联 USE-004、COMPAT-004 | — | 准入 |
| INTENT-USE-036 | 命名双轨 id/identifier、pr_comment、comments/keyword | P1 | RISK-USE-01 / 未知字段 ❓ | 关联 COMP-024（pr_comment 别名行为面） | — | 准入 |
| INTENT-USE-037 | 未文档化字段 select/manual_override/code-update/顶层 inputs | P1 | RISK-USE-01 / 未知字段 ❓ | 关联 COMP-021/031（行为面） | — | 准入 |
| INTENT-USE-038 | 变量插值双语法 ${gitcode_*}/${PIPELINE_*}/repositoryurl | P1 | RISK-USE-01 / 上下文 ❌ | 关联 COMP-032（行为面） | — | 准入 |
| INTENT-USE-039 | 未文档化函数 default() 的真实语义（文档面） | P2 | RISK-USE-01 / 表达式函数 ❓ | 关联 COMP-022（行为面） | — | 准入 |
| INTENT-USE-040 | runs-on 含资源池名 4 段式写法文档未提 | P1 | RISK-USE-01 / runs-on 🟡 | runs-on 主题簇（关联 COMP-029） | — | 准入 |
| INTENT-USE-041 | runner 上下文值大小写/格式与文档不一致 | P1 | RISK-COMPAT-01 / 上下文值格式 | 关联 COMPAT-018/019（GitHub 差异面；本条=文档-实际一致面），展开时共享证据 | TC-095, TC-137/138 | 准入 |
| INTENT-USE-042 | container.image 文档声明可用但实际不可用 | P1 | RISK-USE-01 / 未知字段 ❓ | 关联 COMPAT-NEW-001（container 报错面） | TC-273 | 准入 |
| INTENT-USE-043 | environment 字段语法文档缺失 | P1 | RISK-USE-01 / 环境字段 | 关联 COMPAT-023（降级行为面） | TC-010 | 准入 |
| INTENT-USE-044 | 系统环境变量清单与实际注入集合不一致 | P1 | RISK-USE-01 / 环境变量 | 关联 COMPAT-017/044 | TC-206, TC-220 | 准入 |
| INTENT-USE-045 | 缺 GitCode 等效 CLI（gh 对应物）迁移指引 | P1 | RISK-USE-01 / 迁移指引 | 独立 | TC-502 | 准入 |
| INTENT-USE-046 | job env 未注入 Runner shell（文档承诺未兑现） | **P0（STOP① 恢复，RISK-USE-02）** | RISK-USE-02 + RISK-USE-01 / env 注入 | 独立（与 COMPAT-017 松关联） | TC-533 | 准入 |
| INTENT-USE-047 | schedule 不触发时无可观测提示 | P1（llm_assisted） | RISK-USE-01 / 可观测性 | schedule 主题簇（REL-085=调度器正确性，本条=可观测性） | TC-391, S3×24 | 准入 |
| INTENT-USE-048 | API 字段与事件类型命名不一致 opened vs open | P2 | RISK-USE-01 / 命名一致性 | 关联 COMPAT-011（事件面；本条=API 面） | TC-064 | 准入 |
| INTENT-USE-049 | rerun 上限在 UI 的明示 | P1（llm_assisted） | RISK-COMPAT-01 / rerun 🟡 | 关联 REL-011~013（行为面） | — | 准入 |
| INTENT-USE-050 | 新手快速开始路径端到端可复刻 | **P0（STOP① 恢复，RISK-USE-02；llm_assisted）** | RISK-USE-02 + RISK-USE-01 / onboarding | 独立 | — | 准入 |
| INTENT-USE-051 | workflow_dispatch 手动触发 UI 与 YAML inputs 一致性 | P1 | RISK-USE-01 / dispatch inputs 🟡 | 关联 COMP-020/031、USE-030 | — | 准入 |
| INTENT-USE-052 | 官方短名 Action 清单与 actions-market 49 插件目录一致性 | P1 | RISK-USE-01 / action 生态 | 关联 COMPAT-024/045 | — | 准入 |
| INTENT-USE-053 | 隐藏开关（ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS）默认值与文档缺失 | P1 | RISK-SEC-01（邻接）/ 安全默认值 | 关联 USE-010、COMPAT-NEW-012 | TC-220 | 准入 |

---

## 打回/待补意图清单

**本轮打回 0 条。** 五维度 agent 均为增量模式产出，ID 无冲突，逐条满足最小可测标准（oracle 明确 + 三线断言），无无法对齐风险登记册的孤立 intent。原疑似重复项（NEW-006⊂COMPAT-041、NEW-011⊂COMPAT-047、USE-041≈COMPAT-018/019）经裁决均以「变体/关联 + 展开时合并证据链」处理，不打回（理由见 gate-log §2）。

---

## 跨维度主题簇索引（展开期合并证据链指引）

| 主题簇 | 成员 intent | 展开纪律 |
|---|---|---|
| runs-on 形态 | COMP-029、COMPAT-046、USE-031、USE-040、NEW-008、COMP-010/REL-074 | 平台行为用例归 COMP-029/046；文档断言归 USE-031/040；共享调度证据 |
| stages 形态 | COMP-019、USE-032、COMP-007、REL-029 | 行为裁定归 COMP-019，文档断言归 USE-032 |
| PR 代码版本语义 | COMP-033、COMPAT-039 | 共享 PR 夹具与 sha/ref 观测证据链 |
| 未文档化字段 | COMP-021/031、USE-037、USE-036、COMP-024 | 平台行为归 COMP 系列，文档 diff 归 USE 系列 |
| default() 函数 | COMP-022、USE-039 | 合并为一组用例（行为+文档双断言） |
| 插值语法 | COMP-032、USE-038 | 同上 |
| needs×matrix | REL-069、COMPAT-041、NEW-006、REL-025 | NEW-006 并入 COMPAT-041；REL-069 独立（成功路径实证 bug） |
| schedule | COMP-005、COMPAT-013/051、REL-085、USE-047 | 触发可靠性归 REL-085，生命周期归 COMPAT-051，可观测性归 USE-047 |
| permissions | COMPAT-002/030/053、SEC-016/017/036、COMP-013、USE-005 | 053 与 SEC-016/036 共享权限观测夹具 |
| pull_request_target | COMP-004/014/023、SEC-002/035、COMPAT-032 | 安全断言归 SEC，文档矛盾归 COMP-023 |
| 取消/post 语义 | COMP-028、REL-028/061、REL-083 | 共享取消时序观测 |
| Runner 隔离边界 | COMP-025、SEC-020~023、COMP-011 | 安全深测归 SEC，COMP-025 提供事实底座 |
| 环境变量清单 | COMPAT-017/044、USE-044、USE-003 | 注入集合探测证据共享 |
| runner 值格式 | COMPAT-018/019、USE-041 | USE-041 展开时复用 018/019 的实测值 |
| action 引用生态 | COMPAT-024/045/048、USE-007/052、NEW-010 | 解析域归 COMPAT-045，文档对照归 USE-052 |
| 废弃命令/隐藏开关 | USE-010/053、COMPAT-NEW-012、COMPAT-042 | 开关默认值探测证据共享 |
