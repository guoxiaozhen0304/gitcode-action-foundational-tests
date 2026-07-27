# Reliability Intents（稳定性意图库）· Run 2026-07-27-01

> 产出者：reliability agent（混沌与边界工程师）
> Run ID：2026-07-27-01
> 输入版本：platform-config/README.md（2026-07-21 修订）、instance-config.md（2026-07-20 快照）、reliability-scenario/README.md（PERF-001~008 / RELI-001~010）、history/issues-encountered.md（2026-07-20 导出）、gitcode-api/api-reference.md
> 基底关系：本 run **沿用** 2026-07-23-01 的 INTENT-REL-001~068 全量作为基底（含 2026-07-27 回填的 REL-067/068），不重复定义；本文件仅产出**增量 delta intent：REL-069 ~ REL-085**。
> 优先级说明：risk-register 中稳定性仅 RISK-REL-01（P1，非 blocker）。本轮 REL-069 依据历史实证 bug #101（★标注）建议升 P0，并建议 risk-register 增补对应 blocker 风险项；其余 P1/P2 均挂靠 RISK-REL-01 或历史实证。

---

## 1. 与上轮（2026-07-23-01）的关系

| 关系 | 范围 | 说明 |
|---|---|---|
| 沿用 | INTENT-REL-001 ~ 068 | 配额边界/越界、执行模型、故障注入、洪泛、大规模、PERF/RELI 场景回归，已全部覆盖，不重复产出 |
| 新增 | INTENT-REL-069 ~ 085 | 历史遗留 bug 回归（#101/#10/#55/#17/#67/#48）+ 未公开配额探测 + 新增混沌注入点 + post 阶段语义 |
| 合并 | — | 无（上轮无重叠定义需合并） |

## 2. 增量缺口分析（为什么有这批新 intent）

1. **历史 ★ 级 bug 未覆盖**：#101（matrix needs 依赖初始化失败）在上一轮 REL-025 只覆盖了「上游失败传播」，未覆盖「job needs matrix job 成功路径」的实证 bug。
2. **历史调度/状态类 bug 未覆盖**：#10（指定 record 取消失效）、#55（成功后状态停留 RUNNING）、#17（新仓库 workflow 不注册）、#67（触发无去抖）、#48（K8s runner 被调度到 arm 节点）。
3. **platform-config 明确列出「文档未公开上限」**：`max_matrix_size`、`max_log_size`、`max_artifact_size`、`max_cache_size` 上轮未做探测型 intent（REL-038/039 仅到 50 组合，REL-040 仅 100MB，REL-041 仅 100MB artifact）。
4. **混沌注入点补全**：runner↔平台心跳分区恢复、artifact 上传中断残留清理、排队期 runner 下线重调度。
5. **GitCode 特有机制**：`post` 后处理阶段（run_always: true）的失败语义未定义 intent。

---

## 3. 新增 Intent 列表

### 3.1 历史实证 bug 回归

```
意图 ID:    INTENT-REL-069
维度标签:   [reliability, completeness]
标题:       needs 依赖 matrix job 成功路径——jobB(matrix) 全部成功后 jobA 应正常初始化执行

风险点:     历史 #101（★标注）：「jobA needs 一个 matrix jobB，jobB 成功了 jobA 依然会初始化失败」。
            needs 与 matrix 展开结果的聚合判定若错误，所有「构建矩阵 → 汇总发布」型主流水线
            会在最后一步无声失败，且用户难以归因（jobB 明明显示成功）。
预期系统行为: jobB 为 matrix（如 3 实例），全部实例 success 后，needs: [jobB] 的 jobA 应正常
            初始化并执行；needs 上下文中的 jobB.outputs/result 聚合值可被 jobA 正确求值。
Oracle 来源: 历史实证（issues-encountered.md #101）；GitHub 行为（needs 引用 matrix job 时按聚合结果判定）

验证要点:
  - [正向] matrix jobB 全部实例 success → jobA 进入 in_progress 并 completed(success)
  - [正向] jobA 内可读取 needs.jobB.result == "success" 与 matrix 聚合 outputs
  - [负向] jobA 不应在 jobB 全成功时初始化失败 / 状态=skipped（无 if 条件时）
  - [负向] jobB 部分实例失败（fail-fast=false）时，jobA（无 if）应 skipped 而非执行

故障/压力参数: matrix 实例数=3，fail-fast=false；两组实验——(a) 3 实例全成功；(b) 1 实例失败。
稳态判据:     (a) jobA 状态=success；(b) jobA 状态=skipped
恢复预期:     N/A（设计行为验证；若复现 #101 记为 blocker）
破坏级别:     none
优先级线索:   RISK-REL-01；历史 #101 ★ 实证 bug，建议 P0（建议 risk-register 增补 matrix-needs blocker 项）
来源输入:     history/issues-encountered.md #101；testing-focus.md §3 执行模型
```

