# 断言-步骤一致性报告

**日期**: 2026-07-25
**用例总数**: 369（另有 50 例缺 Phase 01 文本规格）

---

## 1. 总览

| 评级 | 数量 | 说明 |
|------|:---:|------|
| 断言一致 | 155 | 所有验证点被 workflow 步骤真实覆盖 |
| 部分不符 | 176 | 部分验证点存在空洞、缺失或无法由步骤产出 |
| 完全不符 | 38 | 全部验证点为空洞/缺失/必然结果 |
| **合计** | **369** | |

**部分不符内部分类**:
- 部分不符: 131
- 存在空洞: 17
- 不可评估: 16
- 混合问题: 12

## 2. 按维度分布

| 维度 | 断言一致 | 部分不符 | 完全不符 | 合计 |
|------|:---:|:---:|:---:|:---:|
| 完备性 | 40 | 32 | 16 | 88 |
| 兼容性 | 72 | 43 | 3 | 118 |
| 可靠性 | 11 | 58 | 5 | 74 |
| 安全性 | 15 | 30 | 6 | 51 |
| 易用性 | 17 | 13 | 8 | 38 |

## 断言一致 — 所有验证点真实覆盖（155 例）

| # | Case ID | 标题 | 原因 |
|---|---------|------|------|
| 1 | [COMP-ARTIFACT-01-001](case/COMP-ARTIFACT-01-001.md) | artifact 可在同 workflow 的 job 间正确传递 | 共 2 个验证点全部真实覆盖 |
| 2 | [COMP-ARTIFACT-01-002](case/COMP-ARTIFACT-01-002.md) | 下载全部制品功能正常 | 共 1 个验证点全部真实覆盖 |
| 3 | [COMP-ARTIFACT-01-003](case/COMP-ARTIFACT-01-003.md) | artifact 保留期设置生效 | 共 2 个验证点全部真实覆盖 |
| 4 | [COMP-CACHE-01-001](case/COMP-CACHE-01-001.md) | cache hit 时恢复缓存内容正确 | 共 2 个验证点全部真实覆盖 |
| 5 | [COMP-CACHE-01-002](case/COMP-CACHE-01-002.md) | restore-keys 前缀匹配兜底生效 | 共 1 个验证点全部真实覆盖 |
| 6 | [COMP-CALL-01-002](case/COMP-CALL-01-002.md) | 3 层 workflow_call 嵌套应被拒绝 | 共 2 个验证点全部真实覆盖 |
| 7 | [COMP-CTX-01-051](case/COMP-CTX-01-051.md) | 上下文在 workflow job step 各级注入验证 | 共 3 个验证点全部真实覆盖 |
| 8 | [COMP-CTX-01-053](case/COMP-CTX-01-053.md) | 上下文在 Action 插件参数中注入验证 | 共 1 个验证点全部真实覆盖 |
| 9 | [COMP-DIR-01-001](case/COMP-DIR-01-001.md) | .gitcode/workflows/ 下的 YAML 被正确识别并触发 | 共 2 个验证点全部真实覆盖 |
| 10 | [COMP-DIR-01-002](case/COMP-DIR-01-002.md) | .github/workflows/ 下的 YAML 不被识别为 workflow | 共 1 个验证点全部真实覆盖 |
| 11 | [COMP-EXPR-01-057](case/COMP-EXPR-01-057.md) | format substring replace 函数边界行为 | 共 3 个验证点全部真实覆盖 |
| 12 | [COMP-ISOLATION-01-002](case/COMP-ISOLATION-01-002.md) | 环境变量不跨 job 泄漏 | 共 1 个验证点全部真实覆盖 |
| 13 | [COMP-JOB-01-067](case/COMP-JOB-01-067.md) | job 可选字段 env if timeout-minutes needs 验证 | 共 3 个验证点全部真实覆盖 |
| 14 | [COMP-JOB-01-068](case/COMP-JOB-01-068.md) | job strategy 矩阵与 continue-on-error 验证 | 共 3 个验证点全部真实覆盖 |
| 15 | [COMP-PERMS-01-001](case/COMP-PERMS-01-001.md) | permissions 空对象时 ATOMGIT_TOKEN 仅 repositor | 共 2 个验证点全部真实覆盖 |
| 16 | [COMP-PERMS-01-002](case/COMP-PERMS-01-002.md) | 声明 repository write 后 TOKEN 可推送代码 | 共 1 个验证点全部真实覆盖 |
| 17 | [COMP-PUSH-01-002](case/COMP-PUSH-01-002.md) | 不匹配 branches 的 push 不触发 workflow | 共 1 个验证点全部真实覆盖 |
| 18 | [COMP-RERUN-01-001](case/COMP-RERUN-01-001.md) | rerun 后 atomgit.sha 保持原始值 run_number 递增 | 共 2 个验证点全部真实覆盖 |
| 19 | [COMP-RUNNER-01-001](case/COMP-RUNNER-01-001.md) | 三段式标签正确调度到对应规格 Runner | 所有断言均可在流程中验证 |
| 20 | [COMP-RUNNER-01-002](case/COMP-RUNNER-01-002.md) | runs-on default 等效 ubuntu-latest x64 small | 所有断言均可在流程中验证 |
| 21 | [COMP-RUNNER-01-080](case/COMP-RUNNER-01-080.md) | runner 上下文属性可访问性验证 | 共 3 个验证点全部真实覆盖 |
| 22 | [COMP-SCRIPT-01-081](case/COMP-SCRIPT-01-081.md) | 仓库内脚本执行与路径验证 | 共 2 个验证点全部真实覆盖 |
| 23 | [COMP-SCRIPT-01-082](case/COMP-SCRIPT-01-082.md) | 脚本权限设置与直接执行验证 | 共 2 个验证点全部真实覆盖 |
| 24 | [COMP-SECRET-01-001](case/COMP-SECRET-01-001.md) | echo secret 在日志中被脱敏为 *** | 共 1 个验证点全部真实覆盖 |
| 25 | [COMP-SECRET-01-002](case/COMP-SECRET-01-002.md) | secret 原始值不应以明文出现在标准日志中 | 共 1 个验证点全部真实覆盖 |
| 26 | [COMP-SECRET-01-003](case/COMP-SECRET-01-003.md) | base64 编码后的 secret 是否仍被脱敏 | 共 1 个验证点全部真实覆盖 |
| 27 | [COMP-STAGES-01-002](case/COMP-STAGES-01-002.md) | fail_fast true 时 stage 内任一 job 失败终止同阶段其余 j | 所有断言均可在流程中验证 |
| 28 | [COMP-STATUS-01-002](case/COMP-STATUS-01-002.md) | 失败 step 的日志完整保留且可查看 | 共 2 个验证点全部真实覆盖 |
| 29 | [COMP-STEP-01-069](case/COMP-STEP-01-069.md) | step 必填与核心字段 name run uses 验证 | 共 3 个验证点全部真实覆盖 |
| 30 | [COMP-STEP-01-070](case/COMP-STEP-01-070.md) | step 可选字段 id env if with 验证 | 共 3 个验证点全部真实覆盖 |
| 31 | [COMP-SUMMARY-01-001](case/COMP-SUMMARY-01-001.md) | ATOMGIT_STEP_SUMMARY Markdown 表格与标题正确渲染 | 共 2 个验证点全部真实覆盖 |
| 32 | [COMP-SUMMARY-01-002](case/COMP-SUMMARY-01-002.md) | summary 中不应暴露系统内部路径 | 共 1 个验证点全部真实覆盖 |
| 33 | [COMP-SYSENV-01-059](case/COMP-SYSENV-01-059.md) | ATOMGIT 系统环境变量关键变量存在性 | 共 2 个验证点全部真实覆盖 |
| 34 | [COMP-SYSENV-01-060](case/COMP-SYSENV-01-060.md) | ATOMGIT 系统环境变量值正确性 | 共 3 个验证点全部真实覆盖 |
| 35 | [COMP-TIMEOUT-01-002](case/COMP-TIMEOUT-01-002.md) | 超时的 job 被强制终止并标记为 failure | 共 2 个验证点全部真实覆盖 |
| 36 | [COMP-TRIG-01-072](case/COMP-TRIG-01-072.md) | push 事件关键字段与过滤验证 | 共 3 个验证点全部真实覆盖 |
| 37 | [COMP-TRIG-01-074](case/COMP-TRIG-01-074.md) | workflow_dispatch 事件关键字段与 inputs 验证 | 共 3 个验证点全部真实覆盖 |
| 38 | [COMP-TRIG-01-077](case/COMP-TRIG-01-077.md) | pull_request_comment 事件关键字段与过滤验证 | 共 3 个验证点全部真实覆盖 |
| 39 | [COMP-UNKNOWN-01-002](case/COMP-UNKNOWN-01-002.md) | 不应静默忽略未知字段导致用户误以为配置生效 | 共 1 个验证点全部真实覆盖 |
| 40 | [COMP-VARREF-01-083](case/COMP-VARREF-01-083.md) | YAML 表达式与 Shell 环境变量引用方式验证 | 共 2 个验证点全部真实覆盖 |
| 41 | [COMPAT-ACTION-01-001](case/COMPAT-ACTION-01-001.md) | checkout 短名等价性——ref 参数支持 | 共 3 个验证点全部真实覆盖 |
| 42 | [COMPAT-ACTION-01-002](case/COMPAT-ACTION-01-002.md) | checkout 短名等价性——path 参数支持 | 共 4 个验证点全部真实覆盖 |
| 43 | [COMPAT-ACTIONDEV-01-001](case/COMPAT-ACTIONDEV-01-001.md) | action.yml 元数据校验与 GitHub 差异 | 所有断言均可在流程中验证 |
| 44 | [COMPAT-ARTIFACT-01-001](case/COMPAT-ARTIFACT-01-001.md) | upload/download-artifact 跨 job 传递等价性 | 共 4 个验证点全部真实覆盖 |
| 45 | [COMPAT-ARTIFACT-01-002](case/COMPAT-ARTIFACT-01-002.md) | upload-artifact 保留期行为等价性 | 共 3 个验证点全部真实覆盖 |
| 46 | [COMPAT-CACHE-01-001](case/COMPAT-CACHE-01-001.md) | cache 行为等价性——缓存命中场景 | 共 3 个验证点全部真实覆盖 |
| 47 | [COMPAT-CACHE-01-002](case/COMPAT-CACHE-01-002.md) | cache 行为等价性——fork PR 写隔离 | 共 3 个验证点全部真实覆盖 |
| 48 | [COMPAT-CONCUR-01-001](case/COMPAT-CONCUR-01-001.md) | concurrency cancel-in-progress false 时应排队而 | 所有断言均可在流程中验证 |
| 49 | [COMPAT-CONCUR-01-002](case/COMPAT-CONCUR-01-002.md) | concurrency 配置越界或不支持时应给出清晰报错 | 所有断言均可在流程中验证 |
| 50 | [COMPAT-CONCUR-01-003](case/COMPAT-CONCUR-01-003.md) | concurrency preemption enable 行为差异 | 所有断言均可在流程中验证 |
| 51 | [COMPAT-CONCUR-01-004](case/COMPAT-CONCUR-01-004.md) | concurrency preemption events 越界时行为差异 | 所有断言均可在流程中验证 |
| 52 | [COMPAT-CONTAINER-01-001](case/COMPAT-CONTAINER-01-001.md) | container 字段不被支持时应明确报错而非静默忽略 | 所有断言均可在流程中验证 |
| 53 | [COMPAT-CONTAINER-01-002](case/COMPAT-CONTAINER-01-002.md) | container 自定义镜像被拒绝时应给出替代指引 | 所有断言均可在流程中验证 |
| 54 | [COMPAT-CTX-01-001](case/COMPAT-CTX-01-001.md) | 使用 github.ref 上下文应报错或求值为空 | 共 2 个验证点全部真实覆盖 |
| 55 | [COMPAT-CTX-01-002](case/COMPAT-CTX-01-002.md) | 使用 atomgit.ref 上下文应正确返回触发引用 | 共 1 个验证点全部真实覆盖 |
| 56 | [COMPAT-CTX-01-003](case/COMPAT-CTX-01-003.md) | github 上下文嵌套属性访问应报错而非返回空 | 共 2 个验证点全部真实覆盖 |
| 57 | [COMPAT-DEPR-01-001](case/COMPAT-DEPR-01-001.md) | ::set-env:: 废弃命令应被拒绝或给出迁移指引 | 所有断言均可在流程中验证 |
| 58 | [COMPAT-DEPR-01-002](case/COMPAT-DEPR-01-002.md) | ::add-path:: 废弃命令应被拒绝或给出迁移指引 | 所有断言均可在流程中验证 |
| 59 | [COMPAT-DIR-01-002](case/COMPAT-DIR-01-002.md) | 工作流目录差异——.github/workflows/ 不应被识别 | 所有断言均可在流程中验证 |
| 60 | [COMPAT-DIR-01-003](case/COMPAT-DIR-01-003.md) | .github/workflows 目录不应被识别且应给出迁移提示 | 所有断言均可在流程中验证 |
| 61 | [COMPAT-ENV-01-001](case/COMPAT-ENV-01-001.md) | ATOMGIT_SHA 环境变量应正确返回触发提交 SHA | 共 1 个验证点全部真实覆盖 |
| 62 | [COMPAT-ENV-01-002](case/COMPAT-ENV-01-002.md) | GITHUB_SHA 环境变量在 GitCode 中应为空或未定义 | 共 2 个验证点全部真实覆盖 |
| 63 | [COMPAT-ENV-01-003](case/COMPAT-ENV-01-003.md) | GITHUB_ENV 环境变量不应被静默映射到 ATOMGIT_ENV | 共 2 个验证点全部真实覆盖 |
| 64 | [COMPAT-ENVIRON-01-002](case/COMPAT-ENVIRON-01-002.md) | environment 字段绑定 secrets 的行为差异 | 所有断言均可在流程中验证 |
| 65 | [COMPAT-EXPR-01-001](case/COMPAT-EXPR-01-001.md) | success 关键字在条件表达式中的可用性 | 共 2 个验证点全部真实覆盖 |
| 66 | [COMPAT-EXPR-01-008](case/COMPAT-EXPR-01-008.md) | toJson 表达式输出格式差异（pretty-print vs compact） | 所有断言均可在流程中验证 |
| 67 | [COMPAT-EXPR-01-009](case/COMPAT-EXPR-01-009.md) | loose equality 跨类型强制求值差异 | 所有断言均可在流程中验证 |
| 68 | [COMPAT-EXPR-01-010](case/COMPAT-EXPR-01-010.md) | loose equality null 与空字符串及零的等价性差异 | 所有断言均可在流程中验证 |
| 69 | [COMPAT-EXPR-01-013](case/COMPAT-EXPR-01-013.md) | success() 带括号与不带括号的兼容性差异 | 所有断言均可在流程中验证 |
| 70 | [COMPAT-EXPR-01-014](case/COMPAT-EXPR-01-014.md) | always() 带括号与不带括号的兼容性差异 | 所有断言均可在流程中验证 |
| 71 | [COMPAT-IF-01-001](case/COMPAT-IF-01-001.md) | step 失败后后续 step 默认跳过行为 | 共 3 个验证点全部真实覆盖 |
| 72 | [COMPAT-IF-01-002](case/COMPAT-IF-01-002.md) | continue-on-error 标记后失败 step 不阻断后续执行 | 共 3 个验证点全部真实覆盖 |
| 73 | [COMPAT-INPUTS-01-002](case/COMPAT-INPUTS-01-002.md) | workflow_dispatch inputs 类型限制 - string 正常通 | 共 2 个验证点全部真实覆盖 |
| 74 | [COMPAT-ISOLATE-01-001](case/COMPAT-ISOLATE-01-001.md) | Runner 环境隔离——跨 job 文件隔离 | 共 3 个验证点全部真实覆盖 |
| 75 | [COMPAT-ISOLATE-01-002](case/COMPAT-ISOLATE-01-002.md) | Runner 环境隔离——跨 job 环境变量隔离 | 共 3 个验证点全部真实覆盖 |
| 76 | [COMPAT-MASK-01-001](case/COMPAT-MASK-01-001.md) | 直接 echo secrets 值应在日志中被脱敏 | 共 2 个验证点全部真实覆盖 |
| 77 | [COMPAT-MASK-01-002](case/COMPAT-MASK-01-002.md) | 通过 env 注入 secret 后输出应在日志中被脱敏 | 共 3 个验证点全部真实覆盖 |
| 78 | [COMPAT-MATRIX-01-003](case/COMPAT-MATRIX-01-003.md) | matrix 三维展开不被支持时的差异 | 共 2 个验证点全部真实覆盖 |
| 79 | [COMPAT-MATRIX-01-004](case/COMPAT-MATRIX-01-004.md) | matrix include 无基础变量不被支持时的差异 | 共 2 个验证点全部真实覆盖 |
| 80 | [COMPAT-MATRIX-01-005](case/COMPAT-MATRIX-01-005.md) | matrix exclude 全排除不被支持时的差异 | 所有断言均可在流程中验证 |
| 81 | [COMPAT-MIGRATE-01-001](case/COMPAT-MIGRATE-01-001.md) | GitHub 风格 permissions 块迁移报错应给出可操作指引 | 所有断言均可在流程中验证 |
| 82 | [COMPAT-MIGRATE-01-002](case/COMPAT-MIGRATE-01-002.md) | GitHub 风格 run-name 语法迁移报错应给出可操作指引 | 所有断言均可在流程中验证 |
| 83 | [COMPAT-OUTCOME-01-001](case/COMPAT-OUTCOME-01-001.md) | continue-on-error false 时 outcome 与 conclu | 所有断言均可在流程中验证 |
| 84 | [COMPAT-OUTCOME-01-002](case/COMPAT-OUTCOME-01-002.md) | continue-on-error true 时 outcome 应为 failur | 所有断言均可在流程中验证 |
| 85 | [COMPAT-OUTCOME-01-003](case/COMPAT-OUTCOME-01-003.md) | outcome 与 conclusion 在 job 条件判断中不应互换语义 | 所有断言均可在流程中验证 |
| 86 | [COMPAT-OUTPUT-01-001](case/COMPAT-OUTPUT-01-001.md) | 跨 Job 引用未声明 output 时返回空值的差异 | 所有断言均可在流程中验证 |
| 87 | [COMPAT-PERM-01-003](case/COMPAT-PERM-01-003.md) | permissions 命名差异——GitHub contents 权限项应报错 | 所有断言均可在流程中验证 |
| 88 | [COMPAT-PERM-01-004](case/COMPAT-PERM-01-004.md) | permissions 命名差异——GitCode repository 权限项正常 | 所有断言均可在流程中验证 |
| 89 | [COMPAT-PERM-01-005](case/COMPAT-PERM-01-005.md) | permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异 | 所有断言均可在流程中验证 |
| 90 | [COMPAT-PR-01-001](case/COMPAT-PR-01-001.md) | pull_request types 命名差异 - GitCode 合法 types | 所有断言均可在流程中验证 |
| 91 | [COMPAT-PR-01-003](case/COMPAT-PR-01-003.md) | PR types 配置后匹配类型不触发与 GitHub 行为差异 | 所有断言均可在流程中验证 |
| 92 | [COMPAT-PR-01-004](case/COMPAT-PR-01-004.md) | PR types 含 merge 时不触发与 GitHub 行为差异 | 所有断言均可在流程中验证 |
| 93 | [COMPAT-PR-01-005](case/COMPAT-PR-01-005.md) | PR paths 过滤不工作时的兼容性差异 | 所有断言均可在流程中验证 |
| 94 | [COMPAT-PR-01-006](case/COMPAT-PR-01-006.md) | PR 目标分支过滤行为差异 | 所有断言均可在流程中验证 |
| 95 | [COMPAT-SCHEDULE-01-001](case/COMPAT-SCHEDULE-01-001.md) | schedule cron 按 UTC 时间触发 | 所有断言均可在流程中验证 |
| 96 | [COMPAT-SCHEDULE-01-003](case/COMPAT-SCHEDULE-01-003.md) | schedule 在非默认分支不触发与 GitHub 差异 | 所有断言均可在流程中验证 |
| 97 | [COMPAT-SECRET-01-005](case/COMPAT-SECRET-01-005.md) | 环境级 secrets 不支持时应明确报错而非降级为项目级 | 所有断言均可在流程中验证 |
| 98 | [COMPAT-SHELL-01-001](case/COMPAT-SHELL-01-001.md) | 默认 shell 隐式行为差异 - 未显式声明时是否为 bash | 所有断言均可在流程中验证 |
| 99 | [COMPAT-SHELL-01-002](case/COMPAT-SHELL-01-002.md) | 默认工作目录隐式行为差异 - 未显式声明时是否为仓库根目录 | 所有断言均可在流程中验证 |
| 100 | [COMPAT-TARGET-01-001](case/COMPAT-TARGET-01-001.md) | pull_request_target 默认 checkout 应为 base 分支 | 所有断言均可在流程中验证 |
| 101 | [COMPAT-TARGET-01-002](case/COMPAT-TARGET-01-002.md) | pull_request_target 在 fork 场景下应保持 secret 隔 | 所有断言均可在流程中验证 |
| 102 | [COMPAT-TARGET-01-003](case/COMPAT-TARGET-01-003.md) | pull_request_target 默认 types 与 GitHub 差异 | 所有断言均可在流程中验证 |
| 103 | [COMPAT-TOKEN-01-001](case/COMPAT-TOKEN-01-001.md) | ATOMGIT_TOKEN 应正确返回有效令牌 | 所有断言均可在流程中验证 |
| 104 | [COMPAT-TOKEN-01-003](case/COMPAT-TOKEN-01-003.md) | GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN | 所有断言均可在流程中验证 |
| 105 | [COMPAT-VARS-01-001](case/COMPAT-VARS-01-001.md) | vars 上下文若支持应正确返回值 | 所有断言均可在流程中验证 |
| 106 | [COMPAT-VARS-01-003](case/COMPAT-VARS-01-003.md) | vars 项目级覆盖组织级的优先级差异 | 所有断言均可在流程中验证 |
| 107 | [COMPAT-VARS-01-004](case/COMPAT-VARS-01-004.md) | vars 与 env 同名时的优先级差异 | 所有断言均可在流程中验证 |
| 108 | [COMPAT-VARS-01-005](case/COMPAT-VARS-01-005.md) | vars 在条件表达式 if 中的可用性差异 | 所有断言均可在流程中验证 |
| 109 | [COMPAT-VARS-01-006](case/COMPAT-VARS-01-006.md) | vars 在 Action 中的可用性差异 | 所有断言均可在流程中验证 |
| 110 | [REL-ART-01-041](case/REL-ART-01-041.md) | 超大 artifact——100 MB artifact 上传后下游 job 应成功 | 所有断言均可在流程中验证 |
| 111 | [REL-ARTCONC-01-063](case/REL-ARTCONC-01-063.md) | 制品并发写一致性——多 job 同时 upload-artifact 同名 arti | 所有断言均可在流程中验证 |
| 112 | [REL-ARTPERF-01-053-V2](case/REL-ARTPERF-01-053-V2.md) | 制品传输性能——1GB artifact 上传下载耗时 | 所有断言均可在流程中验证 |
| 113 | [REL-ARTPERF-01-053](case/REL-ARTPERF-01-053.md) | 制品传输性能——100MB artifact 上传下载耗时 | 所有断言均可在流程中验证 |
| 114 | [REL-CANCEL-01-028](case/REL-CANCEL-01-028.md) | 手动取消 workflow——运行中取消时 always() cleanup ste | 所有断言均可在流程中验证 |
| 115 | [REL-FAULT-01-035](case/REL-FAULT-01-035.md) | 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务 | 所有断言均可在流程中验证 |
| 116 | [REL-LOGPERF-01-051-V2](case/REL-LOGPERF-01-051-V2.md) | 日志加载性能——200MB 日志下载与查看耗时 | 所有断言均可在流程中验证 |
| 117 | [REL-MATRIX-01-039](case/REL-MATRIX-01-039.md) | 大规模 matrix——50 个组合应全部生成并正确调度 | 所有断言均可在流程中验证 |
| 118 | [REL-RETAIN-01-047](case/REL-RETAIN-01-047.md) | artifact 保留期 90 天边界——第 91 天应不可下载 | 所有断言均可在流程中验证 |
| 119 | [REL-STATE-01-058](case/REL-STATE-01-058.md) | Runner 状态机正确性——空闲/运行/离线转换与时序一致性 | 所有断言均可在流程中验证 |
| 120 | [REL-TIMEOUT-01-009](case/REL-TIMEOUT-01-009.md) | 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被 | 所有断言均可在流程中验证 |
| 121 | [SEC-ARTF-01-002](case/SEC-ARTF-01-002.md) | 跨仓库 artifact 下载返回 403 或 404 | 所有断言均可在流程中验证 |
| 122 | [SEC-BASE-01-001](case/SEC-BASE-01-001.md) | pull_request_target 使用 base 分支的 workflow 版 | 所有断言均可在流程中验证 |
| 123 | [SEC-BASE-01-002](case/SEC-BASE-01-002.md) | fork PR 改 workflow 不被 pull_request_target  | 所有断言均可在流程中验证 |
| 124 | [SEC-CACHE-01-002](case/SEC-CACHE-01-002.md) | 主仓 cache restore 对 fork cache miss | 所有断言均可在流程中验证 |
| 125 | [SEC-DEFPERM-01-002](case/SEC-DEFPERM-01-002.md) | job 级覆盖后权限正确收窄 | 所有断言均可在流程中验证 |
| 126 | [SEC-ENV-01-001](case/SEC-ENV-01-001.md) | 环境级 secret 必须经审批后才能被 workflow 访问 | 所有断言均可在流程中验证 |
| 127 | [SEC-ENV-01-002](case/SEC-ENV-01-002.md) | 环境级 secret 审批前 workflow 不可读取 | 所有断言均可在流程中验证 |
| 128 | [SEC-MASK-01-002](case/SEC-MASK-01-002.md) | Secret 值在 step summary 和错误堆栈中必须被脱敏 | 所有断言均可在流程中验证 |
| 129 | [SEC-NAME-01-001](case/SEC-NAME-01-001.md) | Secret/变量名含特殊字符时不可导致意外求值或权限绕过 | 所有断言均可在流程中验证 |
| 130 | [SEC-SIDE-01-001](case/SEC-SIDE-01-001.md) | Secret 不经 output 侧信道绕过脱敏外泄 | 所有断言均可在流程中验证 |
| 131 | [SEC-SIDE-01-002](case/SEC-SIDE-01-002.md) | Secret 不经 artifact 侧信道绕过脱敏外泄 | 所有断言均可在流程中验证 |
| 132 | [SEC-SUPPLY-01-001](case/SEC-SUPPLY-01-001.md) | 第三方 Action 引用应支持完整 commit hash 固定 | 所有断言均可在流程中验证 |
| 133 | [SEC-SUPPLY-01-002](case/SEC-SUPPLY-01-002.md) | commit hash 不匹配时第三方 Action 应被拒绝执行 | 所有断言均可在流程中验证 |
| 134 | [SEC-SUPPLY-01-003](case/SEC-SUPPLY-01-003.md) | 第三方 Action 来源应具备信任边界（typosquatting 限制） | 所有断言均可在流程中验证 |
| 135 | [SEC-WCMD-01-002](case/SEC-WCMD-01-002.md) | 跨运行 artifact 必须被视为不可信数据 | 所有断言均可在流程中验证 |
| 136 | [USE-ACT-01-001](case/USE-ACT-01-001.md) | 使用裸插件名 checkout 时正常拉取官方 Action | 所有断言均可在流程中验证 |
| 137 | [USE-ANNOT-01-001](case/USE-ANNOT-01-001.md) | workflow 命令 ::error:: 与 ::warning:: 在日志中保留 | 所有断言均可在流程中验证 |
| 138 | [USE-CONC-01-001](case/USE-CONC-01-001.md) | concurrency.max 配置 0 或 10 时报错应提示有效范围 1-5 | 所有断言均可在流程中验证 |
| 139 | [USE-CONC-01-002](case/USE-CONC-01-002.md) | concurrency.max 配置 -1 时报错应提示有效范围 | 所有断言均可在流程中验证 |
| 140 | [USE-CTX-01-002](case/USE-CTX-01-002.md) | 使用 github 上下文时报错应提示 atomgit 替代 | 所有断言均可在流程中验证 |
| 141 | [USE-DISP-01-001](case/USE-DISP-01-001.md) | workflow_dispatch 必填参数未提供时应给出明确校验错误 | 所有断言均可在流程中验证 |
| 142 | [USE-ENV-01-001](case/USE-ENV-01-001.md) | 使用 ATOMGIT_SHA 环境变量时正常取值 | 所有断言均可在流程中验证 |
| 143 | [USE-INPT-01-001](case/USE-INPT-01-001.md) | 使用 string 类型 input 时正常通过校验 | 所有断言均可在流程中验证 |
| 144 | [USE-INPT-01-002](case/USE-INPT-01-002.md) | 使用 boolean 类型 input 时报错应提示仅支持 string | 所有断言均可在流程中验证 |
| 145 | [USE-LBL-01-001](case/USE-LBL-01-001.md) | runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表 | 所有断言均可在流程中验证 |
| 146 | [USE-LBL-01-002](case/USE-LBL-01-002.md) | runs-on 标签因容量不足排队时应提示排队状态而非无可用 runner | 所有断言均可在流程中验证 |
| 147 | [USE-NEST-01-001](case/USE-NEST-01-001.md) | workflow_call 嵌套 3 层时报错应明确提示上限为 2 层 | 所有断言均可在流程中验证 |
| 148 | [USE-PERM-01-001](case/USE-PERM-01-001.md) | 使用 GitCode 权限域命名时正常生效 | 所有断言均可在流程中验证 |
| 149 | [USE-RUN-01-001](case/USE-RUN-01-001.md) | 使用三段式标签时 job 正常调度 | 所有断言均可在流程中验证 |
| 150 | [USE-RUN-01-002](case/USE-RUN-01-002.md) | 使用单标签 ubuntu-latest 时报错应给出三段式格式指引 | 所有断言均可在流程中验证 |
| 151 | [USE-SEARCH-01-001](case/USE-SEARCH-01-001.md) | 日志搜索与下载功能可用且交互流畅 | 所有断言均可在流程中验证 |
| 152 | [USE-SECNAME-01-001](case/USE-SECNAME-01-001.md) | Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误 | 所有断言均可在流程中验证 |
| 153 | [USE-SECNAME-01-002](case/USE-SECNAME-01-002.md) | Secret 名称以数字开头时应给出命名规则错误 | 所有断言均可在流程中验证 |
| 154 | [USE-STAT-01-001](case/USE-STAT-01-001.md) | 使用 always() 带括号时若被接受则正常执行 | 所有断言均可在流程中验证 |
| 155 | [USE-STAT-01-002](case/USE-STAT-01-002.md) | 使用 success() 带括号时报错应提示 GitCode 括号差异 | 所有断言均可在流程中验证 |

