# Valid Classify Report

## 总览

| 分组 | 数量 |
|------|:---:|
| valid (direct) | 255 |
| valid (WAF whitelist) | 10 |
| invalid | 72 |
| WAF | 0 |
| SKIP | 26 |
| **total** | **363** |

## WAF 白名单 (13 total, 10 hit this batch)

| Case ID | 拦截原因 | This Batch |
|---------|------|:---:|
| COMP-ATOMGIT-01-047 | workflow body 含 `${}` 触发 WAF，人工验证通过 | yes |
| COMP-ATOMGIT-01-048 | 同上 | yes |
| COMP-ATOMGIT-01-049 | 同上 | yes |
| COMP-SCRIPT-01-082 | 同上 | yes |
| COMPAT-TOKEN-01-001 | token 值在 YAML 中触发注入检测 | yes |
| COMPAT-TOKEN-01-002 | 同上 | yes |
| REL-OUTPUT-01-017 | ATOMGIT_OUTPUT 相关模式触发 WAF | yes |
| SEC-ARTF-01-002 | artifact 下载相关触发 WAF，人工验证通过 | yes |
| SEC-TOKEN-01-004 | token 作用域触发 WAF，人工验证通过 | yes |
| USE-MASK-01-001 | secret masking 相关 | yes |
| REL-LOG-01-040 | 日志相关表达式触发 WAF | — |
| SEC-ENV-WAIT-02-001 | 环境等待相关（不在本批次） | — |
| SEC-NAME-01-002 | secret 名触发 WAF（不在本批次） | — |

## Invalid 明细 (72)

| Case ID | 诊断数 | 诊断摘要 |
|---------|:-----:|------|
| COMP-CTX-01-052 | 1 | jobs[downstream].if: if表达式无法解析 表达式：needs.verify.result == 'success'第1位出现不支持的关键字 |
| COMP-EXPR-01-058 | 4 | jobs[verify].steps[4].if: if表达式无法解析 {0} |
| COMP-RUNNER-01-003 | 1 | jobs[verify].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]，如['codeart... |
| COMP-RUNNER-01-082 | 5 | jobs[probe].runs-on.small: unknown property |
| COMP-STAGES-01-002 | 1 | Cannot deserialize value of type `java.util.LinkedHashMap<java.lang.String,com.huawei.devcloud.cloud... |
| COMP-STAGES-01-003 | 2 | post.steps: unknown property |
| COMP-STAGES-01-004 | 2 | stages[build_stage].name: 值不能为空 |
| COMP-STAGES-01-005 | 1 | Cannot deserialize value of type `java.util.LinkedHashMap<java.lang.String,com.huawei.devcloud.cloud... |
| COMP-TRIG-01-079 | 1 | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32 |
| COMP-UNKNOWN-01-001 | 1 | unknown_field: unknown property |
| COMP-UNKNOWN-01-004 | 1 | stages[gated_stage].name: 值不能为空 |
| COMP-UNKNOWN-01-005 | 1 | inputs[branch_name].type: 值不能为空 |
| COMP-WFLOW-01-065 | 2 | post.steps: unknown property |
| COMPAT-ACTIONDEV-01-001 | 2 | jobs[test-action-meta].steps[1].uses: 格式错误：pluginname@version，其中 pluginname 为 1~50 位字母、数字、"-"、"_"，ve... |
| COMPAT-CONCUR-01-001 | 2 | concurrency.exceed-action: 值不能为空 |
| COMPAT-CONCUR-01-002 | 1 | Cannot deserialize value of type `java.lang.String` from Array value (token `JsonToken.START_ARRAY`)... |
| COMPAT-CONCUR-01-003 | 2 | concurrency.exceed-action: 值不能为空 |
| COMPAT-CONCUR-01-004 | 3 | concurrency.exceed-action: 值不能为空 |
| COMPAT-ENVIRON-01-001 | 1 | jobs[test].environment: unknown property |
| COMPAT-ENVIRON-01-002 | 1 | jobs[test-environment].environment: unknown property |
| COMPAT-EVENT-01-001 | 1 | on.release: unknown property |
| COMPAT-EXPR-01-013 | 2 | jobs[test-success-paren].steps[0].if: if表达式无法解析 表达式：success()第1位出现不支持的函数 |
| COMPAT-EXPR-01-014 | 1 | jobs[test-always-paren].steps[1].if: if表达式无法解析 表达式：always第1位出现不支持的关键字 |
| COMPAT-FIELD-01-001 | 1 | run-name: unknown property |
| COMPAT-FIELD-01-002 | 1 | jobs[test].services: unknown property |
| COMPAT-FIELD-01-003 | 1 | custom_field: unknown property |
| COMPAT-MIGRATE-01-001 | 1 | jobs[migrate-permissions].permissions: unknown property |
| COMPAT-MIGRATE-01-002 | 1 | run-name: unknown property |
| COMPAT-PATHS-01-001 | 1 | on.push: 列表长度超出限制，paths paths-ignore之和不能小于1或超过32 |
| COMPAT-PATHS-01-002 | 1 | on.push: 列表长度超出限制，paths paths-ignore之和不能小于1或超过32 |
| COMPAT-PERM-01-003 | 1 | permissions.contents: unknown property |
| COMPAT-PERM-01-006 | 2 | jobs[probe].permissions: unknown property |
| COMPAT-PR-01-002 | 1 | on.merge_requests.types: 列表中存在非法值:[opened] 允许值:[close, merge, open, reopen, update] |
| COMPAT-PR-01-003 | 1 | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32 |
| COMPAT-PR-01-004 | 1 | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32 |
| COMPAT-PR-01-005 | 1 | on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32 |
| COMPAT-PR-01-007 | 1 | on.merge_requests.types: 列表中存在非法值:[labeled] 允许值:[close, merge, open, reopen, update] |
| COMPAT-PR-01-008 | 1 | on.merge_requests.types: 列表中存在非法值:[ready_for_review] 允许值:[close, merge, open, reopen, update] |
| COMPAT-RUNNER-01-004 | 1 | jobs[test-custom-label].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]... |
| COMPAT-RUNNER-01-005 | 1 | jobs[test-intranet].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]，如['... |
| COMPAT-RUNSON-01-003 | 5 | jobs[probe].runs-on.group: unknown property |
| COMPAT-RUNSON-01-005 | 1 | jobs[probe].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]，如['codearts... |
| COMPAT-RUNSON-01-006 | 1 | jobs[probe].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]，如['codearts... |
| COMPAT-SECRET-01-005 | 1 | jobs[test-env-secret].environment: unknown property |
| COMPAT-SHELL-01-003 | 1 | jobs[test-windows-shell].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}... |
| COMPAT-VARS-01-005 | 1 | jobs[test-vars-if].steps[1].if: if表达式无法解析 表达式：vars.ENABLE_FEATURE == 'true'第1位出现不支持的关键字 |
| REL-POST-01-001 | 2 | post.steps: unknown property |
| REL-PREEMPT-01-006 | 2 | concurrency.preemption.events: 列表中存在非法值:[push] 允许值:[mr_id] |
| REL-RACE-01-048 | 1 | jobs[job_b].if: if表达式无法解析 表达式：failure()第1位出现不支持的函数 |
| REL-STAGES-01-029 | 2 | stages[next_stage].name: 值不能为空 |
| REL-STEPS-01-042 | 1 | jobs[test].steps: 列表长度必须在0到16之间 |
| SEC-DEFPERM-01-001 | 1 | jobs[override-write].permissions: unknown property |
| SEC-DEFPERM-01-002 | 1 | jobs[override-test].permissions: unknown property |
| SEC-ENV-01-001 | 1 | jobs[env-secret-approved].environment: unknown property |
| SEC-ENV-01-002 | 1 | jobs[env-secret-denied].environment: unknown property |
| SEC-PERM-01-001 | 1 | jobs[perm-read].permissions: unknown property |
| SEC-PERM-01-002 | 1 | jobs[perm-write-denied].permissions: unknown property |
| SEC-SUPPLY-01-003 | 2 | jobs[typo-test].steps[0].uses: 格式错误：pluginname@version，其中 pluginname 为 1~50 位字母、数字、"-"、"_"，version（官... |
| SEC-WCMD-01-003 | 1 | while scanning a simple key
 in 'string', line 11, column 1:
    INJECTED_VAR=bad" >> $ATOMGIT_ENV
 ... |
