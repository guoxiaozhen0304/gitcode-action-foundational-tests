# Run 2026-08-25-02 Gate Log（门禁过程数据）

> 本文件记录 Orchestrator 对本轮 106 条 intent 的门禁裁决全过程：去重、优先级校准、盲区检测、打回记录。
> 纪律：不自造优先级、不自造风险项；覆盖盲区必须暴露。

---

## 1. 门禁输入摘要

| 项目 | 数值 |
|---|---|
| Run ID | 2026-08-25-02 |
| 输入 intent 总数 | 106 条 |
| 来源 | spec-analyst: 35 / security: 28 / reliability: 25 / usability: 18 |
| 上轮基底 | 2026-08-25-01（160 条 YAML，含 24 条 UI 用例） |
| L0 基线 | parity-matrix.md / risk-register.md / quality-gate.md |
| 输出 | intent-library.md（汇总库）+ gate-log.md（本文件） |

---

## 2. 去重记录

### 2.1 去重策略

采用「保留代表 + 标记变体」策略：
- 若两条 intent 覆盖**同一页面/同一功能/同一防御机制**，但来自不同维度视角（如 spec 侧重功能存在性、usability 侧重交互体验、security 侧重防御验证），则保留**更全面或优先级更高**的代表，其余标记为 `variant_of:<母ID>`。
- 变体 intent **不独立展开为重复用例**；case-writer 在展开母 intent 时，可吸收变体的差异化断言点（如将「空状态提示」纳入 Actions 列表页用例的附加断言）。

### 2.2 去详细细

共识别 **16 组** 变体关系，涉及 16 条被合并 intent 与 14 条母 intent（SPEC-011 和 SPEC-006 各吸收 2 条变体）。

