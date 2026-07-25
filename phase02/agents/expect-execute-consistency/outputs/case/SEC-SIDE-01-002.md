# SEC-SIDE-01-002

- 标题: Secret 不经 artifact 侧信道绕过脱敏外泄
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
操作步骤:
  1. 1. 提交一个 workflow，将 secret 写入文件并上传为 artifact
  2. 2. 触发 workflow 并下载 artifact 检查内容
预期结果:
  - Artifact 中不应包含 secret 明文
  - 若 artifact 包含 secret，应被拦截或遮蔽

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Write secret to file | echo "token=${{ secrets.DEPLOY_TOKEN }}" > secret.txt  | 是 |
| 2 | Upload artifact | uses: upload-artifact | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] artifact_content must_not_contain_secret: DEPLOY_TOKEN | COVERED | target=artifact_content 的断言可由执行结果验证 |
| [positive] run_status equals: blocked_or_masked | COVERED | 步骤含实际命令或 action，运行状态取决于真实执行结果 |

### 问题

- 无

---
