# USE-LBL-01-003  - **标题**: runs-on 标签写法跨文档形态扫描（同一字段不应出现三种以上互斥形态）   - **维度**: usability   - **评级**: 断言一致

## 想测什么

同一字段在全集文档中形态应统一，或在 Runner 文档一处集中声明等价关系与推荐写法

## 做了什么

- 1. 对 gitcode-spec 全文检索 runs-on: 的所有示例写法
- 2. 归纳形态类别（单标签字符串 / 数组三段式 / 花括号三段式 / 自托管对象式）
- 3. 检查是否存在任一处集中说明各形态等价关系或推荐写法

- - [负向] 同一字段在 3 个以上官方页面给出互不相同形态且无任何一处说明等价关系，即为缺陷
- - [非功能] 选择 Runner 标签页应列出全部合法形态并标注推荐项

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 文档形态归约确定性计数 |
| 2 | documentation | nonfunctional | eval=deterministic | COVERED | documentation+deterministic: 推荐写法清单确定性检查 |
