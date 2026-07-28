# COMPAT-ENV-01-004
- **标题**: ATOMGIT_ENV 覆写系统默认变量的防护（对齐 GitHub 同名禁止）   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证通过 ATOMGIT_ENV 环境文件覆写 ATOMGIT_WORKSPACE 被拒绝/忽略，普通自定义变量正常传递。
## 做了什么
workflow_dispatch 触发，step1 记录原始 WORKSPACE，step2 经 env 文件写入 ATOMGIT_WORKSPACE=/tmp/override-probe 和 CUSTOM_PROBE=custom-ok，step3 读取两者当前值并 echo `PROBE_DONE`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；WORKSPACE_NOW 不应等于污染值 |
| 2 | run_logs | positive | must_contain: CUSTOM_NOW=custom-ok | GENUINE→COVERED | 步骤中真实写入 env 文件后读取，有 `$ATOMGIT_ENV` + shell 变量 |
| 3 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；覆写尝试应有警告/拒绝痕迹 |
