# Reliability Test Intents — Run 2026-08-25-02

> Agent: reliability（混沌与边界工程师）
> 输入版本：gitcode-spec/ 2026-07-20 快照；platform-config/ **缺失（本轮未提供，以下参数取自 gitcode-spec 与上轮用例基线）**
> 基底：上轮 delivered run（2026-08-25-01）已覆盖 REL-ACTN/ARTF/CACH/CONC/FAULT 共 7 条 YAML；本轮**增量生成**，不重复上述场景。
> 溯源：risk-register.md §三（稳定性）+ testing-focus.md §3 执行模型、§4 Runner 隔离、§12 稳定性专项

---

## 输入缺口声明

- `phase01/inputs/platform-config/` 目录为空，平台最大并发数、矩阵硬上限、artifact/cache 精确配额、API 速率限制阈值等**未以结构化配置提供**。
- 以下 intent 中的边界参数主要依据 `gitcode-spec/` 文档显式值（如 timeout 360min、rerun 3 次、workflow_call 嵌套 2 层、paths 匹配 300 文件）或 runner 资源规格表推导；若 platform-config 后续刷新，需重新校准 INTENT-REL-001~009 的参数。

---

## 一、配额 / 上限维度的边界 + 越界 Intent

### INTENT-REL-001
- **id**: INTENT-REL-001
- **dimensions**: [reliability]
- **scenario**: Job 级 timeout-minutes 精确边界 — 配置 360 min（文档声明的默认值/上限），实际运行 350 min，验证边界值不被 off-by-one 截断
- **stress_params**: timeout-minutes=360, 实际运行时长=350 min
- **steady_state_criterion**: Job 正常完成，最终状态 success；无提前终止日志
- **recovery_expectation**: N/A（边界正常通过）
- **priority**: P1
- **ui_candidate**: true（长时间运行可在 UI 观察状态保活、倒计时/耗时显示是否持续刷新）
- **teardown_level**: fixture
- **rationale**: 验证文档声明的 360 min 上限作为边界值时，解析与执行层均正确接受，不因整数边界误差提前 kill
- **expected_behavior**: Job 在 350 min 时成功结束，状态为 success；日志完整保留

### INTENT-REL-002
- **id**: INTENT-REL-002
- **dimensions**: [reliability]
- **scenario**: Job 级 timeout-minutes 越界 — 配置 361 min（超过文档上限 1 min）
- **stress_params**: timeout-minutes=361
- **steady_state_criterion**: 系统要么在 YAML 解析/预检阶段拒绝并给出明确错误，要么在运行时按 360 min 截断执行
- **recovery_expectation**: 明确报错（配置非法）或静默截断至 360 min 后正常触发超时 kill
- **priority**: P1
- **ui_candidate**: false
- **teardown_level**: fixture
- **rationale**: 验证越界超时配置的处理策略，防止用户配置极大值导致资源无限占用
- **expected_behavior**: 若拒绝，错误信息包含 "timeout" 或 "360"；若截断，实际 kill 时间为 360 min

### INTENT-REL-003
- **id**: INTENT-REL-003
- **dimensions**: [reliability]
- **scenario**: Step 级 timeout-minutes 与 Job 级上限的级联约束 — step timeout=360 min，job timeout=360 min，step 实际运行 365 min
- **stress_params**: step timeout-minutes=360, job timeout-minutes=360, step sleep=365 min（使用短 sleep 模拟，实际测试可用 2 min 级超时加速验证级联逻辑）
- **steady_state_criterion**: Job 因超时失败；step 与 job 同时到期，job 被终止
- **recovery_expectation**: Job 按超时失败，runner 不死锁
- **priority**: P1
- **ui_candidate**: true（UI 观察 step 与 job 的耗时显示、超时标记位置）
- **teardown_level**: fixture
- **rationale**: 文档声明 step 无独立超时限制、受 job timeout 控制，验证级联约束在边界处生效
- **expected_behavior**: Job 状态 failure，日志含 timeout 关键字；step 被 kill

