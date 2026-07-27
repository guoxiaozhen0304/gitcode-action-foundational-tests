# COMPAT-ARTIFACT-01-001
- **标题**: upload/download-artifact 跨 job 传递等价性
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**upload-artifact 成功上传到 artifact 存储，download-artifact 成功下载，内容跨 job 一致**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-026
通过标准：
1. upload-artifact 步骤成功
2. download-artifact 步骤成功
3. 跨 job 后文件内容一致
4. 不应因裸插件名解析失败
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | create artifact file | `mkdir -p artifacts; echo marker > artifacts/marker.txt` | — | artifacts/marker.txt |
| 2 | upload artifact | `uses: upload-artifact with: name/path` | — | 上传成功 |
| 3 | download artifact | `uses: download-artifact with: name/path` | — | 下载成功 |
| 4 | verify artifact content | `if grep ... echo ARTIFACT_TRANSFER_OK else FAILED; exit 1` | — | ARTIFACT_TRANSFER_OK 或 FAILED |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status=completed_success | positive | — | ✅ GENUINE | 步骤含 uses: 动作，真实命令和 exit 1，跨 job needs 依赖 |
| 2 | run_logs ARTIFACT_TRANSFER_OK | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | run_logs 不应出现 FAILED | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 4 | workflow_parse 不应因裸插件名失败 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
