# Gate Log（评审门禁过程记录）

> Run: 2026-07-27-01
> 评审角色: review-gate + orchestrator（串行执行）
> 评审日期: 2026-07-27
> 输入: intents/spec.md（+15）、intents/compat.md（+18）、intents/security.md（46）、intents/reliability.md（+17）、intents/usability.md（52）
> 基线: baseline/risk-register.md（5 风险项，blocker=RISK-SEC-01/02）、baseline/parity-matrix.md（26 能力项）、baseline/quality-gate.md
> 对照: runs/2026-07-23-01/intent-library.md（186 准入 + 回填 14 = 198 沿用基底）

---

## 1. 评审结论摘要

| 项 | 结果 |
|---|---|
| 意图总数 | 282（沿用 198 + 新增 84，含 STOP① 增补 COMPAT-054） |
| 准入 | **282** |
| 打回 | **0** |
| STOP① 用户裁决（2026-07-27） | ① REL-069 升 P0 + 登记册增补 RISK-REL-02 ✅已落实；② 增补 RISK-USE-02，USE-031/032/033/046/050 恢复 P0 ✅已落实；③ 19 条 P2 降档**用户确认接受**；④ 增补 COMPAT-054 闭环盲区 B1 ✅已落实；B2/B3 用户知悉不阻塞本轮（安排后续补输入）；B5 记录建议本轮后回写基线 |
| blocker 覆盖 | RISK-SEC-01 / RISK-SEC-02 / RISK-REL-02 / RISK-USE-02 四个 blocker 均有 P0 intent 覆盖，无遗漏 |
| 覆盖盲区 | 5 项（见 §4；B1 已由 COMPAT-054 闭环，B2/B3 为输入退化待补，B4 已由 RISK-REL-02 闭环，B5 为基线维护建议） |

---

## 2. 去重记录（聚类裁决）

### 2.1 本轮新增之间的同义/包含关系

| 组 | 成员 | 裁决 | 理由 |
|---|---|---|---|
| needs×matrix | COMPAT-041（父）⊃ NEW-006（子） | **均准入，NEW-006 标注变体/子集，展开时并入 041** | agent 已标注父集关系，裁决确认；NEW-006 单一边界（未声明 output 返空）可作为 041 的一个验证点，不单独展开用例 |
| 预装工具链 | COMPAT-047（父）⊃ NEW-011（子） | **均准入，NEW-011 标注变体/子集** | 同上；NEW-011 的 Java 单点并入 047 的全量对账 |
| PR 代码版本语义 | COMP-033 ≈ COMPAT-039 | **均准入，显式关联，共享 PR 夹具与证据链** | COMP-033=GitCode 特有 pre-merge ref 存在性/刷新语义；COMPAT-039=对齐 GitHub merge commit 模型 + 冲突不触发。断言目标不同（一为特有 ref 语义、一为跨平台对齐），不构成重复，但观测手段相同，展开期必须共享夹具防止重复造数 |
| 评论触发变体 | SEC-042 变体自 SEC-026；SEC-043 变体自 SEC-031 | **准入，变体关系确认** | agent 已显式标注；042 细化 GitCode 特有正则面、043 扩展 TOCTOU 至评论编辑维度，均为母 intent 未覆盖的新攻击面 |
| 混沌注入补全 | REL-080 补全 REL-031；REL-081 补全 REL-032 | **准入，标注变体/补全** | 031=永久失联、080=临时分区恢复；032=网络分区、081=进程被杀元数据一致性。故障模式不同，保留 |

### 2.2 跨维度边界重叠裁决（usability 新增 23 条 vs spec/compat）

usability agent 的边界声明（§4：assertion 目标是文档与可观测 UI，非行为等价）经逐条复核**成立**。裁决原则：**同一事实的「平台行为裁定」归 spec/compat，「文档一致性/可发现性/可理解性」归 usability，两者准入并显式关联，展开期共享实测证据**。

