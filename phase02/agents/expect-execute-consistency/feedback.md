# 一致性分析反馈记录

1.  trigger=pull_request， it can be trigger

<<<<<<< HEAD
---

## 2026-07-27 误报模式回写（基于 369 条基底用例全量研判）

> 背景：对 consistency-report.md 中 199 条 flagged 用例（28 完全不符 + 171 部分不符）逐条独立研判后，**122 条（61%）为分析器误报或可接受口径**，仅 41 条为真实缺陷必修订。以下误报模式请在下轮分析时校准，避免重复误报。

### 模式 1：job 级 `uses:` 可复用 workflow 被误判为「无步骤/空 workflow」

- **误判案例**：COMPAT-NEST-01-001、COMPAT-NEST-01-002、REL-NEST-01-023/024
- **问题**：可复用 workflow 调用是 job 级 `uses: ./.gitcode/workflows/xxx.yml`，job 内没有 steps 是语法常态。分析器把「无 steps」等同「空 workflow」，判 NOT COVERED / 完全不符
- **校准建议**：job 级 `uses:` 指向可复用 workflow 时，该 job 本身就是真实测试动作，嵌套调用真实发生；应判 GENUINE。需要检查的是 fixture/setup 是否提供了被引用的子 workflow 文件（REL-NEST-01-023/024 的真实缺陷正是 fixture 缺文件，而非「无步骤」）

### 模式 2：平台/action 产出的日志被忽略，误判 MISSING_SOURCE / UNVERIFIABLE

- **误判案例**：REL-FAULT-01-034（"cache miss" 由 cache action 内部日志产出）、REL-TIMEOUT-01-008/010（"timeout" 由平台终止日志产出）、USE-LOG-01-001（步骤名由平台步骤头产出）、REL-MEM-01-021（"Killed" 由内核产出）、USE-ACT-01-002（action 拒绝报错为平台产出）
- **校准建议**：CLAUDE.md 规则 1 已声明「平台/action 日志行 = GENUINE」，但实际分析未覆盖：cache/upload-artifact 等官方 action 的内部日志、平台终止/调度日志、平台步骤头（step name）。这几类产出源应列入白名单

### 模式 3：负向验证点的固有局限被计入问题

- **误判案例**：约 22 条（如 COMPAT-EXPR-01-002/003 条件式负向、REL 系列负向饿死/丢失点、COMP-RERUN-01-002/003 次数/时限上限）
- **问题**：「证明某事不发生」（无新运行、无丢失、无排队饿死）单次 workflow 执行无法自证，观测点本就在 harness 侧（运行列表对账、多次编排采样）。这是用例设计的固有分层，不是缺陷
- **校准建议**：负向验证点若可由 harness 编排观测（运行列表为空、计数对账、多次 dispatch 采样），且 yaml 已有对应 negative 断言或文本已声明观测方式，应判 COVERED 而非 UNVERIFIABLE。真正需要报的是：负向点既无 negative 断言、文本也未声明任何观测方式

### 模式 4：平台行为型用例的载荷 workflow 被判「all steps trivial」

- **误判案例**：约 20 条并发/排队/限流/取消/故障注入类（REL-CONC-01-001、REL-PRESSURE-01-055、REL-PROJLIMIT-01-067/068、REL-QUEUE-01-003、REL-K8S-01-045、REL-RERUN 系列等）
- **问题**：这类用例的被测对象是平台调度行为本身，workflow 只是载荷（sleep/echo 探针是刻意设计），并发与对账由 harness 编排。步骤「简单」不等于「空洞」
- **校准建议**：识别载荷型用例特征——断言目标是 run 计数/状态分布/时序（queued_count、completed_count、P50/P95、cancelled 数）而非日志内容时，sleep/echo 探针应判 GENUINE；检查重点应放在 trigger 配置是否与 `on:` 一致（如 REL-FLOOD-01-036/037 的真实缺陷就是 on 缺 push）

### 模式 5：`${{ }}` 动态求值与真实命令被误判

- **误判案例**：USE-CTX-01-001（`${{ atomgit.ref }}` 判 MISSING_SOURCE）、USE-DISP-01-002（inputs default 求值误判）、COMPAT-RUNNER-01-006（`java -version || true` 真实命令判 trivial）、COMPAT-SHELL-01-003（`echo %OS%` cmd 探针）、COMPAT-TOKEN-01-002（curl 真实 API 调用）、COMPAT-WCMD 系列（`::add-mask::` 本身就是对命令解析器的真实演练）
- **校准建议**：CLAUDE.md 规则 6 与护栏已覆盖但执行不严——含 `${{ }}` 的步骤、含除 echo 外真实命令的步骤、`::xxx::` workflow 命令演练，均不应判 VACUOUS/MISSING_SOURCE

### 模式 6：统计污染——"NOT COVERED" 被计入 "COVERED"

- **问题**：逐用例文件中 "NOT COVERED" 字样含 "COVERED" 子串，程序化统计时污染 verdict 分布（本次研判中 COMPAT-NEST-01-001 等因此出现「全 COVERED 却评级完全不符」的矛盾）
- **校准建议**：输出格式统一为 `COVERED` / `NOT_COVERED`（下划线连写），或统计端按词边界排除否定形式

### 差异记录类用例的特殊口径（非误报，需显式支持）

- **案例**：COMPAT-PR-01-003/004/005、COMP-SCHEDULE-01-002、COMP-PUSH-01-003、REL-PATHS-01-015、COMPAT-SCHEDULE-01-002
- **口径**：这类用例的预期结果就是「无运行/不触发」（记录 GitCode 与 GitHub 的已知差异），"无运行"本身即观测点。步骤不产出任何内容是正确的，不应判 VACUOUS/MISSING
- **校准建议**：识别预期结果含「GitCode 实际：…没有对应 workflow 运行（已知问题）」或验证点含「不通过…无运行」的差异记录类用例，单设口径判 COVERED

---

## 真实缺陷模式清单（本轮 41 条必修订的归类，供分析器强化检测）

1. **占位符断言无源**（17 条）：`equals "masked_with_asterisks"` 等断言值与任何步骤/平台输出都不可能匹配——这是分析器最应抓住的模式（MISSING_SOURCE），本轮对部分 SEC 用例漏报
2. **表达式/命令损坏**（6 条）：`${{{{ }}}}` 四重大括号、`${{i}}`（shell 循环变量误写为平台表达式）、curl 命令含字面 `\n`——建议增加静态 lint 规则直接扫描
3. **被测对象未构造**（9 条）：runs-on 规格与规格书不符（探针全写 small）、matrix 实例数不足、并发场景只有单 job、镜像不达规格量级
4. **fixture/结构缺失**（5 条）：setup 引用不存在的子 workflow 文件、reusable workflow 误放 step 级
5. **断言逻辑自相矛盾**（2 条）：continue-on-error:true 吞失败却断言 job_status=failure；断言字符串（marker_v2）无任何步骤能产生
6. **trigger 与 on 不一致**（3 条）：trigger.event=push 但 workflow `on:` 无 push——建议列为规则 3 的强制检查项
=======
2. | 171 | [USE-YAML-01-002](case/USE-YAML-01-002.md) | YAML 缩进错误时报错应指出具体行号与列号 | [负向] 未找到可能导致非成功状态的步骤，单次调度无法证明 !=success |  not true, i can validate it by  phase02/classify-experiment/2026-07-23/batch_validate.py
 
>>>>>>> dd1d825892681f79ef146873c84b4867716159e0
