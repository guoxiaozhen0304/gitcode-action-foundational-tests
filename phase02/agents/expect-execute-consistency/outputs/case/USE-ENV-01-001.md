# USE-ENV-01-001
- **标题**: 使用 ATOMGIT_SHA 环境变量时正常取值
- **维度**: usability
- **评级**: 断言一致

## 想测什么
`$ATOMGIT_SHA` 环境变量正常输出当前 commit SHA。

## 做了什么
step `echo "sha=$ATOMGIT_SHA"` 显式输出 SHA 值。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains:"sha=" | COVERED | step 显式 echo sha=$ATOMGIT_SHA，精确匹配前缀 |
