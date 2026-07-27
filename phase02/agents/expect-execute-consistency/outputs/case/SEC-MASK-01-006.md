# SEC-MASK-01-006
- **标题**: Secret 日志脱敏不可通过分片输出绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**逐字符或逐小段输出的 secret 各片段仍被脱敏**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-008
通过标准：
1. 日志不含 DEPLOY_TOKEN 明文
2. 任意连续子串（3 字符以上）命中数为 0
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo secret character by character | `secret="${{ secrets.DEPLOY_TOKEN }}"; for (( i=0; i<${#secret}; i++ )); do echo "char $i: ${secret:$i:1}"; done` | — | 逐字符输出 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | DEPLOY_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 DEPLOY_TOKEN 明文 | negative | run_logs must_not_contain_secret | ✅ GENUINE | ${{ secrets.DEPLOY_TOKEN }} + shell 循环逐字符输出 → NEVER VACUOUS |
| 2 | 连续子串命中为 0 | negative | run_logs eval=llm_assisted | 🔶 LLM_DEPENDENT | llm 辅助判定 |
### 问题
(无)
---