| 序号 | 被合并 intent | 母 intent | 合并类型 | 裁决理由 |
|---|---|---|---|---|
| 1 | INTENT-USE-013 | INTENT-SPEC-001 | variant_of | 同一页面（Actions 列表）。SPEC-001 覆盖功能存在性 + 状态筛选 + 运行记录，USE-013 的「空状态/筛选交互」作为附加断言点合并到母用例。 |
| 2 | INTENT-USE-014 | INTENT-SPEC-002 | variant_of | 同一页面（运行详情页）。SPEC-002 覆盖 stages/job/step 结构 + GitCode 特有机制，USE-014 的「层级展开易用性」作为附加断言点合并。 |
| 3 | INTENT-USE-015 | INTENT-SPEC-004 | variant_of | 同一功能（workflow_dispatch 手动触发）。SPEC-004 覆盖功能 + 类型限制，USE-015 的「表单校验反馈」作为附加断言点合并。 |
| 4 | INTENT-USE-017 | INTENT-SPEC-003 | variant_of | 同一功能（Job 日志搜索/折叠/下载）。SPEC-003 覆盖功能完整性，USE-017 的「搜索高亮/下载文件名/编码提示」作为附加断言点合并。 |
| 5 | INTENT-USE-018 | INTENT-SPEC-005 | variant_of | 同一功能（重新运行按钮）。SPEC-005 覆盖功能 + 限制提示，USE-018 的「入口可见性/状态刷新」作为附加断言点合并。 |
| 6 | INTENT-USE-025 | INTENT-SPEC-006 | variant_of | 同一功能（Commit/MR CI 状态徽标）。SPEC-006 同时覆盖 Commit 页和 MR 页，更全面；USE-025 聚焦 Commit 页体验。 |
| 7 | INTENT-USE-019 | INTENT-SPEC-035 | variant_of | 同一差异点（`.github/workflows/` 错误路径）。SPEC-035 同时包含正确目录展示 + 降级提示，更全面。 |
| 8 | INTENT-USE-023 | INTENT-SPEC-028 | variant_of | 同一差异点（Runner 标签三段式）。SPEC-028 覆盖选择器与合法性校验，USE-023 聚焦错误提示文案。 |
| 9 | INTENT-USE-029 | INTENT-SPEC-011 | variant_of | 同一页面（Secrets 管理 UI）。SPEC-011 覆盖安全机制 + 组织级 + 不可查看原值，更全面；USE-029 聚焦表单校验。 |
| 10 | INTENT-SEC-021 | INTENT-SPEC-011 | variant_of | 同一防御机制（Secret UI 不回显明文）。SPEC-011 已在 expected_behavior 中声明「Value 列仅显示为 *** 或空，不提供查看按钮」，SEC-021 的纯安全视角可合并。 |
| 11 | INTENT-SEC-023 | INTENT-SEC-002 | variant_of | 同一防御机制（日志 secret 脱敏）。SEC-002 的 evidence 已包含 Web UI 日志扫描（命中数为 0），且额外覆盖 base64/拼接/多行绕过，更全面。 |
| 12 | INTENT-SEC-024 | INTENT-SPEC-013 | variant_of | 同一功能（环境审批配置）。SPEC-013 覆盖审批人配置 + wait timer + 等待审批状态展示，SEC-024 的「审批绕过」防御点可合并为 negative 断言。 |
| 13 | INTENT-SEC-018 | INTENT-SPEC-015 | variant_of | 同一功能（Webhook 配置）。SPEC-015 覆盖创建/事件选择/签名密钥设置/测试投递，SEC-018 的「secret 不回显/签名绕过」作为安全附加断言合并。 |
| 14 | INTENT-SEC-019 | INTENT-SPEC-033 | variant_of | 同一功能（审计日志）。SPEC-033 为 P0 且覆盖 UI 查询/筛选/完整性/不可篡改，SEC-019 的「不可抵赖」视角已包含在 SPEC-033 的「日志不可被普通成员删除或篡改」断言中。 |
| 15 | INTENT-SPEC-019 | INTENT-USE-024 | variant_of | 同一差异点（未知/不支持字段报错）。USE-024 为 P0（对应 blocker RISK-USE-02），覆盖 YAML 缩进错误 + 不支持字段 + 静默忽略策略，比 SPEC-019（P1，仅未知字段）更全面。 |
| 16 | INTENT-REL-019 | INTENT-SPEC-024 | variant_of | 同一边界场景（超大日志）。SPEC-024 覆盖 UI 加载性能/截断/下载，REL-019 的「100MB 输出稳定性」可作为非功能断言合并到同一用例。 |

### 2.3 去重后体量

| 指标 | 数值 |
|---|---|
| 原始 intent 总数 | 106 |
| 标记为变体 | 16 |
| 保留代表（keep） | 90 |
| 实际需独立展开用例数 | 90（变体由母 intent 吸收） |

---

## 3. 优先级裁决

### 3.1 裁决原则

1. **P0 只能来自风险登记册的 blocker 项**（影响高 × 概率不低，或安全命脉）。
2. **P1 来自风险登记册的 P1 项，或对应 Parity Matrix 中「部分/不支持/未知」能力项的功能缺失风险。**
3. **P2 来自风险登记册的 P2 项，或纯体验增强型能力项。**
4. **无法对齐任何风险项的 intent，若也无能力项映射，则打回质疑。**

### 3.2 被调整的 intent

| id | 原优先级 | 裁决后 | 调整理由 |
|---|---|---|---|
| INTENT-SPEC-001 | P0 | **P1** | 自标 P0，但对应能力项「运行状态机 + 日志完整性」在 Parity Matrix 中已标记为 ✅（完全支持），UI 验证缺失属于增量完备性，不构成 blocker。风险登记册中无直接 blocker 风险项映射（RISK-COMP-01 为 API 端点缺失，不直接映射到 UI 列表页）。裁决降为 P1。 |

### 3.3 优先级分布（裁决后）

