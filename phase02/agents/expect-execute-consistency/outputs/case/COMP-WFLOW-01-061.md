# COMP-WFLOW-01-061
- **标题**: workflow name 与 on 字段必填与类型验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**name 为可选但 on 为必填，on 必须为 map**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-061
通过标准：
1. 含 name 的 workflow 被正确显示
2. on 为 map 时 workflow 可被触发
3. on 为数组时平台拒绝
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo ok | `echo "workflow_ok"` | — | workflow_ok |
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
| 2 | must_contain workflow_ok | positive | — | ❌ VACUOUS | 步骤唯一动作即 echo 该字符串，无任何平台行为验证 |
### 问题
on 为数组格式的负向验证点完全缺失（YAML 中 on 为 map 格式但未测试数组格式被拒绝的场景）。
---
