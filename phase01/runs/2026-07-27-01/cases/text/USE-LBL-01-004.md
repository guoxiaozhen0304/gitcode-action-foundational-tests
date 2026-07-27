用例 ID:   USE-LBL-01-004
维度标签:   ['usability']
维度:      usability
优先级:    P0
溯源意图:  INTENT-USE-031
参照来源:  inputs/gitcode-spec/01-quick-start.md
母意图:    —
标题:      quick-start 单标签写法 runs-on ubuntu-latest 的可调度性验证

前置条件:
  - 隔离测试实例可正常调度 workflow

操作步骤:
  1. 按 01-quick-start.md 示例写法，以单标签字符串形式声明 runs-on 并提交 workflow
  2. 观察平台校验与调度结果

预期结果:
  若 quick-start 示例写法合法，workflow 应被接受并成功调度；若平台拒绝，则证明 quick-start 示例本身错误（文档缺陷）

验证点:
  - [正向] 文档示例写法应可被平台接受并运行成功
  - [负向] 平台不应接受一种写法而文档示例给出另一种却不加说明

清理:      无
