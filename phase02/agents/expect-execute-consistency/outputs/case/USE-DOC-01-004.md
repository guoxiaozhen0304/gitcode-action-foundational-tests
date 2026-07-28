# USE-DOC-01-004
- **标题**: workflow-commands 多行输出示例漏写重定向照抄得空输出
- **维度**: usability
- **评级**: 断言一致

## 想测什么
照抄文档多行输出示例（不写重定向）应得到空输出，实证示例缺陷。

## 做了什么
step1 按文档示例输出 multiline 标记（无 ATOMGIT_OUTPUT 重定向），step2 `echo "got=[${{ steps.producer.outputs.multiline }}]"` 读取结果。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval:deterministic | COVERED | step2 显式 echo got=[...]，若为空则实证示例漏写重定向 |
| 2 | documentation | negative | eval:deterministic | COVERED | 文档缺陷检查 |
