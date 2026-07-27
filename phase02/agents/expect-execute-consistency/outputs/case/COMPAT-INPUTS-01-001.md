# COMPAT-INPUTS-01-001
- **标题**: workflow_dispatch inputs 类型限制 - boolean 应报错
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**workflow_dispatch inputs 类型限制 - boolean 应报错**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-014
通过标准：
1. 平台应对不支持的 boolean 类型给出明确的校验错误
2. 错误信息应提示仅支持 string 类型
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo input | `echo "INPUT_OK"` | — | "INPUT_OK" |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | negative | — | ✅ GENUINE | boolean 类型 input 不应被静默接受，若平台拒绝此配置，run_status 将不会为 success |
| 2 | error_message eval=llm_assisted | nonfunctional | — | 🔶 LLM_DEPENDENT | 错误信息质量由 LLM 判定 |
### 问题
- 断言2（LLM判定）被跳过
---
