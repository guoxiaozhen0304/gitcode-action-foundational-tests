# COMPAT-PERM-01-004
- **标题**: permissions 命名差异——GitCode repository 权限项正常生效
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**permissions 命名差异——GitCode repository 权限项正常生效**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-030
通过标准：
1. `repository: read` 被平台正确解析并生效
2. 工作流可正常执行 clone 和读取仓库内容
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout with repository read | uses: checkout | — | — |
| 2 | verify repo access | if README.md exists echo "REPOSITORY_PERM_OK" else echo "REPOSITORY_PERM_FAILED" + exit 1 | — | REPOSITORY_PERM_OK 或 FAILED |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals completed_success | positive | — | ✅ GENUINE | uses: checkout + cat README.md 依赖真实权限生效 |
| 2 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | REPOSITORY_PERM_OK 由 LLM 判定 |
| 3 | run_logs eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | REPOSITORY_PERM_FAILED 由 LLM 判定 |
| 4 | workflow_parse eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 解析失败由 LLM 判定 |
### 问题
- 断言2、3、4（LLM判定）被跳过；断言1 为 GENUINE
---
