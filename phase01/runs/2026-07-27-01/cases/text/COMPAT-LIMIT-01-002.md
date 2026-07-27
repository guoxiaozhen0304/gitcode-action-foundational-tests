```
用例 ID:   COMPAT-LIMIT-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P2
溯源意图:  INTENT-COMPAT-052
参照来源:  inputs/github-reference/reference/events.md（dispatch 25 inputs/65535 chars、默认分支要求）; inputs/gitcode-spec/syntax-reference/trigger-events.md
母意图:    —（变体自 COMPAT-LIMIT-01-001：workflow_dispatch 输入上限面）
标题:      workflow_dispatch 输入数量上限（GitHub 25 个）与非默认分支可用性

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个声明 26 个 inputs 的 workflow_dispatch workflow
  2. 观察保存期响应（明确报错或截断）
  3. 在非默认分支上尝试触发 workflow_dispatch，确认可用性结论

预期结果:
  - 保存期对超限 inputs 给出明确报错或确定的截断行为，而非静默接受
  - 非默认分支上 dispatch 的可用性结论确定（与 GitHub 必须默认分支的要求比对）

验证点:
  - [正向] 26 个 inputs 的保存期行为确定（报错或截断）
  - [负向] 超限不应静默接受后触发时异常
  - [正向] 非默认分支 dispatch 可用性结论确定

清理:      重置 fixture 仓库
```
