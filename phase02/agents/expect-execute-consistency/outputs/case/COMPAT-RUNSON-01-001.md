# COMPAT-RUNSON-01-001

- 标题: runs-on 标签体系——三段式数组正常匹配
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: runs-on 标签体系——三段式数组正常匹配

- [正向] 工作流成功启动并执行
- [正向] 日志中显示 Runner 标签与声明一致
- [负向] 不应因数组格式而被平台拒绝解析

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) echo runner info | echo "RUNSON_ARRAY_OK" echo "Runner labels: dedicate-hosted x64 large" | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | completed_success |
| positive | run_logs |  |
| negative | workflow_parse |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 工作流成功启动并执行 | WEAK | assertions present but all steps trivial |
| [正向] 日志中显示 Runner 标签与声明一致 | WEAK | assertions present but all steps trivial |
| [负向] 不应因数组格式而被平台拒绝解析 | COVERED | negative assertion present |

### 问题

- [正向] 工作流成功启动并执行: assertions present but all steps trivial
- [正向] 日志中显示 Runner 标签与声明一致: assertions present but all steps trivial

---
