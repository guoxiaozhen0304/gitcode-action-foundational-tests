# SEC-BASE-01-002
- **标题**: fork PR 改 workflow 不被 pull_request_target 采用
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**pull_request_target 不采用 fork PR 的 workflow 改动，仅执行 base 分支定义**
- 触发事件: `pull_request_target` (as maintainer)
- 规格引用: INTENT-SEC-035
通过标准：
1. 日志不含 fork_injected_step
2. 运行状态为 success_with_base_workflow
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Base step only | `echo "Only base steps run"` | — | "Only base steps run" |

## 3. 触发与运行环境
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | DEPLOY_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 fork_injected_step | negative | run_logs must_not_contain | ✅ GENUINE | 步骤不产生该字符串，依赖平台行为阻止 fork 注入执行 |
| 2 | success_with_base_workflow | positive | run_status equals | ⚠️ STATUS_GUARANTEED | 步骤仅 `echo`，无 if:/exit 1/${{ }}，必然成功；该值由外部判定器映射 |
### 问题
断言 2 STATUS_GUARANTEED：步骤无任何失败路径，workflow 必然 success，无法区分 base/fork 行为差异。
---
