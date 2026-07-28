# Scriptable-Classify / 可脚本化判定

## 角色定位

从**断言一致**的用例中筛出哪些能通过 dispatch API 自动执行。不关心是否欠妥、平台合法性——已由 validate-classify 负责。

输入是 expect-execute-consistency 判定为"断言一致"的 YAML，输出把 YAML 文件分到 `scriptable` / `not-scriptable` 两个文件夹。

## 输入

| 来源 | 路径 |
|------|------|
| 断言一致用例 | `phase02/agents/expect-execute-consistency/outputs/accessable/*.yaml` |

## 判定规则

以下任一条命中 → **not-scriptable**，否则 → **scriptable**。

| # | 规则 | 说明 |
|---|------|------|
| 1 | trigger.event = `schedule` | 无按需 dispatch API |
| 2 | 复杂步骤 — assertion target 需要复杂验证 | harness 仅支持 run_logs/run_status/job_status/step_status/run_event/workflow_parse 这类日志扫描或字段读取 |

**什么是复杂步骤**：

harses 可通过 API 直接读取 run_status、event 等字段，或 grep 日志匹配字符串。但以下 target 需要额外操作，harses 不支持：

| target | 需要的操作 |
|--------|------|
| `artifacts` / `artifact_content` / `artifact_download` | 下载 artifact zip → 解压 → 读取内容 |
| `cache_step` / `cache_pollution` | 跨多次运行对比缓存状态 |
| `rerun_context` | rerun API → 对比两次运行的 sha/run_number |
| `step_summary` | 下载 job log → 解析 step summary 字段 |

**示例**：

`SEC-SIDECHAN-02-001` 的第三个断言 `target: artifacts` 需要下载 artifact 后搜索 secret 明文，harness 仅能 grep 日志，无法做到。

```yaml
assertions:
  - type: negative
    target: artifacts    # ← complex: 需要 artifact_download
    eval: "deterministic"
    rubric: "artifact 内容不含 secret 明文"
```

`COMP-CALL-01-001`：2 层 workflow_call 嵌套正常执行。验证嵌套调用链需要检查多个子工作流 run 的 status/event，harness 仅能扫描当前 run 的日志和字段，无法跨 run 验证调用链。

`COMP-ARTIFACT-01-003`：artifact 保留期设置生效 (retention-days)。验证保留期实际生效需要检查 artifact service 在过期后 artifact 是否被删除，属于 artifact-level 操作，harness 不支持。

`REL-FAULT-01-031`：故障注入——runner 进程被 SIGKILL。`fault_injection.action: kill_runner` 需要在 job 执行过程中向 runner 注入 SIGKILL，harness 仅能 dispatch 和轮询，无法注入运行时故障。

`REL-FAULT-01-032`：故障注入——网络分区。`fault_injection.action: network_partition` 需要制造网络隔离，harness 不支持。

`REL-FAULT-01-033`：故障注入——磁盘满。`fault_injection.action: disk_full` 需要填满 runner 磁盘，harness 不支持。

`REL-FAULT-01-034`：故障注入——并发洪水。`fault_injection.action: concurrent_flood` 需要触发大量并发 dispatch，harness 无法精确控制并发量和时序。

`REL-FAULT-01-035`：故障注入——并发洪水。同上。

| 3 | trigger 复杂 | 仅 schedule |
| 4 | 长时间等待（timing assertions） | `max_queued_to_running_seconds` 等时序断言 |
| 5 | UI 检查（`ui_visual` / `ui_interaction` / `ui_layout`） | 需要浏览器自动化 |

### 硬编码不可脚本化

以下 case 无需规则判定，直接归入 `not-scriptable`。即使 assertion target 为简单字段，其验证需要平台特性差异理解、跨运行对比或语义判断，harness 无法全自动执行。

