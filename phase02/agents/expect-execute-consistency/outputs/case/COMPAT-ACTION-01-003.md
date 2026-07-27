# COMPAT-ACTION-01-003
- **标题**: GitHub 风格 action 引用 actions/checkout@v4 的解析域探测
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**解析结果二选一且明确：成功执行或保存期明确报错并提示官方短名替代**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-045
通过标准：
1. 解析结果明确
2. 不可解析时不应无限 queued
3. 报错或文档给出 GitHub 引用到 GitCode 短名的映射指引
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Reference actions checkout v4 | `uses: actions/checkout@v4` | — | 平台解析结果（成功或报错） |
| 2 | Mark if reference executed | `echo "GITHUB_STYLE_REF_EXECUTED"` | — | GITHUB_STYLE_REF_EXECUTED |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | save_result 结局必须明确 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | run_status 不应长期排队 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | save_result 报错应含映射指引 | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
