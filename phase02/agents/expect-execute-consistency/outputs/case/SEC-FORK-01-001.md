# SEC-FORK-01-001

- 标题: fork PR 触发 pull_request 时不可读取项目 secrets
- 维度: 安全性 | 优先级: P0
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
  - 存在一个来自外部 fork 的 PR
操作步骤:
  1. 1. 以 fork 贡献者身份提交一个引用 secrets.DEPLOY_TOKEN 的 workflow
  2. 2. 在 fork PR 场景下触发该 workflow
预期结果:
  - 系统阻止 fork PR 访问 DEPLOY_TOKEN，引用时返回空值或安全报错
  - 运行日志中不出现 DEPLOY_TOKEN 明文

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Try access secret | echo "secret value is ${{ secrets.DEPLOY_TOKEN }}"  | 是 |
| 2 | Print env | env \| grep DEPLOY_TOKEN \|\| echo "not found"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: DEPLOY_TOKEN | TRIGGER_BLOCKED | 触发事件 pull_request 无法通过 dispatch API 调度 |
| [positive] run_status equals: completed_or_blocked | TRIGGER_BLOCKED | 触发事件 pull_request 无法通过 dispatch API 调度 |

### 问题

- **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request 无法通过 dispatch API 调度
- **断言 2 - TRIGGER_BLOCKED**: 触发事件 pull_request 无法通过 dispatch API 调度

---
