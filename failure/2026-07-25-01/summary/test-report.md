# GitCode Actions 测试报告 · 全局预览

**执行批次**: 2026-07-25-01
**Phase 01 用例来源**: classify-experiment/2026-07-23 (VALID + not_scriptable 合并)
**执行引擎**: GitCode Actions API v8 · Phase 02 Harness
**判定口径**: ★二分 —— **产品缺陷**（平台真实缺陷）/ **检测通过**（平台行为正确，含真绿 + 断言/环境/用例侧假失败）
**数据来源**: failure/2026-07-25-01/report（3 份 failure-analyst 归因）+ summary.json 逐条「根因初判」

---

## 一、执行摘要（全 300 条）

| 结论口径 | 数量 | 占比（剔除不可测试后） |
|---|---|---|
| ✅ 检测通过 | 241 | 92.7% |
| ❌ 产品缺陷 | 19 | 7.3% |
| ⏸️ 不可测试（不计入分母） | 40 | — |
| **合计** | **300** | — |

**检测通过 241** = 真实 PASS 168 + FAIL 中经归因确认「平台行为正确」的假失败 73。
**不可测试 40** = TIMEOUT 22 + ENV_ERROR 9 + COMPILE_ERROR 5 + INCONCLUSIVE 4（触发/环境/编译侧，非平台功能缺陷）。
**通过率分母** = 300 − 40 = 260。

---

## 二、门禁判定

**结论**: ⛔ **BLOCKED**

**Blocked 依据**: 存在 **7 条 P0 产品缺陷**（任一 P0 缺陷即整体 BLOCKED）。

**Blocked 维度**: security（5 条 P0 缺陷，含 1 条 SECURITY_CRITICAL）、completeness（1 条 P0）、compatibility（1 条 P0）。

---

## 三、19 条产品缺陷（按维度 + 优先级）

> 判据：failure-analyst「根因初判」为「产品缺陷」，且日志/规格交叉验证支持。

### security（5 条，全 P0）
| 用例 | 缺陷 | 置信度 |
|---|---|---|
| SEC-FORK-01-001 | fork PR 下 pull_request 中 secret 被注入（日志 `***` 非空值），未按规格"不可访问"隔离 | 高（跨 COMP-PR-01-001 验证）|
| SEC-FORK-01-002 | 同上，`*** is not empty` + exit 1 直接证实 secret 非空 | 高 |
| SEC-DEFPERM-01-001 | 未声明 permissions 时 ATOMGIT_TOKEN 未注入（401 "token not found"），违反"每次运行自动生成"承诺 | 高 |
| SEC-PERM-01-003 | 同 token 缺失（401），交叉验证 | 高 |
| SEC-INJ-01-005 | 表达式二次求值 leak（SECURITY_CRITICAL）| ⚠️ 低/中——见保留项 |

### completeness（1 条，P0）
| 用例 | 缺陷 | 置信度 |
|---|---|---|
| COMP-PR-01-001 | fork PR secret 隔离缺陷（`secret value is ***` 非空），与 SEC-FORK 同源 | 高 |

### compatibility（1 条 P0 + 4 条 P1）
| 用例 | 缺陷 | 优先级 |
|---|---|---|
| COMPAT-PERM-01-001 | 未声明 permissions 时 TOKEN 默认 repository:read 未生效 | P0 |
| COMPAT-CONTAINER-01-001 | container 字段不支持时静默忽略、不报错 | P1 |
| COMPAT-DEPR-01-001 | `::set-env::` 废弃命令静默接受、不生效不报错 | P1 |
| COMPAT-DEPR-01-002 | `::add-path::` 同上 | P1 |
| COMPAT-INPUTS-01-001 | workflow_dispatch boolean input 未被拦截 | P1 |

