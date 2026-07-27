# COMP-RUNNER-01-082
- **标题**: flow-mapping 写法 runs-on 的处理结果裁定
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**flow-mapping 写法 runs-on 的处理结果裁定**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-029
通过标准：
1. flow-mapping 写法的实际处理逐字记录（正向/记录）
2. 不应语法被接受但调度到非预期 Runner 且无提示（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print runner identity | `echo "FLOW_MAPPING_RUNNER_RAN"` | - | FLOW_MAPPING_RUNNER_RAN |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | save_validation | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估平台校验期是否报错或等价解析 flow-mapping 写法 |
| 2 | runner_mismatch | negative | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估是否出现非预期调度 |
---
