# USE-ACT-01-003
- **标题**: 官方短名 Action 清单与 actions-market 插件目录的映射一致性
- **维度**: usability
- **评级**: 断言一致

## 想测什么
文档短名集合与市场目录插件名集合应建立映射，不一致处需文档明示。

## 做了什么
workflow: null。纯文档验证用例，断言指向 documentation。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | eval:deterministic | COVERED | 文档-only 用例，无 workflow 步骤；断言直接对标文档内容做确定性 diff |
