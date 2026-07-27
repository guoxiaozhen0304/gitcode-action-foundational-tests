# 断言-步骤一致性报告

**日期**: 2026-07-27
**数据源**: phase01/runs/2026-07-27-01/cases/yaml/
**用例总数**: 498

---

## 1. 总览

| 评级 | 数量 | 说明 |
|------|:---:|------|
| 断言一致 | 268 | 所有验证点可被步骤真实覆盖 |
| 部分不符 | 147 | 部分验证点为 VACUOUS / MISSING_SOURCE / UNVERIFIABLE 等 |
| 完全不符 | 83 | 全部验证点未能由步骤产出 |
| **合计** | **498** | |

| 维度 | 断言一致 | 部分不符 | 完全不符 | 合计 |
|------|:---:|:---:|:---:|:---:|
| 完备性 | 49 | 30 | 31 | 110 |
| 兼容性 | 39 | 82 | 16 | 137 |
| 可靠性 | 90 | 14 | 1 | 105 |
| 安全性 | 64 | 3 | 0 | 67 |
| 易用性 | 26 | 18 | 35 | 79 |

---

## 2. 判定分布

| 判定 | 数量 | 说明 |
|------|:---:|------|
| COVERED | 1 | 步骤覆盖验证点（含平台验证型用例） |
| GENUINE | 525 | 步骤真实执行被测功能，产出断言所需输出 |
| IMPOSSIBLE | 27 | 期望 !=success 但无步骤可能失败 |
| LLM_DEPENDENT | 404 | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| MISSING_SOURCE | 58 | 无任何步骤产出断言期望的字符串 |
| STATUS_GUARANTEED | 34 | run_status=success 为必然结果（所有步骤 trivial） |
| UNEXERCISED | 8 | 安全断言无对应步骤使用 secret |
| VACUOUS | 47 | 步骤仅 echo 期望字符串，未执行功能（假测试） |

---

## 3. 断言一致 — 所有验证点真实覆盖（268 例）

