## 失败分诊 · USE-YAML-01-002 · YAML 缩进错误时报错应指出具体行号与列号

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 14 — YAML 写入注意事项（步骤缩进不一致导致 YAML 解析失败）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）— steps 列表中第 2 个 step 缩进错误:
  # 行 22:       - name: step one
  # 行 23:         run: |
  # 行 24:           echo "hello"
  # 行 25:        - name: step two      ← 仅 7 空格，与 step one 的 6 空格不一致
  # 行 26:          run: |
  # 行 27:            echo "world"

  # 应改为（统一缩进）:
  steps:
    - name: step one
      run: |
        echo "hello"
    - name: step two
      run: |
        echo "world"
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 14: "YAML 写入注意事项 — workflow 字段用 block scalar `|` 写入时，缩进必须正确。" 该用例的 workflow block scalar 内，steps 列表中第 1 个 step 的 `- name:` 缩进与第 2 个 step 的 `- name:` 缩进不一致（7 空格 vs 6 空格），YAML 解析器无法正确识别列表结构，报缩进错误。

**置信度**: 高（YAML 列表元素缩进不一致导致解析失败，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — YAML 解析阶段直接失败，无法提交至平台
- **静默性**: 🟢明确报错 — YAML 解析器返回缩进/格式错误
- **影响面**: 所有 YAML 缩进不一致的工作流
- **综合**: steps 列表中第二个 `- name` 缩进与第一个不一致，破坏了 YAML 列表结构
- **是否有规避手段**: 是 — 统一 steps 列表所有元素的缩进层级

**建议**:
- 修正第 2 个 step 的 `- name` 缩进，使其与第 1 个 step 的缩进一致（通常为 6 空格或 8 空格取决于上下文）
