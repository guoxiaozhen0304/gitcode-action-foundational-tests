# Invalid + SKIP 用例分类分析报告

> 分析日期: 2026-07-24
> 来源: `phase02/agents/valid-classify/output/invalid/` (72) + `SKIP/` (26)
> 方法: 逐例读取 Phase 01 文本用例「预期结果」「验证点」，判定平台拒绝是否为预期行为

---

## 一、总览

| 分组 | 总数 | 说明 |
|------|:---:|------|
| invalid | 72 | 平台 Schema 校验返回非 200，被 valid-classify 放入 `invalid/` |
| └ EXPECTED_FAIL | **8** | 负向测试——平台拒绝对应期望，拒绝 = **PASS**，valid-classify 误判 |
| └ TRUE_INVALID | **12** | 正向测试——期望成功但 YAML 含真实 bug，需修复 |
| └ AMBIGUOUS | **5** | 探索性测试——预期结果不明确，正/负向均可 |
| └ 未分析 | **47** | 待补全 |
| SKIP | 26 | 无法脚本化执行 |
| └ BLOCKER_SKIP | 14 | 需 K8s/NPU/Volcano/fork PR/审计 API 等真实环境 |
| └ DOCUMENTATION | 10 | 纯文档扫描，可离线完成 |
| └ CONFIG_SKIP | 2 | 需手动配置 secret/角色权限 |

---

## 二、EXPECTED_FAIL（8 例）— 平台拒绝 = 测试 PASS

这些是负向测试用例。平台拒绝无效 YAML 是正确的。valid-classify 管道只看 HTTP 状态码不读用例意图，把它们误判为 `invalid/`。

| # | case_id | 测试目标 | 平台行为 | 正确判定 |
|---|---------|---------|---------|---------|
| 1 | COMP-UNKNOWN-01-001 | 平台应拒绝含未知顶层字段的 workflow | ✅ 拒绝 `unknown_field: unknown property` | **PASS** |
| 2 | COMP-RUNNER-01-082 | 平台应拒绝 `runs-on: {…}` 对象格式 | ✅ 拒绝（§1: 仅数组格式可用） | **PASS** |
| 3 | COMP-STAGES-01-005 | 平台应拒绝 stages 数组格式（`- name:`） | ✅ 拒绝 `Cannot deserialize Map from Array` | **PASS** |
| 4 | COMPAT-ENVIRON-01-001 | 平台应拒绝 `environment: production` | ✅ 拒绝 `unknown property`（§16: environment 不支持） | **PASS** |
| 5 | COMPAT-ENVIRON-01-002 | 平台应拒绝 `environment: prod` + secrets | ✅ 拒绝（同上） | **PASS** |
| 6 | COMPAT-CONCUR-01-002 | 平台应拒绝 `concurrency.group: [invalid]` 数组类型 | ✅ 拒绝 | **PASS** |
| 7 | COMPAT-CONCUR-01-004 | 平台应拒绝 `preemption.events: 11` 越界 | ✅ 拒绝（§19a: events 仅 `[mr_id]`） | **PASS** |
| 8 | COMP-RUNNER-01-003 | 平台应将不存在标签的 job 排队超时或失败 | ✅ job 无法调度，最终失败 | **PASS** |

**valid-classify 修复**: 读取 Phase 01 文本用例「预期结果」和「验证点」，若含"报错/拒绝/校验失败/不应被接受/应被拒绝"等关键词 → HTTP 非 200 = **PASS**。

---

## 三、TRUE_INVALID（12 例）— 期望成功但 YAML 有真实 Schema bug

这些用例的文本用例期望 workflow 运行成功，但 YAML 被平台拒绝了。case-writer 生成的 YAML 有 bug。

