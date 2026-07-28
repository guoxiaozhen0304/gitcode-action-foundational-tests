# USE-EXPR-01-003  - **标题**: expressions 函数表语法标记可解析性与状态关键字术语区分   - **维度**: usability   - **评级**: 断言一致

## 想测什么

函数表语法示意应可粘贴即用；状态关键字应与真正函数明确分区

## 做了什么

- 1. 抽取 expressions.md 函数表语法列每行示意字符串
- 2. 检查是否存在无法通过表达式 parser 的字符串（如多余括号）
- 3. 检查文档是否把无括号状态关键字与函数混称而不加区分

- - [负向] 语法列含多余括号等无法解析的字符串即不合格
- - [负向] 文档把 success 等无括号关键字称为函数且不加区别说明即不合格
- - [非功能] 状态关键字与函数应在章节或视觉上有明确区分

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 函数表语法列确定性扫描 |
| 2 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 状态关键字分类确定性检查 |
