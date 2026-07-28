# COMP-EXPR-01-058
- **标题**: 表达式运算符与优先级边界行为
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
各运算符（== / != / ! / && / || / > / < / >= / <=）按正确优先级求值。

## 做了什么
1. step `Equality`（if: ${{ atomgit.event_name == 'workflow_dispatch' }}）：`echo "eq_passed"`
2. step `Equality negative`（if: ${{ atomgit.event_name == 'push' }}）：`echo "eq_negative_unexpected"`（条件不成立应跳过）
3. step `Not equal`（if: ${{ atomgit.ref_name != 'nonexistent' }}）：`echo "ne_passed"`
4. step `Not operator`（if: ${{ !false }}）：`echo "not_passed"`
5. step `Greater than`（if: ${{ 5 > 3 }}）：`echo "gt_passed"`
6. step `Less than`（if: ${{ 2 < 3 }}）：`echo "lt_passed"`
7. step `Greater or equal`（if: ${{ 3 >= 3 }}）：`echo "ge_passed"`
8. step `Less or equal`（if: ${{ 3 <= 4 }}）：`echo "le_passed"`
9. step `Logical combo`（if: ${{ true && (false || true) }}）：`echo "logic_passed"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: eq_passed | COVERED | ${{ == }} 表达式成立，step 执行 |
| 2 | run_logs | positive | must_contain: ne_passed | COVERED | ${{ != }} 表达式成立 |
| 3 | run_logs | positive | must_contain: not_passed | COVERED | ${{ !false }} 成立 |
| 4 | run_logs | positive | must_contain: gt_passed | COVERED | ${{ 5 > 3 }} 成立 |
| 5 | run_logs | positive | must_contain: lt_passed | COVERED | ${{ 2 < 3 }} 成立 |
| 6 | run_logs | positive | must_contain: ge_passed | COVERED | ${{ 3 >= 3 }} 成立 |
| 7 | run_logs | positive | must_contain: le_passed | COVERED | ${{ 3 <= 4 }} 成立 |
| 8 | run_logs | positive | must_contain: logic_passed | COVERED | ${{ true && (false || true) }} 成立 |
| 9 | run_logs | negative | must_not_contain: eq_negative_unexpected | COVERED | if 条件不成立，step 被跳过 |
