```
用例 ID:   COMPAT-PR-01-009
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-039
参照来源:  inputs/github-reference/reference/events.md; inputs/gitcode-spec/syntax-reference/context.md; inputs/gitcode-spec/syntax-reference/trigger-events.md
母意图:    —（与 INTENT-COMP-033 同主题两面，共享 PR 夹具与证据链；与 INTENT-COMPAT-032 正交）
标题:      pull_request 触发时 atomgit.sha/ref 的代码版本语义（对齐 GitHub merge commit 模型）

前置条件:
  - fixture 仓库存在一个对 main 的开放 PR，head sha 与 base sha 已知

操作步骤:
  1. 在 pull_request 触发的 workflow 中输出 atomgit.sha、atomgit.ref 及对应环境变量
  2. 检出代码后记录实际检出的提交 SHA
  3. 将观测值与 PR head sha、base sha、试合并 sha 逐一比对，定位 GitCode 的取值语义

预期结果:
  - atomgit.sha/ref 的确切语义得到确定结论；与 GitHub merge commit 模型不一致时按重大差异文档化并回写 Parity Matrix
  - checkout 检出的代码版本与 atomgit.sha 指向的版本一致

验证点:
  - [正向] 观测 atomgit.sha / atomgit.ref 实际取值并与 head/base/试合并 sha 比对定位语义
  - [负向] 不应出现 checkout 检出版本与 atomgit.sha 指向版本不一致
  - [非功能] 语义确认后回写 Parity Matrix 作为该点 oracle

清理:      重置 fixture 仓库
```
