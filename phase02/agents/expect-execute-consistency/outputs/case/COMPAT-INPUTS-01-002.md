# COMPAT-INPUTS-01-002
- **标题**: workflow_dispatch inputs 类型限制 - string 正常通过
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**workflow_dispatch inputs 类型限制 - string 正常通过**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-014
通过标准：
1. workflow 应被平台接受，不报错
2. string 类型的 input 应能正常接收和输出
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo input value | `echo "ENV=${{ inputs.environment }}"` 后 `echo "STRING_INPUT_OK"` | — | ENV=production 及 STRING_INPUT_OK |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch (params: environment=production) |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | positive | — | ✅ GENUINE | 步骤使用 ${{ inputs.environment }} 表达式，若 inputs 传递机制异常则 run_status 非 success |
| 2 | run_logs must_contain "STRING_INPUT_OK" | positive | — | ⚠️ STATUS_GUARANTEED | echo "STRING_INPUT_OK" 为纯字面输出，在步骤执行时必然出现 |
| 3 | run_logs must_contain "ENV=production" | positive | — | ✅ GENUINE | ENV=production 依赖 ${{ inputs.environment }} 正确传递值 "production" |
### 问题
- 断言2 为 STATUS_GUARANTEED（纯 echo），但断言1 和断言3 均为 GENUINE
---
