# COMPAT-EXPR-01-006
- **标题**: hashFiles 表达式无匹配路径边界
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**hashFiles 表达式无匹配路径边界**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-007
通过标准：
1. hashFiles 对无匹配路径返回空字符串或确定的默认值
2. 无匹配时不应抛出异常导致 step 失败
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | — | — |
| 2 | hash no match | `echo "hash no match: ${{ hashFiles('**/nonexistent-pattern.xyz') }}"` | — | hashFiles 对不存在文件的求值结果 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains "hash no match:" | positive | — | ✅ GENUINE | 步骤使用 ${{ hashFiles('**/nonexistent-pattern.xyz') }} 表达式求值，若 hashFiles 对无匹配路径崩溃则日志不输出 |
---