| usability 条目 | 关联条目 | 裁决 |
|---|---|---|
| USE-031（runs-on 文档矛盾） | COMP-029（平台裁定）、COMPAT-046（自托管）、USE-040（4 段式） | 四者构成 runs-on 主题簇，oracle 各异（文档扫描/调度行为/自托管调度/文档缺口），**全部准入**，无合并 |
| USE-032（stages 文档 4 形态） | COMP-019（平台裁定） | 准入+关联 |
| USE-036（命名双轨） | COMP-024（pr_comment 行为） | 准入+关联 |
| USE-037（未文档化字段群） | COMP-021/031 | 准入+关联；USE-037 粒度可接受（单一文档 diff 扫描动作），不打回 |
| USE-038（插值双语法） | COMP-032 | 准入+关联 |
| USE-039（default() 文档缺失） | COMP-022 | 准入+关联，展开时合并为一组双断言用例 |
| USE-040（4 段式资源池） | COMP-029 | 准入+关联 |
| USE-041（runner 值格式文档失实） | COMPAT-018/019 | **最接近重复的一组**。裁决：保留——018/019 的 oracle 是「GitHub vs GitCode」，USE-041 的 oracle 是「GitCode 文档 vs GitCode 实测」，断言方向不同；但展开时 USE-041 必须复用 018/019 的实测值，不得重复探测 |
| USE-042（container.image 不可用） | COMPAT-NEW-001 | 准入+关联（NEW-001=报错质量，042=文档能力标注） |
| USE-043（environment 语法缺失） | COMPAT-023 | 准入+关联 |
| USE-044（环境变量清单不一致） | COMPAT-017/044 | 准入+关联 |
| USE-047（schedule 不触发无提示） | REL-085、COMPAT-051 | 准入+关联（可观测性 vs 调度器正确性 vs 生命周期，三面正交） |
| USE-048（API opened vs 事件 open） | COMPAT-011 | 准入+关联（API 面 vs workflow 语法面） |
| USE-049（rerun UI 明示） | REL-011~013 | 准入+关联 |
| USE-053（隐藏开关文档缺失） | USE-010、COMPAT-NEW-012 | 准入+关联 |

### 2.3 compat 新增 18 条与上轮 001~035/NEW-001~012 的重叠裁决

agent 在条目内已标注邻近关系（038↔011、041↔NEW-006、042↔NEW-009、046↔NEW-008、047↔NEW-011、048↔NEW-010、053↔030、040↔016/017、036↔006、037↔011/NEW-004、039↔032、043↔017、044↔018/019、045↔024、050↔009、051↔013、052↔012）。逐条复核结论：

- **全部「互补/父集/正交」标注成立**，无隐性重复。
- 两处父集关系（041⊃NEW-006、047⊃NEW-011）按 §2.1 处理（子项不单独展开）。
- 037（事件不存在）与 011/NEW-004（types 差异）为半径包含关系，但 037 的负向断言（静默保存永不触发）是 011 未覆盖的更差形态，保留。

---

## 3. 优先级裁决记录

### 3.1 P0 覆盖核对（blocker 强制）

| blocker 风险项 | 覆盖 P0 intent | 结论 |
|---|---|---|
| RISK-SEC-01（fork PR 读 secrets） | SEC-001~008/016~022/025/027/028/032/035/036、COMPAT-002/025/028/030/032/033/NEW-002、COMP-004/011/012/013/014/016、USE-016 | ✅ 足额（含 #51 实证强化的 SEC-001/003 回归命脉） |
| RISK-SEC-02（不可信输入注入） | SEC-009~015/023/024/026/029/030/031/033 | ✅ 足额 |

### 3.2 降档裁决：agent 自评 P0 但无法对齐登记册 blocker（5 条）

rules.md §2：「P0 必须逐条对应风险登记册中的 blocker 项，不滥用」。登记册 blocker 仅 RISK-SEC-01/02。以下 5 条自评 P0 均挂靠 RISK-USE-01（P1），**裁决降档为 P1**：

| 意图 ID | 自评 | 裁决 | 理由 |
|---|---|---|---|
| USE-031 | P0 | **P1** | 文档矛盾影响 onboarding，但有 workaround（实测任一种写法即知），不满足 blocker「不修不能上线」 |
| USE-032 | P0 | **P1** | 同上 |
| USE-033 | P0 | **P1** | 示例不可复刻影响新手转化，非上线 blocker；quality-gate 易用性 blocker 判定为「核心迁移路径完全不可用且无提示」，文档示例错误不满足「完全不可用」 |
| USE-046 | P0 | **P1** | job env 不注入 shell 属「文档承诺未兑现」+ TC-533 实证，严重但有 workaround（表达式层/ step 级 env 重声明）；建议产品侧按缺陷修复，但测试优先级按登记册为 P1 |
| USE-050 | P0 | **P1** | onboarding 路径评估，同 USE-033 理由 |

