# COMPAT-MIGRATE-01-001
- **标题**: GitHub 风格 permissions 块迁移报错应给出可操作指引
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**GitHub 风格 permissions 块迁移报错应给出可操作指引**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-031
通过标准：
1. 系统拒绝该 workflow（GitCode 不支持 permissions 块）
2. 报错信息应明确指出 permissions 字段不被支持
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | — | — |
| 2 | echo hello | `echo "hello"` | — | "hello" |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | permissions 拒绝行为由 LLM 判定 |
| 2 | error_message eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 报错信息质量由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