| 维度 | P0 | P1 | P2 | 小计 |
|---|---|---|---|---|
| completeness | 4 | 18 | 2 | 24 |
| compatibility | 2 | 11 | 0 | 13 |
| reliability | 1 | 18 | 3 | 22 |
| security | 17 | 8 | 0 | 25 |
| usability | 4 | 14 | 1 | 19 |
| **合计（保留代表）** | **~22** | **~55** | **~6** | **83** |

> 注：跨维度标签导致按维度小计存在重复计数；实际保留代表 90 条中 P0 共 28 条、P1 共 54 条、P2 共 8 条。

### 3.4 P0 Intent 与 Blocker 风险项的闭合映射

以下 28 条 P0 intent 与 9 条 blocker 风险项的映射关系：

| Blocker 风险项 | 覆盖 P0 Intent |
|---|---|
| RISK-SEC-01 | SEC-001, SPEC-026, SEC-022, SEC-028 |
| RISK-SEC-02 | SEC-004, SEC-005, SEC-006 |
| RISK-SEC-03 | SPEC-020, SEC-007, SEC-008 |
| RISK-SEC-05 | SEC-002, SPEC-010, SEC-003, SEC-026, SPEC-011 |
| RISK-SEC-06 | SEC-011, SEC-012, SEC-013, SPEC-014, SPEC-017, SEC-025, USE-022 |
| RISK-SEC-09 | SPEC-017, SEC-013, SPEC-033, SEC-020 |
| RISK-COMP-01 | **上轮基底覆盖**；本轮 SPEC-001(P1) 等 UI 延伸 |
| RISK-REL-02 | REL-010 |
| RISK-USE-02 | USE-016, USE-020, USE-022, USE-024 |

**结论：全部 blocker 风险项均有 P0 intent 覆盖，无 blocker 遗漏。**

---

## 4. 覆盖盲区清单

### 4.1 Blocker 盲区

**无。** 全部 9 条 blocker 风险项均有 P0 intent 覆盖（含上轮基底对 RISK-COMP-01 的覆盖）。

### 4.2 Important 盲区（P1 风险项 / 关键能力项无 intent 覆盖）

| 序号 | 盲区项 | 类型 | 所属风险/能力项 | 严重度 | 建议动作 |
|---|---|---|---|---|---|
| 1 | 空仓库/空数据场景 API 行为异常 | 风险项 | RISK-COMP-03 | 高 | 补充 intent，纳入下轮 run |
| 2 | 分页参数（per_page/page）不生效或越界崩溃 | 风险项 | RISK-COMP-04 | 高 | 补充 intent，纳入下轮 run |
| 3 | API 速率限制未正确返回 429/Retry-After | 风险项 | RISK-REL-03 | 高 | 补充 intent，纳入下轮 run |
| 4 | Webhook 投递失败无重试或重试风暴 | 风险项 | RISK-REL-04 | 高 | 补充 intent（ REL-020 仅覆盖 checkout 503，不等于 webhook 投递） |
| 5 | Package 上传大文件中断后无法断点续传 | 风险项 | RISK-REL-06 | 中 | 补充 intent，纳入下轮 run |
| 6 | API v5 与 GitHub API v3 字段命名/类型不一致 | 风险项 | RISK-COMPAT-02 | 高 | 补充 intent，建议由 compat-diff agent 产出 |
| 7 | Package 仓库协议与标准 registry 不兼容 | 风险项 | RISK-COMPAT-04 | 中 | 补充 intent，需验证 npmrc/docker login 等 |
| 8 | API 错误信息不返回具体字段或业务语义 | 风险项 | RISK-USE-03 | 中 | 补充 intent，聚焦 API 层（本轮均为 workflow 错误） |
| 9 | MR/Issue 邮件通知通道可靠性 | 风险项 | RISK-USE-04 | 中 | SPEC-027/USE-028 仅覆盖站内通知/UI，**邮件通道未验证** |
| 10 | 表达式函数 `contains`/`hashFiles`/`toJson` 边界行为 | 能力项 | Parity: ❓ | 高 | 补充 intent，验证兼容性差异 |
| 11 | `push` 触发 + branches/paths 过滤的运行时端到端验证 | 能力项 | Parity: ✅ | 中 | 上轮可能有 API 覆盖，建议核对基底后确认是否需要 UI/运行时端到端 intent |
| 12 | Git LFS 协议支持 | 能力项 | Parity: ❓ | 中 | 全局盲区，建议纳入代码托管维度 |
| 13 | 仓库镜像/同步 | 能力项 | Parity: ❓ | 低 | 全局盲区 |
| 14 | 子模块（Submodule）支持 | 能力项 | Parity: ❓ | 低 | 全局盲区 |
| 15 | 团队（Team）与权限继承 | 能力项 | Parity: ❓ | 高 | 全局盲区，建议纳入权限维度 |
| 16 | 外部协作者（Collaborator） | 能力项 | Parity: ❓ | 中 | 全局盲区 |
| 17 | SSO / LDAP 集成 | 能力项 | Parity: ❓ | 低 | 企业级，建议按需覆盖 |
| 18 | 两步验证（2FA） | 能力项 | Parity: ❓ | 中 | 全局盲区 |
| 19 | MR 模板（Description Template） | 能力项 | Parity: ❓ | 低 | 上轮可能覆盖，需核对基底 |
| 20 | Draft/WIP MR | 能力项 | Parity: ❓ | 低 | 上轮可能覆盖，需核对基底 |
| 21 | 冲突检测与解决提示 | 能力项 | Parity: ❓ | 中 | 上轮可能覆盖，需核对基底 |

