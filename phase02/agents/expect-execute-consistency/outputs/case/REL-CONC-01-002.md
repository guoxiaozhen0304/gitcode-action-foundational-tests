# REL-CONC-01-002

- 标题: concurrency.max=6 配置应被系统拒绝
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: concurrency.max=6 配置应被系统拒绝

- [正向] YAML 校验失败或保存被拒
- [负向] 不应静默截断为 5

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 10 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | yaml_validation | rejected |
| negative | run_status | should_not_start |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] YAML 校验失败或保存被拒 | WEAK | assertions present but all steps trivial |
| [负向] 不应静默截断为 5 | COVERED | negative assertion present |

### 问题

- [正向] YAML 校验失败或保存被拒: assertions present but all steps trivial

---
