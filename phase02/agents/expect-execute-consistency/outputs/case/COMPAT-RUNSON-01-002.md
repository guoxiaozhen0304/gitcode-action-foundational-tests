# COMPAT-RUNSON-01-002

- 标题: runs-on 标签体系——单标签字符串应报错
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: runs-on 标签体系——单标签字符串应报错

- [负向] 单标签字符串格式在解析/校验阶段报错
- [正向] 错误信息应明确说明需使用数组格式
- [负向] 不应静默调度到不匹配标签的 Runner

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) should not reach here | echo "RUNSON_STRING_ACCEPTED" | - |

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
| [负向] 单标签字符串格式在解析/校验阶段报错 | COVERED | negative assertion present |
| [正向] 错误信息应明确说明需使用数组格式 | WEAK | assertions present but all steps trivial |
| [负向] 不应静默调度到不匹配标签的 Runner | COVERED | negative assertion present |

### 问题

- [正向] 错误信息应明确说明需使用数组格式: assertions present but all steps trivial

---
