# COMPAT-PATHS-01-002

- 标题: paths 过滤器 301 条越界测试
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: paths 过滤器 301 条越界测试

- [负向] 超出上限的 paths 不应被静默接受
- [正向] 错误信息应明确指出 paths 数量限制

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo paths ok | echo "PATHS_301_OK" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_status | success |
| nonfunctional | error_message |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | push |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 超出上限的 paths 不应被静默接受 | COVERED | negative assertion present |
| [正向] 错误信息应明确指出 paths 数量限制 | NOT COVERED | no real steps, no assertions |

### 问题

- [正向] 错误信息应明确指出 paths 数量限制: no real steps, no assertions

---
