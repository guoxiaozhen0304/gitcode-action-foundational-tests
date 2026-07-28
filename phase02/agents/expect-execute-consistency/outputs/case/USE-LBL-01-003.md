# USE-LBL-01-003
- **标题**: runs-on 标签写法跨文档形态扫描（同一字段不应出现三种以上互斥形态）
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
对 gitcode-spec 全文扫描 runs-on 示例写法，归纳形态类别，检查文档是否集中说明各形态的等价关系与推荐写法。

## 做了什么
纯文档检查用例（workflow: null）。grep 文档中全部 runs-on 写法，归纳形态数，检查 selecting-runner-labels.md 是否列出全部合法形态并标注推荐项。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | 形态数 > 2 且未集中说明等价关系即不合格 | COVERED | eval: deterministic，grep + 形态归纳可程序化 |
| 2 | documentation | nonfunctional | selecting-runner-labels.md 应列出全部合法形态并标注推荐 | COVERED | eval: deterministic，文档内容检查可程序化 |
