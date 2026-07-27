# COMPAT-EXPR-01-001
- **标题**: success 关键字在条件表达式中的可用性
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**若平台支持 success 关键字，则可在适当上下文中获取到状态值，若不支持应有明确行为**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-004
通过标准：
1. 表达式被正确解析
2. 若平台拒绝该关键字应记录兼容性差异
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | `uses: checkout` | — | 检出代码 |
| 2 | previous step succeeds | `echo "Step completed successfully"` | — | Step completed successfully |
| 3 | observe next step runs | `echo "Next step executed, implicit success confirmed"` | — | implicit success confirmed |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains implicit success confirmed | positive | — | ❌ VACUOUS | 第3步仅 echo 该字符串，无 if/uses/${{ }}/任何表达式；workflow 未使用 success 关键字或 success() 函数 |
### 问题
文本规格声称测试 'success 关键字在条件表达式中的可用性'，但 YAML 中完全未使用 success、success() 或任何条件表达式。step 无条件顺序执行，无法验证 success 关键字是否存在或被支持。
---
