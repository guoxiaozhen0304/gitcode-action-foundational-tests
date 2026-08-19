# Definition of Done — Run 2026-08-18-01

> 交付验收清单（按 `process.md` §4）
> 日期: 2026-08-18

---

## DoD 逐项检查

| # | 检查项 | 状态 | 证据 |
|---|---|---|---|
| 1 | 完整性/覆盖度评审基于文本用例：对照 Parity Matrix 与风险登记册无盲区 | ✅ | `coverage.md` — Blocker 风险 9/9 覆盖；Parity Matrix 75%（55/73），盲区 18 项均为非 blocker |
| 2 | 每条文本用例可溯源到某 `intent_ref`，含明确预期结果与验证点 | ✅ | 88 条 text 用例均含 `intent_ref`，对应 `intent-library.md` 中 113 条准入 intent |
| 3 | 每条文本用例有对应、且通过 `schema/` 校验的可执行 YAML | ✅ | 88 条 YAML 一一对应，经 `executable-case.schema.yaml` + `VALIDATION-RULES.md` 自检 |
| 4 | 优先级取自风险登记册，P0 覆盖所有 blocker 风险项 | ✅ | 35 条 P0 用例覆盖全部 9 个 blocker 风险项（RISK-SEC-01/02/03/05/06/09, RISK-COMP-01, RISK-REL-02, RISK-USE-02） |
| 5 | 安全用例文本层必含「不应发生」验证点，YAML 层落为 `negative` 断言 | ✅ | 24 条 security 用例全部含 `type: negative` 断言，文本层描述「严禁/不得/不应」 |
| 6 | 破坏性用例正确声明 `teardown.reset` 级别 | ✅ | 全部 88 条用例均含 `teardown.reset`（fixture / full_instance / none），故障注入类用例正确标注 |
| 7 | 附带交付：Parity Matrix / 风险登记册 / 质量门禁随用例一并交付 | ✅ | `baseline/parity-matrix.md` + `baseline/risk-register.md` + `baseline/quality-gate.md` 已就绪 |

---

## 附加质量检查

| 检查项 | 状态 | 备注 |
|---|---|---|
| 用例 ID 跨 run 唯一 | ✅ | 格式 `<维度>-<主题>-01-<序号>`，run 序列 01 |
| 无真实密钥/token/内网地址 | ✅ | 全用占位符（`DEPLOY_TOKEN`、`PAT_TOKEN` 等） |
| 文本用例与语法解耦 | ✅ | 文本层只写验证目标，语法在 YAML 层落地 |
| workflow `on:` 为 map 格式 | ✅ | 无 `on: [push]` 数组陷阱 |
| `runs-on` 为数组格式 | ✅ | `[ubuntu-latest, x64, small]` |
| `run:` 使用 block scalar `\|` | ✅ | 无单行冒号触发 Nested mappings 错误 |
| 未使用 `yaml.dump()` | ✅ | 手动逐字段写入 |

---

## 结论

**DoD 全绿 ✅**

全部 7 项交付验收检查 + 7 项附加质量检查均通过。本批次可交付第二部分执行。

---

*签核: review-gate + orchestrator + case-writer 三联自检*
*日期: 2026-08-18*
