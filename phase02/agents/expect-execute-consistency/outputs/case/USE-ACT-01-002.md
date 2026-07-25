# USE-ACT-01-002

- 标题: 使用 actions/checkout@v4 时报错应给出迁移指引
- 维度: usability/compatibility | 优先级: P1
- 评级: 混合问题

---

## 1. 想测什么（规格）

前置条件:
  - workflow 文件位于 .gitcode/workflows/
操作步骤:
  1. 1. 在 step 中写 uses: actions/checkout@v4
预期结果:
  系统报错并提示 GitCode 官方 Action 使用短名引用

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout with github style | uses: actions/checkout@v4 | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_status equals: COMPLETED | COVERED | 步骤含实际命令/action，失败状态取决于真实执行 |
| [nonfunctional] error_message  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 报错信息必须同时出现 actions/checkout 与 checkout 对照，或给出 GitCode 官方 Action 使用短名的说明 |

### 问题

- **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 报错信息必须同时出现 actions/checkout 与 checkout 对照，或给出 GitCode 官方 Action 使用短名的说明

---