| # | Case ID | 标题 |
|---|---------|------|
| 1 | [COMP-ACT-01-001](case/COMP-ACT-01-001.md) | action inputs.required 未传参时平台不自动校验 |
| 2 | [COMP-ACT-01-002](case/COMP-ACT-01-002.md) | 含连字符 input_id 的 INPUT_ 环境变量命名裁定 |
| 3 | [COMP-ACT-01-003](case/COMP-ACT-01-003.md) | 手动取消时 action runs.post 由调度服务调用 |
| 4 | [COMP-ARTIFACT-01-001](case/COMP-ARTIFACT-01-001.md) | artifact 可在同 workflow 的 job 间正确传递 |
| 5 | [COMP-ARTIFACT-01-002](case/COMP-ARTIFACT-01-002.md) | 下载全部制品功能正常 |
| 6 | [COMP-ARTIFACT-01-003](case/COMP-ARTIFACT-01-003.md) | artifact 保留期设置生效 |
| 7 | [COMP-BOUND-01-086](case/COMP-BOUND-01-086.md) | 矩阵构建 include exclude 与单值边界验证 |
| 8 | [COMP-CACHE-01-001](case/COMP-CACHE-01-001.md) | cache hit 时恢复缓存内容正确 |
| 9 | [COMP-CACHE-01-002](case/COMP-CACHE-01-002.md) | restore-keys 前缀匹配兜底生效 |
| 10 | [COMP-CACHE-01-003](case/COMP-CACHE-01-003.md) | fork PR 不应覆盖或污染主分支 cache |
| 11 | [COMP-CTX-01-053](case/COMP-CTX-01-053.md) | 上下文在 Action 插件参数中注入验证 |
| 12 | [COMP-CTX-01-054](case/COMP-CTX-01-054.md) | pull_request 触发下 inputs 上下文求值裁定 |
| 13 | [COMP-DIR-01-002](case/COMP-DIR-01-002.md) | .github/workflows/ 下的 YAML 不被识别为 workflow |
| 14 | [COMP-EXPR-01-054](case/COMP-EXPR-01-054.md) | 字符串函数 contains startsWith endsWith 边界行为 |
| 15 | [COMP-EXPR-01-055](case/COMP-EXPR-01-055.md) | hashFiles 函数边界行为 |
| 16 | [COMP-EXPR-01-058](case/COMP-EXPR-01-058.md) | 表达式运算符与优先级边界行为 |
| 17 | [COMP-ISOLATION-01-001](case/COMP-ISOLATION-01-001.md) | 同一 workflow 先后 job 的文件系统相互隔离 |
| 18 | [COMP-ISOLATION-01-002](case/COMP-ISOLATION-01-002.md) | 环境变量不跨 job 泄漏 |
| 19 | [COMP-ISOLATION-01-004](case/COMP-ISOLATION-01-004.md) | 托管 Runner 上特权 options 与敏感路径挂载的边界核查 |
| 20 | [COMP-PERMS-01-001](case/COMP-PERMS-01-001.md) | permissions 空对象时 ATOMGIT_TOKEN 仅 repository read |
| 21 | [COMP-PERMS-01-002](case/COMP-PERMS-01-002.md) | 声明 repository write 后 TOKEN 可推送代码 |
| 22 | [COMP-PERMS-01-003](case/COMP-PERMS-01-003.md) | fork PR 的 pull_request 下声明 write 仍仅 read |
| 23 | [COMP-PR-01-001](case/COMP-PR-01-001.md) | fork PR 触发 pull_request 时不可读取项目 secrets |
| 24 | [COMP-PR-01-002](case/COMP-PR-01-002.md) | pull_request_target 可访问 secrets 且 TOKEN 拥有写权限 |
| 25 | [COMP-PR-01-003](case/COMP-PR-01-003.md) | fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限 |
| 26 | [COMP-PR-01-004](case/COMP-PR-01-004.md) | pre-merge ref 在 PR 存续期可解析且语义裁定 |
| 27 | [COMP-PR-01-005](case/COMP-PR-01-005.md) | 源分支更新后 pre-merge ref 指向刷新验证 |
| 28 | [COMP-PUSH-01-002](case/COMP-PUSH-01-002.md) | 不匹配 branches 的 push 不触发 workflow |
| 29 | [COMP-PUSH-01-003](case/COMP-PUSH-01-003.md) | paths 过滤匹配前 300 个变更文件行为符合预期 |
| 30 | [COMP-RERUN-01-001](case/COMP-RERUN-01-001.md) | rerun 后 atomgit.sha 保持原始值 run_number 递增 |
| 31 | [COMP-RERUN-01-002](case/COMP-RERUN-01-002.md) | 第 4 次 rerun 应被系统拒绝 |
| 32 | [COMP-RERUN-01-003](case/COMP-RERUN-01-003.md) | 超过 6 小时的运行不可 rerun |
| 33 | [COMP-RUNNER-01-080](case/COMP-RUNNER-01-080.md) | runner 上下文属性可访问性验证 |
| 34 | [COMP-RUNNER-01-081](case/COMP-RUNNER-01-081.md) | 四段式 runs-on（codearts-hosted 首段）调度行为裁定 |
| 35 | [COMP-SCHEDULE-01-002](case/COMP-SCHEDULE-01-002.md) | 非默认分支的 schedule workflow 不应触发 |
| 36 | [COMP-SCHEDULE-01-003](case/COMP-SCHEDULE-01-003.md) | cron 间隔短于 5 分钟时被拒绝或降级 |
| 37 | [COMP-SCRIPT-01-082](case/COMP-SCRIPT-01-082.md) | 脚本权限设置与直接执行验证 |
| 38 | [COMP-STAGES-01-002](case/COMP-STAGES-01-002.md) | fail_fast true 时 stage 内任一 job 失败终止同阶段其余 job |
| 39 | [COMP-STAGES-01-003](case/COMP-STAGES-01-003.md) | post.run_always true 时 workflow 失败仍执行 post |
| 40 | [COMP-SUMMARY-01-001](case/COMP-SUMMARY-01-001.md) | ATOMGIT_STEP_SUMMARY Markdown 表格与标题正确渲染 |
| 41 | [COMP-SUMMARY-01-002](case/COMP-SUMMARY-01-002.md) | summary 中不应暴露系统内部路径 |
| 42 | [COMP-TRIG-01-073](case/COMP-TRIG-01-073.md) | pull_request 事件关键字段与 types 验证 |
| 43 | [COMP-TRIG-01-074](case/COMP-TRIG-01-074.md) | workflow_dispatch 事件关键字段与 inputs 验证 |
| 44 | [COMP-TRIG-01-075](case/COMP-TRIG-01-075.md) | schedule 事件关键字段与 cron 格式验证 |
| 45 | [COMP-TRIG-01-076](case/COMP-TRIG-01-076.md) | issue_comment 事件关键字段与 types 验证 |
| 46 | [COMP-TRIG-01-077](case/COMP-TRIG-01-077.md) | pull_request_comment 事件关键字段与过滤验证 |
| 47 | [COMP-UNKNOWN-01-001](case/COMP-UNKNOWN-01-001.md) | 包含未知顶层字段的 workflow 触发 YAML 校验失败 |
| 48 | [COMP-UNKNOWN-01-002](case/COMP-UNKNOWN-01-002.md) | 不应静默忽略未知字段导致用户误以为配置生效 |
| 49 | [COMP-UNKNOWN-01-005](case/COMP-UNKNOWN-01-005.md) | 顶层 inputs 与 manual_override 字段的实际处理记录 |
| 50 | [COMPAT-ACTION-01-001](case/COMPAT-ACTION-01-001.md) | checkout 短名等价性——ref 参数支持 |
| 51 | [COMPAT-ACTION-01-002](case/COMPAT-ACTION-01-002.md) | checkout 短名等价性——path 参数支持 |
| 52 | [COMPAT-ARTIFACT-01-001](case/COMPAT-ARTIFACT-01-001.md) | upload/download-artifact 跨 job 传递等价性 |
| 53 | [COMPAT-ARTIFACT-01-002](case/COMPAT-ARTIFACT-01-002.md) | upload-artifact 保留期行为等价性 |
| 54 | [COMPAT-CACHE-01-002](case/COMPAT-CACHE-01-002.md) | cache 行为等价性——fork PR 写隔离 |
| 55 | [COMPAT-CTX-01-002](case/COMPAT-CTX-01-002.md) | 使用 atomgit.ref 上下文应正确返回触发引用 |
| 56 | [COMPAT-CTX-01-004](case/COMPAT-CTX-01-004.md) | atomgit.actor 规格自相矛盾的实测仲裁 |
| 57 | [COMPAT-DIR-01-001](case/COMPAT-DIR-01-001.md) | 工作流目录差异——.gitcode/workflows/ 正常识别 |
| 58 | [COMPAT-EXPR-01-003](case/COMPAT-EXPR-01-003.md) | failure() 与 failed 关键字的处理行为差异 |
| 59 | [COMPAT-EXPR-01-004](case/COMPAT-EXPR-01-004.md) | contains 表达式大小写敏感边界 |
| 60 | [COMPAT-EXPR-01-005](case/COMPAT-EXPR-01-005.md) | contains 表达式空值与空字符串边界 |
| 61 | [COMPAT-EXPR-01-006](case/COMPAT-EXPR-01-006.md) | hashFiles 表达式无匹配路径边界 |
| 62 | [COMPAT-EXPR-01-007](case/COMPAT-EXPR-01-007.md) | hashFiles 表达式多路径组合边界 |
| 63 | [COMPAT-EXPR-01-008](case/COMPAT-EXPR-01-008.md) | toJson 表达式输出格式差异（pretty-print vs compact） |
| 64 | [COMPAT-EXPR-01-009](case/COMPAT-EXPR-01-009.md) | loose equality 跨类型强制求值差异 |
| 65 | [COMPAT-EXPR-01-010](case/COMPAT-EXPR-01-010.md) | loose equality null 与空字符串及零的等价性差异 |
| 66 | [COMPAT-EXPR-01-011](case/COMPAT-EXPR-01-011.md) | join() 函数缺失时的降级行为 |
| 67 | [COMPAT-EXPR-01-012](case/COMPAT-EXPR-01-012.md) | fromJSON() 函数缺失时的降级行为 |
| 68 | [COMPAT-EXPR-01-016](case/COMPAT-EXPR-01-016.md) | format() 花括号转义与字符串字面量引号规则边界 |
| 69 | [COMPAT-MASK-01-001](case/COMPAT-MASK-01-001.md) | 直接 echo secrets 值应在日志中被脱敏 |
| 70 | [COMPAT-NEEDS-01-002](case/COMPAT-NEEDS-01-002.md) | needs 上游 job 被跳过时的 result 取值语义 |
| 71 | [COMPAT-NEEDS-01-003](case/COMPAT-NEEDS-01-003.md) | matrix 上游 job 的 needs outputs 聚合语义与未声明 output 边界 |
| 72 | [COMPAT-PERM-01-001](case/COMPAT-PERM-01-001.md) | 未声明 permissions 时默认 TOKEN 读操作权限范围 |
| 73 | [COMPAT-PERM-01-002](case/COMPAT-PERM-01-002.md) | 未声明 permissions 时 fork PR 写操作隔离 |
| 74 | [COMPAT-PERM-01-004](case/COMPAT-PERM-01-004.md) | permissions 命名差异——GitCode repository 权限项正常生效 |
| 75 | [COMPAT-PR-01-001](case/COMPAT-PR-01-001.md) | pull_request types 命名差异 - GitCode 合法 types 应被接受 |
| 76 | [COMPAT-PR-01-002](case/COMPAT-PR-01-002.md) | pull_request types 命名差异 - GitHub 风格 types 应报错 |
| 77 | [COMPAT-PR-01-009](case/COMPAT-PR-01-009.md) | pull_request 触发时 atomgit.sha/ref 的代码版本语义（对齐 GitHub merg |
| 78 | [COMPAT-RUNNER-01-001](case/COMPAT-RUNNER-01-001.md) | runner.os 在 Linux Runner 上应返回 Linux |
| 79 | [COMPAT-RUNNER-01-002](case/COMPAT-RUNNER-01-002.md) | runner.arch 在 x86_64 Runner 上应返回 X64 |
| 80 | [COMPAT-RUNNER-01-007](case/COMPAT-RUNNER-01-007.md) | Runner 预装工具链规格清单与实测全面对账 |
| 81 | [COMPAT-RUNNER-01-008](case/COMPAT-RUNNER-01-008.md) | 与 GitHub hosted image 的关键能力差距（docker 守护进程、浏览器）探测 |
| 82 | [COMPAT-RUNSON-01-001](case/COMPAT-RUNSON-01-001.md) | runs-on 标签体系——三段式数组正常匹配 |
| 83 | [COMPAT-SCHEDULE-01-004](case/COMPAT-SCHEDULE-01-004.md) | schedule 生命周期语义（自动停用策略与触发延迟可观测性）确认 |
| 84 | [COMPAT-SHELL-01-001](case/COMPAT-SHELL-01-001.md) | 默认 shell 隐式行为差异 - 未显式声明时是否为 bash |
| 85 | [COMPAT-SHELL-01-002](case/COMPAT-SHELL-01-002.md) | 默认工作目录隐式行为差异 - 未显式声明时是否为仓库根目录 |
| 86 | [COMPAT-TARGET-01-001](case/COMPAT-TARGET-01-001.md) | pull_request_target 默认 checkout 应为 base 分支而非 head 分支 |
| 87 | [COMPAT-TARGET-01-002](case/COMPAT-TARGET-01-002.md) | pull_request_target 在 fork 场景下应保持 secret 隔离 |
| 88 | [COMPAT-VARS-01-001](case/COMPAT-VARS-01-001.md) | vars 上下文若支持应正确返回值 |
| 89 | [REL-API-01-065](case/REL-API-01-065.md) | API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据 |
| 90 | [REL-ART-01-041](case/REL-ART-01-041.md) | 超大 artifact——100 MB artifact 上传后下游 job 应成功下载 |
| 91 | [REL-ART-01-042](case/REL-ART-01-042.md) | artifact 大小上限探测——2GB 上传应完整成功（MD5 一致）或上传阶段明确拒绝 |
| 92 | [REL-ARTCONC-01-063](case/REL-ARTCONC-01-063.md) | 制品并发写一致性——多 job 同时 upload-artifact 同名 artifact |
| 93 | [REL-ARTPERF-01-053](case/REL-ARTPERF-01-053.md) | 制品传输性能——100MB artifact 上传下载耗时 |
| 94 | [REL-ARTPERF-01-053-V2](case/REL-ARTPERF-01-053-V2.md) | 制品传输性能——1GB artifact 上传下载耗时 |
| 95 | [REL-BIGRUNNER-01-066](case/REL-BIGRUNNER-01-066.md) | 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率 |
| 96 | [REL-CACHE-01-046](case/REL-CACHE-01-046.md) | 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰 |
| 97 | [REL-CACHE-01-047](case/REL-CACHE-01-047.md) | cache 容量上限探测——500MB/1GB/2GB 单 cache 的接受/拒绝语义 |
| 98 | [REL-CACHE-01-048](case/REL-CACHE-01-048.md) | cache 同 key 并发写一致性——3 方并行写同一 key 不得产生混合/损坏内容 |
| 99 | [REL-CANCEL-01-028](case/REL-CANCEL-01-028.md) | 手动取消 workflow——运行中取消时 always() cleanup step 仍应执行 |
| 100 | [REL-CANCEL-01-029](case/REL-CANCEL-01-029.md) | 多并发 run 中取消指定 run——取消应按 run_id 寻址而非栈序误杀最新一条 |
| 101 | [REL-CANCELREL-01-061](case/REL-CANCELREL-01-061.md) | 取消操作可靠性——queued/running/post 各阶段取消状态正确过渡 |
| 102 | [REL-CHILDSTATE-01-064](case/REL-CHILDSTATE-01-064.md) | 子任务状态传播——workflow_call 失败时父 workflow 不应假阳性完成 |
| 103 | [REL-CHILDSTATE-01-064-V2](case/REL-CHILDSTATE-01-064-V2.md) | 子任务状态传播——workflow_call 未拉起时父 workflow 不应假阳性完成 |
| 104 | [REL-CONC-01-001](case/REL-CONC-01-001.md) | concurrency.max=5 时同时触发 5 个运行应全部进入执行态 |
| 105 | [REL-CONC-01-002](case/REL-CONC-01-002.md) | concurrency.max=6 配置应被系统拒绝 |
| 106 | [REL-CONTINUE-01-030](case/REL-CONTINUE-01-030.md) | continue-on-error=true——job 失败后 workflow 不应终止 |
| 107 | [REL-CPU-01-022](case/REL-CPU-01-022.md) | Runner CPU 饱和——small runner 运行 4 个 CPU 密集型进程应完成但耗时延长 |
| 108 | [REL-DEBOUNCE-01-001](case/REL-DEBOUNCE-01-001.md) | 触发幂等——同分支 10 秒内连续 5 次 push 的 run 记录应与事件一一对账 |
| 109 | [REL-DEBOUNCE-01-002](case/REL-DEBOUNCE-01-002.md) | 触发幂等——10 秒内推送 10 个 tag 的 run 记录应与 tag 事件 100% 可解释 |
| 110 | [REL-DISK-01-018](case/REL-DISK-01-018.md) | Runner 磁盘边界——small runner 写入 49 GB 应成功 |
| 111 | [REL-FAULT-01-032](case/REL-FAULT-01-032.md) | 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误 |
| 112 | [REL-FAULT-01-034](case/REL-FAULT-01-034.md) | 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss |
| 113 | [REL-FAULT-01-035](case/REL-FAULT-01-035.md) | 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务错误 |
| 114 | [REL-FAULT-01-037](case/REL-FAULT-01-037.md) | 故障注入——runner 与平台心跳分区 300 秒，行为应确定可归因（续跑或明确失联失败） |
| 115 | [REL-FAULT-01-038](case/REL-FAULT-01-038.md) | 故障注入——artifact 上传中途 runner 被杀，半成品不得作为有效 artifact 出现 |
| 116 | [REL-FAULT-01-039](case/REL-FAULT-01-039.md) | 故障注入——排队期唯一匹配 runner 下线，job 应重调度或有界等待后明确失败 |
| 117 | [REL-FLOOD-01-036](case/REL-FLOOD-01-036.md) | 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失 |
| 118 | [REL-FLOOD-01-037](case/REL-FLOOD-01-037.md) | 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃 |
| 119 | [REL-IGNORE-01-004](case/REL-IGNORE-01-004.md) | concurrency IGNORE 策略——超上限运行应直接执行 |
| 120 | [REL-IMAGE-01-052](case/REL-IMAGE-01-052.md) | 镜像拉取性能——500MB 自定义 container 环境准备耗时基准 |
| 121 | [REL-IMAGE-01-052-V2](case/REL-IMAGE-01-052-V2.md) | 镜像拉取性能——5GB 自定义 container 环境准备耗时基准 |
| 122 | [REL-K8S-01-045](case/REL-K8S-01-045.md) | 自托管 K8s Runner 弹性伸缩——min=1/max=1 时并发 3 个 jobs 应排队执行 |
| 123 | [REL-K8S-01-046](case/REL-K8S-01-046.md) | K8s 单集群接入与 NPU 资源发现正确性 |
| 124 | [REL-K8S-01-047](case/REL-K8S-01-047.md) | Karmada 多集群接入、聚合资源发现与指定成员集群调度 |
| 125 | [REL-K8S-01-048](case/REL-K8S-01-048.md) | Karmada 按卡型号/数量自动分发与成员资源不足时的终态语义 |
| 126 | [REL-K8S-01-049](case/REL-K8S-01-049.md) | pod NPU 单卡/多卡调度正确性与非法请求 Pending 语义 |
| 127 | [REL-K8S-01-050](case/REL-K8S-01-050.md) | 【回归】pod 多副本任务（Worker）指定 NPU 调度——当前已知不通过，修复后回归 |
| 128 | [REL-K8S-01-051](case/REL-K8S-01-051.md) | 同一集群重复接入的幂等性 |
| 129 | [REL-LATENCY-01-050-V2](case/REL-LATENCY-01-050-V2.md) | 调度延迟压力——并发 20 个 job 的排队延迟与完成率 |
| 130 | [REL-LOG-01-040](case/REL-LOG-01-040.md) | 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看 |
| 131 | [REL-LOG-01-041](case/REL-LOG-01-041.md) | 单 job 日志大小上限探测——500MB 带序号日志的完整保留或明确截断标识 |
| 132 | [REL-LOGPERF-01-051](case/REL-LOGPERF-01-051.md) | 日志加载性能——50MB 日志下载与查看耗时 |
| 133 | [REL-LOGPERF-01-051-V2](case/REL-LOGPERF-01-051-V2.md) | 日志加载性能——200MB 日志下载与查看耗时 |
| 134 | [REL-LOGPERF-01-052](case/REL-LOGPERF-01-052.md) | 日志实时性——运行中 job 的日志流式可见延迟应有界且与完成后日志一致 |
| 135 | [REL-LOGSTABLE-01-059](case/REL-LOGSTABLE-01-059.md) | 日志系统稳定性——6 万行日志无乱序/无丢失/无截断 |
| 136 | [REL-LONG-01-043](case/REL-LONG-01-043.md) | 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常 |
| 137 | [REL-MATRIX-01-026](case/REL-MATRIX-01-026.md) | matrix fail-fast=true——任意 job 实例失败应立即取消其余实例 |
| 138 | [REL-MATRIX-01-027](case/REL-MATRIX-01-027.md) | matrix max-parallel=4——9 个组合应最多同时运行 4 个 |
| 139 | [REL-MATRIX-01-038](case/REL-MATRIX-01-038.md) | 大规模 matrix——20 个组合应全部生成并正确调度 |
| 140 | [REL-MATRIX-01-039](case/REL-MATRIX-01-039.md) | 大规模 matrix——50 个组合应全部生成并正确调度 |
| 141 | [REL-MATRIX-01-040](case/REL-MATRIX-01-040.md) | matrix 组合数边界——256 组合（GitHub 上限）应全部展开或被明确拒绝 |
| 142 | [REL-MATRIX-01-041](case/REL-MATRIX-01-041.md) | matrix 组合数越界——300 组合超上限时应明确报错（含上限值）不得静默截断 |
| 143 | [REL-MATRIXFAIR-01-056](case/REL-MATRIXFAIR-01-056.md) | 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 的无饿死验证 |
| 144 | [REL-MEM-01-020](case/REL-MEM-01-020.md) | Runner 内存边界——small runner 分配 7.5 GB 应成功 |
| 145 | [REL-NEEDS-01-025](case/REL-NEEDS-01-025.md) | needs 失败传播——上游 job 失败时下游 job 应被 skip |
| 146 | [REL-NEEDS-01-026](case/REL-NEEDS-01-026.md) | needs 依赖 matrix job 成功路径——matrix 全部成功后下游 job 应正常初始化执行 |
| 147 | [REL-NEEDS-01-027](case/REL-NEEDS-01-027.md) | needs 依赖 matrix job 部分失败——无 if 条件的下游 job 应 skipped 而非执行 |
| 148 | [REL-NEST-01-023](case/REL-NEST-01-023.md) | workflow_call 嵌套边界——2 层嵌套调用应成功执行 |
| 149 | [REL-NETFAULT-01-062](case/REL-NETFAULT-01-062.md) | 网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时 |
| 150 | [REL-OUTPUT-01-016](case/REL-OUTPUT-01-016.md) | step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递 |
| 151 | [REL-PATHS-01-014](case/REL-PATHS-01-014.md) | paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效 |
| 152 | [REL-PATHS-01-015](case/REL-PATHS-01-015.md) | paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断 |
| 153 | [REL-POST-01-001](case/REL-POST-01-001.md) | post 后处理阶段失败语义——run_always=true 下 post 失败对 workflow 结论的 |
| 154 | [REL-PREEMPT-01-005](case/REL-PREEMPT-01-005.md) | preemption events 边界值——配置 10 个应正常解析 |
| 155 | [REL-PREEMPT-01-006](case/REL-PREEMPT-01-006.md) | preemption events 越界值——配置 11 个应被拒绝 |
| 156 | [REL-PRESSURE-01-055](case/REL-PRESSURE-01-055.md) | 并发压测——concurrency.max=5 时触发 20 个 workflow 的排队与完成率 |
| 157 | [REL-PROJLIMIT-01-067](case/REL-PROJLIMIT-01-067.md) | 项目级 workflow 并发上限——200 条同时触发时全部完成无丢失 |
| 158 | [REL-PROJLIMIT-01-068](case/REL-PROJLIMIT-01-068.md) | 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排队 |
| 159 | [REL-QUEUE-01-003](case/REL-QUEUE-01-003.md) | concurrency QUEUE 策略——超上限运行应排队等待 |
| 160 | [REL-RACE-01-048](case/REL-RACE-01-048.md) | 取消与 needs 条件竞态——job A 被取消时 job B(if: failure())应正确判定 |
| 161 | [REL-REG-01-001](case/REL-REG-01-001.md) | 新仓库 workflow 注册——首次 push 含合法流水线配置即应触发，无需手动再改一次 |
| 162 | [REL-RERUN-01-011](case/REL-RERUN-01-011.md) | rerun 边界值——单条运行连续重新运行 3 次应全部成功 |
| 163 | [REL-RERUN-01-012](case/REL-RERUN-01-012.md) | rerun 越界值——尝试第 4 次重新运行应被系统拒绝 |
| 164 | [REL-RERUN-01-013](case/REL-RERUN-01-013.md) | rerun 6 小时年龄限制——超期运行不可重新运行 |
| 165 | [REL-RETAIN-01-047](case/REL-RETAIN-01-047.md) | artifact 保留期 90 天边界——第 91 天应不可下载 |
| 166 | [REL-RUNNER-01-049](case/REL-RUNNER-01-049.md) | Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值 |
| 167 | [REL-RUNNER-01-049-V2](case/REL-RUNNER-01-049-V2.md) | Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存/磁盘 vs 声明值 |
| 168 | [REL-RUNNER-01-050](case/REL-RUNNER-01-050.md) | 架构标签调度正确性——x64 请求不得落到 arm64 节点（反之亦然） |
| 169 | [REL-SCHED-01-058](case/REL-SCHED-01-058.md) | schedule 触发准点性与丢失率——cron 最短 5 分钟间隔下 2 小时窗口的触发可靠性 |
| 170 | [REL-STAGES-01-029](case/REL-STAGES-01-029.md) | stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs |
| 171 | [REL-STATE-01-058](case/REL-STATE-01-058.md) | Runner 状态机正确性——空闲/运行/离线转换与时序一致性 |
| 172 | [REL-STATE-01-059](case/REL-STATE-01-059.md) | 运行状态收敛——job 全部终态后 run 状态应在有界时间内脱离 RUNNING 且单调无抖动 |
| 173 | [REL-STEPS-01-042](case/REL-STEPS-01-042.md) | 超多 step——单 job 内 50 个 step 应全部串行执行无丢失 |
| 174 | [REL-TIMEOUT-01-007](case/REL-TIMEOUT-01-007.md) | job timeout 边界值——359 分钟运行应在 360 分钟边界前完成 |
| 175 | [REL-TIMEOUT-01-009](case/REL-TIMEOUT-01-009.md) | 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被强制终止 |
| 176 | [REL-TIMEOUT-01-011](case/REL-TIMEOUT-01-011.md) | 自定义 timeout 超默认值——timeout-minutes=720 的接受/拒绝语义探测 |
| 177 | [REL-VCJOB-01-001](case/REL-VCJOB-01-001.md) | 【回归】vcjob（volcano job）格式任务解析与运行——当前已知不通过，修复后回归 |
| 178 | [REL-VCJOB-01-002](case/REL-VCJOB-01-002.md) | 大规模 vcjob 并发提交（≥50）无丢失、无级联失败 |
| 179 | [SEC-ARTF-01-001](case/SEC-ARTF-01-001.md) | fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执行 |
| 180 | [SEC-ARTF-01-002](case/SEC-ARTF-01-002.md) | 跨仓库 artifact 下载返回 403 或 404 |
| 181 | [SEC-ARTF-01-003](case/SEC-ARTF-01-003.md) | 宽通配打包含敏感文件名的 artifact 绝不应在无警示情况下静默成功且可被无痕下载 |
| 182 | [SEC-AUDIT-01-001](case/SEC-AUDIT-01-001.md) | 敏感操作（secret/权限/rerun/审批/评论触发）必须全部留有不可擦除的审计记录 |
| 183 | [SEC-BASE-01-001](case/SEC-BASE-01-001.md) | pull_request_target 使用 base 分支的 workflow 版本 |
| 184 | [SEC-BASE-01-002](case/SEC-BASE-01-002.md) | fork PR 改 workflow 不被 pull_request_target 采用 |
| 185 | [SEC-CACHE-01-001](case/SEC-CACHE-01-001.md) | fork PR 写入的 cache 必须不可被主仓后续 workflow 读取 |
| 186 | [SEC-CACHE-01-002](case/SEC-CACHE-01-002.md) | 主仓 cache restore 对 fork cache miss |
| 187 | [SEC-COMM-01-001](case/SEC-COMM-01-001.md) | issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过 |
| 188 | [SEC-COMM-01-002](case/SEC-COMM-01-002.md) | 引用/反讽/代码块内嵌指令文本绝不应造成 pull_request_comment 预期外触发 |
| 189 | [SEC-COMM-01-003](case/SEC-COMM-01-003.md) | 变形伪装评论（大小写/多余空白/markdown 包裹）不得绕过 comments 过滤语义 |
| 190 | [SEC-DEFPERM-01-001](case/SEC-DEFPERM-01-001.md) | ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效 |
| 191 | [SEC-DEFPERM-01-002](case/SEC-DEFPERM-01-002.md) | job 级覆盖后权限正确收窄 |
| 192 | [SEC-DOS-01-001](case/SEC-DOS-01-001.md) | 大 artifact / 大 cache 必须受配额与边界限制 |
| 193 | [SEC-ENV-01-002](case/SEC-ENV-01-002.md) | 环境级 secret 审批前 workflow 不可读取 |
| 194 | [SEC-FORK-01-001](case/SEC-FORK-01-001.md) | fork PR 触发 pull_request 时不可读取项目 secrets |
| 195 | [SEC-INJ-01-001](case/SEC-INJ-01-001.md) | 不可信 PR 标题不可直接插进 run 脚本导致命令注入 |
| 196 | [SEC-INJ-01-002](case/SEC-INJ-01-002.md) | 不可信分支名不可直接插进 run 脚本导致命令注入 |
| 197 | [SEC-INJ-01-003](case/SEC-INJ-01-003.md) | 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入 |
| 198 | [SEC-INJ-01-004](case/SEC-INJ-01-004.md) | 不可信 commit message 不可直接插进 run 脚本导致命令注入 |
| 199 | [SEC-INJ-01-005](case/SEC-INJ-01-005.md) | 表达式求值必须防止双重模板渲染（二次求值） |
| 200 | [SEC-LOG-01-001](case/SEC-LOG-01-001.md) | 无权限角色读取/下载运行日志必须被拒，过期日志绝不应可恢复 |
| 201 | [SEC-LOG-01-002](case/SEC-LOG-01-002.md) | 导出/历史日志副本中 secret 原值命中数必须为 0，遮蔽状态不可回退 |
| 202 | [SEC-MASK-01-001](case/SEC-MASK-01-001.md) | Secret 值在运行日志中必须被自动脱敏为 *** |
| 203 | [SEC-MASK-01-002](case/SEC-MASK-01-002.md) | Secret 值在 step summary 和错误堆栈中必须被脱敏 |
| 204 | [SEC-MASK-01-003](case/SEC-MASK-01-003.md) | Secret 日志脱敏不可通过 base64 编码绕过 |
| 205 | [SEC-MASK-01-004](case/SEC-MASK-01-004.md) | Secret 日志脱敏不可通过字符串拼接或插值绕过 |
| 206 | [SEC-MASK-01-005](case/SEC-MASK-01-005.md) | Secret 日志脱敏不可通过多行值输出绕过 |
| 207 | [SEC-MASK-01-006](case/SEC-MASK-01-006.md) | Secret 日志脱敏不可通过分片输出绕过 |
| 208 | [SEC-NAME-01-001](case/SEC-NAME-01-001.md) | Secret/变量名含特殊字符时不可导致意外求值或权限绕过 |
| 209 | [SEC-NAME-01-003](case/SEC-NAME-01-003.md) | 可遮蔽系统变量的 secret 命名（ATOMGIT_ 前缀/非法字符/数字开头）创建时必须被拒 |
| 210 | [SEC-NAME-01-004](case/SEC-NAME-01-004.md) | 与系统变量同名的用户自定义值绝不应覆盖 job 环境中的平台注入值 |
| 211 | [SEC-NET-01-001](case/SEC-NET-01-001.md) | Runner 网络出站必须受控，防止 SSRF 与内网跳板 |
| 212 | [SEC-OIDC-01-001](case/SEC-OIDC-01-001.md) | OIDC / 短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案 |
| 213 | [SEC-ORG-01-001](case/SEC-ORG-01-001.md) | 可见范围外仓库的 workflow 绝不应读到组织级 secret 原值 |
| 214 | [SEC-ORG-01-002](case/SEC-ORG-01-002.md) | fork PR 触发的运行绝不应读取组织级 secret（与项目级同等隔离） |
| 215 | [SEC-PERM-01-001](case/SEC-PERM-01-001.md) | 显式声明的 permissions 必须在 job 级实际生效并限制 ATOMGIT_TOKEN |
| 216 | [SEC-PERM-01-002](case/SEC-PERM-01-002.md) | permissions 声明 read 时写操作被平台拒绝 |
| 217 | [SEC-PERM-01-003](case/SEC-PERM-01-003.md) | 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only） |
| 218 | [SEC-PERM-01-004](case/SEC-PERM-01-004.md) | 默认状态下写操作被 403 拒绝 |
| 219 | [SEC-PRTGT-01-001](case/SEC-PRTGT-01-001.md) | pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控 |
| 220 | [SEC-PRTGT-01-002](case/SEC-PRTGT-01-002.md) | pull_request_target 无审批不执行 fork PR 代码 |
| 221 | [SEC-RUN-01-001](case/SEC-RUN-01-001.md) | Job 结束后 workspace 与临时文件必须被彻底清理 |
| 222 | [SEC-RUN-01-002](case/SEC-RUN-01-002.md) | Runner 环境变量与共享目录必须跨 job 隔离 |
| 223 | [SEC-RUN-01-003](case/SEC-RUN-01-003.md) | 自托管 Runner 跨项目残留必须被隔离 |
| 224 | [SEC-SECMGMT-01-001](case/SEC-SECMGMT-01-001.md) | Secret 写入后任何 API/UI 路径绝不应回读明文 |
| 225 | [SEC-SECMGMT-01-002](case/SEC-SECMGMT-01-002.md) | 无权限角色对 secret 的创建/更新/删除必须被拒且不改变现有集合 |
| 226 | [SEC-SIDE-01-001](case/SEC-SIDE-01-001.md) | Secret 不经 output 侧信道绕过脱敏外泄 |
| 227 | [SEC-SIDE-01-002](case/SEC-SIDE-01-002.md) | Secret 不经 artifact 侧信道绕过脱敏外泄 |
| 228 | [SEC-SUPPLY-01-001](case/SEC-SUPPLY-01-001.md) | 第三方 Action 引用应支持完整 commit hash 固定 |
| 229 | [SEC-SUPPLY-01-002](case/SEC-SUPPLY-01-002.md) | commit hash 不匹配时第三方 Action 应被拒绝执行 |
| 230 | [SEC-SUPPLY-01-003](case/SEC-SUPPLY-01-003.md) | 第三方 Action 来源应具备信任边界（typosquatting 限制） |
| 231 | [SEC-TOCTOU-01-001](case/SEC-TOCTOU-01-001.md) | 审批后推送新 commit 不应被已授权特权运行执行 |
| 232 | [SEC-TOCTOU-01-002](case/SEC-TOCTOU-01-002.md) | 评论触发不应绕过代码固定与 PR 审批 |
| 233 | [SEC-TOCTOU-01-003](case/SEC-TOCTOU-01-003.md) | 评论触发后被编辑的内容绝不应改变已排队/运行中 workflow 读取的事件负载 |
| 234 | [SEC-TOKEN-01-001](case/SEC-TOKEN-01-001.md) | fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限 |
| 235 | [SEC-TOKEN-01-002](case/SEC-TOKEN-01-002.md) | fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝 |
| 236 | [SEC-TOKEN-01-003](case/SEC-TOKEN-01-003.md) | run 结束后旧 ATOMGIT_TOKEN 调用任何 API 必须失效 |
| 237 | [SEC-TOKEN-01-004](case/SEC-TOKEN-01-004.md) | 残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权 |
| 238 | [SEC-WCMD-01-001](case/SEC-WCMD-01-001.md) | Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值 |
| 239 | [SEC-WCMD-01-002](case/SEC-WCMD-01-002.md) | 跨运行 artifact 必须被视为不可信数据 |
| 240 | [SEC-WCMD-01-003](case/SEC-WCMD-01-003.md) | ATOMGIT_ENV 不被不可信输入污染提权 |
| 241 | [SEC-WCMD-01-004](case/SEC-WCMD-01-004.md) | ATOMGIT_OUTPUT 不被不可信输入污染提权 |
| 242 | [SEC-WFRUN-01-001](case/SEC-WFRUN-01-001.md) | 不可信运行绝不应存在隐式拉起高权限后续运行的链式路径 |
| 243 | [USE-ACT-01-003](case/USE-ACT-01-003.md) | 官方短名 Action 清单与 actions-market 插件目录的映射一致性 |
| 244 | [USE-ACT-01-004](case/USE-ACT-01-004.md) | 文档短名与市场名两种写法解析一致性验证 |
| 245 | [USE-API-01-001](case/USE-API-01-001.md) | API 字段值与事件类型命名同一概念分裂的对照检查 |
| 246 | [USE-CLI-01-001](case/USE-CLI-01-001.md) | Runner 无 gh 等效 CLI 时迁移指引的替代方案说明 |
| 247 | [USE-CONT-01-001](case/USE-CONT-01-001.md) | container.image 文档声明可用与实际可用性的一致性 |
| 248 | [USE-DISP-01-003](case/USE-DISP-01-003.md) | workflow_dispatch 手动触发 UI 与 YAML inputs 定义的集合一致性 |
| 249 | [USE-DOC-01-002](case/USE-DOC-01-002.md) | stages 与 stages 内 jobs 字段语法跨文档四种形态互相矛盾的扫描 |
| 250 | [USE-DOC-01-003](case/USE-DOC-01-003.md) | trigger-events 每分钟 cron 示例与最短间隔 5 分钟声明自相矛盾 |
| 251 | [USE-DOC-01-004](case/USE-DOC-01-004.md) | workflow-commands 多行输出示例漏写重定向照抄得空输出 |
| 252 | [USE-DOC-01-006](case/USE-DOC-01-006.md) | syntax-reference 章节编号连续性扫描 |
| 253 | [USE-DOC-01-007](case/USE-DOC-01-007.md) | environment 字段能力描述存在而语法参考缺失及平台报错指引 |
| 254 | [USE-ENV-01-003](case/USE-ENV-01-003.md) | ATOMGIT 系统环境变量实际注入集合与文档清单双向 diff |
| 255 | [USE-EXPR-01-003](case/USE-EXPR-01-003.md) | expressions 函数表语法标记可解析性与状态关键字术语区分 |
| 256 | [USE-EXPR-01-004](case/USE-EXPR-01-004.md) | 未文档化函数 default() 的文档缺失 diff（与平台行为断言合并证据链） |
| 257 | [USE-LBL-01-003](case/USE-LBL-01-003.md) | runs-on 标签写法跨文档形态扫描（同一字段不应出现三种以上互斥形态） |
| 258 | [USE-LBL-01-005](case/USE-LBL-01-005.md) | runs-on 含资源池名写法的文档资源池清单 diff |
| 259 | [USE-MD-01-001](case/USE-MD-01-001.md) | ATOMGIT_STEP_SUMMARY 写入的 Markdown 正确渲染为 HTML |
| 260 | [USE-ONBD-01-001](case/USE-ONBD-01-001.md) | 新手快速开始路径端到端可复刻走查（判定方式：llm_assisted） |
| 261 | [USE-OS-01-002](case/USE-OS-01-002.md) | runner 上下文返回值精确格式与文档枚举值逐字符一致性 |
| 262 | [USE-STAT-01-001](case/USE-STAT-01-001.md) | 使用 always() 带括号时若被接受则正常执行 |
| 263 | [USE-TOGGLE-01-001](case/USE-TOGGLE-01-001.md) | 隐藏安全开关 ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS 默认值与文档缺失 |
| 264 | [USE-TYPE-01-003](case/USE-TYPE-01-003.md) | pull_request_comment 与 pr_comment 事件名双轨的文档说明 |
| 265 | [USE-UNKN-01-003](case/USE-UNKN-01-003.md) | step 标识 id 与 identifier 命名双轨的接受一致性与文档说明 |
| 266 | [USE-UNKN-01-004](case/USE-UNKN-01-004.md) | 未文档化字段 select/manual_override/code-update/顶层 inputs 的文档 |
| 267 | [USE-VARS-01-002](case/USE-VARS-01-002.md) | 变量插值双语法与 atomgit 属性名的文档清单 diff 及求值探测 |
| 268 | [USE-YAML-01-002](case/USE-YAML-01-002.md) | YAML 缩进错误时报错应指出具体行号与列号 |