## 部分不符 — 验证点与步骤产出部分不一致（176 例）

| # | Case ID | 标题 | 原因 |
|---|---------|------|------|
| 1 | [COMP-ATOMGIT-01-047](case/COMP-ATOMGIT-01-047.md) | atomgit 核心上下文属性可访问性 | 2 TRIVIAL（仅 echo 未执行功能） |
| 2 | [COMP-ATOMGIT-01-048](case/COMP-ATOMGIT-01-048.md) | atomgit 事件相关属性可访问性 | 2 TRIVIAL（仅 echo 未执行功能） |
| 3 | [COMP-ATOMGIT-01-049](case/COMP-ATOMGIT-01-049.md) | atomgit 边界格式校验 | 1 TRIVIAL（仅 echo 未执行功能） |
| 4 | [COMP-BOUND-01-084](case/COMP-BOUND-01-084.md) | 路径与分支过滤组合及否定模式边界验证 | 唯一步骤 `echo "filter_boundary_ok"` 为纯字面量输出，无任何条件判断、表达式求值或实质逻辑，属于 trivial |
| 5 | [COMP-BOUND-01-086](case/COMP-BOUND-01-086.md) | 矩阵构建 include exclude 与单值边界验证 | exclude 排除验证不可达：需要统计 job 实例数量证明 version=2 未执行，但当前无此类断言 |
| 6 | [COMP-BOUND-01-087](case/COMP-BOUND-01-087.md) | 步骤输出与跨 job 传递边界验证 | 跨 job 未声明 outputs 时引用为空：该负向验证点需要第二个 job 尝试引用 writer 的 outputs，当前仅在同 jo |
| 7 | [COMP-BOUND-01-088](case/COMP-BOUND-01-088.md) | 工作流命令 set-env add-path 与文件写入边界验证 | 1 TRIVIAL（仅 echo 未执行功能） |
| 8 | [COMP-CALL-01-001](case/COMP-CALL-01-001.md) | 2 层 workflow_call 嵌套正常执行 | 1 TRIVIAL（仅 echo 未执行功能） |
| 9 | [COMP-CTX-01-052](case/COMP-CTX-01-052.md) | 上下文在条件表达式 if 中注入验证 | 1 TRIVIAL（仅 echo 未执行功能） |
| 10 | [COMP-ENVCTX-01-050](case/COMP-ENVCTX-01-050.md) | env 优先级链 step 大于 job 大于 workflow | 1 TRIVIAL（仅 echo 未执行功能） |
| 11 | [COMP-EXPR-01-054](case/COMP-EXPR-01-054.md) | 字符串函数 contains startsWith endsWith 边界行 | 大小写不匹配返回假：需额外步骤测试大小写差异场景（如 contains(ref_name, 'MAIN')），当前无此测试 |
| 12 | [COMP-EXPR-01-055](case/COMP-EXPR-01-055.md) | hashFiles 函数边界行为 | 3 TRIVIAL（仅 echo 未执行功能） |
| 13 | [COMP-EXPR-01-056](case/COMP-EXPR-01-056.md) | toJson 函数边界行为 | 1 TRIVIAL（仅 echo 未执行功能） |
| 14 | [COMP-EXPR-01-058](case/COMP-EXPR-01-058.md) | 表达式运算符与优先级边界行为 | 1 TRIVIAL（仅 echo 未执行功能） |
| 15 | [COMP-ISOLATION-01-001](case/COMP-ISOLATION-01-001.md) | 同一 workflow 先后 job 的文件系统相互隔离 | 1 TRIVIAL（仅 echo 未执行功能） |
| 16 | [COMP-JOB-01-066](case/COMP-JOB-01-066.md) | job 必填字段 name runs-on steps 验证 | 负向验证点全部缺失：仅验证合法 job 通过，未创建缺 name/steps 的 workflow 变体测试拒绝行为 |
| 17 | [COMP-PUSH-01-001](case/COMP-PUSH-01-001.md) | 匹配 branches 的 push 正确触发 workflow | [正向] 运行记录存在且 event 为 push: PARTIAL - all steps are trivial echo |
| 18 | [COMP-PUSH-01-003](case/COMP-PUSH-01-003.md) | paths 过滤匹配前 300 个变更文件行为符合预期 | 验证点 `运行列表中不存在该 push 触发的运行` → 空洞: no real logic, negative assertion may |
| 19 | [COMP-RERUN-01-002](case/COMP-RERUN-01-002.md) | 第 4 次 rerun 应被系统拒绝 | [非功能] 报错信息应说明最多 3 次限制: PARTIAL - all steps are trivial echo |
| 20 | [COMP-RERUN-01-003](case/COMP-RERUN-01-003.md) | 超过 6 小时的运行不可 rerun | 验证点 `超 6h 的运行的 rerun 不应成功` → 空洞: no real logic, negative assertion may |
| 21 | [COMP-STAGES-01-003](case/COMP-STAGES-01-003.md) | post.run_always true 时 workflow 失败仍执行  | 断言 `[positive] post_logs` → VACUOUS: step Post cleanup only echoes 'po |
| 22 | [COMP-STATUS-01-001](case/COMP-STATUS-01-001.md) | 运行状态机 queued 到 completed 转换正确 | [正向] 状态转换序列符合预期: PARTIAL - all steps are trivial echo |
| 23 | [COMP-STEP-01-071](case/COMP-STEP-01-071.md) | step 执行控制 shell working-directory cont | [正向] shell bash 和 sh 均可执行: PARTIAL - all steps are trivial echo |
| 24 | [COMP-TIMEOUT-01-001](case/COMP-TIMEOUT-01-001.md) | 未声明 timeout-minutes 的 job 在 360 分钟内正常完 | [正向] 运行状态为 success: PARTIAL - all steps are trivial echo |
| 25 | [COMP-TRIG-01-078](case/COMP-TRIG-01-078.md) | 多事件组合与分支路径过滤验证 | [正向] 多事件组合通过校验: PARTIAL - all steps are trivial echo |
| 26 | [COMP-TRIG-01-079](case/COMP-TRIG-01-079.md) | 触发事件 types 取值与过滤边界验证 | [正向] 合法 types 通过校验: PARTIAL - all steps are trivial echo |
| 27 | [COMP-UNKNOWN-01-001](case/COMP-UNKNOWN-01-001.md) | 包含未知顶层字段的 workflow 触发 YAML 校验失败 | [正向] workflow 提交后触发校验失败: PARTIAL - all steps are trivial echo |
| 28 | [COMP-WFLOW-01-061](case/COMP-WFLOW-01-061.md) | workflow name 与 on 字段必填与类型验证 | [正向] 含 name 的 workflow 被正确显示: PARTIAL - all steps are trivial echo |
| 29 | [COMP-WFLOW-01-062](case/COMP-WFLOW-01-062.md) | workflow env 与 defaults 字段验证 | [正向] workflow env 在 step 中可访问: PARTIAL - all steps are trivial echo |
| 30 | [COMP-WFLOW-01-063](case/COMP-WFLOW-01-063.md) | workflow concurrency 并发控制字段验证 | [正向] 合法 concurrency 配置通过校验: PARTIAL - all steps are trivial echo |
| 31 | [COMP-WFLOW-01-064](case/COMP-WFLOW-01-064.md) | workflow stages 阶段结构字段验证 | [正向] stages map 格式通过校验: NOT_COVERED - no steps found |
| 32 | [COMP-WFLOW-01-065](case/COMP-WFLOW-01-065.md) | workflow post 后处理阶段字段验证 | [正向] post 步骤在成功时执行: PARTIAL - all steps are trivial echo |
| 33 | [COMPAT-DIR-01-001](case/COMPAT-DIR-01-001.md) | 工作流目录差异——.gitcode/workflows/ 正常识别 | 验证点 `不应出现 .gitcode 目录下文件被忽略的情况` → 未覆盖: 缺少负向断言 |
| 34 | [COMPAT-ENVIRON-01-001](case/COMPAT-ENVIRON-01-001.md) | 含 environment 字段的 job 应被报错或警告 | 验证点 `不应被静默接受` → 未覆盖: 缺少负向断言 |
| 35 | [COMPAT-EXPR-01-002](case/COMPAT-EXPR-01-002.md) | success() 函数的处理行为差异 | [负向] 若不支持，应有表达式解析错误或降级行为: UNVERIFIABLE - single dispatch cannot prove  |
| 36 | [COMPAT-EXPR-01-003](case/COMPAT-EXPR-01-003.md) | failure() 与 failed 关键字的处理行为差异 | [负向] 若不支持，应有表达式解析错误或降级行为: UNVERIFIABLE - single dispatch cannot prove  |
| 37 | [COMPAT-EXPR-01-004](case/COMPAT-EXPR-01-004.md) | contains 表达式大小写敏感边界 | [负向] 结果不应与预期语义矛盾: UNVERIFIABLE - single dispatch cannot prove negation |
| 38 | [COMPAT-EXPR-01-005](case/COMPAT-EXPR-01-005.md) | contains 表达式空值与空字符串边界 | [负向] 空值场景不应导致表达式解析崩溃: UNVERIFIABLE - single dispatch cannot prove nega |
| 39 | [COMPAT-EXPR-01-006](case/COMPAT-EXPR-01-006.md) | hashFiles 表达式无匹配路径边界 | [负向] 无匹配时不应抛出异常导致 step 失败: UNVERIFIABLE - single dispatch cannot prove |
| 40 | [COMPAT-EXPR-01-007](case/COMPAT-EXPR-01-007.md) | hashFiles 表达式多路径组合边界 | [负向] 多路径组合不应导致解析错误或异常: UNVERIFIABLE - single dispatch cannot prove neg |
| 41 | [COMPAT-EXPR-01-011](case/COMPAT-EXPR-01-011.md) | join() 函数缺失时的降级行为 | 验证点 `错误信息应足够清晰，帮助迁移者识别函数缺失` → 未覆盖: 缺少正向断言 |
| 42 | [COMPAT-EXPR-01-012](case/COMPAT-EXPR-01-012.md) | fromJSON() 函数缺失时的降级行为 | 验证点 `错误信息应足够清晰，帮助迁移者识别函数缺失` → 未覆盖: 缺少正向断言 |
| 43 | [COMPAT-FIELD-01-001](case/COMPAT-FIELD-01-001.md) | 含 run-name 字段的 workflow 应被报错或警告 | [负向] 不应被静默接受: UNVERIFIABLE - single dispatch cannot prove negation |
| 44 | [COMPAT-FIELD-01-002](case/COMPAT-FIELD-01-002.md) | 含 services 字段的 job 应被报错或警告 | [负向] 不应被静默接受: UNVERIFIABLE - single dispatch cannot prove negation |
| 45 | [COMPAT-FIELD-01-003](case/COMPAT-FIELD-01-003.md) | 未知顶层字段不应被静默忽略而应给出警告 | [正向] 系统给出警告或错误，提示未知字段: PARTIAL - all steps are trivial echo |
| 46 | [COMPAT-INPUTS-01-001](case/COMPAT-INPUTS-01-001.md) | workflow_dispatch inputs 类型限制 - boolea | [正向] 错误信息应明确指出仅支持 string 类型: PARTIAL - all steps are trivial echo |
| 47 | [COMPAT-NEST-01-002](case/COMPAT-NEST-01-002.md) | workflow_call 嵌套层数 - 3 层越界应报错 | [正向] 错误信息应明确指出嵌套层数限制: no steps in workflow |
| 48 | [COMPAT-PATHS-01-001](case/COMPAT-PATHS-01-001.md) | paths 过滤器 300 条边界测试 | [正向] workflow 校验通过: assertions present but all steps trivial |
| 49 | [COMPAT-PATHS-01-002](case/COMPAT-PATHS-01-002.md) | paths 过滤器 301 条越界测试 | [正向] 错误信息应明确指出 paths 数量限制: no real steps, no assertions |
| 50 | [COMPAT-PERM-01-001](case/COMPAT-PERM-01-001.md) | 未声明 permissions 时默认 TOKEN 读操作权限范围 | [负向] 读操作不应因权限不足而失败: single dispatch cannot prove negative |
| 51 | [COMPAT-PERM-01-002](case/COMPAT-PERM-01-002.md) | 未声明 permissions 时 fork PR 写操作隔离 | [正向] fork 身份无法获得写权限: 1 real steps but no assertions |
| 52 | [COMPAT-PR-01-002](case/COMPAT-PR-01-002.md) | pull_request types 命名差异 - GitHub 风格 ty | [正向] 错误信息应明确指出类型名称不兼容并给出正确写法: 1 real steps but no assertions |
| 53 | [COMPAT-RUNNER-01-001](case/COMPAT-RUNNER-01-001.md) | runner.os 在 Linux Runner 上应返回 Linux | [负向] 不应返回小写的 linux: single dispatch cannot prove negative |
| 54 | [COMPAT-RUNNER-01-002](case/COMPAT-RUNNER-01-002.md) | runner.arch 在 x86_64 Runner 上应返回 X64 | [负向] 不应返回 x86_64: single dispatch cannot prove negative |
| 55 | [COMPAT-RUNNER-01-003](case/COMPAT-RUNNER-01-003.md) | self-hosted 标签不被支持时应明确报错 | [正向] 系统对不支持的 self-hosted 标签给出明确报错: assertions present but all steps tr |
| 56 | [COMPAT-RUNNER-01-004](case/COMPAT-RUNNER-01-004.md) | 自定义特征标签不被支持时应给出可用标签列表 | [正向] 报错信息说明标签不匹配: assertions present but all steps trivial |
| 57 | [COMPAT-RUNNER-01-005](case/COMPAT-RUNNER-01-005.md) | 内网环境 Runner 不支持时的差异 | [正向] 系统对内网标签给出明确报错: assertions present but all steps trivial |
| 58 | [COMPAT-RUNNER-01-006](case/COMPAT-RUNNER-01-006.md) | Runner 未预装 Java 工具链与 GitHub 差异 | [正向] 系统对缺失的 Java 工具链给出明确提示: assertions present but all steps trivial |
| 59 | [COMPAT-RUNSON-01-001](case/COMPAT-RUNSON-01-001.md) | runs-on 标签体系——三段式数组正常匹配 | [正向] 工作流成功启动并执行: assertions present but all steps trivial |
| 60 | [COMPAT-RUNSON-01-002](case/COMPAT-RUNSON-01-002.md) | runs-on 标签体系——单标签字符串应报错 | [正向] 错误信息应明确说明需使用数组格式: assertions present but all steps trivial |
| 61 | [COMPAT-SCHEDULE-01-002](case/COMPAT-SCHEDULE-01-002.md) | schedule 不支持 timezone 字段差异 | [正向] 错误信息应明确指出 timezone 字段不支持或文档说明忽略策略: no real steps, no assertions |
| 62 | [COMPAT-SHELL-01-003](case/COMPAT-SHELL-01-003.md) | Windows runner 默认 shell 差异 | [正向] 默认 shell 正确执行 Windows 命令: assertions present but all steps trivia |
| 63 | [COMPAT-TOKEN-01-002](case/COMPAT-TOKEN-01-002.md) | GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射 | [非功能] 报错信息应提示使用 ATOMGIT_TOKEN 替代: 1 real steps but no assertions |
| 64 | [COMPAT-VARS-01-002](case/COMPAT-VARS-01-002.md) | vars 上下文若不支持应报错而非静默为空 | [非功能] 报错信息应说明 vars 上下文不支持: 1 real steps but no assertions |
| 65 | [COMPAT-WCMD-01-001](case/COMPAT-WCMD-01-001.md) | ::add-mask:: 不被支持时应静默降级而非报错 | [正向] workflow 不因 add-mask 命令而失败: assertions present but all steps triv |
| 66 | [COMPAT-WCMD-01-002](case/COMPAT-WCMD-01-002.md) | ::group:: 不被支持时应静默降级而非报错 | [正向] workflow 不因 group 命令而失败: assertions present but all steps trivial |
| 67 | [COMPAT-WCMD-01-003](case/COMPAT-WCMD-01-003.md) | ::stop-commands:: 不被支持时应静默降级而非报错 | [正向] workflow 不因 stop-commands 而失败: assertions present but all steps t |
| 68 | [REL-API-01-065](case/REL-API-01-065.md) | API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据 | [正向] 200 占比=100%: assertions present but all steps trivial |
| 69 | [REL-BIGRUNNER-01-066](case/REL-BIGRUNNER-01-066.md) | 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率 | [正向] 成功率≥90%: assertions present but all steps trivial |
| 70 | [REL-CACHE-01-046](case/REL-CACHE-01-046.md) | 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰 | [负向] 不应所有 10 个 key 同时命中: single dispatch cannot prove negative |
| 71 | [REL-CACHEPERF-01-054](case/REL-CACHEPERF-01-054.md) | 缓存加速比——cache 命中 vs 未命中构建耗时对比 | [正向] 加速比≥2x: 2 real steps but no assertions |
| 72 | [REL-CANCELREL-01-061](case/REL-CANCELREL-01-061.md) | 取消操作可靠性——queued/running/post 各阶段取消状态正确 | [负向] queued 取消后不应错标 success/failure: single dispatch cannot prove nega |
| 73 | [REL-CHILDSTATE-01-064-V2](case/REL-CHILDSTATE-01-064-V2.md) | 子任务状态传播——workflow_call 未拉起时父 workflow  | [正向] 父 workflow 状态=failure: assertions present but all steps trivial |
| 74 | [REL-CHILDSTATE-01-064](case/REL-CHILDSTATE-01-064.md) | 子任务状态传播——workflow_call 失败时父 workflow 不 | [正向] 父 workflow 状态=failure: assertions present but all steps trivial |
| 75 | [REL-CONC-01-001](case/REL-CONC-01-001.md) | concurrency.max=5 时同时触发 5 个运行应全部进入执行态 | [正向] 5 个运行状态均为 completed(success): assertions present but all steps tr |
| 76 | [REL-CONC-01-002](case/REL-CONC-01-002.md) | concurrency.max=6 配置应被系统拒绝 | [正向] YAML 校验失败或保存被拒: assertions present but all steps trivial |
| 77 | [REL-CONTINUE-01-030](case/REL-CONTINUE-01-030.md) | continue-on-error=true——job 失败后 workfl | [正向] job_a 状态=failure: assertions present but all steps trivial |
| 78 | [REL-CPU-01-022](case/REL-CPU-01-022.md) | Runner CPU 饱和——small runner 运行 4 个 CPU | [正向] job 状态=success: assertions present but all steps trivial |
| 79 | [REL-DISK-01-018](case/REL-DISK-01-018.md) | Runner 磁盘边界——small runner 写入 49 GB 应成功 | [正向] job 状态=success: assertions present but all steps trivial |
| 80 | [REL-DISK-01-019](case/REL-DISK-01-019.md) | Runner 磁盘越界——small runner 写入 51 GB 应失败 | [正向] job 状态=failure: assertions present but all steps trivial |
| 81 | [REL-FAULT-01-031](case/REL-FAULT-01-031.md) | 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失 | [正向] job 状态=failure: assertions present but all steps trivial |
| 82 | [REL-FAULT-01-032](case/REL-FAULT-01-032.md) | 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误 | [负向] 不应无限挂起超过 120 秒: single dispatch cannot prove negative |
| 83 | [REL-FAULT-01-033](case/REL-FAULT-01-033.md) | 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满 | [正向] job 状态=failure: assertions present but all steps trivial |
| 84 | [REL-FAULT-01-034](case/REL-FAULT-01-034.md) | 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cac | [负向] job 不应因 cache 服务不可用而整体 failure: single dispatch cannot prove nega |
| 85 | [REL-FLOOD-01-036](case/REL-FLOOD-01-036.md) | 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflo | [正向] 10 个运行均被创建: assertions present but all steps trivial |
| 86 | [REL-FLOOD-01-037](case/REL-FLOOD-01-037.md) | 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃 | [正向] 50 个运行均被创建: assertions present but all steps trivial |
| 87 | [REL-IGNORE-01-004](case/REL-IGNORE-01-004.md) | concurrency IGNORE 策略——超上限运行应直接执行 | [正向] 4 个运行全部 completed(success): assertions present but all steps triv |
| 88 | [REL-IMAGE-01-052-V2](case/REL-IMAGE-01-052-V2.md) | 镜像拉取性能——5GB 自定义 container 环境准备耗时基准 | [负向] 不应 pending 后无解释失败: single dispatch cannot prove negative |
| 89 | [REL-IMAGE-01-052](case/REL-IMAGE-01-052.md) | 镜像拉取性能——500MB 自定义 container 环境准备耗时基准 | [负向] 不应 pending 10min 后无解释失败: single dispatch cannot prove negative |
| 90 | [REL-K8S-01-045](case/REL-K8S-01-045.md) | 自托管 K8s Runner 弹性伸缩——min=1/max=1 时并发 3 | [正向] Pod 数=1: assertions present but all steps trivial |
| 91 | [REL-LATENCY-01-050-V2](case/REL-LATENCY-01-050-V2.md) | 调度延迟压力——并发 20 个 job 的排队延迟与完成率 | [正向] 20 个 job 全部完成: assertions present but all steps trivial |
| 92 | [REL-LOG-01-040](case/REL-LOG-01-040.md) | 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看 | [负向] 不应截断或乱序: single dispatch cannot prove negative |
| 93 | [REL-LOGPERF-01-051](case/REL-LOGPERF-01-051.md) | 日志加载性能——50MB 日志下载与查看耗时 | [负向] 不应 UI 卡死: single dispatch cannot prove negative |
| 94 | [REL-LOGSTABLE-01-059](case/REL-LOGSTABLE-01-059.md) | 日志系统稳定性——6 万行日志无乱序/无丢失/无截断 | [负向] 不应出现行号跳变或乱序: single dispatch cannot prove negative |
| 95 | [REL-LONG-01-043](case/REL-LONG-01-043.md) | 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常 | [负向] 不应在 350 分钟前被终止: single dispatch cannot prove negative |
| 96 | [REL-MATRIX-01-026](case/REL-MATRIX-01-026.md) | matrix fail-fast=true——任意 job 实例失败应立即取 | [负向] 不应继续执行已失败的 matrix 其余实例: single dispatch cannot prove negative |
| 97 | [REL-MATRIX-01-027](case/REL-MATRIX-01-027.md) | matrix max-parallel=4——9 个组合应最多同时运行 4  | [负向] 不应超过 4 个同时运行: single dispatch cannot prove negative |
| 98 | [REL-MATRIX-01-038](case/REL-MATRIX-01-038.md) | 大规模 matrix——20 个组合应全部生成并正确调度 | [负向] 不应出现重复组合或遗漏组合: single dispatch cannot prove negative |
| 99 | [REL-MATRIXFAIR-01-056](case/REL-MATRIXFAIR-01-056.md) | 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 | [负向] 无实例被无限饿死: single dispatch cannot prove negative |
| 100 | [REL-MEM-01-020](case/REL-MEM-01-020.md) | Runner 内存边界——small runner 分配 7.5 GB 应成 | [正向] job 状态=success: assertions present but all steps trivial |
| 101 | [REL-MEM-01-021](case/REL-MEM-01-021.md) | Runner 内存越界——small runner 分配 9 GB 应被 O | [正向] job 状态=failure: assertions present but all steps trivial |
| 102 | [REL-NEEDS-01-025](case/REL-NEEDS-01-025.md) | needs 失败传播——上游 job 失败时下游 job 应被 skip | [正向] job_a 状态=failure: assertions present but all steps trivial |
| 103 | [REL-NETFAULT-01-062](case/REL-NETFAULT-01-062.md) | 网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时 | [负向] 不可达地址不应 hang>60s: single dispatch cannot prove negative |
| 104 | [REL-OUTPUT-01-016](case/REL-OUTPUT-01-016.md) | step output 边界值——ATOMGIT_OUTPUT 写入 1 M | [负向] 不应截断或丢失: single dispatch cannot prove negative |
| 105 | [REL-OUTPUT-01-017](case/REL-OUTPUT-01-017.md) | step output 越界值——ATOMGIT_OUTPUT 写入 1 M | [负向] 不应静默截断且无提示: single dispatch cannot prove negative |
| 106 | [REL-PATHS-01-014](case/REL-PATHS-01-014.md) | paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效 | [正向] workflow 运行被创建: assertions present but all steps trivial |
| 107 | [REL-PATHS-01-015](case/REL-PATHS-01-015.md) | paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断 | [正向] workflow 不触发: assertions present but all steps trivial |
| 108 | [REL-PREEMPT-01-005](case/REL-PREEMPT-01-005.md) | preemption events 边界值——配置 10 个应正常解析 | [正向] workflow 保存成功并运行 completed(success): assertions present but all s |
| 109 | [REL-PREEMPT-01-006](case/REL-PREEMPT-01-006.md) | preemption events 越界值——配置 11 个应被拒绝 | [正向] 明确报错: assertions present but all steps trivial |
| 110 | [REL-PRESSURE-01-055](case/REL-PRESSURE-01-055.md) | 并发压测——concurrency.max=5 时触发 20 个 workf | [正向] completed=20: assertions present but all steps trivial |
| 111 | [REL-PROJLIMIT-01-067](case/REL-PROJLIMIT-01-067.md) | 项目级 workflow 并发上限——200 条同时触发时全部完成无丢失 | [负向] 不应出现触发后无对应 run 记录（丢失）: single dispatch cannot prove negative |
| 112 | [REL-PROJLIMIT-01-068](case/REL-PROJLIMIT-01-068.md) | 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排 | [负向] 不应出现触发后无对应 run 记录（丢失）: single dispatch cannot prove negative |
| 113 | [REL-QUEUE-01-003](case/REL-QUEUE-01-003.md) | concurrency QUEUE 策略——超上限运行应排队等待 | [正向] 4 个运行最终全部 completed(success): assertions present but all steps tr |
| 114 | [REL-RACE-01-048](case/REL-RACE-01-048.md) | 取消与 needs 条件竞态——job A 被取消时 job B(if: f | [正向] job A 状态=cancelled: assertions present but all steps trivial |
| 115 | [REL-RERUN-01-011](case/REL-RERUN-01-011.md) | rerun 边界值——单条运行连续重新运行 3 次应全部成功 | [正向] 运行编号递增: assertions present but all steps trivial |
| 116 | [REL-RERUN-01-012](case/REL-RERUN-01-012.md) | rerun 越界值——尝试第 4 次重新运行应被系统拒绝 | [正向] 第 4 次 rerun 按钮不可用或点击后报错: assertions present but all steps trivial |
| 117 | [REL-RERUN-01-013](case/REL-RERUN-01-013.md) | rerun 6 小时年龄限制——超期运行不可重新运行 | 验证点 `不应创建新运行` → 未覆盖: 缺少负向断言 |
| 118 | [REL-RUNNER-01-049-V2](case/REL-RUNNER-01-049-V2.md) | Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存 | 验证点 `不应因架构不匹配而随机失败` → 未覆盖: 缺少负向断言 |
| 119 | [REL-RUNNER-01-049](case/REL-RUNNER-01-049.md) | Runner 规格真实性——small/medium/large 实际 CP | 验证点 `实际资源不应显著低于声明` → 未覆盖: 缺少负向断言 |
| 120 | [REL-SCHED-01-057](case/REL-SCHED-01-057.md) | 资源调度状态一致性——空闲 runner 存在时 job 不应死等 | 验证点 `10 次全部≤60s` → 未覆盖: 缺少正向断言 |
| 121 | [REL-STAGES-01-029](case/REL-STAGES-01-029.md) | stages fail_fast 机制——阶段内任一 job 失败应立即终止 | 验证点 `不应进入下一阶段` → 未覆盖: 缺少负向断言 |
| 122 | [REL-STEPS-01-042](case/REL-STEPS-01-042.md) | 超多 step——单 job 内 50 个 step 应全部串行执行无丢失 | 验证点 `50 个 step 全部出现在运行详情页` → 空洞: steps only echo literal strings |
| 123 | [REL-TIMEOUT-01-007](case/REL-TIMEOUT-01-007.md) | job timeout 边界值——359 分钟运行应在 360 分钟边界前完 | 验证点 `不应在 358 分钟前被强制终止` → 未覆盖: 缺少负向断言 |
| 124 | [REL-TIMEOUT-01-008](case/REL-TIMEOUT-01-008.md) | job timeout 越界触发——361 分钟应在 360 分钟被强制终止 | 验证点 `不应运行超过 365 分钟` → 未覆盖: 缺少负向断言 |
| 125 | [REL-TIMEOUT-01-010](case/REL-TIMEOUT-01-010.md) | 默认超时——未声明 timeout-minutes 运行 361 分钟应被强 | 验证点 `不应无限运行` → 未覆盖: 缺少负向断言 |
| 126 | [SEC-DEFPERM-01-001](case/SEC-DEFPERM-01-001.md) | ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效 | 验证点 `权限范围与覆盖关系可被观测判定` → 未覆盖: 缺少非功能断言 |
| 127 | [SEC-DOS-01-001](case/SEC-DOS-01-001.md) | 大 artifact / 大 cache 必须受配额与边界限制 | 验证点 `超限时应给出明确报错（大小限制值），不应静默截断或卡死` → 未覆盖: 缺少非功能断言 |
| 128 | [SEC-FORK-01-001](case/SEC-FORK-01-001.md) | fork PR 触发 pull_request 时不可读取项目 secret | **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request 无法通过 dispatch API 调度 |
| 129 | [SEC-FORK-01-002](case/SEC-FORK-01-002.md) | fork PR 中 secrets 引用返回空值且 job 不崩溃 | **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request 无法通过 dispatch API 调度 |
| 130 | [SEC-INJ-01-001](case/SEC-INJ-01-001.md) | 不可信 PR 标题不可直接插进 run 脚本导致命令注入 | **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request 无法通过 dispatch API 调度 |
| 131 | [SEC-INJ-01-002](case/SEC-INJ-01-002.md) | 不可信分支名不可直接插进 run 脚本导致命令注入 | **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request 无法通过 dispatch API 调度 |
| 132 | [SEC-INJ-01-003](case/SEC-INJ-01-003.md) | 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入 | **断言 1 - TRIGGER_BLOCKED**: 触发事件 issue_comment 无法通过 dispatch API 调度 |
| 133 | [SEC-INJ-01-004](case/SEC-INJ-01-004.md) | 不可信 commit message 不可直接插进 run 脚本导致命令注入 | **断言 1 - TRIGGER_BLOCKED**: 触发身份为 untrusted_contributor，无法调度 |
| 134 | [SEC-INJ-01-005](case/SEC-INJ-01-005.md) | 表达式求值必须防止双重模板渲染（二次求值） | **断言 1 - MISSING_SOURCE**: 期望值 [2] 未在任何步骤输出中找到 |
| 135 | [SEC-MASK-01-001](case/SEC-MASK-01-001.md) | Secret 值在运行日志中必须被自动脱敏为 *** | **断言 2 - MISSING_SOURCE**: 期望值 [masked_with_asterisks] 未在任何步骤输出中找到 |
| 136 | [SEC-MASK-01-003](case/SEC-MASK-01-003.md) | Secret 日志脱敏不可通过 base64 编码绕过 | **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 日志中 base64 编码后的字符串与 sec |
| 137 | [SEC-MASK-01-004](case/SEC-MASK-01-004.md) | Secret 日志脱敏不可通过字符串拼接或插值绕过 | **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 日志全文搜索 secret 的任意连续子串（长 |
| 138 | [SEC-MASK-01-005](case/SEC-MASK-01-005.md) | Secret 日志脱敏不可通过多行值输出绕过 | **断言 2 - MISSING_SOURCE**: 期望值 [multiline_masked_with_asterisks] 未在任何步 |
| 139 | [SEC-MASK-01-006](case/SEC-MASK-01-006.md) | Secret 日志脱敏不可通过分片输出绕过 | **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 日志中 secret 的任意连续子串（如 3  |
| 140 | [SEC-NAME-01-002](case/SEC-NAME-01-002.md) | 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secr | **断言 2 - MISSING_SOURCE**: 期望值 [masked_or_not_found] 未在任何步骤输出中找到 |
| 141 | [SEC-NET-01-001](case/SEC-NET-01-001.md) | Runner 网络出站必须受控，防止 SSRF 与内网跳板 | **断言 1 - MISSING_SOURCE**: 期望值 [metadata_service_response] 未在任何步骤输出中找到 |
| 142 | [SEC-OIDC-01-001](case/SEC-OIDC-01-001.md) | OIDC / 短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案 | 验证点 `不支持 OIDC 时，系统绝不应提供可长期复用的高权限云部署凭证作为默认方案` → 空洞: no real logic, nega |
| 143 | [SEC-PERM-01-001](case/SEC-PERM-01-001.md) | 显式声明的 permissions 必须在 job 级实际生效并限制 ATO | **断言 1 - MISSING_SOURCE**: 期望值 [read_operations_successful] 未在任何步骤输出中找 |
| 144 | [SEC-PERM-01-002](case/SEC-PERM-01-002.md) | permissions 声明 read 时写操作被平台拒绝 | **断言 1 - MISSING_SOURCE**: 期望值 [push_successful] 未在任何步骤输出中找到 |
| 145 | [SEC-PERM-01-003](case/SEC-PERM-01-003.md) | 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须 | **断言 1 - MISSING_SOURCE**: 期望值 [write_permission_granted] 未在任何步骤输出中找到 |
| 146 | [SEC-PERM-01-004](case/SEC-PERM-01-004.md) | 默认状态下写操作被 403 拒绝 | **断言 1 - MISSING_SOURCE**: 期望值 [push_successful] 未在任何步骤输出中找到 |
| 147 | [SEC-PRTGT-01-001](case/SEC-PRTGT-01-001.md) | pull_request_target 下显式 checkout 不可信 P | **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request_target 无法通过 dispatch API |
| 148 | [SEC-PRTGT-01-002](case/SEC-PRTGT-01-002.md) | pull_request_target 无审批不执行 fork PR 代码 | **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request_target 无法通过 dispatch API |
| 149 | [SEC-RUN-01-001](case/SEC-RUN-01-001.md) | Job 结束后 workspace 与临时文件必须被彻底清理 | **断言 2 - MISSING_SOURCE**: 期望值 [cleaned_as_expected] 未在任何步骤输出中找到 |
| 150 | [SEC-RUN-01-002](case/SEC-RUN-01-002.md) | Runner 环境变量与共享目录必须跨 job 隔离 | **断言 2 - MISSING_SOURCE**: 期望值 [isolated_as_expected] 未在任何步骤输出中找到 |
| 151 | [SEC-RUN-01-003](case/SEC-RUN-01-003.md) | 自托管 Runner 跨项目残留必须被隔离 | **断言 2 - MISSING_SOURCE**: 期望值 [isolated_as_expected] 未在任何步骤输出中找到 |
| 152 | [SEC-TOCTOU-01-001](case/SEC-TOCTOU-01-001.md) | 审批后推送新 commit 不应被已授权特权运行执行 | **断言 1 - MISSING_SOURCE**: 期望值 [unapproved_commit_executed] 未在任何步骤输出中找 |
| 153 | [SEC-WCMD-01-001](case/SEC-WCMD-01-001.md) | Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的  | **断言 2 - MISSING_SOURCE**: 期望值 [mask_command_without_payload] 未在任何步骤输出 |
| 154 | [SEC-WCMD-01-003](case/SEC-WCMD-01-003.md) | ATOMGIT_ENV 不被不可信输入污染提权 | **断言 1 - MISSING_SOURCE**: 期望值 [injection succeeded] 未在任何步骤输出中找到 |
| 155 | [SEC-WCMD-01-004](case/SEC-WCMD-01-004.md) | ATOMGIT_OUTPUT 不被不可信输入污染提权 | **断言 1 - MISSING_SOURCE**: 期望值 [hijack succeeded] 未在任何步骤输出中找到 |
| 156 | [USE-ACT-01-002](case/USE-ACT-01-002.md) | 使用 actions/checkout@v4 时报错应给出迁移指引 | **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 报错信息必须同时出现 actions/chec |
| 157 | [USE-BADGE-01-001](case/USE-BADGE-01-001.md) | workflow 运行完成后状态徽标及时回写且语义清晰 | **断言 1 - STATUS_GUARANTEED**: 所有步骤无实质逻辑/条件/action，workflow 永远成功 |
| 158 | [USE-DEPR-01-002](case/USE-DEPR-01-002.md) | 使用 ::set-output 时应给出弃用警告与替代示例 | 验证点 `不应静默生效` → 未覆盖: 缺少负向断言 |
| 159 | [USE-DIR-01-001](case/USE-DIR-01-001.md) | workflow 放置于 .gitcode/workflows/ 下可正常触 | **断言 1 - STATUS_GUARANTEED**: 所有步骤无实质逻辑/条件/action，workflow 永远成功 |
| 160 | [USE-DIR-01-002](case/USE-DIR-01-002.md) | .github/workflows/ 下 workflow 未被识别时应给出 | **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 提示信息必须同时包含 .github/work |
| 161 | [USE-DOC-01-001](case/USE-DOC-01-001.md) | stages 与 post 概念在迁移文档中具备可发现性 | **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 文档中关于 stages/post 的说明必须 |
| 162 | [USE-ENV-01-002](case/USE-ENV-01-002.md) | 引用 GITHUB_SHA 时日志应给出环境变量映射提示 | **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 日志警告是否足够醒目且包含有效指引：应提示 G |
| 163 | [USE-EXPR-01-001](case/USE-EXPR-01-001.md) | 引用不存在的上下文属性时报错应包含原始表达式与错误类型 | **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 报错信息必须包含出错的原始表达式（或截断后的前 |
| 164 | [USE-EXPR-01-002](case/USE-EXPR-01-002.md) | 调用未知函数时报错应提示函数名错误与修正方向 | **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 报错信息必须包含出错的原始表达式（或截断后的前 |
| 165 | [USE-MASK-01-001](case/USE-MASK-01-001.md) | secret 脱敏文档描述与实际行为一致并给出缓解建议 | **断言 1 - UNEXERCISED**: secret TEST_SECRET 从未被任何步骤使用，安全断言无效 |
| 166 | [USE-MASK-01-002](case/USE-MASK-01-002.md) | 直接 echo secrets 值时文档描述的绕过风险与实际一致 | 验证点 `若绕过确实发生，日志中可能出现明文` → 未覆盖: 缺少负向断言 |
| 167 | [USE-MD-01-001](case/USE-MD-01-001.md) | ATOMGIT_STEP_SUMMARY 写入的 Markdown 正确渲染 | **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: Markdown 表格必须有表头样式区分（背景 |
| 168 | [USE-NEST-01-002](case/USE-NEST-01-002.md) | workflow_call 嵌套 2 层时应正常执行 | 验证点 `不应报嵌套超限错误` → 未覆盖: 缺少负向断言 |
| 169 | [USE-PATH-01-001](case/USE-PATH-01-001.md) | paths 300 文件上限在文档与行为中一致且明示 | **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 文档 configure-triggers.m |
| 170 | [USE-PERM-01-002](case/USE-PERM-01-002.md) | 使用 GitHub 权限域命名时报错应给出 GitCode 对照表 | **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 报错信息必须同时出现 contents 等 G |
| 171 | [USE-RES-01-001](case/USE-RES-01-001.md) | runtime-environment-variables.md 中不应出现 | **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 独立出现的 GITHUB_ 前缀（非引用、非对 |
| 172 | [USE-UNKN-01-001](case/USE-UNKN-01-001.md) | 未知字段如 run-name 不应被静默忽略而应给出警告或错误 | **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 对未知字段的提示必须包含字段名和不支持/unk |
| 173 | [USE-UNKN-01-002](case/USE-UNKN-01-002.md) | 未知字段报错若识别为 GitHub 特有应追加迁移提示 | **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 对未知字段的提示必须包含字段名和不支持/unk |
| 174 | [USE-VARS-01-001](case/USE-VARS-01-001.md) | vars 上下文在文档与样本中的声明必须一致 | **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 文档与样本对同一能力 vars 上下文的声明必 |
| 175 | [USE-YAML-01-001](case/USE-YAML-01-001.md) | 缺少必填字段 on 时报错应指出具体字段名与位置 | **断言 1 - UNVERIFIABLE**: [负向] 未找到可能导致非成功状态的步骤，单次调度无法证明 !=success |
| 176 | [USE-YAML-01-002](case/USE-YAML-01-002.md) | YAML 缩进错误时报错应指出具体行号与列号 | **断言 1 - UNVERIFIABLE**: [负向] 未找到可能导致非成功状态的步骤，单次调度无法证明 !=success |

## 完全不符 — 全部验证点未能由步骤产出（38 例）

| # | Case ID | 标题 | 原因 |
|---|---------|------|------|
| 1 | [COMP-BOUND-01-085](case/COMP-BOUND-01-085.md) | cron 表达式格式与位置边界验证 | 触发事件为 schedule，无法在可控的测试环境中即时执行和验证 |
| 2 | [COMP-CACHE-01-003](case/COMP-CACHE-01-003.md) | fork PR 不应覆盖或污染主分支 cache | 触发身份为 untrusted_contributor，需要第二个独立账号 fork 仓库后发起 PR，测试环境无此能力 |
| 3 | [COMP-PERMS-01-003](case/COMP-PERMS-01-003.md) | fork PR 的 pull_request 下声明 write 仍仅 re | [负向] 写操作应失败: BLOCKED - trigger=pull_request |
| 4 | [COMP-PR-01-001](case/COMP-PR-01-001.md) | fork PR 触发 pull_request 时不可读取项目 secret | [负向] 日志不含 DEPLOY_TOKEN 明文: BLOCKED - trigger=pull_request |
| 5 | [COMP-PR-01-002](case/COMP-PR-01-002.md) | pull_request_target 可访问 secrets 且 TOKE | [正向] pull_request_target 可访问 secrets: BLOCKED - trigger=pull_request_t |
| 6 | [COMP-PR-01-003](case/COMP-PR-01-003.md) | fork PR 的 pull_request workflow ATOMGI | [负向] 写操作（如推送、评论）应失败: BLOCKED - trigger=pull_request |
| 7 | [COMP-PRTARGET-01-001](case/COMP-PRTARGET-01-001.md) | pull_request_target 默认使用 base 分支 workf | [正向] 执行的 step 内容与 base 分支 workflow 一致: BLOCKED - trigger=pull_request_ |
| 8 | [COMP-PRTARGET-01-002](case/COMP-PRTARGET-01-002.md) | 显式 checkout head.sha 后执行不可信代码的风险可控 | [正向] checkout head.sha 成功: BLOCKED - trigger=pull_request_target, trig |
| 9 | [COMP-RUNNER-01-003](case/COMP-RUNNER-01-003.md) | 不存在的标签组合导致 job 排队或失败 | 验证点 `job 不应成功执行` → 空洞: no failure path exists, status=success guarante |
| 10 | [COMP-SCHEDULE-01-001](case/COMP-SCHEDULE-01-001.md) | 合法 cron 在默认分支按时触发 | [正向] 运行记录存在且 event 为 schedule: BLOCKED - trigger=schedule |
| 11 | [COMP-SCHEDULE-01-002](case/COMP-SCHEDULE-01-002.md) | 非默认分支的 schedule workflow 不应触发 | [负向] 运行列表中不存在该 schedule 触发的运行: BLOCKED - trigger=schedule |
| 12 | [COMP-SCHEDULE-01-003](case/COMP-SCHEDULE-01-003.md) | cron 间隔短于 5 分钟时被拒绝或降级 | [负向] 不应允许每分钟触发的 schedule: BLOCKED - trigger=schedule |
| 13 | [COMP-STAGES-01-001](case/COMP-STAGES-01-001.md) | stages 阶段间串行、阶段内 job 并行执行 | 验证点 `stage 2 的 job 开始时间晚于 stage 1 所有 job 的结束时间` → 空洞: all steps trivia |
| 14 | [COMP-TRIG-01-073](case/COMP-TRIG-01-073.md) | pull_request 事件关键字段与 types 验证 | [正向] PR 创建时触发 workflow: BLOCKED - trigger=pull_request |
| 15 | [COMP-TRIG-01-075](case/COMP-TRIG-01-075.md) | schedule 事件关键字段与 cron 格式验证 | [正向] 数组格式 schedule 通过校验: BLOCKED - trigger=schedule |
| 16 | [COMP-TRIG-01-076](case/COMP-TRIG-01-076.md) | issue_comment 事件关键字段与 types 验证 | [正向] issue 评论创建时触发: BLOCKED - trigger=issue_comment |
| 17 | [COMPAT-COMM-01-001](case/COMPAT-COMM-01-001.md) | issue_comment types 命名差异 - GitCode 合法  | 触发事件 `issue_comment` 无 dispatch API，无法在自动化框架中验证 |
| 18 | [COMPAT-COMM-01-002](case/COMPAT-COMM-01-002.md) | issue_comment types:created 不支持时应给出降级指 | 触发事件 `issue_comment` 无 dispatch API，无法在自动化框架中验证 |
| 19 | [COMPAT-NEST-01-001](case/COMPAT-NEST-01-001.md) | workflow_call 嵌套层数 - 2 层正常执行 | [正向] 2 层嵌套 workflow 能正常触发并执行: no steps in workflow |
| 20 | [REL-FAIR-01-044](case/REL-FAIR-01-044.md) | 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调 | [正向] 启动时延差≤60 秒: no real steps, no assertions |
| 21 | [REL-LATENCY-01-050](case/REL-LATENCY-01-050.md) | 调度延迟基准——queued→running P50/P95 等待时间 | [正向] P95≤60s: no real steps, no assertions |
| 22 | [REL-NEST-01-023](case/REL-NEST-01-023.md) | workflow_call 嵌套边界——2 层嵌套调用应成功执行 | [正向] 最外层运行状态=success: no steps in workflow |
| 23 | [REL-NEST-01-024](case/REL-NEST-01-024.md) | workflow_call 嵌套越界——3 层嵌套调用应被拒绝 | [正向] 运行状态=failure: no steps in workflow |
| 24 | [REL-YAMLCACHE-01-060](case/REL-YAMLCACHE-01-060.md) | Workflow YAML 缓存失效——修改后无旧代码残留 | 验证点 `日志打印 marker_v2` → 空洞: no step produces 'marker_v2' |
| 25 | [SEC-ARTF-01-001](case/SEC-ARTF-01-001.md) | fork PR 上传的 artifact 必须不可被主仓 workflow  | 触发事件 `pull_request` 无 dispatch API，无法在自动化框架中验证 |
| 26 | [SEC-CACHE-01-001](case/SEC-CACHE-01-001.md) | fork PR 写入的 cache 必须不可被主仓后续 workflow 读 | 触发事件 `pull_request` 无 dispatch API，无法在自动化框架中验证 |
| 27 | [SEC-COMM-01-001](case/SEC-COMM-01-001.md) | issue_comment / pull_request_comment 触 | 触发事件 `issue_comment` 无 dispatch API，无法在自动化框架中验证 |
| 28 | [SEC-TOCTOU-01-002](case/SEC-TOCTOU-01-002.md) | 评论触发不应绕过代码固定与 PR 审批 | 触发事件 `issue_comment` 无 dispatch API，无法在自动化框架中验证 |
| 29 | [SEC-TOKEN-01-001](case/SEC-TOKEN-01-001.md) | fork PR 触发 pull_request 时 ATOMGIT_TOKE | 触发事件 `pull_request` 无 dispatch API，无法在自动化框架中验证 |
| 30 | [SEC-TOKEN-01-002](case/SEC-TOKEN-01-002.md) | fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝 | 触发事件 `pull_request` 无 dispatch API，无法在自动化框架中验证 |
| 31 | [USE-ANNOT-01-002](case/USE-ANNOT-01-002.md) | ::error:: 生成的 PR annotation 具备文件路径、行号与 | 触发事件 `pull_request` 无 dispatch API，无法在自动化框架中验证 |
| 32 | [USE-CTX-01-001](case/USE-CTX-01-001.md) | 使用 atomgit 上下文时表达式正常求值 | 验证点 `日志中输出当前分支引用值` → 空洞: no step produces 'ref=refs/heads/' |
| 33 | [USE-DEPR-01-001](case/USE-DEPR-01-001.md) | 使用 ATOMGIT_OUTPUT 文件协议时正常生效 | 验证点 `下游步骤通过 steps.*.outputs.key 获取到值` → 空洞: no step produces 'val=myva |
| 34 | [USE-DISP-01-002](case/USE-DISP-01-002.md) | workflow_dispatch 未提供参数但存在 default 时应使 | 验证点 `运行成功完成` → 空洞: no step produces 'env=staging' |
| 35 | [USE-LOG-01-001](case/USE-LOG-01-001.md) | 多 step 日志按时间线组织且边界清晰 | 验证点 `日志面板中 step 按定义顺序排列，step 内 shell 输出内容（如 "prepare done"）可在 run_logs |
| 36 | [USE-OS-01-001](case/USE-OS-01-001.md) | runner.os 返回值与文档声明的平台支持一致 | 验证点 `runner.os 返回 Linux` → 空洞: no step produces 'os=Linux' |
| 37 | [USE-TYPE-01-001](case/USE-TYPE-01-001.md) | 使用 GitCode types 命名时正常触发 | 触发事件 `pull_request` 无 dispatch API，无法在自动化框架中验证 |
| 38 | [USE-TYPE-01-002](case/USE-TYPE-01-002.md) | 使用 GitHub types 命名 opened/synchronize  | 触发事件 `pull_request` 无 dispatch API，无法在自动化框架中验证 |

## 规格缺失 — 无 Phase 01 文本用例（50 例）

以下用例缺少对应 Phase 01 文本规格，无法进行规格-实现对照分析：

| # | Case ID | 标题 |
|---|---------|------|
| 1 | [SEC-DOS-01-002](case/SEC-DOS-01-002.md) | 该用例规格文件缺失，无法分析 |
| 2 | [USE-ACTION-01-001](case/USE-ACTION-01-001.md) | 该用例规格文件缺失，无法分析 |
| 3 | [USE-ACTION-01-002](case/USE-ACTION-01-002.md) | 该用例规格文件缺失，无法分析 |
| 4 | [USE-ACTION-01-003](case/USE-ACTION-01-003.md) | 该用例规格文件缺失，无法分析 |
| 5 | [USE-AUDIT-01-001](case/USE-AUDIT-01-001.md) | 该用例规格文件缺失，无法分析 |
| 6 | [USE-CONF-01-001](case/USE-CONF-01-001.md) | 该用例规格文件缺失，无法分析 |
| 7 | [USE-CONF-01-002](case/USE-CONF-01-002.md) | 该用例规格文件缺失，无法分析 |
| 8 | [USE-CONF-01-003](case/USE-CONF-01-003.md) | 该用例规格文件缺失，无法分析 |
| 9 | [USE-CONF-01-004](case/USE-CONF-01-004.md) | 该用例规格文件缺失，无法分析 |
| 10 | [USE-CONF-01-005](case/USE-CONF-01-005.md) | 该用例规格文件缺失，无法分析 |
| 11 | [USE-DEF-01-001](case/USE-DEF-01-001.md) | 该用例规格文件缺失，无法分析 |
| 12 | [USE-DEF-01-002](case/USE-DEF-01-002.md) | 该用例规格文件缺失，无法分析 |
| 13 | [USE-DEF-01-003](case/USE-DEF-01-003.md) | 该用例规格文件缺失，无法分析 |
| 14 | [USE-ERR-01-001](case/USE-ERR-01-001.md) | 该用例规格文件缺失，无法分析 |
| 15 | [USE-ERR-01-002](case/USE-ERR-01-002.md) | 该用例规格文件缺失，无法分析 |
| 16 | [USE-FIELD-01-001](case/USE-FIELD-01-001.md) | 该用例规格文件缺失，无法分析 |
| 17 | [USE-MIGRATE-01-001](case/USE-MIGRATE-01-001.md) | 该用例规格文件缺失，无法分析 |
| 18 | [USE-NAME-01-001](case/USE-NAME-01-001.md) | 该用例规格文件缺失，无法分析 |
| 19 | [USE-NAME-01-002](case/USE-NAME-01-002.md) | 该用例规格文件缺失，无法分析 |
| 20 | [USE-OPTI-01-001](case/USE-OPTI-01-001.md) | 该用例规格文件缺失，无法分析 |
| 21 | [USE-OPTI-01-002](case/USE-OPTI-01-002.md) | 该用例规格文件缺失，无法分析 |
| 22 | [USE-OPTI-01-003](case/USE-OPTI-01-003.md) | 该用例规格文件缺失，无法分析 |
| 23 | [USE-PR-01-001](case/USE-PR-01-001.md) | 该用例规格文件缺失，无法分析 |
| 24 | [USE-PR-01-002](case/USE-PR-01-002.md) | 该用例规格文件缺失，无法分析 |
| 25 | [USE-PUSH-01-001](case/USE-PUSH-01-001.md) | 该用例规格文件缺失，无法分析 |
| 26 | [USE-REPORT-01-001](case/USE-REPORT-01-001.md) | 该用例规格文件缺失，无法分析 |
| 27 | [USE-REPORT-01-002](case/USE-REPORT-01-002.md) | 该用例规格文件缺失，无法分析 |
| 28 | [USE-REPORT-01-003](case/USE-REPORT-01-003.md) | 该用例规格文件缺失，无法分析 |
| 29 | [USE-REUS-01-001](case/USE-REUS-01-001.md) | 该用例规格文件缺失，无法分析 |
| 30 | [USE-REUS-01-002](case/USE-REUS-01-002.md) | 该用例规格文件缺失，无法分析 |
| 31 | [USE-REUSABLE-01-001](case/USE-REUSABLE-01-001.md) | 该用例规格文件缺失，无法分析 |
| 32 | [USE-REUSABLE-01-002](case/USE-REUSABLE-01-002.md) | 该用例规格文件缺失，无法分析 |
| 33 | [USE-RUNNER-01-001](case/USE-RUNNER-01-001.md) | 该用例规格文件缺失，无法分析 |
| 34 | [USE-RUNNER-01-002](case/USE-RUNNER-01-002.md) | 该用例规格文件缺失，无法分析 |
| 35 | [USE-RUNNER-01-003](case/USE-RUNNER-01-003.md) | 该用例规格文件缺失，无法分析 |
| 36 | [USE-SCHED-01-001](case/USE-SCHED-01-001.md) | 该用例规格文件缺失，无法分析 |
| 37 | [USE-SCHED-01-002](case/USE-SCHED-01-002.md) | 该用例规格文件缺失，无法分析 |
| 38 | [USE-SECRET-01-001](case/USE-SECRET-01-001.md) | 该用例规格文件缺失，无法分析 |
| 39 | [USE-SECRET-01-002](case/USE-SECRET-01-002.md) | 该用例规格文件缺失，无法分析 |
| 40 | [USE-STATUS-01-001](case/USE-STATUS-01-001.md) | 该用例规格文件缺失，无法分析 |
| 41 | [USE-STATUS-01-002](case/USE-STATUS-01-002.md) | 该用例规格文件缺失，无法分析 |
| 42 | [USE-STATUS-01-003](case/USE-STATUS-01-003.md) | 该用例规格文件缺失，无法分析 |
| 43 | [USE-STEP-01-001](case/USE-STEP-01-001.md) | 该用例规格文件缺失，无法分析 |
| 44 | [USE-STEP-01-002](case/USE-STEP-01-002.md) | 该用例规格文件缺失，无法分析 |
| 45 | [USE-STEPSUM-01-001](case/USE-STEPSUM-01-001.md) | 该用例规格文件缺失，无法分析 |
| 46 | [USE-TIMEOUT-01-001](case/USE-TIMEOUT-01-001.md) | 该用例规格文件缺失，无法分析 |
| 47 | [USE-TOKEN-01-001](case/USE-TOKEN-01-001.md) | 该用例规格文件缺失，无法分析 |
| 48 | [USE-TOKEN-01-002](case/USE-TOKEN-01-002.md) | 该用例规格文件缺失，无法分析 |
| 49 | [USE-TRIG-01-001](case/USE-TRIG-01-001.md) | 该用例规格文件缺失，无法分析 |
| 50 | [USE-TRIG-01-002](case/USE-TRIG-01-002.md) | 该用例规格文件缺失，无法分析 |
