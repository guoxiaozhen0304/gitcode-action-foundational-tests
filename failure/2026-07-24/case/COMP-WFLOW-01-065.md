## 失败分诊 · COMP-WFLOW-01-065 · workflow post 后处理阶段字段验证

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `post` 块（含 `post.run_always` 和 `post.steps`）不为平台支持，报 `unknown property`
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 20（`services` / `post.steps` 不支持）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    post:
      run_always: true
      steps:
        - name: Post notification
          run: |
            echo "post_done"
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 20: "GitCode 平台不支持 GitHub Actions 的 `jobs[id].services` 和 `post.steps`，均报 `unknown property`"

**置信度**: 高（平台 Schema 明确拒绝 `post.steps` 字段）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `unknown property`
- **影响面**: 所有使用 `post` 块的 workflow
- **综合**: `post` 作为一个独立的 workflow 块不被平台支持
- **是否有规避手段**: 是 — 将 post 逻辑移入最后一个 job 的最后一个 step，使用 `if: ${{ always() }}`

**建议**:
- 删除整个 `post` 块
- 在 `failing` job 中将 post notification step 添加在 Force failure step 之后，使用 `if: ${{ always() }}`
- 移除 `verify` job 中不必要的步骤
