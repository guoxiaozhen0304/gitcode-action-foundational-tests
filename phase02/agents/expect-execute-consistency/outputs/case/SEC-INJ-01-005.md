# SEC-INJ-01-005
- **标题**: 表达式求值必须防止双重模板渲染（二次求值）
- **维度**: security
- **评级**: 断言一致

## 想测什么
外层 ${{ }} 求值结果中的 {{ 1 + 1 }} 字面串不应被内层二次求值为 2。

## 做了什么
workflow echo "${{ '{{ 1 + 1 }}' }}"; 断言日志不含 "Input: 2"、含 "{{ 1 + 1 }}"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "Input: 2" | COVERED | 对应"日志绝不应出现求值结果 2"；${{ }} + echo→GENUINE |
| 2 | run_logs | positive | contains "{{ 1 + 1 }}" | COVERED | 对应"日志中原样包含转义后的字面模板串"；echo→GENUINE |
