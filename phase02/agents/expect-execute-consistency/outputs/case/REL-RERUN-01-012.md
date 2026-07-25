# REL-RERUN-01-012

- 标题: rerun 越界值——尝试第 4 次重新运行应被系统拒绝
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: rerun 越界值——尝试第 4 次重新运行应被系统拒绝

- [正向] 第 4 次 rerun 按钮不可用或点击后报错
- [正向] 错误信息含最多 3 次或类似提示

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | sleep step | sleep 5 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | rerun_request | rejected |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 第 4 次 rerun 按钮不可用或点击后报错 | WEAK | assertions present but all steps trivial |
| [正向] 错误信息含最多 3 次或类似提示 | WEAK | assertions present but all steps trivial |

### 问题

- [正向] 第 4 次 rerun 按钮不可用或点击后报错: assertions present but all steps trivial
- [正向] 错误信息含最多 3 次或类似提示: assertions present but all steps trivial

---
