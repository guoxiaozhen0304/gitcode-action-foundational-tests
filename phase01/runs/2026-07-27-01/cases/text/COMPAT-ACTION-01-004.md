```
用例 ID:   COMPAT-ACTION-01-004
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-045
参照来源:  inputs/gitcode-spec/writing-pipelines/using-actions.md（docker/build-push-action@v6 示例）
母意图:    —（变体自 COMPAT-ACTION-01-003：官方文档自带示例的可用性仲裁；负向探测，预期报错对象）
标题:      官方文档示例 docker/build-push-action@v6 引用的可用性仲裁

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个按官方文档示例使用 docker/build-push-action@v6 的 workflow
  2. 观察保存/解析/运行各阶段响应

预期结果:
  - 官方文档自带示例必须可用，或确认不可用后文档勘误
  - 文档不得展示实际不可用的引用写法而不加说明

验证点:
  - [正向] 文档示例引用得到确定可用性结论
  - [负向] 不可用时文档不应继续无说明展示该示例

清理:      重置 fixture 仓库
```
