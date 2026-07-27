# 断言-步骤一致性报告

**用例总数**: 419（已分析 369 例，另有 50 例缺文本规格）

---

## 1. 总览

| 评级 | 数量 | 说明 |
|------|:---:|------|
| 断言一致 | 170 | 所有验证点可被步骤真实覆盖 |
| 部分不符 | 171 | 部分验证点为 TRIVIAL / MISSING / UNVERIFIABLE |
| 完全不符 | 28 | 全部验证点未能由步骤产出 |
| 合计 | **369** | |

| 维度 | 断言一致 | 部分不符 | 完全不符 | 合计 |
|------|:---:|:---:|:---:|:---:|
| usability/compatibility | 3 | 4 | 4 | 11 |
| usability/security | 0 | 1 | 0 | 1 |
| 兼容性 | 70 | 35 | 2 | 107 |
| 可靠性 | 3 | 9 | 1 | 13 |
| 安全性 | 23 | 28 | 0 | 51 |
| 完备性 | 45 | 36 | 7 | 88 |
| 易用性 | 18 | 9 | 10 | 37 |
| 稳定性 | 8 | 49 | 4 | 61 |

---

## 断言一致 — 所有验证点真实覆盖（170 例）

| # | Case ID | 标题 | 原因 |
|---|---------|------|------|
| 1 | [COMP-ARTIFACT-01-001](case/COMP-ARTIFACT-01-001.md) | artifact 可在同 workflow 的 job 间正确传递 |  |
| 2 | [COMP-ARTIFACT-01-002](case/COMP-ARTIFACT-01-002.md) | 下载全部制品功能正常 |  |
| 3 | [COMP-ARTIFACT-01-003](case/COMP-ARTIFACT-01-003.md) | artifact 保留期设置生效 |  |
| 4 | [COMP-CACHE-01-001](case/COMP-CACHE-01-001.md) | cache hit 时恢复缓存内容正确 |  |
| 5 | [COMP-CACHE-01-002](case/COMP-CACHE-01-002.md) | restore-keys 前缀匹配兜底生效 |  |
| 6 | [COMP-CALL-01-002](case/COMP-CALL-01-002.md) | 3 层 workflow_call 嵌套应被拒绝 |  |
| 7 | [COMP-CTX-01-051](case/COMP-CTX-01-051.md) | 上下文在 workflow job step 各级注入验证 |  |
| 8 | [COMP-CTX-01-053](case/COMP-CTX-01-053.md) | 上下文在 Action 插件参数中注入验证 |  |
| 9 | [COMP-DIR-01-001](case/COMP-DIR-01-001.md) | .gitcode/workflows/ 下的 YAML 被正确识别并触发 |  |
| 10 | [COMP-DIR-01-002](case/COMP-DIR-01-002.md) | .github/workflows/ 下的 YAML 不被识别为 workflow |  |
| 11 | [COMP-EXPR-01-057](case/COMP-EXPR-01-057.md) | format substring replace 函数边界行为 |  |
| 12 | [COMP-ISOLATION-01-002](case/COMP-ISOLATION-01-002.md) | 环境变量不跨 job 泄漏 |  |
| 13 | [COMP-JOB-01-067](case/COMP-JOB-01-067.md) | job 可选字段 env if timeout-minutes needs 验证 |  |
| 14 | [COMP-JOB-01-068](case/COMP-JOB-01-068.md) | job strategy 矩阵与 continue-on-error 验证 |  |
| 15 | [COMP-PERMS-01-001](case/COMP-PERMS-01-001.md) | permissions 空对象时 ATOMGIT_TOKEN 仅 repositor |  |
| 16 | [COMP-PERMS-01-002](case/COMP-PERMS-01-002.md) | 声明 repository write 后 TOKEN 可推送代码 |  |
| 17 | [COMP-PERMS-01-003](case/COMP-PERMS-01-003.md) | fork PR 的 pull_request 下声明 write 仍仅 read |  |
| 18 | [COMP-PR-01-001](case/COMP-PR-01-001.md) | fork PR 触发 pull_request 时不可读取项目 secrets |  |
| 19 | [COMP-PR-01-002](case/COMP-PR-01-002.md) | pull_request_target 可访问 secrets 且 TOKEN 拥有 |  |
| 20 | [COMP-PR-01-003](case/COMP-PR-01-003.md) | fork PR 的 pull_request workflow ATOMGIT_TO |  |
| 21 | [COMP-PUSH-01-002](case/COMP-PUSH-01-002.md) | 不匹配 branches 的 push 不触发 workflow |  |
| 22 | [COMP-RERUN-01-001](case/COMP-RERUN-01-001.md) | rerun 后 atomgit.sha 保持原始值 run_number 递增 |  |
| 23 | [COMP-RUNNER-01-001](case/COMP-RUNNER-01-001.md) | 三段式标签正确调度到对应规格 Runner |  |
| 24 | [COMP-RUNNER-01-002](case/COMP-RUNNER-01-002.md) | runs-on default 等效 ubuntu-latest x64 small |  |
| 25 | [COMP-RUNNER-01-080](case/COMP-RUNNER-01-080.md) | runner 上下文属性可访问性验证 |  |
| 26 | [COMP-SCRIPT-01-081](case/COMP-SCRIPT-01-081.md) | 仓库内脚本执行与路径验证 |  |
| 27 | [COMP-SCRIPT-01-082](case/COMP-SCRIPT-01-082.md) | 脚本权限设置与直接执行验证 |  |
| 28 | [COMP-SECRET-01-001](case/COMP-SECRET-01-001.md) | echo secret 在日志中被脱敏为 *** |  |
| 29 | [COMP-SECRET-01-002](case/COMP-SECRET-01-002.md) | secret 原始值不应以明文出现在标准日志中 |  |
| 30 | [COMP-SECRET-01-003](case/COMP-SECRET-01-003.md) | base64 编码后的 secret 是否仍被脱敏 |  |
| 31 | [COMP-STAGES-01-002](case/COMP-STAGES-01-002.md) | fail_fast true 时 stage 内任一 job 失败终止同阶段其余 j |  |
| 32 | [COMP-STATUS-01-002](case/COMP-STATUS-01-002.md) | 失败 step 的日志完整保留且可查看 |  |
| 33 | [COMP-STEP-01-069](case/COMP-STEP-01-069.md) | step 必填与核心字段 name run uses 验证 |  |
| 34 | [COMP-STEP-01-070](case/COMP-STEP-01-070.md) | step 可选字段 id env if with 验证 |  |
| 35 | [COMP-SUMMARY-01-001](case/COMP-SUMMARY-01-001.md) | ATOMGIT_STEP_SUMMARY Markdown 表格与标题正确渲染 |  |
| 36 | [COMP-SUMMARY-01-002](case/COMP-SUMMARY-01-002.md) | summary 中不应暴露系统内部路径 |  |
| 37 | [COMP-SYSENV-01-059](case/COMP-SYSENV-01-059.md) | ATOMGIT 系统环境变量关键变量存在性 |  |
| 38 | [COMP-SYSENV-01-060](case/COMP-SYSENV-01-060.md) | ATOMGIT 系统环境变量值正确性 |  |
| 39 | [COMP-TIMEOUT-01-002](case/COMP-TIMEOUT-01-002.md) | 超时的 job 被强制终止并标记为 failure |  |
| 40 | [COMP-TRIG-01-072](case/COMP-TRIG-01-072.md) | push 事件关键字段与过滤验证 |  |
| 41 | [COMP-TRIG-01-074](case/COMP-TRIG-01-074.md) | workflow_dispatch 事件关键字段与 inputs 验证 |  |
| 42 | [COMP-TRIG-01-076](case/COMP-TRIG-01-076.md) | issue_comment 事件关键字段与 types 验证 |  |
| 43 | [COMP-TRIG-01-077](case/COMP-TRIG-01-077.md) | pull_request_comment 事件关键字段与过滤验证 |  |
| 44 | [COMP-UNKNOWN-01-002](case/COMP-UNKNOWN-01-002.md) | 不应静默忽略未知字段导致用户误以为配置生效 |  |
| 45 | [COMP-VARREF-01-083](case/COMP-VARREF-01-083.md) | YAML 表达式与 Shell 环境变量引用方式验证 |  |
| 46 | [COMPAT-ACTION-01-001](case/COMPAT-ACTION-01-001.md) | checkout 短名等价性——ref 参数支持 |  |
| 47 | [COMPAT-ACTION-01-002](case/COMPAT-ACTION-01-002.md) | checkout 短名等价性——path 参数支持 |  |
| 48 | [COMPAT-ACTIONDEV-01-001](case/COMPAT-ACTIONDEV-01-001.md) | action.yml 元数据校验与 GitHub 差异 |  |
| 49 | [COMPAT-ARTIFACT-01-001](case/COMPAT-ARTIFACT-01-001.md) | upload/download-artifact 跨 job 传递等价性 |  |
| 50 | [COMPAT-ARTIFACT-01-002](case/COMPAT-ARTIFACT-01-002.md) | upload-artifact 保留期行为等价性 |  |
| 51 | [COMPAT-CACHE-01-001](case/COMPAT-CACHE-01-001.md) | cache 行为等价性——缓存命中场景 |  |
| 52 | [COMPAT-CACHE-01-002](case/COMPAT-CACHE-01-002.md) | cache 行为等价性——fork PR 写隔离 |  |
| 53 | [COMPAT-COMM-01-001](case/COMPAT-COMM-01-001.md) | issue_comment types 命名差异 - GitCode 合法 type |  |
| 54 | [COMPAT-CONCUR-01-001](case/COMPAT-CONCUR-01-001.md) | concurrency cancel-in-progress false 时应排队而 |  |
| 55 | [COMPAT-CONCUR-01-002](case/COMPAT-CONCUR-01-002.md) | concurrency 配置越界或不支持时应给出清晰报错 |  |
| 56 | [COMPAT-CONCUR-01-003](case/COMPAT-CONCUR-01-003.md) | concurrency preemption enable 行为差异 |  |
| 57 | [COMPAT-CONCUR-01-004](case/COMPAT-CONCUR-01-004.md) | concurrency preemption events 越界时行为差异 |  |
| 58 | [COMPAT-CONTAINER-01-001](case/COMPAT-CONTAINER-01-001.md) | container 字段不被支持时应明确报错而非静默忽略 |  |
| 59 | [COMPAT-CONTAINER-01-002](case/COMPAT-CONTAINER-01-002.md) | container 自定义镜像被拒绝时应给出替代指引 |  |
| 60 | [COMPAT-CTX-01-001](case/COMPAT-CTX-01-001.md) | 使用 github.ref 上下文应报错或求值为空 |  |
| 61 | [COMPAT-CTX-01-002](case/COMPAT-CTX-01-002.md) | 使用 atomgit.ref 上下文应正确返回触发引用 |  |
| 62 | [COMPAT-CTX-01-003](case/COMPAT-CTX-01-003.md) | github 上下文嵌套属性访问应报错而非返回空 |  |
| 63 | [COMPAT-DEPR-01-001](case/COMPAT-DEPR-01-001.md) | ::set-env:: 废弃命令应被拒绝或给出迁移指引 |  |
| 64 | [COMPAT-DEPR-01-002](case/COMPAT-DEPR-01-002.md) | ::add-path:: 废弃命令应被拒绝或给出迁移指引 |  |
| 65 | [COMPAT-DIR-01-002](case/COMPAT-DIR-01-002.md) | 工作流目录差异——.github/workflows/ 不应被识别 |  |
| 66 | [COMPAT-DIR-01-003](case/COMPAT-DIR-01-003.md) | .github/workflows 目录不应被识别且应给出迁移提示 |  |
| 67 | [COMPAT-ENV-01-001](case/COMPAT-ENV-01-001.md) | ATOMGIT_SHA 环境变量应正确返回触发提交 SHA |  |
| 68 | [COMPAT-ENV-01-002](case/COMPAT-ENV-01-002.md) | GITHUB_SHA 环境变量在 GitCode 中应为空或未定义 |  |
| 69 | [COMPAT-ENV-01-003](case/COMPAT-ENV-01-003.md) | GITHUB_ENV 环境变量不应被静默映射到 ATOMGIT_ENV |  |
| 70 | [COMPAT-ENVIRON-01-002](case/COMPAT-ENVIRON-01-002.md) | environment 字段绑定 secrets 的行为差异 |  |
| 71 | [COMPAT-EXPR-01-001](case/COMPAT-EXPR-01-001.md) | success 关键字在条件表达式中的可用性 |  |
| 72 | [COMPAT-EXPR-01-008](case/COMPAT-EXPR-01-008.md) | toJson 表达式输出格式差异（pretty-print vs compact） |  |
| 73 | [COMPAT-EXPR-01-009](case/COMPAT-EXPR-01-009.md) | loose equality 跨类型强制求值差异 |  |
| 74 | [COMPAT-EXPR-01-010](case/COMPAT-EXPR-01-010.md) | loose equality null 与空字符串及零的等价性差异 |  |
| 75 | [COMPAT-EXPR-01-013](case/COMPAT-EXPR-01-013.md) | success() 带括号与不带括号的兼容性差异 |  |
| 76 | [COMPAT-EXPR-01-014](case/COMPAT-EXPR-01-014.md) | always() 带括号与不带括号的兼容性差异 |  |
| 77 | [COMPAT-IF-01-001](case/COMPAT-IF-01-001.md) | step 失败后后续 step 默认跳过行为 |  |
| 78 | [COMPAT-IF-01-002](case/COMPAT-IF-01-002.md) | continue-on-error 标记后失败 step 不阻断后续执行 |  |
| 79 | [COMPAT-INPUTS-01-002](case/COMPAT-INPUTS-01-002.md) | workflow_dispatch inputs 类型限制 - string 正常通 |  |
| 80 | [COMPAT-ISOLATE-01-001](case/COMPAT-ISOLATE-01-001.md) | Runner 环境隔离——跨 job 文件隔离 |  |
| 81 | [COMPAT-ISOLATE-01-002](case/COMPAT-ISOLATE-01-002.md) | Runner 环境隔离——跨 job 环境变量隔离 |  |
| 82 | [COMPAT-MASK-01-001](case/COMPAT-MASK-01-001.md) | 直接 echo secrets 值应在日志中被脱敏 |  |
| 83 | [COMPAT-MASK-01-002](case/COMPAT-MASK-01-002.md) | 通过 env 注入 secret 后输出应在日志中被脱敏 |  |
| 84 | [COMPAT-MATRIX-01-003](case/COMPAT-MATRIX-01-003.md) | matrix 三维展开不被支持时的差异 |  |
| 85 | [COMPAT-MATRIX-01-004](case/COMPAT-MATRIX-01-004.md) | matrix include 无基础变量不被支持时的差异 |  |
| 86 | [COMPAT-MATRIX-01-005](case/COMPAT-MATRIX-01-005.md) | matrix exclude 全排除不被支持时的差异 |  |
| 87 | [COMPAT-MIGRATE-01-001](case/COMPAT-MIGRATE-01-001.md) | GitHub 风格 permissions 块迁移报错应给出可操作指引 |  |
| 88 | [COMPAT-MIGRATE-01-002](case/COMPAT-MIGRATE-01-002.md) | GitHub 风格 run-name 语法迁移报错应给出可操作指引 |  |
| 89 | [COMPAT-OUTCOME-01-001](case/COMPAT-OUTCOME-01-001.md) | continue-on-error false 时 outcome 与 conclu |  |
| 90 | [COMPAT-OUTCOME-01-002](case/COMPAT-OUTCOME-01-002.md) | continue-on-error true 时 outcome 应为 failur |  |
| 91 | [COMPAT-OUTCOME-01-003](case/COMPAT-OUTCOME-01-003.md) | outcome 与 conclusion 在 job 条件判断中不应互换语义 |  |
| 92 | [COMPAT-OUTPUT-01-001](case/COMPAT-OUTPUT-01-001.md) | 跨 Job 引用未声明 output 时返回空值的差异 |  |
| 93 | [COMPAT-PERM-01-003](case/COMPAT-PERM-01-003.md) | permissions 命名差异——GitHub contents 权限项应报错 |  |
| 94 | [COMPAT-PERM-01-004](case/COMPAT-PERM-01-004.md) | permissions 命名差异——GitCode repository 权限项正常 |  |
| 95 | [COMPAT-PERM-01-005](case/COMPAT-PERM-01-005.md) | permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异 |  |
| 96 | [COMPAT-PR-01-001](case/COMPAT-PR-01-001.md) | pull_request types 命名差异 - GitCode 合法 types |  |
| 97 | [COMPAT-PR-01-003](case/COMPAT-PR-01-003.md) | PR types 配置后匹配类型不触发与 GitHub 行为差异 |  |
| 98 | [COMPAT-PR-01-004](case/COMPAT-PR-01-004.md) | PR types 含 merge 时不触发与 GitHub 行为差异 |  |
| 99 | [COMPAT-PR-01-005](case/COMPAT-PR-01-005.md) | PR paths 过滤不工作时的兼容性差异 |  |
| 100 | [COMPAT-PR-01-006](case/COMPAT-PR-01-006.md) | PR 目标分支过滤行为差异 |  |
| 101 | [COMPAT-SCHEDULE-01-001](case/COMPAT-SCHEDULE-01-001.md) | schedule cron 按 UTC 时间触发 |  |
| 102 | [COMPAT-SCHEDULE-01-003](case/COMPAT-SCHEDULE-01-003.md) | schedule 在非默认分支不触发与 GitHub 差异 |  |
| 103 | [COMPAT-SECRET-01-005](case/COMPAT-SECRET-01-005.md) | 环境级 secrets 不支持时应明确报错而非降级为项目级 |  |
| 104 | [COMPAT-SHELL-01-001](case/COMPAT-SHELL-01-001.md) | 默认 shell 隐式行为差异 - 未显式声明时是否为 bash |  |
| 105 | [COMPAT-SHELL-01-002](case/COMPAT-SHELL-01-002.md) | 默认工作目录隐式行为差异 - 未显式声明时是否为仓库根目录 |  |
| 106 | [COMPAT-TARGET-01-001](case/COMPAT-TARGET-01-001.md) | pull_request_target 默认 checkout 应为 base 分支 |  |
| 107 | [COMPAT-TARGET-01-002](case/COMPAT-TARGET-01-002.md) | pull_request_target 在 fork 场景下应保持 secret 隔 |  |
| 108 | [COMPAT-TARGET-01-003](case/COMPAT-TARGET-01-003.md) | pull_request_target 默认 types 与 GitHub 差异 |  |
| 109 | [COMPAT-TOKEN-01-001](case/COMPAT-TOKEN-01-001.md) | ATOMGIT_TOKEN 应正确返回有效令牌 |  |
| 110 | [COMPAT-TOKEN-01-003](case/COMPAT-TOKEN-01-003.md) | GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN |  |
| 111 | [COMPAT-VARS-01-001](case/COMPAT-VARS-01-001.md) | vars 上下文若支持应正确返回值 |  |
| 112 | [COMPAT-VARS-01-003](case/COMPAT-VARS-01-003.md) | vars 项目级覆盖组织级的优先级差异 |  |
| 113 | [COMPAT-VARS-01-004](case/COMPAT-VARS-01-004.md) | vars 与 env 同名时的优先级差异 |  |
| 114 | [COMPAT-VARS-01-005](case/COMPAT-VARS-01-005.md) | vars 在条件表达式 if 中的可用性差异 |  |
| 115 | [COMPAT-VARS-01-006](case/COMPAT-VARS-01-006.md) | vars 在 Action 中的可用性差异 |  |
| 116 | [REL-ART-01-041](case/REL-ART-01-041.md) | 超大 artifact——100 MB artifact 上传后下游 job 应成功 |  |
| 117 | [REL-ARTCONC-01-063](case/REL-ARTCONC-01-063.md) | 制品并发写一致性——多 job 同时 upload-artifact 同名 arti |  |
| 118 | [REL-ARTPERF-01-053-V2](case/REL-ARTPERF-01-053-V2.md) | 制品传输性能——1GB artifact 上传下载耗时 |  |
| 119 | [REL-ARTPERF-01-053](case/REL-ARTPERF-01-053.md) | 制品传输性能——100MB artifact 上传下载耗时 |  |
| 120 | [REL-CANCEL-01-028](case/REL-CANCEL-01-028.md) | 手动取消 workflow——运行中取消时 always() cleanup ste |  |
| 121 | [REL-FAULT-01-035](case/REL-FAULT-01-035.md) | 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务 |  |
| 122 | [REL-LOGPERF-01-051-V2](case/REL-LOGPERF-01-051-V2.md) | 日志加载性能——200MB 日志下载与查看耗时 |  |
| 123 | [REL-MATRIX-01-039](case/REL-MATRIX-01-039.md) | 大规模 matrix——50 个组合应全部生成并正确调度 |  |
| 124 | [REL-RETAIN-01-047](case/REL-RETAIN-01-047.md) | artifact 保留期 90 天边界——第 91 天应不可下载 |  |
| 125 | [REL-STATE-01-058](case/REL-STATE-01-058.md) | Runner 状态机正确性——空闲/运行/离线转换与时序一致性 |  |
| 126 | [REL-TIMEOUT-01-009](case/REL-TIMEOUT-01-009.md) | 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被 |  |
| 127 | [SEC-ARTF-01-001](case/SEC-ARTF-01-001.md) | fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执 |  |
| 128 | [SEC-ARTF-01-002](case/SEC-ARTF-01-002.md) | 跨仓库 artifact 下载返回 403 或 404 |  |
| 129 | [SEC-BASE-01-001](case/SEC-BASE-01-001.md) | pull_request_target 使用 base 分支的 workflow 版 |  |
| 130 | [SEC-BASE-01-002](case/SEC-BASE-01-002.md) | fork PR 改 workflow 不被 pull_request_target  |  |
| 131 | [SEC-CACHE-01-002](case/SEC-CACHE-01-002.md) | 主仓 cache restore 对 fork cache miss |  |
| 132 | [SEC-DEFPERM-01-002](case/SEC-DEFPERM-01-002.md) | job 级覆盖后权限正确收窄 |  |
| 133 | [SEC-ENV-01-001](case/SEC-ENV-01-001.md) | 环境级 secret 必须经审批后才能被 workflow 访问 |  |
| 134 | [SEC-ENV-01-002](case/SEC-ENV-01-002.md) | 环境级 secret 审批前 workflow 不可读取 |  |
| 135 | [SEC-FORK-01-001](case/SEC-FORK-01-001.md) | fork PR 触发 pull_request 时不可读取项目 secrets |  |
| 136 | [SEC-FORK-01-002](case/SEC-FORK-01-002.md) | fork PR 中 secrets 引用返回空值且 job 不崩溃 |  |
| 137 | [SEC-MASK-01-002](case/SEC-MASK-01-002.md) | Secret 值在 step summary 和错误堆栈中必须被脱敏 |  |
| 138 | [SEC-NAME-01-001](case/SEC-NAME-01-001.md) | Secret/变量名含特殊字符时不可导致意外求值或权限绕过 |  |
| 139 | [SEC-PRTGT-01-001](case/SEC-PRTGT-01-001.md) | pull_request_target 下显式 checkout 不可信 PR 时  |  |
| 140 | [SEC-PRTGT-01-002](case/SEC-PRTGT-01-002.md) | pull_request_target 无审批不执行 fork PR 代码 |  |
| 141 | [SEC-SIDE-01-001](case/SEC-SIDE-01-001.md) | Secret 不经 output 侧信道绕过脱敏外泄 |  |
| 142 | [SEC-SIDE-01-002](case/SEC-SIDE-01-002.md) | Secret 不经 artifact 侧信道绕过脱敏外泄 |  |
| 143 | [SEC-SUPPLY-01-001](case/SEC-SUPPLY-01-001.md) | 第三方 Action 引用应支持完整 commit hash 固定 |  |
| 144 | [SEC-SUPPLY-01-002](case/SEC-SUPPLY-01-002.md) | commit hash 不匹配时第三方 Action 应被拒绝执行 |  |
| 145 | [SEC-SUPPLY-01-003](case/SEC-SUPPLY-01-003.md) | 第三方 Action 来源应具备信任边界（typosquatting 限制） |  |
| 146 | [SEC-TOCTOU-01-002](case/SEC-TOCTOU-01-002.md) | 评论触发不应绕过代码固定与 PR 审批 |  |
| 147 | [SEC-TOKEN-01-001](case/SEC-TOKEN-01-001.md) | fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须 |  |
| 148 | [SEC-TOKEN-01-002](case/SEC-TOKEN-01-002.md) | fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝 |  |
| 149 | [SEC-WCMD-01-002](case/SEC-WCMD-01-002.md) | 跨运行 artifact 必须被视为不可信数据 |  |
| 150 | [USE-ACT-01-001](case/USE-ACT-01-001.md) | 使用裸插件名 checkout 时正常拉取官方 Action |  |
| 151 | [USE-ANNOT-01-001](case/USE-ANNOT-01-001.md) | workflow 命令 ::error:: 与 ::warning:: 在日志中保留 |  |
| 152 | [USE-CONC-01-001](case/USE-CONC-01-001.md) | concurrency.max 配置 0 或 10 时报错应提示有效范围 1-5 |  |
| 153 | [USE-CONC-01-002](case/USE-CONC-01-002.md) | concurrency.max 配置 -1 时报错应提示有效范围 |  |
| 154 | [USE-CTX-01-002](case/USE-CTX-01-002.md) | 使用 github 上下文时报错应提示 atomgit 替代 |  |
| 155 | [USE-DISP-01-001](case/USE-DISP-01-001.md) | workflow_dispatch 必填参数未提供时应给出明确校验错误 |  |
| 156 | [USE-ENV-01-001](case/USE-ENV-01-001.md) | 使用 ATOMGIT_SHA 环境变量时正常取值 |  |
| 157 | [USE-INPT-01-001](case/USE-INPT-01-001.md) | 使用 string 类型 input 时正常通过校验 |  |
| 158 | [USE-INPT-01-002](case/USE-INPT-01-002.md) | 使用 boolean 类型 input 时报错应提示仅支持 string |  |
| 159 | [USE-LBL-01-001](case/USE-LBL-01-001.md) | runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表 |  |
| 160 | [USE-LBL-01-002](case/USE-LBL-01-002.md) | runs-on 标签因容量不足排队时应提示排队状态而非无可用 runner |  |
| 161 | [USE-NEST-01-001](case/USE-NEST-01-001.md) | workflow_call 嵌套 3 层时报错应明确提示上限为 2 层 |  |
| 162 | [USE-PERM-01-001](case/USE-PERM-01-001.md) | 使用 GitCode 权限域命名时正常生效 |  |
| 163 | [USE-RUN-01-001](case/USE-RUN-01-001.md) | 使用三段式标签时 job 正常调度 |  |
| 164 | [USE-RUN-01-002](case/USE-RUN-01-002.md) | 使用单标签 ubuntu-latest 时报错应给出三段式格式指引 |  |
| 165 | [USE-SEARCH-01-001](case/USE-SEARCH-01-001.md) | 日志搜索与下载功能可用且交互流畅 |  |
| 166 | [USE-SECNAME-01-001](case/USE-SECNAME-01-001.md) | Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误 |  |
| 167 | [USE-SECNAME-01-002](case/USE-SECNAME-01-002.md) | Secret 名称以数字开头时应给出命名规则错误 |  |
| 168 | [USE-STAT-01-001](case/USE-STAT-01-001.md) | 使用 always() 带括号时若被接受则正常执行 |  |
| 169 | [USE-STAT-01-002](case/USE-STAT-01-002.md) | 使用 success() 带括号时报错应提示 GitCode 括号差异 |  |
| 170 | [USE-TYPE-01-001](case/USE-TYPE-01-001.md) | 使用 GitCode types 命名时正常触发 |  |

