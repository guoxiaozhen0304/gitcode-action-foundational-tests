```
用例 ID:   COMPAT-ACTIONDEV-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-048
参照来源:  inputs/gitcode-spec/action-development/action-yml-metadata-syntax.md; inputs/gitcode-spec/COMPAT-NOTES.md §10; inputs/github-reference（action 运行时类型）
母意图:    —（与 INTENT-COMPAT-NEW-010 互补成完整 action 元数据面）
标题:      action 运行时 runs.using 类型覆盖（node16/composite/docker/node20）探测

前置条件:
  - fixture 仓库内置四类本地 action：runs.using 分别为 node16、composite、docker、node20

操作步骤:
  1. 提交一个依次引用四类本地 action 的 workflow
  2. 观察各 action 在加载阶段与运行阶段的响应

预期结果:
  - GitCode 支持的 runs.using 取值全集得到确定结论
  - 不支持的类型在 action 加载阶段给出明确报错与替代指引，而非运行期模糊失败

验证点:
  - [正向] runs.using node16 的本地 action 正常执行
  - [正向] composite/docker/node20 类型得到确定响应（支持执行或加载期明确报错）
  - [负向] 不支持的 using 类型不应表现为运行期模糊失败
  - [非功能] 支持的运行时清单进入差异文档

清理:      重置 fixture 仓库
```