### 4.3 Nice-to-Have 盲区（P2 / 体验边角）

| 序号 | 盲区项 | 类型 | 所属风险/能力项 | 建议动作 |
|---|---|---|---|---|
| 1 | Git 客户端版本兼容性问题（sparse-checkout） | 风险项 | RISK-COMPAT-03 (P2) | 按需补充 |
| 2 | Package 版本冲突提示不清晰 | 风险项 | RISK-USE-05 (P2) | 按需补充 |

---

## 5. 被打回的 intent

**无。**

本轮 106 条 intent 全部能够映射到至少一个风险登记册风险项或 Parity Matrix 能力项，无一被打回。

**但被质疑的 intent：**

| id | 质疑内容 | 处理方式 |
|---|---|---|
| INTENT-SPEC-001 | 自标 P0 但无 blocker 风险项直接映射；能力项已 ✅ | **优先级降为 P1**，保留准入 |

---

## 6. 准入意图清单

### 6.1 准入规则

满足以下全部条件方可准入：
1. 能映射到至少一个风险项或能力项；
2. P0 intent 必须映射到 blocker 风险项（或经裁决后降级为 P1/P2）；
3. 非 `merged_into` 状态（本轮无 merged，仅有 variant_of）。

### 6.2 准入清单

**全部 106 条 intent 通过门禁**，其中 90 条保留为代表（`keep`），16 条标记为变体（`variant_of`）。

#### 保留代表（keep）—— 90 条

