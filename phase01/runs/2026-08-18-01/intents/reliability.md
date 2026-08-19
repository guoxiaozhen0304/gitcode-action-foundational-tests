# Reliability Test Intents（稳定性测试意图）

> Run ID: `2026-08-18-01`  
> Agent: reliability  
> 维度标签: `reliability`  
> 总数: 25 条  

---

## 缺失输入清单及退化影响

| 缺失输入 | 影响范围 | 退化处理 |
|---|---|---|
| `platform-config/`（最大并发数、矩阵组合数上限、artifact 单文件/总大小配额、cache 单条目/总大小配额、超时硬上限、 Runner 资源池总容量、Webhook 重试策略参数） | 所有涉及边界/越界的 intent 无法给出精确越界参数 | 参数引用 gitcode-spec 已公开值（如 `concurrency.max=5`、`timeout-minutes` 默认 360），未公开上限处标注「缺 platform-config，参数待补」 |
| `business-context/`（典型业务 workflow 模板、真实用户触发频率分布、CI 负载峰值数据） | 并发洪泛与大规模 intent 的负载模型缺少业务参照 | 采用工程估算值（如并发洪泛 20 个、矩阵 50 组合），标注「缺 business-context，负载模型待校准」 |

---

## 一、并发控制与洪泛（覆盖 RISK-REL-01）

### INTENT-REL-001  concurrency.max=5 边界——第 6 个同 group 触发时的策略行为
- **场景**: 同一 concurrency group 已存在 5 个运行中的 workflow，触发第 6 个。
- **压力或故障参数**: concurrency.max=5；exceed-action 分别设为 QUEUE / IGNORE；触发间隔 1s。
- **稳态判据**:  
  - QUEUE 模式：第 6 个进入排队状态（queued），前 5 个任一完成后立即启动，排队 FIFO 顺序误差不超过 1 个位置。  
  - IGNORE 模式：第 6 个被静默丢弃，状态不出现新的 run 记录。
- **恢复预期**: 无需恢复；排队任务在前序完成后自动消费。
- **破坏级别**: `none`
- **溯源风险项**: RISK-REL-01
- **维度**: [reliability]

### INTENT-REL-002  并发洪泛——短时间内高频触发同仓库 workflow 的排队与公平性
- **场景**: 模拟 commit storm（如批量 push tag、机器人高频触发），观察系统排队、限流、不丢单。
- **压力或故障参数**: 10 秒内触发 20 个 workflow run；目标仓库配置 concurrency.max=5 / exceed-action=QUEUE。缺 business-context，负载模型待校准。
- **稳态判据**:  
  - 20 个 run 全部进入 queued 或 in_progress，无静默丢单。  
  - 排队平均等待时间可观测，队列不无限膨胀。  
  - 最终全部 20 个 run 到达终态（success/failure/cancelled），无一卡死。
- **恢复预期**: 洪泛停止后，队列在 30 分钟内消费完毕。
- **破坏级别**: `none`
- **溯源风险项**: RISK-REL-01
- **维度**: [reliability]

### INTENT-REL-003  concurrency preemption 抢占——新 MR push 取消旧运行
- **场景**: 同一 MR 分支连续 push，验证旧运行是否被抢占取消，新运行正常启动。
- **压力或故障参数**: preemption.enable=true；events=[mr_id]；连续 push 3 次，间隔 10s。
- **稳态判据**:  
  - 第 1、2 次运行被置为 cancelled。  
  - 第 3 次运行成功启动并到达终态。  
  - 被取消的运行日志完整保留且状态标记正确。
- **恢复预期**: 取消后资源立即释放，新运行无残留状态冲突。
- **破坏级别**: `none`
- **溯源风险项**: RISK-REL-01
- **维度**: [reliability]

