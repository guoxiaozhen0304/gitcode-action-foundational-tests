# COMP-VARREF-01-083

- **标题**: YAML 表达式与 Shell 环境变量引用方式验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 ${{ env.VAR }} 与 $VAR 引用同一变量时值一致，${{ atomgit.sha }} 与 $ATOMGIT_SHA 值一致。

## 做了什么
顶层设置 env.TEST_VAR=hello，verify job 中 echo 比较表达式 (${{ env.TEST_VAR }}) 与环境变量 ($TEST_VAR) 的值。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: EXPR=hello | COVERED | run: echo "EXPR=${{ env.TEST_VAR }}" |
| 2 | run_logs | positive | must_contain: ENV=hello | COVERED | run: echo "ENV=$TEST_VAR" |
| 3 | run_logs | positive | must_contain: ref_ok | COVERED | run: echo "ref_ok" |
