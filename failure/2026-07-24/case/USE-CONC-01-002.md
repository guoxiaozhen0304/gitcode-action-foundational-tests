## 失败分诊 · USE-CONC-01-002 · concurrency.max 配置 -1 时报错应提示有效范围

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 19b — `concurrency.max` ≥ 1
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  concurrency:
    max: -1
    exceed-action: QUEUE

  # 应改为（max 取值 ≥ 1）:
  concurrency:
    max: 1
    exceed-action: QUEUE
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 19b: "`concurrency.max` ≥ 1。`concurrency.max` 不得小于 1，报 `值不能小于1`。"

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `值不能小于1` 错误
- **影响面**: 所有 concurrency.max 配置为负数的工作流
- **综合**: `max: -1` 违反 ≥1 的约束，Schema 校验拒绝
- **是否有规避手段**: 是 — 改为 `max: 1` 或更大正整数

**建议**:
- 将 `max: -1` 替换为 `max: 1` 或目标并发数；负值测试通过期望 Schema 拒绝来验证
