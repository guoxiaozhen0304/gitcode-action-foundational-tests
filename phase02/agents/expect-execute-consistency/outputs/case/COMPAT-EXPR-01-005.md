# COMPAT-EXPR-01-005
- **标题**: contains 表达式空值与空字符串边界
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**contains 表达式空值与空字符串边界**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-006
通过标准：
1. contains 表达式对空字符串和空值有确定性的返回值
2. 验证边界行为与 GitHub Actions 是否一致
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | — | — |
| 2 | test empty haystack | `echo "empty haystack: ${{ contains('', 'a') }}"` | — | contains 表达式求值结果 |
| 3 | test empty needle | `echo "empty needle: ${{ contains('abc', '') }}"` | — | contains 表达式求值结果 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains "empty needle:" | positive | — | ✅ GENUINE | 步骤使用 ${{ contains('abc', '') }} 表达式求值，若表达式解析或求值失败则 echo 不执行，"empty needle:" 不会出现在日志中 |
---
