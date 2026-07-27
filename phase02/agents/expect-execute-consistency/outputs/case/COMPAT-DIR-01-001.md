# COMPAT-DIR-01-001
- **标题**: 工作流目录差异——.gitcode/workflows/ 正常识别
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**.gitcode/workflows/ 下的 .yml 文件被平台识别为有效工作流**
- 触发事件: `push`
- 规格引用: INTENT-COMPAT-029
通过标准：
1. .gitcode/workflows/*.yml 被正确识别
2. 对应事件触发后工作流正常执行
3. 不应出现 .gitcode 目录下文件被忽略
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo from gitcode dir | `echo "GITCODE_DIR_RECOGNIZED_OK"` | — | GITCODE_DIR_RECOGNIZED_OK |
## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status=completed_success | positive | — | ⚠️ STATUS_GUARANTEED | 全步骤仅 echo，无 if:/uses:/${{ }}/真实命令 |
| 2 | run_logs GITCODE_DIR_RECOGNIZED_OK | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | workflow_discovery 正确识别 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
### 问题
run_status 断言为 STATUS_GUARANTEED（全步骤 trivial echo），无法验证 .gitcode/workflows/ 目录确实被平台识别。目录发现行为仅依赖 LLM 断言。
---
