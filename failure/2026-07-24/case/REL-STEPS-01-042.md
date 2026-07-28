## 失败分诊 · REL-STEPS-01-042 · 超多 step——单 job 内 50 个 step 应全部串行执行无丢失

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 5 — Job steps 数量限制 ≤ 16
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  jobs:
    test:
      name: steps count 50 test
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: step 01
          ...
        ... (共 50 个 step)

  # 应改为（拆分为 ≤16 steps 的多个 job）:
  jobs:
    test-a:
      name: steps 1-16
      runs-on: [ubuntu-latest, x64, small]
      steps: [...16 steps]
    test-b:
      name: steps 17-32
      runs-on: [ubuntu-latest, x64, small]
      steps: [...16 steps]
    test-c:
      name: steps 33-48
      runs-on: [ubuntu-latest, x64, small]
      steps: [...16 steps]
    test-d:
      name: steps 49-50
      runs-on: [ubuntu-latest, x64, small]
      steps: [...2 steps]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 5: "Job steps 数量限制 ≤ 16。超出 16 个 step 必须拆分 job（加 `-b`、`-c` 后缀）。"

**置信度**: 高（平台明确限制 ≤16 steps/job，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 steps 数量超限错误
- **影响面**: 所有单个 job 内 steps > 16 的工作流
- **综合**: 50 个 step 远超平台 16 个 step 上限，YAML 校验直接拒绝
- **是否有规避手段**: 是 — 拆分为多个 job（每个 ≤16 steps），用 needs 串联

**建议**:
- 将 50 个 step 拆分为至少 4 个 job（3×16 + 1×2），通过 `needs` 保证串行执行顺序
