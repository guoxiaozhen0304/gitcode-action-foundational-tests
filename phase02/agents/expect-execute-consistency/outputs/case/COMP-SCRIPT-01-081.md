# COMP-SCRIPT-01-081
- **标题**: 仓库内脚本执行与路径验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**仓库内脚本执行与路径验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-081
通过标准：
1. 仓库内脚本成功执行（正向）
2. 脚本输出出现在日志中（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Run inline script | `echo "inline_script_ok"` | - | inline_script_ok |
| 2 | Run repo script | `./scripts/hello.sh || echo "script_fallback"` | - | 脚本实际输出 或 script_fallback |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: inline_script_ok | ❌ VACUOUS | 步骤仅 echo 字面量，未执行仓库内脚本；步骤 2 的真实脚本执行结果未被断言 |
### 问题
**断言 1 — VACUOUS**: 步骤仅 echo 了 literal 字符串 "inline_script_ok"，未执行仓库内相对路径脚本。虽然步骤 2 执行了 `./scripts/hello.sh`，但该步骤的输出并未被断言覆盖——真正执行仓库脚本的行为未被验证。
---
