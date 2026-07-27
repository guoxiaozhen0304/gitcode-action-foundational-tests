# COMPAT-EXPR-01-002
- **标题**: success() 函数的处理行为差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**平台可能对 success() 函数与 bare success 关键字有不同的支持策略**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-004
通过标准：
1. 若支持，表达式返回布尔结果
2. 若不支持，应有表达式解析错误或降级行为
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | `uses: checkout` | — | 检出代码 |
| 2 | succeed (Job A) | `echo "Job A done"` | — | Job A done |
| 3 | checkout source (Job B) | `uses: checkout` | — | 检出代码 |
| 4 | observe dependency success (Job B) | `echo "Job B ran after Job A success"` | — | Job B ran after Job A success |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains Job B ran after Job A success | positive | — | ❌ VACUOUS | 第4步仅 echo 该字符串，不验证 success() 函数行为 |
| 2 | run_status=success | positive | — | ✅ GENUINE | workflow 含 needs: job-a 依赖和 uses: checkout，有真实行为 |
### 问题
文本规格声称测试 success() 函数，但 YAML 中完全未使用 success()。仅在 job 级使用了 needs 依赖（job-a → job-b），但 echo 断言无法验证 success() 函数行为的差异。
---
