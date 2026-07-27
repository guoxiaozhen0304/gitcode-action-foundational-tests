用例 ID:   COMP-ACT-01-002
维度标签:   [completeness]
维度:      完备性
优先级:    P2
溯源意图:  INTENT-COMP-027
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/action-development/top-level-fields.md L41-57
母意图:    —
标题:      含连字符 input_id 的 INPUT_ 环境变量命名裁定

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库含本地 action（action.yml 声明 input_id 为 dry-run，脚本枚举并输出所有匹配 INPUT_DRY 的环境变量名与值）

操作步骤:
  1. 编写调用该 action 并以 with 传入 dry-run 参数的 workflow
  2. 手动触发，从日志裁定实际注入的环境变量名

预期结果:
  - 命名转换规则对连字符确定：实际环境变量名（INPUT_DRY-RUN / INPUT_DRY_RUN / 其他）被逐字记录并回写规格缺口

验证点:
  - [正向] 大写化与空格转换与文档一致（回归，复用基底证据）
  - [正向/记录] 含连字符 input_id 的实际环境变量名逐字记录
  - [非功能] 同一 input_id 经 with 传参与环境变量两条路径取值一致

清理:      重置 fixture 仓库