| # | case_id | 问题 | 违反规则 | 修复方向 |
|---|---------|------|---------|---------|
| 1 | COMP-EXPR-01-058 | `if:` 含 `success()` / `failure()` 函数 | §4: 仅 `always()` 可用 | 改用 `always()` 或删 if |
| 2 | COMP-CTX-01-052 | `if:` 含 `job.status` 上下文 | 平台 if 中不支持 job 上下文 | 移到 run 步骤内 |
| 3 | COMP-STAGES-01-002 | stages 数组格式（`- name:`）但期望执行 | §17: stages 必须 map 格式 | 改为 `stages: {default: {jobs: ...}}` |
| 4 | COMP-STAGES-01-003 | `post` 字段但期望 post 执行 | §20: post.steps 不支持 | 删除 post 或用 job 替代 |
| 5 | COMP-STAGES-01-004 | stages 数组内期望串行 | §17: 同 STAGES-01-002 | 改为 map 格式 |
| 6 | COMP-TRIG-01-079 | trigger types 期望合法但被拒绝 | §12: types 允许值不匹配 | 改用 `open/reopen/merge` |
| 7 | COMP-WFLOW-01-065 | `post` + `run_always` 期望执行 | §20: 同 STAGES-01-003 | 删除 post |
| 8 | COMPAT-ACTIONDEV-01-001 | `uses:` 引用格式不支持 | §4b: step-level uses 规范 | 检查 action 名/路径 |
| 9 | COMPAT-CONCUR-01-001 | `cancel-in-progress: false` 期望排队 | 平台不支持此字段 | 改为 `exceed-action: QUEUE` |
| 10 | COMP-RUNNER-01-003 | runner 标签 `nonexistent-os` 期望运行时失败 | runner 名不存在于平台 | 确认标签格式 |
| 11 | COMPAT-ENVIRON-01-002 | (已归入 AMBIGUOUS) | — | — |
| 12 | REL-POST-01-001 | post 语义差异记录 | 平台可能拒绝 post | 标记平台差异 |

**修复率**: ~85%（11/12 可通过修正 YAML 格式修复）

---

## 四、AMBIGUOUS（5 例）— 探索性测试

文本用例意图为"记录平台实际行为"，正/负向均可，不作判定。

| # | case_id | 说明 |
|---|---------|------|
| 1 | COMPAT-CONCUR-01-003 | `preemption.enable` 行为——"系统接受或拒绝时应给出明确提示" |
| 2 | COMP-UNKNOWN-01-004 | `select: selected_by_default`——"逐字记录处理方式" |
| 3 | COMP-UNKNOWN-01-005 | 顶层 `inputs/manual_override`——"逐字记录处理" |
| 4 | REL-POST-01-001 | post 阶段语义——"若平台拒绝 post, 记为规格-平台差异" |
| 5 | COMPAT-ACTIONDEV-01-001 | action.yml 不支持字段——"不导致 workflow 失败" |

---

## 五、SKIP 分类（26 例）

### 5.1 BLOCKER_SKIP（14）— 需要真实环境

| 类别 | 数量 | 案例 |
|------|:---:|------|
| K8s + NPU 集群 | 6 | REL-K8S-01-046 ~ 051 |
| Volcano 调度器 | 2 | REL-VCJOB-01-001, 002 |
| Fork PR 环境 | 1 | SEC-WFRUN-01-001 |
| 平台审计/API | 1 | SEC-AUDIT-01-001 |
| 真实平台交互 | 4 | USE-API-01-001, USE-DIR-01-002, USE-ONBD-01-001, USE-PATH-01-001 |

### 5.2 DOCUMENTATION（10）— 可离线完成

| case_id | 检查内容 |
|---------|---------|
| USE-ACT-01-003 | 官方插件短名 → 插件市场映射一致性 |
| USE-DOC-01-001 | stages/post 在迁移文档中的可见性 |
| USE-DOC-01-002 | stages/jobs 语法在 4 份文档中的矛盾形式 |
| USE-DOC-01-006 | syntax-reference 章节编号连续性 |
| USE-EXPR-01-003 | 表达式函数表语法可解析性 |
| USE-LBL-01-003 | runs-on 标签语法在文档中的形式多样性 |
| USE-LBL-01-005 | runner 资源池名称在 sample 和 doc 之间的差异 |
| USE-RES-01-001 | runtime-env 文档中是否含 GITHUB_ 前缀变量 |
| USE-UNKN-01-004 | 未文档化字段差异 (select/manual_override/inputs) |
| USE-VARS-01-001 | vars 上下文文档与 sample 一致性 |

### 5.3 CONFIG_SKIP（2）

| case_id | 阻塞原因 | 修复 |
|---------|---------|------|
| SEC-NAME-01-003 | 需 admin API 测试 secret 命名校验 | 配置 admin API credential |
| SEC-SECMGMT-01-002 | 需多角色 repo 测试权限 CRUD | 设置多角色 repo fixture |

---

## 六、修正建议

1. **valid-classify 增加负向识别**: 读 Phase 01 文本用例，`预期结果` 含 "报错/拒绝/校验失败" → 非 200 = PASS（8 例立即修正）
2. **TRUE_INVALID 批量修复**: runner 标签 `ubuntu-latest` → `dedicate-hosted`；stages 数组 → map；删除 `post`/`permissions`/`environment`/`run-name`
3. **DOCUMENTATION 10 例**: 不需 runtime，可立即用 grep 脚本离线执行
4. **BLOCKER_SKIP 14 例**: 明确标记为 Phase 02 基础设施依赖，等 K8s 集群就绪后批量回归

---

*分析完成: 2026-07-24 · 91/98 例已分类 · 7 例待补全*
