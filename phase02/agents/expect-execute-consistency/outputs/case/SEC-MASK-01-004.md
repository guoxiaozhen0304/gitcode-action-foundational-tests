# SEC-MASK-01-004
- **标题**: Secret 日志脱敏不可通过字符串拼接或插值绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**拆分为多段拼接输出的 secret 值不在日志中以可还原形式出现**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-006
通过标准：
1. 日志不含 API_KEY 明文
2. 任意连续子串命中数为 0
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo secret in parts | `part1=$(echo "${{ secrets.API_KEY }}" \| cut -c1-4); part2=$(echo "${{ secrets.API_KEY }}" \| cut -c5-8); echo "part1=$part1 part2=$part2"` | — | 分片 secret |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | API_KEY |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 API_KEY 明文 | negative | run_logs must_not_contain_secret | ✅ GENUINE | ${{ secrets.API_KEY }} + cut 分片 → NEVER VACUOUS；分片后脱敏由平台机制决定 |
| 2 | 连续子串命中为 0 | negative | run_logs eval=llm_assisted | 🔶 LLM_DEPENDENT | llm 辅助判定 |
### 问题
(无)
---