## 4. 部分不符 — 验证点与步骤产出部分不一致（147 例）

| # | Case ID | 标题 | 问题判定 |
|---|---------|------|------|
| 1 | [COMP-ATOMGIT-01-047](case/COMP-ATOMGIT-01-047.md) | atomgit 核心上下文属性可访问性 | MISSING_SOURCE |
| 2 | [COMP-ATOMGIT-01-048](case/COMP-ATOMGIT-01-048.md) | atomgit 事件相关属性可访问性 | MISSING_SOURCE |
| 3 | [COMP-BOUND-01-087](case/COMP-BOUND-01-087.md) | 步骤输出与跨 job 传递边界验证 | MISSING_SOURCE |
| 4 | [COMP-CTX-01-051](case/COMP-CTX-01-051.md) | 上下文在 workflow job step 各级注入验证 | MISSING_SOURCE |
| 5 | [COMP-CTX-01-052](case/COMP-CTX-01-052.md) | 上下文在条件表达式 if 中注入验证 | VACUOUS |
| 6 | [COMP-CTX-01-055](case/COMP-CTX-01-055.md) | workflow_dispatch 触发下 inputs 正常求值（回归保护 | MISSING_SOURCE |
| 7 | [COMP-DIR-01-001](case/COMP-DIR-01-001.md) | .gitcode/workflows/ 下的 YAML 被正确识别并触发 | STATUS_GUARANTEED |
| 8 | [COMP-EXPR-01-057](case/COMP-EXPR-01-057.md) | format substring replace 函数边界行为 | MISSING_SOURCE |
| 9 | [COMP-ISOLATION-01-003](case/COMP-ISOLATION-01-003.md) | container.volumes 常规挂载在托管 Runner 的行为记录 | LLM_DEPENDENT |
| 10 | [COMP-JOB-01-068](case/COMP-JOB-01-068.md) | job strategy 矩阵与 continue-on-error 验证 | MISSING_SOURCE |
| 11 | [COMP-PRTARGET-01-001](case/COMP-PRTARGET-01-001.md) | pull_request_target 默认使用 base 分支 workf | VACUOUS |
| 12 | [COMP-PRTARGET-01-002](case/COMP-PRTARGET-01-002.md) | 显式 checkout head.sha 后执行不可信代码的风险可控 | VACUOUS |
| 13 | [COMP-PUSH-01-001](case/COMP-PUSH-01-001.md) | 匹配 branches 的 push 正确触发 workflow | STATUS_GUARANTEED |
| 14 | [COMP-RUNNER-01-001](case/COMP-RUNNER-01-001.md) | 三段式标签正确调度到对应规格 Runner | STATUS_GUARANTEED |
| 15 | [COMP-RUNNER-01-002](case/COMP-RUNNER-01-002.md) | runs-on default 等效 ubuntu-latest x64 s | STATUS_GUARANTEED |
| 16 | [COMP-RUNNER-01-082](case/COMP-RUNNER-01-082.md) | flow-mapping 写法 runs-on 的处理结果裁定 | LLM_DEPENDENT |
| 17 | [COMP-SCHEDULE-01-001](case/COMP-SCHEDULE-01-001.md) | 合法 cron 在默认分支按时触发 | STATUS_GUARANTEED |
| 18 | [COMP-SECRET-01-001](case/COMP-SECRET-01-001.md) | echo secret 在日志中被脱敏为 *** | MISSING_SOURCE |
| 19 | [COMP-SECRET-01-003](case/COMP-SECRET-01-003.md) | base64 编码后的 secret 是否仍被脱敏 | LLM_DEPENDENT |
| 20 | [COMP-STAGES-01-001](case/COMP-STAGES-01-001.md) | stages 阶段间串行、阶段内 job 并行执行 | STATUS_GUARANTEED |
| 21 | [COMP-STAGES-01-005](case/COMP-STAGES-01-005.md) | list 形式 stages 的实际处理裁定记录 | LLM_DEPENDENT |
| 22 | [COMP-STATUS-01-001](case/COMP-STATUS-01-001.md) | 运行状态机 queued 到 completed 转换正确 | STATUS_GUARANTEED |
| 23 | [COMP-STATUS-01-002](case/COMP-STATUS-01-002.md) | 失败 step 的日志完整保留且可查看 | VACUOUS |
| 24 | [COMP-STEP-01-069](case/COMP-STEP-01-069.md) | step 必填与核心字段 name run uses 验证 | VACUOUS |
| 25 | [COMP-STEP-01-071](case/COMP-STEP-01-071.md) | step 执行控制 shell working-directory cont | VACUOUS |
| 26 | [COMP-TIMEOUT-01-002](case/COMP-TIMEOUT-01-002.md) | 超时的 job 被强制终止并标记为 failure | IMPOSSIBLE, VACUOUS |
| 27 | [COMP-TRIG-01-072](case/COMP-TRIG-01-072.md) | push 事件关键字段与过滤验证 | MISSING_SOURCE |
| 28 | [COMP-TRIG-01-080](case/COMP-TRIG-01-080.md) | 触发事件别名 pr_comment 的有效性与等价性记录 | LLM_DEPENDENT |
| 29 | [COMP-UNKNOWN-01-004](case/COMP-UNKNOWN-01-004.md) | select 与 selected_by_default 声明时的实际行为记 | LLM_DEPENDENT |
| 30 | [COMP-VARREF-01-083](case/COMP-VARREF-01-083.md) | YAML 表达式与 Shell 环境变量引用方式验证 | MISSING_SOURCE |
| 31 | [COMPAT-ACTION-01-003](case/COMPAT-ACTION-01-003.md) | GitHub 风格 action 引用 actions/checkout@v | LLM_DEPENDENT |
| 32 | [COMPAT-ACTION-01-004](case/COMPAT-ACTION-01-004.md) | 官方文档示例 docker/build-push-action@v6 引用的 | LLM_DEPENDENT |
| 33 | [COMPAT-ACTIONDEV-01-001](case/COMPAT-ACTIONDEV-01-001.md) | action.yml 元数据校验与 GitHub 差异 | LLM_DEPENDENT |
| 34 | [COMPAT-ACTIONDEV-01-002](case/COMPAT-ACTIONDEV-01-002.md) | action 运行时 runs.using 类型覆盖（node16/comp | LLM_DEPENDENT |
| 35 | [COMPAT-CACHE-01-001](case/COMPAT-CACHE-01-001.md) | cache 行为等价性——缓存命中场景 | LLM_DEPENDENT |
| 36 | [COMPAT-COMM-01-001](case/COMPAT-COMM-01-001.md) | issue_comment types 命名差异 - GitCode 合法  | LLM_DEPENDENT |
| 37 | [COMPAT-COMM-01-002](case/COMPAT-COMM-01-002.md) | issue_comment types:created 不支持时应给出降级指 | LLM_DEPENDENT |
| 38 | [COMPAT-CONCUR-01-001](case/COMPAT-CONCUR-01-001.md) | concurrency cancel-in-progress false 时 | LLM_DEPENDENT |
| 39 | [COMPAT-CONCUR-01-002](case/COMPAT-CONCUR-01-002.md) | concurrency 配置越界或不支持时应给出清晰报错 | LLM_DEPENDENT |
| 40 | [COMPAT-CONCUR-01-003](case/COMPAT-CONCUR-01-003.md) | concurrency preemption enable 行为差异 | LLM_DEPENDENT |
| 41 | [COMPAT-CONCUR-01-004](case/COMPAT-CONCUR-01-004.md) | concurrency preemption events 越界时行为差异 | LLM_DEPENDENT |
| 42 | [COMPAT-CONTAINER-01-001](case/COMPAT-CONTAINER-01-001.md) | container 字段不被支持时应明确报错而非静默忽略 | LLM_DEPENDENT |
| 43 | [COMPAT-CONTAINER-01-002](case/COMPAT-CONTAINER-01-002.md) | container 自定义镜像被拒绝时应给出替代指引 | LLM_DEPENDENT |
| 44 | [COMPAT-CTX-01-001](case/COMPAT-CTX-01-001.md) | 使用 github.ref 上下文应报错或求值为空 | LLM_DEPENDENT |
| 45 | [COMPAT-CTX-01-003](case/COMPAT-CTX-01-003.md) | github 上下文嵌套属性访问应报错而非返回空 | LLM_DEPENDENT |
| 46 | [COMPAT-DEPR-01-001](case/COMPAT-DEPR-01-001.md) | ::set-env:: 废弃命令应被拒绝或给出迁移指引 | LLM_DEPENDENT |
| 47 | [COMPAT-DEPR-01-002](case/COMPAT-DEPR-01-002.md) | ::add-path:: 废弃命令应被拒绝或给出迁移指引 | LLM_DEPENDENT |
| 48 | [COMPAT-DIR-01-002](case/COMPAT-DIR-01-002.md) | 工作流目录差异——.github/workflows/ 不应被识别 | LLM_DEPENDENT |
| 49 | [COMPAT-DIR-01-003](case/COMPAT-DIR-01-003.md) | .github/workflows 目录不应被识别且应给出迁移提示 | LLM_DEPENDENT |
| 50 | [COMPAT-ENV-01-002](case/COMPAT-ENV-01-002.md) | GITHUB_SHA 环境变量在 GitCode 中应为空或未定义 | LLM_DEPENDENT |
| 51 | [COMPAT-ENV-01-003](case/COMPAT-ENV-01-003.md) | GITHUB_ENV 环境变量不应被静默映射到 ATOMGIT_ENV | LLM_DEPENDENT |
| 52 | [COMPAT-ENVIRON-01-001](case/COMPAT-ENVIRON-01-001.md) | 含 environment 字段的 job 应被报错或警告 | LLM_DEPENDENT |
| 53 | [COMPAT-ENVIRON-01-002](case/COMPAT-ENVIRON-01-002.md) | environment 字段绑定 secrets 的行为差异 | LLM_DEPENDENT |
| 54 | [COMPAT-EVENT-01-001](case/COMPAT-EVENT-01-001.md) | GitHub 全量事件集中不受支持事件（release 等）的降级方式 | LLM_DEPENDENT |
| 55 | [COMPAT-EXPR-01-002](case/COMPAT-EXPR-01-002.md) | success() 函数的处理行为差异 | VACUOUS |
| 56 | [COMPAT-EXPR-01-013](case/COMPAT-EXPR-01-013.md) | success() 带括号与不带括号的兼容性差异 | LLM_DEPENDENT |
| 57 | [COMPAT-EXPR-01-014](case/COMPAT-EXPR-01-014.md) | always() 带括号与不带括号的兼容性差异 | LLM_DEPENDENT |
| 58 | [COMPAT-EXPR-01-015](case/COMPAT-EXPR-01-015.md) | startsWith/endsWith 大小写敏感性两侧文档矛盾的差异确认 | LLM_DEPENDENT, VACUOUS |
| 59 | [COMPAT-FIELD-01-001](case/COMPAT-FIELD-01-001.md) | 含 run-name 字段的 workflow 应被报错或警告 | LLM_DEPENDENT |
| 60 | [COMPAT-FIELD-01-002](case/COMPAT-FIELD-01-002.md) | 含 services 字段的 job 应被报错或警告 | LLM_DEPENDENT |
| 61 | [COMPAT-FIELD-01-003](case/COMPAT-FIELD-01-003.md) | 未知顶层字段不应被静默忽略而应给出警告 | LLM_DEPENDENT |
| 62 | [COMPAT-IF-01-001](case/COMPAT-IF-01-001.md) | step 失败后后续 step 默认跳过行为 | VACUOUS |
| 63 | [COMPAT-IF-01-002](case/COMPAT-IF-01-002.md) | continue-on-error 标记后失败 step 不阻断后续执行 | VACUOUS |
| 64 | [COMPAT-INPUTS-01-002](case/COMPAT-INPUTS-01-002.md) | workflow_dispatch inputs 类型限制 - string | MISSING_SOURCE |
| 65 | [COMPAT-ISOLATE-01-001](case/COMPAT-ISOLATE-01-001.md) | Runner 环境隔离——跨 job 文件隔离 | LLM_DEPENDENT |
| 66 | [COMPAT-ISOLATE-01-002](case/COMPAT-ISOLATE-01-002.md) | Runner 环境隔离——跨 job 环境变量隔离 | LLM_DEPENDENT |
| 67 | [COMPAT-LIMIT-01-001](case/COMPAT-LIMIT-01-001.md) | 单次推送多个 tag 的事件生成上限行为（GitHub 超过 3 个不生成事 | LLM_DEPENDENT |
| 68 | [COMPAT-LIMIT-01-002](case/COMPAT-LIMIT-01-002.md) | workflow_dispatch 输入数量上限（GitHub 25 个）与 | LLM_DEPENDENT |
| 69 | [COMPAT-MATRIX-01-003](case/COMPAT-MATRIX-01-003.md) | matrix 三维展开不被支持时的差异 | LLM_DEPENDENT |
| 70 | [COMPAT-MATRIX-01-004](case/COMPAT-MATRIX-01-004.md) | matrix include 无基础变量不被支持时的差异 | LLM_DEPENDENT |
| 71 | [COMPAT-MATRIX-01-005](case/COMPAT-MATRIX-01-005.md) | matrix exclude 全排除不被支持时的差异 | LLM_DEPENDENT |
| 72 | [COMPAT-MIGRATE-01-001](case/COMPAT-MIGRATE-01-001.md) | GitHub 风格 permissions 块迁移报错应给出可操作指引 | LLM_DEPENDENT |
| 73 | [COMPAT-MIGRATE-01-002](case/COMPAT-MIGRATE-01-002.md) | GitHub 风格 run-name 语法迁移报错应给出可操作指引 | LLM_DEPENDENT |
| 74 | [COMPAT-OUTCOME-01-001](case/COMPAT-OUTCOME-01-001.md) | continue-on-error false 时 outcome 与 co | LLM_DEPENDENT |
| 75 | [COMPAT-OUTCOME-01-002](case/COMPAT-OUTCOME-01-002.md) | continue-on-error true 时 outcome 应为 fa | LLM_DEPENDENT |
| 76 | [COMPAT-OUTCOME-01-003](case/COMPAT-OUTCOME-01-003.md) | outcome 与 conclusion 在 job 条件判断中不应互换语义 | LLM_DEPENDENT |
| 77 | [COMPAT-OUTPUT-01-001](case/COMPAT-OUTPUT-01-001.md) | 跨 Job 引用未声明 output 时返回空值的差异 | LLM_DEPENDENT |
| 78 | [COMPAT-PERM-01-003](case/COMPAT-PERM-01-003.md) | permissions 命名差异——GitHub contents 权限项应 | LLM_DEPENDENT |
| 79 | [COMPAT-PERM-01-005](case/COMPAT-PERM-01-005.md) | permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差 | LLM_DEPENDENT |
| 80 | [COMPAT-PERM-01-006](case/COMPAT-PERM-01-006.md) | job 级 permissions 字段的支持度与降级方式（权限不得宽于声明 | LLM_DEPENDENT |
| 81 | [COMPAT-PR-01-003](case/COMPAT-PR-01-003.md) | PR types 配置后匹配类型不触发与 GitHub 行为差异 | LLM_DEPENDENT |
| 82 | [COMPAT-PR-01-004](case/COMPAT-PR-01-004.md) | PR types 含 merge 时不触发与 GitHub 行为差异 | LLM_DEPENDENT |
| 83 | [COMPAT-PR-01-005](case/COMPAT-PR-01-005.md) | PR paths 过滤不工作时的兼容性差异 | LLM_DEPENDENT |
| 84 | [COMPAT-PR-01-006](case/COMPAT-PR-01-006.md) | PR 目标分支过滤行为差异 | LLM_DEPENDENT |
| 85 | [COMPAT-PR-01-007](case/COMPAT-PR-01-007.md) | pull_request 不支持的 activity type（labele | LLM_DEPENDENT |
| 86 | [COMPAT-PR-01-008](case/COMPAT-PR-01-008.md) | pull_request 不支持的 activity type（ready_ | LLM_DEPENDENT |
| 87 | [COMPAT-PR-01-010](case/COMPAT-PR-01-010.md) | 存在合并冲突的 PR 的触发行为（GitHub 不触发）对齐确认 | LLM_DEPENDENT |
| 88 | [COMPAT-RUNNER-01-003](case/COMPAT-RUNNER-01-003.md) | self-hosted 标签不被支持时应明确报错 | LLM_DEPENDENT |
| 89 | [COMPAT-RUNNER-01-004](case/COMPAT-RUNNER-01-004.md) | 自定义特征标签不被支持时应给出可用标签列表 | LLM_DEPENDENT |
| 90 | [COMPAT-RUNNER-01-005](case/COMPAT-RUNNER-01-005.md) | 内网环境 Runner 不支持时的差异 | LLM_DEPENDENT |
| 91 | [COMPAT-RUNNER-01-006](case/COMPAT-RUNNER-01-006.md) | Runner 未预装 Java 工具链与 GitHub 差异 | LLM_DEPENDENT |
| 92 | [COMPAT-RUNSON-01-002](case/COMPAT-RUNSON-01-002.md) | runs-on 标签体系——单标签字符串应报错 | LLM_DEPENDENT |
| 93 | [COMPAT-RUNSON-01-003](case/COMPAT-RUNSON-01-003.md) | 自托管 runs-on 对象式写法（type/group/labels）的实 | LLM_DEPENDENT |
| 94 | [COMPAT-RUNSON-01-004](case/COMPAT-RUNSON-01-004.md) | 自托管 runs-on 数组式写法（标签列表子集匹配）的实测仲裁 | LLM_DEPENDENT |
| 95 | [COMPAT-RUNSON-01-005](case/COMPAT-RUNSON-01-005.md) | Runner OS 多样性探测：windows-latest 的调度结局（不 | LLM_DEPENDENT |
| 96 | [COMPAT-RUNSON-01-006](case/COMPAT-RUNSON-01-006.md) | Runner OS 多样性探测：macos-latest 的调度结局（不支持 | LLM_DEPENDENT |
| 97 | [COMPAT-SCHEDULE-01-001](case/COMPAT-SCHEDULE-01-001.md) | schedule cron 按 UTC 时间触发 | LLM_DEPENDENT, STATUS_GUARANTEED |
| 98 | [COMPAT-SCHEDULE-01-003](case/COMPAT-SCHEDULE-01-003.md) | schedule 在非默认分支不触发与 GitHub 差异 | LLM_DEPENDENT |
| 99 | [COMPAT-SECRET-01-005](case/COMPAT-SECRET-01-005.md) | 环境级 secrets 不支持时应明确报错而非降级为项目级 | LLM_DEPENDENT |
| 100 | [COMPAT-SHELL-01-003](case/COMPAT-SHELL-01-003.md) | Windows runner 默认 shell 差异 | LLM_DEPENDENT |
| 101 | [COMPAT-TARGET-01-003](case/COMPAT-TARGET-01-003.md) | pull_request_target 默认 types 与 GitHub  | LLM_DEPENDENT |
| 102 | [COMPAT-TOKEN-01-001](case/COMPAT-TOKEN-01-001.md) | ATOMGIT_TOKEN 应正确返回有效令牌 | LLM_DEPENDENT, UNEXERCISED |
| 103 | [COMPAT-TOKEN-01-002](case/COMPAT-TOKEN-01-002.md) | GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射 | LLM_DEPENDENT |
| 104 | [COMPAT-TOKEN-01-003](case/COMPAT-TOKEN-01-003.md) | GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN | LLM_DEPENDENT |
| 105 | [COMPAT-VARS-01-002](case/COMPAT-VARS-01-002.md) | vars 上下文若不支持应报错而非静默为空 | LLM_DEPENDENT |
| 106 | [COMPAT-VARS-01-003](case/COMPAT-VARS-01-003.md) | vars 项目级覆盖组织级的优先级差异 | LLM_DEPENDENT |
| 107 | [COMPAT-VARS-01-004](case/COMPAT-VARS-01-004.md) | vars 与 env 同名时的优先级差异 | LLM_DEPENDENT |
| 108 | [COMPAT-VARS-01-005](case/COMPAT-VARS-01-005.md) | vars 在条件表达式 if 中的可用性差异 | LLM_DEPENDENT |
| 109 | [COMPAT-VARS-01-006](case/COMPAT-VARS-01-006.md) | vars 在 Action 中的可用性差异 | LLM_DEPENDENT |
| 110 | [COMPAT-WCMD-01-001](case/COMPAT-WCMD-01-001.md) | ::add-mask:: 不被支持时应静默降级而非报错 | LLM_DEPENDENT |
| 111 | [COMPAT-WCMD-01-002](case/COMPAT-WCMD-01-002.md) | ::group:: 不被支持时应静默降级而非报错 | LLM_DEPENDENT |
| 112 | [COMPAT-WCMD-01-003](case/COMPAT-WCMD-01-003.md) | ::stop-commands:: 不被支持时应静默降级而非报错 | LLM_DEPENDENT |
| 113 | [REL-CACHEPERF-01-054](case/REL-CACHEPERF-01-054.md) | 缓存加速比——cache 命中 vs 未命中构建耗时对比 | LLM_DEPENDENT |
| 114 | [REL-CLUSTER-01-001](case/REL-CLUSTER-01-001.md) | 集群断连恢复后断连窗口任务日志同步 | LLM_DEPENDENT |
| 115 | [REL-DISK-01-019](case/REL-DISK-01-019.md) | Runner 磁盘越界——small runner 写入 51 GB 应失败 | MISSING_SOURCE |
| 116 | [REL-FAIR-01-044](case/REL-FAIR-01-044.md) | 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调 | LLM_DEPENDENT |
| 117 | [REL-FAULT-01-031](case/REL-FAULT-01-031.md) | 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失 | VACUOUS |
| 118 | [REL-FAULT-01-033](case/REL-FAULT-01-033.md) | 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满 | MISSING_SOURCE |
| 119 | [REL-FAULT-01-036](case/REL-FAULT-01-036.md) | 故障注入——runner 与平台心跳分区 60 秒后恢复，job 应续跑完成 | LLM_DEPENDENT, VACUOUS |
| 120 | [REL-LATENCY-01-050](case/REL-LATENCY-01-050.md) | 调度延迟基准——queued→running P50/P95 等待时间 | LLM_DEPENDENT |
| 121 | [REL-MEM-01-021](case/REL-MEM-01-021.md) | Runner 内存越界——small runner 分配 9 GB 应被 O | MISSING_SOURCE |
| 122 | [REL-NEST-01-024](case/REL-NEST-01-024.md) | workflow_call 嵌套越界——3 层嵌套调用应被拒绝 | MISSING_SOURCE |
| 123 | [REL-OUTPUT-01-017](case/REL-OUTPUT-01-017.md) | step output 越界值——ATOMGIT_OUTPUT 写入 1 M | MISSING_SOURCE |
| 124 | [REL-SCHED-01-057](case/REL-SCHED-01-057.md) | 资源调度状态一致性——空闲 runner 存在时 job 不应死等 | LLM_DEPENDENT |
| 125 | [REL-TIMEOUT-01-008](case/REL-TIMEOUT-01-008.md) | job timeout 越界触发——361 分钟应在 360 分钟被强制终止 | MISSING_SOURCE |
| 126 | [REL-TIMEOUT-01-010](case/REL-TIMEOUT-01-010.md) | 默认超时——未声明 timeout-minutes 运行 361 分钟应被强 | MISSING_SOURCE |
| 127 | [SEC-ENV-01-001](case/SEC-ENV-01-001.md) | 环境级 secret 必须经审批后才能被 workflow 访问 | UNEXERCISED |
| 128 | [SEC-FORK-01-002](case/SEC-FORK-01-002.md) | fork PR 中 secrets 引用返回空值且 job 不崩溃 | UNEXERCISED |
| 129 | [SEC-NAME-01-002](case/SEC-NAME-01-002.md) | 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secr | UNEXERCISED |
| 130 | [USE-ANNOT-01-002](case/USE-ANNOT-01-002.md) | ::error:: 生成的 PR annotation 具备文件路径、行号与 | LLM_DEPENDENT |
| 131 | [USE-DEPR-01-002](case/USE-DEPR-01-002.md) | 使用 ::set-output 时应给出弃用警告与替代示例 | LLM_DEPENDENT |
| 132 | [USE-DIR-01-002](case/USE-DIR-01-002.md) | .github/workflows/ 下 workflow 未被识别时应给出 | LLM_DEPENDENT |
| 133 | [USE-DOC-01-001](case/USE-DOC-01-001.md) | stages 与 post 概念在迁移文档中具备可发现性 | LLM_DEPENDENT |
| 134 | [USE-DOC-01-005](case/USE-DOC-01-005.md) | configure-steps 的 shell 类型与命令语言不匹配示例照抄 | IMPOSSIBLE |
| 135 | [USE-ENV-01-002](case/USE-ENV-01-002.md) | 引用 GITHUB_SHA 时日志应给出环境变量映射提示 | LLM_DEPENDENT |
| 136 | [USE-ENV-01-004](case/USE-ENV-01-004.md) | job env 在 shell 层与表达式层取值一致性（文档承诺兑现验证） | MISSING_SOURCE |
| 137 | [USE-LBL-01-002](case/USE-LBL-01-002.md) | runs-on 标签因容量不足排队时应提示排队状态而非无可用 runner | LLM_DEPENDENT |
| 138 | [USE-LBL-01-004](case/USE-LBL-01-004.md) | quick-start 单标签写法 runs-on ubuntu-lates | STATUS_GUARANTEED |
| 139 | [USE-MASK-01-002](case/USE-MASK-01-002.md) | 直接 echo secrets 值时文档描述的绕过风险与实际一致 | LLM_DEPENDENT |
| 140 | [USE-ONBD-01-002](case/USE-ONBD-01-002.md) | quick-start 示例提交后运行结果可见性检查点 | STATUS_GUARANTEED |
| 141 | [USE-PATH-01-001](case/USE-PATH-01-001.md) | paths 300 文件上限在文档与行为中一致且明示 | LLM_DEPENDENT |
| 142 | [USE-RES-01-001](case/USE-RES-01-001.md) | runtime-environment-variables.md 中不应出现 | LLM_DEPENDENT |
| 143 | [USE-RUN-01-003](case/USE-RUN-01-003.md) | rerun 上限与 6 小时时限在 UI 的明示（判定方式：llm_assi | LLM_DEPENDENT |
| 144 | [USE-SCHED-01-001](case/USE-SCHED-01-001.md) | schedule 不触发时的可观测提示（判定方式：llm_assisted） | LLM_DEPENDENT |
| 145 | [USE-UNKN-01-001](case/USE-UNKN-01-001.md) | 未知字段如 run-name 不应被静默忽略而应给出警告或错误 | LLM_DEPENDENT |
| 146 | [USE-UNKN-01-002](case/USE-UNKN-01-002.md) | 未知字段报错若识别为 GitHub 特有应追加迁移提示 | LLM_DEPENDENT |
| 147 | [USE-VARS-01-001](case/USE-VARS-01-001.md) | vars 上下文在文档与样本中的声明必须一致 | LLM_DEPENDENT |

