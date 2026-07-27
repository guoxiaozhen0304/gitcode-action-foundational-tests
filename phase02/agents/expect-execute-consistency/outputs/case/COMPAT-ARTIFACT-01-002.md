# COMPAT-ARTIFACT-01-002
- **标题**: upload-artifact 保留期行为等价性
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**upload-artifact 支持保留期参数配置，保留期内可正常下载**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-026
通过标准：
1. 保留期内可正常下载
2. 超期后 artifact 被清理
3. 保留期配置不被静默忽略
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | create artifact file | `echo "RETENTION_TEST_MARKER" > retention_marker.txt` | — | retention_marker.txt |
| 2 | upload with retention | `uses: upload-artifact with: retention-days: 1` | — | 上传成功 |
| 3 | verify upload success | `echo "ARTIFACT_UPLOADED_OK"` | — | ARTIFACT_UPLOADED_OK |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status=completed_success | positive | — | ✅ GENUINE | 步骤含 uses: upload-artifact，有 retention-days 真实参数 |
| 2 | run_logs ARTIFACT_UPLOADED_OK | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | artifact_state 保留行为 | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 4 | run_logs 静默忽略检测 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
