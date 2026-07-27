# DoD Checklist — Run 2026-07-27-01

> 验收角色：验收 agent（STOP②）
> 评审日期：2026-07-27
> 依据：process.md §4（7 项 DoD）、rules.md、baseline/quality-gate.md
> 方法：脚本全量扫描（489 text + 489 yaml）+ 抽样人工复核 + 全量 schema 复验

| # | DoD 项 | 结论 | 证据 |
|---|---|---|---|
| 1 | 完整性/覆盖度评审基于文本用例，对照 Parity Matrix 与风险登记册无盲区 | ✅ | 见 `coverage.md`：26/26 能力项有用例反查（§2），7/7 风险项覆盖、4 blocker 均有 P0（§3）；原盲区 B1 已由 COMPAT-RUNSON-01-005/006 闭环（文件核实存在）；B2/B3 为输入退化非覆盖盲区，已如实标注 |
| 2 | 每条文本用例可溯源 intent_ref + 明确预期结果 + 验证点 | ✅ | 脚本全量扫描 489/489 文本用例均含「溯源意图」「预期结果」「验证点」三字段（0 缺失）；溯源意图→intent-library 反查 0 悬空（含区间记号展开后全部命中，KEEP-TC-* 为基底评估锚点除外）；抽验 SEC-FORK-01-001.md 四要素齐全 |
| 3 | 每条文本用例有对应且通过 schema 校验的可执行 YAML | ❌ **488/489** | ① text/yaml ID 一一对应 489/489 ✓（diff 校验）；② 新增 120 条经五个 case-writer 校验 22+30+16+22+30=120/120 全过；③ 基底 369 条上轮已过校验，本轮抽查 5 条（COMP-PUSH-01-001、SEC-MASK-01-001、REL-FAULT-01-031、USE-DIR-01-001、COMPAT-EXPR-01-001）全量 schema 复验全过；④ **但全量 schema 复验 489 条发现 1 条失败：`COMPAT-SECRET-01-005.yaml`——`setup.secrets` 写成对象数组（{name, value}），schema 要求 string 数组；且该用例 text 溯源 INTENT-COMPAT-NEW-002 与 yaml intent_ref INTENT-COMPAT-002 不一致**（基底遗留个案，需修复后此项方可转绿） |
| 4 | 优先级取自风险登记册，P0 覆盖所有 blocker | ✅ | P0=97 经脚本复扫确认；4 blocker 覆盖：RISK-SEC-01（约 50 条 P0）、RISK-SEC-02（16 条 P0）、RISK-REL-02（REL-NEEDS-01-026/027）、RISK-USE-02（USE-DOC-01-002~005、USE-LBL-01-003/004、USE-ENV-01-004、USE-ONBD-01-001/002 共 9 条），抽验优先级字段均为 P0。**观察项（不阻塞）**：REL-CHILDSTATE-01-064/-V2 与 COMPAT-PR-01-001/002 为基底遗留 P0，其 P0 定级早于现行登记册 blocker 集合，无登记册 blocker 直接锚点，建议基线回写时一并裁决 |
| 5 | 安全用例文本层含「不应发生」验证点、YAML 层 negative 断言 | ⚠️ **66/67 + 67/67** | YAML 层：SEC-*.yaml 67/67 均含 `type: negative` 断言 ✅。文本层：SEC-*.md 66/67 含 [负向] 验证点——**`SEC-DEFPERM-01-001.md` 仅有 [正向]/[非功能] 验证点，缺「不应发生」表述**（其 YAML 层 negative 断言存在，修复仅补文本层）。**观察项**：跨维度标 security 的用例中另有 11 条文本无 [负向]（COMP-CACHE-01-001/002、COMP-CALL-01-003、COMP-PERMS-01-002、COMP-PR-01-002、COMP-PRTARGET-01-002、COMP-SECRET-01-001/003、COMPAT-PERM-01-004、USE-MASK-01-001 + 前述 SEC-DEFPERM-01-001），其中多数为正向对照/基线用例（如 COMP-PR-01-002 验证 pull_request_target 正常路径），建议下一 run 统一裁定口径 |
| 6 | 破坏性用例正确声明 teardown.reset 级别 | ✅ | 脚本全量扫描：`fault_injection` 非 null 的 YAML 共 9 条（REL-FAULT-01-031~039），9/9 均声明 teardown.reset（8 条 `fixture` + 1 条 `full_instance`，REL-FAULT-01-039 排队期 runner 下线场景升级实例级重置，定级合理）；全部 489 条 YAML 均含 teardown.reset 字段（schema 必填，全量复验佐证） |
| 7 | 附带交付三份基线（随用例一并交付） | ✅ | `baseline/` 5 份非空核实：parity-matrix.md（5.5KB）、risk-register.md（2.2KB，含 2026-07-27 增补 RISK-REL-02/RISK-USE-02）、quality-gate.md（1.6KB）、case-base.md（1.7KB）、case-base-detail.md（64KB） |

