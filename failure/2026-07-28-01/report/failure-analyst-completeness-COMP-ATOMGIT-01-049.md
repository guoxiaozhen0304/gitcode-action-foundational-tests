## 失败分诊 · COMP-ATOMGIT-01-049 · atomgit 边界格式校验

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_logs) — 期望 log contains 'SHA_LEN=40'，实际 absent（日志实际输出 `SHA_LEN=0`）
- assertions[1] (positive, run_logs) — 期望 log contains 'REF_PREFIX=refs'，实际 absent（日志实际输出 `REF_PREFIX=main`）
- assertions[2] (positive, run_logs) — 期望 log contains 'REF_NAME_NO_PREFIX='，实际 present（PASS，输出 `REF_NAME_NO_PREFIX=main`）
- assertions[3] (negative, run_logs, leak) — 期望 plaintext 'REF_NAME_NO_PREFIX=refs/' 0 hits，实际 0（PASS）
- assertions[4] (positive, run_logs) — 期望 log contains 'ACTOR_LEN='，实际 present（PASS，输出 `ACTOR_LEN=11`）

**根因初判**: 产品缺陷

**责任人**: 平台方 — GitCode Actions 平台 `ATOMGIT_SHA` 环境变量为空、`ATOMGIT_REF` 格式与文档不符

**证据**:

- **Job 日志全量**（共 8 行）:
  ```
  SHA_LEN=0                  (行 5 — ATOMGIT_SHA 为空，长度 0)
  REF_PREFIX=main            (行 6 — 字符串截取后得到 main，而非 refs)
  REF_NAME_NO_PREFIX=main    (行 7)
  ACTOR_LEN=11               (行 8)
  ```
  `ATOMGIT_SHA` 环境变量为空导致 `${#ATOMGIT_SHA}` = 0。`ATOMGIT_REF` 返回 `main` 而非 `refs/heads/main`，导致 `${ATOMGIT_REF%%/*}` 截取结果为 `main` 而非 `refs`。

- **预期行为**（用例 YAML COMP-ATOMGIT-01-049，P1，维度 completeness）:
  - `ATOMGIT_SHA` 应有值，长度应为 40（hex SHA）
  - `ATOMGIT_REF` 应以 `refs/` 开头（如 `refs/heads/main`），取前缀后 `REF_PREFIX=refs`

- **实际行为**:
  - `ATOMGIT_SHA` 在 workflow_dispatch 下为空 → `SHA_LEN=0`
  - `ATOMGIT_REF` 返回 `main` → `${ATOMGIT_REF%%/*}` = `main`

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/context.md`:
  - 第 30 行：`atomgit.sha` 承诺为 "触发提交的 SHA"（类型 string）— 实际为空
  - 第 31 行：`atomgit.ref` 承诺为 "触发引用（分支或标签全名，如 `refs/heads/main`）" — 实际返回 `main`
  - 测试 YAML 使用 `$ATOMGIT_SHA` 和 `$ATOMGIT_REF` 环境变量（shell 中访问上下文的方式），这正是文档 `configure-steps.md` 第 220 行描述的用法："在 shell 命令中直接使用环境变量，如 `$ATOMGIT_SHA`"

**置信度**: 高（日志证据直接，文档与行为明确矛盾）

**影响**:
- **阻塞性**: 🟡非阻塞 — Workflow 可跑完，但环境变量值与文档不符
- **静默性**: 🔴静默错误 — 平台不报错，`ATOMGIT_SHA` 返回空值，`ATOMGIT_REF` 返回短格式；用户脚本若依赖全格式或 SHA 值，会静默产生错误结果
- **影响面**: 🔴跨维度 — 所有依赖 `ATOMGIT_SHA` 和 `ATOMGIT_REF` 环境变量的 workflow 均受影响
- **综合**: 非阻塞但静默且跨维度，核心环境变量值偏离文档承诺
- **是否有规避手段**: 是 — 部分缓解：可用 `atomgit.ref_name` 代替 `atomgit.ref` 获取短名（但无法获取全格式 ref）；SHA 缺失无替代方案

**建议**:
- 平台方修复 `ATOMGIT_SHA` 在 workflow_dispatch 下返回实际 commit SHA
- 平台方修复 `ATOMGIT_REF` 返回 `refs/heads/<branch>` 全格式
- 若 workflow_dispatch 无关联 commit SHA，文档应明确标注此限制
- 相关用例: COMP-ATOMGIT-01-047, COMP-CTX-01-051, COMP-SYSENV-01-059
