# SEC-SIDE-01-001

- 标题: Secret 不经 output 侧信道绕过脱敏外泄
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret API_KEY
操作步骤:
  1. 1. 提交一个 workflow，将 secret 写入 ATOMGIT_OUTPUT
  2. 2. 触发 workflow 并检查 output 内容
预期结果:
  - Secret 明文不应以未遮蔽形式出现在 job output 中
  - output 中 secret 值应为 *** 或被拦截

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Write secret to output | echo "result=${{ secrets.API_KEY }}" >> $ATOMGIT_OUTPUT  | 是 |
| 2 | Check output masked | echo "output is ${{ steps.step1.outputs.result }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: API_KEY | COVERED | 步骤使用了 API_KEY，平台需在日志中脱敏 |
| [negative] step_output must_not_contain_secret: API_KEY | COVERED | target=step_output 的断言可由执行结果验证 |

### 问题

- 无

---
