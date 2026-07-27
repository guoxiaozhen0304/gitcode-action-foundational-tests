```
用例 ID:   COMPAT-RUNSON-01-003
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-046
参照来源:  inputs/gitcode-spec/writing-pipelines/configure-jobs.md（对象式）; inputs/gitcode-spec/syntax-reference/runner-images-tools.md（数组式）
母意图:    —（与 INTENT-COMPAT-NEW-008 互补；runs-on 主题簇成员，关联 INTENT-COMP-029）
标题:      自托管 runs-on 对象式写法（type/group/labels）的实测仲裁

前置条件:
  - 实例已注册带 linux、x64 标签的自托管 Runner

操作步骤:
  1. 提交一个按 configure-jobs.md 对象式写法声明自托管 runs-on 的 workflow
  2. 观察解析与调度结果

预期结果:
  - 对象式写法得到确定响应：在已注册自托管 Runner 上调度成功，或解析期明确报错
  - 不被接受时不应表现为 job 无限排队无提示

验证点:
  - [正向] 对象式写法的调度或报错结局确定
  - [负向] 不应无限 queued 无提示

清理:      重置 fixture 仓库
```
