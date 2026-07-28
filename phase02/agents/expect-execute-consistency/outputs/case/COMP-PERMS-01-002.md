# COMP-PERMS-01-002
- **标题**: 声明 repository write 后 TOKEN 可推送代码
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
permissions: repository: write 时 ATOMGIT_TOKEN 可成功推送代码。

## 做了什么
1. permissions: repository: write
2. step `Push code`：git config → echo "change" >> README.md → git add → git commit → git push 使用 ATOMGIT_TOKEN

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | git push 使用真实 ATOMGIT_TOKEN，成功则 step 通过 |