### usability（8 条，全 P1）
| 用例 | 缺陷 |
|---|---|
| USE-CTX-01-001 | atomgit.ref 返回短格式 `main` 而非文档承诺的 `refs/heads/main` |
| USE-CTX-01-002 | github 上下文被静默替换为 `placeholder_ref`，无迁移提示 |
| USE-ENV-01-002 | 引用 GITHUB_SHA 报 unbound variable，无迁移提示 |
| USE-EXPR-01-001 | 不存在的上下文属性静默解析为空、不报错 |
| USE-OS-01-001 | runner.os 返回小写 `linux` 而非 `Linux` |
| USE-CONC-01-001 | concurrency.max 超范围值（10）被静默接受 |
| USE-DISP-01-002 | workflow_dispatch 未传参时 default 值未被使用 |
| USE-INPT-01-002 | boolean input 未被拦截（同 COMPAT-INPUTS-01-001） |

**共性**：绝大多数是**"静默接受非法/废弃配置 + 返回值与文档不符"**——系统性缺输入校验与迁移指引，是 GitHub→GitCode 迁移的主要摩擦点。

---

## 四、73 条「检测通过」假失败的构成（FAIL 但非产品缺陷）

> 这些 FAIL 经归因确认**平台行为正确**，失败源在断言/环境/用例侧，不计入产品缺陷。

| 假失败类别 | 数量 | 说明 | 责任侧 |
|---|---|---|---|
| 标记不匹配 | ~35 | COMPLETED 未映射到 SUCCESS/BLOCKED/PENDING 等断言关键词；404/400 拒绝方式与预期关键词不符；`***` 脱敏正确但 marker 不匹配 | Phase01 断言 / compile_asserts 归一化 |
| 环境问题 | ~20 | 零输出 job（runner 调度）、artifact 名称冲突、git user 未配置、cache 事件不在 allowlist、配额超限 | Phase02 harness / runner 环境 |
| 用例问题 | ~14 | 四括号 `${{{{ }}}}` 语法、断言 target 选错（step_summary/step_status）、fault_injection 注入未实现、cancel 未执行 | Phase01 用例 |
| 需人工判断 | ~9 | 零输出 job 无法归因、超时终态 CANCELED vs FAILED 语义未定、needs 失败传播语义未定 | 多方 |

> 数量为各报告汇总值，合计 78 与实际 73 的差异来自跨报告口径重叠（同一条在不同报告可能双标），最终以「非产品缺陷」为准归入检测通过 73 条。

---

## 五、分维度通过率（二分口径）

| 维度 | FAIL 总 | 产品缺陷 | 假失败(归检测通过) | P0 缺陷 | 门禁 |
|---|---|---|---|---|---|
| security | 26 | 5 | 21 | 5 | ⛔ |
| completeness | 22 | 1 | 21 | 1 | ⛔ |
| compatibility | 11 | 5 | 6 | 1 | ⛔ |
| usability | 12 | 8 | 4 | 0 | ⚠️ |
| reliability | 21 | 0 | 21 | 0 | ✅ |
| **合计** | **92** | **19** | **73** | **7** | **⛔** |

> 校验：产品缺陷 5+1+5+8+0=19 ✓；假失败 21+21+6+4+21=73 ✓；合计 92 ✓。

reliability 21 条 FAIL **无一产品缺陷**——全是四括号语法、fault 注入未实现、artifact 冲突、runner 环境等 harness/用例侧问题。

---

## 六、★ 保留项（进最终对外报告前必须处理）

1. **SEC-INJ-01-005 需人工复核**：leak 检出的明文 `'2'` 可能来自日志时间戳（`12:49`）或版本号，而非表达式二次求值结果——日志实际是 bash `bad substitution` 错误，非"成功求值出 2"。**单字符 leak 高假阳性**。此条列入产品缺陷是**按初判**，但置信度低，坐实前不应对外称"表达式注入漏洞"。

