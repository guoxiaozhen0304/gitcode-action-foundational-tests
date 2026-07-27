# COMPAT-PERM-01-005
- **标题**: permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-030
通过标准：
1. 读操作成功
2. 写操作被平台拒绝
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Try read with token | curl 读取 /user API，Authorization: Bearer $ATOMGIT_TOKEN | — | HTTP status code |
| 2 | Try write with token | curl POST 创建 repo，Authorization: Bearer $ATOMGIT_TOKEN | — | HTTP status code |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 读操作返回 200 由 LLM 判定 |
| 2 | run_logs eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 写操作返回 403/401 由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
