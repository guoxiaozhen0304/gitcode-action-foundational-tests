# Valid Classify Report

## 总览

| 分组 | 数量 |
|------|:---:|
| valid (direct) | 214 |
| valid (WAF whitelist) | 7 |
| invalid | 63 |
| WAF | 0 |
| SKIP | 23 |
| **total** | **307** |

## WAF 白名单 (11 total, 7 hit this batch)

| Case ID | 拦截原因 | This Batch |
|---------|------|:---:|
| COMP-ATOMGIT-01-047 | workflow body 含 `${}` 触发 WAF，人工验证通过 | yes |
| COMP-ATOMGIT-01-048 | 同上 | yes |
| COMP-ATOMGIT-01-049 | 同上 | yes |
| COMP-SCRIPT-01-082 | 同上 | yes |
| COMPAT-TOKEN-01-001 | token 值在 YAML 中触发注入检测 | yes |
| COMPAT-TOKEN-01-002 | 同上 | yes |
| REL-LOG-01-040 | 日志相关表达式触发 WAF（不在本批次 scriptable 中） | — |
| REL-OUTPUT-01-017 | ATOMGIT_OUTPUT 相关模式触发 WAF | yes |
| SEC-ENV-WAIT-02-001 | 环境等待相关（不在本批次 scriptable 中） | — |
| SEC-NAME-01-002 | secret 名触发 WAF（不在本批次 scriptable 中） | — |
| USE-MASK-01-001 | secret masking 相关（不在本批次 scriptable 中） | — |

## Invalid 明细 (63)

