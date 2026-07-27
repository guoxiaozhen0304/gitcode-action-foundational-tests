# COMP-PRTARGET-01-001
- **标题**: pull_request_target 默认使用 base 分支 workflow 版本
- **维度**: 完备性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**pull_request_target 默认使用 base 分支 workflow 版本**
- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMP-014
通过标准：
1. 执行的 step 内容与 base 分支 workflow 一致（正向）
2. 不应执行 fork 分支修改后的 workflow 逻辑（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo base version marker | `echo "BASE_VERSION_MARKER"` | - | BASE_VERSION_MARKER |
## 3. 触发与运行环境
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: BASE_VERSION_MARKER | ❌ VACUOUS | 步骤仅 echo 字面量，无 uses:/if:/${{ }}/实质命令，未验证 pull_request_target 的实际语义 |
| 2 | run_logs | negative | must_not_contain: FORK_VERSION_MARKER | ❌ VACUOUS | 无任何步骤产生该字符串，断言空洞为真 |
### 问题
**断言 1 — VACUOUS**: 步骤仅 echo 了期望字符串 BASE_VERSION_MARKER，未执行 pull_request_target base 分支版本约束的验证逻辑。

**断言 2 — VACUOUS**: 无任何步骤产生 FORK_VERSION_MARKER，must_not_contain 天然为真，未验证任何安全行为。
---
