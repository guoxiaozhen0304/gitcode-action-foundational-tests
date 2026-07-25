# USE-PERM-01-002

- 标题: 使用 GitHub 权限域命名时报错应给出 GitCode 对照表
- 维度: usability/compatibility | 优先级: P1
- 评级: 混合问题

---

## 1. 想测什么（规格）

前置条件:
  - workflow 文件位于 .gitcode/workflows/
操作步骤:
  1. 1. 在 workflow 中使用 permissions: contents: read
预期结果:
  YAML 校验报错，提示 GitCode 支持的权限域列表，并指出命名差异

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout | uses: checkout | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_status equals: COMPLETED | COVERED | 步骤含实际命令/action，失败状态取决于真实执行 |
| [nonfunctional] error_message  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 报错信息必须同时出现 contents 等 GitHub 命名与 repository/pr 等 GitCode 命名，形成对照 |

### 问题

- **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 报错信息必须同时出现 contents 等 GitHub 命名与 repository/pr 等 GitCode 命名，形成对照

---
