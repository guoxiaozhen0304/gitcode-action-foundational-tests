# COMP-STEP-01-069
- **标题**: step 必填与核心字段 name run uses 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**step 必填与核心字段 name run uses 验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-069
通过标准：
1. name + run 步骤正常执行（正向）
2. name + uses 步骤正常执行（正向）
3. step name 含非法字符被拒绝（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Run step | `echo "run_ok"` | - | run_ok |
| 2 | Uses step | `uses: checkout` | - | action 内部日志 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: run_ok | ❌ VACUOUS | 步骤仅 echo 字面量，未验证 name/run 字段的实际功能 |
| 2 | run_status | positive | equals: success | ✅ GENUINE | 步骤含 uses: checkout action，有实质平台行为 |
### 问题
**断言 1 — VACUOUS**: 步骤仅 echo 了字面量 "run_ok"，该步骤虽然测试了 name + run 字段的组合接受性，但 echo 输出本身不区分 name/run 字段是否有缺陷。规格中提到"step name 含非法字符被拒绝"的验证点也未在 YAML 中实现。
---
