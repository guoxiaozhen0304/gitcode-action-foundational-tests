# SEC-ARTF-01-001
- **标题**: fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执行
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**主仓不可下载 fork PR 上传的 artifact，应返回 404 或权限拒绝**
- 触发事件: `pull_request` (as untrusted_contributor)
- 规格引用: INTENT-SEC-019
通过标准：
1. artifact_download 失败（非 success）
2. 返回 404 或权限拒绝
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Create file | `echo fork content > fork-artifact.txt` | — | — |
| 2 | Upload artifact | `uses: upload-artifact` with name=fork-artifact, path=fork-artifact.txt | — | artifact 上传 |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | with-artifacts |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | artifact_download != success | negative | must_not_equal "success" | ❌ MISSING_SOURCE | target=artifact_download 是平台外部接口，workflow 步骤仅上传 artifact，无步骤执行下载操作 |
| 2 | 返回 404 或权限拒绝 | positive | artifact_download equals "404_or_permission_denied" | ❌ MISSING_SOURCE | 同上，workflow 无任何下载验证步骤 |
### 问题
两个断言 target 均为 artifact_download（外部 API 接口），workflow 仅上传 artifact 不做下载验证，无法驱动断言。
---
