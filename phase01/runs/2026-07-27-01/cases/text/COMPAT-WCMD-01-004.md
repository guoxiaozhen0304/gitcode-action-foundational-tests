```
用例 ID:   COMPAT-WCMD-01-004
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-042
参照来源:  inputs/github-reference/reference/workflow-commands.md; inputs/gitcode-spec/syntax-reference/workflow-commands.md; baseline/case-base-detail.md（TC-247~250 FAIL）
母意图:    —（与 INTENT-COMPAT-NEW-009 互补成完整 workflow-commands 面）
标题:      注解命令 error/warning/notice 的不中断降级行为

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个在步骤中输出 ::error::、::warning::、::notice:: 注解命令且后续仍有正常命令的 workflow
  2. 触发并观察运行状态与日志

预期结果:
  - 注解命令不导致 step 或 workflow 失败（退出码仍由脚本控制），日志保留可见原文
  - 注解命令不被解析出非预期副作用（如截断后续日志）

验证点:
  - [正向] 输出注解命令后 workflow 仍按脚本逻辑成功结束
  - [负向] 注解命令不应截断后续日志或产生非预期副作用
  - [非功能] 与 GitHub 注解 UI 能力的差距进入差异清单

清理:      重置 fixture 仓库
```