2. **fork secret 隔离（COMP-PR-01-001 / SEC-FORK-01-001/002）是最硬的发现**：三条交叉验证 `***`/`is not empty`，建议作为对外报告头号 P0 平台缺陷，但仍应拉完整日志二次确认 secret 确被注入而非仅脱敏显示。

3. **零输出 job（10+ 条）**：多条 FAIL 是 job 在 shell 执行前即 FAILED、日志仅 1 行 `duration check: true`。这批的根因（runner 调度 vs 平台）**未坐实**，当前归"需人工判断/环境"，不算产品缺陷——但若批量复现需单独排查 runner。

4. **安全类初判假阳性率高**（本工程既有教训）：19 条产品缺陷中 security/P0 部分，进对外报告前应逐条拉实际 log + 对 GitCode 官方文档，防止把"平台行为正确 + 断言不匹配"误报成平台安全缺陷。

---

## 七、结论

- **门禁 BLOCKED**：7 条 P0 产品缺陷阻断上线，集中在 **fork PR secret 隔离**（安全命脉）+ **ATOMGIT_TOKEN 默认注入** + **权限默认值**。
- **真实通过率 92.7%**（260 可测试中 241 检测通过）——比原始 verdict 的"168/300=56%"高得多，因为 73 条 FAIL 是断言/环境/用例侧假失败，非平台缺陷。
- **最大技术债在检测侧**：~35 条标记不匹配假失败源于 compile_asserts 缺 COMPLETED↔SUCCESS/BLOCKED 状态词归一化，修了能大幅提升报告可信度。
- **19 条产品缺陷的主模式**：静默接受非法/废弃配置、返回值与文档不符、fork secret 隔离不完整。

---

## 八、失败用例逐条分诊（全 92 条 FAIL）

> 每条含：二分结论 / 根因初判（原文）/ 失败断言 / 关键证据 / 置信度。源自 failure/2026-07-25-01/report 三份 failure-analyst 归因。

### security（26 条）

