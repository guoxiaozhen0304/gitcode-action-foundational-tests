# COMPAT-NEST-01-001
- **标题**: workflow_call 嵌套层数 - 2 层正常执行
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**workflow_call 嵌套层数 - 2 层正常执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-015
通过标准：
1. 2 层 workflow_call 嵌套应正常执行
2. 运行状态应为成功
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | call-level2 | uses: ./.gitcode/workflows/level2.yml | — | 调用 level2 可复用 workflow |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | reusable-workflow |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | positive | — | ✅ GENUINE | uses: 调用另一个 workflow 文件，2 层嵌套能否成功取决于平台对 reusability 和嵌套的实际支持 |
---
