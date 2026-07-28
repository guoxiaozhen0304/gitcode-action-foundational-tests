# 断言-步骤一致性报告

**日期**: 2026-07-28
**数据源**: [phase01/runs/2026-07-27-01/cases/](https://github.com/opensourceways/gitcode-action-foundational-tests/tree/main/phase01/runs/2026-07-27-01/cases/)
**用例总数**: 498

---

## 1. 总览

| 维度 | 断言一致 | 部分不符 | 完全不符 |
|------|:---:|:---:|:---:|
| 完备性 | 96 | 12 | 2 |
| 兼容性 | 127 | 4 | 6 |
| 可靠性 | 85 | 18 | 2 |
| 安全性 | 45 | 19 | 3 |
| 易用性 | 43 | 10 | 0 |
| 易用性/兼容性 | 13 | 7 | 0 |
| 易用性/安全性 | 2 | 3 | 0 |
| 易用性/可靠性 | 1 | 0 | 0 |
| **合计** | **412** | **73** | **13** |

---

## 2. 完全不符 (13 例)

- [COMP-CALL-01-001](case/COMP-CALL-01-001.md): 2 层 workflow_call 嵌套正常执行
- [COMP-CALL-01-002](case/COMP-CALL-01-002.md): 3 层 workflow_call 嵌套应被拒绝
- [COMPAT-ISOLATE-01-001](case/COMPAT-ISOLATE-01-001.md): Runner 环境隔离——跨 job 文件隔离
- [COMPAT-ISOLATE-01-002](case/COMPAT-ISOLATE-01-002.md): Runner 环境隔离——跨 job 环境变量隔离
- [COMPAT-LIMIT-01-001](case/COMPAT-LIMIT-01-001.md): 单次推送多个 tag 的事件生成上限行为
- [COMPAT-LIMIT-01-002](case/COMPAT-LIMIT-01-002.md): workflow_dispatch 输入数量上限与非默认分支可用性
- [COMPAT-MATRIX-01-003](case/COMPAT-MATRIX-01-003.md): matrix 三维展开不被支持时的差异
- [COMPAT-MATRIX-01-004](case/COMPAT-MATRIX-01-004.md): matrix include 无基础变量不被支持时的差异
- [REL-BIGRUNNER-01-066](case/REL-BIGRUNNER-01-066.md): 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率
- [REL-MATRIX-01-026](case/REL-MATRIX-01-026.md): matrix fail-fast=true——任意 job 实例失败应立即取消其余实例
- [SEC-ARTF-01-003](case/SEC-ARTF-01-003.md): 宽通配打包含敏感文件名的 artifact 绝不应在无警示情况下静默成功且可被无痕下载
- [SEC-AUDIT-01-001](case/SEC-AUDIT-01-001.md): 敏感操作（secret/权限/rerun/审批/评论触发）必须全部留有不可擦除的审计记录
- [SEC-OIDC-01-001](case/SEC-OIDC-01-001.md): OIDC/短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案   - **维度**: 安全性   - **评级**: 完全不符

## 3. 部分不符 (73 例)

- [COMP-PRTARGET-01-001](case/COMP-PRTARGET-01-001.md): pull_request_target 默认使用 base 分支 workflow 版本
- [COMP-PRTARGET-01-002](case/COMP-PRTARGET-01-002.md): 显式 checkout head.sha 后执行不可信代码的风险可控
- [COMP-PUSH-01-001](case/COMP-PUSH-01-001.md): 匹配 branches 的 push 正确触发 workflow
- [COMP-SCRIPT-01-081](case/COMP-SCRIPT-01-081.md): 仓库内脚本执行与路径验证
- [COMP-STAGES-01-004](case/COMP-STAGES-01-004.md): map 形式 stages 按定义顺序串行执行（回归保护）
- [COMP-STATUS-01-001](case/COMP-STATUS-01-001.md): 运行状态机 queued 到 completed 转换正确
- [COMP-STATUS-01-002](case/COMP-STATUS-01-002.md): 失败 step 的日志完整保留且可查看
- [COMP-STEP-01-069](case/COMP-STEP-01-069.md): step 必填与核心字段 name run uses 验证
- [COMP-TIMEOUT-01-001](case/COMP-TIMEOUT-01-001.md): 未声明 timeout-minutes 的 job 在 360 分钟内正常完成
- [COMP-UNKNOWN-01-003](case/COMP-UNKNOWN-01-003.md): 未声明 select 的 stage 与 job 默认被执行
- [COMP-WFLOW-01-061](case/COMP-WFLOW-01-061.md): workflow name 与 on 字段必填与类型验证
- [COMP-WFLOW-01-063](case/COMP-WFLOW-01-063.md): workflow concurrency 并发控制字段验证
- [COMPAT-CACHE-01-002](case/COMPAT-CACHE-01-002.md): cache 行为等价性——fork PR 写隔离
- [COMPAT-ENV-01-001](case/COMPAT-ENV-01-001.md): ATOMGIT_SHA 环境变量应正确返回触发提交 SHA
- [COMPAT-EXPR-01-002](case/COMPAT-EXPR-01-002.md): success() 函数的处理行为差异
- [COMPAT-INPUTS-01-002](case/COMPAT-INPUTS-01-002.md): workflow_dispatch inputs 类型限制 - string 正常通过
- [REL-ARTPERF-01-053-V2](case/REL-ARTPERF-01-053-V2.md): 制品传输性能——1GB artifact 上传下载耗时
- [REL-ARTPERF-01-053](case/REL-ARTPERF-01-053.md): 制品传输性能——100MB artifact 上传下载耗时
- [REL-CACHE-01-047](case/REL-CACHE-01-047.md): cache 容量上限探测——500MB/1GB/2GB 单 cache 的接受/拒绝语义
- [REL-CACHE-01-048](case/REL-CACHE-01-048.md): cache 同 key 并发写一致性——3 方并行写同一 key 不得产生混合/损坏内容
- [REL-CACHEPERF-01-054](case/REL-CACHEPERF-01-054.md): 缓存加速比——cache 命中 vs 未命中构建耗时对比
- [REL-CANCELREL-01-061](case/REL-CANCELREL-01-061.md): 取消操作可靠性——queued/running/post 各阶段取消状态正确过渡
- [REL-FAIR-01-044](case/REL-FAIR-01-044.md): 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调度
- [REL-FAULT-01-031](case/REL-FAULT-01-031.md): 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失败并保留已执行日志
- [REL-FAULT-01-032](case/REL-FAULT-01-032.md): 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误
- [REL-FLOOD-01-036](case/REL-FLOOD-01-036.md): 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失
- [REL-FLOOD-01-037](case/REL-FLOOD-01-037.md): 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃
- [REL-LATENCY-01-050](case/REL-LATENCY-01-050.md): 调度延迟基准——queued→running P50/P95 等待时间
- [REL-LOG-01-040](case/REL-LOG-01-040.md): 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看
- [REL-LOGPERF-01-051](case/REL-LOGPERF-01-051.md): 日志加载性能——50MB 日志下载与查看耗时
- [REL-MATRIX-01-040](case/REL-MATRIX-01-040.md): matrix 组合数边界——256 组合（GitHub 上限）应全部展开或被明确拒绝
- [REL-MATRIX-01-041](case/REL-MATRIX-01-041.md): matrix 组合数越界——300 组合超上限时应明确报错（含上限值）不得静默截断
- [REL-VCJOB-01-002](case/REL-VCJOB-01-002.md): 大规模 vcjob 并发提交（≥50）无丢失、无级联失败   - **维度**: 可靠性   - **评级**: 部分不符
- [REL-YAMLCACHE-01-060](case/REL-YAMLCACHE-01-060.md): Workflow YAML 缓存失效——修改后无旧代码残留
- [SEC-ARTF-01-001](case/SEC-ARTF-01-001.md): fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执行
- [SEC-ARTF-01-002](case/SEC-ARTF-01-002.md): 跨仓库 artifact 下载返回 403 或 404
- [SEC-BASE-01-001](case/SEC-BASE-01-001.md): pull_request_target 使用 base 分支的 workflow 版本
- [SEC-BASE-01-002](case/SEC-BASE-01-002.md): fork PR 改 workflow 不被 pull_request_target 采用
- [SEC-CACHE-01-001](case/SEC-CACHE-01-001.md): fork PR 写入的 cache 必须不可被主仓后续 workflow 读取
- [SEC-CACHE-01-002](case/SEC-CACHE-01-002.md): 主仓 cache restore 对 fork cache miss
- [SEC-COMM-01-001](case/SEC-COMM-01-001.md): issue_comment/pull_request_comment 触发关键字过滤必须不可被绕过   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-COMM-01-002](case/SEC-COMM-01-002.md): 引用/反讽/代码块内嵌指令文本绝不应造成 pull_request_comment 预期外触发   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-COMM-01-003](case/SEC-COMM-01-003.md): 变形伪装评论（大小写/多余空白/markdown 包裹）不得绕过 comments 过滤语义   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-LOG-01-001](case/SEC-LOG-01-001.md): 无权限角色读取/下载运行日志必须被拒，过期日志绝不应可恢复   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-LOG-01-002](case/SEC-LOG-01-002.md): 导出/历史日志副本中 secret 原值命中数必须为 0，遮蔽状态不可回退   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-MASK-01-003](case/SEC-MASK-01-003.md): Secret 日志脱敏不可通过 base64 编码绕过   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-MASK-01-004](case/SEC-MASK-01-004.md): Secret 日志脱敏不可通过字符串拼接或插值绕过   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-MASK-01-006](case/SEC-MASK-01-006.md): Secret 日志脱敏不可通过分片输出绕过   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-NAME-01-003](case/SEC-NAME-01-003.md): 可遮蔽系统变量的 secret 命名（ATOMGIT_前缀/非法字符/数字开头）创建时必须被拒   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-NAME-01-004](case/SEC-NAME-01-004.md): 与系统变量同名的用户自定义值绝不应覆盖 job 环境中的平台注入值   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-ORG-01-001](case/SEC-ORG-01-001.md): 可见范围外仓库的 workflow 绝不应读到组织级 secret 原值   - **维度**: 安全性   - **评级**: 部分不符
- [SEC-TOKEN-01-004](case/SEC-TOKEN-01-004.md): 残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权
- [SEC-WCMD-01-002](case/SEC-WCMD-01-002.md): 跨运行 artifact 必须被视为不可信数据
- [USE-ACT-01-004](case/USE-ACT-01-004.md): 文档短名与市场名两种写法解析一致性验证
- [USE-EXPR-01-001](case/USE-EXPR-01-001.md): 引用不存在的上下文属性时报错应包含原始表达式与错误类型
- [USE-EXPR-01-002](case/USE-EXPR-01-002.md): 调用未知函数时报错应提示函数名错误与修正方向
- [USE-INPT-01-002](case/USE-INPT-01-002.md): 使用 boolean 类型 input 时报错应提示仅支持 string
- [USE-LBL-01-001](case/USE-LBL-01-001.md): runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表
- [USE-LOG-01-001](case/USE-LOG-01-001.md): 多 step 日志按时间线组织且边界清晰
- [USE-MASK-01-001](case/USE-MASK-01-001.md): secret 脱敏文档描述与实际行为一致并给出缓解建议
- [USE-MD-01-001](case/USE-MD-01-001.md): ATOMGIT_STEP_SUMMARY 写入的 Markdown 正确渲染为 HTML
- [USE-NEST-01-001](case/USE-NEST-01-001.md): workflow_call 嵌套 3 层时报错应明确提示上限为 2 层
- [USE-ONBD-01-001](case/USE-ONBD-01-001.md): 新手快速开始路径端到端可复刻走查（判定方式：llm_assisted）
- [USE-OS-01-001](case/USE-OS-01-001.md): runner.os 返回值与文档声明的平台支持一致
- [USE-PERM-01-002](case/USE-PERM-01-002.md): 使用 GitHub 权限域命名时报错应给出 GitCode 对照表
- [USE-RUN-01-002](case/USE-RUN-01-002.md): 使用单标签 ubuntu-latest 时报错应给出三段式格式指引
- [USE-SEARCH-01-001](case/USE-SEARCH-01-001.md): 日志搜索与下载功能可用且交互流畅
- [USE-SECNAME-01-001](case/USE-SECNAME-01-001.md): Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误
- [USE-SECNAME-01-002](case/USE-SECNAME-01-002.md): Secret 名称以数字开头时应给出命名规则错误
- [USE-STAT-01-002](case/USE-STAT-01-002.md): 使用 success() 带括号时报错应提示 GitCode 括号差异
- [USE-TYPE-01-002](case/USE-TYPE-01-002.md): 使用 GitHub types 命名 opened/synchronize 时应给出可理解提示
- [USE-YAML-01-001](case/USE-YAML-01-001.md): 缺少必填字段 on 时报错应指出具体字段名与位置
- [USE-YAML-01-002](case/USE-YAML-01-002.md): YAML 缩进错误时报错应指出具体行号与列号

## 4. 断言一致 (412 例)

共 412 例断言一致的用例 YAML 已复制到 [outputs/accessable/](https://github.com/opensourceways/gitcode-action-foundational-tests/tree/main/phase02/agents/expect-execute-consistency/outputs/accessable/)，可直接 dispatch。

## 5. 逐用例详情

每个用例的详细分析见 [outputs/case/](https://github.com/opensourceways/gitcode-action-foundational-tests/tree/main/phase02/agents/expect-execute-consistency/outputs/case/)。