| Case ID | 诊断 |
|---------|------|
| COMP-CTX-01-052 | jobs[downstream].if: if表达式无法解析 表达式：needs.verify.result == 'success'第1位出现不支持的关键字 |
| COMP-EXPR-01-058 | jobs[verify].steps[4].if: if表达式无法解析 {0}; jobs[verify].steps[5].if: if表达式无法解析 {0} |
| COMP-RUNNER-01-003 | jobs[verify].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]， |
| COMP-RUNNER-01-082 | jobs[probe].runs-on.small: unknown property; jobs[probe].runs-on.ubuntu-24: unknown property |
| COMP-STAGES-01-002 | Cannot deserialize value of type `java.util.LinkedHashMap<java.lang.String,com.huawei.devc |
| COMP-STAGES-01-003 | post.steps: unknown property; post.run_always: unknown property |
| COMP-STAGES-01-005 | Cannot deserialize value of type `java.util.LinkedHashMap<java.lang.String,com.huawei.devc |
| COMP-TRIG-01-079 | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32 |
| COMP-UNKNOWN-01-001 | unknown_field: unknown property |
| COMP-UNKNOWN-01-004 | stages[gated_stage].name: 值不能为空 |
| COMP-UNKNOWN-01-005 | inputs[branch_name].type: 值不能为空 |
| COMP-WFLOW-01-065 | post.steps: unknown property; post.run_always: unknown property |
| COMPAT-ACTIONDEV-01-001 | jobs[test-action-meta].steps[1].uses: 格式错误：pluginname@version，其中 pluginname 为 1~50 位字母、数字、; stages[default].jobs[test-action-meta]: 插件./.github/actions/my-action不存在 |
| COMPAT-CONCUR-01-001 | concurrency.exceed-action: 值不能为空; concurrency.max: 值不能小于1 |
| COMPAT-CONCUR-01-002 | Cannot deserialize value of type `java.lang.String` from Array value (token `JsonToken.STA |
| COMPAT-CONCUR-01-003 | concurrency.exceed-action: 值不能为空; concurrency.max: 值不能小于1 |
| COMPAT-CONCUR-01-004 | concurrency.exceed-action: 值不能为空; concurrency.max: 值不能小于1 |
| COMPAT-ENVIRON-01-001 | jobs[test].environment: unknown property |
| COMPAT-ENVIRON-01-002 | jobs[test-environment].environment: unknown property |
| COMPAT-EVENT-01-001 | on.release: unknown property |
| COMPAT-EXPR-01-013 | jobs[test-success-paren].steps[0].if: if表达式无法解析 表达式：success()第1位出现不支持的函数; jobs[test-success-paren].steps[1].if: if表达式无法解析 表达式：success第1位出现不支持的关键字 |
| COMPAT-EXPR-01-014 | jobs[test-always-paren].steps[1].if: if表达式无法解析 表达式：always第1位出现不支持的关键字 |
| COMPAT-FIELD-01-001 | run-name: unknown property |
| COMPAT-FIELD-01-002 | jobs[test].services: unknown property |
| COMPAT-FIELD-01-003 | custom_field: unknown property |
| COMPAT-MIGRATE-01-001 | jobs[migrate-permissions].permissions: unknown property |
| COMPAT-MIGRATE-01-002 | run-name: unknown property |
| COMPAT-PATHS-01-001 | on.push: 列表长度超出限制，paths paths-ignore之和不能小于1或超过32 |
| COMPAT-PATHS-01-002 | on.push: 列表长度超出限制，paths paths-ignore之和不能小于1或超过32 |
| COMPAT-PERM-01-003 | permissions.contents: unknown property |
| COMPAT-PERM-01-006 | jobs[probe].permissions: unknown property; permissions.contents: unknown property |
| COMPAT-PR-01-002 | on.merge_requests.types: 列表中存在非法值:[opened] 允许值:[close, merge, open, reopen, update] |
| COMPAT-PR-01-003 | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32 |
| COMPAT-PR-01-004 | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32 |
| COMPAT-PR-01-005 | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32 |
| COMPAT-PR-01-007 | on.merge_requests.types: 列表中存在非法值:[labeled] 允许值:[close, merge, open, reopen, update] |
| COMPAT-PR-01-008 | on.merge_requests.types: 列表中存在非法值:[ready_for_review] 允许值:[close, merge, open, reopen, upda |
| COMPAT-RUNNER-01-004 | jobs[test-custom-label].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch} |
| COMPAT-RUNNER-01-005 | jobs[test-intranet].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{fl |
| COMPAT-RUNSON-01-003 | jobs[probe].runs-on.group: unknown property; jobs[probe].runs-on.labels: unknown property |
| COMPAT-RUNSON-01-005 | jobs[probe].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]，如 |
| COMPAT-RUNSON-01-006 | jobs[probe].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]，如 |
| COMPAT-SECRET-01-005 | jobs[test-env-secret].environment: unknown property |
| COMPAT-SHELL-01-003 | jobs[test-windows-shell].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch |
| COMPAT-VARS-01-005 | jobs[test-vars-if].steps[1].if: if表达式无法解析 表达式：vars.ENABLE_FEATURE == 'true'第1位出现不支持的关键字 |
| REL-POST-01-001 | post.steps: unknown property; post.run_always: unknown property |
| REL-PREEMPT-01-005 | concurrency.preemption.events: 列表中存在非法值:[push] 允许值:[mr_id] |
| REL-PREEMPT-01-006 | concurrency.preemption.events: 列表中存在非法值:[push] 允许值:[mr_id]; concurrency.preemption.events: 列表长度必须在0到10之间 |
| REL-RACE-01-048 | jobs[job_b].if: if表达式无法解析 表达式：failure()第1位出现不支持的函数 |
| REL-STAGES-01-029 | stages[next_stage].name: 值不能为空; stages[test_stage].name: 值不能为空 |
| REL-STEPS-01-042 | jobs[test].steps: 列表长度必须在0到16之间 |
| SEC-DEFPERM-01-001 | jobs[override-write].permissions: unknown property |
| SEC-DEFPERM-01-002 | jobs[override-test].permissions: unknown property |
| SEC-ENV-01-001 | jobs[env-secret-approved].environment: unknown property |
| SEC-ENV-01-002 | jobs[env-secret-denied].environment: unknown property |
| SEC-PERM-01-001 | jobs[perm-read].permissions: unknown property |
| SEC-PERM-01-002 | jobs[perm-write-denied].permissions: unknown property |
| SEC-SUPPLY-01-003 | jobs[typo-test].steps[0].uses: 格式错误：pluginname@version，其中 pluginname 为 1~50 位字母、数字、"-"、"_"; stages[default].jobs[typo-test]: 插件checkout-action@v1不存在 |
| SEC-WCMD-01-003 | while scanning a simple key
 in 'string', line 11, column 1:
    INJECTED_VAR=bad" >> $ATO |
| SEC-WCMD-01-004 | while scanning a simple key
 in 'string', line 12, column 1:
    hijacked=bad" >> $ATOMGIT |
| USE-CONC-01-002 | concurrency.max: 值不能小于1 |
| USE-DOC-01-007 | jobs[deploy].environment: unknown property |
| USE-UNKN-01-001 | run-name: unknown property |