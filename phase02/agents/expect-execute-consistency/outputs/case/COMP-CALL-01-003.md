# COMP-CALL-01-003

- **标题**: 本地路径 workflow_call 完整 secrets 映射正常执行
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**本地路径 workflow_call 完整 secrets 映射正常执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-030

通过标准：
1. [正向] 本地路径调用正常执行，被调 workflow 输出完成标记 —— 断言 run_logs must_contain REUSABLE_OK、run_status=success
2. [正向/记录] 本地路径解析基准逐字记录 —— 🔶 LLM_DEPENDENT

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Call local reusable workflow | `uses: ./.gitcode/workflows/reusable.yml` + secrets: OBS_AK, OBS_SK | - | 被调 workflow 内部输出 REUSABLE_OK |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | reusable-workflow-local |
| Secrets | [OBS_AK, OBS_SK] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | uses: 调用本地路径 reusable workflow 并映射 secrets，真实被测行为 |
| 2 | run_logs | positive | must_contain: REUSABLE_OK | ✅ GENUINE | REUSABLE_OK 来自被调 workflow 内部真实执行输出 |

