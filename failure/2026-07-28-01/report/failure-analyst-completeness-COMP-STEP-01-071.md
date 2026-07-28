## 失败分诊 · COMP-STEP-01-071 · step 执行控制 shell working-directory continue-on-error timeout-minutes 验证

**判定结果**: FAIL
**失败断言**:
- assertions[3] (positive, run_logs) — 期望 log contains 'PWD_NOW=/tmp'，实际 absent（日志实际输出 `wd_ok`）
- assertions[4] (positive, run_logs) — 期望 log contains 'before_fail'，实际 absent
- assertions[0] (positive, run_status) — 期望 COMPLETED，实际 COMPLETED（PASS）
- assertions[1] (positive, run_logs) — 期望 log contains 'bash_ok'，实际 present（PASS）
- assertions[2] (positive, run_logs) — 期望 log contains 'sh_ok'，实际 present（PASS）
- assertions[5] (positive, run_logs) — 期望 log contains 'continue_ok'，实际 present（PASS）

**根因初判**: 标记不匹配 + 需人工判断

**责任人**: Phase 01 — `compile_asserts.py` 编译器修复词汇映射/编译产物的 YAML 与原始 YAML 不一致导致的断言失配

**证据**:

- **Job 日志全文**（共 18 行）:
  ```
  bash_ok                    (行 4)
  sh_ok                      (行 8)
  wd_ok                      (行 13)
  continue_ok                (行 18)
  ```
  - **working-directory 步骤**: 日志输出的是 `wd_ok`（第 13 行），而非 YAML 中所写的 `PWD_NOW=$(pwd)`。这说明编译后的 workflow YAML 中该步骤的 run 内容与原始 YAML 不同
  - **continue-on-error 步骤**: 日志中未出现 `before_fail`，直接跳到了 `continue_ok`。但 run_status 为 COMPLETED（非 FAILED），说明 `continue-on-error: true` **确实生效**（退出码 1 未导致 job 失败）

- **预期行为**（用例 YAML COMP-STEP-01-071，P1，维度 completeness）:
  - `working-directory: /tmp` → `pwd` 应输出 `PWD_NOW=/tmp`
  - `continue-on-error: true` → `echo "before_fail"; exit 1` → 后续步骤仍可执行 → 输出 `continue_ok`

- **实际行为**:
  - working-directory 步骤实际输出了 `wd_ok`，说明编译后的 run 脚本与 YAML 不同
  - continue-on-error 步骤中 `echo "before_fail"` 未出现在日志中，`continue_ok` 出现了，说明 continue-on-error 功能正常但步骤内容被修改
  - shell 指定（bash/sh）正常工作

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/configure-steps.md`:
  - 第 124-134 行：`working-directory` 说明直接给出示例 `working-directory: frontend`，强调相对于仓库根目录
  - 第 190-199 行：`continue-on-error` 说明 — run_status COMPLETED 与此一致
  - 第 106-110 行：`shell` 说明 bash/sh 均支持 — 实际 PASS

**置信度**: 中 — 日志输出 `wd_ok` 与断言 `PWD_NOW=/tmp` 不符是确定的，但具体是编译阶段修改了 run 内容还是 runner 行为差异，需比对编译产物确认

**影响**:
- **阻塞性**: ⚪无影响 — continue-on-error 经验证功能正常，shell 指定正常；working-directory 因编译差异无法判定
- **静默性**: 🟡可察觉 — 断言因关键词失配而 FAIL，用户可看到 FAIL 标识
- **影响面**: 🟢单用例 — 断言关键词与实际输出不同，平台功能可能正常
- **综合**: 无影响但可察觉，实际行为可能符合文档预期但断言关键词与编译产物不匹配
- **是否有规避手段**: 是 — 更新断言关键词以匹配编译后的实际输出

**建议**:
- Phase 01 比对原始 YAML 与编译后的 workflow YAML（`.gitcode/workflows/comp-step-01-071.yml`），确定 working-directory 和 continue-on-error 步骤的 run 内容是否在编译阶段被修改
- 若编译产物与原 YAML 一致但 runner 输出不同，则属平台行为偏差，需变更分类
- 若编译产物已被修改，则属 Phase 01 的编译逻辑问题
