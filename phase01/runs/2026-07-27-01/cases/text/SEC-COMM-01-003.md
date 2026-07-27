用例 ID:   SEC-COMM-01-003
维度标签:   [security, compatibility]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-042
参照来源:  inputs/gitcode-spec/syntax-reference/trigger-events.md §1.5; inputs/security-knowledge/github-actions-security-series.md Part 4
母意图:    INTENT-SEC-026
标题:      变形伪装评论（大小写/多余空白/markdown 包裹）不得绕过 comments 过滤语义

前置条件:
  - fixture 仓库配置 pull_request_comment workflow，comments 过滤配置意图为「精确指令匹配」
  - 存在一个 PR 供评论

操作步骤:
  1. 依次发表变形评论：大小写变形、指令中插入多余空白、以 markdown 格式包裹指令文本
  2. 观察各变形评论的触发结果与配置意图是否一致
  3. 检索文档中对 comments 匹配语义（子串/全串/锚定）的说明

预期结果:
  - 变形评论的触发结果与配置意图一致，无预期外触发、无预期内漏触发
  - 匹配语义有文档说明，误触发面有警示

验证点:
  - [正向] 未变形的精确指令评论正常触发
  - [负向] 绕过过滤语义的伪装评论绝不应触发与配置意图不一致的运行
  - [非功能] 匹配语义与误触发面有文档化说明（llm 辅助判定）

清理:      重置 fixture 仓库