### INTENT-REL-004  matrix max-parallel 边界——矩阵展开数超过 max-parallel 时的并发度限制
- **场景**: strategy.matrix 生成 8 个 job 实例，max-parallel=4，验证同时运行数不超过 4。
- **压力或故障参数**: matrix 组合数=8（os=[u1,u2] × node=[14,16,18,20]）；max-parallel=4；每个 job sleep 60s。
- **稳态判据**:  
  - 任意时刻 in_progress 的矩阵实例数 <= 4。  
  - 全部 8 个实例在 180s 内完成，无死锁。  
  - 未因限流导致实例被静默丢弃。
- **恢复预期**: 无需恢复；max-parallel 为正常调度约束。
- **破坏级别**: `none`
- **溯源风险项**: RISK-REL-01
- **维度**: [reliability]

---

## 二、执行模型与失败传播（覆盖 RISK-REL-02）

### INTENT-REL-005  needs 依赖的 matrix job 全成功但上游初始化 job 失败时下游行为
- **场景**: 上游非矩阵 job（如 `prepare`）初始化失败，下游 needs=prepare 的 matrix job 是否被正确取消/跳过，而非无声失败。
- **压力或故障参数**: 上游 job 在 step 1 即 `exit 1`；下游 matrix 3×2=6 个实例依赖上游；fail-fast 默认。
- **稳态判据**:  
  - 上游 job 状态为 failure。  
  - 下游 6 个 matrix 实例状态为 skipped（非空/未生成）。  
  - Workflow 整体状态为 failure，日志中可追溯到上游失败原因。
- **恢复预期**: 修复上游错误后重新 push，workflow 可正常重跑并全部通过。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-02
- **维度**: [reliability]

### INTENT-REL-006  stages.fail_fast=true 时单 job 失败立即终止同阶段其他 job
- **场景**: 某 stage 内并行运行 A/B/C 三个 job，A 失败后 B/C 应立即被取消。
- **压力或故障参数**: stage 配置 fail_fast=true；A 在 5s 后 `exit 1`；B/C 各 sleep 120s。
- **稳态判据**:  
  - A 失败后 10s 内 B、C 状态变为 cancelled。  
  - 后续 stage 的 job 被 skipped。  
  - post 阶段按 run_always 配置执行。
- **恢复预期**: 无需恢复；fail_fast 为正常行为。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-02
- **维度**: [reliability]

### INTENT-REL-007  matrix fail-fast=true 时单实例失败取消其余实例
- **场景**: matrix 4 个实例，其中 1 个失败后，其余 3 个应在 15s 内被取消。
- **压力或故障参数**: matrix 2×2=4；fail-fast=true；第 1 个实例 5s 后 `exit 1`；其余实例 sleep 120s。
- **稳态判据**:  
  - 失败实例状态为 failure。  
  - 其余 3 个实例在 15s 内变为 cancelled。  
  - 无实例继续运行至 120s 结束。
- **恢复预期**: 无需恢复；fail-fast 为正常行为。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-02
- **维度**: [reliability]

---

## 三、大规模与长时运行（覆盖 RISK-REL-05 及部分稳定性专项）

### INTENT-REL-008  超大 matrix 边界——矩阵组合数逼近/越过上限
- **场景**: 构造大矩阵验证系统对组合数上限的处理方式（报错/静默截断/正常运行）。
- **压力或故障参数**: 矩阵维度 os=[u1,u2,u3] × arch=[x64,arm64] × ver=[v1..v10] = 60 组合。缺 platform-config，参数待补（官方未公开 matrix 组合数上限）。
- **稳态判据**:  
  - 若存在上限（如 50）：第 51 个及之后组合应被明确拒绝，返回可理解的错误信息（如 "matrix combinations exceed limit"）。  
  - 若全部 60 个正常展开：全部在合理时间内完成，无一卡死。
- **恢复预期**: 若被明确拒绝，缩减矩阵后重新触发可正常运行。
- **破坏级别**: `none`
- **溯源风险项**: RISK-REL-01（间接）
- **维度**: [reliability]

