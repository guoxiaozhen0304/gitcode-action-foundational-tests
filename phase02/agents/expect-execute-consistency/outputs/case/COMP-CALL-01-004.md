# COMP-CALL-01-004

- **标题**: 未传 required secret 的 workflow_call 不应空值执行
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**未传 required secret 的 workflow_call 不应空值执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-030

通过标准：
1. [负向] 未传 required secret 时不应以空值静默进入执行 —— 断言 run_status != success
2. [负向] 不应出现以空 secret 执行副作用 —— 断言 run_logs must_contain UPLOAD_DONE（负向）
3. [非功能] 缺参报错信息应指明缺失的 secret 名 —— 🔶 LLM_DEPENDENT（跳过）

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Call reusable missing secret | `uses: ./.gitcode/workflows/reusable.yml` 无 secrets 映射 | - | 被调 workflow 若执行会输出 UPLOAD_DONE，但预期因缺参被拒绝 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | reusable-workflow-local |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success | ✅ GENUINE | uses: 调用 reusable workflow 但故意不传 required secret，平台应拒绝执行 |
| 2 | run_logs | negative | must_contain: UPLOAD_DONE | ✅ GENUINE | 负向断言：UPLOAD_DONE 不应出现（因为 workflow 不应执行到上传步骤）。uses: 真实调用 |
| 3 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |

