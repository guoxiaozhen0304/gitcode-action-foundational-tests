# COMPAT-EXPR-01-007
- **标题**: hashFiles 表达式多路径组合边界
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**hashFiles 表达式多路径组合边界**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-007
通过标准：
1. hashFiles 对多路径组合返回组合的哈希值
2. 验证多路径匹配行为与 GitHub Actions 是否一致
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | — | — |
| 2 | hash multiple paths | `echo "hash multi: ${{ hashFiles('**/package.json', '**/package-lock.json') }}"` | — | hashFiles 多路径哈希值 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains "hash multi:" | positive | — | ✅ GENUINE | 步骤使用 ${{ hashFiles(...) }} 真实表达式求值，非纯字面 echo |
---
