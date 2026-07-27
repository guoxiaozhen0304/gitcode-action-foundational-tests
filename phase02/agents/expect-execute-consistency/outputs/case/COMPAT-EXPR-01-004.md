# COMPAT-EXPR-01-004
- **标题**: contains 表达式大小写敏感边界
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**contains 表达式按平台实际实现返回 true 或 false，验证大小写敏感行为**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-006
通过标准：
1. 大小写匹配时返回 true
2. 大小写不匹配时返回 false
3. 结果不应与预期语义矛盾
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | `uses: checkout` | — | 检出代码 |
| 2 | test lowercase match | `echo "lowercase match: ${{ contains('Hello World', 'world') }}"` | — | lowercase match: true/false |
| 3 | test exact case match | `echo "exact case match: ${{ contains('Hello World', 'World') }}"` | — | exact case match: true/false |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains exact case match: true | positive | — | ✅ GENUINE | 步骤使用 `${{ contains() }}` 表达式，真实验证平台 contains 表达式求值 |
---
