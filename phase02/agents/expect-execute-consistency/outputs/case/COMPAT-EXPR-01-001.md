# COMPAT-EXPR-01-001
- **标题**: success 关键字在条件表达式中的可用性   - **维度**: 兼容性   - **评级**: 部分不符
## 想测什么
探测 success 关键字在条件表达式中的可用性（支持则返值，不支持则记录差异）。
## 做了什么
workflow_dispatch 触发，checkout + 两个简单 echo step（无任何 if:/${{ success }}/${{ failure }} 等表达式）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | contains: implicit success confirmed | GENUINE→COVERED | 步骤 echo 产生，uses: checkout + 纯 echo 为真实操作 |
说明：文本关注 success 关键字/函数在表达式中的行为，但 YAML 中无任何 `success`/`success()` 相关表达式引用或 if 条件。文本称"尝试通过表达式获取"，但 YAML 仅做了两个普通 step 执行。success 关键字的使用场景为 MISSING——当前 YAML 只是验证了正常 step 顺序执行，未实质触及 success 关键字。 |