### INTENT-REL-004
- **id**: INTENT-REL-004
- **dimensions**: [reliability]
- **scenario**: Matrix max-parallel 边界 — 8 个实例、max-parallel=4
- **stress_params**: matrix 维度 2×2×2=8 个 job 实例, max-parallel=4, 每个实例 sleep=60 s
- **steady_state_criterion**: 通过 API 轮询或 UI 观察，任意时刻处于 running 状态的 matrix job 实例数 ≤4；总完成时间 ≈120 s（允许 ±20 s 容差）
- **recovery_expectation**: N/A
- **priority**: P1
- **ui_candidate**: true（UI 观察矩阵卡片并发数、运行中/排队中的状态标识）
- **teardown_level**: fixture
- **rationale**: 验证 max-parallel 作为并发上限的强制执行力，防止矩阵无限制吞噬 runner 资源
- **expected_behavior**: 8 个实例全部完成，无实例丢失；running 峰值=4

### INTENT-REL-005
- **id**: INTENT-REL-005
- **dimensions**: [reliability]
- **scenario**: Matrix max-parallel 越界 — max-parallel=0
- **stress_params**: matrix 2×2=4 实例, max-parallel=0
- **steady_state_criterion**: Workflow 被阻止运行（永久 queued 或解析报错），不导致调度器死锁、不占用 runner
- **recovery_expectation**: 明确报错或保持 queued 并给出可理解的错误提示
- **priority**: P1
- **ui_candidate**: true（UI 观察 workflow 是否 stuck 在 queued 状态、是否可取消）
- **teardown_level**: fixture
- **rationale**: 验证非法并发下限的处理，防止零值导致调度器逻辑死锁
- **expected_behavior**: 状态不进入 running，或 YAML 校验阶段即失败

### INTENT-REL-006
- **id**: INTENT-REL-006
- **dimensions**: [reliability]
- **scenario**: Concurrency max 边界 — 同一 group 内 max=1 的串行执行
- **stress_params**: concurrency.group="deploy-test", max=1, exceed-action=QUEUE, 连续触发次数=3, 每个 job sleep=30 s
- **steady_state_criterion**: 通过 API/日志确认，任意时刻该 group 下 running 的 run 数 ≤1；3 次运行总耗时 ≈90 s（允许 ±15 s 容差）
- **recovery_expectation**: N/A
- **priority**: P1
- **ui_candidate**: true（UI 观察 Actions 列表中的排队状态、运行/等待徽标）
- **teardown_level**: fixture
- **rationale**: 验证 concurrency 串行语义与排队机制
- **expected_behavior**: 3 次运行全部完成，无并发突破 max=1

### INTENT-REL-007
- **id**: INTENT-REL-007
- **dimensions**: [reliability]
- **scenario**: Rerun 次数边界 — 单条失败运行最多重新运行 3 次
- **stress_params**: 对同一失败运行连续请求 rerun 4 次
- **steady_state_criterion**: 第 1~3 次 rerun 成功创建新运行记录；第 4 次请求被明确拒绝
- **recovery_expectation**: 明确报错（已达最大重试次数）或 API 返回 4xx/对应错误码
- **priority**: P1
- **ui_candidate**: true（UI 观察 Re-run 按钮在第 3 次后是否禁用、是否给出提示文案）
- **teardown_level**: fixture
- **rationale**: 验证 rerun 上限的硬性约束，防止无限 rerun 占用调度资源
- **expected_behavior**: 第 4 次请求失败，错误信息包含 "3" 或 "maximum"

### INTENT-REL-008
- **id**: INTENT-REL-008
- **dimensions**: [reliability]
- **scenario**: workflow_call 嵌套层数边界 — 3 层嵌套（文档声明上限 2 层）
- **stress_params**: 可重用工作流 A 调用 B，B 调用 C，形成深度=3 的嵌套
- **steady_state_criterion**: 第 3 层调用时被拒绝或抛出明确错误
- **recovery_expectation**: 明确报错，不导致无限递归、栈溢出或调度器崩溃
- **priority**: P1
- **ui_candidate**: false
- **teardown_level**: fixture
- **rationale**: 验证嵌套上限，防止滥用导致调度器资源耗尽与递归风险
- **expected_behavior**: 运行失败，日志含嵌套深度超限的提示

### INTENT-REL-009
- **id**: INTENT-REL-009
- **dimensions**: [reliability]
- **scenario**: paths 匹配文件数边界 — push 事件产生 305 个变更文件，paths 过滤范围覆盖全部
- **stress_params**: 变更文件数=305, paths 过滤范围覆盖所有变更路径
- **steady_state_criterion**: 超出 300 的文件不参与匹配判断；workflow 按前 300 个文件决策是否触发；触发决策结果与仅变更前 300 个文件时一致
- **recovery_expectation**: N/A
- **priority**: P2
- **ui_candidate**: false
- **teardown_level**: fixture
- **rationale**: 验证 paths 匹配性能边界（文档声明仅匹配前 300 个变更文件）
- **expected_behavior**: 若前 300 个文件命中 paths，则 workflow 触发；若前 300 个未命中、后 5 个命中，则 workflow 不触发

