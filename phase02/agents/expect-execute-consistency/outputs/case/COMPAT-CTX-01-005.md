# COMPAT-CTX-01-005
- **标题**: atomgit 缺位字段（job/run_attempt/triggering_actor/ref_protected）求值行为探测
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**四个缺位字段的求值行为逐一确定并记录，缺失字段清单进入迁移对照文档**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-040
通过标准：
1. 四个缺位字段的求值行为逐一确定并记录
2. 缺失字段清单进入迁移对照文档
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo job and run attempt | `echo "CTX_JOB=${{ atomgit.job }}" ... CTX_RUN_ATTEMPT` | — | CTX_JOB=..., CTX_RUN_ATTEMPT=... |
| 2 | Echo actor related fields | `echo "CTX_TRIGGERING_ACTOR=${{ atomgit.triggering_actor }}" ...` | — | CTX_TRIGGERING_ACTOR=... |
| 3 | Compare with env side | `echo "ENV_RUN_ATTEMPT=$ATOMGIT_RUN_ATTEMPT" && echo "PROBE_DONE"` | — | ENV_RUN_ATTEMPT=..., PROBE_DONE |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | must_contain PROBE_DONE | positive | — | ✅ GENUINE | 步骤使用 ${{ }} 表达式及 shell 环境变量，有真实平台行为 |
| 2 | run_logs 逐字段记录 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
