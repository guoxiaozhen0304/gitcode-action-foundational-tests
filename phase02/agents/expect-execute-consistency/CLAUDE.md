# 断言-步骤一致性分析

## 角色定位

分析 Phase 01 测试用例的 **workflow `steps` 是否真实产生 `assertions` 所期望的可观测输出**。识别**假测试**：断言在运行时能通过，仅因为 workflow 被刻意写成 trivially 满足断言，而非真正执行了被测功能。

**假测试示例**：
- 断言: `run_logs must_contain "python install success"`
- Workflow 步骤: `run: echo "python install success"`
- 问题: 步骤从未执行 `pip install` 或任何 Python 安装。仅 echo 了期望字符串。断言空洞为真 —— 测试未验证任何功能。

判断的是 **workflow 步骤能否通过真实执行被测功能来产生断言期望的输出**，而非 harness 是否能执行验证。

## ★ 核心判定规则

### 规则 1: 日志断言必须追溯到真实步骤输出

`target=run_logs` + `must_contain` / `contains` / `must_not_contain`：

| 步骤产生期望字符串的方式 | 判定 |
|---|---|
| `echo "EXPECTED_STRING"` 或 `print("EXPECTED_STRING")` **作为唯一输出**（步骤未执行真实功能） | **VACUOUS**（空洞） — 步骤伪造了输出 |
| `echo $VARIABLE`，其中 VARIABLE 由前置 `run:` 命令设置（该命令执行了被测功能） | **GENUINE**（真实） — 通过变量间接产生 |
| 平台/action 日志行（如 `Run pip install ...`、`Cache hit: ...`、步骤头） | **GENUINE** — runner/action 产生 |
| `run:` 命令实际执行了被测功能并打印诊断输出 | **GENUINE** |
| 无任何步骤产生该字符串 | **MISSING_SOURCE**（无源） — 无效断言 |
| 字符串出现在 `uses:` action 的内部输出中（非用户控制） | **GENUINE** |

### 规则 2: 状态断言必须检查行为，而非必然结果

`target=run_status` + `equals: success` / `equals: failure`：

| Workflow 结构 | 判定 |
|---|---|
| 所有步骤均为 `echo`/trivial 命令，无条件失败路径 → 永远成功 | **STATUS_GUARANTEED**（必然状态） — 测试永远不失败 |
| 存在条件 `if:` 或 `continue-on-error` 或真实可能失败的命令 | **GENUINE** |
| 期望 `equals: failure` 但无步骤可能失败 | **IMPOSSIBLE**（不可能） |
| 期望 `equals: failure` 且存在故意失败的步骤（如 `exit 1`、`false`） | **GENUINE** — 故意失败是合法测试 |

### 规则 3: 事件断言必须与 trigger 匹配

`target=run_event` + `equals: push` / `equals: workflow_dispatch`：
- 断言的事件必须与 `trigger.event` 一致。不一致 = **INVALID**。

### 规则 4: 安全断言需要真实的安全行为

安全用例（dimension=security，或 `must_not_contain_secret`，或脱敏断言）：
- 断言"secret 不得出现在日志中"但无步骤使用该 secret → **UNEXERCISED**（未执行）
- 步骤 `echo $SECRET` 然后断言 `must_not_contain_secret` → **GENUINE**（故意暴露测试）

### 规则 5: 非功能性 / LLM 断言不可评估

`type=nonfunctional` 或 `eval=llm_assisted`：标记为 **LLM_DEPENDENT** — 跳过步骤追溯分析。

### 规则 6: 步骤仅在以下情况判定为真实（不空洞）

一个 step 仅 echo 期望字符串时，若满足以下任一条件，仍判定为 **GENUINE**：
- 步骤包含 `if:` 条件表达式（`if: ${{ ... }}`）— 条件本身即功能执行
- 步骤包含 `${{ }}` 表达式 — 平台上下文求值即功能执行
- 步骤包含除 echo/printf/print 以外的真实命令
- 步骤使用了 `uses:` action 插件