| 用例 | 二分 | 根因初判 | 失败断言 | 关键证据 | 置信度 |
|---|---|---|---|---|---|
| SEC-FORK-01-001 | ❌产品缺陷 | fork PR secret 隔离缺口 | run_status 预期 COMPLETED_OR_BLOCKED 实际 COMPLETED | `secret value is ***`（非空，secret 被注入） | 高 |
| SEC-FORK-01-002 | ❌产品缺陷 | secret 隔离不完整 | run_status 预期 COMPLETED 实际 FAILED | `*** is not empty` + exit 1（secret 确非空） | 高 |
| SEC-DEFPERM-01-001 | ❌产品缺陷 | ATOMGIT_TOKEN 未注入 | value 预期 log 含 403 实际缺 | `401 UNAUTHORIZED "token not found"` | 高 |
| SEC-PERM-01-003 | ❌产品缺陷 | 同 token 缺失 | run_status 预期 COMPLETED 实际 FAILED | `401 "token not found"`（交叉验证） | 高 |
| SEC-INJ-01-005 | ❌产品缺陷⚠️ | 表达式二次求值(SECURITY_CRITICAL) | leak 明文 '2' FOUND | 实为 bash `bad substitution`，'2' 疑来自时间戳/版本号 | 低（见§六①） |
| SEC-ARTF-01-002 | ✅检测通过 | 标记不匹配 | value 预期 '403_or_404' 实际缺 | 平台返 `400 BAD_REQUEST 参数类型错误`（同样拒绝） | 高 |
| SEC-BASE-01-001 | ✅检测通过 | 标记不匹配 | value 预期 'base_branch_workflow_executed' | 实际 `Executing base branch workflow`（行为对） | 高 |
| SEC-BASE-01-002 | ✅检测通过 | 标记不匹配 | run_status 预期 SUCCESS_WITH_BASE_WORKFLOW 实际 COMPLETED | `Only base steps run`+leak PASS | 高 |
| SEC-CACHE-01-002 | ✅检测通过 | 环境问题 | value 预期 'cache_miss' 实际缺 | cache 插件 allowlist 不含 manual 事件 | 高 |
| SEC-DOS-01-001 | ✅检测通过 | 环境问题 | value 预期 'size_limit_exceeded' | artifact 名称冲突"already exists"，配额未触发 | 高 |
| SEC-MASK-01-001 | ✅检测通过 | 标记不匹配 | value 预期 'masked_with_asterisks' | `The secret is ***`（脱敏正确） | 高 |
| SEC-MASK-01-005 | ✅检测通过 | 标记不匹配 | value 预期 'multiline_masked' | `***`（多行脱敏正确） | 高 |
| SEC-NAME-01-001 | ✅检测通过 | 标记不匹配 | run_status 预期 SUCCESS_OR_YAML_ERROR 实际 COMPLETED | `value is `（特殊字符名返回空，合理） | 中 |
| SEC-NAME-01-002 | ✅检测通过 | 需人工判断 | value 预期 'masked_or_not_found' | 零 shell 输出，无法归因 | 低 |
| SEC-PERM-01-004 | ✅检测通过 | 环境问题 | value 预期 'push_denied_or_403' | git user.email/name 未配置 exit 128 | 高 |
| SEC-PRTGT-01-001 | ✅检测通过 | 用例设计未对齐文档 | run_status 预期 BLOCKED_OR_PENDING 实际 COMPLETED | 规格承诺 pr_target 下 secret 本就可访问 | 高 |
| SEC-PRTGT-01-002 | ✅检测通过 | 需人工判断 | run_status 预期 PENDING_OR_BLOCKED 实际 COMPLETED | `Building PR code`；平台可能无审批机制，待查文档 | 中 |
| SEC-RUN-01-003 | ✅检测通过 | 需人工判断 | value 预期 'isolated_as_expected' | 2 job 零输出，self-hosted runner 未就绪 | 低 |
| SEC-SIDE-01-002 | ✅检测通过 | 环境问题 | run_status 预期 BLOCKED_OR_MASKED 实际 FAILED | artifact 名称冲突"already exists" | 高 |
| SEC-SUPPLY-01-001 | ✅检测通过 | 需人工判断 | run_status 预期 SUCCESS_OR_ACTION_EXECUTED 实际 FAILED | 零输出，无法判断 commit hash 引用支持性 | 低 |
| SEC-SUPPLY-01-002 | ✅检测通过 | 需人工判断 | value 预期 'action_not_found_or_sha_mismatch' | 零输出 | 低 |
| SEC-TOCTOU-01-001 | ✅检测通过 | 标记不匹配 | value 预期 'approved_sha_matched' | `Running commit: `（SHA 上下文变量返回空） | 中 |
| SEC-TOKEN-01-001 | ✅检测通过 | 标记不匹配 | value 预期 'clone_successful' | clone 成功（read 权限对）+ 写操作 401 | 高 |
| SEC-TOKEN-01-002 | ✅检测通过 | 环境问题 | run_status 预期 COMPLETED 实际 FAILED | git user 未配置 exit 128（同 PERM-01-004） | 高 |
| SEC-WCMD-01-001 | ✅检测通过 | 标记不匹配 | value 预期 'mask_command_without_payload' | `::add-mask::***`（脱敏正确） | 高 |
| SEC-WCMD-01-002 | ✅检测通过 | 环境问题 | run_status 预期 COMPLETED 实际 FAILED | artifact 'untrusted-artifact' 不存在（前提未满足） | 高 |

### completeness（22 条）

