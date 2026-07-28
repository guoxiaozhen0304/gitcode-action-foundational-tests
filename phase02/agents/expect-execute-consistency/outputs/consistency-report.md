# 断言-步骤一致性报告

**日期**: 2026-07-28（优化后重评）
**数据源**: [phase01/runs/2026-07-27-01/cases/](https://github.com/opensourceways/gitcode-action-foundational-tests/tree/main/phase01/runs/2026-07-27-01/cases/)
**用例总数**: 498

---

## 0. 本轮变化（2026-07-28 优化重评）

针对上一轮的 13 个完全不符 + 73 个部分不符用例（共 86 个）执行了用例优化与复核：

| 动作 | 数量 | 说明 |
|------|:---:|------|
| 修复 YAML | 78 | 原地修改 `phase01/runs/2026-07-27-01/cases/yaml/` |
| 跳过（已符合最优形态） | 8 | REL-MATRIX-01-026、COMP-CALL-01-001（前一轮已修复）；SEC-COMM-01-001/003、USE-MASK-01-001、USE-OS-01-001、USE-YAML-01-001/002（仅含本质 llm 断言） |
| 转为断言一致 | 44 | YAML 已复制到 [outputs/accessable/](https://github.com/opensourceways/gitcode-action-foundational-tests/tree/main/phase02/agents/expect-execute-consistency/outputs/accessable/) |
| 仍为部分不符 | 42 | 均含本质不可确定化的 llm_assisted 断言（文档内容、UI 渲染、报错文案质量、平台行为探针），已在 YAML 中注释说明 |
| 完全不符 | 0 | 全部消除 |

修复手法分类：裸 echo 加 `${{ }}` 表达式/真实校验（约 30 例）、llm 断言转确定性 must_contain/must_not_contain（约 25 例）、补规格缺失断言（约 15 例）、补真实校验步骤（md5 对账/git 比对/curl 状态码判定等，约 12 例）、修正 workflow 结构（job 级 workflow_call、删除必败的 v1 步骤、修复 curl 断行等，6 例）、抽象断言显式化 + 注释（约 10 例）。

全部 78 个修改文件通过 YAML 语法校验与 GitCode 平台规则 lint（on: map 格式、job/step name 必填及非法字符、禁用字段等，故意违规的负向用例按白名单豁免）。

---

## 1. 总览

| 维度 | 断言一致 | 部分不符 | 完全不符 |
|------|:---:|:---:|:---:|
| 完备性 | 109 | 1 | 0 |
| 兼容性 | 131 | 6 | 0 |
| 可靠性 | 99 | 6 | 0 |
| 安全性 | 57 | 10 | 0 |
| 易用性（含跨维度） | 60 | 19 | 0 |
| **合计** | **456** | **42** | **0** |

> 上一轮的"易用性/兼容性"、"易用性/安全性"、"易用性/可靠性"三行合并入"易用性"行。

---

## 2. 完全不符 (0 例)

已全部消除。原 13 个完全不符用例中：

- 转断言一致 (7)：COMPAT-ISOLATE-01-001/002、REL-MATRIX-01-026、SEC-ARTF-01-003 的确定性部分、SEC-AUDIT-01-001、COMP-CALL-01-001、REL-BIGRUNNER-01-066 的确定性部分——其中 COMPAT-ISOLATE x2、SEC-AUDIT-01-001、COMP-CALL-01-001、REL-MATRIX-01-026 共 5 例整体转一致；REL-BIGRUNNER-01-066、SEC-ARTF-01-003、COMPAT-LIMIT-01-001/002、COMPAT-MATRIX-01-003/004、SEC-OIDC-01-001、COMP-CALL-01-002 因保留本质 llm 断言升为部分不符。

## 3. 部分不符 (42 例)

均含本质不可确定化的 llm_assisted 断言（已在 YAML 注释说明原因）；可执行部分已全部真实化、可确定化部分已全部转为确定性断言。

**平台行为探针（被测目标本身是未知数）**：
- [COMPAT-LIMIT-01-001](case/COMPAT-LIMIT-01-001.md): 单次推送多个 tag 的事件生成上限行为
- [COMPAT-LIMIT-01-002](case/COMPAT-LIMIT-01-002.md): workflow_dispatch 输入数量上限与非默认分支可用性
- [COMPAT-MATRIX-01-003](case/COMPAT-MATRIX-01-003.md): matrix 三维展开不被支持时的差异
- [COMPAT-MATRIX-01-004](case/COMPAT-MATRIX-01-004.md): matrix include 无基础变量不被支持时的差异
- [COMPAT-CACHE-01-002](case/COMPAT-CACHE-01-002.md): cache 行为等价性——fork PR 写隔离
- [COMPAT-EXPR-01-002](case/COMPAT-EXPR-01-002.md): success() 函数的处理行为差异

**平台插件/审计内容判读**：
- [SEC-ARTF-01-003](case/SEC-ARTF-01-003.md): 宽通配打包含敏感文件名的 artifact 警示行为
- [SEC-COMM-01-001](case/SEC-COMM-01-001.md): issue_comment/pull_request_comment 触发关键字过滤必须不可被绕过
- [SEC-COMM-01-002](case/SEC-COMM-01-002.md): 引用/反讽/代码块内嵌指令文本绝不应造成预期外触发
- [SEC-COMM-01-003](case/SEC-COMM-01-003.md): 变形伪装评论不得绕过 comments 过滤语义
- [SEC-OIDC-01-001](case/SEC-OIDC-01-001.md): OIDC/短时凭据支持标注与替代方案
- [SEC-ORG-01-001](case/SEC-ORG-01-001.md): 可见范围外仓库的 workflow 绝不应读到组织级 secret 原值

**动态值判定（编码/子串形式依赖 secret 原值）**：
- [SEC-MASK-01-003](case/SEC-MASK-01-003.md): Secret 日志脱敏不可通过 base64 编码绕过
- [SEC-MASK-01-004](case/SEC-MASK-01-004.md): Secret 日志脱敏不可通过字符串拼接或插值绕过
- [SEC-MASK-01-006](case/SEC-MASK-01-006.md): Secret 日志脱敏不可通过分片输出绕过

**实测记录型指标（无数值阈值）**：
- [REL-CACHE-01-047](case/REL-CACHE-01-047.md): cache 容量上限探测
- [REL-CACHE-01-048](case/REL-CACHE-01-048.md): cache 同 key 并发写一致性
- [REL-MATRIX-01-041](case/REL-MATRIX-01-041.md): matrix 组合数越界
- [REL-BIGRUNNER-01-066](case/REL-BIGRUNNER-01-066.md): 大规格资源调度稳定性（failure_attribution 归因判读）
- [REL-VCJOB-01-002](case/REL-VCJOB-01-002.md): 大规模 vcjob 并发提交（级联失败归因判读）

**UI/前端观测**：
- [REL-LOGPERF-01-051](case/REL-LOGPERF-01-051.md): 日志加载性能（UI 卡死观测）
- [USE-LOG-01-001](case/USE-LOG-01-001.md): 多 step 日志按时间线组织且边界清晰
- [USE-MD-01-001](case/USE-MD-01-001.md): ATOMGIT_STEP_SUMMARY 写入的 Markdown 正确渲染为 HTML
- [USE-SEARCH-01-001](case/USE-SEARCH-01-001.md): 日志搜索与下载功能可用且交互流畅

**文档内容检查**：
- [USE-MASK-01-001](case/USE-MASK-01-001.md): secret 脱敏文档描述与实际行为一致并给出缓解建议
- [USE-ONBD-01-001](case/USE-ONBD-01-001.md): 新手快速开始路径端到端可复刻走查
- [USE-OS-01-001](case/USE-OS-01-001.md): runner.os 返回值与文档声明的平台支持一致

**报错文案质量（关键内容已确定性覆盖，文案质量保留 llm）**：
- [COMP-CALL-01-002](case/COMP-CALL-01-002.md): 3 层 workflow_call 嵌套应被拒绝
- [USE-EXPR-01-001](case/USE-EXPR-01-001.md): 引用不存在的上下文属性时报错应包含原始表达式与错误类型
- [USE-EXPR-01-002](case/USE-EXPR-01-002.md): 调用未知函数时报错应提示函数名错误与修正方向
- [USE-INPT-01-002](case/USE-INPT-01-002.md): 使用 boolean 类型 input 时报错应提示仅支持 string
- [USE-LBL-01-001](case/USE-LBL-01-001.md): runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表
- [USE-NEST-01-001](case/USE-NEST-01-001.md): workflow_call 嵌套 3 层时报错应明确提示上限为 2 层
- [USE-PERM-01-002](case/USE-PERM-01-002.md): 使用 GitHub 权限域命名时报错应给出 GitCode 对照表
- [USE-RUN-01-002](case/USE-RUN-01-002.md): 使用单标签 ubuntu-latest 时报错应给出三段式格式指引
- [USE-SECNAME-01-001](case/USE-SECNAME-01-001.md): Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误
- [USE-SECNAME-01-002](case/USE-SECNAME-01-002.md): Secret 名称以数字开头时应给出命名规则错误
- [USE-STAT-01-002](case/USE-STAT-01-002.md): 使用 success() 带括号时报错应提示 GitCode 括号差异
- [USE-TYPE-01-002](case/USE-TYPE-01-002.md): 使用 GitHub types 命名 opened/synchronize 时应给出可理解提示
- [USE-YAML-01-001](case/USE-YAML-01-001.md): 缺少必填字段 on 时报错应指出具体字段名与位置
- [USE-YAML-01-002](case/USE-YAML-01-002.md): YAML 缩进错误时报错应指出具体行号与列号
- [SEC-NAME-01-003](case/SEC-NAME-01-003.md): 可遮蔽系统变量的 secret 命名创建时必须被拒

## 4. 断言一致 (456 例)

共 456 例断言一致的用例 YAML 已复制到 [outputs/accessable/](https://github.com/opensourceways/gitcode-action-foundational-tests/tree/main/phase02/agents/expect-execute-consistency/outputs/accessable/)，可直接 dispatch（其中 44 例为本轮优化后新增）。

## 5. 逐用例详情

每个用例的详细分析见 [outputs/case/](https://github.com/opensourceways/gitcode-action-foundational-tests/tree/main/phase02/agents/expect-execute-consistency/outputs/case/)。本轮复核的 86 个用例详情均已更新为重评结论（含修复内容说明）。
