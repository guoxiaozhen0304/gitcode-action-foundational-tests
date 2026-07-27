# COMP-WFLOW-01-063
- **标题**: workflow concurrency 并发控制字段验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**concurrency 配置被平台接受，max >= 1，exceed-action 为 QUEUE 或 IGNORE**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-063
通过标准：
1. 合法 concurrency 配置通过校验
2. max 小于 1 被拒绝
3. preemption.events 含非 mr_id 被拒绝
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo ok | `echo "concurrency_ok"` | — | concurrency_ok |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status=success | positive | — | ⚠️ STATUS_GUARANTEED | 全步骤仅 echo，无 if:/uses:/${{ }}/真实命令 |
| 2 | must_contain concurrency_ok | positive | — | ❌ VACUOUS | 步骤唯一动作即 echo 该字符串，不验证并发控制行为 |
### 问题
concurrency 的配置校验仅靠 echo 标记，max<1 或 events 越界等负向验证完全缺失。
---
