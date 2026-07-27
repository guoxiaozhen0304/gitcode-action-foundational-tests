# COMPAT-CONCUR-01-002
- **标题**: concurrency 配置越界或不支持时应给出清晰报错
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**系统拒绝不支持的 concurrency 配置，报错应明确指出错误位置和原因**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-034
通过标准：
1. 不通过无指引的原始报错
2. 报错信息包含 concurrency 关键字
3. 报错指向具体字段
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | `uses: checkout` | — | 检出代码 |
| 2 | echo hello | `echo "hello"` | — | hello |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error 无指引报错 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | error_message 含 concurrency 关键字 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
