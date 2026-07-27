# COMP-STEP-01-071
- **标题**: step 执行控制 shell working-directory continue-on-error timeout-minutes 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**step 执行控制 shell working-directory continue-on-error timeout-minutes 验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-069
通过标准：
1. shell bash 和 sh 均可执行（正向）
2. working-directory 改变执行目录（正向）
3. continue-on-error true 被接受（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Bash shell | `shell: bash`, `echo "bash_ok"` | - | bash_ok |
| 2 | Sh shell | `shell: sh`, `echo "sh_ok"` | - | sh_ok |
| 3 | Working directory | `working-directory: .`, `echo "wd_ok"` | - | wd_ok |
| 4 | Continue on error | `continue-on-error: true`, `echo "continue_ok"` | - | continue_ok |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: bash_ok | ❌ VACUOUS | 步骤仅 echo 字面量。shell: bash 的验证无意义——echo 在 bash/sh 中行为相同，无法区分 shell；run 命令无 ${{ }}/if/uses/实质命令 |
| 2 | run_logs | positive | must_contain: sh_ok | ❌ VACUOUS | 同上，shell: sh 的验证空洞 |
| 3 | run_logs | positive | must_contain: wd_ok | ❌ VACUOUS | working-directory: . 指定当前目录，echo 不依赖目录，无法验证 wd 是否真正改变执行路径 |
| 4 | run_logs | positive | must_contain: continue_ok | ❌ VACUOUS | continue-on-error: true 仅在步骤失败时才有意义，但该步骤成功执行 echo，未验证 continue-on-error 的实际效果 |
### 问题
**全部断言 — VACUOUS**: 所有步骤仅 echo 字面量，shell/workdir/continue-on-error 字段需要差异化命令才能体现效果（如 shell 需执行 bash 特性语法、workdir 需输出 pwd、continue-on-error 需故意失败）。当前 echo 无法区分这些配置是否真正生效。
---
