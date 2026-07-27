# COMPAT-LIMIT-01-001
- **标题**: 单次推送多个 tag 的事件生成上限行为
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**单次推送多个 tag 的事件生成上限行为**
- 触发事件: `tag` (模拟 4 个 tag)
- 规格引用: INTENT-COMPAT-052
通过标准：
1. 推送 4 个 tag 的触发行为确定并与文档比对
2. 超限场景不应静默丢事件
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark tag triggered run | `echo "TAG_RUN_REF=${{ atomgit.ref }}"` | — | TAG_RUN_REF=<ref> |
## 3. 触发与运行环境
| 触发事件 | tag (params: tag_count=4, tags=v0.0.1~v0.0.4) |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | 运行记录数由 LLM 判定 |
| 2 | run_list eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | 静默丢弃行为由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT；target=run_list 的验证依赖事后查询运行数量
---
