# DoD Checklist — Run 2026-08-25-01

> Definition of Done 验收表（process.md §4）

## 完整性/覆盖度评审

- [x] 对照 Parity Matrix 与风险登记册无盲区 → coverage.md 有据
- [x] 每条文本用例可溯源到 `intent_ref`，含明确预期结果与验证点
- [x] 每条文本用例有对应、且通过 schema 校验的可执行 YAML
- [x] 优先级取自风险登记册，P0 覆盖所有 blocker 风险项
- [x] 安全用例文本层必含「不应发生」验证点，YAML 层落为 `negative` 断言（本轮无新增安全用例，上轮已覆盖）
- [x] 破坏性用例正确声明 `teardown.reset` 级别（本轮 UI 用例均为 `none`，无破坏性操作）
- [x] 附带交付：Parity Matrix / 风险登记册 / 质量门禁随用例一并交付

## Schema 合规

- [x] 全部 159 条 YAML 通过 `executable-case.schema.yaml` 校验
- [x] `test_type=ui` 的 24 条用例均包含 `ui` 节点，无 `workflow`/`api`/`git` 混用
- [x] ID 全局唯一，跨 run 不碰撞

## 溯源链闭合

- [x] 24 条准入 intent → 24 条文本用例 → 24 条 YAML（intent_ref 完整）
- [x] 3 条已有 UI 用例（UI-ISSUE-01-002 / UI-MR-01-002 / UI-MR-01-003）映射到对应 intent，不重复生成

## 交付物清单

| 产物 | 路径 | 状态 |
|---|---|---|
| 文本用例（24 条）| `cases/text/UI-*.md` | ✅ |
| 可执行 YAML（24 条）| `cases/yaml/UI-*.yaml` | ✅ |
| 意图库 | `intent-library.md` | ✅ |
| 覆盖度报告 | `coverage.md` | ✅ |
| 全集清单 | `case-manifest.md` | ✅ |
| 门禁日志 | `gate-log.md`（含于 intent-library.md）| ✅ |

## 结论

**DoD 全绿，本批次可交付 Phase 02。**
