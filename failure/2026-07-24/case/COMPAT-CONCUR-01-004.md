## 失败分诊 · COMPAT-CONCUR-01-004 · concurrency preemption events 越界时行为差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `concurrency.preemption.events` 使用了数值 `11` 而非数组格式 `[mr_id]`，违反类型约束
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 19a（`preemption.events` 仅允许 `[mr_id]`）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    concurrency:
      group: test-preemption-events
      preemption:
        enable: true
        events: 11                      # 应为数组 [mr_id]，不是数值
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 19a: "Concurrency `preemption.events` 仅允许 `[mr_id]`"
  - `events` 期望数组格式且元素值必须在 `[mr_id]` 集合中

**置信度**: 高（`events: 11` 类型不匹配且值不在允许集合中）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回类型/值错误
- **影响面**: 所有在 `preemption.events` 中使用非法值的配置
- **综合**: 负向测试 events 越界值，平台正确拒绝
- **是否有规避手段**: 否 — 此用例目的即为验证 events 越界被拒绝，标记为 `expected_rejection`

**建议**:
- 此用例为预期被拒绝的负向测试
- 标注为 `expected_rejection`，记录平台报错信息
- 若需正向测试 preemption，使用合规配置 `events: [mr_id]`
