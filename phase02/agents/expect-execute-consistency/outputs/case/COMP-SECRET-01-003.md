# COMP-SECRET-01-003
- **标题**: base64 编码后的 secret 是否仍被脱敏
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**base64 编码后的 secret 是否仍被脱敏**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-012
通过标准：
1. 记录 base64 编码输出是否被脱敏（非功能）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo base64 secret | `echo "base64 secret is $(echo -n '${{ secrets.TEST_SECRET }}' | base64)"` | - | base64 编码结果 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | [TEST_SECRET] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估 base64 编码后的 secret 输出是否仍被脱敏为 *** |
---