```
意图 ID:    INTENT-REL-070
维度标签:   [reliability]
标题:       多并发 run 中取消指定 run——取消目标正确性（不得总是取消最新一条）

风险点:     历史 #10：「同时触发多个 records，停止指定 record 时不管用，总是以出栈方式停止
            最上面的」。取消操作若按栈序而非 run 标识寻址，用户会误杀仍在运行的关键流水线，
            而想停的那条继续消耗资源。
预期系统行为: 同一 workflow 并发 3 条 run（RUN-1/2/3，均 sleep 300），通过 API/UI 取消中间的
            RUN-2 后：RUN-2 状态→cancelled，RUN-1/RUN-3 不受干扰继续运行至完成。
Oracle 来源: 历史实证（issues-encountered.md #10）；GitHub 行为（cancel 按 run_id 寻址）

验证要点:
  - [正向] RUN-2 状态=cancelled，RUN-1/RUN-3 状态=success
  - [负向] RUN-1/RUN-3 不应被取消或中断；取消 API 不应作用于「最新一条」而非指定 run_id
  - [非功能] 取消请求到 RUN-2 终态稳定 ≤60 秒

故障/压力参数: 并发 run 数=3，每 run 单 job sleep 300 秒；触发后 30 秒取消第 2 条（按 run_id 指定）。
稳态判据:     RUN-2 cancelled、RUN-1/RUN-3 success，无串扰
恢复预期:     优雅降级（被指定取消的 run 终止，其余 run 不受影响）
破坏级别:     fixture
优先级线索:   RISK-REL-01；历史 #10 实证，建议 P1
来源输入:     history/issues-encountered.md #10；gitcode-api/api-reference.md（run 取消端点）
```

```
意图 ID:    INTENT-REL-071
维度标签:   [reliability]
标题:       运行状态收敛——job 全部完成后 run 状态应在有界时间内脱离 RUNNING

风险点:     历史 #55：「全量代码检查任务已经跑成功，状态一直显示运行中」；#19：「job 执行后
            概率性展示异常信息，刷新后恢复」。run 级状态与 job 级状态聚合若存在延迟或丢失，
            依赖状态轮询的外挂系统（merge gate、机器人）会永久阻塞。
预期系统行为: 所有 job 进入终态后，run 级 status 在 ≤120 秒内收敛为 completed 且 conclusion
            与 job 聚合结果一致；连续轮询不出现 RUNNING↔COMPLETED 抖动。
Oracle 来源: 历史实证（issues-encountered.md #55/#19）；GitHub 行为（run 状态为 job 聚合）

验证要点:
  - [正向] 全部 job 终态后 ≤120 秒，run.status=completed
  - [正向] run.conclusion 与 job 结果聚合一致（任一 job failure → run failure）
  - [负向] 不应出现 job 全 success 而 run 长期（>10 分钟）停留 in_progress
  - [非功能] 每 10 秒轮询共 10 分钟，status 序列单调（QUEUED→RUNNING→COMPLETED 无倒退）

故障/压力参数: 单 workflow 含 3 个并行 job（各 sleep 60 秒）；触发后每 10 秒轮询 run/job 状态至收敛。
稳态判据:     收敛时延 ≤120 秒，状态序列单调无抖动，conclusion 聚合正确
恢复预期:     N/A（状态一致性验证；若复现 #55 记为调度状态缺陷）
破坏级别:     none
优先级线索:   RISK-REL-01；历史 #55/#19 实证，建议 P1
来源输入:     history/issues-encountered.md #55/#19；gitcode-api/api-reference.md
```

