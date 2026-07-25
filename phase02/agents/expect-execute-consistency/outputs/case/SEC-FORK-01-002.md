# SEC-FORK-01-002

- 标题: fork PR 中 secrets 引用返回空值且 job 不崩溃
- 维度: 安全性 | 优先级: P0
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret API_KEY
  - 存在一个来自外部 fork 的 PR
操作步骤:
  1. 1. 以 fork 贡献者身份提交一个将 secrets.API_KEY 注入环境变量的 workflow
  2. 2. 在 fork PR 场景下触发该 workflow
预期结果:
  - secrets.API_KEY 返回空字符串，环境变量未设置
  - job 正常完成，不因 secret 不可访问而失败

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Check env empty | if [ -z "$API_KEY" ]; then   echo "API_KEY is empty as expected" else   echo "API_KEY is not empty"   exit 1 fi  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: API_KEY | TRIGGER_BLOCKED | 触发事件 pull_request 无法通过 dispatch API 调度 |
| [positive] run_status equals: success | TRIGGER_BLOCKED | 触发事件 pull_request 无法通过 dispatch API 调度 |

### 问题

- **断言 1 - TRIGGER_BLOCKED**: 触发事件 pull_request 无法通过 dispatch API 调度
- **断言 2 - TRIGGER_BLOCKED**: 触发事件 pull_request 无法通过 dispatch API 调度

---
