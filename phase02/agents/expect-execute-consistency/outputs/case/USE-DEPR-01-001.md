# USE-DEPR-01-001
- **标题**: 使用 ATOMGIT_OUTPUT 文件协议时正常生效
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
`echo key=val >> $ATOMGIT_OUTPUT` 输出参数正确设置，下游步骤可引用。

## 做了什么
workflow 中 step 写 `echo "mykey=myvalue" >> "$ATOMGIT_OUTPUT"`，下游 `${{ steps.out.outputs.mykey }}` 读取。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: val=myvalue | COVERED | `${{ steps.out.outputs.mykey }}` 真实表达式读取 output，验证值传递正确 |

