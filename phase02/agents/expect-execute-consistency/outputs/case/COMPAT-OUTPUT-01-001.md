# COMPAT-OUTPUT-01-001

- 标题: 跨 Job 引用未声明 output 时返回空值的差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: 跨 Job 引用未声明 output 时返回空值的差异

- [正向] 跨 Job 引用未声明 output 时不导致 workflow 崩溃
- [正向] 返回值与 GitHub 行为一致（空字符串）

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Set output | echo "declared_key=value_a" >> $ATOMGIT_OUTPUT | Y |
| 2 | Echo outputs | echo "declared=${{ needs.job-a.outputs.declared_key }}" echo "undeclared=${{ needs.job-a.outputs.und | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | success |
| positive | run_logs |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 跨 Job 引用未声明 output 时不导致 workflow 崩溃 | COVERED | 2 real steps, assertions present |
| [正向] 返回值与 GitHub 行为一致（空字符串） | COVERED | 2 real steps, assertions present |

### 问题

无重大问题。

---
