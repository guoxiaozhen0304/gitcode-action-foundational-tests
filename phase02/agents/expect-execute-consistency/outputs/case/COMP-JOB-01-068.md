# COMP-JOB-01-068

- **标题**: job strategy 矩阵与 continue-on-error 验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `strategy.matrix` 正确展开多实例，`continue-on-error: true` 和 `fail-fast: false` 被平台接受。

## 做了什么
job 定义 `strategy.matrix.version: [a, b]`、`fail-fast: false`、`continue-on-error: true`；每个实例 step 输出 `VERSION=${{ matrix.version }}` 和 `strategy_ok`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: VERSION=a | COVERED | `${{ matrix.version }}` 输出矩阵实例 a 的值 |
| 2 | run_logs | positive | must_contain: VERSION=b | COVERED | `${{ matrix.version }}` 输出矩阵实例 b 的值 |
| 3 | run_logs | positive | must_contain: strategy_ok | COVERED | 矩阵实例均执行 marker |
