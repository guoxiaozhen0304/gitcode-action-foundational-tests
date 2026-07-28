## 失败分诊 · REL-STAGES-01-029 · stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 17 — `stages` 必须是 map，不是数组；stage 名必须为 `default`
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  stages:
    test_stage:
      fail_fast: true
      jobs:
        job_a: ...
        job_b: ...
        job_c: ...
    next_stage:
      jobs:
        job_d: ...

  # 应改为（stage 名使用 default）:
  stages:
    default:
      jobs:
        test:
          name: stage job test
          runs-on: [ubuntu-latest, x64, small]
          steps: [...]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 17: "GitCode 的 `stages` 字段必须是 map 格式（`stages: {default: {jobs: {...}}}`）。" 平台 schema 仅接受 `default` 作为 stage 的名称键；使用 `test_stage` / `next_stage` 等自定义键名会被平台视为 schema 不匹配。

**置信度**: 高（平台 Schema 明确要求 default 键名，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 schema 匹配错误（未知 stage 名）
- **影响面**: 所有使用自定义 stage 名称或 fail_fast 的工作流
- **综合**: stages 仅接受 `default` 作为 stage 键名，`test_stage`/`next_stage` 不被识别
- **是否有规避手段**: 是 — 将所有 job 放入 `stages: default: jobs:` 下，用 needs 控制执行顺序

**建议**:
- 将 stages 改为单一 `default` 节点，使用 `needs` 字段在 jobs 间建立依赖关系来模拟阶段语义
