# USE-DOC-01-006
- **标题**: syntax-reference 章节编号连续性扫描
- **维度**: usability
- **评级**: 断言一致

## 想测什么
syntax-reference 下各页二级标题编号应连续；跳号处需有沿革说明。

## 做了什么
workflow: null。纯文档验证用例，断言指向 documentation 确定性正则扫描。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | eval:deterministic | COVERED | 正则扫描二级编号连续性，跳号且无说明即不合格 |
