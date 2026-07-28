# COMPAT-EXPR-01-003
- **标题**: failure() 与 failed 关键字的处理行为差异   - **维度**: 兼容性   - **评级**: 部分不符
## 想测什么
探测 failure() 或 failed 关键字的处理行为——支持时正确返回状态，不支持时记录差异。
## 做了什么
workflow_dispatch 触发，checkout + exit 1 强制失败 + `if: ${{ always() }}` echo `Cleanup ran after failure`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | contains: Cleanup ran after failure | GENUINE→COVERED | `if: ${{ always() }}` 为真实条件表达式 |
| 2 | run_status | positive | equals: failure | GENUINE→COVERED | exit 1 真实引发失败 |
说明：文本关注 failure()/failed 关键字行为，但 YAML 仅使用了 `always()`，并未使用 `failure()` 或 `failed`。failure()/failed 关键字的使用场景为 MISSING——当前 YAML 验证了 exit 1 + `if: always()` 的清理执行，但未触及 failure()/failed 的实际行为探测。 |
