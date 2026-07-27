# COMPAT-EXPR-01-015
- **标题**: startsWith/endsWith 大小写敏感性两侧文档矛盾的差异确认
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**startsWith/endsWith 大小写敏感性两侧文档矛盾的差异确认**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-036
通过标准：
1. startsWith('Hello World', 'hello') 实测求值与 GitCode 文档一致
2. 差异确认结论回写 Parity Matrix
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Evaluate startsWith with mixed case | `echo "SW_RESULT=${{ startsWith('Hello World', 'hello') }}"` | — | SW_RESULT=true/false |
| 2 | Evaluate endsWith with mixed case | `echo "EW_RESULT=${{ endsWith('v1.0.rc', '.RC') }}"` | — | EW_RESULT=true/false |
| 3 | Mark probe complete | `echo "PROBE_DONE"` | — | PROBE_DONE |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | positive | — | ✅ GENUINE | 步骤含 ${{ startsWith(...) }} 和 ${{ endsWith(...) }} 真实表达式求值，若表达式解析失败则状态非 success |
| 2 | run_logs must_contain "PROBE_DONE" | positive | — | ⚠️ STATUS_GUARANTEED | echo "PROBE_DONE" 是纯字面输出，无 if/uses/${{ }}，在前序步骤成功时必然输出 |
| 3 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | SW_RESULT/EW_RESULT 值与文档一致性由 LLM 判定 |
### 问题
- 断言2 为 STATUS_GUARANTEED（纯 echo），但断言1 为 GENUINE（run_status 依赖于表达式求值成功）
---
