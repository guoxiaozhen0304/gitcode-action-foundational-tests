```
用例 ID:   COMPAT-ACTION-01-003
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-045
参照来源:  inputs/gitcode-spec/writing-pipelines/using-actions.md; testing-focus.md §7/§11
母意图:    —（与 INTENT-COMPAT-024 互补：本条为 GitHub 风格全名引用能否解析的前置问题；本用例为负向探测，GitHub 全名引用属预期报错对象）
标题:      GitHub 风格 action 引用 actions/checkout@v4 的解析域探测

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个步骤中使用 GitHub 风格全名引用 actions/checkout@v4 的 workflow
  2. 观察保存/解析/调度各阶段响应

预期结果:
  - 解析结果二选一且明确：成功执行（存在代理/镜像机制），或保存期明确报错并提示官方短名替代
  - 不应表现为 job 无限排队或运行到该步骤才报模糊错误

验证点:
  - [正向] 解析结果明确（成功执行或保存期明确报错）
  - [负向] 不可解析时不应无限 queued 或运行期模糊失败
  - [非功能] 报错或文档给出 GitHub 引用到 GitCode 短名的映射指引

清理:      重置 fixture 仓库
```
