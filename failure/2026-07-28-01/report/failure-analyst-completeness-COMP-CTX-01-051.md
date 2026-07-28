## 失败分诊 · COMP-CTX-01-051 · 上下文在 workflow job step 各级注入验证

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_logs) — 期望 log contains 'WF_REF=refs/'，实际 absent（日志实际输出 `WF_REF=main`）
- assertions[1] (positive, run_logs) — 期望 log contains 'JOB_REF=refs/'，实际 absent（日志实际输出 `JOB_REF=main`）
- assertions[2] (positive, run_logs) — 期望 log contains 'JOB_STATUS='，实际 present（PASS，输出 `JOB_STATUS=success`）

**根因初判**: 产品缺陷

**责任人**: 平台方 — `atomgit.ref` 在 workflow_dispatch 下返回短格式 `main` 而非文档承诺的 `refs/heads/main`

**证据**:

- **Job 日志全量**（共 8 行）:
  ```
  WF_REF=main                (行 5)
  JOB_REF=main               (行 6)
  JOB_STATUS=success          (行 7)
  ATOMGIT_REF=main            (行 8)
  ```
  所有级别的 ref 注入均得到 `main`，无 `refs/` 前缀。

- **预期行为**（用例 YAML COMP-CTX-01-051，P1，维度 completeness）:
  - workflow 级 `env: WF_REF: ${{ atomgit.ref }}` → 预期输出 `WF_REF=refs/heads/main`
  - job 级 `env: JOB_REF: ${{ env.WF_REF }}` → 预期输出 `JOB_REF=refs/heads/main`（跨级传递成立）
  - step 级 `${{ job.status }}` 可用 → PASS

- **实际行为**:
  - `atomgit.ref` 返回 `main`（短格式），导致 `WF_REF=main`、`JOB_REF=main`
  - **上下文注入机制本身正常工作**（各级 env 均被正确注入），失败原因纯为源数据 `atomgit.ref` 格式不符文档

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/context.md`:
  - 第 31 行：`atomgit.ref` 承诺为 "触发引用（分支或标签全名，如 `refs/heads/main`）"
  - 第 117-148 行：env 在 workflow/job/step 三级注入机制文档完整
  - 第 279-291 行：上下文可用性表确认 `atomgit` 和 `env` 在 workflow/job/step 级均可用
  - 上下文注入功能本身符合文档承诺；失败原因**仅在于 `atomgit.ref` 返回值与文档不符**

**置信度**: 高（日志直接对应源数据缺陷，上下文的级联注入机制本身未发现异常）

**影响**:
- **阻塞性**: 🟡非阻塞 — Workflow 可跑完
- **静默性**: 🔴静默错误 — 各级 env 被静默设置为主观上正确的值，用户难以察觉返回值实际格式与文档不同
- **影响面**: 🔴跨维度 — 所有依赖 `atomgit.ref` 进行条件判断（如 `if: atomgit.ref == 'refs/heads/main'`）或脚本处理的 workflow 均受影响
- **综合**: 非阻塞但静默且跨维度，上层上下文注入机制正常，但根数据源 `atomgit.ref` 格式错误
- **是否有规避手段**: 是 — 可在判断中用 `atomgit.ref_name` 代替 `atomgit.ref`，但会失去对标签/分支类型的区分能力

**建议**:
- 此用例的 FAIL 是 COMP-ATOMGIT-01-047 的派生结果，**优先修复 `atomgit.ref` 返回值格式**
- 上下文注入机制（三级 env 传递）经验证正常，无需修改
- 相关用例: COMP-ATOMGIT-01-047, COMP-ATOMGIT-01-049, COMP-ENVCTX-01-050
