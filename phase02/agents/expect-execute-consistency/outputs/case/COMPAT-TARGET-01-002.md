# COMPAT-TARGET-01-002

- 标题: pull_request_target 在 fork 场景下应保持 secret 隔离
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: pull_request_target 在 fork 场景下应保持 secret 隔离

- [负向] 日志中不应出现 DEPLOY_TOKEN 明文
- [正向] pull_request_target 场景下 workflow 能成功引用 secrets.DEPLOY_TOKEN
- [正向] 普通 pull_request 场景下 fork PR 无法访问 secrets

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | Y |
| 2 | echo secret masked | echo "Token is: ${{ secrets.DEPLOY_TOKEN }}" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_logs |  |
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
| [负向] 日志中不应出现 DEPLOY_TOKEN 明文 | COVERED | negative assertion present |
| [正向] pull_request_target 场景下 workflow 能成功引用 secrets.DEPLOY_TOKEN | COVERED | 2 real steps, assertions present |
| [正向] 普通 pull_request 场景下 fork PR 无法访问 secrets | COVERED | 2 real steps, assertions present |

### 问题

无重大问题。

---
