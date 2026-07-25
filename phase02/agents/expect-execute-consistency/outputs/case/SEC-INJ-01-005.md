# SEC-INJ-01-005

- 标题: 表达式求值必须防止双重模板渲染（二次求值）
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库支持表达式求值
操作步骤:
  1. 1. 提交一个 workflow，在输入中包含模板语法字符（如 {{ 1 + 1 }}）
  2. 2. 触发 workflow 并查看运行日志
预期结果:
  - 外层 ${{ }} 求值结果中的模板语法字符应被转义
  - 不再触发内层模板引擎求值

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Pass template syntax | echo "Input: ${{ '{{ 1 + 1 }}' }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: 2 | UNCOVERED | 期望值 [2] 未在任何步骤输出中找到 |
| [positive] run_logs equals: template_chars_escaped | UNCOVERED | 期望值 [template_chars_escaped] 未在任何步骤输出中找到 |

### 问题

- **断言 1 - MISSING_SOURCE**: 期望值 [2] 未在任何步骤输出中找到
- **断言 2 - MISSING_SOURCE**: 期望值 [template_chars_escaped] 未在任何步骤输出中找到

---