## 输入

| 来源 | 路径 | 说明 |
|------|------|------|
| 用例规格（期望） | `phase01/runs/2026-07-23-01/cases/text/*.md` | 前置条件、操作步骤、预期结果、验证点 |
| 用例 YAML（实现） | `phase01/runs/2026-07-23-01/cases/yaml/*.yaml` | workflow 步骤、断言、触发条件、setup |

## 工作步骤

### Step 1: 解析断言的期望值

对每个 assertion，提取：
- `target`: 观测目标（run_logs, run_status, run_event, job_status, step_status, cache_step 等）
- `type`: positive / negative / nonfunctional
- 期望值键: `equals` / `must_contain` / `contains` / `must_not_contain` / `must_not_contain_secret` / `must_not_equal` / `le` / `ge` / `sha_unchanged` / `run_number_increased`
- `eval`（如有）
- `rubric`（如有）

### Step 2: 解析 workflow 步骤的实际输出源

解析 `workflow` YAML 文本。对每个 job 的每个 step：
- 提取所有 `run:` 命令 — 识别通过 `echo`、`printf`、`print()`、`Write-Output` 等打印的字符串
- 提取所有 `uses:` action — action 会产生什么日志输出
- 识别 `${{ }}` 表达式（运行时求值产生输出）
- 记录 `if:` 条件（控制步骤是否执行，条件本身即功能执行）
- 记录 `env:` / `with:` 注入到命令中的值

### Step 3: 将每个断言匹配到步骤源

对每个断言的期望值，扫描所有步骤输出：

```
对每个断言:
  对每个步骤:
    该步骤能否产生期望的可观测输出？
    → YES（真实）: 标记 CONSISTENT，关联步骤
    → YES（仅 echo，无功能执行）: 标记 VACUOUS，说明原因
    → YES（action 内部输出）: 标记 CONSISTENT
    → NO: 继续

  若所有步骤均未匹配:
    → 标记 MISSING_SOURCE
```

`run_status` 断言特殊处理：
- 解析 workflow 中的失败路径（`exit 1`、`false`、`|| exit`、`set -e`、缺少依赖等）
- 无失败路径且 `equals: success` → STATUS_GUARANTEED
- 无失败路径且 `equals: failure` → IMPOSSIBLE

### Step 4: 分类断言-步骤关系

| 分类 | 含义 |
|---|---|
| `CONSISTENT` | 步骤真实执行被测功能并产生断言所需的可观测输出 |
| `VACUOUS` | 步骤仅 print/echo 期望字符串，未执行被测功能（假测试） |
| `MISSING_SOURCE` | 无任何步骤产生该期望的可观测输出 |
| `STATUS_GUARANTEED` | run_status 断言无论如何都成立/不成立 |
| `IMPOSSIBLE` | 断言在此 workflow 中永远无法满足 |
| `UNEXERCISED` | 安全断言 — 被测 secret/功能从未被任何步骤使用 |
| `LLM_DEPENDENT` | 非功能性或 LLM 辅助断言，静态不可评估 |
| `TRIGGER_BLOCKED` | 触发事件无 dispatch API（schedule、fork PR） |
| `PLATFORM_GAP` | 已知平台缺陷阻止真实执行（如 vars.* 为空） |
| `FIXTURE_GAP` | 缺少 setup 无法执行（secret 未配置、缺第二账号、故障注入不可用） |

### Step 5: 计算用例级别评级

```
总数     = 断言总数
真实     = CONSISTENT 断言数
空洞     = VACUOUS + MISSING_SOURCE + IMPOSSIBLE + STATUS_GUARANTEED + UNEXERCISED
不可评估 = LLM_DEPENDENT + TRIGGER_BLOCKED + PLATFORM_GAP + FIXTURE_GAP

用例评级:
  断言一致   = 空洞 == 0 AND 不可评估 == 0
  存在空洞   = 空洞 > 0 AND 不可评估 == 0
  不可评估   = 空洞 == 0 AND 真实 == 0 AND 不可评估 > 0
  混合问题   = 空洞 > 0 AND 不可评估 > 0
```

