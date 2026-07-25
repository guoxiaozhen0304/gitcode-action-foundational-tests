# 66 INVALID Cases — 逐例失败分析报告

> 批次: 2026-07-23-01 | 生成日期: 2026-07-25
> 分析方法: 遵循 `phase02/agents/failure-analyst/CLAUDE.md`
> 数据源: 369 cases → 289 通过 API 校验 → 66 被拒绝

## 统计

| 类别 | 数量 |
|------|------|
| 预期非法 (negative test) | 24 |
| 非预期非法 (需修复) | 42 |
| **总计** | **66** |

## 逐例分析

### 预期非法 — Negative Tests

| # | case_id | dimension | trigger | 标题 | 诊断 |
|---|---------|-----------|---------|------|------|
| 1 | [COMP-SCHEDULE-01-002](./COMP-SCHEDULE-01-002.md) | completeness | schedule | 非默认分支的 schedule workflow 不应触发 | on.schedule[0].cron: 不是可识别的cron表达式 |
| 2 | [COMP-SCHEDULE-01-003](./COMP-SCHEDULE-01-003.md) | completeness | schedule | cron 间隔短于 5 分钟时被拒绝或降级 | on.schedule[0].cron: 不是可识别的cron表达式 |
| 3 | [COMPAT-CONCUR-01-002](./COMPAT-CONCUR-01-002.md) | compatibility | workflow_dispatch | concurrency 配置越界或不支持时应给出清晰报错 | Cannot deserialize value of type `java.lang.String` from Arr |
| 4 | [COMPAT-ENVIRON-01-001](./COMPAT-ENVIRON-01-001.md) | compatibility | workflow_dispatch | 含 environment 字段的 job 应被报错或警告 | jobs[test].environment: unknown property |
| 5 | [COMPAT-FIELD-01-001](./COMPAT-FIELD-01-001.md) | compatibility | workflow_dispatch | 含 run-name 字段的 workflow 应被报错或警告 | run-name: unknown property |
| 6 | [COMPAT-FIELD-01-002](./COMPAT-FIELD-01-002.md) | compatibility | workflow_dispatch | 含 services 字段的 job 应被报错或警告 | jobs[test].services: unknown property |
| 7 | [COMPAT-FIELD-01-003](./COMPAT-FIELD-01-003.md) | compatibility | workflow_dispatch | 未知顶层字段不应被静默忽略而应给出警告 | custom_field: unknown property |
| 8 | [COMPAT-MIGRATE-01-001](./COMPAT-MIGRATE-01-001.md) | compatibility | workflow_dispatch | GitHub 风格 permissions 块迁移报错应给出可操作指引 | jobs[migrate-permissions].permissions: unknown property |
| 9 | [COMPAT-MIGRATE-01-002](./COMPAT-MIGRATE-01-002.md) | compatibility | workflow_dispatch | GitHub 风格 run-name 语法迁移报错应给出可操作指引 | run-name: unknown property |
| 10 | [COMPAT-PERM-01-003](./COMPAT-PERM-01-003.md) | compatibility | workflow_dispatch | permissions 命名差异——GitHub contents 权限项应报错 | permissions.contents: unknown property |
| 11 | [COMPAT-PR-01-002](./COMPAT-PR-01-002.md) | compatibility | pull_request | pull_request types 命名差异 - GitHub 风格 types 应报错 | on.merge_requests.types: 列表中存在非法值:[opened] 允许值:[close, merge |
| 12 | [COMPAT-RUNNER-01-004](./COMPAT-RUNNER-01-004.md) | compatibility | workflow_dispatch | 自定义特征标签不被支持时应给出可用标签列表 | jobs[test-custom-label].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为 |
| 13 | [REL-PREEMPT-01-006](./REL-PREEMPT-01-006.md) | reliability | workflow_dispatch | preemption events 越界值——配置 11 个应被拒绝 | concurrency.preemption.events: 列表中存在非法值:[push] 允许值:[mr_id] |
| 14 | [USE-CONC-01-002](./USE-CONC-01-002.md) | usability | workflow_dispatch | concurrency.max 配置 -1 时报错应提示有效范围 | concurrency.max: 值不能小于1 |
| 15 | [USE-EXPR-01-002](./USE-EXPR-01-002.md) | usability | workflow_dispatch | 调用未知函数时报错应提示函数名错误与修正方向 | jobs[bad].steps[0].if: if表达式无法解析 表达式：unknownFunc()第1位出现不支持的函 |
| 16 | [USE-LBL-01-001](./USE-LBL-01-001.md) | usability | workflow_dispatch | runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表 | jobs[bad].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hos |
| 17 | [USE-NEST-01-001](./USE-NEST-01-001.md) | usability | workflow_dispatch | workflow_call 嵌套 3 层时报错应明确提示上限为 2 层 | jobs[caller].steps[0].uses: 格式错误：pluginname@version，其中 plugi |
| 18 | [USE-PERM-01-002](./USE-PERM-01-002.md) | usability | workflow_dispatch | 使用 GitHub 权限域命名时报错应给出 GitCode 对照表 | permissions.contents: unknown property |
| 19 | [USE-RUN-01-002](./USE-RUN-01-002.md) | usability | workflow_dispatch | 使用单标签 ubuntu-latest 时报错应给出三段式格式指引 | jobs[bad-runner].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codea |
| 20 | [USE-STAT-01-002](./USE-STAT-01-002.md) | usability | workflow_dispatch | 使用 success() 带括号时报错应提示 GitCode 括号差异 | jobs[bad-stat].steps[0].if: if表达式无法解析 表达式：success()第1位出现不支持的 |
| 21 | [USE-TYPE-01-002](./USE-TYPE-01-002.md) | usability | pull_request | 使用 GitHub types 命名 opened/synchronize 时应给出可理解提示 | on.merge_requests.types: 列表中存在非法值:[opened] 允许值:[close, merge |
| 22 | [USE-UNKN-01-001](./USE-UNKN-01-001.md) | usability | workflow_dispatch | 未知字段如 run-name 不应被静默忽略而应给出警告或错误 | run-name: unknown property |
| 23 | [USE-YAML-01-001](./USE-YAML-01-001.md) | usability | workflow_dispatch | 缺少必填字段 on 时报错应指出具体字段名与位置 | on: 值不能为空 |
| 24 | [USE-YAML-01-002](./USE-YAML-01-002.md) | usability | workflow_dispatch | YAML 缩进错误时报错应指出具体行号与列号 | while parsing a block mapping
 in 'string', line 5, column 5 |

### 非预期非法 — 需修复

| # | case_id | root_cause | responsible | dimension | 诊断 |
|---|---------|-----------|-------------|-----------|------|
| 1 | [COMP-BOUND-01-085](./COMP-BOUND-01-085.md) | 产品bug (cron 表达式被拒 (合法语法)) | 平台方 | completeness | on.schedule[0].cron: 不是可识别的cron表达式 |
| 2 | [COMP-EXPR-01-058](./COMP-EXPR-01-058.md) | 产品bug (if 表达式解析器不支持合法运算符组合) | 平台方 | completeness | jobs[verify].steps[2].if: if表达式无法解析 {0} |
| 3 | [COMP-RUNNER-01-003](./COMP-RUNNER-01-003.md) | 产品bug (runs-on 数组校验过严) | 平台方 | completeness | jobs[verify].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts- |
| 4 | [COMP-SCHEDULE-01-001](./COMP-SCHEDULE-01-001.md) | 产品bug (cron 表达式被拒 (合法语法)) | 平台方 | completeness | on.schedule[0].cron: 不是可识别的cron表达式 |
| 5 | [COMP-STAGES-01-001](./COMP-STAGES-01-001.md) | 文档冲突 (stages 反序列化错误 (array vs map)) | 平台方 | completeness | Cannot deserialize value of type `java.util.LinkedHashMap<ja |
| 6 | [COMP-STAGES-01-002](./COMP-STAGES-01-002.md) | 文档冲突 (stages 反序列化错误 (array vs map)) | 平台方 | completeness | Cannot deserialize value of type `java.util.LinkedHashMap<ja |
| 7 | [COMP-STAGES-01-003](./COMP-STAGES-01-003.md) | 文档冲突 (post.steps/run_always 文档描述但平台拒) | 平台方 | completeness | post.steps: unknown property |
| 8 | [COMP-TRIG-01-075](./COMP-TRIG-01-075.md) | 产品bug (cron 表达式被拒 (合法语法)) | 平台方 | completeness | on.schedule[0].cron: 不是可识别的cron表达式 |
| 9 | [COMP-UNKNOWN-01-001](./COMP-UNKNOWN-01-001.md) | 平台缺陷 (未知字段静默拒绝) | 平台方 | completeness | unknown_field: unknown property |
| 10 | [COMP-WFLOW-01-065](./COMP-WFLOW-01-065.md) | 文档冲突 (post.steps/run_always 文档描述但平台拒) | 平台方 | completeness | post.steps: unknown property |
| 11 | [COMPAT-ACTIONDEV-01-001](./COMPAT-ACTIONDEV-01-001.md) | 用例问题 (uses 路径引用不存在的文件) | Phase 01 | compatibility | jobs[test-action-meta].steps[1].uses: 格式错误：pluginname@versio |
| 12 | [COMPAT-CONCUR-01-001](./COMPAT-CONCUR-01-001.md) | 产品bug (concurrency 字段语义与文档不符) | 平台方 | compatibility | concurrency.exceed-action: 值不能为空 |
| 13 | [COMPAT-CONCUR-01-003](./COMPAT-CONCUR-01-003.md) | 产品bug (concurrency preemption 配置校验过严) | 平台方 | compatibility | concurrency.exceed-action: 值不能为空 |
| 14 | [COMPAT-CONCUR-01-004](./COMPAT-CONCUR-01-004.md) | 文档缺失 (preemption events 取值限制) | 平台方 | compatibility | concurrency.exceed-action: 值不能为空 |
| 15 | [COMPAT-ENVIRON-01-002](./COMPAT-ENVIRON-01-002.md) | 平台缺陷 (environment 字段不支持) | 平台方 | compatibility | jobs[test-environment].environment: unknown property |
| 16 | [COMPAT-EXPR-01-013](./COMPAT-EXPR-01-013.md) | 用例问题 (GitHub 表达式函数 vs GitCode 关键字——success 关键字未使用) | Phase 01 | compatibility | jobs[test-success-paren].steps[0].if: if表达式无法解析 表达式：success( |
| 17 | [COMPAT-EXPR-01-014](./COMPAT-EXPR-01-014.md) | 用例问题 (GitHub 表达式函数 vs GitCode 关键字——always 关键字未使用) | Phase 01 | compatibility | jobs[test-always-paren].steps[1].if: if表达式无法解析 表达式：always第1位 |
| 18 | [COMPAT-PATHS-01-001](./COMPAT-PATHS-01-001.md) | 平台缺陷 (列表长度限制未在文档声明) | 平台方 | compatibility | on.push: 列表长度超出限制，paths paths-ignore之和不能小于1或超过32 |
| 19 | [COMPAT-PATHS-01-002](./COMPAT-PATHS-01-002.md) | 平台缺陷 (列表长度限制未在文档声明) | 平台方 | compatibility | on.push: 列表长度超出限制，paths paths-ignore之和不能小于1或超过32 |
| 20 | [COMPAT-PR-01-003](./COMPAT-PR-01-003.md) | 平台缺陷 (列表长度限制未在文档声明) | 平台方 | compatibility | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或 |
| 21 | [COMPAT-PR-01-004](./COMPAT-PR-01-004.md) | 平台缺陷 (列表长度限制未在文档声明) | 平台方 | compatibility | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或 |
| 22 | [COMPAT-PR-01-005](./COMPAT-PR-01-005.md) | 平台缺陷 (列表长度限制未在文档声明) | 平台方 | compatibility | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或 |
| 23 | [COMPAT-RUNNER-01-005](./COMPAT-RUNNER-01-005.md) | 产品bug (runs-on 数组校验过严) | 平台方 | compatibility | jobs[test-intranet].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['co |
| 24 | [COMPAT-SCHEDULE-01-001](./COMPAT-SCHEDULE-01-001.md) | 产品bug (schedule 反序列化错误——array 期望 vs object) | 平台方 | compatibility | Cannot deserialize value of type `java.util.ArrayList<com.hu |
| 25 | [COMPAT-SCHEDULE-01-002](./COMPAT-SCHEDULE-01-002.md) | 产品bug (schedule 反序列化错误——array 期望 vs object) | 平台方 | compatibility | Cannot deserialize value of type `java.util.ArrayList<com.hu |
| 26 | [COMPAT-SCHEDULE-01-003](./COMPAT-SCHEDULE-01-003.md) | 产品bug (cron 表达式被拒 (合法语法)) | 平台方 | compatibility | on.schedule[0].cron: 不是可识别的cron表达式 |
| 27 | [COMPAT-SECRET-01-005](./COMPAT-SECRET-01-005.md) | 平台缺陷 (environment 字段不支持) | 平台方 | compatibility | jobs[test-env-secret].environment: unknown property |
| 28 | [COMPAT-SHELL-01-003](./COMPAT-SHELL-01-003.md) | 产品bug (runs-on 数组校验过严) | 平台方 | compatibility | jobs[test-windows-shell].runs-on: runs-on以数组形式定义时，若为默认资源池则定义 |
| 29 | [COMPAT-VARS-01-005](./COMPAT-VARS-01-005.md) | 用例问题 (GitHub 表达式函数 vs GitCode 关键字——vars 上下文不支持 if 条件) | Phase 01 | compatibility | jobs[test-vars-if].steps[1].if: if表达式无法解析 表达式：vars.ENABLE_FE |
| 30 | [REL-PREEMPT-01-005](./REL-PREEMPT-01-005.md) | 文档缺失 (preemption events 取值限制) | 平台方 | reliability | concurrency.preemption.events: 列表中存在非法值:[push] 允许值:[mr_id] |
| 31 | [REL-RACE-01-048](./REL-RACE-01-048.md) | 用例问题 (GitHub 表达式函数 vs GitCode 关键字——failure() 函数不支持) | Phase 01 | reliability | jobs[job_b].if: if表达式无法解析 表达式：failure()第1位出现不支持的函数 |
| 32 | [REL-STAGES-01-029](./REL-STAGES-01-029.md) | 文档冲突 (stages 反序列化错误 (array vs map)) | 平台方 | reliability | Cannot deserialize value of type `java.util.LinkedHashMap<ja |
| 33 | [REL-STEPS-01-042](./REL-STEPS-01-042.md) | 文档缺失 (steps <=16 限制未在文档声明) | 平台方 | reliability | jobs[test].steps: 列表长度必须在0到16之间 |
| 34 | [SEC-DEFPERM-01-002](./SEC-DEFPERM-01-002.md) | 平台缺陷 (job 级 permissions 不支持) | 平台方 | security | jobs[override-test].permissions: unknown property |
| 35 | [SEC-ENV-01-001](./SEC-ENV-01-001.md) | 平台缺陷 (environment 字段不支持) | 平台方 | security | jobs[env-secret-approved].environment: unknown property |
| 36 | [SEC-ENV-01-002](./SEC-ENV-01-002.md) | 平台缺陷 (environment 字段不支持) | 平台方 | security | jobs[env-secret-denied].environment: unknown property |
| 37 | [SEC-PERM-01-001](./SEC-PERM-01-001.md) | 平台缺陷 (job 级 permissions 不支持) | 平台方 | security | jobs[perm-read].permissions: unknown property |
| 38 | [SEC-PERM-01-002](./SEC-PERM-01-002.md) | 平台缺陷 (job 级 permissions 不支持) | 平台方 | security | jobs[perm-write-denied].permissions: unknown property |
| 39 | [SEC-SUPPLY-01-003](./SEC-SUPPLY-01-003.md) | 用例问题 (uses 引用不存在的插件) | Phase 01 | security | jobs[typo-test].steps[0].uses: 格式错误：pluginname@version，其中 pl |
| 40 | [SEC-WCMD-01-003](./SEC-WCMD-01-003.md) | 用例问题 (YAML 语法错误——引号未正确闭合) | Phase 01 | security | while scanning a simple key
 in 'string', line 11, column 1: |
| 41 | [SEC-WCMD-01-004](./SEC-WCMD-01-004.md) | 用例问题 (YAML 语法错误——引号未正确闭合) | Phase 01 | security | while scanning a simple key
 in 'string', line 12, column 1: |
| 42 | [USE-NEST-01-002](./USE-NEST-01-002.md) | 用例问题 (uses 路径引用不存在的 workflow 文件) | Phase 01 | usability | jobs[caller].steps[0].uses: 格式错误：pluginname@version，其中 plugi |
