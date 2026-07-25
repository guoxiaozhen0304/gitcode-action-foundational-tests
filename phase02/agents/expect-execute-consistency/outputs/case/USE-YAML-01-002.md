# USE-YAML-01-002

- 标题: YAML 缩进错误时报错应指出具体行号与列号
- 维度: usability | 优先级: P1
- 评级: 混合问题

---

## 1. 想测什么（规格）

前置条件:
  - workflow 文件位于 .gitcode/workflows/
操作步骤:
  1. 1. 提交一个 steps 缩进错误的 workflow
预期结果:
  报错包含具体的行号、列号，指出缩进错误位置

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| - | (无步骤) | - | - |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_status equals: COMPLETED | UNCOVERED | [负向] 未找到可能导致非成功状态的步骤，单次调度无法证明 !=success |
| [nonfunctional] error_message  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 报错信息必须同时包含字段名、所在行号、正确写法示例三项中的至少两项 |

### 问题

- **断言 1 - UNVERIFIABLE**: [负向] 未找到可能导致非成功状态的步骤，单次调度无法证明 !=success
- **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 报错信息必须同时包含字段名、所在行号、正确写法示例三项中的至少两项

---
