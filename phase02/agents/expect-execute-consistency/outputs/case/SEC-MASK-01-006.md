# SEC-MASK-01-006

- 标题: Secret 日志脱敏不可通过分片输出绕过
- 维度: 安全性 | 优先级: P0
- 评级: 混合问题

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
操作步骤:
  1. 1. 提交一个 workflow，逐字符或逐小段输出 secret
  2. 2. 触发 workflow 并查看运行日志
预期结果:
  - 即使分片输出，secret 的各片段仍被脱敏
  - 或分片到不可还原长度以下

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo secret character by character | secret="${{ secrets.DEPLOY_TOKEN }}" for (( i=0; i<${#secret}; i++ )); do   echo "char $i: ${secret:$i:1}" done  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: DEPLOY_TOKEN | COVERED | 步骤使用了 DEPLOY_TOKEN，平台需在日志中脱敏 |
| [negative] run_logs  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 日志中 secret 的任意连续子串（如 3 字符以上）命中数应为 0 |

### 问题

- **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 日志中 secret 的任意连续子串（如 3 字符以上）命中数应为 0

---