| Case ID | 原因 |
|---------|------|
| COMP-ARTIFACT-01-001 | artifact 跨 job 传递 |
| COMP-ARTIFACT-01-002 | artifact 批量下载 |
| COMP-ARTIFACT-01-003 | artifact 保留期设置生效 |
| COMP-CACHE-01-001 | cache 命中/恢复 |
| COMP-CACHE-01-002 | cache 跨 job 隔离 |
| COMP-PERMS-01-001 | permissions 权限作用域 |
| COMP-PERMS-01-002 | permissions 继承与覆盖 |
| COMP-PERMS-01-003 | permissions 与 secret 交互 |
| COMP-PR-01-001 | PR 双向 fork 合并 |
| COMP-PR-01-003 | PR 关闭后 workflow 终止 |
| COMP-SECRET-01-001 | secret 跨 job 可用性 |
| COMP-SUMMARY-01-001 | step_summary Markdown 渲染 |
| COMP-TIMEOUT-01-002 | 超时后 job 状态转换 |
| COMPAT-CONTAINER-01-001 | 容器化 runner 行为差异 |
| COMPAT-DEPR-01-002 | 废弃字段向后兼容 |
| COMPAT-INPUTS-01-001 | workflow_call inputs 类型校验 |
| COMPAT-MATRIX-01-003 | matrix 策略差异 |
| COMPAT-MATRIX-01-004 | matrix include 无基础变量不被支持时的差异 |
| COMPAT-OUTCOME-01-002 | continue-on-error true 时 outcome 应为 failure 而 conclusion 应为 success |
| COMPAT-OUTCOME-01-003 | outcome 与 conclusion 在 job 条件判断中不应互换语义 |
| COMPAT-PERM-01-001 | 未声明 permissions 时默认 TOKEN 读操作权限范围 |
| COMPAT-PR-01-006 | PR 目标分支过滤行为差异 |
| COMPAT-VARS-01-006 | vars 在 Action 中的可用性差异 |
| REL-ART-01-041 | artifact 可靠性 |
| REL-ARTCONC-01-063 | artifact 并发上传 |
| REL-ARTPERF-01-053 | artifact 上传/下载性能 |
| REL-ARTPERF-01-053-V2 | 同上 V2 |
| REL-BIGRUNNER-01-066 | 大规格 runner 稳定性 |
| REL-CANCEL-01-028 | workflow 取消后状态一致性 |
| REL-CONTINUE-01-030 | continue-on-error 后后续 job 执行 |
| REL-FAULT-01-031 | 故障注入——SIGKILL |
| REL-FAULT-01-032 | 故障注入——网络分区 |
| REL-K8S-01-045 | K8s 调度稳定性 |
| REL-MATRIX-01-026 | matrix 大矩阵稳定性 |
| REL-MATRIX-01-038 | matrix 失败隔离 |
| REL-MATRIX-01-039 | matrix 调度延迟 |
| REL-NEEDS-01-025 | needs 依赖链完整性 |
| REL-RUNNER-01-049-V2 | runner 注册/回收 V2 |
| REL-TIMEOUT-01-009 | 超时边界行为 |
| REL-YAMLCACHE-01-060 | YAML 缓存一致性 |
| SEC-BASE-01-001 | 安全基线——token 最小权限 |
| SEC-BASE-01-002 | 安全基线——secret 加密传输 |
| SEC-FORK-01-001 | fork PR token 隔离 |
| SEC-FORK-01-002 | fork PR secret 不可访问 |
| SEC-MASK-01-001 | secret 日志脱敏 |
| SEC-MASK-01-005 | secret 在 artifact 中脱敏 |
| SEC-NAME-01-001 | secret 名称规则校验 |
| SEC-NAME-01-002 | secret 名称 WAF 触发 |
| SEC-PERM-01-003 | permissions 最小权限生效 |
| SEC-PERM-01-004 | permissions 提权检测 |
| SEC-PRTGT-01-001 | pull_request_target token 权限 |
| SEC-PRTGT-01-002 | pull_request_target secret 隔离 |
| SEC-SIDE-01-002 | side-channel artifact 内容泄露 |
| SEC-TOKEN-01-001 | token 过期后请求拒绝 |
| SEC-TOKEN-01-002 | token scope 越权拒绝 |
| USE-ANNOT-01-002 | ::error:: 生成的 PR annotation 具备文件路径、行号与可点击跳转 |
| USE-CONC-01-001 | concurrency.max 配置 0 或 10 时报错应提示有效范围 1-5 |
| USE-CTX-01-001 | 使用 atomgit 上下文时表达式正常求值 |
| USE-CTX-01-002 | 使用 github 上下文时报错应提示 atomgit 替代 |
| USE-DISP-01-002 | workflow_dispatch 未提供参数但存在 default 时应使用默认值运行 |
| USE-ENV-01-002 | 引用 GITHUB_SHA 时日志应给出环境变量映射提示 |
| USE-EXPR-01-001 | 引用不存在的上下文属性时报错应包含原始表达式与错误类型 |
| USE-INPT-01-002 | 使用 boolean 类型 input 时报错应提示仅支持 string |
| USE-LOG-01-001 | 多 step 日志按时间线组织且边界清晰 |
| USE-MD-01-001 | ATOMGIT_STEP_SUMMARY 写入的 Markdown 正确渲染为 HTML |
| USE-OS-01-001 | runner.os 返回值与文档声明的平台支持一致 |
| USE-SECNAME-01-001 | Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误 |

