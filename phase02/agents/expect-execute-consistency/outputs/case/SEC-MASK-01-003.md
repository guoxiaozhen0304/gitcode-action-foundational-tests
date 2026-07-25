# SEC-MASK-01-003

- 标题: Secret 日志脱敏不可通过 base64 编码绕过
- 维度: 安全性 | 优先级: P0
- 评级: 混合问题

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
操作步骤:
  1. 1. 提交一个 workflow，在 job 中对 secret 做 base64 编码后再输出到日志
  2. 2. 触发 workflow 并查看运行日志
预期结果:
  - base64 编码后的 secret 值不应以明文形式出现在日志中
  - 系统应能识别编码后的 secret 并执行脱敏

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Encode and echo secret | encoded=$(echo -n "${{ secrets.DEPLOY_TOKEN }}" \| base64) echo "encoded=$encoded"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: DEPLOY_TOKEN | COVERED | 步骤使用了 DEPLOY_TOKEN，平台需在日志中脱敏 |
| [negative] run_logs  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 日志中 base64 编码后的字符串与 secret 原值存在一一对应关系时应被遮蔽 |

### 问题

- **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 日志中 base64 编码后的字符串与 secret 原值存在一一对应关系时应被遮蔽

---
