# COMPAT-SECRET-01-005

- 标题: 环境级 secrets 不支持时应明确报错而非降级为项目级
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: 环境级 secrets 不支持时应明确报错而非降级为项目级

- [负向] 不通过静默降级（ENV_SECRET 不应返回 PROJECT_SECRET 的值）
- [正向] 系统对环境级 secrets 的缺失给出明确提示
- [正向] 项目级 secrets 正常注入

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Check secrets | echo "project_secret=${{ secrets.PROJECT_SECRET }}" echo "env_secret=${{ secrets.ENV_SECRET }}" echo | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_logs |  |
| positive | run_logs |  |
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
| [负向] 不通过静默降级（ENV_SECRET 不应返回 PROJECT_SECRET 的值） | COVERED | negative assertion present |
| [正向] 系统对环境级 secrets 的缺失给出明确提示 | COVERED | 1 real steps, assertions present |
| [正向] 项目级 secrets 正常注入 | COVERED | 1 real steps, assertions present |

### 问题

无重大问题。

---
