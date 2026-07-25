# USE-PATH-01-001

- 标题: paths 300 文件上限在文档与行为中一致且明示
- 维度: usability/compatibility | 优先级: P1
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - 文档版本为 2026-07-20 抓取版本
操作步骤:
  1. 1. 检查 configure-triggers.md 中 paths 说明
  2. 2. 触发一次变更文件数超过 300 的 push
预期结果:
  文档在显眼位置标注 300 文件上限；超出时调试日志有提示

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
| [nonfunctional] documentation  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 文档 configure-triggers.md 中 paths/paths-ignore 说明必须在首段或独立的注意块中写明匹配前 300 个变更文件 |

### 问题

- **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 文档 configure-triggers.md 中 paths/paths-ignore 说明必须在首段或独立的注意块中写明匹配前 300 个变更文件

---
