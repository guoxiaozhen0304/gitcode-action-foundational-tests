# GitCode Actions 测试报告

**执行批次**: 2026-07-28-01
**Phase 01 用例来源**: valid-classify agent 产出（phase02/agents/valid-classify/output/VALID）
**执行时间**: 2026-07-28 12:11 ~ 14:05（约 1h54min）
**执行引擎**: GitCode Actions API v8 · Phase 02 Harness

---

## 一、执行摘要

| 指标 | 数值 |
|---|---|
| 总用例数 | 221 |
| ✅ 通过（PASS） | 140（63.3%） |
| ❌ 失败（FAIL） | 37（16.7%） |
| ⏱️ 超时（TIMEOUT） | 22（10.0%） |
| 🔧 环境错误（ENV_ERROR） | 12（5.4%） |
| ⏸️ 未决（INCONCLUSIVE） | 8（3.6%） |
| 🚫 编译错误（COMPILE_ERROR） | 2（0.9%） |
| **可执行通过率**（除 TIMEOUT/ENV/INCONCL/COMPILE） | **140/177 = 79.1%** |

---

## 二、分维度通过率

| 维度 | 总数 | PASS | FAIL | 通过率 | P0 FAIL |
|---|---|---|---|---|---|
| completeness | 59 | 30 | 19 | 50.8% | 1 |
| compatibility | 80 | 63 | 6 | 78.8% | 0 |
| reliability | 28 | 13 | 4 | 46.4% | 0 |
| security | 20 | 8 | 6 | 40.0% | 4 |
| usability | 34 | 26 | 2 | 76.5% | 0 |
| **合计** | **221** | **140** | **37** | **63.3%** | **5** |

---

## 三、门禁判定

**结论**: ⛔ **BLOCKED**

**Blocked 维度**: completeness（50.8%，低于阈值）、reliability（46.4%）、security（40.0%）

**P0 失败数**: 5 条（P0 失败即整体 BLOCKED）

---

## 四、P0 失败（Blocker）

| 用例 ID | 维度 | 标题 | 失败原因 |
|---|---|---|---|
| COMP-ISOLATION-01-001 | completeness | 同一 workflow 先后 job 文件系统互相干扰 | build job FAILED → 下游 Verify IGNORED，日志无 shell 输出 |
| SEC-DOS-01-001 | security | 无 artifact / 无 cache 的极限边界拒绝 | 全零文件 ZIP 压缩仅 ~1MB，未触达配额边界 |
| SEC-RUN-01-003 | security | 非公有 Runner 项目不应该被读取 | 自托管 runner 不可用 |
| SEC-SUPPLY-01-001 | security | 第三方 Action 应支持 commit hash 固定 | 文档标注为推荐方式，平台静默拒绝 |
| SEC-SUPPLY-01-002 | security | commit hash 不匹配时应拒绝执行 Action | 正确拒绝但日志零诊断（静默失败） |

---

## 五、FAIL 归因格局

37 条 FAIL 经 failure-analyst 逐条归因，分类分布：

| 根因分类 | 数量 | 主责方 | 说明 |
|---|---|---|---|
| **产品缺陷** | 16 | 平台方 | atomgit 值格式/空值、表达式引擎、workflow 语义、磁盘容量、输入输出边界 |
| **环境问题** | 10 | Phase 02 | runner/fixture 未就绪、外部资源依赖、日志采集缺口 |
| **标记不匹配**（假 FAIL） | 4 | Phase 01 | 断言关键词映射/大小写匹配缺陷，平台行为实际正确 |
| **用例设计问题** | 4 | Phase 01 | 夹具边界未覆盖、PR merge ref 不存在 |
| **编译缺口** | 2 | Phase 01 | 编译器不支持 target 类型导致断言退化 |
| **需人工判断** | 1 | 多方 | 单行日志无法区分原因 |

### 关键系统性缺陷

1. **atomgit.ref/atomgit.sha** —— `ref` 返回短格式 `main` 而非 `refs/heads/main`，`sha` 在 workflow_dispatch 下为空（影响 4 条）
2. **表达式引擎** —— `hashFiles()` / `format()` 未求值，直接送入 bash（影响 2 条）
3. **静默失败** —— 多数产品缺陷无日志无诊断，用户定位问题困难