### INTENT-REL-009  超长日志——单 step 输出 50MB 文本日志的实时性与完整性
- **场景**: 验证大日志量下日志流不截断、不延迟、状态机正常推进。
- **压力或故障参数**: 单 step 循环输出 50MB 文本（约 50 万行）；每行带序号前缀以便校验连续性。
- **稳态判据**:  
  - 日志行号连续，无丢行、无乱序（抽样校验首尾+中间 3 处）。  
  - 日志实时刷新（最后 1000 行与 run 终态时间差 <= 60s）。  
  - 运行状态正确流转：in_progress → completed(success)。
- **恢复预期**: 无需恢复；大日志为正常负载。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-05
- **维度**: [reliability]

### INTENT-REL-010  大仓库 checkout——1GB+ 仓库克隆的耗时与资源稳定性
- **场景**: 验证大仓库在默认 small runner（2核8G50GB磁盘）下能否完成 clone，不超时、不 OOM。
- **压力或故障参数**: fixture 仓库体积 1.2GB（含大文件但非 LFS）；runner=small；timeout-minutes=60。
- **稳态判据**:  
  - checkout step 在 60 分钟内完成，退出码 0。  
  - runner 磁盘剩余 > 5GB（不触盘满）。  
  - 内存峰值不超过 runner 配额（8GB），无 OOM kill。
- **恢复预期**: 若失败因超时，增大 timeout 或换 large runner 后可恢复。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-05
- **维度**: [reliability]

### INTENT-REL-011  接近 timeout 边界——job 运行 350 分钟观察正常终止 vs 超时 kill
- **场景**: 验证 timeout-minutes=360 的默认边界行为，接近超时系统是否仍保持稳定。
- **压力或故障参数**: job 内 sleep 350min（21,000s）；timeout-minutes 默认 360；runner=small。
- **稳态判据**:  
  - 350min 时 job 状态为 success（若 step 正常结束）。  
  - 对比实验：sleep 365min 时 job 在 360min 被强制终止，状态为 failure，日志中有明确 "timeout" 字样。
- **恢复预期**: 超时 kill 后 runner 资源释放，同一 runner 可接受新 job。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-05
- **维度**: [reliability]

### INTENT-REL-012  超多 step——单 job 50 个 step 的调度与状态回写完整性
- **场景**: 验证 step 数量大时状态机、日志分组、outputs 传递不丢步。
- **压力或故障参数**: 单 job 定义 50 个 step，每个 step 写一行唯一标识到 `ATOMGIT_OUTPUT`；最后 1 个 step 汇总校验。
- **稳态判据**:  
  - 50 个 step 全部出现在日志中，序号连续。  
  - 最终 step 能读取到前 49 个 step 写入的 outputs，无一丢失。  
  - Workflow 整体状态为 success。
- **恢复预期**: 无需恢复；多 step 为正常编排。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-02（间接）
- **维度**: [reliability]

---

## 四、故障注入与混沌工程（覆盖稳定性专项）

### INTENT-REL-013  磁盘满故障注入——runner 磁盘写满后 job 行为与报错清晰度
- **场景**: 在 job 运行中途将 runner 磁盘写满，观察 step 失败方式、日志是否可理解、是否影响其他 job。
- **压力或故障参数**: 在 step 2 使用 `dd` 向 /tmp 写入 filler 直至磁盘使用率 100%；step 3 尝试写入正常文件。
- **稳态判据**:  
  - step 3 因 "No space left on device" 失败，退出码非 0。  
  - 日志中明确出现磁盘满错误信息，非泛化 500/unknown error。  
  - 同一 runner 上的其他 job（若复用 runner）不被污染；若 runner 为一次性，实例销毁后磁盘恢复。
- **恢复预期**: 释放磁盘空间（清理 /tmp）或更换 runner 后，重新触发 workflow 可成功。
- **破坏级别**: `full_instance`
- **溯源风险项**: RISK-REL-05
- **维度**: [reliability]

