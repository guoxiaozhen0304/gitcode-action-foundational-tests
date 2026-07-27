# COMPAT-NEEDS-01-003
- **标题**: matrix 上游 job 的 needs outputs 聚合语义与未声明 output 边界
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**matrix 上游 job 的 needs outputs 聚合语义与未声明 output 边界**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-041
通过标准：
1. matrix 上游聚合取值确定且语义明确
2. 未声明 output 引用返回空而非报错
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | gen: Emit per instance mark | `echo "mark=instance-${{ matrix.idx }}" >> "$ATOMGIT_OUTPUT"` | — | mark=instance-1/2 |
| 2 | consume: Read aggregated and undeclared outputs | `echo "AGG_MARK=${{ needs.gen.outputs.mark }}"` 及 UNDECLARED/PROBE_DONE | — | AGG_MARK=<值>, UNDECLARED=<空> |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_contain "PROBE_DONE" | positive | — | ✅ GENUINE | ${{ needs.gen.outputs.mark }} 和 ${{ needs.gen.outputs.never_declared }} 均为真实表达式，若解析失败则不输出 |
| 2 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | AGG_MARK 取值由 LLM 判定 |
| 3 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | UNDECLARED 空值由 LLM 判定 |
### 问题
- 断言2、3（LLM判定）被跳过；断言1 为 GENUINE
---
