# COMPAT-EXPR-01-016
- **标题**: format() 花括号转义与字符串字面量引号规则边界
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**format() 花括号转义与字符串字面量引号规则边界**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-050
通过标准：
1. format 双花括号转义求值结果与 GitHub 对齐
2. 字符串字面量引号规则与 GitHub 一致
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Evaluate format brace escaping | `echo "FMT_BRACE=${{ format('{{{0}}}', 'x') }}"` | — | FMT_BRACE={x}或错误 |
| 2 | Evaluate single quote escaping | `echo "FMT_QUOTE=${{ format('it''s {0}', 'ok') }}"` 及 `echo "PROBE_DONE"` | — | FMT_QUOTE=it's ok 及 PROBE_DONE |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_contain "PROBE_DONE" | positive | — | ⚠️ STATUS_GUARANTEED | echo "PROBE_DONE" 是纯字面输出，无 if/uses/${{ }} |
| 2 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | format 转义结果与 GitHub 一致性由 LLM 判定 |
| 3 | run_logs eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 双引号字符串行为由 LLM 判定 |
### 问题
- 断言1 为 STATUS_GUARANTEED（纯 echo "PROBE_DONE"）；断言2、3 均为 LLM_DEPENDENT
---
