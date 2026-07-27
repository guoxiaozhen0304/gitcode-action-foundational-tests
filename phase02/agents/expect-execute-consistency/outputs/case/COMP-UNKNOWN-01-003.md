# COMP-UNKNOWN-01-003
- **标题**: 未声明 select 的 stage 与 job 默认被执行
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**未声明 select 的 stage/job 默认执行（与全部官方示例一致）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-021
通过标准：
1. 未声明 select 的 job 全部执行并输出标记
2. 不应出现未声明 select 的 job 被默认跳过
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark alpha | `echo "NO_SELECT_JOB_RAN"` | — | NO_SELECT_JOB_RAN |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status=success | positive | — | ⚠️ STATUS_GUARANTEED | 全步骤仅 echo，无 if:/uses:/${{ }}/真实命令，成功无条件成立 |
| 2 | must_contain NO_SELECT_JOB_RAN | positive | — | ❌ VACUOUS | 步骤唯一动作即 echo 该字符串，无任何条件分支或平台行为验证 |
### 问题
两个断言均不能验证平台行为：成功无条件成立，日志输出仅为自证预言式 echo。select 字段的实际行为未被测试。
---