---

## 六、FAIL 详情

### COMP-ISOLATION-01-001 — 同一 workflow 先后 job 文件系统互相干扰
| 项目 | 值 |
|---|---|
| 判定 | FAIL |
| 维度 | completeness · P0 |
| 断言 | run_status FAILED + leak（通过）|
| 根因 | 环境问题 — build job 在执行前 FAILED，下游 Verify IGNORED，日志无 shell 输出 |
| 证据 | `failure/2026-07-28-01/report/failure-analyst-completeness-COMP-ISOLATION-01-001.md` |

### COMP-ATOMGIT-01-047 — atomgit 核心上下文属性可访问性
| 项目 | 值 |
|---|---|
| 判定 | FAIL |
| 维度 | completeness · P1 |
| 断言 | atomgit.ref 期望 `refs/` 前缀，实际返回 `main`；atomgit.sha 期望 40 字符，实际为空 |
| 根因 | 产品缺陷 — 平台上下文返回值格式不符合文档承诺 |
| 证据 | `failure/2026-07-28-01/report/failure-analyst-completeness-COMP-ATOMGIT-01-047.md` |

### COMP-ATOMGIT-01-049 — 同上（另一 dispatch 上下文）
详见 COMP-ATOMGIT-01-047 分析。

### COMP-CTX-01-051 — atomgit.ref 格式偏差连锁失败
atomgit.ref 短格式导致 checkout 步骤失败。

### COMP-SYSENV-01-059 — ATOMGIT_SHA 在 dispatch 下为空
dispatch 上下文无法获取 commit SHA。

### COMP-EXPR-01-054 — 表达式字符串操作
startsWith 断言退化 + CASE_MATCH 失效，与 atomgit.ref 格式偏差连锁。

### COMP-EXPR-01-055 — hashFiles 表达式
`${{ hashFiles }}` 未被求值，原始文本送入 bash → `bad substitution`。

### COMP-EXPR-01-056 — format 表达式
`${{ format }}` 同上，表达式引擎未工作。

### COMP-WFLOW-01-064 — workflow_dispatch inputs 传递
inputs 传递机制不符合文档描述。

### COMP-BOUND-01-087 — 多 job 隔离性
多 job 日志采集不完整，第二个 job 缺失。

### COMP-BOUND-01-088 — stages fail_fast 失效
build stage FAILED 后 test stage 仍被调度（fail_fast 应为 true）。

### COMP-STEP-01-071 — step 执行状态检测
断言关键词映射问题（`success` vs `COMPLETED`），平台实际正常（假 FAIL）。

### COMP-SCRIPT-01-082 — 脚本执行环境
零 shell 输出，fixture 未就绪。

### COMP-ENVCTX-01-050 — env context 边界
多 job 日志采集缺口。

### COMP-ACT-01-001 — action 引用与调用
零 shell 输出，runner/fixture 环境问题。

### COMP-ACT-01-002 — 同上
同上。

### COMP-UNKNOWN-01-002 — 未分类用例
断言与平台实际行为不符（用例设计问题）。

### COMP-PR-01-004 — PR merge ref 不存在
`refs/merge-requests/1/merge` 远程不可解析。

### COMP-PR-01-005 — 同上
同上。

### COMPAT-ARTIFACT-01-001 — artifact 名称冲突
跨运行 artifact 名称残留，"already exists" 环境问题。

### COMPAT-ACTIONDEV-01-002 — action 开发环境
fixture 未验证，零 shell 输出。

### COMPAT-DEPR-01-001 — 废弃语法兼容
`::set-env::` 被平台静默忽略，无警告（产品缺陷）。

### COMPAT-EXPR-01-016 — `${{ }}` 表达式兼容
表达式未求值，原始字符直接送入 bash（产品缺陷）。

### COMPAT-PR-01-009 — PR 上下文 atomgit.ref
atomgit.ref 指向不存在的 `refs/merge-requests/41/merge`（产品缺陷）。

