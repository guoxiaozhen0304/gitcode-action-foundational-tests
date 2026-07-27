# COMP-STATUS-01-002
- **标题**: 失败 step 的日志完整保留且可查看
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**失败 step 的日志完整保留且可查看**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-017
通过标准：
1. 失败 step 前的输出存在于日志（正向）
2. 失败 step 的错误信息存在于日志（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Before failure | `echo "BEFORE_FAILURE_MARKER"` | - | BEFORE_FAILURE_MARKER |
| 2 | Force failure | `echo "ERROR_MARKER"` / `exit 1` | - | ERROR_MARKER (然后失败) |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: BEFORE_FAILURE_MARKER | ❌ VACUOUS | 步骤仅 echo 字面量，未产生与被测功能相关的输出；虽然步骤 2 有 exit 1（真实失败路径），但 BEFORE_FAILURE_MARKER 本身是空洞标记 |
| 2 | run_logs | positive | contains: ERROR_MARKER | ✅ GENUINE | 步骤含 exit 1 真实失败命令，ERROR_MARKER 在失败步骤中输出，测试了失败日志保留 |
### 问题
**断言 1 — VACUOUS**: 步骤仅 echo 了字面量 BEFORE_FAILURE_MARKER，该标记本身空洞，但断言目的在于验证失败前日志保留——exit 1 步骤提供了真实失败场景。
---
