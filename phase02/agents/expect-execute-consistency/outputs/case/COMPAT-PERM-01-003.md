# COMPAT-PERM-01-003

- 标题: permissions 命名差异——GitHub contents 权限项应报错
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: permissions 命名差异——GitHub contents 权限项应报错

- [负向] 使用 `contents` 时 workflow 解析/校验阶段应报错
- [正向] 错误信息应明确提示 unknown property 或类似说明
- [负向] 不应静默忽略导致实际权限与开发者预期不符

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) attempt clone | uses: checkout | Y |
| 2 | (TC) should not reach | echo "CONTENTS_PERM_ACCEPTED" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | workflow_parse |  |
| positive | run_logs |  |
| negative | run_logs |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 使用 `contents` 时 workflow 解析/校验阶段应报错 | COVERED | negative assertion present |
| [正向] 错误信息应明确提示 unknown property 或类似说明 | COVERED | 1 real steps, assertions present |
| [负向] 不应静默忽略导致实际权限与开发者预期不符 | COVERED | negative assertion present |

### 问题

无重大问题。

---
