```
用例 ID:   COMPAT-ENV-01-005
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-044
参照来源:  inputs/github-reference/reference/variables.md; inputs/gitcode-spec/syntax-reference/variables.md; baseline/case-base-detail.md（TC-441/442 FAIL）
母意图:    —（与 INTENT-COMPAT-018/019 互补：上下文对象面 vs 环境变量面）
标题:      RUNNER_* 系列环境变量在 GitCode Runner 上的注入情况探测

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个逐一输出 RUNNER_OS、RUNNER_ARCH、RUNNER_NAME、RUNNER_TEMP、RUNNER_TOOL_CACHE、RUNNER_ENVIRONMENT 的 workflow
  2. 触发并逐字记录各变量取值

预期结果:
  - 各 RUNNER_* 变量的注入情况得到逐字记录；不注入的列入差异清单并给出 runner 上下文替代写法对照
  - 不应出现文档未声明的部分注入（半套兼容）

验证点:
  - [正向] 六个 RUNNER_* 变量取值逐一确定并记录
  - [负向] 不应出现部分有值部分为空且文档未声明的不一致
  - [非功能] 缺失变量清单进入迁移对照表

清理:      重置 fixture 仓库
```
