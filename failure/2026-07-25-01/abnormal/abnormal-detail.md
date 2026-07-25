# Abnormal明细

## COMPILE_ERROR（7条）

> 7条 | preflight拦截

| # | case_id | 维度 | 预期 | 错误 |
|---|---|---|---|---|
| 1 | COMP-SCHEDULE-01-001 | completeness | 合法 cron 在默认分支按时触发 | cron表达式不合法 |
| 2 | COMP-SCHEDULE-01-002 | completeness | 非默认分支的 schedule workflow 不应触发 | cron表达式不合法 |
| 3 | COMP-SCHEDULE-01-003 | completeness | cron 间隔短于 5 分钟时被拒绝或降级 | cron表达式不合法 |
| 4 | COMP-WFLOW-01-064 | completeness | workflow stages 阶段结构字段验证 | 缺jobs或jobs为空 |
| 5 | REL-FAULT-01-034 | reliability | 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss | fault_injection与teardown冲突 |
| 6 | REL-FAULT-01-035 | reliability | 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误 | fault_injection与teardown冲突 |
| 7 | REL-OUTPUT-01-017 | reliability | step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错 | step name含非法字符 |

## ENV_ERROR（11条）

> 11条 | dispatch API拒绝

| # | case_id | 维度 | 预期 | 错误 |
|---|---|---|---|---|
| 1 | COMP-TRIG-01-074 | completeness | workflow_dispatch 事件关键字段与 inputs 验证 | dispatch API拒绝(HTTP 400) |
| 2 | COMPAT-NEST-01-001 | compatibility | workflow_call 嵌套层数 - 2 层正常执行 | dispatch API拒绝(HTTP 400) |
| 3 | COMPAT-NEST-01-002 | compatibility | workflow_call 嵌套层数 - 3 层越界应报错 | dispatch API拒绝(HTTP 400) |
| 4 | COMPAT-TOKEN-01-001 | compatibility | ATOMGIT_TOKEN 应正确返回有效令牌 | dispatch API拒绝(HTTP 400) |
| 5 | COMPAT-TOKEN-01-002 | compatibility | GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射 | dispatch API拒绝(HTTP 400) |
| 6 | REL-CHILDSTATE-01-064-V2 | reliability | 子任务状态传播——workflow_call 未拉起时父 workflow 不应假阳性完成 | dispatch API拒绝(HTTP 400) |
| 7 | REL-CHILDSTATE-01-064 | reliability | 子任务状态传播——workflow_call 失败时父 workflow 不应假阳性完成 | dispatch API拒绝(HTTP 400) |
| 8 | REL-NEST-01-023 | reliability | workflow_call 嵌套边界——2 层嵌套调用应成功执行 | dispatch API拒绝(HTTP 400) |
| 9 | REL-NEST-01-024 | reliability | workflow_call 嵌套越界——3 层嵌套调用应被拒绝 | dispatch API拒绝(HTTP 400) |
| 10 | USE-DISP-01-001 | usability | workflow_dispatch 必填参数未提供时应给出明确校验错误 | dispatch API拒绝(HTTP 400) |
| 11 | USE-INPT-01-001 | usability | 使用 string 类型 input 时正常通过校验 | dispatch API拒绝(HTTP 400) |

## TIMEOUT（27条）

> 27条 | 未等到run

| # | case_id | 维度 | 预期 | 错误 |
|---|---|---|---|---|
| 1 | COMP-BOUND-01-084 | completeness | 路径与分支过滤组合及否定模式边界验证 | 未等到run(347s) |
| 2 | COMP-PUSH-01-003 | completeness | paths 过滤匹配前 300 个变更文件行为符合预期 | 未等到run(308s) |
| 3 | COMP-TRIG-01-076 | completeness | issue_comment 事件关键字段与 types 验证 | 未等到run(310s) |
| 4 | COMP-TRIG-01-077 | completeness | pull_request_comment 事件关键字段与过滤验证 | 未等到run(300s) |
| 5 | COMP-TRIG-01-078 | completeness | 多事件组合与分支路径过滤验证 | 未等到run(365s) |
| 6 | COMPAT-COMM-01-001 | compatibility | issue_comment types 命名差异 - GitCode 合法 types 应被接受 | 未等到run(311s) |
| 7 | COMPAT-COMM-01-002 | compatibility | issue_comment types:created 不支持时应给出降级指引 | 未等到run(300s) |
| 8 | COMPAT-CONTAINER-01-002 | compatibility | container 自定义镜像被拒绝时应给出替代指引 | 未等到run(301s) |
| 9 | COMPAT-DIR-01-003 | compatibility | .github/workflows 目录不应被识别且应给出迁移提示 | 未等到run(387s) |
| 10 | COMPAT-MATRIX-01-005 | compatibility | matrix exclude 全排除不被支持时的差异 | 未等到run(301s) |
| 11 | COMPAT-TARGET-01-003 | compatibility | pull_request_target 默认 types 与 GitHub 差异 | 未等到run(380s) |
| 12 | REL-DISK-01-018 | reliability | Runner 磁盘边界——small runner 写入 49 GB 应成功 | 未等到run(301s) |
| 13 | REL-DISK-01-019 | reliability | Runner 磁盘越界——small runner 写入 51 GB 应失败并报磁盘满 | 未等到run(333s) |
| 14 | REL-FAULT-01-033 | reliability | 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满 | 未等到run(310s) |
| 15 | REL-FLOOD-01-036 | reliability | 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失 | 未等到run(482s) |
| 16 | REL-FLOOD-01-037 | reliability | 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃 | 未等到run(478s) |
| 17 | REL-LOG-01-040 | reliability | 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看 | 未等到run(369s) |
| 18 | REL-LONG-01-043 | reliability | 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常 | 未等到run(745s) |
| 19 | REL-OUTPUT-01-016 | reliability | step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递 | 未等到run(319s) |
| 20 | REL-PATHS-01-014 | reliability | paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效 | 未等到run(589s) |
| 21 | REL-PATHS-01-015 | reliability | paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断 | 未等到run(497s) |
| 22 | REL-TIMEOUT-01-007 | reliability | job timeout 边界值——359 分钟运行应在 360 分钟边界前完成 | 未等到run(335s) |
| 23 | REL-TIMEOUT-01-008 | reliability | job timeout 越界触发——361 分钟应在 360 分钟被强制终止 | 未等到run(404s) |
| 24 | REL-TIMEOUT-01-010 | reliability | 默认超时——未声明 timeout-minutes 运行 361 分钟应被强制终止 | 未等到run(384s) |
| 25 | SEC-COMM-01-001 | security | issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过 | 未等到run(336s) |
| 26 | SEC-INJ-01-003 | security | 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入 | 未等到run(369s) |
| 27 | SEC-TOCTOU-01-002 | security | 评论触发不应绕过代码固定与 PR 审批 | 未等到run(419s) |

## INCONCLUSIVE（1条）

> 1条

| # | case_id | 维度 | 预期 | 错误 |
|---|---|---|---|---|
| 1 | COMPAT-PERM-01-002 | compatibility | 未声明 permissions 时 fork PR 写操作隔离 | fork_pr需第二账号 |
