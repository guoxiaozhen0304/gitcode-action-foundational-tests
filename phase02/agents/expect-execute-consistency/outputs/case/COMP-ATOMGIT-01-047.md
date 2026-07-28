# COMP-ATOMGIT-01-047
- **标题**: atomgit 核心上下文属性可访问性
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
atomgit 核心属性（sha/ref/ref_name/ref_type/event_name/repository/run_number/run_attempt/workflow/server_url/api_url/workspace/actor/repositoryUrl/base_ref）可正常访问并输出非空值。

## 做了什么
1. step `Print core properties`：echo 各 atomgit 属性（如 `echo "SHA=${{ atomgit.sha }}"` 等 15 个属性）
2. step `Check sha length and ref name prefix`：检查 sha 长度 `${#SHA}` 和 ref_name 是否以 refs/ 开头

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: SHA= | COVERED | step `echo "SHA=${{ atomgit.sha }}"` 使用 ${{ }} 表达式，输出平台注入的上下文值 |
| 2 | run_logs | positive | must_contain: REF=refs/ | COVERED | step `echo "REF=${{ atomgit.ref }}"` 输出 |
| 3 | run_logs | positive | must_contain: REPO= | COVERED | step `echo "REPO=${{ atomgit.repository }}"` 输出 |
| 4 | run_logs | positive | must_contain: SHA_LEN=40 | COVERED | `${#SHA}` 计算输出，SHA 来自 ${{ atomgit.sha }} 表达式 |
| 5 | run_logs | positive | must_contain: REF_NAME_HAS_PREFIX=no | COVERED | case 语句判断并 echo 输出 |