## 部分不符 — 验证点与步骤产出部分不一致（171 例）

| # | Case ID | 标题 | 原因 |
|---|---------|------|------|
| 1 | [COMP-ATOMGIT-01-047](case/COMP-ATOMGIT-01-047.md) | atomgit 核心上下文属性可访问性 |  |
| 2 | [COMP-ATOMGIT-01-048](case/COMP-ATOMGIT-01-048.md) | atomgit 事件相关属性可访问性 |  |
| 3 | [COMP-ATOMGIT-01-049](case/COMP-ATOMGIT-01-049.md) | atomgit 边界格式校验 |  |
| 4 | [COMP-BOUND-01-084](case/COMP-BOUND-01-084.md) | 路径与分支过滤组合及否定模式边界验证 |  |
| 5 | [COMP-BOUND-01-086](case/COMP-BOUND-01-086.md) | 矩阵构建 include exclude 与单值边界验证 |  |
| 6 | [COMP-BOUND-01-087](case/COMP-BOUND-01-087.md) | 步骤输出与跨 job 传递边界验证 |  |
| 7 | [COMP-BOUND-01-088](case/COMP-BOUND-01-088.md) | 工作流命令 set-env add-path 与文件写入边界验证 |  |
| 8 | [COMP-CALL-01-001](case/COMP-CALL-01-001.md) | 2 层 workflow_call 嵌套正常执行 |  |
| 9 | [COMP-CTX-01-052](case/COMP-CTX-01-052.md) | 上下文在条件表达式 if 中注入验证 |  |
| 10 | [COMP-ENVCTX-01-050](case/COMP-ENVCTX-01-050.md) | env 优先级链 step 大于 job 大于 workflow |  |
| 11 | [COMP-EXPR-01-054](case/COMP-EXPR-01-054.md) | 字符串函数 contains startsWith endsWith 边界行 |  |
| 12 | [COMP-EXPR-01-055](case/COMP-EXPR-01-055.md) | hashFiles 函数边界行为 |  |
| 13 | [COMP-EXPR-01-056](case/COMP-EXPR-01-056.md) | toJson 函数边界行为 |  |
| 14 | [COMP-EXPR-01-058](case/COMP-EXPR-01-058.md) | 表达式运算符与优先级边界行为 |  |
| 15 | [COMP-ISOLATION-01-001](case/COMP-ISOLATION-01-001.md) | 同一 workflow 先后 job 的文件系统相互隔离 |  |
| 16 | [COMP-JOB-01-066](case/COMP-JOB-01-066.md) | job 必填字段 name runs-on steps 验证 |  |
| 17 | [COMP-PRTARGET-01-001](case/COMP-PRTARGET-01-001.md) | pull_request_target 默认使用 base 分支 workf |  |
| 18 | [COMP-PRTARGET-01-002](case/COMP-PRTARGET-01-002.md) | 显式 checkout head.sha 后执行不可信代码的风险可控 |  |
| 19 | [COMP-PUSH-01-001](case/COMP-PUSH-01-001.md) | 匹配 branches 的 push 正确触发 workflow |  |
| 20 | [COMP-PUSH-01-003](case/COMP-PUSH-01-003.md) | paths 过滤匹配前 300 个变更文件行为符合预期 |  |
| 21 | [COMP-RERUN-01-002](case/COMP-RERUN-01-002.md) | 第 4 次 rerun 应被系统拒绝 |  |
| 22 | [COMP-RERUN-01-003](case/COMP-RERUN-01-003.md) | 超过 6 小时的运行不可 rerun |  |
| 23 | [COMP-STAGES-01-003](case/COMP-STAGES-01-003.md) | post.run_always true 时 workflow 失败仍执行  |  |
| 24 | [COMP-STATUS-01-001](case/COMP-STATUS-01-001.md) | 运行状态机 queued 到 completed 转换正确 |  |
| 25 | [COMP-STEP-01-071](case/COMP-STEP-01-071.md) | step 执行控制 shell working-directory cont |  |
| 26 | [COMP-TIMEOUT-01-001](case/COMP-TIMEOUT-01-001.md) | 未声明 timeout-minutes 的 job 在 360 分钟内正常完 |  |
| 27 | [COMP-TRIG-01-073](case/COMP-TRIG-01-073.md) | pull_request 事件关键字段与 types 验证 |  |
| 28 | [COMP-TRIG-01-075](case/COMP-TRIG-01-075.md) | schedule 事件关键字段与 cron 格式验证 |  |
| 29 | [COMP-TRIG-01-078](case/COMP-TRIG-01-078.md) | 多事件组合与分支路径过滤验证 |  |
| 30 | [COMP-TRIG-01-079](case/COMP-TRIG-01-079.md) | 触发事件 types 取值与过滤边界验证 |  |
| 31 | [COMP-UNKNOWN-01-001](case/COMP-UNKNOWN-01-001.md) | 包含未知顶层字段的 workflow 触发 YAML 校验失败 |  |
| 32 | [COMP-WFLOW-01-061](case/COMP-WFLOW-01-061.md) | workflow name 与 on 字段必填与类型验证 |  |
| 33 | [COMP-WFLOW-01-062](case/COMP-WFLOW-01-062.md) | workflow env 与 defaults 字段验证 |  |
| 34 | [COMP-WFLOW-01-063](case/COMP-WFLOW-01-063.md) | workflow concurrency 并发控制字段验证 |  |
| 35 | [COMP-WFLOW-01-064](case/COMP-WFLOW-01-064.md) | workflow stages 阶段结构字段验证 |  |
| 36 | [COMP-WFLOW-01-065](case/COMP-WFLOW-01-065.md) | workflow post 后处理阶段字段验证 |  |
| 37 | [COMPAT-DIR-01-001](case/COMPAT-DIR-01-001.md) | 工作流目录差异——.gitcode/workflows/ 正常识别 |  |
| 38 | [COMPAT-ENVIRON-01-001](case/COMPAT-ENVIRON-01-001.md) | 含 environment 字段的 job 应被报错或警告 |  |
| 39 | [COMPAT-EXPR-01-002](case/COMPAT-EXPR-01-002.md) | success() 函数的处理行为差异 |  |
| 40 | [COMPAT-EXPR-01-003](case/COMPAT-EXPR-01-003.md) | failure() 与 failed 关键字的处理行为差异 |  |
| 41 | [COMPAT-EXPR-01-004](case/COMPAT-EXPR-01-004.md) | contains 表达式大小写敏感边界 |  |
| 42 | [COMPAT-EXPR-01-005](case/COMPAT-EXPR-01-005.md) | contains 表达式空值与空字符串边界 |  |
| 43 | [COMPAT-EXPR-01-006](case/COMPAT-EXPR-01-006.md) | hashFiles 表达式无匹配路径边界 |  |
| 44 | [COMPAT-EXPR-01-007](case/COMPAT-EXPR-01-007.md) | hashFiles 表达式多路径组合边界 |  |
| 45 | [COMPAT-EXPR-01-011](case/COMPAT-EXPR-01-011.md) | join() 函数缺失时的降级行为 |  |
| 46 | [COMPAT-EXPR-01-012](case/COMPAT-EXPR-01-012.md) | fromJSON() 函数缺失时的降级行为 |  |
| 47 | [COMPAT-FIELD-01-001](case/COMPAT-FIELD-01-001.md) | 含 run-name 字段的 workflow 应被报错或警告 |  |
| 48 | [COMPAT-FIELD-01-002](case/COMPAT-FIELD-01-002.md) | 含 services 字段的 job 应被报错或警告 |  |
| 49 | [COMPAT-FIELD-01-003](case/COMPAT-FIELD-01-003.md) | 未知顶层字段不应被静默忽略而应给出警告 |  |
| 50 | [COMPAT-INPUTS-01-001](case/COMPAT-INPUTS-01-001.md) | workflow_dispatch inputs 类型限制 - boolea |  |
| 51 | [COMPAT-NEST-01-002](case/COMPAT-NEST-01-002.md) | workflow_call 嵌套层数 - 3 层越界应报错 |  |
| 52 | [COMPAT-PATHS-01-001](case/COMPAT-PATHS-01-001.md) | paths 过滤器 300 条边界测试 |  |
| 53 | [COMPAT-PATHS-01-002](case/COMPAT-PATHS-01-002.md) | paths 过滤器 301 条越界测试 |  |
| 54 | [COMPAT-PERM-01-001](case/COMPAT-PERM-01-001.md) | 未声明 permissions 时默认 TOKEN 读操作权限范围 |  |
| 55 | [COMPAT-PERM-01-002](case/COMPAT-PERM-01-002.md) | 未声明 permissions 时 fork PR 写操作隔离 |  |
| 56 | [COMPAT-PR-01-002](case/COMPAT-PR-01-002.md) | pull_request types 命名差异 - GitHub 风格 ty |  |
| 57 | [COMPAT-RUNNER-01-001](case/COMPAT-RUNNER-01-001.md) | runner.os 在 Linux Runner 上应返回 Linux |  |
| 58 | [COMPAT-RUNNER-01-002](case/COMPAT-RUNNER-01-002.md) | runner.arch 在 x86_64 Runner 上应返回 X64 |  |
| 59 | [COMPAT-RUNNER-01-003](case/COMPAT-RUNNER-01-003.md) | self-hosted 标签不被支持时应明确报错 |  |
| 60 | [COMPAT-RUNNER-01-004](case/COMPAT-RUNNER-01-004.md) | 自定义特征标签不被支持时应给出可用标签列表 |  |
| 61 | [COMPAT-RUNNER-01-005](case/COMPAT-RUNNER-01-005.md) | 内网环境 Runner 不支持时的差异 |  |
| 62 | [COMPAT-RUNNER-01-006](case/COMPAT-RUNNER-01-006.md) | Runner 未预装 Java 工具链与 GitHub 差异 |  |
| 63 | [COMPAT-RUNSON-01-001](case/COMPAT-RUNSON-01-001.md) | runs-on 标签体系——三段式数组正常匹配 |  |
| 64 | [COMPAT-RUNSON-01-002](case/COMPAT-RUNSON-01-002.md) | runs-on 标签体系——单标签字符串应报错 |  |
| 65 | [COMPAT-SCHEDULE-01-002](case/COMPAT-SCHEDULE-01-002.md) | schedule 不支持 timezone 字段差异 |  |
| 66 | [COMPAT-SHELL-01-003](case/COMPAT-SHELL-01-003.md) | Windows runner 默认 shell 差异 |  |
| 67 | [COMPAT-TOKEN-01-002](case/COMPAT-TOKEN-01-002.md) | GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射 |  |
| 68 | [COMPAT-VARS-01-002](case/COMPAT-VARS-01-002.md) | vars 上下文若不支持应报错而非静默为空 |  |
| 69 | [COMPAT-WCMD-01-001](case/COMPAT-WCMD-01-001.md) | ::add-mask:: 不被支持时应静默降级而非报错 |  |
| 70 | [COMPAT-WCMD-01-002](case/COMPAT-WCMD-01-002.md) | ::group:: 不被支持时应静默降级而非报错 |  |
| 71 | [COMPAT-WCMD-01-003](case/COMPAT-WCMD-01-003.md) | ::stop-commands:: 不被支持时应静默降级而非报错 |  |
| 72 | [REL-API-01-065](case/REL-API-01-065.md) | API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据 |  |
| 73 | [REL-BIGRUNNER-01-066](case/REL-BIGRUNNER-01-066.md) | 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率 |  |
| 74 | [REL-CACHE-01-046](case/REL-CACHE-01-046.md) | 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰 |  |
| 75 | [REL-CACHEPERF-01-054](case/REL-CACHEPERF-01-054.md) | 缓存加速比——cache 命中 vs 未命中构建耗时对比 |  |
| 76 | [REL-CANCELREL-01-061](case/REL-CANCELREL-01-061.md) | 取消操作可靠性——queued/running/post 各阶段取消状态正确 |  |
| 77 | [REL-CHILDSTATE-01-064-V2](case/REL-CHILDSTATE-01-064-V2.md) | 子任务状态传播——workflow_call 未拉起时父 workflow  |  |
| 78 | [REL-CHILDSTATE-01-064](case/REL-CHILDSTATE-01-064.md) | 子任务状态传播——workflow_call 失败时父 workflow 不 |  |
| 79 | [REL-CONC-01-001](case/REL-CONC-01-001.md) | concurrency.max=5 时同时触发 5 个运行应全部进入执行态 |  |
| 80 | [REL-CONC-01-002](case/REL-CONC-01-002.md) | concurrency.max=6 配置应被系统拒绝 |  |
| 81 | [REL-CONTINUE-01-030](case/REL-CONTINUE-01-030.md) | continue-on-error=true——job 失败后 workfl |  |
| 82 | [REL-CPU-01-022](case/REL-CPU-01-022.md) | Runner CPU 饱和——small runner 运行 4 个 CPU |  |
| 83 | [REL-DISK-01-018](case/REL-DISK-01-018.md) | Runner 磁盘边界——small runner 写入 49 GB 应成功 |  |
| 84 | [REL-DISK-01-019](case/REL-DISK-01-019.md) | Runner 磁盘越界——small runner 写入 51 GB 应失败 |  |
| 85 | [REL-FAULT-01-031](case/REL-FAULT-01-031.md) | 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失 |  |
| 86 | [REL-FAULT-01-032](case/REL-FAULT-01-032.md) | 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误 |  |
| 87 | [REL-FAULT-01-033](case/REL-FAULT-01-033.md) | 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满 |  |
| 88 | [REL-FAULT-01-034](case/REL-FAULT-01-034.md) | 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cac |  |
| 89 | [REL-FLOOD-01-036](case/REL-FLOOD-01-036.md) | 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflo |  |
| 90 | [REL-FLOOD-01-037](case/REL-FLOOD-01-037.md) | 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃 |  |
| 91 | [REL-IGNORE-01-004](case/REL-IGNORE-01-004.md) | concurrency IGNORE 策略——超上限运行应直接执行 |  |
| 92 | [REL-IMAGE-01-052-V2](case/REL-IMAGE-01-052-V2.md) | 镜像拉取性能——5GB 自定义 container 环境准备耗时基准 |  |
| 93 | [REL-IMAGE-01-052](case/REL-IMAGE-01-052.md) | 镜像拉取性能——500MB 自定义 container 环境准备耗时基准 |  |
| 94 | [REL-K8S-01-045](case/REL-K8S-01-045.md) | 自托管 K8s Runner 弹性伸缩——min=1/max=1 时并发 3 |  |
| 95 | [REL-LATENCY-01-050-V2](case/REL-LATENCY-01-050-V2.md) | 调度延迟压力——并发 20 个 job 的排队延迟与完成率 |  |
| 96 | [REL-LOG-01-040](case/REL-LOG-01-040.md) | 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看 |  |
| 97 | [REL-LOGPERF-01-051](case/REL-LOGPERF-01-051.md) | 日志加载性能——50MB 日志下载与查看耗时 |  |
| 98 | [REL-LOGSTABLE-01-059](case/REL-LOGSTABLE-01-059.md) | 日志系统稳定性——6 万行日志无乱序/无丢失/无截断 |  |
| 99 | [REL-LONG-01-043](case/REL-LONG-01-043.md) | 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常 |  |
| 100 | [REL-MATRIX-01-026](case/REL-MATRIX-01-026.md) | matrix fail-fast=true——任意 job 实例失败应立即取 |  |
| 101 | [REL-MATRIX-01-027](case/REL-MATRIX-01-027.md) | matrix max-parallel=4——9 个组合应最多同时运行 4  |  |
| 102 | [REL-MATRIX-01-038](case/REL-MATRIX-01-038.md) | 大规模 matrix——20 个组合应全部生成并正确调度 |  |
| 103 | [REL-MATRIXFAIR-01-056](case/REL-MATRIXFAIR-01-056.md) | 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 |  |
| 104 | [REL-MEM-01-020](case/REL-MEM-01-020.md) | Runner 内存边界——small runner 分配 7.5 GB 应成 |  |
| 105 | [REL-MEM-01-021](case/REL-MEM-01-021.md) | Runner 内存越界——small runner 分配 9 GB 应被 O |  |
| 106 | [REL-NEEDS-01-025](case/REL-NEEDS-01-025.md) | needs 失败传播——上游 job 失败时下游 job 应被 skip |  |
| 107 | [REL-NETFAULT-01-062](case/REL-NETFAULT-01-062.md) | 网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时 |  |
| 108 | [REL-OUTPUT-01-016](case/REL-OUTPUT-01-016.md) | step output 边界值——ATOMGIT_OUTPUT 写入 1 M |  |
| 109 | [REL-OUTPUT-01-017](case/REL-OUTPUT-01-017.md) | step output 越界值——ATOMGIT_OUTPUT 写入 1 M |  |
| 110 | [REL-PATHS-01-014](case/REL-PATHS-01-014.md) | paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效 |  |
| 111 | [REL-PATHS-01-015](case/REL-PATHS-01-015.md) | paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断 |  |
| 112 | [REL-PREEMPT-01-005](case/REL-PREEMPT-01-005.md) | preemption events 边界值——配置 10 个应正常解析 |  |
| 113 | [REL-PREEMPT-01-006](case/REL-PREEMPT-01-006.md) | preemption events 越界值——配置 11 个应被拒绝 |  |
| 114 | [REL-PRESSURE-01-055](case/REL-PRESSURE-01-055.md) | 并发压测——concurrency.max=5 时触发 20 个 workf |  |
| 115 | [REL-PROJLIMIT-01-067](case/REL-PROJLIMIT-01-067.md) | 项目级 workflow 并发上限——200 条同时触发时全部完成无丢失 |  |
| 116 | [REL-PROJLIMIT-01-068](case/REL-PROJLIMIT-01-068.md) | 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排 |  |
| 117 | [REL-QUEUE-01-003](case/REL-QUEUE-01-003.md) | concurrency QUEUE 策略——超上限运行应排队等待 |  |
| 118 | [REL-RACE-01-048](case/REL-RACE-01-048.md) | 取消与 needs 条件竞态——job A 被取消时 job B(if: f |  |
| 119 | [REL-RERUN-01-011](case/REL-RERUN-01-011.md) | rerun 边界值——单条运行连续重新运行 3 次应全部成功 |  |
| 120 | [REL-RERUN-01-012](case/REL-RERUN-01-012.md) | rerun 越界值——尝试第 4 次重新运行应被系统拒绝 |  |
| 121 | [REL-RERUN-01-013](case/REL-RERUN-01-013.md) | rerun 6 小时年龄限制——超期运行不可重新运行 |  |
| 122 | [REL-RUNNER-01-049-V2](case/REL-RUNNER-01-049-V2.md) | Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存 |  |
| 123 | [REL-RUNNER-01-049](case/REL-RUNNER-01-049.md) | Runner 规格真实性——small/medium/large 实际 CP |  |
| 124 | [REL-SCHED-01-057](case/REL-SCHED-01-057.md) | 资源调度状态一致性——空闲 runner 存在时 job 不应死等 |  |
| 125 | [REL-STAGES-01-029](case/REL-STAGES-01-029.md) | stages fail_fast 机制——阶段内任一 job 失败应立即终止 |  |
| 126 | [REL-STEPS-01-042](case/REL-STEPS-01-042.md) | 超多 step——单 job 内 50 个 step 应全部串行执行无丢失 |  |
| 127 | [REL-TIMEOUT-01-007](case/REL-TIMEOUT-01-007.md) | job timeout 边界值——359 分钟运行应在 360 分钟边界前完 |  |
| 128 | [REL-TIMEOUT-01-008](case/REL-TIMEOUT-01-008.md) | job timeout 越界触发——361 分钟应在 360 分钟被强制终止 |  |
| 129 | [REL-TIMEOUT-01-010](case/REL-TIMEOUT-01-010.md) | 默认超时——未声明 timeout-minutes 运行 361 分钟应被强 |  |
| 130 | [SEC-CACHE-01-001](case/SEC-CACHE-01-001.md) | fork PR 写入的 cache 必须不可被主仓后续 workflow 读 |  |
| 131 | [SEC-COMM-01-001](case/SEC-COMM-01-001.md) | issue_comment / pull_request_comment 触 |  |
| 132 | [SEC-DEFPERM-01-001](case/SEC-DEFPERM-01-001.md) | ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效 |  |
| 133 | [SEC-DOS-01-001](case/SEC-DOS-01-001.md) | 大 artifact / 大 cache 必须受配额与边界限制 |  |
| 134 | [SEC-INJ-01-001](case/SEC-INJ-01-001.md) | 不可信 PR 标题不可直接插进 run 脚本导致命令注入 |  |
| 135 | [SEC-INJ-01-002](case/SEC-INJ-01-002.md) | 不可信分支名不可直接插进 run 脚本导致命令注入 |  |
| 136 | [SEC-INJ-01-003](case/SEC-INJ-01-003.md) | 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入 |  |
| 137 | [SEC-INJ-01-004](case/SEC-INJ-01-004.md) | 不可信 commit message 不可直接插进 run 脚本导致命令注入 |  |
| 138 | [SEC-INJ-01-005](case/SEC-INJ-01-005.md) | 表达式求值必须防止双重模板渲染（二次求值） |  |
| 139 | [SEC-MASK-01-001](case/SEC-MASK-01-001.md) | Secret 值在运行日志中必须被自动脱敏为 *** |  |
| 140 | [SEC-MASK-01-003](case/SEC-MASK-01-003.md) | Secret 日志脱敏不可通过 base64 编码绕过 |  |
| 141 | [SEC-MASK-01-004](case/SEC-MASK-01-004.md) | Secret 日志脱敏不可通过字符串拼接或插值绕过 |  |
| 142 | [SEC-MASK-01-005](case/SEC-MASK-01-005.md) | Secret 日志脱敏不可通过多行值输出绕过 |  |
| 143 | [SEC-MASK-01-006](case/SEC-MASK-01-006.md) | Secret 日志脱敏不可通过分片输出绕过 |  |
| 144 | [SEC-NAME-01-002](case/SEC-NAME-01-002.md) | 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secr |  |
| 145 | [SEC-NET-01-001](case/SEC-NET-01-001.md) | Runner 网络出站必须受控，防止 SSRF 与内网跳板 |  |
| 146 | [SEC-OIDC-01-001](case/SEC-OIDC-01-001.md) | OIDC / 短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案 |  |
| 147 | [SEC-PERM-01-001](case/SEC-PERM-01-001.md) | 显式声明的 permissions 必须在 job 级实际生效并限制 ATO |  |
| 148 | [SEC-PERM-01-002](case/SEC-PERM-01-002.md) | permissions 声明 read 时写操作被平台拒绝 |  |
| 149 | [SEC-PERM-01-003](case/SEC-PERM-01-003.md) | 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须 |  |
| 150 | [SEC-PERM-01-004](case/SEC-PERM-01-004.md) | 默认状态下写操作被 403 拒绝 |  |
| 151 | [SEC-RUN-01-001](case/SEC-RUN-01-001.md) | Job 结束后 workspace 与临时文件必须被彻底清理 |  |
| 152 | [SEC-RUN-01-002](case/SEC-RUN-01-002.md) | Runner 环境变量与共享目录必须跨 job 隔离 |  |
| 153 | [SEC-RUN-01-003](case/SEC-RUN-01-003.md) | 自托管 Runner 跨项目残留必须被隔离 |  |
| 154 | [SEC-TOCTOU-01-001](case/SEC-TOCTOU-01-001.md) | 审批后推送新 commit 不应被已授权特权运行执行 |  |
| 155 | [SEC-WCMD-01-001](case/SEC-WCMD-01-001.md) | Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的  |  |
| 156 | [SEC-WCMD-01-003](case/SEC-WCMD-01-003.md) | ATOMGIT_ENV 不被不可信输入污染提权 |  |
| 157 | [SEC-WCMD-01-004](case/SEC-WCMD-01-004.md) | ATOMGIT_OUTPUT 不被不可信输入污染提权 |  |
| 158 | [USE-ACT-01-002](case/USE-ACT-01-002.md) | 使用 actions/checkout@v4 时报错应给出迁移指引 |  |
| 159 | [USE-BADGE-01-001](case/USE-BADGE-01-001.md) | workflow 运行完成后状态徽标及时回写且语义清晰 |  |
| 160 | [USE-DEPR-01-002](case/USE-DEPR-01-002.md) | 使用 ::set-output 时应给出弃用警告与替代示例 |  |
| 161 | [USE-DIR-01-001](case/USE-DIR-01-001.md) | workflow 放置于 .gitcode/workflows/ 下可正常触 |  |
| 162 | [USE-EXPR-01-001](case/USE-EXPR-01-001.md) | 引用不存在的上下文属性时报错应包含原始表达式与错误类型 |  |
| 163 | [USE-EXPR-01-002](case/USE-EXPR-01-002.md) | 调用未知函数时报错应提示函数名错误与修正方向 |  |
| 164 | [USE-MASK-01-001](case/USE-MASK-01-001.md) | secret 脱敏文档描述与实际行为一致并给出缓解建议 |  |
| 165 | [USE-MASK-01-002](case/USE-MASK-01-002.md) | 直接 echo secrets 值时文档描述的绕过风险与实际一致 |  |
| 166 | [USE-MD-01-001](case/USE-MD-01-001.md) | ATOMGIT_STEP_SUMMARY 写入的 Markdown 正确渲染 |  |
| 167 | [USE-NEST-01-002](case/USE-NEST-01-002.md) | workflow_call 嵌套 2 层时应正常执行 |  |
| 168 | [USE-PERM-01-002](case/USE-PERM-01-002.md) | 使用 GitHub 权限域命名时报错应给出 GitCode 对照表 |  |
| 169 | [USE-TYPE-01-002](case/USE-TYPE-01-002.md) | 使用 GitHub types 命名 opened/synchronize  |  |
| 170 | [USE-YAML-01-001](case/USE-YAML-01-001.md) | 缺少必填字段 on 时报错应指出具体字段名与位置 |  |
| 171 | [USE-YAML-01-002](case/USE-YAML-01-002.md) | YAML 缩进错误时报错应指出具体行号与列号 |  |

## 完全不符 — 全部验证点未能由步骤产出（28 例）

| # | Case ID | 标题 | 原因 |
|---|---------|------|------|
| 1 | [COMP-BOUND-01-085](case/COMP-BOUND-01-085.md) | cron 表达式格式与位置边界验证 |  |
| 2 | [COMP-CACHE-01-003](case/COMP-CACHE-01-003.md) | fork PR 不应覆盖或污染主分支 cache |  |
| 3 | [COMP-RUNNER-01-003](case/COMP-RUNNER-01-003.md) | 不存在的标签组合导致 job 排队或失败 |  |
| 4 | [COMP-SCHEDULE-01-001](case/COMP-SCHEDULE-01-001.md) | 合法 cron 在默认分支按时触发 |  |
| 5 | [COMP-SCHEDULE-01-002](case/COMP-SCHEDULE-01-002.md) | 非默认分支的 schedule workflow 不应触发 |  |
| 6 | [COMP-SCHEDULE-01-003](case/COMP-SCHEDULE-01-003.md) | cron 间隔短于 5 分钟时被拒绝或降级 |  |
| 7 | [COMP-STAGES-01-001](case/COMP-STAGES-01-001.md) | stages 阶段间串行、阶段内 job 并行执行 |  |
| 8 | [COMPAT-COMM-01-002](case/COMPAT-COMM-01-002.md) | issue_comment types:created 不支持时应给出降级指 |  |
| 9 | [COMPAT-NEST-01-001](case/COMPAT-NEST-01-001.md) | workflow_call 嵌套层数 - 2 层正常执行 |  |
| 10 | [REL-FAIR-01-044](case/REL-FAIR-01-044.md) | 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调 |  |
| 11 | [REL-LATENCY-01-050](case/REL-LATENCY-01-050.md) | 调度延迟基准——queued→running P50/P95 等待时间 |  |
| 12 | [REL-NEST-01-023](case/REL-NEST-01-023.md) | workflow_call 嵌套边界——2 层嵌套调用应成功执行 |  |
| 13 | [REL-NEST-01-024](case/REL-NEST-01-024.md) | workflow_call 嵌套越界——3 层嵌套调用应被拒绝 |  |
| 14 | [REL-YAMLCACHE-01-060](case/REL-YAMLCACHE-01-060.md) | Workflow YAML 缓存失效——修改后无旧代码残留 |  |
| 15 | [USE-ANNOT-01-002](case/USE-ANNOT-01-002.md) | ::error:: 生成的 PR annotation 具备文件路径、行号与 |  |
| 16 | [USE-CTX-01-001](case/USE-CTX-01-001.md) | 使用 atomgit 上下文时表达式正常求值 |  |
| 17 | [USE-DEPR-01-001](case/USE-DEPR-01-001.md) | 使用 ATOMGIT_OUTPUT 文件协议时正常生效 |  |
| 18 | [USE-DIR-01-002](case/USE-DIR-01-002.md) | .github/workflows/ 下 workflow 未被识别时应给出 |  |
| 19 | [USE-DISP-01-002](case/USE-DISP-01-002.md) | workflow_dispatch 未提供参数但存在 default 时应使 |  |
| 20 | [USE-DOC-01-001](case/USE-DOC-01-001.md) | stages 与 post 概念在迁移文档中具备可发现性 |  |
| 21 | [USE-ENV-01-002](case/USE-ENV-01-002.md) | 引用 GITHUB_SHA 时日志应给出环境变量映射提示 |  |
| 22 | [USE-LOG-01-001](case/USE-LOG-01-001.md) | 多 step 日志按时间线组织且边界清晰 |  |
| 23 | [USE-OS-01-001](case/USE-OS-01-001.md) | runner.os 返回值与文档声明的平台支持一致 |  |
| 24 | [USE-PATH-01-001](case/USE-PATH-01-001.md) | paths 300 文件上限在文档与行为中一致且明示 |  |
| 25 | [USE-RES-01-001](case/USE-RES-01-001.md) | runtime-environment-variables.md 中不应出现 |  |
| 26 | [USE-UNKN-01-001](case/USE-UNKN-01-001.md) | 未知字段如 run-name 不应被静默忽略而应给出警告或错误 |  |
| 27 | [USE-UNKN-01-002](case/USE-UNKN-01-002.md) | 未知字段报错若识别为 GitHub 特有应追加迁移提示 |  |
| 28 | [USE-VARS-01-001](case/USE-VARS-01-001.md) | vars 上下文在文档与样本中的声明必须一致 |  |

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
