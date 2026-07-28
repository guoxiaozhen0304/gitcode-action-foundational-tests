# USE-DOC-01-004
- **标题**: workflow-commands 多行输出示例漏写重定向照抄得空输出
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
照抄 workflow-commands.md 多行输出示例（不写重定向）应得到空输出，实证示例缺陷。

## 做了什么
workflow 中照抄文档示例：`echo "multiline<<EOF" ... echo "EOF"`（不写 `>> $ATOMGIT_OUTPUT`）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | got=[] 即实证示例漏写重定向 | COVERED | `${{ steps.producer.outputs.multiline }}` 真实表达式读取，若为空则证明缺陷 |
| 2 | documentation | negative | 文档示例缺少重定向行且未标注即不合格 | COVERED | 文档扫描确定性判定 |

