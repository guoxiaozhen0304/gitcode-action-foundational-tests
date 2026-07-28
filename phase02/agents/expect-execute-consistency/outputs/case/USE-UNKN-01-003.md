# USE-UNKN-01-003
- **标题**: step 标识 id 与 identifier 命名双轨的接受一致性与文档说明
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
验证平台对 `id` 和 `identifier` 两种 step 标识写法的接受情况与行为一致性，检查文档是否说明双名关系。

## 做了什么
workflow 含两个 job：一个使用 `id: producer` 标准写法，另一个使用 `identifier: producer` 样本写法。分别记录平台对两种写法的接受与求值行为。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result | positive | 记录 id 与 identifier 写法的平台接受情况与求值行为 | COVERED | eval: deterministic，校验结果可记录 |
| 2 | documentation | negative | identifier 不在文档字段集合且未说明即不合格 | COVERED | eval: deterministic，字段集合 diff 可程序化 |