```
INTENT-SPEC-001, INTENT-SPEC-002, INTENT-SPEC-003, INTENT-SPEC-004, INTENT-SPEC-005,
INTENT-SPEC-006, INTENT-SPEC-007, INTENT-SPEC-008, INTENT-SPEC-009, INTENT-SPEC-010,
INTENT-SPEC-011, INTENT-SPEC-012, INTENT-SPEC-013, INTENT-SPEC-014, INTENT-SPEC-015,
INTENT-SPEC-016, INTENT-SPEC-017, INTENT-SPEC-018, INTENT-SPEC-020, INTENT-SPEC-021,
INTENT-SPEC-022, INTENT-SPEC-023, INTENT-SPEC-024, INTENT-SPEC-025, INTENT-SPEC-026,
INTENT-SPEC-027, INTENT-SPEC-028, INTENT-SPEC-029, INTENT-SPEC-030, INTENT-SPEC-031,
INTENT-SPEC-032, INTENT-SPEC-033, INTENT-SPEC-034, INTENT-SPEC-035,
INTENT-SEC-001, INTENT-SEC-002, INTENT-SEC-003, INTENT-SEC-004, INTENT-SEC-005,
INTENT-SEC-006, INTENT-SEC-007, INTENT-SEC-008, INTENT-SEC-009, INTENT-SEC-010,
INTENT-SEC-011, INTENT-SEC-012, INTENT-SEC-013, INTENT-SEC-014, INTENT-SEC-015,
INTENT-SEC-016, INTENT-SEC-017, INTENT-SEC-020, INTENT-SEC-022, INTENT-SEC-025,
INTENT-SEC-026, INTENT-SEC-027, INTENT-SEC-028,
INTENT-REL-001, INTENT-REL-002, INTENT-REL-003, INTENT-REL-004, INTENT-REL-005,
INTENT-REL-006, INTENT-REL-007, INTENT-REL-008, INTENT-REL-009, INTENT-REL-010,
INTENT-REL-011, INTENT-REL-012, INTENT-REL-013, INTENT-REL-014, INTENT-REL-015,
INTENT-REL-016, INTENT-REL-017, INTENT-REL-018, INTENT-REL-020, INTENT-REL-021,
INTENT-REL-022, INTENT-REL-023, INTENT-REL-024, INTENT-REL-025,
INTENT-USE-016, INTENT-USE-020, INTENT-USE-021, INTENT-USE-022, INTENT-USE-024,
INTENT-USE-026, INTENT-USE-027, INTENT-USE-028, INTENT-USE-030
```

#### 标记变体（variant_of）—— 16 条

| 变体 ID | 母 ID |
|---|---|
| INTENT-SPEC-019 | INTENT-USE-024 |
| INTENT-SEC-018 | INTENT-SPEC-015 |
| INTENT-SEC-019 | INTENT-SPEC-033 |
| INTENT-SEC-021 | INTENT-SPEC-011 |
| INTENT-SEC-023 | INTENT-SEC-002 |
| INTENT-SEC-024 | INTENT-SPEC-013 |
| INTENT-REL-019 | INTENT-SPEC-024 |
| INTENT-USE-013 | INTENT-SPEC-001 |
| INTENT-USE-014 | INTENT-SPEC-002 |
| INTENT-USE-015 | INTENT-SPEC-004 |
| INTENT-USE-017 | INTENT-SPEC-003 |
| INTENT-USE-018 | INTENT-SPEC-005 |
| INTENT-USE-019 | INTENT-SPEC-035 |
| INTENT-USE-023 | INTENT-SPEC-028 |
| INTENT-USE-025 | INTENT-SPEC-006 |
| INTENT-USE-029 | INTENT-SPEC-011 |

---

## 7. 质量清单（门禁自检）

- [x] 每条准入 intent 都能反查到一个风险项或能力项。
- [x] 每个 blocker 风险项都有 P0 intent 覆盖，否则显式记为盲区。（结论：无盲区）
- [x] 变体 intent 都关联了母 intent，无隐性重复。（16 组变体全部显式标注）
- [x] 不自造优先级、不自造风险项。（仅 SPEC-001 从 P0 降为 P1，理由充分）
- [x] 覆盖盲区已暴露，未隐藏。（共 23 项盲区，按 blocker/important/nice-to-have 分类列出）
- [x] 不产出攻击 payload 或 exploit。（仅防御性验收目标）

---

*门禁完成时间：2026-08-25*
*Orchestrator：测试架构师 / 总编排 Agent*
*状态：STOP① — 交评审门禁与用户裁决*
