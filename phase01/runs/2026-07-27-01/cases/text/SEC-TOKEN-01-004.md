用例 ID:   SEC-TOKEN-01-004
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-037
参照来源:  inputs/security-knowledge/issues.md §2; inputs/security-knowledge/github-actions-security-series.md 总结#6
母意图:    —
标题:      残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权

前置条件:
  - fixture 仓库具备 artifact 上传/下载能力
  - 已存在一个历史 run（run A），其 artifact 中意外残留了当次 ATOMGIT_TOKEN 值（由 harness 预置，模拟意外残留场景）

操作步骤:
  1. 触发新 run（run B），job 下载 run A 的 artifact，提取残留 token
  2. 持残留 token 调用只读 API，记录响应码
  3. 同 job 内用 run B 自身的 ATOMGIT_TOKEN 执行一次权限内只读操作

预期结果:
  - 残留 token 在 run B 中调用 API 返回 401/403
  - run B 自身 token 正常工作

验证点:
  - [正向] 新 run 自身的 ATOMGIT_TOKEN 在其权限范围内可用
  - [负向] 残留于 artifact 的旧 token 绝不应在新 run 中通过鉴权

清理:      重置 fixture 仓库
