# COMPAT-EXPR-01-003
- **标题**: failure() 与 failed 关键字的处理行为差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**平台对 failure() 函数与 failed 关键字可能有不同的支持策略，验证失败后步骤的清理执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-005
通过标准：
1. 若支持，可在失败后获取到正确的状态值
2. 若不支持，应有表达式解析错误或降级行为
3. 失败后 step 的执行状态可被观察
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | `uses: checkout` | — | 检出代码 |
| 2 | force failure | `exit 1` | — | 步骤失败 |
| 3 | cleanup after failure | `echo "Cleanup ran after failure"` | if: ${{ always() }} | Cleanup ran after failure |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains Cleanup ran after failure | positive | — | ✅ GENUINE | 步骤有 `if: ${{ always() }}` 条件（真实表达式），且前一步 exit 1 制造失败 |
| 2 | run_status=failure | positive | — | ✅ GENUINE | 步骤含 exit 1 的 deliberate failure，真实验证失败状态 |
---