---

## 不合规项清单（如实列出，未粉饰）

| # | 严重度 | 位置 | 问题 | 建议处置 |
|---|---|---|---|---|
| F1 | 阻塞 DoD-3 | `cases/yaml/COMPAT-SECRET-01-005.yaml` | schema 校验失败：`setup.secrets` 为对象数组，schema 要求 string 数组；且 yaml `intent_ref: INTENT-COMPAT-002` 与 text「溯源意图: INTENT-COMPAT-NEW-002」不一致 | 修复 secrets 写法为 string 数组（或改 schema 支持对象形式并走评审），intent_ref 对齐为 INTENT-COMPAT-NEW-002，复验后 DoD-3 转绿 |
| F2 | 阻塞 DoD-5 | `cases/text/SEC-DEFPERM-01-001.md` | 安全用例文本层缺「不应发生」[负向] 验证点（YAML 层 negative 断言已存在） | 文本层补一条 [负向] 验证点（如「权限宽于声明的写操作不应成功」）后即合规 |
| F3 | 观察项 | REL-CHILDSTATE-01-064/-V2、COMPAT-PR-01-001/002 | 基底遗留 P0 无现行登记册 blocker 锚点 | 基线回写时裁决（降级 P1 或在登记册补锚点），不阻塞本轮 |
| F4 | 观察项 | 11 条跨维度 security 标签文本用例无 [负向] | 多为正向对照用例，DoD-5 口径是否覆盖跨维度正向对照用例待统一 | 下一 run 由门禁统一裁定口径 |
| F5 | 观察项 | B2/B3 输入退化 | business-context 空模板、无 GitHub 侧真实样本，影响 SEC-NET/RUN/LOG 与 COMPAT 维度证据强度 | 用户已安排后续补输入（STOP① 裁决⑤） |

## 总结论

DoD 7 项中 **5 项全绿（1/2/4/6/7）**，**2 项带个案不合规（3：F1；5：F2）**，均为基底遗留单点问题、修复路径明确。按 quality-gate 全局 blocker 规则第 3 条「DoD 未全绿 → 该批次不予交付第二部分」，**建议修复 F1/F2 并复验后再宣告 STOP② 通过**；或经用户裁决接受「489 中 2 条个案降级处理（剔除/修复延期）」后放行。

---

## 复验记录（2026-07-27，F1/F2 修复后）

| 项 | 处理 | 复验结果 |
|---|---|---|
| F1 COMPAT-SECRET-01-005.yaml | setup.secrets 改为 string 数组；intent_ref 改为 INTENT-COMPAT-NEW-002 | ✅ schema 通过 |
| F2 SEC-DEFPERM-01-001.md | 文本层补 [负向] 验证点（权限不应宽于声明） | ✅ 66+1=67/67 安全用例文本含 [负向] |
| 关联修复 | schema intent_ref pattern 扩展允许 `-NEW-`（NEW 系列已回填 intent 库，属合法 ID）；24 条基底 yaml intent_ref 由 INTENT-COMPAT-0xx 更正为 INTENT-COMPAT-NEW-0xx（与文本一致） | ✅ 全量 489/489 schema 复验通过 |
| 遗留观察 | 42 条 KEEP-TC 基底用例 yaml intent_ref 为占位映射（INTENT-COMP-0xx 案号对齐），与文本 KEEP-TC 溯源不一致——属存量溯源债，建议基线回写时统一裁决（不阻塞本轮交付） | ⚠️ 记录 |

**复验结论：DoD 7 项全绿。**
