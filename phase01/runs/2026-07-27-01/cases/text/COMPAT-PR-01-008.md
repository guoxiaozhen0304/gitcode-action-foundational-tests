```
用例 ID:   COMPAT-PR-01-008
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-038
参照来源:  inputs/github-reference/reference/events.md; inputs/gitcode-spec/syntax-reference/trigger-events.md
母意图:    —（变体自 COMPAT-PR-01-007：探测 ready_for_review 的静默不触发形态）
标题:      pull_request 不支持的 activity type（ready_for_review）不应静默不触发

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 pull_request 触发且 types 含 ready_for_review 的 workflow
  2. 观察保存/解析阶段响应
  3. 若被接受，将 draft PR 转为正式 PR，观察是否触发运行及有无任何提示

预期结果:
  - 平台在解析阶段明确报错并列出合法 types 取值
  - 不应静默接受后任何事件都不触发且无任何提示

验证点:
  - [负向] types 含 ready_for_review 不应被静默接受后永不触发且无提示
  - [正向] 解析期报错列出 GitCode 合法的 4 种 types

清理:      重置 fixture 仓库
```