```
意图 ID:    INTENT-REL-072
维度标签:   [reliability, completeness]
标题:       新仓库 workflow 注册延迟——同步代码后首次 push 应识别流水线配置

风险点:     历史 #17：「新建代码仓同步代码后，Actions 不识别流水线配置；需手动修改一次 yml
            后才能识别到」，结论注明「存在文件处理上限」。首次注册失败会让新接入用户误以为
            平台不支持其配置，且无任何报错提示。
预期系统行为: 新建仓库（或导入仓库）首次提交 `.gitcode/workflows/*.yml` 后，push 事件应在
            ≤5 分钟内触发对应 workflow；不应需要「手动再改一次 yml」作为注册开关。
Oracle 来源: 历史实证（issues-encountered.md #17）；GitHub 行为（workflow 文件随 push 即时生效）

验证要点:
  - [正向] 新仓库首次 push 含合法 workflow 文件 → run 被创建
  - [负向] 不应出现「workflow 文件存在但 push 无任何 run 记录」的静默丢失
  - [非功能] 从 push 到 run 创建的注册延迟 ≤5 分钟；连续 3 个新仓库全部成功

故障/压力参数: 新建空仓库 3 个，各推入 1 条极简 workflow（push 触发）；记录 push→run 创建时延。
稳态判据:     3/3 仓库首次 push 即触发，注册延迟 ≤5 分钟
恢复预期:     自动恢复（平台注册流程完成后正常触发；若需人工干预记为缺陷）
破坏级别:     fixture（新建/销毁测试仓库）
优先级线索:   RISK-REL-01；历史 #17 实证，建议 P1
来源输入:     history/issues-encountered.md #17
```

```
意图 ID:    INTENT-REL-073
维度标签:   [reliability]
标题:       触发幂等与去抖——同一 ref 短时间重复 push 的触发语义应可预期

风险点:     历史 #67：「流水线频繁触发，每次改动标签都会触发流水线」（已修复）。触发链路
            若无去抖/幂等语义，monorepo 高频提交或批量 tag 操作会产生运行风暴，耗尽
            concurrency 配额并拖垮队列。
预期系统行为: 同一分支 10 秒内连续 5 次 push（不同 commit），平台按声明语义处理——要么
            每次 push 都触发（5 条 run 全部可追踪），要么有明确去抖窗口且文档化；绝不应
            出现「触发记录与 push 次数对不上且无法解释」。tag 批量创建（10 个 tag）同理。
Oracle 来源: 历史实证（issues-encountered.md #67）；GitHub 行为（每次 push 均触发，无去抖）

验证要点:
  - [正向] 每次 push 均能在 run 列表中找到对应 sha 的 run 记录（一一对应可审计）
  - [负向] 不应出现 run 数 < push 数且无文档化去抖说明；不应同一 sha 触发 2 次
  - [非功能] 10 个 tag 10 秒内推送，run 创建与 tag 事件对账 100% 可解释

故障/压力参数: (a) 同分支 10 秒内 5 次 push；(b) 10 秒内推 10 个 tag；均配置 push/tag 触发。
稳态判据:     run 记录与事件对账一致（5/5、10/10 或文档化去抖后的确定数量）
恢复预期:     N/A（触发语义验证）
破坏级别:     fixture
优先级线索:   RISK-REL-01；历史 #67 实证，建议 P1
来源输入:     history/issues-encountered.md #67；testing-focus.md §2 触发器语义（幂等与去抖）
```

```
意图 ID:    INTENT-REL-074
维度标签:   [reliability]
标题:       架构标签调度正确性——x64 请求不得落到 arm64 节点（反之亦然）

风险点:     历史 #48：「kubernetes-Runner 会被调度到 arm 节点上」；#96：「2xlarge arm 任务
            申请资源错误」。异构调度错误会让 x86 编译产物在 arm 上静默执行错误或崩溃，
            且错误归因极难（表现为 flaky 编译失败）。
预期系统行为: runs-on 声明 `[ubuntu-latest, x64, small]` 的 job 只调度到 x64 runner；
            `[dedicate-hosted, arm64, large]` 只调度到 arm64 runner；job 内 `uname -m`
            与声明架构 100% 一致。无匹配架构 runner 时应明确排队/报错，而非错配。
Oracle 来源: 历史实证（issues-encountered.md #48/#96）；GitCode 规格（runs-on 三段式 {os,arch,flavor}）

验证要点:
  - [正向] x64 job 的 `uname -m` 输出=x86_64；arm64 job 输出=aarch64
  - [负向] 任一档位 10 次采样中架构错配次数=0
  - [非功能] 无对应架构空闲 runner 时，job 状态=queued 或明确报错，不错配执行

故障/压力参数: x64/small 与 arm64/large 两种 runs-on 各触发 10 次探针 job（打印 uname -m）。
稳态判据:     20 次采样架构匹配率=100%；无资源时不错配
恢复预期:     明确报错（无匹配架构 runner 时排队或报资源不可用）
破坏级别:     none
优先级线索:   RISK-REL-01；历史 #48/#96 实证，建议 P1
来源输入:     history/issues-encountered.md #48/#96；platform-config/instance-config.md（runner 池配置）
```

### 3.2 未公开配额探测（platform-config 标注「文档未公开上限」）

```
意图 ID:    INTENT-REL-075
维度标签:   [reliability]
标题:       自定义 timeout 超默认值——timeout-minutes=720 的接受/拒绝语义探测

风险点:     上轮 REL-007~010 覆盖默认 360 分钟与短超时，但未探测「显式声明超过 360」的行为。
            若平台静默截断为 360，用户为长任务（全量回归、大型训练）设置的 720 会在 360 分钟
            被误杀，且无任何提示。
预期系统行为: timeout-minutes=720 要么被接受并按 720 执行，要么在解析/保存阶段明确报错并
            指出上限值；不允许「保存成功但按 360 截断」的静默行为。
Oracle 来源: 未知·待实测（GitCode 未公开 timeout-minutes 最大值；GitHub 默认 360 且可自定义更大值）

验证要点:
  - [正向] 配置 720 后，平台行为二选一并可判定：接受（job 可运行超过 360 分钟）或拒绝（明确报错）
  - [负向] 不应保存成功却按 360 静默截断
  - [非功能] 若接受，job 运行 370 分钟不被终止（用分段 sleep 验证，成本可控时缩比验证）

故障/压力参数: timeout-minutes=720；job 运行时长探针=370 分钟（或按 harness 成本约束缩比）。
稳态判据:     行为确定可归因（接受→超 360 仍运行；拒绝→明确错误信息含上限值）
恢复预期:     明确报错（若拒绝，用户调整配置后重试成功）
破坏级别:     none
优先级线索:   RISK-REL-01；未公开配额探测，建议 P2
来源输入:     platform-config/README.md（default_job_timeout_minutes=360，最大值未声明）
```

```
意图 ID:    INTENT-REL-076
维度标签:   [reliability]
标题:       matrix 组合数上限探测——256 组合（GitHub 上限）边界与 300 组合越界行为

风险点:     platform-config 标注 max_matrix_size 未公开；GitHub 上限为 256 jobs/workflow。
            上轮 REL-038/039 仅验证 20/50 组合。若 GitCode 上限低于 256 且超限静默截断，
            大矩阵项目（多 OS×多版本）会静默少跑组合，形成危险的「测试覆盖假象」。
预期系统行为: 256 组合应全部展开或被平台明确拒绝；300 组合若超上限应明确报错（含上限值），
            不得静默截断为前 N 个继续执行。
Oracle 来源: GitHub 行为（256 jobs/workflow 上限）作默认 oracle；GitCode 差异待实测确认

验证要点:
  - [正向] 256 组合：全部展开（job 数=256）或明确报错
  - [正向] 300 组合：若拒绝，错误信息含实际上限数值
  - [负向] 不应「声明 300 实际只跑 256 且不报错」
  - [非功能] 256 组合展开/入队时延 ≤600 秒

故障/压力参数: matrix 组合数=256（如 os×8 × ver×32）与 300（os×10 × ver×30）；max-parallel=5 控速。
稳态判据:     job 数与声明组合数一致，或收到含上限值的明确错误；无静默截断
恢复预期:     明确报错（超限时用户拆分 matrix 后重试成功）
破坏级别:     none
优先级线索:   RISK-REL-01；未公开配额探测，建议 P2（若发现静默截断升 P1）
来源输入:     platform-config/README.md（max_matrix_size 未声明）；parity-matrix（strategy.matrix 组合数上限 ❓）
```

```
意图 ID:    INTENT-REL-077
维度标签:   [reliability]
标题:       单 job 日志大小上限探测——500MB/1GB 日志的截断语义

风险点:     platform-config 标注 max_log_size 未公开；上轮 REL-040/051 仅覆盖到 100MB/200MB。
            若日志达上限后被静默截断，用户在日志尾部找不到真实报错（最痛的调试场景），
            且无任何「已截断」提示。
预期系统行为: 500MB/1GB 日志输出时，平台要么完整保留可下载，要么在有界大小处截断并给出
            明确「truncated」标识；不得静默丢失尾部且无提示。
Oracle 来源: 未知·待实测（GitCode 未公开日志上限）；GitHub 行为（超大日志截断且有提示）

验证要点:
  - [正向] 日志可下载，且能判定为「完整」或「带明确截断标识」
  - [负向] 不应无截断提示却缺尾部行
  - [非功能] 记录实际上限值（首次截断点），回写 parity-matrix/platform-config

故障/压力参数: job 输出 500MB 与 1GB 带序号日志（seq 生成，行号可校验完整性）。
稳态判据:     下载文件行号连续性可判定：完整 → 行号连续到末行；截断 → 存在平台级截断提示
恢复预期:     明确报错/降级（截断时用户可见「日志已截断」提示）
破坏级别:     fixture
优先级线索:   RISK-REL-01；未公开配额探测，建议 P2（若发现静默截断升 P1）
来源输入:     platform-config/README.md（max_log_size 未声明）；history #6/#14（日志痛点）
```

```
意图 ID:    INTENT-REL-078
维度标签:   [reliability]
标题:       artifact 大小上限探测——2GB/5GB 上传的接受/拒绝语义

风险点:     platform-config 标注 max_artifact_size 未公开（仅「不超过限制」）；上轮 REL-041/053
            仅到 1GB。超限若静默失败或上传成功但下载损坏，会摧毁跨 job 产物传递的信任。
预期系统行为: 2GB/5GB artifact 上传，平台要么完整成功（下载 MD5 一致），要么在上传阶段
            明确拒绝并给出上限值；不得「上传报成功、下载损坏/404」。
Oracle 来源: 未知·待实测（GitCode 未公开 artifact 上限）；GitHub 行为作参照

验证要点:
  - [正向] 上传结果与下载完整性一致：成功↔MD5 匹配；失败↔上传阶段明确报错
  - [负向] 不应上传成功但 artifact 列表查不到 / 下载 404 / MD5 不匹配
  - [非功能] 记录实际上限值，回写 platform-config

故障/压力参数: dd 生成 2GB 与 5GB 文件，large runner（200GB 磁盘）上传，下游 job 下载校验 MD5。
稳态判据:     上传-下载完整性对账 100% 一致；或收到含上限值的明确错误
恢复预期:     明确报错（超限时用户改对象存储/分包后重试成功）
破坏级别:     fixture
优先级线索:   RISK-REL-01；未公开配额探测，建议 P2
来源输入:     platform-config/README.md（max_artifact_size 未声明）
```

```
意图 ID:    INTENT-REL-079
维度标签:   [reliability]
标题:       cache 容量上限与同 key 并发写一致性探测

风险点:     platform-config 标注 max_cache_size 未公开；上轮 REL-046 仅验证 LRU 淘汰策略，
            未探测单 cache 体积上限与同 key 并发写语义。并发写同 key 若产生损坏缓存，
            后续所有命中该 key 的构建会批量失败且难以归因。
预期系统行为: (a) 单 cache 体积逐步增至上限时，平台明确接受或拒绝（含上限值）；
            (b) 3 个并行 job 同时写同一 cache key，最终 cache 内容确定（某一方完整胜出
            或明确冲突报错），不得为混合/损坏内容。
Oracle 来源: 未知·待实测（GitCode 未公开 cache 上限与并发写语义）

验证要点:
  - [正向] cache 写后读回内容完整（MD5 一致）
  - [负向] 并发写后读回内容不应为多个写入方的混合态/截断态
  - [非功能] 记录单 cache 实际上限值，回写 platform-config

故障/压力参数: (a) 单 cache 体积档=500MB/1GB/2GB；(b) 3 个并行 job 各写不同内容到同一 key。
稳态判据:     读回内容完整可归属（单一写入方或明确冲突错误）；无损坏静默成功
恢复预期:     明确报错（超限/冲突时给出可理解错误）
破坏级别:     fixture
优先级线索:   RISK-REL-01；未公开配额探测+竞态，建议 P2
来源输入:     platform-config/README.md（max_cache_size 未声明）；testing-focus.md §8
```

### 3.3 新增混沌注入点

```
意图 ID:    INTENT-REL-080
维度标签:   [reliability]
标题:       故障注入——runner 与平台心跳分区 60 秒后恢复，job 应续跑完成而非误判失败

风险点:     上轮 REL-031 覆盖 runner 被 SIGKILL（永久失联），未覆盖「临时分区后恢复」场景。
            真实网络抖动中 runner 与平台心跳中断数十秒是常态：若平台在 30 秒无心跳即判
            job 失败，会造成大面积 flaky；若永久不判，失联 job 会挂死占用配额。
预期系统行为: job 运行中 runner↔平台网络分区 60 秒后恢复，job 应继续执行并成功完成；
            期间平台状态可为 in_progress/unknown，但不得在分区窗口内判 failure；
            分区超过平台宣告的超时阈值（若有）后才允许判失败，且失败归因明确。
Oracle 来源: GitHub 行为（runner 心跳超时才判 lost，窗口期内不误杀）；待实测确认 GitCode 阈值

验证要点:
  - [正向] 分区 60 秒恢复后 job 状态=success，日志含分区前后的连续输出
  - [负向] 分区 ≤60 秒窗口内 job 不应被判 failure/cancelled
  - [非功能] 记录平台实际心跳判死阈值（首次误判时间点），回写 platform-config

故障/压力参数: 注入时机=step 执行中（第 2/4 step）；故障类型=runner 出站网络分区（仅断平台方向）；
            持续时间=60 秒；另设对照组分区=300 秒探测判死阈值。
稳态判据:     60 秒组：job success；300 秒组：行为确定可归因（续跑成功 or 明确失联失败）
恢复预期:     自动恢复（网络恢复后 job 续跑完成；超阈值失败时 rerun 成功）
破坏级别:     fixture
优先级线索:   RISK-REL-01；混沌注入补全，建议 P1
来源输入:     testing-focus.md §12 稳定性专项；platform-config/instance-config.md
```

```
意图 ID:    INTENT-REL-081
维度标签:   [reliability]
标题:       故障注入——artifact 上传中途 runner 被杀，半成品不得作为有效 artifact 出现

风险点:     上传中断后若 artifact 以「完整」面目留在列表中，下游 job 会下载到截断文件并
            继续使用（损坏产物进入发布链路）；若残留半成品永久占位，同名重传可能冲突。
            上轮 REL-032 覆盖网络分区失败路径，未覆盖「进程被杀」的元数据一致性路径。
预期系统行为: upload-artifact 执行到 ~50% 时 runner 进程被 SIGKILL，平台应将该 artifact
            标记为失败/不完整（或自动清理），artifact 列表中不得出现「可下载但内容截断」
            的条目；rerun 后同名 artifact 可正常重传成功。
Oracle 来源: GitHub 行为（未完成上传的 artifact 不可见）；数据完整性通用要求

验证要点:
  - [正向] job 状态=failure；artifact 列表中该 artifact 不存在或明确标记 incomplete
  - [负向] 不应存在「可下载且 HTTP 200 但内容截断」的 artifact
  - [正向] rerun 后同名 artifact 上传成功、下载 MD5 一致

故障/压力参数: 注入时机=100MB artifact 上传进度 ~50%；故障类型=runner 进程 SIGKILL。
稳态判据:     无半成品 artifact 可下载；rerun 后重传成功且完整
恢复预期:     明确报错（job 标记失败），rerun 后自动恢复成功
破坏级别:     fixture
优先级线索:   RISK-REL-01；数据完整性（质量门禁：故障后数据损坏=blocker），建议 P1
来源输入:     testing-focus.md §8/§12；gitcode-spec/upload-download-artifacts.md
```

```
意图 ID:    INTENT-REL-082
维度标签:   [reliability]
标题:       故障注入——排队期目标 runner 下线，job 应重调度或有界等待后明确失败

风险点:     历史 #12/#54：资源池已释放/资源空闲但 job 持续等待。job 在 queued 期间其目标
            runner 下线时，若调度器不重调度也不超时，job 会无限挂起（用户只能取消重跑）。
预期系统行为: job 处于 queued 时唯一匹配 runner 被下线，平台应在有界时间（≤10 分钟）内：
            (a) 重调度到其他匹配 runner，或 (b) 判定无可用资源并明确报错；不得无限 queued。
            runner 重新上线后，排队 job 应能被正常接管。
Oracle 来源: 历史实证（issues-encountered.md #12/#54）；调度系统通用可用性要求

验证要点:
  - [正向] runner 下线后 ≤10 分钟，job 状态脱离 queued（转 running 或明确失败）
  - [负向] 不应 queued 挂起 >10 分钟无任何状态变化或提示
  - [正向] runner 恢复上线后，新触发 job 正常调度（池自恢复）

故障/压力参数: 注入时机=job queued 且等待中；故障类型=唯一匹配 runner 下线（停 agent 进程）；
            观察窗口=10 分钟；随后 runner 重新上线验证接管。
稳态判据:     job 在 10 分钟内脱离 queued 且归因明确；runner 恢复后调度功能复原
恢复预期:     优雅降级（重调度或明确报资源不可用；runner 恢复后自动复原）
破坏级别:     full_instance（操作实例级 runner 池，执行后须恢复 runner 注册状态）
优先级线索:   RISK-REL-01；历史 #12/#54 实证，建议 P1
来源输入:     history/issues-encountered.md #12/#54；platform-config/instance-config.md
```

### 3.4 GitCode 特有机制与语义补全

```
意图 ID:    INTENT-REL-083
维度标签:   [reliability, completeness]
标题:       post 后处理阶段失败语义——run_always=true 下 post 失败对 workflow 结论的影响

风险点:     post 是 GitCode 特有阶段（默认 run_always: true，job 结束后执行）。若 post
            失败但 workflow 显示成功，清理/上报类动作（如测试结果上传、环境回收）静默失效；
            若 post 失败把已成功的 job 拖成 failure，又会误伤正常构建。语义必须确定可预期。
预期系统行为: 主 steps 全部 success 后 post 阶段 step 失败：平台应有文档化的确定语义——
            要么 workflow conclusion=success 且 post 失败单独标注，要么 conclusion=failure
            且日志明确归因到 post 阶段；取消场景下 post 是否执行也应与文档一致。
Oracle 来源: GitCode 规格（workflow-file-location-structure.md：post 默认 run_always=true）；无 GitHub 对应物

验证要点:
  - [正向] post 失败时 conclusion 与文档声明一致，且日志明确归因 post 阶段
  - [正向] 主 step 失败时 post（run_always）仍执行
  - [负向] 不应 post 失败无任何标注而 conclusion=success（静默吞掉），除非文档明确如此
  - [负向] 不应 post 阶段 hang 导致 job 超过 timeout 仍不收敛

故障/压力参数: 三组——(a) 主 steps 成功+post 失败；(b) 主 step 失败+post 正常；(c) post 内 sleep
            超过 job timeout 残余时间。
稳态判据:     三组终态均与文档语义一致；post 失败归因在日志/状态可见；无 hang
恢复预期:     明确报错（post 失败可归因、可重跑）
破坏级别:     fixture
优先级线索:   RISK-REL-01；GitCode 特有机制语义未定，建议 P1
来源输入:     gitcode-spec/workflow-file-location-structure.md；parity-matrix（post 后处理阶段 ❌ 特有）
```

```
意图 ID:    INTENT-REL-084
维度标签:   [reliability]
标题:       日志实时性——运行中 job 的日志流式可见延迟应有界

风险点:     历史 #14/#81：日志加载慢、大概率不显示。上轮 REL-059 验证完成后日志完整性，
            未验证「运行中」的流式可见性。长任务（30 分钟编译）若前 20 分钟看不到任何日志，
            用户无法判断是 hang 还是正常执行，只能盲目取消重跑。
预期系统行为: job 运行中持续输出日志，UI/API 上首行日志可见延迟 ≤30 秒，后续行的追平
            延迟 ≤60 秒；运行中日志与完成后日志内容一致（无运行中可见、完成后缺失的行）。
Oracle 来源: 历史实证（issues-encountered.md #14/#81）；GitHub 行为（日志准实时流式）

验证要点:
  - [正向] 首行日志从产生到 UI/API 可见 ≤30 秒
  - [正向] 运行中可见日志是完成后日志的前缀（内容一致）
  - [非功能] 10 分钟运行窗口内，日志追平延迟 P95 ≤60 秒

故障/压力参数: job 每 5 秒输出一行带时间戳日志，共 10 分钟（120 行）；harness 每 10 秒拉取
            运行中日志并记录各行可见延迟。
稳态判据:     首行延迟 ≤30 秒；追平延迟 P95 ≤60 秒；运行中日志为完成后日志前缀
恢复预期:     N/A（性能基准；超限记为日志链路缺陷）
破坏级别:     none
优先级线索:   RISK-REL-01；历史 #14/#81 实证，建议 P1
来源输入:     history/issues-encountered.md #14/#81；gitcode-api/api-reference.md（日志端点）
```

```
意图 ID:    INTENT-REL-085
维度标签:   [reliability]
标题:       schedule 触发准点性与丢失率——cron 最短 5 分钟间隔下的长期触发可靠性

风险点:     parity-matrix 标注 schedule 🟡（GitCode 最短 5 分钟、UTC、仅默认分支）。定时
            任务（夜间构建、定时同步）若静默丢失触发，用户数天后才发现产物过期，且无告警。
            触发链路的准点性与丢失率需要实测基线。
预期系统行为: 配置 */5 cron 的 schedule workflow 连续运行 2 小时（理论 24 次触发），实际
            触发次数 ≥23（丢失率 ≤5%）；每次触发延迟（计划时刻→run 创建）P95 ≤5 分钟；
            非默认分支上的 schedule 不触发（符合声明）。