**同时给出登记册增补建议（待用户确认）**：若产品策略认为「文档可信度/核心迁移路径」应与安全同级管控，建议在 risk-register.md 增补 `RISK-USE-02（文档承诺未兑现/核心迁移路径失效，P0/blocker）`，则上述条目可恢复 P0。未增补前一律按 P1 执行。

### 3.3 升档裁决：REL-069（争议点①）

- 事实：历史 #101 为 ★ 标注实证 bug——「jobA needs matrix jobB，jobB 全部成功 jobA 仍初始化失败」。
- 登记册现状：REL 维度仅 RISK-REL-01（P1，非 blocker）。
- agent 自评：P0 + 建议登记册增补 blocker。
- **门禁裁决：升级为 P0（条件生效）**，理由：①实证 bug 且 ★ 标注；②命中「matrix 构建→汇总发布」主流编排模式，影响面=所有 matrix 用户；③失败形态无声（jobB 显示成功），概率与影响乘积满足 blocker 定义；④quality-gate 稳定性 blocker 含「故障后数据损坏/无法恢复」精神相近项。
- **附带动作**：建议 risk-register.md 增补 `RISK-REL-02（matrix×needs 聚合判定错误，P0/blocker，依据 #101）`。
- **条件条款**：用户 STOP① 否决增补，则 REL-069 按 P1 执行（仍准入、仍展开，仅火力排序降档）。

### 3.4 维持 P1 但附执行期升级条款（2 条）

| 意图 ID | 裁决 | 条款 |
|---|---|---|
| COMPAT-053（job 级 permissions 静默忽略面） | P1 | 若实测为「静默忽略→权限宽于声明」，执行期直接记 blocker 缺陷（quality-gate 安全零容忍），无需等登记册变更 |
| COMP-023/025/030（RISK-SEC-01 邻接） | P1 | 维持 agent 自评；主攻击面已由 SEC 维度 P0 覆盖，此三条提供事实底座，不重复占 P0 额度 |

### 3.5 自评 P2 降档接受（19 条）

登记册无 P2 级风险项，以下条目 agent 按「影响面长尾/有 workaround」自评 P2。门禁逐条复核：

- **接受**：COMPAT-049（YAML on: 陷阱，平台通常已处理）、050（format 转义边界）、051（schedule 生命周期长尾）、052（批量/超限额长尾）；COMP-022（default() 影响面限于 select 模式）、024（pr_comment 别名）、026（required 声明行为）、027（连字符命名边界）、031（顶层 inputs）、032（遗留插值）；SEC-045（用户卫生与平台护栏结合部）；USE-034（章节编号）、039（default() 文档面）、048（命名对照）；REL-075~079（未公开配额探测，条内已注「发现静默截断/损坏升 P1」的自动升级条款）。
- 理由：P2 档位在 rules.md §2 中定义为「体验/边角」，上述条目概率×影响均低于同族 P1 条目；且探测类条目自带升级条款，不会埋藏高危发现。
- **提交用户确认**：若任一条目用户认为应回到 P1，在 STOP① 指出即可。

---

## 4. 覆盖盲区清单

### 4.1 风险登记册维度（逐风险项核对）

| 风险项 | 覆盖结论 |
|---|---|
| RISK-SEC-01（blocker） | ✅ 无盲区 |
| RISK-SEC-02（blocker） | ✅ 无盲区 |
| RISK-COMPAT-01 | ✅ 无盲区 |
| RISK-REL-01 | ✅ 无盲区 |
| RISK-USE-01 | ✅ 无盲区 |

### 4.2 Parity Matrix 能力项维度（26 项逐条核对）

全部 26 个能力项（含 ❓/🟡/❌ 项）均能反查到至少一条准入 intent（含沿用）。无未覆盖能力项。核对明细：未知字段❓→COMP-002/COMPAT-021/USE-023/036/037；Runner ephemeral❓→COMP-011/COMPAT-028/SEC-020~022；permissions 默认❓→COMP-013/COMPAT-002/SEC-017；cache fork 隔离❓→COMP-016/SEC-018/COMPAT-025；函数边界❓→COMPAT-006~010/036/050；matrix 上限❓→REL-038/039/076/NEW-007；迁移报错质量❓→COMPAT-031/USE-001~010；其余 ✅/🟡/❌ 项均有对应沿用 intent。

### 4.3 真实盲区（如实暴露）

