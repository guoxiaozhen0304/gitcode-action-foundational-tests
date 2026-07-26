# Phase 01 意图与 Case 关联覆盖报告

## 0. 分析元数据

- 分析提示词：`仓库的测试意图全集在 phase01/result/2026-07-22-01/intents，分析 phase01/runs/2026-07-23-01/cases/yaml 中的 369 个用例是否覆盖这些意图。输出一个意图和 case 关联的报告，md 格式，输出到 eval 目录下。`
- 模型：`gpt-5.6-luna`
- 分析时间：2026-07-27，时区 `Asia/Shanghai`
- 工作目录：`/home/lcr/gitcode-action-foundational-tests`
- 主要工具及版本：`Python 3.13.14`、`ripgrep 15.2.0`、`git 2.47.3`、`rtk 0.43.0`
- 分析方法：使用 Python 标准库读取 YAML 文本/结构、使用 `pathlib` 收集文件、使用集合比对意图 ID 与 `intent_ref`，并使用 `rg` 进行仓库检索。

## 1. 报告范围

- 意图来源：`phase01/result/2026-07-22-01/intents/`
- Case 来源：`phase01/runs/2026-07-23-01/cases/yaml/`
- 分析方式：静态读取每个 YAML 的 `intent_ref`，与意图文件中的 `INTENT-*` ID 做集合比对；同时抽查意图标题、Case 标题和断言目标的一致性。
- 本报告不代表已实际执行这些 Case。

## 2. 总结结论

| 指标 | 数量 | 结论 |
|---|---:|---|
| 意图总数 | 185 | 以意图文件中出现的唯一 ID 计 |
| Case 总数 | 369 | YAML 文件数 |
| 至少被一个 Case 引用的意图 | 184 | 引用覆盖率 99.5% |
| 没有 Case 的意图 | 1 | `INTENT-USE-029` |
| 引用已存在意图的 Case | 325 | 可进入有效关联统计 |
| 引用不存在意图的 Case | 44 | 孤立关联，不能算覆盖 |
| Case 中唯一 `intent_ref` 数 | 218 | 包含 34 个不存在的意图 ID |

结论：当前是“高引用覆盖、非全集有效覆盖”。不能把 369 个 Case 直接判定为覆盖全部意图：存在 1 个漏测意图、44 个孤立 Case，以及若干已有 ID 下的语义错配。

## 3. 按维度统计

| 维度 | 意图数 | 有 Case 的意图 | 未覆盖意图 | 有效关联 Case | 孤立 Case |
|---|---:|---:|---|---:|---:|
| completeness | 18 | 18 | 无 | 46 | 42 |
| compatibility | 35 | 35 | 无 | 107 | 0 |
| reliability | 66 | 66 | 无 | 72 | 2 |
| security | 36 | 36 | 无 | 51 | 0 |
| usability | 30 | 29 | `INTENT-USE-029` | 49 | 0 |
| **合计** | **185** | **184** | **1** | **325** | **34 个 ID / 44 个文件** |

注意：`孤立 Case` 按文件数计为 44；按不存在的唯一 `intent_ref` 计为 34。

## 4. 意图 → Case 关联清单

下面的数字是每个意图被有效 Case 引用的数量。`0` 表示没有关联 Case；孤立 ID 不列入有效数量。

### 4.1 completeness

| 意图 | Case 数 |
|---|---:|
| `INTENT-COMP-001` | 2 |
| `INTENT-COMP-002` | 2 |
| `INTENT-COMP-003` | 3 |
| `INTENT-COMP-004` | 3 |
| `INTENT-COMP-005` | 3 |
| `INTENT-COMP-006` | 2 |
| `INTENT-COMP-007` | 3 |
| `INTENT-COMP-008` | 2 |
| `INTENT-COMP-009` | 3 |
| `INTENT-COMP-010` | 3 |
| `INTENT-COMP-011` | 2 |
| `INTENT-COMP-012` | 3 |
| `INTENT-COMP-013` | 3 |
| `INTENT-COMP-014` | 2 |
| `INTENT-COMP-015` | 3 |
| `INTENT-COMP-016` | 3 |
| `INTENT-COMP-017` | 2 |
| `INTENT-COMP-018` | 2 |

这 18 个意图的有效 Case 主要是 `COMP-DIR`、`COMP-UNKNOWN`、`COMP-PUSH`、`COMP-PR`、`COMP-SCHEDULE`、`COMP-CALL`、`COMP-STAGES`、`COMP-TIMEOUT`、`COMP-RERUN`、`COMP-RUNNER`、`COMP-ISOLATION`、`COMP-SECRET`、`COMP-PERMS`、`COMP-PRTARGET`、`COMP-ARTIFACT`、`COMP-CACHE`、`COMP-STATUS`、`COMP-SUMMARY`。

