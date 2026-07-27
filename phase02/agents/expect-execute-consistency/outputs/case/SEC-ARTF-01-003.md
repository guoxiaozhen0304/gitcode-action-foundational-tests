# SEC-ARTF-01-003
- **标题**: 宽通配打包含敏感文件名的 artifact 绝不应在无警示情况下静默成功且可被无痕下载
- **维度**: 安全性
- **优先级**: P2
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**上传含敏感文件名的 artifact 时应有警示，跨角色下载应留痕**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-045
通过标准：
1. 日志不可显示 silent_success_no_warning
2. 跨角色下载不可无痕
3. 文档需说明风险
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Create placeholder sensitive named files | `echo "placeholder..." > .env.fixture` 等 | — | 占位文件 |
| 2 | Upload workspace with wide glob | `uses: upload-artifact` with name=workspace-bundle, path=. | — | artifact 上传 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-sensitive-files |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 日志 != silent_success_no_warning | negative | run_logs must_not_equal | ⚠️ STATUS_GUARANTEED | 步骤仅 echo 占位符 + uses upload-artifact；无 if/${{ }}/exit 1，步骤必然成功；断言检查的是平台是否产生警示日志，但步骤本身不会输出 "silent_success_no_warning"，该值是外部判定器赋予的 |
| 2 | 下载 != cross_role_download_without_trace | negative | artifact_download must_not_equal | ❌ MISSING_SOURCE | target=artifact_download 为外部接口，workflow 无下载验证步骤 |
| 3 | 文档说明风险 | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | llm 辅助判定 |
### 问题
断言 1 STATUS_GUARANTEED：步骤无任何能触发警示的机制，仅做正常上传。断言 2 MISSING_SOURCE：目标在 workflow 外。双非 LLM 断言均有问题。
---
