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
| 3 | trigger 复杂 | 仅 schedule |
| 4 | 长时间等待（timing assertions） | `max_queued_to_running_seconds` 等时序断言 |
| 5 | UI 检查（`ui_visual` / `ui_interaction` / `ui_layout`） | 需要浏览器自动化 |

## 工作步骤

### Step 1: 准备 accessable 目录

从 expect-execute-consistency 报告中提取"断言一致"的 case ID，将对应 YAML 文件从 `phase01/runs/2026-07-23-01/cases/yaml/` 复制到 `phase02/agents/scriptable-classify/inputs/accessable/`。

### Step 2: 逐 case 判定

对每个 accessable YAML，逐条检查 §判定规则。命中任意一条 → 移至 `not-scriptable/`，否则移至 `scriptable/`。

### Step 3: 输出汇总

输出 `scriptable-classify/output/` 下的文件结构：

```
scriptable-classify/output/
├── scriptable/          ← 可通过 dispatch API 自动执行的 YAML
├── not-scriptable/      ← 被规则命中的 YAML
└── report.md            ← 汇总：各类数量、每个 not-scriptable 的原因
```

输出到 `phase02/agents/scriptable-classify/output/report.md`：

```markdown
# Scriptable Classify Report

## 总览

| 分类 | 数量 |
|------|:---:|
| scriptable | N |
| not-scriptable | N |

## 不可脚本化明细

| Case ID | 命中规则 |
|---------|------|
| xxx | trigger = schedule |
```

## 护栏

- **不** 执行 dispatch / deploy 操作。
- **不** 修改源 YAML。
- 仅判定可脚本化性，不判定平台合法性。