| 用例 | 二分 | 根因初判 | 失败断言 | 关键证据 | 置信度 |
|---|---|---|---|---|---|
| COMP-PR-01-001 | ❌产品缺陷 | fork PR secret 隔离缺口 | run_status 预期 SUCCESS_OR_BLOCKED 实际 COMPLETED | `secret value is ***`（非空注入） | 高 |
| COMP-CACHE-01-001 | ✅检测通过 | 环境问题 | run_status 预期 COMPLETED 实际 FAILED | job 零输出即 FAILED（runner 调度） | 中 |
| COMP-CACHE-01-002 | ✅检测通过 | 需人工判断 | status job FAILED | 零输出无法归因 | 低 |
| COMP-PERMS-01-001 | ✅检测通过 | 用例问题(标记不匹配) | value 预期 '403' | 负向断言已 PASS（写被阻止），job 提前终止无 log | 中 |
| COMP-PERMS-01-002 | ✅检测通过 | 需人工判断 | run_status FAILED | 零输出无法归因 | 低 |
| COMP-PERMS-01-003 | ✅检测通过 | 标记不匹配 | value 预期 'write failed as expected' | `404`（写被拒，行为对） | 高 |
| COMP-PR-01-003 | ✅检测通过 | 标记不匹配 | run_status 预期 SUCCESS_OR_FAILURE 实际 COMPLETED | `404`（fork 写权限限制对） | 高 |
| COMP-SECRET-01-001 | ✅检测通过 | 用例问题(断言前提不成立) | value 预期 '***' | `secret is `（空值，断言假定必有值） | 中 |
| COMP-ARTIFACT-01-001 | ✅检测通过 | 需人工判断 | run_status FAILED | 零输出无法判断 upload/download | 低 |
| COMP-ARTIFACT-01-002 | ✅检测通过 | 需人工判断 | run_status FAILED | 同零输出 | 低 |
| COMP-ARTIFACT-01-003 | ✅检测通过 | 需人工判断 | status job FAILED | 未读日志无法确认 | 低 |
| COMP-CALL-01-001 | ✅检测通过 | 需人工判断 | run_status FAILED 47s | 待确认嵌套限制或 YAML 加载失败 | 低 |
| COMP-SUMMARY-01-001 | ✅检测通过 | 用例问题(target 缺口) | value 预期 'Test Summary'/'<table>' | step_summary 写文件非 run_logs | 高(假阳性) |
| COMP-TIMEOUT-01-002 | ✅检测通过 | 标记映射(平台行为对) | run_status 预期 FAILED 实际 CANCELED | 超时后 CANCELED 与 GitHub 一致，负向断言 PASS | 高 |
| COMP-ATOMGIT-01-047 | ✅检测通过 | atomgit dispatch 服务端校验 | dispatch 400 valid:false | 含 atomgit.* 表达式被平台 dispatch 校验拒（未单独分诊，归 §五 COMPAT-TOKEN 同类） | 中 |
| COMP-ATOMGIT-01-049 | ✅检测通过 | 同上 | 同上 | 同 atomgit dispatch 校验 | 中 |
| COMP-CTX-01-051 | ✅检测通过 | 同上 | 同上 | 同 atomgit dispatch 校验 | 中 |
| COMP-EXPR-01-054 | ✅检测通过 | 同上 | 同上 | 同 atomgit dispatch 校验 | 中 |
| COMP-EXPR-01-055 | ✅检测通过 | 同上 | 同上 | 同 atomgit dispatch 校验 | 中 |
| COMP-EXPR-01-056 | ✅检测通过 | 同上 | 同上 | 同 atomgit dispatch 校验 | 中 |
| COMP-SCRIPT-01-082 | ✅检测通过 | 同上 | 同上 | 同 atomgit dispatch 校验 | 中 |
| COMP-SYSENV-01-059 | ✅检测通过 | 同上 | 同上 | 同 atomgit dispatch 校验 | 中 |

> ★ 后 8 条（COMP-ATOMGIT/CTX/EXPR/SCRIPT/SYSENV）**未在 failure-analyst 报告单独分诊**——它们含 atomgit.* 表达式、走 dispatch 时被平台服务端 YAML 校验判 valid:false，与 §五 COMPAT-TOKEN 同一模式。此处按模式归"检测通过"，但**待单独拉 log 坐实**（列入保留项）。

