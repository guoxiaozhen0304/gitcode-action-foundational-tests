# COMP-ATOMGIT-01-049

- **标题**: atomgit 边界格式校验
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `ATOMGIT_SHA` 长度为 40、`ATOMGIT_REF` 以 `refs` 开头、`ATOMGIT_REF_NAME` 不含 `refs/` 前缀、`ATOMGIT_ACTOR` 非空。

## 做了什么
单个 step 使用 bash 内置语法（`${#VAR}`、`%%`、`#refs/`）操作运行时注入的 `$ATOMGIT_*` 环境变量，echo 输出校验结果。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: SHA_LEN=40 | COVERED | `${#ATOMGIT_SHA}` 计算平台注入变量长度后输出 |
| 2 | run_logs | positive | must_contain: REF_PREFIX=refs | COVERED | `${ATOMGIT_REF%%/*}` bash 分隔提取前缀后输出 |
| 3 | run_logs | positive | must_contain: REF_NAME_NO_PREFIX= | COVERED | `${ATOMGIT_REF_NAME#refs/}` bash 剥离前缀后输出 |
| 4 | run_logs | negative | must_not_contain: REF_NAME_NO_PREFIX=refs/ | COVERED | 负向校验 ref_name 剥离后不残留 `refs/`，与正向断言互补 |
| 5 | run_logs | positive | must_contain: ACTOR_LEN= | COVERED | `${#ATOMGIT_ACTOR}` 计算长度后输出 |
