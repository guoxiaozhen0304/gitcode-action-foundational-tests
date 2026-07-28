## 失败分诊 · COMP-PR-01-005 · 源分支更新后 pre-merge ref 指向刷新验证

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_logs) — 期望 log contains 'REF_SHA_RECORDED'，实际 absent

**根因初判**: 产品缺陷 / 环境问题

**责任人**: 平台方 — 与 COMP-PR-01-004 同一根因：`refs/merge-requests/1/merge` 在 GitCode 平台上不可解析

**证据**:

- **Job 日志关键行**（共 49 行，与 COMP-PR-01-004 完全相同的错误模式）:
  ```
  行 30: git -c protocol.version=2 fetch ... +refs/merge-requests/1/merge:refs/remotes/merge-requests/1/merge
  行 31: fatal: couldn't find remote ref refs/merge-requests/1/merge
  行 33-36: ERROR ID: CHECKOUT.00010010 — Git命令执行失败
  行 47: ::error::git进行拉取动作失败, 执行git命令失败
  ```
  试图 checkout `refs/merge-requests/1/merge` 但远程仓库不存在该 ref。

- **预期行为**（用例 YAML COMP-PR-01-005，P1，维度 completeness）:
  - 调用 checkout action 指定 `ref: refs/merge-requests/1/merge`
  - checkout 成功后，`git rev-parse HEAD` 记录当前 HEAD SHA
  - 输出 `REF_SHA_RECORDED`
  - 非功能性验证（llm_assisted）：源分支新增提交后再次运行，HEAD sha 应不同（刷新验证）；PR 合并/关闭后再次解析该 ref 的行为

- **实际行为**:
  - 与 COMP-PR-01-004 完全一致：checkout 在 fetch 阶段失败，"couldn't find remote ref"
  - 本用例的 HEAD SHA 记录和刷新验证均未进行

- **对照 GitCode 规格**:
  - 同 COMP-PR-01-004 — 未在文档中找到对 `refs/merge-requests/N/merge` 格式的承诺
  - 两个用例（COMP-PR-01-004 和 COMP-PR-01-005）共享同一个 `intent_ref: INTENT-COMP-033` 和 `repo_fixture: pr-merge-ref`

**置信度**: 高 — 与 COMP-PR-01-004 的错误完全一致，同一夹具、同一 ref 格式、同一错误信息

**影响**:
- **阻塞性**: 🔴阻塞 — checkout 失败，merge ref 刷新验证未进行
- **静默性**: 🟡可察觉 — 平台明确报错
- **影响面**: 🟡同维度 — 若平台不支持此 ref，两个用例（004/005）同时受影响
- **综合**: 阻塞但可察觉，与 COMP-PR-01-004 同根因
- **是否有规避手段**: 否

**建议**:
- 与 COMP-PR-01-004 合并排查
- 确认 `pr-merge-ref` fixture 状态（是否有活跃 PR #1）
- 确认平台是否支持 `refs/merge-requests/N/merge`（若非平台功能，记入能力边界，两个用例均无效）
- 相关用例: COMP-PR-01-004
