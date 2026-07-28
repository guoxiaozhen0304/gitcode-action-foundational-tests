# SEC-ARTF-01-003
- **标题**: 宽通配打包含敏感文件名的 artifact 绝不应在无警示情况下静默成功且可被无痕下载
- **维度**: 安全性
- **优先级**: P2
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
补真实校验步骤（ls 敏感文件 + SENSITIVE_GLOB_UPLOAD_ATTEMPTED 标记）；断言 1 原 STATUS_GUARANTEED（外部判定器字面值）改为 llm rubric 明确判读内容；跨角色下载留痕检查保留 harness 判定并注释。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain SENSITIVE_GLOB_UPLOAD_ATTEMPTED | ✅ GENUINE | 真实 ls + 标记输出 |
| 2 | run_logs | negative | llm_assisted | 🔶 LLM_DEPENDENT | 平台警示日志有无属日志内容判读 |
| 3 | artifact_download | negative | must_not_equal cross_role_download_without_trace | ✅ COVERED | harness 跨角色下载留痕检查 |
| 4 | documentation | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 文档内容判读 |

### 残留问题
平台警示措辞与文档内容判读本质不可确定化，保留 llm_assisted（YAML 已注释）。