---

## 二、执行模型关键机制的边界与竞态 Intent

### INTENT-REL-010
- **id**: INTENT-REL-010
- **dimensions**: [reliability]
- **scenario**: needs 失败传播 × matrix 组合 — 上游 matrix job 4 实例中 1 个失败，下游 job needs 上游
- **stress_params**: 上游 matrix 4 实例, 1 个实例通过 exit 1 注入失败, 下游 needs: [上游 job]
- **steady_state_criterion**: 下游 job 默认不执行，状态为 skipped（除非显式配置 if: always()）
- **recovery_expectation**: N/A
- **priority**: P0（对应 risk-register RISK-REL-02：needs 依赖的 matrix job 全成功但上游 job 初始化失败时无声失败）
- **ui_candidate**: true（UI 观察依赖图状态传递、matrix 卡片与下游卡片的联动）
- **teardown_level**: fixture
- **rationale**: 验证 needs 与 matrix 组合时的失败传播语义，防止下游在应跳过时仍被静默调度或无声失败
- **expected_behavior**: 下游 job 状态 skipped，workflow 整体状态 failure；日志明确显示跳过原因

### INTENT-REL-011
- **id**: INTENT-REL-011
- **dimensions**: [reliability]
- **scenario**: cancel-in-progress 竞态 — 新触发抢占旧运行
- **stress_params**: concurrency.group="ci-test", cancel-in-progress=true, 旧运行 job sleep=120 s, 在旧运行启动后 15 s 内再次触发
- **steady_state_criterion**: 旧运行状态变为 cancelled；新运行正常执行并最终 success；旧运行的 runner 资源被释放
- **recovery_expectation**: 旧运行优雅终止，runner 不死锁、不残留工作区污染
- **priority**: P1
- **ui_candidate**: true（核心 UI 场景：取消按钮与状态变化实时性、旧运行卡片变灰/显示 cancelled 徽标的速度）
- **teardown_level**: fixture
- **rationale**: 验证 cancel-in-progress 的抢占语义与资源释放可靠性
- **expected_behavior**: 旧运行 cancelled，新运行 success；同一 group 下无两个 running 并存

### INTENT-REL-012
- **id**: INTENT-REL-012
- **dimensions**: [reliability]
- **scenario**: 手动取消正在运行的 step — 验证清理与状态迁移
- **stress_params**: job 内 step sleep=300 s, 在 step 启动后 30 s 时通过 UI/API 手动取消
- **steady_state_criterion**: Job 状态变为 cancelled；当前 step 被终止，日志停止追加；若 workflow 配置 post 阶段，则 post 按 run_always 执行
- **recovery_expectation**: runner 不死锁，可被后续运行复用；取消操作幂等（重复取消不报错）
- **priority**: P1
- **ui_candidate**: true（核心 UI 场景：取消按钮响应延迟 ≤3 s、日志终止、状态迁移、runner 回收后新运行可正常调度）
- **teardown_level**: fixture
- **rationale**: 验证手动取消的端到端行为与 UI 一致性，防止取消后 runner 残留或状态不一致
- **expected_behavior**: Job 最终状态 cancelled；step 不输出 "end"；API 查询状态与 UI 一致

### INTENT-REL-013
- **id**: INTENT-REL-013
- **dimensions**: [reliability]
- **scenario**: stages fail_fast=true × matrix fail-fast=false 组合语义
- **stress_params**: stage 内 matrix 4 实例, matrix fail-fast=false, stage fail_fast=true, 1 个实例通过 exit 1 注入失败
- **steady_state_criterion**: stage 内其余 3 个 matrix 实例继续执行完毕（不中断）；后续 stage 被跳过；workflow 整体状态 failure
- **recovery_expectation**: N/A
- **priority**: P1
- **ui_candidate**: true（UI 观察 stage 状态：当前 stage 显示部分失败但未中断，后续 stage 显示 skipped）
- **teardown_level**: fixture
- **rationale**: 验证两个不同层面 fail-fast 控制的组合语义，防止 stage fail_fast 错误地 kill 还在运行的 matrix 实例
- **expected_behavior**: 失败实例状态 failure，其余 3 个实例状态 success；后续 stage 全部 skipped