Oracle 来源: GitCode 规格（trigger-events.md：最短 5 分钟、UTC、仅默认分支）

验证要点:
  - [正向] 2 小时窗口内触发次数 ≥23/24，每次 run 的 sha=默认分支 HEAD
  - [负向] 非默认分支 schedule 配置不应产生任何 run
  - [非功能] 触发延迟 P95 ≤5 分钟；无重复触发（同一计划时刻 2 条 run）

故障/压力参数: cron=*/5 * * * *（UTC）；观察窗口=2 小时；对照组=非默认分支同配置。
稳态判据:     丢失率 ≤5%；延迟 P95 ≤5 分钟；重复触发=0；分支隔离符合声明
恢复预期:     N/A（触发可靠性基准）
破坏级别:     fixture
优先级线索:   RISK-REL-01；parity-matrix schedule 🟡 项实证补全，建议 P1
来源输入:     gitcode-spec/trigger-events.md；parity-matrix（schedule cron 最短间隔 🟡）
```

---

## 4. 统计摘要

| 分类 | 数量 | 明细 |
|---|---|---|
| **本轮新增 intent** | **17** | REL-069 ~ REL-085 |
| 历史实证 bug 回归 | 6 | REL-069(#101), REL-070(#10), REL-071(#55/#19), REL-072(#17), REL-073(#67), REL-074(#48/#96) |
| 未公开配额探测 | 5 | REL-075(timeout 上限), REL-076(matrix 上限), REL-077(日志上限), REL-078(artifact 上限), REL-079(cache 上限+并发写) |
| 混沌故障注入 | 3 | REL-080(心跳分区恢复), REL-081(上传中断半成品), REL-082(排队期 runner 下线) |
| 特有机制/语义补全 | 2 | REL-083(post 阶段语义), REL-085(schedule 可靠性) |
| 性能基准 | 1 | REL-084(日志实时性) |
| **破坏级别分布** | | none=7, fixture=9, full_instance=1(REL-082) |
| **P0** | **1** | REL-069（历史 #101 ★ matrix-needs bug；建议 risk-register 增补 blocker 项） |
| **P1** | **11** | REL-070, 071, 072, 073, 074, 080, 081, 082, 083, 084, 085 |
| **P2** | **5** | REL-075, 076, 077, 078, 079（探测类；发现静默截断/损坏时按条内注记升级 P1） |

> 合计 1 + 11 + 5 = 17 条，与 REL-069~085 一一对应。

### 与上轮的关系汇总
- **沿用**：INTENT-REL-001~068（2026-07-23-01），覆盖配额边界/越界、执行模型机制、5 类故障注入、洪泛/大规模、PERF-001~008 与 RELI-001~010 全部场景回归。
- **新增**：INTENT-REL-069~085，补历史 ★ bug（#101）、调度/状态/触发类实证 bug（#10/#55/#17/#67/#48/#96）、platform-config 四项未公开上限探测、3 个新混沌注入点、post 阶段与 schedule 语义。
- **合并**：无。
- **ID 冲突**：无（069 起编，与 001~068 无重叠）。

## 5. 质量清单自检

- [x] 每条故障注入 intent 均声明恢复预期与破坏级别（REL-080/081 恢复预期=自动恢复/明确报错，REL-082=优雅降级+full_instance）。
- [x] 参数具体：并发度、组合数、字节数、时间窗口、采样次数均为确定数值，无「大量/很快」。
- [x] 每条 intent 对齐 RISK-REL-01 或历史实证编号；P0 仅 REL-069 并注明需 risk-register 增补 blocker。
- [x] 探测类 intent（REL-075~079）均要求把实测值回写 platform-config/parity-matrix，闭环未公开配额。
- [x] 输入版本已在头部标注；reliability-scenario 的 PERF/RELI 场景与沿用基底的映射关系已核对（全部已由 REL-049~066 覆盖，本轮不重复）。

---

## 增补意图（2026-07-27 回填：NPU/Karmada 调度层，应用户要求补盲区）

> 来源：`inputs/existing-cases/gitcode-pipeline-test-cases.xlsx`「NPU用例」sheet（14 条），对应上轮门禁盲区 GAP-019/GAP-020 未闭环项。
> ⚠️ 输入退化声明：inputs 中无 Karmada/volcano/NPU 平台侧文档（仅该 xlsx 的测试内容+预期结果两列可作为 oracle），intent 的「预期系统行为」以 xlsx 预期结果为准，执行时需平台侧同学提供环境。
> 优先级说明：登记册无对应 blocker，按 rules §2 不自造 P0；但 xlsx 中「pod 多副本 Worker 指定 NPU」「vcjob 格式」两条实测结果为**不通过**（已知失败实证），对应 intent 标 P1 并在风险点中注明回归依据。

```
意图 ID:    INTENT-REL-086
维度标签:   [reliability]
标题:       K8s 单集群接入与 NPU 资源发现

