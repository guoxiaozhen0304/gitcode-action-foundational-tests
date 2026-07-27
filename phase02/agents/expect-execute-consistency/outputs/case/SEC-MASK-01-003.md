# SEC-MASK-01-003
- **标题**: Secret 日志脱敏不可通过 base64 编码绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**base64 编码后的 secret 值不在日志中以明文出现**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-005
通过标准：
1. 日志不含 DEPLOY_TOKEN 明文
2. base64 编码后的字符串被遮蔽
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Encode and echo secret | `encoded=$(echo -n "${{ secrets.DEPLOY_TOKEN }}" \| base64); echo "encoded=$encoded"` | — | base64 编码值 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | DEPLOY_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 DEPLOY_TOKEN 明文 | negative | run_logs must_not_contain_secret | ✅ GENUINE | ${{ secrets.DEPLOY_TOKEN }} → NEVER VACUOUS；base64 编码后脱敏由平台机制决定 |
| 2 | base64 编码后被遮蔽 | negative | run_logs eval=llm_assisted | 🔶 LLM_DEPENDENT | llm 辅助判定 |
### 问题
(无)
---
