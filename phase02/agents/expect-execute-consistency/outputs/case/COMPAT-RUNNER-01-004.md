# COMPAT-RUNNER-01-004

- 标题: 自定义特征标签不被支持时应给出可用标签列表
- 维度: 兼容性 | 优先级: P2
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 自定义特征标签不被支持时应给出可用标签列表

- [正向] 报错信息说明标签不匹配
- [正向] 报错给出可用标签列表或标签格式指引

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo hello | echo "hello" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | error_message |  |
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
| [正向] 报错信息说明标签不匹配 | WEAK | assertions present but all steps trivial |
| [正向] 报错给出可用标签列表或标签格式指引 | WEAK | assertions present but all steps trivial |

### 问题

- [正向] 报错信息说明标签不匹配: assertions present but all steps trivial
- [正向] 报错给出可用标签列表或标签格式指引: assertions present but all steps trivial

---
