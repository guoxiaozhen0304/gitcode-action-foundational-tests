## 失败分诊 · COMP-SYSENV-01-059 · ATOMGIT 系统环境变量关键变量存在性

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_logs) — 期望 log contains 'SHA_SET=yes'，实际 absent（日志实际输出 `SHA_SET=no`）
- assertions[1] (positive, run_logs) — 期望 log contains 'REF_SET=yes'，实际 present（PASS）
- assertions[2] (positive, run_logs) — 期望 log contains 'EVENT_NAME_SET=yes'，实际 present（PASS）
- assertions[3] (positive, run_logs) — 期望 log contains 'WORKSPACE_SET=yes'，实际 present（PASS）
- assertions[4] (positive, run_logs) — 期望 log contains 'REPO_SET=yes'，实际 present（PASS）
- assertions[5] (positive, run_logs) — 期望 log contains 'RUN_ID_SET=yes'，实际 present（PASS）

**根因初判**: 产品缺陷

**责任人**: 平台方 — `ATOMGIT_SHA` 环境变量在 workflow_dispatch 下为空，与文档承诺不一致

**证据**:

- **Job 日志全文**（共 14 行）:
  ```
  SHA_SET=no                 (行 5)
  REF_SET=yes                (行 6)
  REF_NAME_SET=yes           (行 7)
  EVENT_NAME_SET=yes         (行 8)
  WORKSPACE_SET=yes          (行 9)
  REPO_SET=yes               (行 10)
  RUN_ID_SET=yes             (行 11)
  RUN_NUM_SET=yes            (行 12)
  SERVER_SET=yes             (行 13)
  API_SET=yes                (行 14)
  ```
  10 个 ATOMGIT_* 环境变量中，**仅 `ATOMGIT_SHA` 为空**（`[ -n "$ATOMGIT_SHA" ]` 结果为假），其余 9 个均有值且 `SET=yes`。

- **预期行为**（用例 YAML COMP-SYSENV-01-059，P1，维度 completeness）:
  - `ATOMGIT_SHA` 应有值 → `SHA_SET=yes`
  - 其余 5 个关键变量（REF, EVENT_NAME, WORKSPACE, REPO, RUN_ID）均 PASS

- **实际行为**:
  - 6 个被测试的断言中 5 个 PASS，仅 `SHA_SET` 因 ATOMGIT_SHA 为空而输出 `no`
  - ATOMGIT_SHA 为空与 COMP-ATOMGIT-01-047/049 的发现一致（`atomgit.sha` 也返回空）

- **对照 GitCode 规格**:
  - `phase01/inputs/gitcode-spec/syntax-reference/context.md` 第 30 行：`atomgit.sha` 承诺为 "触发提交的 SHA"
  - `phase01/inputs/gitcode-spec/action-development/runtime-environment-variables.md`（如存在）应列出环境变量版的 ATOMGIT_SHA
  - 测试 YAML 使用 `$ATOMGIT_SHA` 环境变量判定，这是 shell 中访问上下文的正确方式（`configure-steps.md` 第 220 行）

**置信度**: 高（日志证据单点明确，其余 9/10 变量均正常，排除了环境变量批量注入失败的怀疑）

**影响**:
- **阻塞性**: 🟡非阻塞 — Workflow 可跑完，仅一个变量为空
- **静默性**: 🔴静默错误 — `ATOMGIT_SHA` 静默为空，用户的脚本若使用此变量做构建标签或缓存 key 会静默产生错误
- **影响面**: 🔴跨维度 — 所有依赖 `ATOMGIT_SHA` 环境变量的 workflow 均受影响
- **综合**: 非阻塞但静默且跨维度，10 个核心变量中 9 个正常、1 个为空——可能是 workflow_dispatch 触发事件没有关联 commit SHA 的设计特征
- **是否有规避手段**: 是 — 可用 `$ATOMGIT_RUN_ID` 作为替代唯一标识，但语义不同

**建议**:
- 平台方确认 workflow_dispatch 是否设计为不关联 commit SHA（若如此则文档需明确标注 `ATOMGIT_SHA` 在此事件下为空）
- 若应为有值，则修复为返回触发时 HEAD commit 的 SHA
- 其他 9/10 变量注入经验证正常，平台在系统环境变量注入方面总体可靠
- 相关用例: COMP-ATOMGIT-01-047, COMP-ATOMGIT-01-049（同根因）