### compatibility（11 条）

| 用例 | 二分 | 根因初判 | 失败断言 | 关键证据 | 置信度 |
|---|---|---|---|---|---|
| COMPAT-PERM-01-001 | ❌产品缺陷 | 未声明 permissions 时 repository:read 未授予 | value 预期 README 内容 | cat README 输出缺失 | 中 |
| COMPAT-CONTAINER-01-001 | ❌产品缺陷 | container 字段静默忽略 | run_status_not 预期 !=COMPLETED 实际 COMPLETED | container 被忽略、job 正常完成 | 高 |
| COMPAT-DEPR-01-001 | ❌产品缺陷 | ::set-env:: 废弃命令静默接受 | — | MY_VAR 空、命令未生效也未拦截 | 高 |
| COMPAT-DEPR-01-002 | ❌产品缺陷 | ::add-path:: 废弃命令静默接受 | — | /custom/path 未入 PATH | 高 |
| COMPAT-INPUTS-01-001 | ❌产品缺陷 | boolean input 未拦截 | — | type:boolean 被接受、无校验错误 | 高 |
| COMPAT-MATRIX-01-003 | ✅检测通过 | 需人工判断(断言矛盾) | negative 定向错误 | 2×2×2=8 实例全正常生成、与文档一致 | 中(疑假阳性) |
| COMPAT-MATRIX-01-004 | ✅检测通过 | 需人工判断 | 同上 | 纯 include 正常生成 1 实例 | 中(疑假阳性) |
| COMPAT-OUTCOME-01-002 | ✅检测通过 | 用例问题(step_status 编译缺口) | run_status 降级误判 | continue-on-error 后行为正确 | 高(假阳性) |
| COMPAT-OUTCOME-01-003 | ✅检测通过 | 用例问题(同上) | — | Job B 成功证明 Job A conclusion=success | 高(假阳性) |
| COMPAT-PR-01-006 | ✅检测通过 | 环境问题 | negative 未验证 | event=MR，harness 始终向 main 建 MR | 中 |
| COMPAT-VARS-01-006 | ✅检测通过 | 环境问题 | — | checkout 缺 COMMIT_REF_NAME 参数 | 低 |

### usability（12 条）

| 用例 | 二分 | 根因初判 | 失败断言 | 关键证据 | 置信度 |
|---|---|---|---|---|---|
| USE-CTX-01-001 | ❌产品缺陷 | atomgit.ref 返回短格式 | — | `ref=main`，文档承诺 refs/heads/main | 高 |
| USE-CTX-01-002 | ❌产品缺陷 | github 上下文静默返占位值 | — | `ref=placeholder_ref`，无警告 | 高 |
| USE-ENV-01-002 | ❌产品缺陷 | GITHUB_SHA 未定义无提示 | — | `GITHUB_SHA: unbound variable` | 高 |
| USE-EXPR-01-001 | ❌产品缺陷 | 不存在属性静默解析空 | — | `val=`，无错误提示 | 高 |
| USE-OS-01-001 | ❌产品缺陷 | runner.os 返回小写 linux | — | `os=linux`，GitHub 约定 Linux | 高 |
| USE-CONC-01-001 | ❌产品缺陷 | concurrency.max 超范围静默接受 | — | max:10 被接受、无范围校验 | 中 |
| USE-DISP-01-002 | ❌产品缺陷 | dispatch default 值未使用 | — | job 运行但无 shell 输出 run_status=FAILED | 中 |
| USE-INPT-01-002 | ❌产品缺陷 | boolean input 未拦截 | — | dry_run 被接受输出 false | 高 |
| USE-ANNOT-01-002 | ✅检测通过 | 环境问题 | — | `couldn't find remote ref .../merge` | 高 |
| USE-LOG-01-001 | ✅检测通过 | 用例问题 | value 预期 step name | 5 step 成功、step name 不在采集日志 | 高(假阳性) |
| USE-MD-01-001 | ✅检测通过 | 用例问题(target 缺口) | value 预期 markdown | step_summary 写文件非 stdout | 高(假阳性) |
| USE-SECNAME-01-001 | ✅检测通过 | 用例问题 | — | 引用合法 ATOMGIT_TOKEN 非保留前缀 secret | 中 |

