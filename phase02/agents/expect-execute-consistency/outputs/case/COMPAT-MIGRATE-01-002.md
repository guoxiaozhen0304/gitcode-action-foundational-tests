# COMPAT-MIGRATE-01-002

- 标题: GitHub 风格 run-name 语法迁移报错应给出可操作指引
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: GitHub 风格 run-name 语法迁移报错应给出可操作指引

- [负向] 不通过无指引的原始报错
- [正向] 报错信息包含 `run-name` 不支持及替代方案
- [正向] 若含 `github.*` 上下文，报错提示改用 `atomgit.*`

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | Y |
| 2 | echo hello | echo "hello" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | validation_error |  |
| positive | error_message |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 不通过无指引的原始报错 | COVERED | negative assertion present |
| [正向] 报错信息包含 `run-name` 不支持及替代方案 | COVERED | 1 real steps, assertions present |
| [正向] 若含 `github.*` 上下文，报错提示改用 `atomgit.*` | COVERED | 1 real steps, assertions present |

### 问题

无重大问题。

---
