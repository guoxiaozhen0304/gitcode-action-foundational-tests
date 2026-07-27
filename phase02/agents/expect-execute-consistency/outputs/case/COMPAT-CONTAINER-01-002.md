# COMPAT-CONTAINER-01-002
- **标题**: container 自定义镜像被拒绝时应给出替代指引
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**系统拒绝 container 自定义镜像，报错应说明限制并给出替代方案**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-001
通过标准：
1. 报错信息说明 container 自定义镜像限制
2. 报错给出替代方案
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo hello | `echo "hello"` | — | hello（若解析通过） |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error 说明限制 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | error_message 替代方案 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
