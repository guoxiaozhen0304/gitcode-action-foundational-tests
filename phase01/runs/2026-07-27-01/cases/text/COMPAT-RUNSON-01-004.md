```
用例 ID:   COMPAT-RUNSON-01-004
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-046
参照来源:  inputs/gitcode-spec/syntax-reference/runner-images-tools.md（数组式 + 子集匹配规则）; inputs/gitcode-spec/writing-pipelines/configure-jobs.md（对象式）
母意图:    —（变体自 COMPAT-RUNSON-01-003：数组式写法仲裁；两案结论合并裁定规格矛盾）
标题:      自托管 runs-on 数组式写法（标签列表子集匹配）的实测仲裁

前置条件:
  - 实例已注册带 linux、x64 标签的自托管 Runner

操作步骤:
  1. 提交一个按 runner-images-tools.md 数组式写法声明自托管 runs-on 的 workflow
  2. 观察解析与调度结果，并与对象式用例结论合并比对匹配语义

预期结果:
  - 数组式写法得到确定响应（调度成功或解析期明确报错）
  - 两种写法的匹配语义（子集规则、分组对应关系）结论合并后统一文档

验证点:
  - [正向] 数组式写法的调度或报错结局确定
  - [负向] 不应无限 queued 无提示
  - [非功能] 两种写法匹配语义是否等价得到结论并统一文档

清理:      重置 fixture 仓库
```
