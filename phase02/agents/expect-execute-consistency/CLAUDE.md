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
| 用例 YAML（实现） | `phase02/agents/expect-execute-consistency/outputs/accessable/*.yaml` | workflow 步骤、断言、触发条件、setup（从 phase01 YAML 复制） |
| 反馈 | `phase02/agents/expect-execute-consistency/feedback.md` | 历史报告的反馈记录 |


## 工作步骤

### Step 1: 阅读规格

从 `text/<ID>.md` 提取：标题、前置条件、操作步骤、预期结果、**验证点**列表。

### Step 2: 阅读实现

从 `yaml/<ID>.yaml` 提取 `workflow:` 中的步骤（run/uses/if/env/with），以及 `assertions:`。

### Step 3: 逐验证点对照

对规格中每条 `[正向]` / `[负向]` 验证点，判断实现步骤是否能验证它。

**⚠️ 一致性与可调度性无关。** 以下 trigger 事件均可调度，不要因为 trigger 类型而标记 BLOCKED：
- `push`、`workflow_dispatch`、`pull_request`、`pull_request_target`、`issue_comment`、`schedule`
- 不要因为 secret 未配置或需要第二账号而标记 FIXTURE_GAP。

**⚠️ 平台验证型用例：** 如果 workflow YAML 本身存在语法错误（缩进错误、非法字段等），且断言要求 `run_status != COMPLETED`（期望平台拒绝该 YAML），则该断言应判为 **COVERED** — 用例通过 `batch_validate.py` 即可验证平台是否拒绝畸形 YAML，不需要实际 dispatch。

判定规则：

| 情况 | 判定 |
|------|------|
| 步骤真实执行了验证点描述的行为，且断言能观测到结果 | **COVERED** |
| 步骤仅 echo/printf 字面量，无 if 条件、无 ${{ }}、无 $ATOMGIT_* 写入、无 uses action、无实质命令 | **TRIVIAL** |
| 验证点是 [负向]（证明某事未发生），但单次 workflow 执行无法证明否定行为 | **UNVERIFIABLE** |
| 验证点是 [负向]，但 YAML 中有 type=negative 断言直接覆盖 | **COVERED** |
| 无任何步骤产出验证点需要的输出 | **MISSING** |

实质命令包括但不限于：curl、pip、npm、python、make、grep、diff、cat >、[[ ]]、$( )、export、if/fi、写入 $ATOMGIT_ENV/PATH/OUTPUT/STEP_SUMMARY。

### Step 4: 评级

逐验证点的判定汇总：

| 评级 | 条件 |
|------|------|
| **断言一致** | 所有验证点 COVERED |
| **部分不符** | 部分 COVERED，部分 TRIVIAL / UNVERIFIABLE / MISSING |
| **完全不符** | 全部 TRIVIAL / UNVERIFIABLE / MISSING |

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
