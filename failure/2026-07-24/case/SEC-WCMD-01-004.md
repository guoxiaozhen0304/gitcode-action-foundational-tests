## 失败分诊 · SEC-WCMD-01-004 · ATOMGIT_OUTPUT 不被不可信输入污染提权

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 14 — YAML 写入注意事项（block scalar 缩进错误导致 YAML 解析失败）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）— block scalar 内容缩进不一致，hijacked=bad 缩进不足:
  # 行 19:           run: |
  # 行 20:             echo "result=good
  # 行 21:   hijacked=bad" >> $ATOMGIT_OUTPUT
  #     ↑ 仅 2 空格缩进，破坏 block scalar 的缩进上下文

  # 应改为（确保 block scalar 内容统一缩进）:
  - name: Write malicious output
    id: bad
    run: |
      echo "result=good
      hijacked=bad" >> $ATOMGIT_OUTPUT
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 14a: "写入 workflow YAML 时必须使用 block scalar `|` 格式。" 该用例使用了 `run: |`，但 block scalar 内部第二行 `hijacked=bad` 缩进仅 2 空格而非与首行一致的缩进层级，YAML 解析器无法正确识别 block scalar 边界，导致解析失败。

**置信度**: 高（YAML block scalar 缩进不一致导致解析失败，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — YAML 解析阶段直接失败，无法提交至平台
- **静默性**: 🟢明确报错 — YAML 解析器返回缩进相关错误
- **影响面**: 所有在 block scalar 中使用多行 echo 且缩进不一致的工作流
- **综合**: block scalar 内 `hijacked=bad` 缩进不足，破坏 YAML 结构
- **是否有规避手段**: 是 — 统一 block scalar 内容缩进，或改用单行 `run:` 写法

**建议**:
- 修正 block scalar 内所有行缩进至与首行一致
