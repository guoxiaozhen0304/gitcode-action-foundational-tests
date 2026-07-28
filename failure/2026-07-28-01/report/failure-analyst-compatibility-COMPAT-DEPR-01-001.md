## 失败分诊 · COMPAT-DEPR-01-001 · ::set-env:: 废弃命令应被拒绝或给出迁移指引

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, run_status_not) — 期望 conclusion != SUCCESS（即不应成功），实际 conclusion=COMPLETED

**根因初判**: 产品缺陷

**责任人**: 平台方 — GitCode Actions 平台在收到已废弃的 `::set-env::` 命令后静默忽略（既不生效也不警告），用户无任何反馈，无法判断配置是否生效

**证据**:

- **Job 日志全量**（7 行，workflow COMPLETED）:
  ```
  [2026/07/28 13:03:37.075 GMT+08:00] [INFO] Job(1531648320789299200_1531648320755744775) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../0428f6bc.sh
  ::debug::Executing: bash -e .../0428f6bc.sh
  ::set-env name=MY_VAR::hello
  MY_VAR=
  done
  ```
  - 第 5 行：废弃命令 `::set-env name=MY_VAR::hello` 被 echo 输出到 stdout，未被 Runner 拦截或警告
  - 第 6 行：`MY_VAR=`（空值）—— 命令未生效，变量未被设置
  - 第 7 行：`done` —— 步骤正常结束，workflow 以 COMPLETED 结案
  - **平台行为**：收到废弃命令后**既不生效也不报错也不警告**，静默忽略

- **预期行为**（Phase 01 文本用例 COMPAT-DEPR-01-001，P1，兼容性/可用性）:
  - 操作步骤: 在 run 步骤中使用 `echo '::set-env name=MY_VAR::hello'`
  - 预期结果: "应明确拒绝该命令或给出弃用警告及替代方案"；"不应静默忽略导致用户误以为配置生效"
  - 验证点: [负向] 不通过命令被静默忽略且 workflow 成功；[正向] 系统给出明确响应：报错拒绝、或警告+替代方案

- **实际行为**:
  - 平台对废弃命令静默忽略：命令不生效（MY_VAR 为空）、workflow 仍以 COMPLETED 结束、日志中无任何 warning/error 信息
  - 用户看到 `done` 以为任务正常完成，实际变量未设置——产生误以为配置生效的隐患

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/workflow-commands.md`:
  - 第 60-68 行（§5.6 废弃的命令格式）：文档明确将 `::set-env::` 列为"已废弃"命令，并提供替代方案 `echo "MY_VAR=my_value" >> $ATOMGIT_ENV`
  - 文档未明确承诺"平台将拒绝废弃命令"，但"废弃+替代"的语义加上 §5.2 的 ATOMGIT_ENV 配套机制，表明平台的设计意图是旧命令不再被支持、用户应迁移至新协议
  - 静默忽略违背了文档传递的信号——用户按文档知道应迁移，但若误用旧命令得不到任何提示

**置信度**: 高（日志直接显示静默忽略，spec 明确标记废弃，实际行为与文档隐含预期矛盾）

**影响**:
- **阻塞性**: ⚪ 无影响 — workflow 本身能跑完（COMPLETED），不阻断 CI pipeline
- **静默性**: 🔴 静默错误 — 用户执行 `::set-env::` 后 workflow 成功但变量未生效，无任何错误或警告提示；用户可能误以为配置已生效
- **影响面**: 🟡 同维度 — 所有使用 `::set-env::` / `::set-output::` / `::add-path::` 等废弃命令的迁移用户均受影响；按文档迁移的用户不受影响
- **综合**: 非阻塞但高度静默——废弃命令被平台吞掉，workflow 成功但变量为空，用户无任何反馈机制判断废弃命令是否执行、是否已迁移成功
- **是否有规避手段**: 是——按文档使用 `$ATOMGIT_ENV` 文件协议替代 `::set-env::`

**建议**:
- 平台应在 Runner 层拦截以 `::` 开头的废弃 workflow 命令，至少输出 deprecation warning 提示用户已废弃并引导至替代方案
- 若不拦截，至少应在 Runner 日志中生成 visible 级别的警告消息
- 相关用例: COMPAT-DEPR 系列所有废弃命令用例（::set-output:: / ::add-path:: 等）
