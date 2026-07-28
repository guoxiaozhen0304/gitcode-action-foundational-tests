# PASS 归档索引 · 2026-07-28-01

- **run-id**: 2026-07-28-01
- **PASS 归档条数**: 167
- **数据源**: results/ 逐文件去重（非 summary.json）
- **生成时间**: 2026-07-28 17:41:01

| # | case_id | dimension | priority | title |
|---|---|---|---|---|
| 1 | COMP-ATOMGIT-01-048 | completeness | P1 | atomgit 事件相关属性可访问性 |
| 2 | COMP-BOUND-01-084 | completeness | P1 | 路径与分支过滤组合及否定模式边界验证 |
| 3 | COMP-BOUND-01-086 | completeness | P1 | 矩阵构建 include exclude 与单值边界验证 |
| 4 | COMP-CTX-01-053 | completeness | P1 | 上下文在 Action 插件参数中注入验证 |
| 5 | COMP-CTX-01-054 | completeness | P1 | pull_request 触发下 inputs 上下文求值裁定 |
| 6 | COMP-CTX-01-055 | completeness | P1 | workflow_dispatch 触发下 inputs 正常求值（回归保护） |
| 7 | COMP-DIR-01-001 | completeness | P1 | .gitcode/workflows/ 下的 YAML 被正确识别并触发 |
| 8 | COMP-EXPR-01-057 | completeness | P1 | format substring replace 函数边界行为 |
| 9 | COMP-EXPR-01-059 | completeness | P2 | 未文档化函数 default() 的存在性与求值记录 |
| 10 | COMP-ISOLATION-01-002 | completeness | P0 | 环境变量不跨 job 泄漏 |
| 11 | COMP-ISOLATION-01-003 | completeness | P1 | container.volumes 常规挂载在托管 Runner 的行为记录 |
| 12 | COMP-ISOLATION-01-004 | completeness | P1 | 托管 Runner 上特权 options 与敏感路径挂载的边界核查 |
| 13 | COMP-JOB-01-066 | completeness | P1 | job 必填字段 name runs-on steps 验证 |
| 14 | COMP-JOB-01-067 | completeness | P1 | job 可选字段 env if timeout-minutes needs 验证 |
| 15 | COMP-JOB-01-068 | completeness | P1 | job strategy 矩阵与 continue-on-error 验证 |
| 16 | COMP-PR-01-002 | completeness | P0 | pull_request_target 可访问 secrets 且 TOKEN 拥有写权限 |
| 17 | COMP-PRTARGET-01-003 | completeness | P1 | fork PR 按文档推荐配置 pull_request_target 的 secret 暴露面核查 |
| 18 | COMP-PUSH-01-002 | completeness | P1 | 不匹配 branches 的 push 不触发 workflow |
| 19 | COMP-PUSH-01-003 | completeness | P1 | paths 过滤匹配前 300 个变更文件行为符合预期 |
| 20 | COMP-RUNNER-01-001 | completeness | P1 | 三段式标签正确调度到对应规格 Runner |
| 21 | COMP-RUNNER-01-002 | completeness | P1 | runs-on default 等效 ubuntu-latest x64 small |
| 22 | COMP-RUNNER-01-080 | completeness | P1 | runner 上下文属性可访问性验证 |
| 23 | COMP-RUNNER-01-081 | completeness | P1 | 四段式 runs-on（codearts-hosted 首段）调度行为裁定 |
| 24 | COMP-SECRET-01-002 | completeness | P0 | secret 原始值不应以明文出现在标准日志中 |
| 25 | COMP-SECRET-01-003 | completeness | P0 | base64 编码后的 secret 是否仍被脱敏 |
| 26 | COMP-STAGES-01-001 | completeness | P1 | stages 阶段间串行、阶段内 job 并行执行 |
| 27 | COMP-STEP-01-070 | completeness | P1 | step 可选字段 id env if with 验证 |
| 28 | COMP-SYSENV-01-060 | completeness | P1 | ATOMGIT 系统环境变量值正确性 |
| 29 | COMP-TRIG-01-072 | completeness | P1 | push 事件关键字段与过滤验证 |
| 30 | COMP-TRIG-01-073 | completeness | P1 | pull_request 事件关键字段与 types 验证 |
| 31 | COMP-TRIG-01-074 | completeness | P1 | workflow_dispatch 事件关键字段与 inputs 验证 |
| 32 | COMP-TRIG-01-076 | completeness | P1 | issue_comment 事件关键字段与 types 验证 |
| 33 | COMP-TRIG-01-077 | completeness | P1 | pull_request_comment 事件关键字段与过滤验证 |
| 34 | COMP-TRIG-01-078 | completeness | P1 | 多事件组合与分支路径过滤验证 |
| 35 | COMP-TRIG-01-080 | completeness | P2 | 触发事件别名 pr_comment 的有效性与等价性记录 |
| 36 | COMP-VARREF-01-083 | completeness | P1 | YAML 表达式与 Shell 环境变量引用方式验证 |
| 37 | COMP-VARREF-01-084 | completeness | P2 | ${gitcode_*} 与 ${PIPELINE_*} 非标准插值的求值行为记录 |
| 38 | COMP-WFLOW-01-062 | completeness | P1 | workflow env 与 defaults 字段验证 |
| 39 | COMPAT-ACTION-01-001 | compatibility | P1 | checkout 短名等价性——ref 参数支持 |
| 40 | COMPAT-ACTION-01-002 | compatibility | P1 | checkout 短名等价性——path 参数支持 |
| 41 | COMPAT-ACTION-01-003 | compatibility | P1 | GitHub 风格 action 引用 actions/checkout@v4 的解析域探测 |
| 42 | COMPAT-ACTION-01-004 | compatibility | P1 | 官方文档示例 docker/build-push-action@v6 引用的可用性仲裁 |
| 43 | COMPAT-CACHE-01-001 | compatibility | P1 | cache 行为等价性——缓存命中场景 |
| 44 | COMPAT-COMM-01-001 | compatibility | P1 | issue_comment types 命名差异 - GitCode 合法 types 应被接受 |
| 45 | COMPAT-COMM-01-002 | compatibility | P1 | issue_comment types:created 不支持时应给出降级指引 |
| 46 | COMPAT-CTX-01-001 | compatibility | P1 | 使用 github.ref 上下文应报错或求值为空 |
| 47 | COMPAT-CTX-01-002 | compatibility | P1 | 使用 atomgit.ref 上下文应正确返回触发引用 |
| 48 | COMPAT-CTX-01-003 | compatibility | P1 | github 上下文嵌套属性访问应报错而非返回空 |
| 49 | COMPAT-CTX-01-004 | compatibility | P1 | atomgit.actor 规格自相矛盾的实测仲裁 |
| 50 | COMPAT-CTX-01-005 | compatibility | P1 | atomgit 缺位字段（job/run_attempt/triggering_actor/ref_protected）求值行为探测 |
| 51 | COMPAT-DIR-01-001 | compatibility | P1 | 工作流目录差异——.gitcode/workflows/ 正常识别 |
| 52 | COMPAT-DIR-01-002 | compatibility | P1 | 工作流目录差异——.github/workflows/ 不应被识别 |
| 53 | COMPAT-ENV-01-002 | compatibility | P1 | GITHUB_SHA 环境变量在 GitCode 中应为空或未定义 |
| 54 | COMPAT-ENV-01-003 | compatibility | P1 | GITHUB_ENV 环境变量不应被静默映射到 ATOMGIT_ENV |
| 55 | COMPAT-ENV-01-004 | compatibility | P1 | ATOMGIT_ENV 覆写系统默认变量的防护（对齐 GitHub 同名禁止） |
| 56 | COMPAT-ENV-01-005 | compatibility | P1 | RUNNER_* 系列环境变量在 GitCode Runner 上的注入情况探测 |
| 57 | COMPAT-EXPR-01-001 | compatibility | P1 | success 关键字在条件表达式中的可用性 |
| 58 | COMPAT-EXPR-01-004 | compatibility | P1 | contains 表达式大小写敏感边界 |
| 59 | COMPAT-EXPR-01-005 | compatibility | P1 | contains 表达式空值与空字符串边界 |
| 60 | COMPAT-EXPR-01-006 | compatibility | P1 | hashFiles 表达式无匹配路径边界 |
| 61 | COMPAT-EXPR-01-007 | compatibility | P1 | hashFiles 表达式多路径组合边界 |
| 62 | COMPAT-EXPR-01-008 | compatibility | P1 | toJson 表达式输出格式差异（pretty-print vs compact） |
| 63 | COMPAT-EXPR-01-009 | compatibility | P1 | loose equality 跨类型强制求值差异 |
| 64 | COMPAT-EXPR-01-010 | compatibility | P1 | loose equality null 与空字符串及零的等价性差异 |
| 65 | COMPAT-EXPR-01-011 | compatibility | P1 | join() 函数缺失时的降级行为 |
| 66 | COMPAT-EXPR-01-012 | compatibility | P1 | fromJSON() 函数缺失时的降级行为 |
| 67 | COMPAT-EXPR-01-015 | compatibility | P1 | startsWith/endsWith 大小写敏感性两侧文档矛盾的差异确认 |
| 68 | COMPAT-IF-01-001 | compatibility | P1 | step 失败后后续 step 默认跳过行为 |
| 69 | COMPAT-IF-01-002 | compatibility | P1 | continue-on-error 标记后失败 step 不阻断后续执行 |
| 70 | COMPAT-MASK-01-001 | compatibility | P0 | 直接 echo secrets 值应在日志中被脱敏 |
| 71 | COMPAT-MASK-01-002 | compatibility | P0 | 通过 env 注入 secret 后输出应在日志中被脱敏 |
| 72 | COMPAT-NEEDS-01-001 | compatibility | P1 | needs 上下文存在性与 outputs/result 字段对齐（规格矛盾仲裁） |
| 73 | COMPAT-NEEDS-01-002 | compatibility | P1 | needs 上游 job 被跳过时的 result 取值语义 |
| 74 | COMPAT-NEEDS-01-003 | compatibility | P1 | matrix 上游 job 的 needs outputs 聚合语义与未声明 output 边界 |
| 75 | COMPAT-OUTCOME-01-001 | compatibility | P1 | continue-on-error false 时 outcome 与 conclusion 应均为 failure |
| 76 | COMPAT-OUTPUT-01-001 | compatibility | P1 | 跨 Job 引用未声明 output 时返回空值的差异 |
| 77 | COMPAT-PERM-01-002 | compatibility | P0 | 未声明 permissions 时 fork PR 写操作隔离 |
| 78 | COMPAT-PERM-01-004 | compatibility | P0 | permissions 命名差异——GitCode repository 权限项正常生效 |
| 79 | COMPAT-PERM-01-005 | compatibility | P0 | permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异 |
| 80 | COMPAT-PR-01-001 | compatibility | P0 | pull_request types 命名差异 - GitCode 合法 types 应被接受 |
| 81 | COMPAT-PR-01-010 | compatibility | P1 | 存在合并冲突的 PR 的触发行为（GitHub 不触发）对齐确认 |
| 82 | COMPAT-RUNNER-01-001 | compatibility | P1 | runner.os 在 Linux Runner 上应返回 Linux |
| 83 | COMPAT-RUNNER-01-002 | compatibility | P1 | runner.arch 在 x86_64 Runner 上应返回 X64 |
| 84 | COMPAT-RUNNER-01-003 | compatibility | P2 | self-hosted 标签不被支持时应明确报错 |
| 85 | COMPAT-RUNNER-01-006 | compatibility | P2 | Runner 未预装 Java 工具链与 GitHub 差异 |
| 86 | COMPAT-RUNNER-01-007 | compatibility | P1 | Runner 预装工具链规格清单与实测全面对账 |
| 87 | COMPAT-RUNNER-01-008 | compatibility | P1 | 与 GitHub hosted image 的关键能力差距（docker 守护进程、浏览器）探测 |
| 88 | COMPAT-RUNSON-01-001 | compatibility | P1 | runs-on 标签体系——三段式数组正常匹配 |
| 89 | COMPAT-RUNSON-01-002 | compatibility | P1 | runs-on 标签体系——单标签字符串应报错 |
| 90 | COMPAT-SHELL-01-001 | compatibility | P1 | 默认 shell 隐式行为差异 - 未显式声明时是否为 bash |
| 91 | COMPAT-SHELL-01-002 | compatibility | P1 | 默认工作目录隐式行为差异 - 未显式声明时是否为仓库根目录 |
| 92 | COMPAT-TARGET-01-001 | compatibility | P0 | pull_request_target 默认 checkout 应为 base 分支而非 head 分支 |
| 93 | COMPAT-TARGET-01-002 | compatibility | P0 | pull_request_target 在 fork 场景下应保持 secret 隔离 |
| 94 | COMPAT-TOKEN-01-001 | compatibility | P0 | ATOMGIT_TOKEN 应正确返回有效令牌 |
| 95 | COMPAT-TOKEN-01-002 | compatibility | P0 | GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射 |
| 96 | COMPAT-TOKEN-01-003 | compatibility | P0 | GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN |
| 97 | COMPAT-VARS-01-001 | compatibility | P1 | vars 上下文若支持应正确返回值 |
| 98 | COMPAT-VARS-01-002 | compatibility | P1 | vars 上下文若不支持应报错而非静默为空 |
| 99 | COMPAT-VARS-01-003 | compatibility | P1 | vars 项目级覆盖组织级的优先级差异 |
| 100 | COMPAT-VARS-01-004 | compatibility | P1 | vars 与 env 同名时的优先级差异 |
| 101 | COMPAT-WCMD-01-001 | compatibility | P2 | ::add-mask:: 不被支持时应静默降级而非报错 |
| 102 | COMPAT-WCMD-01-002 | compatibility | P2 | ::group:: 不被支持时应静默降级而非报错 |
| 103 | COMPAT-WCMD-01-003 | compatibility | P2 | ::stop-commands:: 不被支持时应静默降级而非报错 |
| 104 | COMPAT-WCMD-01-004 | compatibility | P1 | 注解命令 error/warning/notice 的不中断降级行为 |
| 105 | COMPAT-WCMD-01-005 | compatibility | P1 | debug 命令默认可见性与 GitHub ACTIONS_STEP_DEBUG 门控差异 |
| 106 | COMPAT-YAML-01-001 | compatibility | P2 | YAML 1.1 on 键布尔陷阱与 env 中 yes/no/on/off 字面量的解析行为 |
| 107 | REL-CACHE-01-046 | reliability | P1 | 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰 |
| 108 | REL-CONC-01-002 | reliability | P1 | concurrency.max=6 配置应被系统拒绝 |
| 109 | REL-DEBOUNCE-01-001 | reliability | P1 | 触发幂等——同分支 10 秒内连续 5 次 push 的 run 记录应与事件一一对账 |
| 110 | REL-DEBOUNCE-01-002 | reliability | P1 | 触发幂等——10 秒内推送 10 个 tag 的 run 记录应与 tag 事件 100% 可解释 |
| 111 | REL-DISK-01-019 | reliability | P1 | Runner 磁盘越界——small runner 写入 51 GB 应失败并报磁盘满 |
| 112 | REL-IGNORE-01-004 | reliability | P1 | concurrency IGNORE 策略——超上限运行应直接执行 |
| 113 | REL-LOG-01-041 | reliability | P2 | 单 job 日志大小上限探测——500MB 带序号日志的完整保留或明确截断标识 |
| 114 | REL-LOGSTABLE-01-059 | reliability | P1 | 日志系统稳定性——6 万行日志无乱序/无丢失/无截断 |
| 115 | REL-MATRIX-01-027 | reliability | P1 | matrix max-parallel=4——9 个组合应最多同时运行 4 个 |
| 116 | REL-MATRIXFAIR-01-056 | reliability | P1 | 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 的无饿死验证 |
| 117 | REL-MEM-01-020 | reliability | P1 | Runner 内存边界——small runner 分配 7.5 GB 应成功 |
| 118 | REL-MEM-01-021 | reliability | P1 | Runner 内存越界——small runner 分配 9 GB 应被 OOM kill |
| 119 | REL-NEEDS-01-027 | reliability | P0 | needs 依赖 matrix job 部分失败——无 if 条件的下游 job 应 skipped 而非执行 |
| 120 | REL-OUTPUT-01-017 | reliability | P1 | step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错 |
| 121 | REL-PATHS-01-014 | reliability | P1 | paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效 |
| 122 | REL-PATHS-01-015 | reliability | P1 | paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断 |
| 123 | REL-RUNNER-01-049 | reliability | P1 | Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值 |
| 124 | REL-TIMEOUT-01-011 | reliability | P2 | 自定义 timeout 超默认值——timeout-minutes=720 的接受/拒绝语义探测 |
| 125 | SEC-INJ-01-001 | security | P0 | 不可信 PR 标题不可直接插进 run 脚本导致命令注入 |
| 126 | SEC-INJ-01-002 | security | P0 | 不可信分支名不可直接插进 run 脚本导致命令注入 |
| 127 | SEC-INJ-01-003 | security | P0 | 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入 |
| 128 | SEC-INJ-01-004 | security | P0 | 不可信 commit message 不可直接插进 run 脚本导致命令注入 |
| 129 | SEC-INJ-01-005 | security | P0 | 表达式求值必须防止双重模板渲染（二次求值） |
| 130 | SEC-NET-01-001 | security | P0 | Runner 网络出站必须受控，防止 SSRF 与内网跳板 |
| 131 | SEC-ORG-01-002 | security | P1 | fork PR 触发的运行绝不应读取组织级 secret（与项目级同等隔离） |
| 132 | SEC-RUN-01-001 | security | P0 | Job 结束后 workspace 与临时文件必须被彻底清理 |
| 133 | SEC-RUN-01-002 | security | P0 | Runner 环境变量与共享目录必须跨 job 隔离 |
| 134 | SEC-SIDE-01-001 | security | P0 | Secret 不经 output 侧信道绕过脱敏外泄 |
| 135 | SEC-TOCTOU-01-001 | security | P0 | 审批后推送新 commit 不应被已授权特权运行执行 |
| 136 | SEC-TOCTOU-01-002 | security | P0 | 评论触发不应绕过代码固定与 PR 审批 |
| 137 | SEC-TOCTOU-01-003 | security | P1 | 评论触发后被编辑的内容绝不应改变已排队/运行中 workflow 读取的事件负载 |
| 138 | SEC-WCMD-01-001 | security | P0 | Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值 |
| 139 | USE-ACT-01-001 | usability | P1 | 使用裸插件名 checkout 时正常拉取官方 Action |
| 140 | USE-ACT-01-002 | usability | P1 | 使用 actions/checkout@v4 时报错应给出迁移指引 |
| 141 | USE-ANNOT-01-001 | usability | P1 | workflow 命令 ::error:: 与 ::warning:: 在日志中保留原文 |
| 142 | USE-CLI-01-001 | usability | P1 | Runner 无 gh 等效 CLI 时迁移指引的替代方案说明 |
| 143 | USE-CONT-01-001 | usability | P1 | container.image 文档声明可用与实际可用性的一致性 |
| 144 | USE-DEPR-01-001 | usability | P1 | 使用 ATOMGIT_OUTPUT 文件协议时正常生效 |
| 145 | USE-DEPR-01-002 | usability | P1 | 使用 ::set-output 时应给出弃用警告与替代示例 |
| 146 | USE-DIR-01-001 | usability | P1 | workflow 放置于 .gitcode/workflows/ 下可正常触发 |
| 147 | USE-DOC-01-004 | usability | P0 | workflow-commands 多行输出示例漏写重定向照抄得空输出 |
| 148 | USE-DOC-01-005 | usability | P0 | configure-steps 的 shell 类型与命令语言不匹配示例照抄失败 |
| 149 | USE-ENV-01-001 | usability | P1 | 使用 ATOMGIT_SHA 环境变量时正常取值 |
| 150 | USE-ENV-01-003 | usability | P1 | ATOMGIT 系统环境变量实际注入集合与文档清单双向 diff |
| 151 | USE-ENV-01-004 | usability | P0 | job env 在 shell 层与表达式层取值一致性（文档承诺兑现验证） |
| 152 | USE-EXPR-01-004 | usability | P2 | 未文档化函数 default() 的文档缺失 diff（与平台行为断言合并证据链） |
| 153 | USE-INPT-01-001 | usability | P1 | 使用 string 类型 input 时正常通过校验 |
| 154 | USE-LBL-01-002 | usability | P1 | runs-on 标签因容量不足排队时应提示排队状态而非无可用 runner |
| 155 | USE-LBL-01-004 | usability | P0 | quick-start 单标签写法 runs-on ubuntu-latest 的可调度性验证 |
| 156 | USE-MASK-01-002 | usability | P0 | 直接 echo secrets 值时文档描述的绕过风险与实际一致 |
| 157 | USE-ONBD-01-002 | usability | P0 | quick-start 示例提交后运行结果可见性检查点 |
| 158 | USE-OS-01-002 | usability | P1 | runner 上下文返回值精确格式与文档枚举值逐字符一致性 |
| 159 | USE-PERM-01-001 | usability | P1 | 使用 GitCode 权限域命名时正常生效 |
| 160 | USE-RUN-01-001 | usability | P1 | 使用三段式标签时 job 正常调度 |
| 161 | USE-STAT-01-001 | usability | P1 | 使用 always() 带括号时若被接受则正常执行 |
| 162 | USE-TOGGLE-01-001 | usability | P1 | 隐藏安全开关 ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS 默认值与文档缺失 |
| 163 | USE-TYPE-01-001 | usability | P1 | 使用 GitCode types 命名时正常触发 |
| 164 | USE-TYPE-01-003 | usability | P1 | pull_request_comment 与 pr_comment 事件名双轨的文档说明 |
| 165 | USE-UNKN-01-002 | usability | P1 | 未知字段报错若识别为 GitHub 特有应追加迁移提示 |
| 166 | USE-UNKN-01-003 | usability | P1 | step 标识 id 与 identifier 命名双轨的接受一致性与文档说明 |
| 167 | USE-VARS-01-002 | usability | P1 | 变量插值双语法与 atomgit 属性名的文档清单 diff 及求值探测 |