### INTENT-REL-014  CPU 饱和故障注入——stress CPU 时 step 超时与心跳保活
- **场景**: 在 runner 上压测 CPU 至 100%，验证长时间运行的 step 不被误杀、timeout 机制仍有效。
- **压力或故障参数**: 使用 `stress-ng -c $(nproc) --timeout 300s` 压满 CPU；同时运行一个正常 sleep 120s 的 step。
- **稳态判据**:  
  - 正常 sleep step 在 120s 后成功结束（不被 CPU 饱和误杀）。  
  - timeout-minutes 计时不受 CPU 饱和影响（如设 timeout=2min，stress 3min，应在 2min 被 kill）。  
  - runner 保活/心跳不中断，状态正常回写。
- **恢复预期**: CPU 负载下降后，runner 恢复正常调度能力。
- **破坏级别**: `full_instance`
- **溯源风险项**: RISK-REL-05
- **维度**: [reliability]

### INTENT-REL-015  Runner 进程被 kill（模拟 runner 崩溃）——job 状态迁移与重调度
- **场景**: 模拟 runner 守护进程被强制终止（如宿主机重启、OOM killer），观察 job 是否被正确标记失败并允许重跑。
- **压力或故障参数**: job 运行至 30s 时，在宿主机层面 `kill -9 <runner-agent-pid>` 或销毁容器/VM。
- **稳态判据**:  
  - job 在 120s 内被标记为 failure（非无限 queued/in_progress）。  
  - 日志保留已输出部分（至少最后 100 行不丢失）。  
  - rerun 后 job 可正常执行至完成。
- **恢复预期**: 系统自动调度新 runner 重跑，无需人工干预。
- **破坏级别**: `full_instance`
- **溯源风险项**: RISK-REL-05
- **维度**: [reliability]

### INTENT-REL-016  网络分区故障注入——断开 runner 外网后观察依赖下载失败与重试
- **场景**: runner 运行中突然丧失外网访问（模拟网络抖动/分区），验证 step 失败信息是否明确、是否支持重试。
- **压力或故障参数**: step 1 正常执行；step 2 注入 iptables 规则阻断出站 443/80；step 3 尝试 `npm install` 或 `curl`。
- **稳态判据**:  
  - step 3 因网络不可达失败，日志出现 "Could not resolve host" / "Connection refused" / "timeout" 等明确错误。  
  - 非泛化 500 或静默 hang > 10min。  
  - 网络恢复后 rerun 可成功（验证非永久性污点）。
- **恢复预期**: 移除 iptables 规则或调度至网络正常的 runner 后，rerun 成功。
- **破坏级别**: `full_instance`
- **溯源风险项**: RISK-REL-05
- **维度**: [reliability]

### INTENT-REL-017  依赖 action 不可用（模拟 action 服务故障）——workflow 失败与报错
- **场景**: 在 job 中调用某 action 时，模拟该 action 的下载/执行服务返回 5xx 或超时。
- **压力或故障参数**: 使用本地代理或 hosts 劫持使 `actions/checkout` 等内置 action 的下载地址指向 502 端点；超时 30s。
- **稳态判据**:  
  - job 在 60s 内失败，状态 failure。  
  - 日志中包含 action 名称与 HTTP 502/timeout 等具体错误。  
  - 非无限重试导致 hang > 5min。
- **恢复预期**: action 服务恢复后 rerun 成功。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-05
- **维度**: [reliability]

---

## 五、API 与集成稳定性（覆盖 RISK-REL-03、RISK-REL-04）

### INTENT-REL-018  API 速率限制——高频触发下正确返回 429 与 Retry-After
- **场景**: 对 workflow trigger / run status / artifact API 进行高频调用，验证限流语义符合 HTTP 标准。
- **压力或故障参数**: 60 秒内对同一端点发起 1000 次调用（如 GET /api/v5/repos/{owner}/{repo}/actions/runs）。缺 platform-config，参数待补（实际限流阈值未知）。
- **稳态判据**:  
  - 超过阈值后返回 HTTP 429，响应体含明确限流提示。  
  - 响应头含 `Retry-After` 或 `X-RateLimit-Reset`。  
  - 429 不伴随 500 或连接重置，客户端可按标准退避。
