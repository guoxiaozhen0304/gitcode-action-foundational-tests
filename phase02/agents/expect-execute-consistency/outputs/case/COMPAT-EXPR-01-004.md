# COMPAT-EXPR-01-004

- **标题**: contains 表达式大小写敏感边界
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 contains 表达式的大小写敏感行为。

## 做了什么
echo "${{ contains('Hello World', 'world') }}" 和 "${{ contains('Hello World', 'World') }}"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: exact case match: true | COVERED | 表达式 ${{ contains('Hello World', 'World') }} 真实求值输出 |
