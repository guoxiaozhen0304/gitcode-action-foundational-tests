## 失败分诊 · COMP-ATOMGIT-01-047 · atomgit 核心上下文属性可访问性

**判定结果**: FAIL
**失败断言**:
- assertions[1] (positive, run_logs) — 期望 log contains 'REF=refs/'，实际 absent（日志实际输出 `REF=main`）
- assertions[3] (positive, run_logs) — 期望 log contains 'SHA_LEN=40'，实际 absent（日志实际输出 `SHA=` 空值）
- assertions[4] (positive, run_logs) — 期望 log contains 'REF_NAME_HAS_PREFIX=no'，实际 absent
- assertions[0] (positive, run_logs) — 期望 log contains 'SHA='，实际 present（PASS，SHA 为空但仍包含 `SHA=`）
- assertions[2] (positive, run_logs) — 期望 log contains 'REPO='，实际 present（PASS）

**根因初判**: 产品缺陷

**责任人**: 平台方 — GitCode Actions 平台需修复 `atomgit.ref` 返回格式和 `atomgit.sha` 为空的问题

**证据**:

- **Job 日志全量**（共 19 行）:
  ```
  SHA=                       (行 5 — ATOMGIT_SHA 为空)
  REF=main                   (行 6 — 仅返回短格式，非文档承诺的 refs/heads/main)
  REF_NAME=main              (行 7)
  REF_TYPE=branch            (行 8)
  ...
  ```
  SHA 行输出空值（`SHA=` 后无内容），`atomgit.ref` 返回 `main` 而非 `refs/heads/main`。

- **预期行为**（用例 YAML COMP-ATOMGIT-01-047，P1，维度 completeness）:
  - `atomgit.sha` 应返回 40 字符 hex SHA（断言 `SHA_LEN=40`）
  - `atomgit.ref` 应返回完整引用格式如 `refs/heads/main`（断言 `REF=refs/`）
  - `atomgit.ref_name` 本身不应带 `refs/` 前缀（断言 `REF_NAME_HAS_PREFIX=no`）

- **实际行为**:
  - `atomgit.sha` 在 workflow_dispatch 触发下为空字符串 → `SHA_LEN=0`
  - `atomgit.ref` 返回短格式 `main` → 断言 `REF=refs/` 不成立
  - `atomgit.ref_name` 返回 `main`（已是短名，不包含 `refs/`），但因 shell 代码在 `SHA` 为空时可能提前退出，`REF_NAME_HAS_PREFIX` 步骤未输出

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/context.md`:
  - 第 31 行明确承诺：`atomgit.ref` 类型为 string，说明为 "触发引用（分支或标签全名，如 `refs/heads/main`）"
  - 第 30 行明确承诺：`atomgit.sha` 类型为 string，说明为 "触发提交的 SHA"
  - 实际平台行为与文档承诺**直接矛盾**：`ref` 返回 `main` 而非 `refs/heads/main`，`sha` 返回空字符串

**置信度**: 高（日志直接对比文档，差异一目了然）

**影响**:
- **阻塞性**: 🟡非阻塞 — Workflow 可跑完，但格式与文档不符
- **静默性**: 🔴静默错误 — 平台不报错，返回了错误格式的值，用户依赖全格式 `refs/heads/` 前缀的脚本会静默失败
- **影响面**: 🔴跨维度 — `atomgit.ref` 和 `atomgit.sha` 是所有 workflow 的基础上下文，所有引用这些属性的 workflow 均受影响
- **综合**: 非阻塞但静默且跨维度，`atomgit.ref` 格式错误 + `atomgit.sha` 为空可导致所有依赖 ref 全格式或 sha 值的 pipeline 静默异常
- **是否有规避手段**: 是 — 用户可在脚本中硬编码 `refs/heads/` 前缀，但这不是文档承诺的标准行为，且无法补救空的 SHA

**建议**:
- 平台方修复 `atomgit.ref` 在 workflow_dispatch 下返回 `refs/heads/<branch>` 全格式
- 平台方修复 `atomgit.sha` 在 workflow_dispatch 下返回实际触发 commit SHA
- 若 workflow_dispatch 确实没有关联 commit，文档应明确标注此约束
- 相关用例: COMP-ATOMGIT-01-049, COMP-CTX-01-051, COMP-SYSENV-01-059, COMP-EXPR-01-054（均受 `atomgit.ref` 格式和 `atomgit.sha` 为空影响）