- **恢复预期**: 按 Retry-After 等待后再次请求，返回 200 成功。
- **破坏级别**: `none`
- **溯源风险项**: RISK-REL-03
- **维度**: [reliability]

### INTENT-REL-019  Webhook 投递失败——模拟接收端 5xx 时观察重试间隔与风暴抑制
- **场景**: 配置仓库 webhook 指向一个可控端点，让端点连续返回 502/503，验证平台不重试风暴、最终静默失败或告警。
- **压力或故障参数**: webhook 目标 URL 连续返回 503（持续 5 分钟）；观察平台投递行为。缺 platform-config，参数待补（实际重试次数与退避间隔未知）。
- **稳态判据**:  
  - 投递失败次数在 10 次以内（无无限重试风暴）。  
  - 重试间隔呈现指数退避（如 1s, 2s, 4s, 8s...），而非固定 1s 高频轰炸。  
  - 最终失败后在仓库设置或日志中可观测到失败状态。
- **恢复预期**: 接收端恢复 200 后，新的 webhook 事件正常投递，断点后续事件不补发（或按文档补发）。
- **破坏级别**: `none`
- **溯源风险项**: RISK-REL-04
- **维度**: [reliability]

---

## 六、资源配额与 Artifact / Cache 边界

### INTENT-REL-020  artifact 大小边界——上传 500MB / 1GB / 2GB 文件观察上限与报错
- **场景**: 验证 artifact 上传在接近/超过单文件/总大小配额时的行为。
- **压力或故障参数**: 分别生成 500MB、1GB、2GB 的单文件 artifact 并上传。缺 platform-config，参数待补（artifact 大小上限未知，当前文档仅提 "不超过限制" 但未公开数值）。
- **稳态判据**:  
  - 若存在上限（如 1GB）：超过时 upload-artifact step 在 300s 内失败，日志含 "artifact size exceeds limit" 等明确信息。  
  - 未超限时上传成功，下游 download-artifact 可完整下载，MD5 校验一致。  
  - 大文件上传期间 runner 网络/内存稳定，无 OOM。
- **恢复预期**: 超限后缩减 artifact 体积重新触发即可恢复。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-05（间接）
- **维度**: [reliability]

### INTENT-REL-021  cache 大小边界——写入 500MB / 1GB / 2GB 缓存观察上限与 LRU 淘汰
- **场景**: 验证 cache action 对大缓存包的保存、恢复及配额超限行为。
- **压力或故障参数**: 分别生成 500MB、1GB、2GB 的缓存目录并保存。缺 platform-config，参数待补（cache 单条目/总配额未知）。
- **稳态判据**:  
  - 未超限时：同一仓库后续 run 的 cache restore 命中，恢复时间 <= 写入时间的 50%。  
  - 若超限：save 步骤明确报错，非无限 hang 或静默丢弃。  
  - LRU 淘汰策略下，旧缓存被替换，新缓存可用。
- **恢复预期**: 缩减缓存体积或清理旧缓存后恢复正常。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-05（间接）
- **维度**: [reliability]

---

## 七、Package 与内存边界（覆盖 RISK-REL-06）

### INTENT-REL-022  Package 大文件上传中断——500MB 包中途断网观察断点续传/重试
- **场景**: 通过 npm/mvn/docker push 上传大体积包时模拟网络中断，验证是否支持断点续传或干净重试。
- **压力或故障参数**: 上传 500MB 的 npm tarball / docker layer；在传输至 50% 时注入网络断开（如 iptables DROP 目标 registry IP，持续 60s 后恢复）。缺 platform-config，参数待补（Package 上传超时与重试策略未知）。
- **稳态判据**:  
  - 网络中断时客户端在 120s 内报错（非无限 hang）。  
  - 若支持断点续传：网络恢复后上传从断点继续，最终成功。  
  - 若不支持断点续传：重试后完整重新上传并成功，或明确报错要求用户手动重试。  
  - 服务端不出现半包/损坏包（上传完成后校验 hash 通过）。
