# COMP-ATOMGIT-01-049
- **标题**: atomgit 边界格式校验
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
atomgit.sha 长度 40，atomgit.ref 以 refs/ 开头，atomgit.ref_name 不含 refs/ 前缀，atomgit.actor 非空。

## 做了什么
1. step `Check formats`：`echo "SHA_LEN=${#ATOMGIT_SHA}"`、`echo "REF_PREFIX=${ATOMGIT_REF%%/*}"`、`echo "REF_NAME_NO_PREFIX=${ATOMGIT_REF_NAME#refs/}"`、`echo "ACTOR_LEN=${#ATOMGIT_ACTOR}"`
   变量 ATOMGIT_SHA、ATOMGIT_REF 等为 Runner 标准注入的环境变量，与 `${{ atomgit.sha }}` 等效

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: SHA_LEN=40 | COVERED | ${#ATOMGIT_SHA} 计算 Runner 注入的 SHA 长度 |
| 2 | run_logs | positive | must_contain: REF_PREFIX=refs | COVERED | ${ATOMGIT_REF%%/*} 提取 refs/ 前缀 |
| 3 | run_logs | positive | must_contain: REF_NAME_NO_PREFIX= | COVERED | ${ATOMGIT_REF_NAME#refs/} 去除 refs/ 前缀 |
| 4 | run_logs | negative | must_not_contain: REF_NAME_NO_PREFIX=refs/ | COVERED | ref_name 经去除 refs/ 后不应仍含该前缀 |
| 5 | run_logs | positive | must_contain: ACTOR_LEN= | COVERED | ${#ATOMGIT_ACTOR} 输出 actor 长度，非空则 > 0 |
