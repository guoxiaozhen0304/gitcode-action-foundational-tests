# COMPAT-TOKEN-01-003

- 标题: GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN

- [负向] GITHUB_TOKEN 不等于 ATOMGIT_TOKEN
- [正向] GITHUB_TOKEN 为空或未定义
- [负向] 不通过静默映射导致用户误用 GITHUB_TOKEN

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Compare tokens | echo "GITHUB_TOKEN=$GITHUB_TOKEN" echo "ATOMGIT_TOKEN=$ATOMGIT_TOKEN" echo "done" | - |
| 2 | Reference secrets GITHUB_TOKEN | echo "secret_github_token=${{ secrets.GITHUB_TOKEN }}" echo "done" | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_logs |  |
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
| [负向] GITHUB_TOKEN 不等于 ATOMGIT_TOKEN | COVERED | negative assertion present |
| [正向] GITHUB_TOKEN 为空或未定义 | COVERED | 1 real steps, assertions present |
| [负向] 不通过静默映射导致用户误用 GITHUB_TOKEN | COVERED | negative assertion present |

### 问题

无重大问题。

---
