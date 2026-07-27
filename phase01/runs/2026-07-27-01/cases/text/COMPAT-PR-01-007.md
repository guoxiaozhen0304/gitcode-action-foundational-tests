```
用例 ID:   COMPAT-PR-01-007
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-038
参照来源:  inputs/github-reference/reference/events.md; inputs/gitcode-spec/syntax-reference/trigger-events.md
母意图:    —（与 INTENT-COMPAT-011 互补：011 为同名 type 命名差异，本条为 GitHub 有而 GitCode 无的 type）
标题:      pull_request 不支持的 activity type（labeled）不应静默退化

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 pull_request 触发且 types 含 labeled（GitCode 合法值仅 open/reopen/update/merge）的 workflow
  2. 观察保存/解析阶段响应
  3. 若被接受，对 PR 执行非 labeled 的普通活动（如提交更新），观察是否触发运行

预期结果:
  - 平台在解析阶段明确报错并列出合法 types 取值
  - 不应静默忽略 labeled 退化为所有 PR 活动均触发，也不应静默接受后永不触发

验证点:
  - [负向] types 含 labeled 不应被静默忽略而退化为全量触发
  - [正向] 解析期报错列出 GitCode 合法的 4 种 types（open/reopen/update/merge）

清理:      重置 fixture 仓库
```
