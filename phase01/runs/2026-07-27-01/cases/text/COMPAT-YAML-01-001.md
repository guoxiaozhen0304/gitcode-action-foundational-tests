```
用例 ID:   COMPAT-YAML-01-001
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P2
溯源意图:  INTENT-COMPAT-049
参照来源:  inputs/github-reference/reference/workflow-syntax.md; inputs/gitcode-spec/writing-pipelines/workflow-file-location-structure.md
母意图:    —
标题:      YAML 1.1 on 键布尔陷阱与 env 中 yes/no/on/off 字面量的解析行为

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 以标准写法提交一个 on 为 push 的 workflow，并在 env 中放入未加引号的 on 字面值变量
  2. 通过 push 触发，确认 workflow 被正确识别为触发配置并运行
  3. 观察 env 变量的取值类型行为

预期结果:
  - GitCode 与 GitHub 一致，对顶层 on 键做显式兼容处理，workflow 正常触发
  - env 中未加引号的 on/off 字面值取值类型行为确定且与 GitHub 对齐

验证点:
  - [正向] 标准 on 写法被正确识别为触发配置而非布尔键
  - [负向] workflow 不应因 on 键被解析为布尔而静默不触发且无告警
  - [正向] env 中 on 字面值的取值类型行为确定

清理:      重置 fixture 仓库
```
