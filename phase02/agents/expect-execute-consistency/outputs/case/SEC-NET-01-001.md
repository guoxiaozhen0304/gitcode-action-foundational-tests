# SEC-NET-01-001
- **标题**: Runner 网络出站必须受控，防止 SSRF 与内网跳板
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**Runner 无法访问内网元数据端点和内部 IP，返回超时或连接拒绝**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-023
通过标准：
1. 日志不含 metadata_service_response
2. 访问被拒或超时
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Access metadata endpoint | `curl -s --max-time 5 http://169.254.169.254/ \|\| echo "access denied or timeout"` | — | 访问结果或拒绝信息 |
| 2 | Access internal IP | `curl -s --max-time 5 http://192.168.1.1/ \|\| echo "access denied or timeout"` | — | 访问结果或拒绝信息 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 metadata_service_response | negative | run_logs must_not_contain | ✅ GENUINE | curl 尝试访问内网元数据端点 → 真实网络行为；输出依赖平台网络隔离 |
| 2 | access_denied_or_timeout | positive | run_logs equals | ❌ VACUOUS | 步骤在 curl 失败时 echo "access denied or timeout"（空格），但断言期望 "access_denied_or_timeout"（下划线）；步骤从不输出下划线版本的精确字符串 |
### 问题
断言 2 VACUOUS：步骤输出自然语言字符串（含空格），断言期望下划线语义标签，精确文本不匹配。
---