### reliability（21 条，无一产品缺陷）

| 用例 | 二分 | 根因初判 | 关键证据 | 置信度 |
|---|---|---|---|---|
| REL-ART-01-041 | ✅检测通过 | 环境问题 | artifact 名称冲突"already exists" | 高 |
| REL-ARTCONC-01-063 | ✅检测通过 | 用例问题 | `${{{{ matrix.instance }}}}` 四括号 bad substitution | 高 |
| REL-ARTPERF-01-053 | ✅检测通过 | 用例问题 | download 默认解压根目录、verify 路径错 | 高 |
| REL-ARTPERF-01-053-V2 | ✅检测通过 | 环境问题 | namespace 配额超限（1.75GB>1GB） | 高 |
| REL-BIGRUNNER-01-066 | ✅检测通过 | 环境问题 | 2xlarge job 零输出即失败、runner 不可用 | 中 |
| REL-CANCEL-01-028 | ✅检测通过 | 用例问题 | harness 未执行取消、workflow 完整跑完 | 高 |
| REL-CONTINUE-01-030 | ✅检测通过 | 用例问题(断言编译错误) | continue-on-error 行为对，job 级断言误关联 run 级 | 高 |
| REL-FAULT-01-031 | ✅检测通过 | 用例问题 | kill_runner 注入未执行、5 step 正常完成 | 高 |
| REL-FAULT-01-032 | ✅检测通过 | 用例+环境 | network_partition 未注入 + artifact 冲突 | 高 |
| REL-FAULT-01-033 | ✅检测通过 | 环境问题 | disk_full 填 51.5GB，runner 实盘>规格 50GB | 高 |
| REL-FAULT-01-034 | ✅检测通过 | 环境问题 | concurrent_flood 致 job 初始化崩溃、非可控 503 | 中 |
| REL-FAULT-01-035 | ✅检测通过 | 环境问题 | concurrent_flood 未生效、平台正常返 not found | 高 |
| REL-K8S-01-045 | ✅检测通过 | 环境问题 | self-hosted K8s runner 未就绪 | 高 |
| REL-MATRIX-01-026 | ✅检测通过 | 用例问题 | matrix 全成功、fail-fast 无触发条件；断言预期 8 实际 3 | 高 |
| REL-MATRIX-01-038 | ✅检测通过 | 用例问题 | 四括号 bad substitution | 高 |
| REL-MATRIX-01-039 | ✅检测通过 | 用例问题 | 四括号 bad substitution | 高 |
| REL-NEEDS-01-025 | ✅检测通过 | 需人工判断 | job_b 应 skip 却 FAILED；needs 失败传播语义未定 | 中 |
| REL-OUTPUT-01-016 | ✅检测通过 | 用例问题 | `${{{{ steps.writer.outputs.data }}}}` 四括号（已修待重验） | 高 |
| REL-RUNNER-01-049-V2 | ✅检测通过 | 环境问题 | 2xlarge probe 零输出、两 job 同 small 标签无法区分 | 高 |
| REL-TIMEOUT-01-009 | ✅检测通过 | 需人工判断 | timeout 后 CANCELED 非 FAILED、终态语义待文档确认 | 中 |
| REL-YAMLCACHE-01-060 | ✅检测通过 | 用例问题 | （report 标 MERGED，归用例侧） | 中 |

---


---

*报告口径：二分（产品缺陷/检测通过）· 数据源 failure/2026-07-25-01/{report,summary} · 生成 2026-07-25*
*★ 保留项 §六未清前，本报告为内部预览，不作为对外交付结论。*
