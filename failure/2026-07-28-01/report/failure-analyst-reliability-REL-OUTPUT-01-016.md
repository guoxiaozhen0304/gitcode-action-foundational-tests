## 失败分诊 · REL-OUTPUT-01-016 · step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递

**判定结果**: FAIL
**失败断言**: assertions[0] (status, positive, run_status) — 期望 all job/step green，实际 job 'output boundary test' status=FAILED

**根因初判**: 产品bug

**责任人**: 平台方 — ATOMGIT_OUTPUT 机制按文档声明"每个参数最大 1MB"，但 1MB 边界测试无法通过：job 静默 FAILED、shell 无任何输出

**证据**:

- **Job 日志全量**（仅 6 行，shell 输出为绝对空）:
  ```
  [2026/07/28 13:19:15.367 GMT+08:00] [INFO] Job(1531652256250470400_1531652256216915975) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: /home/slave1/runner/workers/0.0.4.4.version/_temp/90a831a5-3fde-4691-887a-25a3b44b8c03.sh
  ::debug::Executing: bash -e /home/slave1/runner/workers/0.0.4.4.version/_temp/90a831a5-3fde-4691-887a-25a3b44b8c03.sh
  ```
  - 步骤 1（write 1MB output）：向 `$ATOMGIT_OUTPUT` 写入 `data=` 键后跟 1,048,576 字符的 `A`——应产生一条约 1MB 长度的输出行，**日志中无任何 trace**。
  - 步骤 2（read 1MB output）：用 `${{ steps.writer.outputs.data }}` 表达式展开 1MB 的输出值——表达式展开和 `echo`/`test` 命令均**无任何 shell 输出**。
  - 整条 job 运行时长 307 秒（5 分钟），但 shell stdout/stderr 完全空白——运行器执行了脚本但未产生任何可见输出即失败。

- **预期行为**（Phase 01 文本用例 `phase01/runs/2026-07-27-01/cases/text/REL-OUTPUT-01-016.md`，优先级 P1，维度 stability）:
  - 操作步骤 1: "job 的 step A 向 ATOMGIT_OUTPUT 写入恰好 1 MB 参数"
  - 操作步骤 2: "step B 读取该参数"
  - 预期结果: "step B 读取到完整 1 MB 内容" / "MD5 校验通过"
  - 验证点 [正向]: "下游读取内容长度=1,048,576 bytes"
  - 验证点 [负向]: "不应截断或丢失"

- **实际行为**:
  - Job 静默 FAILED，shell 输出完全为空。无法判断失败发生在步骤 1（写入 `$ATOMGIT_OUTPUT` 时失败）还是步骤 2（表达式 `${{ steps.writer.outputs.data }}` 展开 1MB 时失败）。
  - 1MB 输出传递功能完全未工作，且无任何诊断输出。

- **对照 GitCode 规格**:
  - `phase01/inputs/gitcode-spec/writing-pipelines/pass-output-between-jobs.md` 第 23 行：原文 "Step 输出：在步骤中使用 `ATOMGIT_OUTPUT` 环境变量写入键值对。**每个参数最大 1MB。**"
  - 同一文件第 23-28 行给出完整示例——Step 通过 `echo "key=value" >> "$ATOMGIT_OUTPUT"` 写入，下游通过 `${{ steps.<id>.outputs.<key> }}` 读取。
  - 测试 YAML 中 `echo "data=$(cat out.txt)" >> $ATOMGIT_OUTPUT`（第 24 行）与规格写入方式一致；`${{ steps.writer.outputs.data }}`（第 27 行）与规格读取方式一致。文档确凿承诺 1MB 参数大小，测试用例精确测试该承诺边界。
  - `phase01/inputs/gitcode-spec/writing-pipelines/configure-jobs.md` 第 143-150 行同样给出 `>> "$ATOMGIT_OUTPUT"` 写法示例，未声明额外限制。

**置信度**: 高（日志证据直接——零 shell 输出 + job FAILED；规格精确承诺 1MB 参数上限，测试用例严格按文档写法编写；307 秒运行时长排除了快速超时退出的可能）

**影响**:
- **阻塞性**: 🔴阻塞 — ATOMGIT_OUTPUT 是 step 间传递数据的唯一标准机制，1MB 是文档声明上限，在此边界下机制完全失效导致 job 失败
- **静默性**: 🔴静默错误 — shell 输出完全为空，无 `::error::` 诊断日志、无退出码信息、无任何可定位失败的 trace。用户只能看到 job 跑了 5 分钟后 FAILED，完全无法自助排查
- **影响面**: 🟡同维度 — 影响所有需要 step 间传递较大数据（接近 1MB）的 workflow，尤其是构建产物哈希、测试结果 JSON、配置文件生成等场景
- **综合**: 阻塞且完全静默——文档承诺 1MB 上限的 ATOMGIT_OUTPUT 在边界值测试中静默失败、无任何诊断输出，用户无法使用也无法排查
- **是否有规避手段**: 否 — 无替代的 step 间数据传递机制（artifact 是 job 间而非 step 间）；唯一选择是避开 ATOMGIT_OUTPUT 或控制输出 < 未知安全阈值

**建议**:
- 定位失败的确切步骤：是写入 `$ATOMGIT_OUTPUT`（1MB 行写入文件失败）还是表达式展开 `${{ steps.writer.outputs.data }}`（1MB 值在 expression engine 中崩溃）。需要在 step 间插入诊断性 echo 来隔离
- 无论根因在哪一层，平台都应：(a) 使 1MB 参数按文档承诺正常工作，或 (b) 若当前实现达不到 1MB，更新文档中的上限声明为真实可达值
- 当前最严重的可用性问题不是功能缺失而是"零诊断输出"——即使有大小限制，也应给出明确报错（如 `##[error] Step output parameter 'data' exceeds maximum size of X bytes`），而不是静默失败
- 相关用例: 所有依赖 ATOMGIT_OUTPUT 传递较大数据（> 几十 KB）的用例