## 5. 完全不符 — 全部验证点未能由步骤产出（83 例）

| # | Case ID | 标题 | 问题判定 |
|---|---------|------|------|
| 1 | [COMP-ATOMGIT-01-049](case/COMP-ATOMGIT-01-049.md) | atomgit 边界格式校验 | MISSING_SOURCE, VACUOUS |
| 2 | [COMP-BOUND-01-084](case/COMP-BOUND-01-084.md) | 路径与分支过滤组合及否定模式边界验证 | STATUS_GUARANTEED, VACUOUS |
| 3 | [COMP-BOUND-01-085](case/COMP-BOUND-01-085.md) | cron 表达式格式与位置边界验证 | STATUS_GUARANTEED, VACUOUS |
| 4 | [COMP-BOUND-01-088](case/COMP-BOUND-01-088.md) | 工作流命令 set-env add-path 与文件写入边界验证 | VACUOUS |
| 5 | [COMP-CALL-01-001](case/COMP-CALL-01-001.md) | 2 层 workflow_call 嵌套正常执行 | STATUS_GUARANTEED |
| 6 | [COMP-CALL-01-002](case/COMP-CALL-01-002.md) | 3 层 workflow_call 嵌套应被拒绝 | LLM_DEPENDENT, STATUS_GUARANTEED |
| 7 | [COMP-CALL-01-003](case/COMP-CALL-01-003.md) | 本地路径 workflow_call 完整 secrets 映射正常执行 | MISSING_SOURCE, STATUS_GUARANTEED |
| 8 | [COMP-CALL-01-004](case/COMP-CALL-01-004.md) | 未传 required secret 的 workflow_call 不应空 | LLM_DEPENDENT, MISSING_SOURCE, STATUS_GUARANTEED |
| 9 | [COMP-ENVCTX-01-050](case/COMP-ENVCTX-01-050.md) | env 优先级链 step 大于 job 大于 workflow | MISSING_SOURCE |
| 10 | [COMP-EXPR-01-056](case/COMP-EXPR-01-056.md) | toJson 函数边界行为 | MISSING_SOURCE |
| 11 | [COMP-EXPR-01-059](case/COMP-EXPR-01-059.md) | 未文档化函数 default() 的存在性与求值记录 | LLM_DEPENDENT, VACUOUS |
| 12 | [COMP-JOB-01-066](case/COMP-JOB-01-066.md) | job 必填字段 name runs-on steps 验证 | STATUS_GUARANTEED, VACUOUS |
| 13 | [COMP-JOB-01-067](case/COMP-JOB-01-067.md) | job 可选字段 env if timeout-minutes needs  | MISSING_SOURCE, VACUOUS |
| 14 | [COMP-PRTARGET-01-003](case/COMP-PRTARGET-01-003.md) | fork PR 按文档推荐配置 pull_request_target 的  | LLM_DEPENDENT, UNEXERCISED |
| 15 | [COMP-RUNNER-01-003](case/COMP-RUNNER-01-003.md) | 不存在的标签组合导致 job 排队或失败 | LLM_DEPENDENT, STATUS_GUARANTEED |
| 16 | [COMP-SCRIPT-01-081](case/COMP-SCRIPT-01-081.md) | 仓库内脚本执行与路径验证 | VACUOUS |
| 17 | [COMP-SECRET-01-002](case/COMP-SECRET-01-002.md) | secret 原始值不应以明文出现在标准日志中 | UNEXERCISED |
| 18 | [COMP-STAGES-01-004](case/COMP-STAGES-01-004.md) | map 形式 stages 按定义顺序串行执行（回归保护） | LLM_DEPENDENT, MISSING_SOURCE, STATUS_GUARANTEED |
| 19 | [COMP-STEP-01-070](case/COMP-STEP-01-070.md) | step 可选字段 id env if with 验证 | MISSING_SOURCE |
| 20 | [COMP-SYSENV-01-059](case/COMP-SYSENV-01-059.md) | ATOMGIT 系统环境变量关键变量存在性 | MISSING_SOURCE |
| 21 | [COMP-SYSENV-01-060](case/COMP-SYSENV-01-060.md) | ATOMGIT 系统环境变量值正确性 | MISSING_SOURCE |
| 22 | [COMP-TIMEOUT-01-001](case/COMP-TIMEOUT-01-001.md) | 未声明 timeout-minutes 的 job 在 360 分钟内正常完 | LLM_DEPENDENT, STATUS_GUARANTEED |
| 23 | [COMP-TRIG-01-078](case/COMP-TRIG-01-078.md) | 多事件组合与分支路径过滤验证 | STATUS_GUARANTEED, VACUOUS |
| 24 | [COMP-TRIG-01-079](case/COMP-TRIG-01-079.md) | 触发事件 types 取值与过滤边界验证 | STATUS_GUARANTEED, VACUOUS |
| 25 | [COMP-UNKNOWN-01-003](case/COMP-UNKNOWN-01-003.md) | 未声明 select 的 stage 与 job 默认被执行 | STATUS_GUARANTEED, VACUOUS |
| 26 | [COMP-VARREF-01-084](case/COMP-VARREF-01-084.md) | ${gitcode_*} 与 ${PIPELINE_*} 非标准插值的求值行 | LLM_DEPENDENT, VACUOUS |
| 27 | [COMP-WFLOW-01-061](case/COMP-WFLOW-01-061.md) | workflow name 与 on 字段必填与类型验证 | STATUS_GUARANTEED, VACUOUS |
| 28 | [COMP-WFLOW-01-062](case/COMP-WFLOW-01-062.md) | workflow env 与 defaults 字段验证 | MISSING_SOURCE, VACUOUS |
| 29 | [COMP-WFLOW-01-063](case/COMP-WFLOW-01-063.md) | workflow concurrency 并发控制字段验证 | STATUS_GUARANTEED, VACUOUS |
| 30 | [COMP-WFLOW-01-064](case/COMP-WFLOW-01-064.md) | workflow stages 阶段结构字段验证 | MISSING_SOURCE |
| 31 | [COMP-WFLOW-01-065](case/COMP-WFLOW-01-065.md) | workflow post 后处理阶段字段验证 | MISSING_SOURCE, VACUOUS |
| 32 | [COMPAT-CTX-01-005](case/COMPAT-CTX-01-005.md) | atomgit 缺位字段（job/run_attempt/triggerin | LLM_DEPENDENT, VACUOUS |
| 33 | [COMPAT-ENV-01-001](case/COMPAT-ENV-01-001.md) | ATOMGIT_SHA 环境变量应正确返回触发提交 SHA | LLM_DEPENDENT, STATUS_GUARANTEED |
| 34 | [COMPAT-ENV-01-004](case/COMPAT-ENV-01-004.md) | ATOMGIT_ENV 覆写系统默认变量的防护（对齐 GitHub 同名禁止 | LLM_DEPENDENT, MISSING_SOURCE |
| 35 | [COMPAT-ENV-01-005](case/COMPAT-ENV-01-005.md) | RUNNER_* 系列环境变量在 GitCode Runner 上的注入情况 | LLM_DEPENDENT, VACUOUS |
| 36 | [COMPAT-EXPR-01-001](case/COMPAT-EXPR-01-001.md) | success 关键字在条件表达式中的可用性 | VACUOUS |
| 37 | [COMPAT-INPUTS-01-001](case/COMPAT-INPUTS-01-001.md) | workflow_dispatch inputs 类型限制 - boolea | LLM_DEPENDENT, STATUS_GUARANTEED |
| 38 | [COMPAT-MASK-01-002](case/COMPAT-MASK-01-002.md) | 通过 env 注入 secret 后输出应在日志中被脱敏 | LLM_DEPENDENT, UNEXERCISED |
| 39 | [COMPAT-NEEDS-01-001](case/COMPAT-NEEDS-01-001.md) | needs 上下文存在性与 outputs/result 字段对齐（规格矛盾 | LLM_DEPENDENT, MISSING_SOURCE |
| 40 | [COMPAT-NEST-01-001](case/COMPAT-NEST-01-001.md) | workflow_call 嵌套层数 - 2 层正常执行 | STATUS_GUARANTEED |
| 41 | [COMPAT-NEST-01-002](case/COMPAT-NEST-01-002.md) | workflow_call 嵌套层数 - 3 层越界应报错 | LLM_DEPENDENT, STATUS_GUARANTEED |
| 42 | [COMPAT-PATHS-01-001](case/COMPAT-PATHS-01-001.md) | paths 过滤器 300 条边界测试 | STATUS_GUARANTEED, VACUOUS |
| 43 | [COMPAT-PATHS-01-002](case/COMPAT-PATHS-01-002.md) | paths 过滤器 301 条越界测试 | LLM_DEPENDENT, STATUS_GUARANTEED |
| 44 | [COMPAT-SCHEDULE-01-002](case/COMPAT-SCHEDULE-01-002.md) | schedule 不支持 timezone 字段差异 | LLM_DEPENDENT, STATUS_GUARANTEED |
| 45 | [COMPAT-WCMD-01-004](case/COMPAT-WCMD-01-004.md) | 注解命令 error/warning/notice 的不中断降级行为 | LLM_DEPENDENT, STATUS_GUARANTEED, VACUOUS |
| 46 | [COMPAT-WCMD-01-005](case/COMPAT-WCMD-01-005.md) | debug 命令默认可见性与 GitHub ACTIONS_STEP_DEB | LLM_DEPENDENT, VACUOUS |
| 47 | [COMPAT-YAML-01-001](case/COMPAT-YAML-01-001.md) | YAML 1.1 on 键布尔陷阱与 env 中 yes/no/on/off | LLM_DEPENDENT, VACUOUS |
| 48 | [REL-YAMLCACHE-01-060](case/REL-YAMLCACHE-01-060.md) | Workflow YAML 缓存失效——修改后无旧代码残留 | MISSING_SOURCE, VACUOUS |
| 49 | [USE-ACT-01-001](case/USE-ACT-01-001.md) | 使用裸插件名 checkout 时正常拉取官方 Action | IMPOSSIBLE |
| 50 | [USE-ACT-01-002](case/USE-ACT-01-002.md) | 使用 actions/checkout@v4 时报错应给出迁移指引 | IMPOSSIBLE, LLM_DEPENDENT |
| 51 | [USE-ANNOT-01-001](case/USE-ANNOT-01-001.md) | workflow 命令 ::error:: 与 ::warning:: 在日 | VACUOUS |
| 52 | [USE-BADGE-01-001](case/USE-BADGE-01-001.md) | workflow 运行完成后状态徽标及时回写且语义清晰 | IMPOSSIBLE, LLM_DEPENDENT |
| 53 | [USE-CONC-01-001](case/USE-CONC-01-001.md) | concurrency.max 配置 0 或 10 时报错应提示有效范围 1 | IMPOSSIBLE, LLM_DEPENDENT |
| 54 | [USE-CONC-01-002](case/USE-CONC-01-002.md) | concurrency.max 配置 -1 时报错应提示有效范围 | IMPOSSIBLE, LLM_DEPENDENT |
| 55 | [USE-CTX-01-001](case/USE-CTX-01-001.md) | 使用 atomgit 上下文时表达式正常求值 | MISSING_SOURCE |
| 56 | [USE-CTX-01-002](case/USE-CTX-01-002.md) | 使用 github 上下文时报错应提示 atomgit 替代 | IMPOSSIBLE, LLM_DEPENDENT |
| 57 | [USE-DEPR-01-001](case/USE-DEPR-01-001.md) | 使用 ATOMGIT_OUTPUT 文件协议时正常生效 | MISSING_SOURCE |
| 58 | [USE-DIR-01-001](case/USE-DIR-01-001.md) | workflow 放置于 .gitcode/workflows/ 下可正常触 | IMPOSSIBLE |
| 59 | [USE-DISP-01-001](case/USE-DISP-01-001.md) | workflow_dispatch 必填参数未提供时应给出明确校验错误 | IMPOSSIBLE, LLM_DEPENDENT |
| 60 | [USE-DISP-01-002](case/USE-DISP-01-002.md) | workflow_dispatch 未提供参数但存在 default 时应使 | MISSING_SOURCE |
| 61 | [USE-ENV-01-001](case/USE-ENV-01-001.md) | 使用 ATOMGIT_SHA 环境变量时正常取值 | VACUOUS |
| 62 | [USE-EXPR-01-001](case/USE-EXPR-01-001.md) | 引用不存在的上下文属性时报错应包含原始表达式与错误类型 | IMPOSSIBLE, LLM_DEPENDENT |
| 63 | [USE-EXPR-01-002](case/USE-EXPR-01-002.md) | 调用未知函数时报错应提示函数名错误与修正方向 | IMPOSSIBLE, LLM_DEPENDENT |
| 64 | [USE-INPT-01-001](case/USE-INPT-01-001.md) | 使用 string 类型 input 时正常通过校验 | IMPOSSIBLE |
| 65 | [USE-INPT-01-002](case/USE-INPT-01-002.md) | 使用 boolean 类型 input 时报错应提示仅支持 string | IMPOSSIBLE, LLM_DEPENDENT |
| 66 | [USE-LBL-01-001](case/USE-LBL-01-001.md) | runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表 | IMPOSSIBLE, LLM_DEPENDENT |
| 67 | [USE-LBL-01-006](case/USE-LBL-01-006.md) | 含资源池名的 runs-on 写法平台识别验证 | LLM_DEPENDENT, STATUS_GUARANTEED |
| 68 | [USE-LOG-01-001](case/USE-LOG-01-001.md) | 多 step 日志按时间线组织且边界清晰 | LLM_DEPENDENT, MISSING_SOURCE |
| 69 | [USE-MASK-01-001](case/USE-MASK-01-001.md) | secret 脱敏文档描述与实际行为一致并给出缓解建议 | LLM_DEPENDENT, UNEXERCISED |
| 70 | [USE-NEST-01-001](case/USE-NEST-01-001.md) | workflow_call 嵌套 3 层时报错应明确提示上限为 2 层 | IMPOSSIBLE, LLM_DEPENDENT |
| 71 | [USE-NEST-01-002](case/USE-NEST-01-002.md) | workflow_call 嵌套 2 层时应正常执行 | IMPOSSIBLE |
| 72 | [USE-OS-01-001](case/USE-OS-01-001.md) | runner.os 返回值与文档声明的平台支持一致 | LLM_DEPENDENT, MISSING_SOURCE |
| 73 | [USE-PERM-01-001](case/USE-PERM-01-001.md) | 使用 GitCode 权限域命名时正常生效 | IMPOSSIBLE |
| 74 | [USE-PERM-01-002](case/USE-PERM-01-002.md) | 使用 GitHub 权限域命名时报错应给出 GitCode 对照表 | IMPOSSIBLE, LLM_DEPENDENT |
| 75 | [USE-RUN-01-001](case/USE-RUN-01-001.md) | 使用三段式标签时 job 正常调度 | IMPOSSIBLE |
| 76 | [USE-RUN-01-002](case/USE-RUN-01-002.md) | 使用单标签 ubuntu-latest 时报错应给出三段式格式指引 | IMPOSSIBLE, LLM_DEPENDENT |
| 77 | [USE-SEARCH-01-001](case/USE-SEARCH-01-001.md) | 日志搜索与下载功能可用且交互流畅 | LLM_DEPENDENT, VACUOUS |
| 78 | [USE-SECNAME-01-001](case/USE-SECNAME-01-001.md) | Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误 | IMPOSSIBLE, LLM_DEPENDENT |
| 79 | [USE-SECNAME-01-002](case/USE-SECNAME-01-002.md) | Secret 名称以数字开头时应给出命名规则错误 | IMPOSSIBLE, LLM_DEPENDENT |
| 80 | [USE-STAT-01-002](case/USE-STAT-01-002.md) | 使用 success() 带括号时报错应提示 GitCode 括号差异 | IMPOSSIBLE, LLM_DEPENDENT |
| 81 | [USE-TYPE-01-001](case/USE-TYPE-01-001.md) | 使用 GitCode types 命名时正常触发 | IMPOSSIBLE |
| 82 | [USE-TYPE-01-002](case/USE-TYPE-01-002.md) | 使用 GitHub types 命名 opened/synchronize  | IMPOSSIBLE, LLM_DEPENDENT |
| 83 | [USE-YAML-01-001](case/USE-YAML-01-001.md) | 缺少必填字段 on 时报错应指出具体字段名与位置 | IMPOSSIBLE, LLM_DEPENDENT |
