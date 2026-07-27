# SEC-NAME-01-004
- **标题**: 与系统变量同名的用户自定义值绝不应覆盖 job 环境中的平台注入值
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**用户自定义 env 不覆盖平台注入的系统变量值**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-041
通过标准：
1. 系统变量完整性保持
2. 用户值不覆盖系统变量
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Verify system variable integrity | `echo "SYSTEM_VAR_CHECK: comparing system variable values against platform injected values"` | env: ATOMGIT_ENV=/tmp/fixture-shadow-path | 检查标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 系统变量完整性保持 | positive | job_env equals "system_var_integrity_preserved" | ❌ MISSING_SOURCE | target=job_env 非 run_logs/run_status；步骤仅 echo 固定字符串，无实际比对逻辑 |
| 2 | 用户值不覆盖系统变量 | negative | job_env must_not_equal | ❌ MISSING_SOURCE | 同上 |
### 问题
所有断言 target=job_env，workflow 步骤无实际环境变量比对输出，仅打印一句描述性文字。
---