### 负向/不可自证类

**问题**：「证明某事不发生」（无新运行、无丢失、无排队饿死）单次 workflow 执行无法自证，观测点本就在 harness 侧（运行列表对账、多次编排采样）。这是用例设计的固有分层，以下 case 全部硬编码为 `not-scriptable`：

- 并发/排队/限流：`REL-CONC-01-001`、`REL-PRESSURE-01-055`、`REL-PROJLIMIT-01-067`、`REL-PROJLIMIT-01-068`、`REL-QUEUE-01-003`、`REL-K8S-01-045`
- 取消/抢占：`REL-CANCEL-01-028`、`REL-PREEMPT-01-005`
- 故障注入：`REL-FAULT-01-031` 至 `REL-FAULT-01-038`
- Rerun 次数/时限：`COMP-RERUN-01-002`、`COMP-RERUN-01-003`、`REL-RERUN-01-011`、`REL-RERUN-01-012`、`REL-RERUN-01-013`
- 条件式负向：`COMPAT-EXPR-01-002`、`COMPAT-EXPR-01-003`（条件表达式不触发时无法观测「未触发」）
- 饿死/丢失点：`REL-NEEDS-01-025`、`REL-MATRIX-01-026`、`REL-MATRIX-01-038`、`REL-MATRIX-01-039`

## 工作步骤

### Step 1: 准备 accessable 目录

从 expect-execute-consistency 报告中提取"断言一致"的 case ID，将对应 YAML 文件从 `phase01/runs/2026-07-23-01/cases/yaml/` 复制到 `phase02/agents/scriptable-classify/inputs/accessable/`。

### Step 2: 逐 case 判定

对每个 accessable YAML，逐条检查 §判定规则。命中任意一条 → 移至 `not-scriptable/`，否则移至 `scriptable/`。

### Step 3: 生成报告

分类完成后，基于 `scriptable/` 和 `not-scriptable/` 的实际文件生成 `output/report.md`。

输出目录结构：

```
scriptable-classify/output/
├── scriptable/          ← 可通过 dispatch API 自动执行的 YAML
├── not-scriptable/      ← 被规则命中的 YAML
└── report.md            ← 汇总：各类数量、每个 not-scriptable 的原因
```

报告必须包含：

1. **总览**：scriptable / not-scriptable 数量
2. **按规则分布**：Rule 1/2/2b/4/5/Hardcoded 各自数量
3. **不可脚本化明细**：按规则分组列出所有 case ID

用 Python 扫描 `not-scriptable/` 目录中每个 YAML，按优先级判定归属规则（Hardcoded > Rule 1 > Rule 2b > Rule 2 > Rule 4 > Rule 5），写入 `report.md`。

```markdown
# Scriptable Classify Report

## 总览
| 分类 | 数量 |
|------|:---:|
| scriptable | N |
| not-scriptable | N |

## 按规则分布
| 规则 | 数量 |
|------|:---:|
| Rule 1 (schedule) | N |
| Rule 2 (complex target) | N |
| Rule 2b (fault injection) | N |
| Rule 4 (timing) | N |
| Rule 5 (UI) | N |
| Hardcoded | N |

## 不可脚本化明细
### Rule 1: schedule trigger
- CASE-ID

### Rule 2: complex target
- CASE-ID

...
```

## 护栏

- **不** 执行 dispatch / deploy 操作。
- **不** 修改源 YAML。
- 仅判定可脚本化性，不判定平台合法性。