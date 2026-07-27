# COMPAT-EVENT-01-001
- **标题**: GitHub 全量事件集中不受支持事件（release 等）的降级方式
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**平台在保存/解析阶段明确报错，报错信息包含事件不受支持的说明与受支持事件清单**
- 触发事件: `manual`
- 规格引用: INTENT-COMPAT-037
通过标准：
1. 含不受支持事件的 workflow 不应被静默保存
2. 保存/解析期报错包含事件不受支持说明
3. 报错应指明为 GitCode 能力差异
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Should never run on unsupported event | `echo "RELEASE_JOB_RAN"` | — | RELEASE_JOB_RAN（不应出现） |
## 3. 触发与运行环境
| 触发事件 | manual |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | save_result 不应静默保存 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | save_result 明确报错 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | save_result 报错可理解性 | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
