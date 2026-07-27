# COMPAT-ENV-01-005
- **标题**: RUNNER_* 系列环境变量在 GitCode Runner 上的注入情况探测
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**六个 RUNNER_* 变量取值逐一确定并记录，不注入的列入差异清单**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-044
通过标准：
1. 六个 RUNNER_* 变量取值逐一确定
2. 不应出现部分有值部分为空的不一致
3. 缺失变量清单进入迁移对照表
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo RUNNER identification vars | `echo "RUNNER_OS=[$RUNNER_OS]" ... RUNNER_NAME` | — | RUNNER_OS=[...], RUNNER_ARCH=[...], RUNNER_NAME=[...] |
| 2 | Echo RUNNER path and capability vars | `echo "RUNNER_TEMP=[$RUNNER_TEMP]" ... PROBE_DONE` | — | RUNNER_TEMP=[...], RUNNER_TOOL_CACHE=[...], RUNNER_ENVIRONMENT=[...], PROBE_DONE |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | must_contain PROBE_DONE | positive | — | ✅ GENUINE | 步骤使用多个 shell 环境变量（RUNNER_*），真实验证平台注入行为 |
| 2 | run_logs 逐字记录 RUNNER_* 值 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 3 | run_logs 半套兼容检测 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
