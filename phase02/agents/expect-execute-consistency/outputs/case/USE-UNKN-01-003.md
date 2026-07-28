# USE-UNKN-01-003  - **标题**: step 标识 id 与 identifier 命名双轨的接受一致性与文档说明   - **维度**: usability   - **评级**: 断言一致

## 想测什么

若两种写法等价，文档应显式声明；若只接受其一，平台应对另一种给出明确报错而非静默忽略

## 做了什么

- 1. 分别用文档字段名与样本字段名声明 step 标识并提交
- 2. 记录平台对两种写法的接受与行为是否一致
- 3. 检查文档是否说明双名关系

- - [正向] 记录平台对两种写法的接受情况与行为一致性
- - [负向] 两种写法并存且行为不同而文档未说明差异即不合格
- - [非功能] 平台对废弃名应给出 deprecation 警告而非静默接受

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | validation_result | positive | eval=deterministic | COVERED | validation_result+deterministic: 两种step标识写法接受度→可确定性验证; $ATOMGIT_OUTPUT→真实平台功能 |
| 2 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 文档字段集合diff确定性检查 |
