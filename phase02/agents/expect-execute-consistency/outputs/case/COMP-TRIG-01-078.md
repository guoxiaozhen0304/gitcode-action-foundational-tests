# COMP-TRIG-01-078
- **标题**: 多事件组合与分支路径过滤验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**多事件组合与分支路径过滤验证**
- 触发事件: `push`
- 规格引用: INTENT-COMP-078
通过标准：
1. 多事件组合通过校验（正向）
2. push 到匹配分支且路径匹配时触发（正向）
3. paths 与 paths-ignore 同时存在时平台拒绝或只保留 paths（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo ok | `echo "multi_event_ok"` | - | multi_event_ok |
## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 步骤仅 echo 字面量，无条件失败路径 |
| 2 | run_logs | positive | must_contain: multi_event_ok | ❌ VACUOUS | 步骤仅 echo 字面量，未验证多事件组合的 branches/paths 过滤逻辑 |
### 问题
**断言 1 — STATUS_GUARANTEED**: 步骤仅 echo 字面量，无条件失败路径。
**断言 2 — VACUOUS**: 步骤仅 echo 字面量。workflow 配置了 push+workflow_dispatch 多事件以及 branches/paths 过滤，但步骤未通过 `${{ }}` 输出事件类型或分支名来验证过滤效果。
---
