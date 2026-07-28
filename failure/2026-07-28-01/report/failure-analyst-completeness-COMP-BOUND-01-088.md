## 失败分诊 · COMP-BOUND-01-088 · 工作流命令 set-env add-path 与文件写入边界验证

**判定结果**: FAIL
**失败断言**:
- assertions[2] (positive, run_logs) — 期望 log contains 'OUT_KEY=out_val'，实际 absent
- assertions[0] (positive, run_logs) — 期望 log contains 'MY_ENV=from_env_file'，实际 present（PASS）
- assertions[1] (positive, run_logs) — 期望 log contains 'PATH_HAS_EXTRA=yes'，实际 present（PASS）
- assertions[3] (positive, run_logs) — 期望 log contains 'commands_ok'，实际 present（PASS）

**根因初判**: 产品缺陷

**责任人**: 平台方 — GitCode Actions 的步骤间 output 传递机制（通过 `ATOMGIT_OUTPUT` 写入 + `steps.<id>.outputs.<key>` 读取）可能在跨 step 时未就绪

**证据**:

- **Job 日志全文**（共 11 行）:
  ```
  MY_ENV=from_env_file      (行 9)
  PATH_HAS_EXTRA=yes         (行 10)
  commands_ok                (行 11)
  ```
  日志中**无 `OUT_KEY=out_val`**。步骤 cmdwriter 向 `$ATOMGIT_OUTPUT` 写入了 `out_key=out_val`（行 26 的 run），但后续步骤读取 `${{ steps.cmdwriter.outputs.out_key }}` 时值为空（否则会输出 `OUT_KEY=out_val`）。

- **预期行为**（用例 YAML COMP-BOUND-01-088，P1，维度 completeness）:
  - 步骤 cmdwriter 通过 echo 写入 `$ATOMGIT_OUTPUT` 三个键值对
  - 后续步骤读取环境变量 MY_ENV 和 PATH（通过 `$ATOMGIT_ENV` / `$ATOMGIT_PATH`）——这两个 PASS
  - 后续步骤通过 `${{ steps.cmdwriter.outputs.out_key }}` 读取步骤输出——**实际为空**

- **实际行为**:
  - `$ATOMGIT_ENV` 写入 → 环境变量继承正常
  - `$ATOMGIT_PATH` 写入 → PATH 追加正常
  - `$ATOMGIT_OUTPUT` 写入 → **跨步骤无法读取**，`steps.cmdwriter.outputs.out_key` 解析为空

- **对照 GitCode 规格**:
  - `phase01/inputs/gitcode-spec/writing-pipelines/pass-output-between-jobs.md` 第 27-28 行：`ATOMGIT_OUTPUT` 用法示例 `echo "version=1.0.0" >> "$ATOMGIT_OUTPUT"`
  - `phase01/inputs/gitcode-spec/writing-pipelines/configure-steps.md` 第 42-46 行：步骤输出读取示例 `${{ steps.<id>.outputs.<key> }}`
  - 测试 YAML 的 `echo "out_key=out_val" >> "$ATOMGIT_OUTPUT"` 和 `${{ steps.cmdwriter.outputs.out_key }}` 与文档示例精确对应
  - 但 `$ATOMGIT_ENV` 和 `$ATOMGIT_PATH` 的同 step 内写入生效（MY_ENV/PATH_HAS_EXTRA PASS），说明文件写入机制本身是工作的

**置信度**: 高（日志证据明确，`OUT_KEY` 缺失但同脚本的其他 output 正常输出，说明 `steps.cmdwriter.outputs.out_key` 解析为空而非脚本提前退出）

**影响**:
- **阻塞性**: 🟡非阻塞 — Workflow 可完成，但步骤输出传递失败
- **静默性**: 🔴静默错误 — 平台不报错，`steps.cmdwriter.outputs.out_key` 静默返回空，用户依赖此输出的后续步骤可能产生错误结果
- **影响面**: 🟡同维度 — 所有使用 `steps.<id>.outputs.<key>` 的 workflow 可能受影响
- **综合**: 非阻塞但静默，步骤输出传递静默失败，是用户在生产中很难发现的 bug
- **是否有规避手段**: 是 — 可用 `$ATOMGIT_ENV` 替代 `$ATOMGIT_OUTPUT` 传递值（仅适用于传递环境变量场景），但语义不同且有安全考量

**建议**:
- 平台方排查 `$ATOMGIT_OUTPUT` 写入后 `steps.<id>.outputs.<key>` 解析为空的根因
- 确认是否仅有 `$ATOMGIT_ENV` 和 `$ATOMGIT_PATH` 被正确处理而 `$ATOMGIT_OUTPUT` 有缺陷
- 相关用例: COMP-BOUND-01-087（跨 job 输出传递，也可能受同一 `ATOMGIT_OUTPUT` 机制影响）
