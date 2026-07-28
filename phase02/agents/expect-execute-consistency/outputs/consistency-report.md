# 断言-步骤一致性报告

**日期**: 2026-07-28
**数据源**: [phase01/runs/2026-07-27-01/cases/](https://github.com/opensourceways/gitcode-action-foundational-tests/tree/main/phase01/runs/2026-07-27-01/cases/)
**用例总数**: 498

---

## 1. 总览

| 维度 | 断言一致 | 部分不符 | 完全不符 |
|------|:---:|:---:|:---:|
| 完备性 | 98 | 7 | 5 |
| 兼容性 | 142 | 11 | 0 |
| 可靠性 | 61 | 44 | 0 |
| 安全性 | 58 | 12 | 1 |
| 易用性 | 58 | 1 | 0 |
| 易用性/兼容性 | 0 | 0 | 0 |
| 易用性/安全性 | 0 | 0 | 0 |
| 易用性/可靠性 | 0 | 0 | 0 |
| **合计** | **417** | **75** | **6** |

---

## 2. 完全不符 (6 例)

- [COMP-ARTIFACT-01-003](case/COMP-ARTIFACT-01-003.md): artifact 保留期设置生效
- [COMP-CACHE-01-002](case/COMP-CACHE-01-002.md): restore-keys 前缀匹配兜底生效
- [COMP-CACHE-01-003](case/COMP-CACHE-01-003.md): fork PR 不应覆盖或污染主分支 cache
- [COMP-DIR-01-002](case/COMP-DIR-01-002.md): .github/workflows/ 下的 YAML 不被识别为 workflow
- [COMP-SUMMARY-01-002](case/COMP-SUMMARY-01-002.md): summary 中不应暴露系统内部路径   - **维度**: 完备性   - **评级**: 完全不符
- [SEC-TOCTOU-01-002](case/SEC-TOCTOU-01-002.md): 评论触发不应绕过代码固定与 PR 审批

## 3. 部分不符 (75 例)

- [COMP-BOUND-01-086](case/COMP-BOUND-01-086.md): 矩阵构建 include exclude 与单值边界验证
- [COMP-CACHE-01-001](case/COMP-CACHE-01-001.md): cache hit 时恢复缓存内容正确
- [COMP-DIR-01-001](case/COMP-DIR-01-001.md): .gitcode/workflows/ 下的 YAML 被正确识别并触发
- [COMP-PR-01-003](case/COMP-PR-01-003.md): fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限
- [COMP-PRTARGET-01-001](case/COMP-PRTARGET-01-001.md): pull_request_target 默认使用 base 分支 workflow 版本   - **维度**: 完备性   - **评级**: 部分不符
- [COMP-WFLOW-01-061](case/COMP-WFLOW-01-061.md): workflow name 与 on 字段必填与类型验证   - **维度**: 完备性   - **评级**: 部分不符
- [COMP-WFLOW-01-063](case/COMP-WFLOW-01-063.md): workflow concurrency 并发控制字段验证   - **维度**: 完备性   - **评级**: 部分不符
- [COMPAT-COMM-01-002](case/COMPAT-COMM-01-002.md): issue_comment types:created 不支持时应给出降级指引   - **维度**: 兼容性   - **评级**: 部分不符
- [COMPAT-CONCUR-01-003](case/COMPAT-CONCUR-01-003.md): concurrency preemption enable 行为差异   - **维度**: 兼容性   - **评级**: 部分不符
- [COMPAT-CONCUR-01-004](case/COMPAT-CONCUR-01-004.md): concurrency preemption events 越界时行为差异   - **维度**: 兼容性   - **评级**: 部分不符
- [COMPAT-EXPR-01-001](case/COMPAT-EXPR-01-001.md): success 关键字在条件表达式中的可用性   - **维度**: 兼容性   - **评级**: 部分不符
- [COMPAT-EXPR-01-003](case/COMPAT-EXPR-01-003.md): failure() 与 failed 关键字的处理行为差异   - **维度**: 兼容性   - **评级**: 部分不符
- [COMPAT-PATHS-01-001](case/COMPAT-PATHS-01-001.md): paths 过滤器 300 条边界测试   - **维度**: 兼容性   - **评级**: 部分不符
- [COMPAT-PERM-01-002](case/COMPAT-PERM-01-002.md): 未声明 permissions 时 fork PR 写操作隔离   - **维度**: 兼容性   - **评级**: 部分不符
- [COMPAT-RUNSON-01-002](case/COMPAT-RUNSON-01-002.md): runs-on 标签体系——单标签字符串应报错
- [COMPAT-SHELL-01-002](case/COMPAT-SHELL-01-002.md): 默认工作目录隐式行为差异 - 未显式声明时是否为仓库根目录
- [COMPAT-SHELL-01-003](case/COMPAT-SHELL-01-003.md): Windows runner 默认 shell 差异
- [COMPAT-VARS-01-006](case/COMPAT-VARS-01-006.md): vars 在 Action 中的可用性差异
- [REL-ARTCONC-01-063](case/REL-ARTCONC-01-063.md): 制品并发写一致性——多 job 同时 upload-artifact 同名 artifact
- [REL-BIGRUNNER-01-066](case/REL-BIGRUNNER-01-066.md): 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率
- [REL-CACHE-01-046](case/REL-CACHE-01-046.md): 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰
- [REL-CACHEPERF-01-054](case/REL-CACHEPERF-01-054.md): 缓存加速比——cache 命中 vs 未命中构建耗时对比
- [REL-CANCEL-01-029](case/REL-CANCEL-01-029.md): 多并发 run 中取消指定 run——取消应按 run_id 寻址而非栈序误杀最新一条
- [REL-CANCELREL-01-061](case/REL-CANCELREL-01-061.md): 取消操作可靠性——queued/running/post 各阶段取消状态正确过渡
- [REL-CLUSTER-01-001](case/REL-CLUSTER-01-001.md): 集群断连恢复后断连窗口任务日志同步
- [REL-DEBOUNCE-01-001](case/REL-DEBOUNCE-01-001.md): 触发幂等——同分支 10 秒内连续 5 次 push 的 run 记录应与事件一一对账
- [REL-DEBOUNCE-01-002](case/REL-DEBOUNCE-01-002.md): 触发幂等——10 秒内推送 10 个 tag 的 run 记录应与 tag 事件 100% 可解释
- [REL-FAIR-01-044](case/REL-FAIR-01-044.md): 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调度
- [REL-FAULT-01-036](case/REL-FAULT-01-036.md): 故障注入——runner 与平台心跳分区 60 秒后恢复，job 应续跑完成而非误判失败
- [REL-FAULT-01-037](case/REL-FAULT-01-037.md): 故障注入——runner 与平台心跳分区 300 秒，行为应确定可归因（续跑或明确失联失败）
- [REL-FAULT-01-039](case/REL-FAULT-01-039.md): 故障注入——排队期唯一匹配 runner 下线，job 应重调度或有界等待后明确失败
- [REL-FLOOD-01-036](case/REL-FLOOD-01-036.md): 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失
- [REL-FLOOD-01-037](case/REL-FLOOD-01-037.md): 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃
- [REL-K8S-01-045](case/REL-K8S-01-045.md): 自托管 K8s Runner 弹性伸缩——min=1/max=1 时并发 3 个 jobs 应排队执行
- [REL-K8S-01-046](case/REL-K8S-01-046.md): K8s 单集群接入与 NPU 资源发现正确性
- [REL-K8S-01-047](case/REL-K8S-01-047.md): Karmada 多集群接入、聚合资源发现与指定成员集群调度
- [REL-K8S-01-048](case/REL-K8S-01-048.md): Karmada 按卡型号/数量自动分发与成员资源不足时的终态语义
- [REL-K8S-01-049](case/REL-K8S-01-049.md): pod NPU 单卡/多卡调度正确性与非法请求 Pending 语义
- [REL-K8S-01-050](case/REL-K8S-01-050.md): 【回归】pod 多副本任务（Worker）指定 NPU 调度——当前已知不通过，修复后回归
- [REL-K8S-01-051](case/REL-K8S-01-051.md): 同一集群重复接入的幂等性
- [REL-LATENCY-01-050](case/REL-LATENCY-01-050.md): 调度延迟基准——queued→running P50/P95 等待时间
- [REL-LONG-01-043](case/REL-LONG-01-043.md): 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常
- [REL-MATRIX-01-026](case/REL-MATRIX-01-026.md): matrix fail-fast=true——任意 job 实例失败应立即取消其余实例
- [REL-MATRIX-01-038](case/REL-MATRIX-01-038.md): 大规模 matrix——20 个组合应全部生成并正确调度
- [REL-MATRIX-01-039](case/REL-MATRIX-01-039.md): 大规模 matrix——50 个组合应全部生成并正确调度
- [REL-MATRIXFAIR-01-056](case/REL-MATRIXFAIR-01-056.md): 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 的无饿死验证
- [REL-MEM-01-020](case/REL-MEM-01-020.md): Runner 内存边界——small runner 分配 7.5 GB 应成功
- [REL-MEM-01-021](case/REL-MEM-01-021.md): Runner 内存越界——small runner 分配 9 GB 应被 OOM kill
- [REL-NEST-01-023](case/REL-NEST-01-023.md): workflow_call 嵌套边界——2 层嵌套调用应成功执行
- [REL-NEST-01-024](case/REL-NEST-01-024.md): workflow_call 嵌套越界——3 层嵌套调用应被拒绝
- [REL-PREEMPT-01-006](case/REL-PREEMPT-01-006.md): preemption events 越界值——配置 11 个应被拒绝
- [REL-PRESSURE-01-055](case/REL-PRESSURE-01-055.md): 并发压测——concurrency.max=5 时触发 20 个 workflow 的排队与完成率
- [REL-PROJLIMIT-01-067](case/REL-PROJLIMIT-01-067.md): 项目级 workflow 并发上限——200 条同时触发时全部完成无丢失
- [REL-PROJLIMIT-01-068](case/REL-PROJLIMIT-01-068.md): 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排队
- [REL-RERUN-01-011](case/REL-RERUN-01-011.md): rerun 边界值——单条运行连续重新运行 3 次应全部成功
- [REL-RERUN-01-012](case/REL-RERUN-01-012.md): rerun 越界值——尝试第 4 次重新运行应被系统拒绝
- [REL-RUNNER-01-049-V2](case/REL-RUNNER-01-049-V2.md): Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存/磁盘 vs 声明值
- [REL-RUNNER-01-049](case/REL-RUNNER-01-049.md): Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值
- [REL-SCHED-01-057](case/REL-SCHED-01-057.md): 资源调度状态一致性——空闲 runner 存在时 job 不应死等
- [REL-TIMEOUT-01-007](case/REL-TIMEOUT-01-007.md): job timeout 边界值——359 分钟运行应在 360 分钟边界前完成
- [REL-TIMEOUT-01-008](case/REL-TIMEOUT-01-008.md): job timeout 越界触发——361 分钟应在 360 分钟被强制终止
- [REL-TIMEOUT-01-010](case/REL-TIMEOUT-01-010.md): 默认超时——未声明 timeout-minutes 运行 361 分钟应被强制终止
- [SEC-SECMGMT-01-001](case/SEC-SECMGMT-01-001.md): Secret 写入后任何 API/UI 路径绝不应回读明文
- [SEC-SECMGMT-01-002](case/SEC-SECMGMT-01-002.md): 无权限角色对 secret 的创建/更新/删除必须被拒且不改变现有集合
- [SEC-SIDE-01-002](case/SEC-SIDE-01-002.md): Secret 不经 artifact 侧信道绕过脱敏外泄
- [SEC-SUPPLY-01-001](case/SEC-SUPPLY-01-001.md): 第三方 Action 引用应支持完整 commit hash 固定
- [SEC-SUPPLY-01-002](case/SEC-SUPPLY-01-002.md): commit hash 不匹配时第三方 Action 应被拒绝执行
- [SEC-SUPPLY-01-003](case/SEC-SUPPLY-01-003.md): 第三方 Action 来源应具备信任边界（typosquatting 限制）
- [SEC-TOCTOU-01-003](case/SEC-TOCTOU-01-003.md): 评论触发后被编辑的内容绝不应改变已排队/运行中 workflow 读取的事件负载
- [SEC-TOKEN-01-001](case/SEC-TOKEN-01-001.md): fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限
- [SEC-TOKEN-01-002](case/SEC-TOKEN-01-002.md): fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝
- [SEC-TOKEN-01-003](case/SEC-TOKEN-01-003.md): run 结束后旧 ATOMGIT_TOKEN 调用任何 API 必须失效
- [SEC-TOKEN-01-004](case/SEC-TOKEN-01-004.md): 残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权
- [SEC-WFRUN-01-001](case/SEC-WFRUN-01-001.md): 不可信运行绝不应存在隐式拉起高权限后续运行的链式路径
- [USE-SEARCH-01-001](case/USE-SEARCH-01-001.md): 日志搜索与下载功能可用且交互流畅   - **维度**: usability   - **评级**: 部分不符

## 4. 断言一致 (417 例)

共 417 例断言一致 YAML 已复制到 [outputs/accessable/](https://github.com/opensourceways/gitcode-action-foundational-tests/tree/main/phase02/agents/expect-execute-consistency/outputs/accessable/)。

## 5. 逐用例详情

见 [outputs/case/](https://github.com/opensourceways/gitcode-action-foundational-tests/tree/main/phase02/agents/expect-execute-consistency/outputs/case/)。
