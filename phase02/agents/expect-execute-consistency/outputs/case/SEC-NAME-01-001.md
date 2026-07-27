# SEC-NAME-01-001
- **标题**: Secret/变量名含特殊字符时不可导致意外求值或权限绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**含中划线的 secret 名不因解析错误而泄露到日志**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-024
通过标准：
1. 日志不含 MY-VAR 原值
2. run_status 为 success 或 YAML 校验报错
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use hyphen secret | `echo "value is ${{ secrets.MY-VAR }}"` | — | secret 值或空/*** |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | MY-VAR |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 MY-VAR 原值 | negative | run_logs must_not_contain_secret | ✅ GENUINE | ${{ secrets.MY-VAR }} → NEVER VACUOUS；含中划线可能导致解析错误 |
| 2 | success_or_yaml_error | positive | run_status equals | ⚠️ STATUS_GUARANTEED | 步骤仅 echo，若 YAML 合法解析则必然成功；步骤无 exit 1 路径 |
### 问题
断言 2 STATUS_GUARANTEED：echo 必然成功，无法区分 "success" vs "yaml_error" 两种预期路径。
---
