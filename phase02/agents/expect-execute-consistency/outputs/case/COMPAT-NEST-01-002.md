# COMPAT-NEST-01-002
- **标题**: workflow_call 嵌套层数 - 3 层越界应报错
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**workflow_call 嵌套层数 - 3 层越界应报错**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-015
通过标准：
1. 平台应对超过 2 层的嵌套给出明确错误
2. 错误信息应说明 workflow_call 最多支持 2 层嵌套
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | call-level2 | uses: ./.gitcode/workflows/level2.yml | — | 调用 level2（其内部再调 level3） |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | reusable-workflow-3layer |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | negative | — | ✅ GENUINE | 3 层嵌套不被接受，run_status 应不为 success；step 使用 uses: 真实调用 |
| 2 | error_message eval=llm_assisted | nonfunctional | — | 🔶 LLM_DEPENDENT | 错误信息质量由 LLM 判定 |
### 问题
- 断言2（LLM判定）被跳过；断言1 为 GENUINE
---
