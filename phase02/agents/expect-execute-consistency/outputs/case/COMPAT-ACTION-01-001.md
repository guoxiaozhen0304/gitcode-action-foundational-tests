# COMPAT-ACTION-01-001
- **标题**: checkout 短名等价性——ref 参数支持
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**uses: checkout 配合 ref 参数可正确检出指定分支，裸插件名写法与 GitHub 全名写法等价**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-024
通过标准：
1. checkout 步骤成功完成
2. 检出后的代码与指定分支一致
3. 不应因使用裸插件名而解析失败
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout with ref main | `uses: checkout with: ref: main` | — | 检出代码到工作目录 |
| 2 | verify branch is main | `git rev-parse ... if/else echo CHECKOUT_REF_OK/FAILED; exit 1` | — | CHECKOUT_REF_OK 或 CHECKOUT_REF_FAILED |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status=completed_success | positive | — | ✅ GENUINE | 步骤含 uses: checkout 动作和 real git 命令，if 条件及 exit 1 |
| 2 | run_logs CHECKOUT_REF_OK | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | run_logs 不应出现 CHECKOUT_REF_FAILED | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 4 | workflow_parse 不应因裸插件名失败 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