另有 42 个 completeness Case 使用了意图库不存在的 `INTENT-COMP-*` ID，详见第 5 节。

### 4.2 compatibility

| 意图 | Case 数 | 意图 | Case 数 |
|---|---:|---|---:|
| `INTENT-COMPAT-001` | 5 | `INTENT-COMPAT-019` | 1 |
| `INTENT-COMPAT-002` | 3 | `INTENT-COMPAT-020` | 3 |
| `INTENT-COMPAT-003` | 6 | `INTENT-COMPAT-021` | 3 |
| `INTENT-COMPAT-004` | 6 | `INTENT-COMPAT-022` | 6 |
| `INTENT-COMPAT-005` | 3 | `INTENT-COMPAT-023` | 2 |
| `INTENT-COMPAT-006` | 3 | `INTENT-COMPAT-024` | 2 |
| `INTENT-COMPAT-007` | 5 | `INTENT-COMPAT-025` | 2 |
| `INTENT-COMPAT-008` | 4 | `INTENT-COMPAT-026` | 2 |
| `INTENT-COMPAT-009` | 5 | `INTENT-COMPAT-027` | 2 |
| `INTENT-COMPAT-010` | 3 | `INTENT-COMPAT-028` | 2 |
| `INTENT-COMPAT-011` | 3 | `INTENT-COMPAT-029` | 3 |
| `INTENT-COMPAT-012` | 4 | `INTENT-COMPAT-030` | 2 |
| `INTENT-COMPAT-013` | 3 | `INTENT-COMPAT-031` | 2 |
| `INTENT-COMPAT-014` | 2 | `INTENT-COMPAT-032` | 3 |
| `INTENT-COMPAT-015` | 2 | `INTENT-COMPAT-033` | 2 |
| `INTENT-COMPAT-016` | 3 | `INTENT-COMPAT-034` | 2 |
| `INTENT-COMPAT-017` | 3 | `INTENT-COMPAT-035` | 3 |
| `INTENT-COMPAT-018` | 1 |  |  |

### 4.3 reliability

`INTENT-REL-001` 至 `INTENT-REL-048` 均有 1 个有效 Case；`INTENT-REL-049` 至 `INTENT-REL-053` 分别有 2、2、2、2、2 个 Case；`INTENT-REL-054` 至 `INTENT-REL-063` 均有 1 个有效 Case；`INTENT-REL-064` 有 2 个；`INTENT-REL-065` 和 `INTENT-REL-066` 各有 1 个。

`INTENT-REL-067`、`INTENT-REL-068` 各有 1 个 Case 文件引用，但这两个 ID 不存在于当前 reliability 意图库，因此不计入有效覆盖。对应文件为 `REL-PROJLIMIT-01-067.yaml` 和 `REL-PROJLIMIT-01-068.yaml`。

### 4.4 security

| 意图范围 | Case 分布 |
|---|---|
| `INTENT-SEC-001` 至 `004` | 分别为 2、2、2、2 |
| `INTENT-SEC-005` 至 `013` | 分别为 1、1、1、1、1、1、1、1、1 |
| `INTENT-SEC-014` | 2 |
| `INTENT-SEC-015` | 1 |
| `INTENT-SEC-016` 至 `019` | 分别为 2、2、2、2 |
| `INTENT-SEC-020` 至 `026` | 均为 1 |
| `INTENT-SEC-027` | 2 |
| `INTENT-SEC-028`、`029` | 各 1 |
| `INTENT-SEC-030` 至 `032` | 分别为 2、2、2 |
| `INTENT-SEC-033`、`034` | 各 1 |
| `INTENT-SEC-035`、`036` | 各 2 |

### 4.5 usability

| 意图范围 | Case 分布 |
|---|---|
| `INTENT-USE-001` 至 `010` | 每个 2 个 |
| `INTENT-USE-011` 至 `015` | 每个 1 个 |
| `INTENT-USE-016` | 2 |
| `INTENT-USE-017` 至 `020` | 每个 1 个 |
| `INTENT-USE-021` | 2 |
| `INTENT-USE-022` 至 `025` | 每个 2 个 |
| `INTENT-USE-026` 至 `028` | 每个 2 个 |
| `INTENT-USE-029` | **0，未覆盖** |
| `INTENT-USE-030` | 2 |

## 5. 孤立 Case 清单