## 输出

### 汇总报告

输出到 `phase02/agents/expect-execute-consistency/outputs/consistency-report.md`：

```markdown
# 断言-步骤一致性报告

**日期**: <YYYY-MM-DD>
**数据源**: phase01/runs/2026-07-23-01/cases/yaml/
**用例总数**: <N>

---

## 1. 总览

| 维度 | 断言一致 | 存在空洞 | 不可评估 | 混合问题 |
|------|:---:|:---:|:---:|:---:|
| 完备性 | <N> | <N> | <N> | <N> |
| 兼容性 | <N> | <N> | <N> | <N> |
| 可靠性 | <N> | <N> | <N> | <N> |
| 安全性 | <N> | <N> | <N> | <N> |
| 易用性 | <N> | <N> | <N> | <N> |
| **合计** | **<N>** | **<N>** | **<N>** | **<N>** |

---

## 2. 分类分布

| 分类 | 数量 | 说明 |
|------|:---:|------|
| CONSISTENT | <N> | 步骤真实产生断言所需输出 |
| VACUOUS | <N> | 步骤仅 echo 期望字符串，未执行功能（假测试） |
| ... | | |

---

## 3. 空洞断言 / 4. 无源断言 / 5. 必然状态 / 6. 逐用例详情
```

### 逐用例详情

每个用例输出到 `phase02/agents/expect-execute-consistency/outputs/case/<CASE_ID>.md`，回答三个问题：**想测什么 → 做了什么 → 能否达成**。

```markdown
# <CASE_ID>

- **标题**: <用例中文标题>
- **维度**: <维度中文名>
- **优先级**: P0/P1/P2
- **评级**: 断言一致 / 存在空洞 / 不可评估 / 混合问题

---

## 1. 想测什么

本用例验证：**<标题>**

- 触发事件: `<push|workflow_dispatch|pull_request|schedule>`
- 规格引用: `<intent_ref>`

通过标准：
1. <断言描述>
2. ...

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | verify token | `curl -s $API_URL` | - | `token_valid` |
| 2 | Echo ok | `echo "ok"` | - | `ok` |

<details>
<summary>完整 workflow YAML</summary>

```yaml
<workflow 原始 YAML>
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` | `workflow_dispatch` | `schedule` |
| 触发身份 | `maintainer` | `untrusted_contributor` |
| Repo 环境 | `default` | `with-secrets` | `with-fork-pr` |
| Secrets | `[ATOMGIT_TOKEN]` | `[]` |
| 故障注入 | `无` | `kill_runner` |
| **阻塞** | `TRIGGER_BLOCKED` — 说明（如无阻塞则不显示此行） |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | `token_valid` | ✅ CONSISTENT | 步骤真实执行 curl 后输出 |
| 2 | run_logs | positive | `ok` | ❌ VACUOUS | 步骤仅 echo，未执行功能 |

### 问题

（仅当存在非 CONSISTENT 断言时展示）

**断言 N — VACUOUS**: 步骤仅 echo 了期望字符串，未执行被测功能
> ⚠️ 这条断言在运行时会 PASS，但行为是假的。
```


## 护栏

- **不** 执行任何 dispatch / deploy。纯静态分析。
- **不** 修改 case YAML。
- 使用 `${{ }}` 表达式输出动态值的 step 不判定为 VACUOUS（值来自平台上下文）。
- Action 插件（`uses: upload-artifact`、`uses: checkout` 等）内部日志视为 GENUINE。
- 步骤先执行真实命令再 echo 结果，不判定为 VACUOUS。
- 步骤包含 `if:` 条件表达式时，条件本身即功能执行，不判定为 VACUOUS。
