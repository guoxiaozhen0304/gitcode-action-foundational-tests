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
| 2 | trigger.event = `pull_request` / `pull_request_target` / `issue_comment` | 平台不触发这些事件 |
| 3 | trigger.as = `untrusted_contributor` | 需要 fork PR 编排（虽有多账号 token，但 infra 未实现） |
| 4 | 步骤中包含 `services:` | 容器 service 启动慢且不稳定 |
| 5 | fault_injection != null | 故障注入基础设施不可用 |
| 6 | assertions 中有 `ui_visual` / `ui_interaction` / `ui_layout` | 需要浏览器自动化 |
| 7 | assertions 中有 `max_queued_to_running_seconds` / `avg_queued_to_running_seconds` | 时序性断言不可自动化 |
| 8 | assertions 中有 `eval: llm_assisted` | 需要 LLM 评估 |
| 9 | setup.secrets 中有非 ATOMGIT_TOKEN 的 secret | secret 未在 .env 配置 |

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