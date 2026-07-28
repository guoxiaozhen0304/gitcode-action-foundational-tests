# USE-DEPR-01-001
- **标题**: 使用 ATOMGIT_OUTPUT 文件协议时正常生效
- **维度**: usability
- **评级**: 断言一致

## 想测什么
`echo key=val >> $ATOMGIT_OUTPUT` 后下游步骤可通过 `steps.*.outputs.key` 获取值。

## 做了什么
step1 `echo "mykey=myvalue" >> "$ATOMGIT_OUTPUT"`（设置 output），step2 `echo "val=${{ steps.out.outputs.mykey }}"`（读取 output）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains:"val=myvalue" | COVERED | step2 显式 echo 期望值，精确匹配 |
