```
用例 ID:   COMPAT-ENV-01-004
维度标签:   [compatibility, security]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-043
参照来源:  inputs/github-reference/reference/workflow-commands.md; inputs/github-reference/reference/variables.md; inputs/gitcode-spec/syntax-reference/workflow-commands.md
母意图:    —（与 INTENT-COMPAT-017 互补：017 为变量清单有无，本条为能否被覆写；安全面邻接 RISK-SEC-02）
标题:      ATOMGIT_ENV 覆写系统默认变量的防护（对齐 GitHub 同名禁止）

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 workflow：步骤一经环境文件尝试覆写系统默认变量（如工作区路径），同时写入一个普通自定义变量
  2. 步骤二读取两类变量的实际值
  3. 观察覆写尝试是否被拒绝或在日志留下警告痕迹

预期结果:
  - 与 GitHub 对齐：经环境文件写入 ATOMGIT_ 前缀系统默认变量被拒绝或忽略，后续步骤读到的不是被污染值
  - 覆写尝试在日志中产生可观测的警告或拒绝痕迹
  - 普通自定义变量写入不受影响

验证点:
  - [负向] 后续步骤读到的工作区变量不应是被污染值
  - [正向] 覆写尝试应有警告或拒绝痕迹而非静默成功
  - [正向] 普通自定义变量经环境文件正常传递

清理:      重置 fixture 仓库
```
