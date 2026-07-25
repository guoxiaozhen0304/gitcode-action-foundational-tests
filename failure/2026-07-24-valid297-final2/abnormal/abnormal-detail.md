# Abnormal 明细（非 PASS 非 FAIL）

> run: 2026-07-24-valid297-final2  |  84 条未执行

| # | case_id | 维度 | 判定 | 预期 | 实际错误 |
|---|---|---|---|---|---|
| 1 | COMP-ATOMGIT-01-047 | completeness | COMPILE_ERROR | atomgit 核心上下文属性可访问性 | intent_ref 格式不合规 |
| 2 | COMP-ATOMGIT-01-048 | completeness | COMPILE_ERROR | atomgit 事件相关属性可访问性 | intent_ref 格式不合规 |
| 3 | COMP-ATOMGIT-01-049 | completeness | COMPILE_ERROR | atomgit 边界格式校验 | intent_ref 格式不合规 |
| 4 | COMP-BOUND-01-084 | completeness | COMPILE_ERROR | 路径与分支过滤组合及否定模式边界验证 | intent_ref 格式不合规 |
| 5 | COMP-BOUND-01-086 | completeness | COMPILE_ERROR | 矩阵构建 include exclude 与单值边界验证 | intent_ref 格式不合规 |
| 6 | COMP-BOUND-01-087 | completeness | COMPILE_ERROR | 步骤输出与跨 job 传递边界验证 | intent_ref 格式不合规 |
| 7 | COMP-BOUND-01-088 | completeness | COMPILE_ERROR | 工作流命令 set-env add-path 与文件写入边界验证 | intent_ref 格式不合规 |
| 8 | COMP-CTX-01-051 | completeness | COMPILE_ERROR | 上下文在 workflow job step 各级注入验证 | intent_ref 格式不合规 |
| 9 | COMP-CTX-01-052 | completeness | COMPILE_ERROR | 上下文在条件表达式 if 中注入验证 | intent_ref 格式不合规 |
| 10 | COMP-CTX-01-053 | completeness | COMPILE_ERROR | 上下文在 Action 插件参数中注入验证 | intent_ref 格式不合规 |
| 11 | COMP-ENVCTX-01-050 | completeness | COMPILE_ERROR | env 优先级链 step 大于 job 大于 workflow | intent_ref 格式不合规 |
| 12 | COMP-EXPR-01-054 | completeness | COMPILE_ERROR | 字符串函数 contains startsWith endsWith 边界行为 | intent_ref 格式不合规 |
| 13 | COMP-EXPR-01-055 | completeness | COMPILE_ERROR | hashFiles 函数边界行为 | intent_ref 格式不合规 |
| 14 | COMP-EXPR-01-056 | completeness | COMPILE_ERROR | toJson 函数边界行为 | intent_ref 格式不合规 |
| 15 | COMP-EXPR-01-057 | completeness | COMPILE_ERROR | format substring replace 函数边界行为 | intent_ref 格式不合规 |
| 16 | COMP-JOB-01-066 | completeness | COMPILE_ERROR | job 必填字段 name runs-on steps 验证 | intent_ref 格式不合规 |
| 17 | COMP-JOB-01-067 | completeness | COMPILE_ERROR | job 可选字段 env if timeout-minutes needs 验证 | intent_ref 格式不合规 |
| 18 | COMP-JOB-01-068 | completeness | COMPILE_ERROR | job strategy 矩阵与 continue-on-error 验证 | intent_ref 格式不合规 |
| 19 | COMP-PUSH-01-003 | completeness | TIMEOUT | paths 过滤匹配前 300 个变更文件行为符合预期 | 触发后未等到 run（335秒） |
| 20 | COMP-RUNNER-01-080 | completeness | COMPILE_ERROR | runner 上下文属性可访问性验证 | intent_ref 格式不合规 |
| 21 | COMP-SCRIPT-01-081 | completeness | COMPILE_ERROR | 仓库内脚本执行与路径验证 | intent_ref 格式不合规 |
| 22 | COMP-SCRIPT-01-082 | completeness | COMPILE_ERROR | 脚本权限设置与直接执行验证 | intent_ref 格式不合规 |
| 23 | COMP-STEP-01-069 | completeness | COMPILE_ERROR | step 必填与核心字段 name run uses 验证 | intent_ref 格式不合规 |
| 24 | COMP-STEP-01-070 | completeness | COMPILE_ERROR | step 可选字段 id env if with 验证 | intent_ref 格式不合规 |
| 25 | COMP-STEP-01-071 | completeness | COMPILE_ERROR | step 执行控制 shell working-directory continue-on-error timeout-minutes 验证 | intent_ref 格式不合规 |
| 26 | COMP-SYSENV-01-059 | completeness | COMPILE_ERROR | ATOMGIT 系统环境变量关键变量存在性 | intent_ref 格式不合规 |
| 27 | COMP-SYSENV-01-060 | completeness | COMPILE_ERROR | ATOMGIT 系统环境变量值正确性 | intent_ref 格式不合规 |
| 28 | COMP-TRIG-01-072 | completeness | COMPILE_ERROR | push 事件关键字段与过滤验证 | intent_ref 格式不合规 |
| 29 | COMP-TRIG-01-073 | completeness | COMPILE_ERROR | pull_request 事件关键字段与 types 验证 | intent_ref 格式不合规 |
| 30 | COMP-TRIG-01-074 | completeness | COMPILE_ERROR | workflow_dispatch 事件关键字段与 inputs 验证 | intent_ref 格式不合规 |
| 31 | COMP-TRIG-01-076 | completeness | COMPILE_ERROR | issue_comment 事件关键字段与 types 验证 | intent_ref 格式不合规 |
| 32 | COMP-TRIG-01-077 | completeness | COMPILE_ERROR | pull_request_comment 事件关键字段与过滤验证 | intent_ref 格式不合规 |
| 33 | COMP-TRIG-01-078 | completeness | COMPILE_ERROR | 多事件组合与分支路径过滤验证 | intent_ref 格式不合规 |
| 34 | COMP-TRIG-01-079 | completeness | COMPILE_ERROR | 触发事件 types 取值与过滤边界验证 | intent_ref 格式不合规 |
| 35 | COMP-VARREF-01-083 | completeness | COMPILE_ERROR | YAML 表达式与 Shell 环境变量引用方式验证 | intent_ref 格式不合规 |
| 36 | COMP-WFLOW-01-061 | completeness | COMPILE_ERROR | workflow name 与 on 字段必填与类型验证 | intent_ref 格式不合规 |
| 37 | COMP-WFLOW-01-062 | completeness | COMPILE_ERROR | workflow env 与 defaults 字段验证 | intent_ref 格式不合规 |
| 38 | COMP-WFLOW-01-063 | completeness | COMPILE_ERROR | workflow concurrency 并发控制字段验证 | intent_ref 格式不合规 |
| 39 | COMP-WFLOW-01-064 | completeness | COMPILE_ERROR | workflow stages 阶段结构字段验证 | intent_ref 格式不合规 |
| 40 | COMPAT-COMM-01-001 | compatibility | COMPILE_ERROR | issue_comment types 命名差异 - GitCode 合法 types 应被接受 | intent_ref 格式不合规 |
| 41 | COMPAT-COMM-01-002 | compatibility | COMPILE_ERROR | issue_comment types:created 不支持时应给出降级指引 | intent_ref 格式不合规 |
| 42 | COMPAT-CONTAINER-01-001 | compatibility | COMPILE_ERROR | container 字段不被支持时应明确报错而非静默忽略 | intent_ref 格式不合规 |
| 43 | COMPAT-CONTAINER-01-002 | compatibility | COMPILE_ERROR | container 自定义镜像被拒绝时应给出替代指引 | intent_ref 格式不合规 |
| 44 | COMPAT-DEPR-01-001 | compatibility | COMPILE_ERROR | ::set-env:: 废弃命令应被拒绝或给出迁移指引 | intent_ref 格式不合规 |
| 45 | COMPAT-DEPR-01-002 | compatibility | COMPILE_ERROR | ::add-path:: 废弃命令应被拒绝或给出迁移指引 | intent_ref 格式不合规 |
| 46 | COMPAT-DIR-01-003 | compatibility | TIMEOUT | .github/workflows 目录不应被识别且应给出迁移提示 | 触发后未等到 run（421秒） |
| 47 | COMPAT-MATRIX-01-003 | compatibility | COMPILE_ERROR | matrix 三维展开不被支持时的差异 | intent_ref 格式不合规 |
| 48 | COMPAT-MATRIX-01-004 | compatibility | COMPILE_ERROR | matrix include 无基础变量不被支持时的差异 | intent_ref 格式不合规 |
| 49 | COMPAT-MATRIX-01-005 | compatibility | COMPILE_ERROR | matrix exclude 全排除不被支持时的差异 | intent_ref 格式不合规 |
| 50 | COMPAT-NEST-01-001 | compatibility | COMPILE_ERROR | workflow_call 嵌套层数 - 2 层正常执行 | runs-on 格式不合规（需数组格式） |
| 51 | COMPAT-NEST-01-002 | compatibility | COMPILE_ERROR | workflow_call 嵌套层数 - 3 层越界应报错 | runs-on 格式不合规（需数组格式） |
| 52 | COMPAT-OUTPUT-01-001 | compatibility | COMPILE_ERROR | 跨 Job 引用未声明 output 时返回空值的差异 | intent_ref 格式不合规 |
| 53 | COMPAT-PERM-01-002 | compatibility | INCONCLUSIVE | 未声明 permissions 时 fork PR 写操作隔离 | fork_pr 需第二 GitCode 账号 |
| 54 | COMPAT-PR-01-006 | compatibility | COMPILE_ERROR | PR 目标分支过滤行为差异 | intent_ref 格式不合规 |
| 55 | COMPAT-RUNNER-01-003 | compatibility | COMPILE_ERROR | self-hosted 标签不被支持时应明确报错 | intent_ref 格式不合规 |
| 56 | COMPAT-RUNNER-01-006 | compatibility | COMPILE_ERROR | Runner 未预装 Java 工具链与 GitHub 差异 | intent_ref 格式不合规 |
| 57 | COMPAT-TARGET-01-003 | compatibility | TIMEOUT | pull_request_target 默认 types 与 GitHub 差异 | 触发后未等到 run（398秒） |
| 58 | COMPAT-TOKEN-01-001 | compatibility | ENV_ERROR | ATOMGIT_TOKEN 应正确返回有效令牌 | dispatch API 拒绝（HTTP 400） |
| 59 | COMPAT-TOKEN-01-002 | compatibility | ENV_ERROR | GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射 | dispatch API 拒绝（HTTP 400） |
| 60 | COMPAT-WCMD-01-001 | compatibility | COMPILE_ERROR | ::add-mask:: 不被支持时应静默降级而非报错 | intent_ref 格式不合规 |
| 61 | COMPAT-WCMD-01-002 | compatibility | COMPILE_ERROR | ::group:: 不被支持时应静默降级而非报错 | intent_ref 格式不合规 |
| 62 | COMPAT-WCMD-01-003 | compatibility | COMPILE_ERROR | ::stop-commands:: 不被支持时应静默降级而非报错 | intent_ref 格式不合规 |
| 63 | REL-CHILDSTATE-01-064-V2 | reliability | COMPILE_ERROR | 子任务状态传播——workflow_call 未拉起时父 workflow 不应假阳性完成 | runs-on 格式不合规（需数组格式） |
| 64 | REL-CHILDSTATE-01-064 | reliability | COMPILE_ERROR | 子任务状态传播——workflow_call 失败时父 workflow 不应假阳性完成 | runs-on 格式不合规（需数组格式） |
| 65 | REL-DISK-01-018 | reliability | TIMEOUT | Runner 磁盘边界——small runner 写入 49 GB 应成功 | 触发后未等到 run（304秒） |
| 66 | REL-FAULT-01-034 | reliability | COMPILE_ERROR | 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss | fault_injection 用例 teardown.reset 不得为 none |
| 67 | REL-FAULT-01-035 | reliability | COMPILE_ERROR | 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误 | fault_injection 用例 teardown.reset 不得为 none |
| 68 | REL-FLOOD-01-036 | reliability | TIMEOUT | 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失 | 触发后未等到 run（343秒） |
| 69 | REL-FLOOD-01-037 | reliability | TIMEOUT | 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃 | 触发后未等到 run（341秒） |
| 70 | REL-LOG-01-040 | reliability | TIMEOUT | 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看 | 触发后未等到 run（424秒） |
| 71 | REL-LONG-01-043 | reliability | TIMEOUT | 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常 | 触发后未等到 run（332秒） |
| 72 | REL-NEST-01-023 | reliability | COMPILE_ERROR | workflow_call 嵌套边界——2 层嵌套调用应成功执行 | runs-on 格式不合规（需数组格式） |
| 73 | REL-NEST-01-024 | reliability | COMPILE_ERROR | workflow_call 嵌套越界——3 层嵌套调用应被拒绝 | runs-on 格式不合规（需数组格式） |
| 74 | REL-OUTPUT-01-017 | reliability | COMPILE_ERROR | step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错 | job 'test' step name 含非法字符 ['+']: 'write 1MB+1 output' |
| 75 | REL-PATHS-01-014 | reliability | TIMEOUT | paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效 | 触发后未等到 run（345秒） |
| 76 | REL-PATHS-01-015 | reliability | TIMEOUT | paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断 | 触发后未等到 run（342秒） |
| 77 | REL-TIMEOUT-01-007 | reliability | TIMEOUT | job timeout 边界值——359 分钟运行应在 360 分钟边界前完成 | 触发后未等到 run（366秒） |
| 78 | REL-TIMEOUT-01-008 | reliability | TIMEOUT | job timeout 越界触发——361 分钟应在 360 分钟被强制终止 | 触发后未等到 run（359秒） |
| 79 | REL-TIMEOUT-01-010 | reliability | TIMEOUT | 默认超时——未声明 timeout-minutes 运行 361 分钟应被强制终止 | 触发后未等到 run（301秒） |
| 80 | SEC-COMM-01-001 | security | TIMEOUT | issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过 | 触发后未等到 run（374秒） |
| 81 | SEC-INJ-01-003 | security | TIMEOUT | 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入 | 触发后未等到 run（392秒） |
| 82 | SEC-TOCTOU-01-002 | security | TIMEOUT | 评论触发不应绕过代码固定与 PR 审批 | 触发后未等到 run（310秒） |
| 83 | USE-DISP-01-001 | usability | ENV_ERROR | workflow_dispatch 必填参数未提供时应给出明确校验错误 | dispatch API 拒绝（HTTP 400） |
| 84 | USE-INPT-01-001 | usability | ENV_ERROR | 使用 string 类型 input 时正常通过校验 | dispatch API 拒绝（HTTP 400） |

> 合计: 84 条