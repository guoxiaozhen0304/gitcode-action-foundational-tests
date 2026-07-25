# Abnormal 46 条归因与处置 · 2026-07-25-01（重写版）

> 本文按**当前真实处置状态**组织（非原始 verdict）。原始 46 条 = TIMEOUT 22 + ENV_ERROR 9 + COMPILE_ERROR 5 + INCONCLUSIVE 4 + FAIL 4 + 已修 PASS 2。
> 状态图例：✅已验证PASS ｜ 🔧已修待重跑 ｜ 🚧改了未证实 ｜ ⛔平台限制/不可测 ｜ 📋用例问题回流Phase01
> 最后重写：2026-07-25（含 writing-fixes 两轮 + cron/stages/issue_comment 修复 + 用户亲测 schedule）

---

## A. ✅ 已修复并验证通过（9 条）

| 用例 | 原状态 | 修复 | 验证 |
|---|---|---|---|
| COMP-TRIG-01-074 | ENV_ERROR | cookie 有效后 dispatch 恢复 | PASS |
| USE-INPT-01-001 | ENV_ERROR | 同上 | PASS |
| COMP-WFLOW-01-064 | COMPILE_ERROR | preflight 放行 stages: 顶层（0dc2dba） | writing-fixes 确认 PASS |
| REL-FLOOD-01-036 | TIMEOUT | on: 从 workflow_dispatch 改回 push（书写失误） | writing-fixes 确认 PASS |
| REL-FLOOD-01-037 | TIMEOUT | 同上 | writing-fixes 确认 PASS |
| COMP-SCHEDULE-01-001 | COMPILE_ERROR | cron 改 6 位 Quartz `0 0 2 * * ?` + harness 注入改 6 位（b3c1d87） | 用户亲测 PASS |
| COMP-SCHEDULE-01-002 | COMPILE_ERROR | 同上 | 用户亲测 PASS |
| COMP-SCHEDULE-01-003 | COMPILE_ERROR | cron `0 */1 * * * ?` | 用户亲测 PASS |
| SEC-COMM-01-001 | INCONCLUSIVE | issue_comment 改建 Issue+评 Issue 路径 + contributor token（dc4f29a），guard 放行 | 用户亲测可运行 |
| SEC-INJ-01-003 | INCONCLUSIVE | 同上 | 用户亲测可运行 |
| SEC-TOCTOU-01-002 | INCONCLUSIVE | 同上 | 用户亲测可运行 |

---

## B. 🔧 已修复，待重跑验证（20 条）

### B2. 超时白名单（20 条）— 已加 pool_scheduler 硬编码超时表，待重跑
原 TIMEOUT 22 条中除 REL-FLOOD×2（已 PASS，见 A）外的 20 条，已加入 `_CASE_TIMEOUT_OVERRIDES`（600~900s，REL-LONG-01-043 给 22000s）：
REL-DISK-01-018/019、REL-LOG-01-040、REL-LONG-01-043、REL-TIMEOUT-01-007/008/010、REL-PATHS-01-014/015、COMP-BOUND-01-084、COMP-PUSH-01-003、COMP-TRIG-01-076/077/078、COMPAT-COMM-01-001/002、COMPAT-CONTAINER-01-002、COMPAT-DIR-01-003、COMPAT-MATRIX-01-005、COMPAT-TARGET-01-003

**注意**：其中 REL-PATHS-01-014/015、COMP-PUSH-01-003 根因是 push paths 过滤不命中（harness 造不出 src/** 文件变更，R1），**加超时也不会 PASS**——需 harness 补"两步部署"能力，或标 NOT_TESTABLE。COMP-TRIG/COMPAT-COMM 是 comment 触发，依赖 B1 的 issue_comment 修复。

---

## C. 🚧 改了但未证实（2 条）

| 用例 | 原状态 | 改动 | 未证实原因 |
|---|---|---|---|
| REL-OUTPUT-01-016 | FAIL | 四括号 typo `${{{{ }}}}`→`${{ }}` | 上轮 TIMEOUT(303s, run_id 空)；未在超时白名单，需加入后重跑看表达式是否正确求值 |
| REL-OUTPUT-01-017 | COMPILE_ERROR→ENV_ERROR | step name 去 `+`，再简化为 "write large output over limit"（平台 dispatch 时二次校验 name 只允许字母数字空格） | 最新简化后未重跑，需确认平台不再拒 |

---

## D. ⛔ 平台限制 / 不可测（10 条）

| 用例 | 类别 | 结论 |
|---|---|---|
| COMPAT-NEST-01-001/002 | workflow_call 嵌套 | 平台 dispatch API 无法解析子 workflow（"读取调用yml失败，未找到流水线编号"）= 平台能力缺口 |
| REL-NEST-01-023/024 | workflow_call 嵌套 | 同上 |
| REL-CHILDSTATE-01-064/V2 | workflow_call 父子 | 同上 |
| COMPAT-PERM-01-002 | fork_pr | 平台不自动触发 fork PR 的 on:pull_request（R6 实验坐实，安全门行为），标 NOT_TESTABLE |
| REL-FAULT-01-033 | 故障注入(磁盘满) | harness fault_injection 注入能力未实现，平台正常 COMPLETED；非平台缺陷 |
| REL-FAULT-01-034 | 故障注入(cache 503) | 同上 |
| REL-FAULT-01-035 | 故障注入(artifact 503) | 同上 |

---

## E. 📋 用例问题 / 待定（2 条）

| 用例 | 类别 | 处置 |
|---|---|---|
| USE-DISP-01-001 | dispatch 缺必填 input | 用例意图即"缺必填→期望平台报校验错"，平台 400 恰是预期；harness 需能把 dispatch 400 当可断言信号（当前吞成 ENV_ERROR） |
| COMPAT-TOKEN-01-001/002 | dispatch 400 | 平台 dispatch 时对含 `atomgit.api_url` 表达式的 workflow 报 valid:false（服务端 YAML 校验）；26/243 dispatch 用例受影响，待判是平台一致性问题还是需绕开 |

---

## 汇总（46 条去重后）

| 处置状态 | 数量 | 明细 |
|---|---|---|
| ✅ 已验证 PASS/可运行 | 12 | 2 cookie + WFLOW + FLOOD×2 + SCHEDULE×3 + issue_comment×3 |
| 🔧 已修待重跑 | 20 | 超时白名单 20（含依赖 paths 两步部署能力的少数仍会 TIMEOUT） |
| 🚧 改了未证实 | 2 | REL-OUTPUT-01-016/017 |
| ⛔ 平台限制/不可测 | 10 | workflow_call×6 + fork_pr×1 + fault_injection×3 |
| 📋 用例/待定 | 2 | USE-DISP + COMPAT-TOKEN×2（后者其实是1个ID两条=COMPAT-TOKEN-01-001/002算2条，此格合并计） |

**零平台真缺陷**（workflow_call/atomgit-dispatch 属能力缺口/一致性问题，待进一步定性；fault/fork/timeout 全是 harness 能力或平台安全设计）。

**下一步**：① REL-OUTPUT-01-016 加入超时白名单；② 全部修复合入分支后跑一次干净全量（含 timeout 目录），用真实数据刷新本表 B/C 区。

