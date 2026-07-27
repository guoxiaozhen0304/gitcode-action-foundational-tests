# COMP-WFLOW-01-065
- **标题**: workflow post 后处理阶段字段验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**post 阶段在 workflow 结束后执行，run_always 为 true 时无论成败都执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-061
通过标准：
1. post 步骤在成功时执行
2. run_always true 时失败 workflow 仍执行 post
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Main step | `echo "main_done"` | — | main_done |
| 2 | Post notification | `echo "post_done"` | — | post_done |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | must_contain main_done | positive | — | ❌ VACUOUS | 步骤仅 echo，不验证任何后处理行为 |
| 2 | must_contain post_done | positive | — | ❌ VACUOUS | 步骤仅 echo，不验证 run_always: true 在失败时是否仍执行 |
### 问题
run_always 失败场景完全未测试（主步骤无条件成功），无法验证 post 在失败时是否仍执行。
---
