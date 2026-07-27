# COMP-SCRIPT-01-082
- **标题**: 脚本权限设置与直接执行验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**脚本权限设置与直接执行验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-081
通过标准：
1. chmod 后脚本可执行（正向）
2. 直接执行输出正确（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Set permission and run | `chmod +x ./scripts/hello.sh` / `./scripts/hello.sh` | - | 脚本执行输出 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | `chmod +x` 和 `./scripts/hello.sh` 为实质系统命令，测试了权限设置与脚本直接执行的完整路径 |
---
