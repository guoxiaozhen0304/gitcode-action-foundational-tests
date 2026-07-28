# COMP-JOB-01-068
- **标题**: job strategy 矩阵与 continue-on-error 验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
strategy.matrix 正确展开多实例，continue-on-error true 被接受，fail-fast false 被接受。

## 做了什么
1. strategy: matrix: version=[a, b], fail-fast: false, continue-on-error: true
2. step `Matrix value`（在每个矩阵实例中执行）：`echo "VERSION=${{ matrix.version }}"` 和 `echo "strategy_ok"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: VERSION=a | COVERED | ${{ matrix.version }} 表达式取 'a' |
| 2 | run_logs | positive | must_contain: VERSION=b | COVERED | ${{ matrix.version }} 表达式取 'b' |
| 3 | run_logs | positive | must_contain: strategy_ok | COVERED | echo 固定标记 |