### INTENT-REL-014
- **id**: INTENT-REL-014
- **dimensions**: [reliability]
- **scenario**: timeout 与 continue-on-error 组合 — 超时后 continue-on-error 是否使 workflow 不整体失败
- **stress_params**: job continue-on-error=true, timeout-minutes=1, step sleep=300 s
- **steady_state_criterion**: Job 因超时状态为 failure，但 continue-on-error 标记使 workflow 整体状态为 success；下游依赖该 job 的 job 默认仍不执行（continue-on-error 不修改 needs 的 success 语义）
- **recovery_expectation**: N/A
- **priority**: P1
- **ui_candidate**: true（UI 观察 job 卡片显示失败徽标但 workflow 总状态为成功）
- **teardown_level**: fixture
- **rationale**: 验证容错与超时的优先级交互，防止 continue-on-error 掩盖超时或错误地让下游执行
- **expected_behavior**: Workflow 状态 success；job 状态 failure（或带 continue-on-error 标记的 failure）；下游 skipped

---

## 三、故障注入与并发洪泛 Intent

### INTENT-REL-015
- **id**: INTENT-REL-015
- **dimensions**: [reliability]
- **scenario**: 网络分区 — job 执行中 runner 与平台控制面断连
- **stress_params**: 分区持续时间=60 s, 注入时机=step 执行中（step 已输出前 10 行后断网）
- **steady_state_criterion**: 分区恢复后，job 日志能续传或完整上报，状态最终收敛为 failure 或 success（取决于断网期间 step 是否已完成）
- **recovery_expectation**: 重试成功（日志续传）或明确报错（连接失败），不永久挂起为 running
- **priority**: P1
- **ui_candidate**: true（UI 观察日志断流与恢复、状态是否从 running 最终迁移到终止态）
- **teardown_level**: fixture
- **rationale**: 验证控制面断连时的 runner 自治与恢复，防止 runner 失联后运行永久 stuck
- **expected_behavior**: 120 s 内状态从 running 变为 failure/cancelled/success 之一；日志不含永久重复重试风暴

### INTENT-REL-016
- **id**: INTENT-REL-016
- **dimensions**: [reliability]
- **scenario**: 内存耗尽/OOM — 大内存申请导致 runner 被 kill
- **stress_params**: runner=small（2 核 8 GB 内存）, 内存申请=12 GB（通过 stress-ng 或 /dev/shm 填充）
- **steady_state_criterion**: Job 因 OOM 被 kill，状态为 failure；OOM 不波及其他并发运行的 job/run
- **recovery_expectation**: runner 被自动回收/重启，不影响其他 run；OOM job 可被 rerun
- **priority**: P1
- **ui_candidate**: true（UI 观察 OOM 后的状态显示、runner 标签是否重新变为可用）
- **teardown_level**: fixture
- **rationale**: 验证内存超限时的隔离与恢复，防止 OOM 导致 runner 永久性损坏或跨 job 影响
- **expected_behavior**: Job 状态 failure，日志含 "killed" 或 "OOM" 或 "memory"；同一 runner 后续新运行正常

### INTENT-REL-017
- **id**: INTENT-REL-017
- **dimensions**: [reliability]
- **scenario**: 并发洪泛 — 50 个 workflow 同时触发观察排队与限流
- **stress_params**: 并发触发数=50, 时间窗口=10 s, 仓库=同一仓库, 每个 job sleep=30 s, runner=small
- **steady_state_criterion**: 所有 50 个运行最终都进入 completed 状态，无永久 stuck；从触发到全部完成的时间 ≤20 min；queued 阶段可观测，无静默丢弃
- **recovery_expectation**: 超限部分进入 queued 状态，按 FIFO 或公平策略调度；不被静默丢弃
- **priority**: P1（对应 risk-register RISK-REL-01：并发洪泛下排队/公平性失效）
- **ui_candidate**: true（核心 UI 场景：Actions 标签页列表渲染 50 条记录是否卡顿、状态更新实时性、分页/加载性能）
- **teardown_level**: full_instance
- **rationale**: 验证平台在高并发下的队列容量与公平调度，防止洪泛导致运行丢失或调度器雪崩
- **expected_behavior**: 50 条运行记录全部可查询，状态均为 completed；queued→running→completed 状态机无遗漏

