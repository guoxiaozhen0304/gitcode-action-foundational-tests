# 基线用例举一反三筛查清单 · 2026-07-25

> 来源：对 `phase02/classify-experiment/2026-07-23/VALID/` 全量基线用例，按 run 2026-07-25-01 失败归因中发现的 14 类历史问题模式自动筛查 + 人工复核。
> 已修复的 18 条（REL-ARTCONC-01-063、REL-ARTPERF-01-053、REL-MATRIX-01-026/038/039、COMPAT-MATRIX-01-003/004、USE-LOG-01-001、COMP-PERMS-01-001、COMP-SECRET-01-001、COMP-SUMMARY-01-001、SEC-ARTF-01-002、COMP-TIMEOUT-01-002、SEC-PRTGT-01-001、REL-ART-01-041、REL-ARTPERF-01-053-V2、REL-RUNNER-01-049-V2、REL-BIGRUNNER-01-066）不在本清单内。

## A 类 · 确凿用例 bug（必然/已实证假 FAIL，建议立即修）

### A1. `${{{{ }}}}` 四层花括号残留（1）
- REL-OUTPUT-01-016

### A2. 非法表达式 + name/runs-on 错配（1）
- REL-RUNNER-01-049 （`${{RUNNER_TEMP}}` 非法表达式；probe-medium/probe-large 名字带规格但 runs-on 全是 small）

### A3. 幽灵标记（断言词 workflow 从未 echo，必然 FAIL，21）
已被 run 2026-07-25-01 实证：
- SEC-MASK-01-001
- SEC-MASK-01-005
- SEC-BASE-01-001
- SEC-TOKEN-01-001
- SEC-WCMD-01-001
- SEC-TOCTOU-01-001
- SEC-DOS-01-001
- SEC-DEFPERM-01-001
- SEC-PERM-01-004
- SEC-TOKEN-01-002
- SEC-CACHE-01-002
- SEC-NAME-01-002
- SEC-SUPPLY-01-002
- SEC-INJ-01-005

同模式未实证：
- SEC-COMM-01-001
- SEC-RUN-01-001
- SEC-RUN-01-002
- SEC-RUN-01-003
- SEC-TOCTOU-01-002
- SEC-NET-01-001
- COMPAT-SHELL-01-002 （疑似）

### A4. git 操作环境问题（3）
- COMP-PERMS-01-002 （有 git config 但无 checkout，工作区非 git 仓库）
- SEC-PERM-01-004 （clone 后缺 `git config user.email/user.name`，已实证 exit 128）
- SEC-TOKEN-01-002 （同 SEC-PERM-01-004）

## B 类 · 平台文案/环境依赖（脆弱但有意，建议改归一化标记，8）
- REL-DISK-01-019 （依赖 "No space left on device"）
- REL-FAULT-01-033 （同上）
- REL-FAULT-01-034 （依赖 "cache miss"）
- REL-MEM-01-021 （依赖 "Killed"）
- REL-TIMEOUT-01-010 （依赖 "timeout"）
- COMPAT-EXPR-01-004 （依赖自然语言输出）
- REL-API-01-065 (contains=429，HTTP 码裸子串，trace_id 可能误命中）
- REL-FAULT-01-035 (contains=503，同上）

## C 类 · artifact 固定名冲突风险（建议加 `${{ atomgit.run_id }}` 后缀，10）
- COMP-ARTIFACT-01-001
- COMP-ARTIFACT-01-002
- COMP-ARTIFACT-01-003
- COMPAT-ARTIFACT-01-001
- COMPAT-ARTIFACT-01-002
- REL-FAULT-01-032 （已实证 "name already exists" FAIL）
- REL-RETAIN-01-047
- SEC-ARTF-01-001
- SEC-DOS-01-001 （已实证）
- SEC-SIDE-01-002 （已实证）

## D 类 · secret 探针缺失（config_probe 空转）

### D1. 脱敏类（workflow_dispatch，应加 `configured_len` 探针，14）
- COMP-SECRET-01-002
- COMPAT-MASK-01-001
- COMPAT-MASK-01-002
- SEC-MASK-01-001
- SEC-MASK-01-002
- SEC-MASK-01-003
- SEC-MASK-01-004
- SEC-MASK-01-005
- SEC-MASK-01-006
- SEC-SIDE-01-001
- SEC-SIDE-01-002
- SEC-WCMD-01-001
- SEC-NAME-01-001
- USE-MASK-01-001

### D2. fork 隔离类（secret 为空是预期，不能加探针，仅需确认断言按空值设计，5）
- COMP-PR-01-001
- COMP-PR-01-002
- COMPAT-TARGET-01-002
- SEC-FORK-01-001
- SEC-FORK-01-002

## E 类 · 结构性问题（需设计决策，不宜直接改 YAML，6）

### E1. 断言互斥（单 run 正负同时压 run_status，3）
- COMPAT-PR-01-006 （已实证，需拆双 trigger：main 分支验证触发 + 非 main 验证不触发）
- REL-IGNORE-01-004
- SEC-PRTGT-01-002

### E2. self-hosted 依赖（环境无对应 runner，建议标记基础设施阻塞/移出自动执行集，3）
- COMPAT-RUNNER-01-003
- REL-K8S-01-045
- SEC-RUN-01-003

## 汇总

| 类别 | 数量 | 处置建议 |
|------|------|----------|
| A 确凿 bug | 26 | 立即修（模式均有已验证模板） |
| B 脆弱依赖 | 8 | 改 shell 归一化标记 |
| C 冲突风险 | 10 | artifact name 加 run_id 后缀 |
| D 探针缺失 | 19 | D1 加探针 / D2 确认断言设计 |
| E 结构性 | 6 | 设计决策（拆 trigger / 移出执行集） |
| **合计** | **69** | |

备注：
- 已排除误报：COMPAT-SHELL-01-001（"bash" 命中平台日志头 default-bash）。
- 零命中模式：download 路径假设、matrix 组合数不匹配、占位符未替换、summary 错 target（此前修复中已根除）。