风险点:     自托管 K8s 集群接入是 NPU 调度的前提。若接入失败或接入后 NPU 资源（型号/数量）未被发现/发现错误，后续所有 NPU 任务将无法调度或调度到错误节点，且失败若无声则极难排查。
预期系统行为: 单集群接入应成功；接入后平台应正确发现该集群的 NPU 资源（型号与可分配数量），资源视图与实际物理拓扑一致。
Oracle 来源: existing-cases xlsx「NPU用例」sheet 第 1 条（实测：通过）

验证要点:
  - [正向] 单集群接入成功
  - [正向] NPU 资源（型号/数量）被正确发现且与物理实际一致
  - [负向] 不应出现接入成功但资源发现为空/错误的假阳性

故障/压力参数: 接入 1 个含 NPU 节点的 K8s 集群，核对平台资源视图与 `kubectl describe node` 实际值。
恢复预期: 不适用（接入验证，无故障注入）。
破坏级别: fixture
来源输入:   inputs/existing-cases/gitcode-pipeline-test-cases.xlsx「NPU用例」sheet
优先级线索: P1
```

```
意图 ID:    INTENT-REL-087
维度标签:   [reliability]
标题:       Karmada 多集群接入、聚合资源发现与按型号/数量分发调度

风险点:     Karmada 多集群是 NPU 资源池化的核心路径：聚合资源发现错误会导致「有卡却调度不出」；按卡型号和数量的自动分发错误会导致训练任务落到无对应型号的集群；成员集群资源不足时若控制面无明确 Pending/Failed 状态，任务会静默悬挂。
预期系统行为: Karmada 多集群接入成功且聚合资源发现正确；指定成员集群提交 pod 正常运行；自动分发能按卡型号和数量选择正确的成员集群；成员集群资源不足时任务在 Karmada 控制面处于明确的 Pending 或 Failed 状态。
Oracle 来源: existing-cases xlsx「NPU用例」sheet 第 2/6/7/10 条（实测：未执行）

