# COMPAT-NEEDS-01-002
- **标题**: needs 上游 job 被跳过时的 result 取值语义
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**needs 上游 job 被跳过时的 result 取值语义**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-041
通过标准：
1. 上游 skipped 时 needs 上游 result 取值与 GitHub（skipped）对齐
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | skipme: Never executed | `echo "SHOULD_NOT_PRINT"` | `${{ false }}` | 永不执行 |
| 2 | downstream: Read result of skipped upstream | `echo "SKIPPED_RESULT=${{ needs.skipme.result }}"` 及 PROBE_DONE | `${{ always() }}` | SKIPPED_RESULT=<值> |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_contain "PROBE_DONE" | positive | — | ✅ GENUINE | downstream job 使用 if: ${{ always() }} 条件确保执行，但 ${{ needs.skipme.result }} 表达式若 crash 则 PROBE_DONE 不输出 |
| 2 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | SKIPPED_RESULT 取值由 LLM 判定 |
### 问题
- 断言2（LLM判定）被跳过；断言1 为 GENUINE
---
