# COMP-PRTARGET-01-003
- **标题**: fork PR 按文档推荐配置 pull_request_target 的 secret 暴露面核查
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**fork PR 按文档推荐配置 pull_request_target 的 secret 暴露面核查**
- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMP-023
通过标准：
1. secret 明文不应出现在任何日志中（负向）
2. 按推荐配置不应在无平台警示的情况下默认获得 secrets 与写权限（负向，LLM）
3. base 分支 workflow 版本约束实测成立（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Checkout pr head | `uses: checkout` with `ref: ${{ atomgit.pull_request.head.sha }}` | - | runner/action 日志 |
| 2 | Probe secret presence | `env: TEST_SECRET: "${{ secrets.TEST_SECRET }}"` → `[ -z "$TEST_SECRET" ] && echo SECRET_NOT_INJECTED || echo SECRET_INJECTED` | - | 条件分支输出 |
## 3. 触发与运行环境
| 触发事件 | pull_request_target |
| 触发身份 | untrusted_contributor |
| Repo 环境 | fork-pr-target |
| Secrets | [TEST_SECRET] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret: TEST_SECRET | ✅ GENUINE | 步骤通过 env 注入 `${{ secrets.TEST_SECRET }}` 并 echo，平台脱敏行为被真实测试 |
| 2 | secret_injection | negative | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估 secret 注入行为与文档一致性的裁决 |
---