| SEC-WCMD-01-004 | 1 | while scanning a simple key
 in 'string', line 12, column 1:
    hijacked=bad" >> $ATOMGIT_OUTPUT
  ... |
| USE-ACT-01-004 | 1 | stages[default].jobs[market-name]: 插件AtomgitCache不存在 |
| USE-CONC-01-002 | 1 | concurrency.max: 值不能小于1 |
| USE-DOC-01-007 | 1 | jobs[deploy].environment: unknown property |
| USE-EXPR-01-002 | 1 | jobs[bad].steps[0].if: if表达式无法解析 表达式：unknownFunc()第1位出现不支持的函数 |
| USE-LBL-01-001 | 1 | jobs[bad].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]，如['codearts-h... |
| USE-PERM-01-002 | 1 | permissions.contents: unknown property |
| USE-RUN-01-002 | 1 | jobs[bad-runner].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]，如['cod... |
| USE-STAT-01-002 | 1 | jobs[bad-stat].steps[0].if: if表达式无法解析 表达式：success()第1位出现不支持的函数 |
| USE-TYPE-01-002 | 1 | on.merge_requests.types: 列表中存在非法值:[opened] 允许值:[close, merge, open, reopen, update] |
| USE-UNKN-01-001 | 1 | run-name: unknown property |
| USE-YAML-01-001 | 1 | on: 值不能为空 |
| USE-YAML-01-002 | 1 | while parsing a block mapping
 in 'string', line 5, column 5:
        name: indent error
        ^
e... |

## SKIP (26)

- REL-K8S-01-046
- REL-K8S-01-047
- REL-K8S-01-048
- REL-K8S-01-049
- REL-K8S-01-050
- REL-K8S-01-051
- REL-VCJOB-01-001
- REL-VCJOB-01-002
- SEC-AUDIT-01-001
- SEC-NAME-01-003
- SEC-SECMGMT-01-002
- SEC-WFRUN-01-001
- USE-ACT-01-003
- USE-API-01-001
- USE-DIR-01-002
- USE-DOC-01-001
- USE-DOC-01-002
- USE-DOC-01-006
- USE-EXPR-01-003
- USE-LBL-01-003
- USE-LBL-01-005
- USE-ONBD-01-001
- USE-PATH-01-001
- USE-RES-01-001
- USE-UNKN-01-004
- USE-VARS-01-001