验证要点:
  - [正向] 多集群接入成功，聚合资源视图 = 各成员集群之和
  - [正向] 指定成员集群的 pod 正常运行
  - [正向] 自动分发按卡型号+数量落到正确成员集群
  - [负向] 资源不足时不应静默悬挂（控制面必须有 Pending/Failed 终态或明确中间态）

故障/压力参数: ≥2 个成员集群（含不同 NPU 型号），分别提交指定集群/自动分发/超额请求三类任务。
恢复预期: 不适用。
破坏级别: fixture
来源输入:   inputs/existing-cases/gitcode-pipeline-test-cases.xlsx「NPU用例」sheet
优先级线索: P1
```

```
意图 ID:    INTENT-REL-088
维度标签:   [reliability]
标题:       pod NPU 资源请求调度正确性（单卡/多卡/多副本）与非法请求 Pending 语义

风险点:     NPU 调度的基本正确性：指定型号单卡/多卡必须分配到正确节点；非法请求（不存在的型号、超过单节点物理上限的数量）必须 Pending 而非错误分配或静默丢失。⚠️ 已知失败实证：xlsx 中「pod 多副本任务（Worker）指定 NPU」实测**不通过**——多副本场景存在调度缺陷，属回归必测项。
预期系统行为: pod 指定单张/多张特定型号 NPU 能正常运行；多副本（Worker）任务指定 NPU 能正常运行（当前已知不通过，修复后回归）；请求不存在的 NPU 型号时 pod 处于 Pending；请求数量超过单节点物理上限时 pod 处于 Pending。
Oracle 来源: existing-cases xlsx「NPU用例」sheet 第 3/4/5/8/9 条（单卡/多卡/非法请求：通过；多副本 Worker：**不通过**）