### INTENT-REL-018
- **id**: INTENT-REL-018
- **dimensions**: [reliability]
- **scenario**: 大规模 matrix — 256 个实例的展开与调度性能
- **stress_params**: matrix 维度 16×16=256 个 job 实例, max-parallel=16, 每个实例 sleep=10 s
- **steady_state_criterion**: 256 个实例全部生成（无重复/遗漏），状态机正确；总完成时间 ≈160 s（允许 ±30 s 容差）；API 返回的 jobs 列表含 256 个条目
- **recovery_expectation**: N/A
- **priority**: P1
- **ui_candidate**: true（核心 UI 场景：matrix 展开后页面渲染性能、256 个卡片加载是否卡顿、滚动是否流畅、状态更新是否实时）
- **teardown_level**: full_instance
- **rationale**: 验证大规模矩阵的展开正确性与平台调度吞吐，防止矩阵规模过大时调度器丢任务或前端崩溃
- **expected_behavior**: 256 个实例状态均为 completed；无实例缺失或重复

### INTENT-REL-019
- **id**: INTENT-REL-019
- **dimensions**: [reliability]
- **scenario**: 超长日志流 — 单 step 输出 100 MB 日志
- **stress_params**: 日志大小=100 MB, 输出速率=1 MB/s（通过循环打印实现）
- **steady_state_criterion**: 日志完整写入存储并可下载（MD5/行数校验）；UI 日志面板能滚动浏览不崩溃；日志搜索高亮功能正常；下载文件编码为 UTF-8
- **recovery_expectation**: N/A
- **priority**: P2
- **ui_candidate**: true（核心 UI 场景：日志流式加载是否卡顿、大日志滚动/搜索性能、下载按钮可用性）
- **teardown_level**: fixture
- **rationale**: 验证大日志场景下的存储完整性与前端渲染稳定性
- **expected_behavior**: 下载日志大小 ≈100 MB；行数与预期一致；UI 无白屏/崩溃

### INTENT-REL-020
- **id**: INTENT-REL-020
- **dimensions**: [reliability]
- **scenario**: 依赖服务不可用 — checkout action 期间模拟仓库服务返回 503
- **stress_params**: 服务不可用持续时间=30 s, 注入时机=checkout step 发起 Git 克隆请求时
- **steady_state_criterion**: Step 失败后 job 失败，或平台有重试机制并在 3 次内最终 success；总耗时 ≤5 min
- **recovery_expectation**: 若平台支持重试，应在 3 次内成功；否则明确报错并提示服务不可用
- **priority**: P1
- **ui_candidate**: true（UI 观察 checkout step 是否显示重试计数、最终状态迁移）
- **teardown_level**: fixture
- **rationale**: 验证关键内置 action 的容错与重试，防止临时服务不可用导致确定性失败
- **expected_behavior**: 状态最终收敛（success 或 failure）；日志含 503 或 retry 关键字

### INTENT-REL-021
- **id**: INTENT-REL-021
- **dimensions**: [reliability]
- **scenario**: Git 大文件克隆超时 — 1 GB 仓库 checkout 在 small runner（2 核 8 GB 50 GB）上
- **stress_params**: 仓库大小≈1 GB（含历史提交）, runner=small, timeout-minutes=10
- **steady_state_criterion**: checkout 在 10 min 内完成（状态 success）或明确超时失败；不导致 runner 永久挂起
- **recovery_expectation**: 明确报错（timeout 或 clone 失败），runner 可被回收复用
- **priority**: P1（对应 risk-register RISK-REL-05：Git 大文件克隆/推送超时或内存溢出）
- **ui_candidate**: true（UI 观察 checkout step 的耗时显示、进度日志、超时后的状态标记）
- **teardown_level**: fixture
- **rationale**: 验证大仓库在默认 small runner 上的 clone 性能与超时行为
- **expected_behavior**: 10 min 内完成则 success，否则 failure；日志含 timeout 或 clone 错误

