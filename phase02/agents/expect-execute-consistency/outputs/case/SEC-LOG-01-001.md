# SEC-LOG-01-001
- **标题**: 无权限角色读取/下载运行日志必须被拒，过期日志绝不应可恢复
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**有权限成员可下载日志，无权限角色返回 403/404，过期日志不可恢复**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-040
通过标准：
1. 有权限下载成功
2. 无权限访问被拒
3. 过期日志不可恢复
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Emit log content | `echo "LOG_ACCESS_CONTROL_FIXTURE: log content produced"` | — | 日志内容 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 有权限下载成功 | positive | log_api equals "authorized_download_ok" | ❌ MISSING_SOURCE | target=log_api 为外部 API 接口，workflow 仅 echo 日志内容，无下载 API 调用 |
| 2 | 无权限访问被拒 | negative | log_api must_not_equal | ❌ MISSING_SOURCE | 同上 |
| 3 | 过期日志不可恢复 | negative | log_api must_not_equal | ❌ MISSING_SOURCE | 同上 |
### 问题
所有断言 target=log_api 为外部平台接口，workflow 步骤仅生成日志内容，无法驱动日志访问控制验证。
---