验证要点:
  - [正向] 单张特定型号 NPU 任务正常运行
  - [正向] 多张特定型号 NPU 任务正常运行
  - [正向][回归] 多副本 Worker 指定 NPU 正常运行（已知失败，修复后必须回归）
  - [负向] 不存在的型号 → Pending，不应错误调度到替代型号
  - [负向] 超单节点上限的数量 → Pending，不应拆分跨节点静默分配

故障/压力参数: 分别提交 1 卡/2 卡/多副本 Worker/不存在型号/超上限数量五类 pod，观察调度结局与节点分配。
恢复预期: 不适用。
破坏级别: fixture
来源输入:   inputs/existing-cases/gitcode-pipeline-test-cases.xlsx「NPU用例」sheet
优先级线索: P1（含已知失败实证，建议回归优先）
```

```
意图 ID:    INTENT-REL-089
维度标签:   [reliability]
标题:       vcjob 格式兼容与大规模并发提交

风险点:     vcjob（volcano job）是 NPU 训练任务的主流提交格式。⚠️ 已知失败实证：xlsx 中「vcjob 格式」实测**不通过**——格式兼容存在缺陷；大规模并发提交若出现丢失/级联失败，批量训练场景不可用。
预期系统行为: vcjob 格式任务能正常解析运行（当前已知不通过，修复后回归）；大规模 vcjob 并发提交全部正常运行，无丢失、无级联失败。
Oracle 来源: existing-cases xlsx「NPU用例」sheet 第 11/14 条（vcjob 格式：**不通过**；大规模并发：通过）

