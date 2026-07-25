# SEC-WCMD-01-003

- 标题: ATOMGIT_ENV 不被不可信输入污染提权
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库支持 workflow 环境变量注入
操作步骤:
  1. 1. 提交一个 workflow，将含换行/协议控制字符的不可信值写入 ATOMGIT_ENV
  2. 2. 触发 workflow 并检查后续 step 的环境变量
预期结果:
  - 不可信值写入 ATOMGIT_ENV 时不应注入额外环境变量
  - 多行/换行注入被安全处理

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| - | (无步骤) | - | - |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: injection succeeded | UNCOVERED | 期望值 [injection succeeded] 未在任何步骤输出中找到 |
| [positive] run_logs equals: no injection | UNCOVERED | 期望值 [no injection] 未在任何步骤输出中找到 |

### 问题

- **断言 1 - MISSING_SOURCE**: 期望值 [injection succeeded] 未在任何步骤输出中找到
- **断言 2 - MISSING_SOURCE**: 期望值 [no injection] 未在任何步骤输出中找到

---
