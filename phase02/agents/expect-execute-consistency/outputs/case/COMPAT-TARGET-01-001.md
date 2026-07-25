# COMPAT-TARGET-01-001

- 标题: pull_request_target 默认 checkout 应为 base 分支而非 head 分支
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: pull_request_target 默认 checkout 应为 base 分支而非 head 分支

- [负向] 日志中显示的 SHA 不应等于 fork PR head SHA
- [正向] 日志中显示的 SHA 等于 base 分支 SHA
- [正向] workflow 能访问仓库 secrets（pull_request_target 的特权语义）

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | Y |
| 2 | print sha info | echo "Current SHA: ${{ atomgit.sha }}" echo "Base SHA: ${{ atomgit.event.pull_request.base.sha }}" e | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_logs |  |
| positive | run_logs |  |
| positive | run_status | success |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | pull_request_target |
| 身份 | untrusted_contributor |
| 触发阻塞 | 是 (untrusted_contributor trigger) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 日志中显示的 SHA 不应等于 fork PR head SHA | COVERED | negative assertion present |
| [正向] 日志中显示的 SHA 等于 base 分支 SHA | COVERED | 2 real steps, assertions present |
| [正向] workflow 能访问仓库 secrets（pull_request_target 的特权语义） | COVERED | 2 real steps, assertions present |

### 问题

无重大问题。

---
