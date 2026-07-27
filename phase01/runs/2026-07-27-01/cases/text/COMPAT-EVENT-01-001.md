```
用例 ID:   COMPAT-EVENT-01-001
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-037
参照来源:  inputs/github-reference/reference/events.md; inputs/gitcode-spec/syntax-reference/trigger-events.md
母意图:    —（与 INTENT-COMPAT-011/NEW-004 为父集关系：本条覆盖事件本身不存在）
标题:      GitHub 全量事件集中不受支持事件（release 等）的降级方式

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 向仓库提交一个 on 触发事件为 release（GitHub 支持、GitCode 未列入支持清单）的 workflow
  2. 观察保存/解析阶段的平台响应
  3. 若保存成功，制造对应仓库事件并观察是否产生任何运行记录或提示

预期结果:
  - 平台在保存/解析阶段明确报错，报错信息包含事件不受支持的说明与受支持事件清单及迁移建议
  - 不应静默保存成功且永不触发、无任何提示

验证点:
  - [负向] 含不受支持事件的 workflow 不应被静默保存且永无触发记录
  - [正向] 保存/解析期报错包含事件不受支持说明与受支持事件清单
  - [非功能] 报错可理解性：指明为 GitCode 能力差异而非泛化 YAML 错误（eval: llm_assisted）

清理:      重置 fixture 仓库
```
