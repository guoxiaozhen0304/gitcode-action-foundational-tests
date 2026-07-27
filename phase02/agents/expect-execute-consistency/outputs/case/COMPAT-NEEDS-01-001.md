# COMPAT-NEEDS-01-001
- **标题**: needs 上下文存在性与 outputs/result 字段对齐
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**needs 上下文存在性与 outputs/result 字段对齐**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-041
通过标准：
1. needs 上游 outputs 取值正确
2. needs 上游 result 与 GitHub 语义对齐
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | build: Generate version output | `echo "version=1.2.3" >> "$ATOMGIT_OUTPUT"` | — | output version=1.2.3 |
| 2 | consume: Read needs outputs and result | `echo "NEEDS_VERSION=${{ needs.build.outputs.version }}"` 及 result/ PROBE_DONE | — | NEEDS_VERSION=1.2.3, NEEDS_RESULT=<值> |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_contain "NEEDS_VERSION=1.2.3" | positive | — | ✅ GENUINE | 下游 job 通过 ${{ needs.build.outputs.version }} 引用上游 output，若 needs 上下文不可用或 output 传递异常，此字符串不出现 |
| 2 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | NEEDS_RESULT 取值由 LLM 判定 |
| 3 | run_logs eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | needs 可用性由 LLM 判定 |
### 问题
- 断言2、3（LLM判定）被跳过；断言1 为 GENUINE
---