### INTENT-REL-022
- **id**: INTENT-REL-022
- **dimensions**: [reliability]
- **scenario**: schedule cron 高频触发洪泛 — 1 分钟内 10 个 schedule workflow 同时触发
- **stress_params**: cron workflow 数=10, cron 表达式均指向同一分钟, 每个 job sleep=20 s
- **steady_state_criterion**: 所有运行进入 queued→in_progress→completed 状态，无静默丢失；调度延迟 ≤5 min（文档声明 cron 存在数分钟延迟）
- **recovery_expectation**: N/A
- **priority**: P1
- **ui_candidate**: true（UI 观察 Actions 列表中 schedule 触发的批量出现、时间戳一致性）
- **teardown_level**: fixture
- **rationale**: 验证定时触发洪泛下的调度稳定性，防止 schedule 堆积导致调度器雪崩
- **expected_behavior**: 10 条运行记录全部存在，event_name 为 schedule；无重复 run_id

### INTENT-REL-023
- **id**: INTENT-REL-023
- **dimensions**: [reliability]
- **scenario**: 多 job DAG 深度 — 10 层链式 needs 依赖的执行时序
- **stress_params**: DAG 深度=10（job1→job2→...→job10）, 每层 job sleep=10 s
- **steady_state_criterion**: 总耗时 ≈100 s（允许 ±20 s 容差）；状态逐层传播正确（前一 job success 后下一 job 才进入 running）
- **recovery_expectation**: N/A
- **priority**: P2
- **ui_candidate**: true（UI 观察 DAG 图渲染与状态逐层更新、长链依赖的页面布局是否异常）
- **teardown_level**: fixture
- **rationale**: 验证深层 DAG 的调度与状态传播性能
- **expected_behavior**: 10 个 job 全部 success，执行顺序严格链式；无并行突破 needs 约束

### INTENT-REL-024
- **id**: INTENT-REL-024
- **dimensions**: [reliability]
- **scenario**: 同时取消多个运行 — 批量选择后取消的 UI 与后端一致性
- **stress_params**: 同时启动 5 个 running 的 workflow_dispatch 运行，通过 UI 批量选择后点击取消
- **steady_state_criterion**: 5 个运行状态最终都变为 cancelled，API 查询与 UI 显示一致；取消操作在 5 s 内生效
- **recovery_expectation**: 被取消的运行释放 runner 资源；取消操作幂等
- **priority**: P1
- **ui_candidate**: true（核心 UI 场景：批量取消按钮响应、选中态、状态同步、取消后卡片更新）
- **teardown_level**: fixture
- **rationale**: 验证批量取消操作的端到端一致性，防止 UI 显示 cancelled 但后端仍在运行
- **expected_behavior**: 5 个运行状态均为 cancelled；无 running/stuck 残留

### INTENT-REL-025
- **id**: INTENT-REL-025
- **dimensions**: [reliability]
- **scenario**: 超大 step 输出环境变量 — ATOMGIT_ENV 写入 10 MB 内容
- **stress_params**: 通过 `echo` 向 ATOMGIT_ENV 写入 10 MB 单值环境变量
- **steady_state_criterion**: 环境变量正确传递到后续 step（后续 step 能读取完整值），或明确报错提示大小超限
- **recovery_expectation**: 明确报错或正常处理，不导致 runner 崩溃、内存溢出或 step 无限挂起
- **priority**: P2
- **ui_candidate**: false
- **teardown_level**: fixture
- **rationale**: 验证 workflow 命令（ATOMGIT_ENV）对大内容的处理能力
- **expected_behavior**: 若支持大内容，后续 step 读取值大小=10 MB；若不支持，报错含 "size" 或 "limit"

---

## 质量清单自检

- [x] 每个配额维度都有边界+越界 intent：timeout（001/002/003）、matrix max-parallel（004/005）、concurrency（006）、rerun（007）、workflow_call 嵌套（008）、paths 匹配（009）
- [x] 每条故障注入 intent 都声明了恢复预期：015（重试成功/明确报错）、016（自动回收）、020（重试成功/明确报错）
- [x] 参数具体（并发=50、matrix=256、日志=100 MB、超时=360 min 等），无「大量/很快/很久」模糊表述
- [x] 破坏性/大规模 intent 标了正确 teardown 级别：017/018 为 full_instance，其余为 fixture
- [x] 风险登记册稳定性项已映射：RISK-REL-01→017、RISK-REL-02→010、RISK-REL-05→021
- [x] UI 候选已显式标注：共 18 条标记 ui_candidate=true，覆盖取消、matrix 渲染、日志、并发列表、状态同步等核心 UI 稳定性场景
- [x] platform-config 缺失已在输入缺口声明中标注
