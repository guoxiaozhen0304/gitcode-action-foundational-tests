# USE-UNKN-01-002

- 标题: 未知字段报错若识别为 GitHub 特有应追加迁移提示
- 维度: usability/compatibility | 优先级: P1
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - workflow 文件位于 .gitcode/workflows/
操作步骤:
  1. 1. 在 workflow 中使用 GitHub 特有的 jobs.<id>.container 字段
预期结果:
  报错除指出字段不支持外，还提示该字段为 GitHub Actions 特有

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | step | echo "hello"  | 否 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [nonfunctional] error_message  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 对未知字段的提示必须包含字段名和不支持/unknown 字样；若能识别该字段为 GitHub 特有如 container，提示中应追加该字段为 GitHub A |

### 问题

- **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 对未知字段的提示必须包含字段名和不支持/unknown 字样；若能识别该字段为 GitHub 特有如 container，提示中应追加该字段为 GitHub A
- **整体空洞**: 所有步骤均无实质逻辑（仅 echo/无 action/无 if 条件）

---
