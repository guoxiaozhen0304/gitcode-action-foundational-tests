# COMP-TRIG-01-079
- **标题**: 触发事件 types 取值与过滤边界验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**触发事件 types 取值与过滤边界验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-079
通过标准：
1. 合法 types 通过校验（正向）
2. 非法 types 被平台拒绝（负向）
3. 默认 types 在未指定时生效（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo ok | `echo "types_boundary_ok"` | - | types_boundary_ok |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 步骤仅 echo 字面量，无条件失败路径 |
| 2 | run_logs | positive | must_contain: types_boundary_ok | ❌ VACUOUS | 步骤仅 echo 字面量。workflow 使用 workflow_dispatch 触发，但规格中提到的 pull_request types/merge_requests types 边界测试未在 YAML 中体现——workflow_dispatch 没有 types 概念 |
### 问题
**断言 1 — STATUS_GUARANTEED**: 步骤仅 echo 字面量。
**断言 2 — VACUOUS**: 步骤仅 echo 字面量。YAML 使用 workflow_dispatch 触发（无 types 概念），但规格期望测试 pull_request/merge_requests 的 types 边界。YAML 与规格严重不匹配——未测试任何 types 过滤逻辑。
---
