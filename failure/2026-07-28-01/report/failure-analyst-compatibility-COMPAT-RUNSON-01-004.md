## 失败分诊 · COMPAT-RUNSON-01-004 · 自托管 runs-on 数组式写法（标签列表子集匹配）的实测仲裁

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED；assertions[1] (negative, run_status_not) — 期望 conclusion != SUCCESS，实际 FAILED（通过）

**根因初判**: 环境问题

**责任人**: Phase 02 — 测试执行环境自托管 runner 配置未验证，job 零 shell 输出，无任何步骤执行痕迹；spec 明确支持该数组式写法，应通过

**证据**:

- **Job 日志全量**（仅 1 行，无任何 shell 执行痕迹）:
  ```
  [2026/07/28 13:13:44.209 GMT+08:00] [INFO] Job(1531650867285602304_1531650867264630791) duration check: true
  ```
  Runner 分配了 job 实例（duration check 通过），但之后零 shell 输出。无 `Script file created`、无 `Executing:` 行、无任何步骤执行或报错信息。

- **预期行为**（Phase 01 文本用例 COMPAT-RUNSON-01-004，P1，兼容性/可用性）:
  - 前置条件: 实例已注册带 linux、x64 标签的自托管 Runner
  - 操作步骤: 提交按 runner-images-tools.md 数组式写法声明自托管 runs-on 的 workflow
  - 预期结果: 数组式写法得到确定响应（调度成功或解析期明确报错）
  - 验证点: [正向] 数组式写法的调度或报错结局确定；[负向] 不应无限 queued 无提示

- **实际行为**:
  - Job 在 duration check 后立即失败，43 秒耗时，零 shell 输出
  - 无法解析任何步骤输出、无法判断是 runner 未匹配到还是 job 被平台拒绝

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/runner-management/selecting-runner-labels.md`:
  - 第 19-31 行（匹配规则 — 规则一：全匹配）：文档 **明确给出数组式 `runs-on: [self-hosted, linux, x64]` 为 ✅ 匹配** 的示例，与测试 YAML 中 `runs-on: [self-hosted, linux, x64]` 完全一致
  - 第 15 行（标签类型对照）：明确 `[self-hosted, linux, gpu]` 为自托管 runner 组合标签格式
  - 第 33-35 行（规则二）：说明 `default` 等价关系
  - 测试 YAML 的 `runs-on: [self-hosted, linux, x64]` 与文档第 27 行示例精确映射——写法被文档认可

**置信度**: 高（spec 明确支持数组式写法，零 shell 输出指向环境配置；但 runner 标签是否已注册未经 config_probe 验证，不能直接归因平台缺陷）

**影响**:
- **阻塞性**: 🟡 非阻塞 — 本次探测未执行，但不影响其他用例
- **静默性**: 🔴 静默错误 — job 分配后静默失败，1 行日志，无诊断信息
- **影响面**: 🟢 单用例 — 仅影响此探测用例
- **综合**: 非阻塞的静默失败——平台正确接受 job 调度但执行层零输出，疑似自托管 runner 未就绪或标签匹配失败
- **是否有规避手段**: 是——在 fixture 环境加 config_probe 验证自托管 runner 的注册状态和标签集合

**建议**:
- 排查 `with-self-hosted-runner` fixture 环境下是否确实注册了带 linux、x64 标签的自托管 Runner 并处于在线状态
- 零 shell 输出缺乏错误诊断——若 runner 标签不匹配导致未被调度，平台应输出明确提示（如 "No runner matching labels [self-hosted, linux, x64] found"）
- 相关用例: COMPAT-RUNSON-01-001/002/003（同一 fixture，同维度）
