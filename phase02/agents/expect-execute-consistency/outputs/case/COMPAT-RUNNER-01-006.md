# COMPAT-RUNNER-01-006

- 标题: Runner 未预装 Java 工具链与 GitHub 差异
- 维度: 兼容性 | 优先级: P2
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: Runner 未预装 Java 工具链与 GitHub 差异

- [正向] 系统对缺失的 Java 工具链给出明确提示
- [正向] 提示应建议替代方案（如使用自定义 Runner 或预装环境）

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Check Java | java -version || true mvn -version || true echo "done" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
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
| [正向] 系统对缺失的 Java 工具链给出明确提示 | WEAK | assertions present but all steps trivial |
| [正向] 提示应建议替代方案（如使用自定义 Runner 或预装环境） | WEAK | assertions present but all steps trivial |

### 问题

- [正向] 系统对缺失的 Java 工具链给出明确提示: assertions present but all steps trivial
- [正向] 提示应建议替代方案（如使用自定义 Runner 或预装环境）: assertions present but all steps trivial

---