| # | 盲区 | 性质 | 建议 |
|---|---|---|---|
| B1 | **Runner OS 多样性**：GitCode 是否提供 Windows/macOS Runner（GitHub 有 windows-latest/macos-latest 生态），26 项 parity 表未列、无 intent 覆盖 | 能力项盲区（parity 表本身缺行） | **已闭环（2026-07-27 STOP①）**：增补 INTENT-COMPAT-054（P1 准入）；执行后回写 parity-matrix 增行 |
| B2 | **business-context 空模板**：SEC-022/023/040 等依赖部署模型/内网拓扑的 intent 证据不足 | 输入退化盲区 | 补齐 business-context（部署模型、历史安全台账、Runner 拓扑）后重审上述 intent；**用户知悉不阻塞本轮，安排后续补输入** |
| B3 | **无真实 GitHub 侧 workflow 样本**：compat 维度「现实命中率」论证依赖 GitHub 官方文档描述而非真实负载统计 | 输入退化盲区 | 补充 3~5 个真实开源项目 GitHub workflow 样本至 inputs/workflow-samples/；**用户知悉不阻塞本轮，安排后续补输入** |
| B4 | **reliability 维度 P0 为空**（登记册 REL 无 blocker） | 待裁决 | **已闭环（2026-07-27 STOP①）**：REL-069 升 P0，登记册增补 RISK-REL-02 |
| B5 | **风险登记册自身维护缺口**：仅 5 条风险项，「覆盖意图」列全为占位（INTENT-SEC-xxx/—），未随两轮 run 回填；usability/compat 多条 P0 诉求无登记册落点 | 基线维护盲区 | **部分落实（2026-07-27 STOP①）**：已增补 RISK-REL-02 / RISK-USE-02 两条 blocker 并回填覆盖意图；「覆盖意图」列全量回填建议本轮后统一回写基线 |

---

## 5. 打回清单

**本轮打回 0 条。** 复核要点：①五维度均为增量产出，与 198 条沿用基底无 ID 冲突；②每条新增 intent 满足最小可测标准（四要素齐、oracle 明确、三线断言）；③无无法对齐风险登记册的孤立 intent；④原疑似重复组均按「变体/关联+合并证据链」处理（§2），保留价值大于打回收益。

---

## 6. STOP① 用户裁决落实记录（2026-07-27）

原提交的 5 个裁决点，用户裁决如下，**全部已落实**：

| # | 裁决点 | 用户裁决 | 落实位置 |
|---|---|---|---|
| ① | REL-069 是否升 P0 | **升 P0**；登记册增补 RISK-REL-02（blocker，needs 依赖的 matrix job 全成功但上游 job 初始化失败时无声失败，依据 #101 ★） | baseline/risk-register.md 新增行；intent-library.md REL-069 行改标 P0；本文件 §3.3 裁决生效 |
| ② | 5 条 usability 自评 P0 降档是否接受 | **不接受降档**：增补 RISK-USE-02（blocker，官方文档承诺与实现不一致/核心迁移路径文档错误导致用户照抄失败），USE-031/032/033/046/050 **恢复 P0** | baseline/risk-register.md 新增行；intent-library.md 5 行改标 P0 |
| ③ | 19 条自评 P2 降档 | **用户确认接受**，按 P2 执行 | 无改动；本文件 §3.5 裁决生效 |
| ④ | 盲区 B1 是否本轮补 intent | **本轮补**：新增 INTENT-COMPAT-054（Runner OS 多样性，P1 准入） | intents/compat.md 追加条目；intent-library.md compatibility 表追加行 |
| ⑤ | B2/B3 输入退化是否阻塞 | **不阻塞本轮**，用户安排后续补输入；B5 基线回写建议本轮后统一处理 | 本文件 §4.3 状态更新 |

**门禁关闭结论**：282 条 intent 全部准入（P0 55 / P1 205 / P2 22），4 个 blocker 风险项（RISK-SEC-01/02、RISK-REL-02、RISK-USE-02）均有 P0 覆盖，无未覆盖 blocker，无打回。run 状态推进为 `gated`，可进入阶段 B（case-writer 基底 diff + 增量生成）。


---

## §7 NPU/Karmada 增补门禁（2026-07-27 用户补盲区）

- 背景：用户提出 inputs/existing-cases xlsx「NPU用例」sheet（14 条）无对应用例，要求补盲区；归并为 INTENT-REL-086~091（6 条）。
- 用户裁决：6 条全准入并展开用例；REL-088/089（含 xlsx 实测不通过实证）维持 P1（不自造 P0）。
- 输入退化声明：inputs 无 Karmada/volcano/NPU 平台侧文档，oracle 仅 xlsx 预期结果列；执行需平台侧环境。
- 状态：准入 6/6，打回 0。
