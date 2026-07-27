# COMPAT-ACTIONDEV-01-002
- **标题**: action 运行时 runs.using 类型覆盖（node16/composite/docker/node20）探测
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**GitCode 支持的 runs.using 取值全集得到确定结论**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-048
通过标准：
1. runs.using node16 正常执行
2. composite/docker/node20 得到确定响应
3. 不支持的 using 类型不出现运行期模糊失败
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Invoke local node16 action | `uses: ./.gitcode/actions/probe-node16` | — | 本地 action 执行结果 |
| 2 | Invoke local composite action | `uses: ./.gitcode/actions/probe-composite` | — | 本地 action 执行结果 |
| 3 | Invoke local docker action | `uses: ./.gitcode/actions/probe-docker` | — | 本地 action 执行结果 |
| 4 | Invoke local node20 action | `uses: ./.gitcode/actions/probe-node20` | — | 本地 action 执行结果 |
| 5 | Mark probe complete | `echo "USING_PROBE_DONE"` | — | USING_PROBE_DONE |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-local-actions |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs 各 using 类型响应 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | run_logs 运行期模糊失败 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | run_logs 运行时清单记录 | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
