# COMP-ATOMGIT-01-047

- **标题**: atomgit 核心上下文属性可访问性
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `atomgit.sha`、`ref`、`ref_name`、`ref_type`、`event_name`、`repository`、`run_number`、`run_attempt`、`workflow`、`server_url`、`api_url`、`workspace`、`actor`、`repositoryUrl`、`base_ref` 等核心上下文属性均可正常访问并输出非空值，sha 长度为 40，ref_name 不含 `refs/` 前缀。

## 做了什么
两个 step：第一个 step 通过 `${{ atomgit.* }}` 表达式输出各核心属性值；第二个 step 用 bash 计算 sha 长度并判断 ref_name 是否含 `refs/` 前缀。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: SHA= | COVERED | `echo "SHA=${{ atomgit.sha }}"` 直接产生该输出 |
| 2 | run_logs | positive | must_contain: REF=refs/ | COVERED | `echo "REF=${{ atomgit.ref }}"` 产生，`${{ }}` 是实时上下文求值 |
| 3 | run_logs | positive | must_contain: REPO= | COVERED | `echo "REPO=${{ atomgit.repository }}"` 直接产生 |
| 4 | run_logs | positive | must_contain: SHA_LEN=40 | COVERED | bash `${#SHA}` 计算 + echo 输出，SHA 来自 `${{ atomgit.sha }}` |
| 5 | run_logs | positive | must_contain: REF_NAME_HAS_PREFIX=no | COVERED | bash `case` 判断 `${{ atomgit.ref_name }}` 是否含 `refs/` 前缀后 echo 输出 |
