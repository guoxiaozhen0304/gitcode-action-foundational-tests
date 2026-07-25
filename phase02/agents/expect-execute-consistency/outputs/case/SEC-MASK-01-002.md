# SEC-MASK-01-002

- 标题: Secret 值在 step summary 和错误堆栈中必须被脱敏
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret API_KEY
操作步骤:
  1. 1. 提交一个 workflow，将 secrets.API_KEY 写入 ATOMGIT_STEP_SUMMARY
  2. 2. 触发 workflow 并查看 step summary 与日志
预期结果:
  - step summary 中 API_KEY 的原值被替换为 ***
  - 若步骤失败产生堆栈，堆栈中亦不应出现原值

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Write secret to summary | echo "Key: ${{ secrets.API_KEY }}" >> $ATOMGIT_STEP_SUMMARY  | 是 |
| 2 | Intentionally fail | echo "Failing with key ${{ secrets.API_KEY }}" exit 1  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] step_summary must_not_contain_secret: API_KEY | COVERED | target=step_summary 的断言可由执行结果验证 |
| [negative] error_stack must_not_contain_secret: API_KEY | COVERED | target=error_stack 的断言可由执行结果验证 |

### 问题

- 无

---
