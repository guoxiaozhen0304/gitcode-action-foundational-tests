## 失败分诊 · SEC-WCMD-01-003 · ATOMGIT_ENV 不被不可信输入污染提权

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 14 — YAML 写入注意事项（block scalar 缩进错误导致 YAML 解析失败）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）— block scalar 内容缩进不一致，INJECTED_VAR=bad 缩进不足:
  # 行 18:           run: |
  # 行 19:             echo "MY_VAR=good
  # 行 20:   INJECTED_VAR=bad" >> $ATOMGIT_ENV
  #     ↑ 仅 2 空格缩进，破坏 block scalar 的缩进上下文，导致 YAML 解析失败

  # 应改为（确保 block scalar 内容统一缩进）:
  - name: Write malicious env
    run: |
      echo "MY_VAR=good
      INJECTED_VAR=bad" >> $ATOMGIT_ENV
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 14a: "写入 workflow YAML 时必须使用 block scalar `|` 格式。" 该用例使用了 `run: |`，但 block scalar 内部多行内容未保持一致的缩进层级，导致 YAML 解析器将 `INJECTED_VAR=bad` 视为独立的顶层键而非 block scalar 内容，触发解析失败。

**置信度**: 高（YAML block scalar 缩进不一致导致解析失败，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — YAML 解析阶段直接失败，无法提交至平台
- **静默性**: 🟢明确报错 — YAML 解析器返回缩进相关错误
- **影响面**: 所有在 block scalar 中使用多行字符串且缩进不一致的工作流
- **综合**: block scalar 内 `INJECTED_VAR=bad` 缩进不足，破坏 YAML 结构
- **是否有规避手段**: 是 — 确保 block scalar 所有行缩进一致，或使用 `run: "echo \"MY_VAR=good\nINJECTED_VAR=bad\" >> $ATOMGIT_ENV"` 单行写法

**建议**:
- 修正 block scalar 缩进，确保所有内容行对齐；或将注入测试改为单行带转义的写法