验证要点:
  - [正向][回归] 标准 vcjob 格式任务正常解析并运行（已知失败，修复后必须回归）
  - [正向] 大规模 vcjob 并发提交全部进入终态，无静默丢失
  - [负向] 不应出现并发下部分 vcjob 无对应任务记录

故障/压力参数: 批量并发提交 vcjob（规模对齐 xlsx 原用例，建议 ≥50 并发），对账提交数与终态数。
恢复预期: 不适用。
破坏级别: fixture
来源输入:   inputs/existing-cases/gitcode-pipeline-test-cases.xlsx「NPU用例」sheet
优先级线索: P1（含已知失败实证，建议回归优先）
```

```
意图 ID:    INTENT-REL-090
维度标签:   [reliability]
标题:       同一集群重复接入的幂等性

风险点:     运维场景中重复接入同一集群（配置变更重提、自动化重试）若产生重复注册、资源重复计数或状态错乱，会污染资源视图并导致调度错误。
预期系统行为: 重复接入同一集群应幂等：不产生重复注册、资源视图不重复计数、既有任务不受影响。
Oracle 来源: existing-cases xlsx「NPU用例」sheet 第 12 条（实测：通过）

验证要点:
  - [正向] 重复接入后集群记录唯一、资源计数不翻倍
  - [负向] 不应出现重复接入导致的资源虚增或既有任务中断

故障/压力参数: 同一集群连续接入 ≥2 次，核对集群列表与资源计数。
恢复预期: 不适用。
破坏级别: fixture
来源输入:   inputs/existing-cases/gitcode-pipeline-test-cases.xlsx「NPU用例」sheet
优先级线索: P2
```

```
意图 ID:    INTENT-REL-091
维度标签:   [reliability]
标题:       集群断连恢复后的任务日志同步

风险点:     集群与平台断连期间任务仍在集群内运行，恢复连接后若日志无法同步，用户将丢失断连窗口内的全部执行证据，训练任务（长周期）尤其不可接受。
预期系统行为: 集群断连后恢复连接，断连期间的任务日志应能正常返回（完整或明确标注缺口）。
Oracle 来源: existing-cases xlsx「NPU用例」sheet 第 13 条（实测：未执行）

验证要点:
  - [正向] 断连恢复后日志可正常返回
  - [负向] 不应出现断连窗口日志静默丢失且无任何提示

故障/压力参数: 任务运行中断开集群连接 ≥ 一个日志采集周期，恢复后核对断连窗口日志完整性。
恢复预期: 恢复连接后日志同步追平，或明确标注缺失区间。
破坏级别: fixture
来源输入:   inputs/existing-cases/gitcode-pipeline-test-cases.xlsx「NPU用例」sheet
优先级线索: P1
```

*增补完毕：INTENT-REL-086 ~ INTENT-REL-091，共 6 条。待门禁确认后展开用例。*
