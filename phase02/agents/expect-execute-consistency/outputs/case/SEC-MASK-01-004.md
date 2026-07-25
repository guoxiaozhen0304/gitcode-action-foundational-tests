# SEC-MASK-01-004

- 标题: Secret 日志脱敏不可通过字符串拼接或插值绕过
- 维度: 安全性 | 优先级: P0
- 评级: 混合问题

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 secret API_KEY
操作步骤:
  1. 1. 提交一个 workflow，将 secret 拆分为多段通过字符串拼接输出
  2. 2. 触发 workflow 并查看运行日志
预期结果:
  - 拼接后的 secret 值不应以可还原形式出现在日志中
  - 即使分多行、多步骤输出，也应保持脱敏一致性

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo secret in parts | part1=$(echo "${{ secrets.API_KEY }}" \| cut -c1-4) part2=$(echo "${{ secrets.API_KEY }}" \| cut -c5-8) echo "part1=$part1 part2=$part2"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain_secret: API_KEY | COVERED | 步骤使用了 API_KEY，平台需在日志中脱敏 |
| [negative] run_logs  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 日志全文搜索 secret 的任意连续子串（长度超过阈值）命中数为 0 |

### 问题

- **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 日志全文搜索 secret 的任意连续子串（长度超过阈值）命中数为 0

---