### COMPAT-RUNSON-01-004 — runs-on 自托管
自托管 runner 不可用，零输出（环境问题）。

### REL-RUNNER-01-050 — arm64 runner 支持
文档声明可用，实际无法调度 arm64 job（产品缺陷）。

### REL-DISK-01-018 — small runner 磁盘容量
文档声明 50 GB，dd 写入到 37.9 GB 即报 `No space left on device`（产品缺陷）。

### REL-OUTPUT-01-016 — ATOMGIT_OUTPUT 1MB 边界
文档承诺单参数最大 1MB，1MB 边界 job 静默 FAILED，307s 无诊断（产品缺陷）。

### REL-ART-01-042 — 2GB artifact 上限
平台正确拒绝 2GB 并给出上限值，但编译器退化了条件断言 → 假 FAIL（编译缺口）。

### SEC-DOS-01-001 — artifact/cache 极限拒绝
用例设计：全零文件 ZIP 压缩仅 ~1MB，未触达配额边界（用例问题）。

### SEC-RUN-01-003 — 自托管 runner 项目隔离
自托管 runner 不可用（环境问题）。

### SEC-SUPPLY-01-001 — SHA 固定引用
文档标注 SHA 引用为生产推荐方式，平台静默拒绝（产品缺陷）。

### SEC-SUPPLY-01-002 — 无效 SHA 拒绝
正确拒绝但日志零诊断（产品缺陷）。

### SEC-SECMGMT-01-001 — secret 脱敏验证
`masked_with_asterisks` 未映射到 `***` 检测，实际脱敏正常（假 FAIL）。

### SEC-TOKEN-01-003 — token 操作化验证
`IN_RUN_TOKEN_OPERATIONAL` 大小写不匹配，实际 token 可用（假 FAIL）。

### USE-LBL-01-006 — label 有效性
日志仅 1 行，无法区分原因（需人工判断）。

### USE-RUN-01-003 — run 状态 UI
编译器不支持 `target: ui` → 断言退化 → 对故意失败的设计用例产生假 FAIL（编译缺口）。

---

## 七、Abnormal 概览

44 条未产生有效判定：

| 类型 | 数量 | 根因归属 |
|---|---|---|
| TIMEOUT | 22 | comment 事件不响应(10) + paths 无变更(3) + 长时 dispatch(4) + 调度慢(5) |
| ENV_ERROR | 12 | workflow_call 嵌套不支持(9) + dispatch inputs 校验(2) + push 冲突(1) |
| INCONCLUSIVE | 8 | guard env 变量名错配(7) + 日志不可得(1) |
| COMPILE_ERROR | 2 | YAML 不合规 |

详细分析见 `failure/2026-07-28-01/abnormal/abnormal-detail.md`

---

## 八、流水线缺口清单

1. **PR 分支不回切污染**：pool_scheduler PR 路径执行后不切回 main，后续同仓用例在 PR 分支提交 → `git push origin main` 推 stale main → ENV_ERROR 级联（已修复于 63c6a34，本次未用）
2. **git clone remote 健康性无校验**：Workspace 只检查 `.git` 存在，不验证 remote URL 是否匹配目标仓库
3. **contributor token env 变量名错配**：`.env` 的 `CONTRIBUTOR_GITCODE_TOKEN` 与代码要求的 `GITCODE_CONTRIBUTOR_TOKEN` 不一致，untrusted_contributor 用例全部被拒

---

## 九、执行环境

| 项目 | 值 |
|---|---|
| 仓库池 | gitcode-test-0 ~ gitcode-test-4（5 仓） |
| 目标分支 | main |
| 并发数 | 5 仓 × 2 容量 = 10 |
| 单用例超时 | 300s（白名单 22 条最高 22000s） |
| 代码分支 | yyl-support |
| Cookie 用户 | yyl-support |
| Teardown | batch_end |

---

*报告由 Customer Agent 汇总 failure-analyst 归因产出生成 · 2026-07-28*
*归因参考：phase02/agents/failure-analyst/CLAUDE.md*
*基线参照：phase02/rules.md §11 判定模型*
