## 失败分诊 · COMPAT-ACTIONDEV-01-002 · action 运行时 runs.using 类型覆盖（node16/composite/docker/node20）探测

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, status) — 期望 all job/step green，实际 job 'Probe runs using runtime coverage' status=FAILED

**根因初判**: 环境问题

**责任人**: Phase 02 — 测试执行环境 `repo_fixture: with-local-actions` 未验证，job 零 shell 输出，无任何步骤执行痕迹

**证据**:

- **Job 日志全量**（仅 6 行，无任何 shell 命令执行痕迹）:
  ```
  [2026/07/28 13:00:21.144 GMT+08:00] [INFO] Job(1531647499071000576_1531647499050029063) duration check: true
  
   
  
  
  
  ```
  Runner 分配了 job 实例（duration check 通过），但之后零个 shell 脚本被创建、零个步骤被执行。没有 `Script file created`、没有 `Executing:` 行、没有任何 `echo` / 编译 / 报错输出。

- **预期行为**（Phase 01 文本用例 COMPAT-ACTIONDEV-01-002，P1，兼容性）:
  - 前置条件: fixture 仓库内置四类本地 action（node16/composite/docker/node20）
  - 操作步骤 1: 提交依次引用四类本地 action 的 workflow
  - 操作步骤 2: 观察各 action 在加载阶段与运行阶段的响应
  - 预期结果: 支持的 runs.using 类型正常执行，不支持的在加载期明确报错
  - 验证点: [正向] node16 正常执行；[正向] composite/docker/node20 得到确定响应

- **实际行为**:
  - Job 在 Runner 上分配后立即失败，零 shell 输出
  - 无法判断是 workflow 解析失败、action 加载失败、还是 fixture 环境缺失
  - 测试 YAML `repo_fixture: with-local-actions` 要求仓库中已有 `.gitcode/actions/probe-node16/action.yml` 等文件，但未做 config_probe 验证

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/using-actions.md`:
  - 第 65-72 行：文档支持自定义插件引用（同仓相对路径 `uses: ./.gitcode/actions/my-custom-action`），要求对应路径下有 `action.yml` 元数据文件
  - 第 77-91 行：文档给出 `action.yml` 结构，`runs.using` 字段支持 `node16` 等值
  - 若本地 action 文件缺失或 `action.yml` 格式不符，应产生加载期明确报错——但日志中无此信息

**置信度**: 中（零 shell 输出的确切原因无法从日志确认，fixture 状态未经 config_probe 验证；但倾向于环境问题而非平台缺陷，因为平台至少在 runner 层面正确响应了 job 调度）

**影响**:
- **阻塞性**: 🟡 非阻塞 — 本次探测未执行，但不影响其他独立用例
- **静默性**: 🔴 静默错误 — job 分配后静默失败，零 shell 输出，无任何诊断信息向用户暴露失败原因
- **影响面**: 🟢 单用例 — 仅影响此探测用例
- **综合**: 非阻塞的静默失败——job 分配后无任何步骤执行且零 shell 输出，fixture 状态未验证导致无法判断平台是否支持各类 runs.using
- **是否有规避手段**: 是——需确认 fixture 仓库中各本地 action 的 action.yml 文件存在且有效；加 config_probe 验证 fixture

**建议**:
- 执行为此测试准备的 fixture 时加 config_probe 步骤，确保 `.gitcode/actions/probe-node16/action.yml` 等文件存在且可被加载
- 零 shell 输出本身是平台诊断信号缺失的体现：即使 action 加载失败，runner 也应输出失败原因而非静默退出
- 相关用例: COMPAT-ACTION 系列所有需要本地 action 的用例
