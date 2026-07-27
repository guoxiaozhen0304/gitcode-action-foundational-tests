# REL-PATHS-01-014
- **标题**: paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效**
- 触发事件: `push`
- 规格引用: INTENT-REL-014
通过标准：
1. workflow 运行被创建

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo triggered | `echo triggered by paths` | — | 固定字符串输出 |

## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status = completed(success) | positive | — | ⚠️ STATUS_GUARANTEED | step 为纯 `echo triggered by paths`，无 if:/uses:/`${{ }}`/真实命令。workflow 被触发则必然成功，不检验 paths 过滤是否正确匹配 |
### 问题
- step 仅为静态 echo，无法验证 paths 过滤行为本身（即 300 文件中 1 个匹配 src/** 是否正确触发）
- 文本要求的"变更恰好 300 个文件，其中 1 个匹配 paths 规则"由外部 harness/commit 实现，YAML workflow 本身不体现此复杂性
---