以下 Case 的 `intent_ref` 在意图目录中不存在：

| Case 文件组 | 引用的不存在 ID |
|---|---|
| `COMP-ATOMGIT-01-047.yaml` 至 `049.yaml` | `INTENT-COMP-047` 至 `049` |
| `COMP-BOUND-01-084.yaml` 至 `088.yaml` | `INTENT-COMP-084` 至 `088` |
| `COMP-CTX-01-051.yaml` 至 `053.yaml` | `INTENT-COMP-051` |
| `COMP-ENVCTX-01-050.yaml` | `INTENT-COMP-050` |
| `COMP-EXPR-01-054.yaml` 至 `058.yaml` | `INTENT-COMP-054` 至 `058` |
| `COMP-JOB-01-066.yaml`、`067.yaml` | `INTENT-COMP-066` |
| `COMP-JOB-01-068.yaml` | `INTENT-COMP-067` |
| `COMP-RUNNER-01-080.yaml` | `INTENT-COMP-080` |
| `COMP-SCRIPT-01-081.yaml`、`082.yaml` | `INTENT-COMP-081` |
| `COMP-STEP-01-069.yaml` 至 `071.yaml` | `INTENT-COMP-069` |
| `COMP-SYSENV-01-059.yaml`、`060.yaml` | `INTENT-COMP-059` |
| `COMP-TRIG-01-072.yaml` 至 `079.yaml` | `INTENT-COMP-072` 至 `079` |
| `COMP-VARREF-01-083.yaml` | `INTENT-COMP-083` |
| `COMP-WFLOW-01-061.yaml`、`062.yaml`、`064.yaml`、`065.yaml` | `INTENT-COMP-061` |
| `COMP-WFLOW-01-063.yaml` | `INTENT-COMP-063` |
| `REL-PROJLIMIT-01-067.yaml` | `INTENT-REL-067` |
| `REL-PROJLIMIT-01-068.yaml` | `INTENT-REL-068` |

## 6. 语义关联质量问题

仅检查 `intent_ref` 是否存在仍然不够。部分已存在的 ID 下，Case 标题与意图主题不一致，说明关联字段可能来自另一套编号体系。例如：

| 意图 | 意图主题 | 发现的错配 Case |
|---|---|---|
| `INTENT-COMPAT-001` | 默认 shell、默认工作目录 | `COMPAT-CONTAINER-01-001/002`：container 不支持 |
| `INTENT-COMPAT-002` | 未声明 permissions 的默认权限 | `COMPAT-SECRET-01-005`：环境级 secrets |
| `INTENT-COMPAT-003` | step/job 默认成功条件 | 多个 PR types、PR paths、PR 分支过滤 Case |
| `INTENT-COMPAT-004` | `success()`、`always()` 等状态函数 | 多个 `issue_comment types` Case |
| `INTENT-COMPAT-005` | `failure()` 与 `failed` 命名差异 | concurrency preemption Case |
| `INTENT-COMPAT-006` | `contains` 边界行为 | 跨 Job 未声明 output Case |
| `INTENT-COMPAT-007` | `hashFiles` 边界行为 | matrix include/exclude Case |
| `INTENT-COMPAT-008` | `toJson`/表达式或对应兼容差异 | self-hosted、内网 Runner Case |
| `INTENT-COMPAT-009` | loose equality 边界行为 | workflow command Case |
| `INTENT-COMPAT-010` | Action 元数据/函数降级 | `join()`、`fromJSON()` Case，主题相近但需确认意图定义是否包含二者 |

因此 compatibility 维度虽然形式上为 35/35 覆盖，仍应进行一次标题/验证点级别的重新归属。

## 7. 断言完整性观察

369 个 Case 共包含：

- positive：476 条
- negative：187 条
- nonfunctional：96 条

大多数断言都包含明确的 `equals`、`contains`、`must_contain`、`must_not_contain`、范围比较或 `rubric` 字段；但 usability 中的文档/UI 类 Case 依赖 `llm_assisted` 或人工评估，不能仅凭 YAML 静态结构确认覆盖质量。

## 8. 建议的修复顺序

1. 建立唯一的意图 ID 清单校验，先阻断不存在的 `intent_ref`。
2. 为 `INTENT-USE-029` 增加 Case，或明确将该意图从全集中移除。
3. 为 44 个孤立 Case 创建正式意图，或将其改关联到现有意图。
4. 重点重排 `INTENT-COMPAT-001` 至 `013` 的 Case 归属。
5. 在 CI 中增加三项检查：意图引用存在性、维度一致性、每个意图至少一个正/负向验证点。
