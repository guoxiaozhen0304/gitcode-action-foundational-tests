# COMPAT-MASK-01-001
- **标题**: 直接 echo secrets 值应在日志中被脱敏
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**直接 echo secrets 值应在日志中被脱敏**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-033
通过标准：
1. 日志中 secrets.TEST_SECRET 的值应被替换为 ***
2. 不应出现明文的 secret 值
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | — | — |
| 2 | echo secret directly | `echo "Secret value: ${{ secrets.TEST_SECRET }}"` | — | Secret value: <secret值或***> |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | TEST_SECRET |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_not_contain_secret TEST_SECRET | negative | deterministic | ✅ GENUINE | 步骤使用 ${{ secrets.TEST_SECRET }} 真实引用了 secret，若脱敏失效则明文泄漏，断言精确测试脱敏机制 |
| 2 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | *** 脱敏确认由 LLM 判定 |
### 问题
- 断言2（LLM判定）被跳过；断言1 为 GENUINE
---
