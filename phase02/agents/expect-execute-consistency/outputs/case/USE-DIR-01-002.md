# USE-DIR-01-002

- 标题: .github/workflows/ 下 workflow 未被识别时应给出目录差异提示
- 维度: usability | 优先级: P1
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - 仓库同时存在 .github/workflows/ 和 .gitcode/workflows/
  - 前者含 workflow 后者为空
操作步骤:
  1. 1. 将 workflow 文件误放到 .github/workflows/ 目录
  2. 2. 推送代码触发 push 事件
预期结果:
  系统在某处（运行页面、日志或校验信息）提示 .gitcode/workflows/ 为正确目录，而非静默忽略

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
| [nonfunctional] system_message  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 提示信息必须同时包含 .github/workflows 与 .gitcode/workflows 对照字样，并指明 GitCode 使用 .gitcode/w |

### 问题

- **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 提示信息必须同时包含 .github/workflows 与 .gitcode/workflows 对照字样，并指明 GitCode 使用 .gitcode/w

---