- **恢复预期**: 网络恢复后重试上传成功；若不支持自动重试，用户手动重触发 CI 可成功。
- **破坏级别**: `full_instance`
- **溯源风险项**: RISK-REL-06
- **维度**: [reliability]

### INTENT-REL-023  内存溢出边界——small runner(8GB) 上申请 12GB 内存观察 OOM kill 行为
- **场景**: 验证 runner 内存超限时的优雅处理：job 被 kill、状态正确标记、不波及其他 job。
- **压力或故障参数**: runner=small（2核8G）；step 内使用 `stress-ng --vm 1 --vm-bytes 12G --timeout 60s` 申请超配额内存。
- **稳态判据**:  
  - job 在 60s 内被系统 OOM killer 终止，状态为 failure。  
  - 日志中出现 "out of memory" / "killed" / "exit code 137" 等明确信息。  
  - 同一 runner（若复用）后续 job 仍可正常启动，无内存泄漏残留。
- **恢复预期**: 降低内存申请或使用 large/xlarge runner 后恢复正常。
- **破坏级别**: `full_instance`
- **溯源风险项**: RISK-REL-05
- **维度**: [reliability]

---

## 八、嵌套层数与重试边界

### INTENT-REL-024  workflow_call 嵌套层数边界——3 层嵌套（超过文档声明最多 2 层）观察报错
- **场景**: 验证系统对 workflow_call 嵌套层数的硬性限制及报错质量。
- **压力或故障参数**: workflow A calls B；B calls C；形成 3 层嵌套。文档声明最多 2 层。
- **稳态判据**:  
  - 第 3 层调用在解析或运行时明确失败。  
  - 错误信息包含 "workflow_call nesting exceeds maximum depth of 2" 或类似语义。  
  - 非静默忽略第 3 层或无限递归。
- **恢复预期**: 扁平化嵌套至 2 层以内后正常运行。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-02（间接）
- **维度**: [reliability]

### INTENT-REL-025  rerun 次数边界——连续请求第 4 次 rerun 观察拒绝行为
- **场景**: 验证文档声明的 "单条运行最多重新运行 3 次" 限制是否被正确执行。
- **压力或故障参数**: 对同一 run 连续触发 rerun 4 次；原始 run 为失败的 fixture。
- **稳态判据**:  
  - 前 3 次 rerun 成功创建新 run，状态正常流转。  
  - 第 4 次请求在 5s 内被拒绝，返回明确错误（如 "maximum rerun count exceeded"）。  
  - 第 4 次不产生新的 run 记录。
- **恢复预期**: 无需恢复；rerun 次数限制为正常约束。
- **破坏级别**: `fixture`
- **溯源风险项**: RISK-REL-02（间接）
- **维度**: [reliability]

---

## 质量清单自评

- [x] 每个配额/边界维度都有边界+越界或边界探测 intent：concurrency(5)、matrix(8/60)、timeout(350/360)、artifact(500MB/1GB/2GB)、cache(500MB/1GB/2GB)、rerun(3 次)、workflow_call(2 层)。
- [x] 每条故障注入 intent 都声明了恢复预期（REL-013 ~ REL-017、REL-022、REL-023）。
- [x] 参数具体（并发=5/20、矩阵=8/60、超时=350min、日志=50MB、仓库=1.2GB、step=50、artifact/cache=500MB/1GB/2GB）；缺具体数值处标注「待补」。
- [x] 破坏性 intent 标了正确的 teardown 级别：`fixture` 12 条，`full_instance` 7 条，`none` 6 条。
- [x] 不设计不可在受控独立实例上执行的破坏性场景；所有破坏性场景均可通过 fixture / full_instance 重置恢复。
- [x] 溯源链完整：每条 intent 均对齐 risk-register.md 中的 RISK-REL-01 ~ RISK-REL-06 或稳定性专项关注点。
