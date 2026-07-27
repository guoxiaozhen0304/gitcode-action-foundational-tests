# Valid Classify Report

## 总览

| 分组 | 数量 |
|------|:---:|
| valid | 221 (+6 WAF whitelist) |
| invalid | 45 |
| WAF | 0 |
| SKIP | 7 |
| **total** | **273** |

## WAF 白名单 (6 cases → valid)

| Case ID | 拦截原因 |
|---------|------|
| COMP-ATOMGIT-01-049 | WAF 418 → whitelist |
| COMP-SCRIPT-01-082 | WAF 418 → whitelist |
| COMPAT-TOKEN-01-001 | WAF 418 → whitelist |
| COMPAT-TOKEN-01-002 | WAF 418 → whitelist |
| REL-LOG-01-040 | WAF 418 → whitelist |
| REL-OUTPUT-01-017 | WAF 418 → whitelist |

## Invalid 明细 (45 cases)

| Case ID | 诊断 |
|---------|------|
| COMP-EXPR-01-058 | jobs[verify].steps[2].if: if表达式无法解析 {0} |
| COMP-RUNNER-01-003 | jobs[verify].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{o |
| COMP-RUNNER-01-082 | jobs[probe].runs-on.small: unknown property; jobs[probe].runs-on.ubuntu-24: unknown property |
| COMP-STAGES-01-002 | Cannot deserialize value of type `java.util.LinkedHashMap<java.lang.St |
| COMP-STAGES-01-003 | post.steps: unknown property; post.run_always: unknown property |
| COMP-STAGES-01-005 | Cannot deserialize value of type `java.util.LinkedHashMap<java.lang.St |
| COMP-TRIG-01-075 | on.schedule[0].cron: 不是可识别的cron表达式 |
| COMP-UNKNOWN-01-001 | unknown_field: unknown property |
| COMP-UNKNOWN-01-004 | stages[gated_stage].name: 值不能为空 |
| COMP-UNKNOWN-01-005 | inputs[branch_name].type: 值不能为空 |
| COMPAT-ACTIONDEV-01-001 | jobs[test-action-meta].steps[1].uses: 格式错误：pluginname@version，其中 plugi; stages[default].jobs[test-action-meta]: 插件./.github/actions/my-action不 |
| COMPAT-CONCUR-01-001 | concurrency.exceed-action: 值不能为空; concurrency.max: 值不能小于1 |
| COMPAT-CONCUR-01-002 | Cannot deserialize value of type `java.lang.String` from Array value ( |
| COMPAT-CONCUR-01-003 | concurrency.exceed-action: 值不能为空; concurrency.max: 值不能小于1 |
| COMPAT-CONCUR-01-004 | concurrency.exceed-action: 值不能为空; concurrency.max: 值不能小于1 |
| COMPAT-ENVIRON-01-001 | jobs[test].environment: unknown property |
| COMPAT-ENVIRON-01-002 | jobs[test-environment].environment: unknown property |
| COMPAT-EVENT-01-001 | on.release: unknown property |
| COMPAT-PATHS-01-002 | on.push: 列表长度超出限制，paths paths-ignore之和不能小于1或超过32 |
| COMPAT-PR-01-002 | on.merge_requests.types: 列表中存在非法值:[opened] 允许值:[close, merge, open, re |
| COMPAT-PR-01-004 | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32 |
| COMPAT-PR-01-005 | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32 |
| COMPAT-PR-01-007 | on.merge_requests.types: 列表中存在非法值:[labeled] 允许值:[close, merge, open, r |
| COMPAT-PR-01-008 | on.merge_requests.types: 列表中存在非法值:[ready_for_review] 允许值:[close, merge |
| COMPAT-RUNNER-01-004 | jobs[test-custom-label].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts |
| COMPAT-RUNNER-01-005 | jobs[test-intranet].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hos |
| COMPAT-RUNSON-01-003 | jobs[probe].runs-on.group: unknown property; jobs[probe].runs-on.labels: unknown property |
| COMPAT-RUNSON-01-005 | jobs[probe].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os |
| COMPAT-RUNSON-01-006 | jobs[probe].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os |
| COMPAT-SCHEDULE-01-004 | on.schedule[0].cron: 不是可识别的cron表达式 |
| COMPAT-SECRET-01-005 | jobs[test-env-secret].environment: unknown property |
| COMPAT-SHELL-01-003 | jobs[test-windows-shell].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codeart |
| COMPAT-VARS-01-005 | jobs[test-vars-if].steps[1].if: if表达式无法解析 表达式：vars.ENABLE_FEATURE == ' |
| REL-POST-01-001 | post.steps: unknown property; post.run_always: unknown property |
| REL-PREEMPT-01-005 | concurrency.preemption.events: 列表中存在非法值:[push] 允许值:[mr_id] |
| REL-RACE-01-048 | jobs[job_b].if: if表达式无法解析 表达式：failure()第1位出现不支持的函数 |
| REL-SCHED-01-058 | on.schedule[0].cron: 不是可识别的cron表达式 |
| REL-STAGES-01-029 | Cannot deserialize value of type `java.util.LinkedHashMap<java.lang.St |
| REL-STEPS-01-042 | jobs[test].steps: 列表长度必须在0到16之间 |
| SEC-ENV-01-002 | jobs[env-secret-denied].environment: unknown property |
| SEC-SUPPLY-01-003 | jobs[typo-test].steps[0].uses: 格式错误：pluginname@version，其中 pluginname 为; stages[default].jobs[typo-test]: 插件checkout-action@v1不存在 |
| SEC-WCMD-01-003 | while scanning a simple key
 in 'string', line 11, column 1:
    INJEC |
| SEC-WCMD-01-004 | while scanning a simple key
 in 'string', line 12, column 1:
    hijac |
| USE-CONC-01-002 | concurrency.max: 值不能小于1 |
| USE-NEST-01-002 | jobs[caller].steps[0].uses: 格式错误：pluginname@version，其中 pluginname 为 1~; stages[default].jobs[caller]: 插件./.gitcode/workflows/reusable-level1.y |