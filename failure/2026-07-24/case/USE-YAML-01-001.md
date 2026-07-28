## 失败分诊 · USE-YAML-01-001 · 缺少必填字段 on 时报错应指出具体字段名与位置

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 22 — 未知顶层字段拒绝 / 必填字段缺失
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  jobs:
    bad:
      name: missing on field
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: step
          run: |
            echo "hello"

  # 应改为（添加 on 字段）:
  on:
    workflow_dispatch:
  jobs:
    bad:
      name: missing on field
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: step
          run: |
            echo "hello"
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 22: "GitCode 校验器拒绝任何不在 schema 中的顶层字段。" 缺少 `on` 字段等同于顶层结构不完整——虽然此规则更多描述多余字段，但缺少必填字段 `on` 触发相同的 schema 匹配失败，平台报 `required field 'on' is missing` 或等效错误。规则 8 要求 `on:` 必须是 map 格式也隐含了其必填性。

**置信度**: 高（平台 Schema 要求 on 为必填字段，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回必填字段缺失错误
- **影响面**: 所有不包含 `on` 的 workflow YAML
- **综合**: workflow YAML 缺少必填的 `on` 字段，Schema 校验直接拒绝
- **是否有规避手段**: 是 — 添加 `on: workflow_dispatch:` 块

**建议**:
- 在 `jobs:` 之前添加 `on:\n  workflow_dispatch:` 块
