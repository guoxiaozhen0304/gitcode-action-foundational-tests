# COMP-SYSENV-01-060

- **标题**: ATOMGIT 系统环境变量值正确性
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 ATOMGIT_SHA、REF、EVENT_NAME 等环境变量与 atomgit 上下文值一致。

## 做了什么
Step: 使用 `[ "$ATOMGIT_SHA" = "${{ atomgit.sha }}" ] && echo yes || echo no` 对比 shell 环境变量与 `${{ }}` 上下文值。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain SHA_MATCH=yes | COVERED | `[ ]` shell 比较 + `${{ atomgit.sha }}` 上下文表达式 |
| 2 | run_logs | positive | must_contain REF_MATCH=yes | COVERED | 同上 |
| 3 | run_logs | positive | must_contain EVENT_MATCH=yes | COVERED | 同上 |
