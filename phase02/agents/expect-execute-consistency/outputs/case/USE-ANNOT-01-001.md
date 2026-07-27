# USE-ANNOT-01-001
- **标题**: workflow 命令 ::error:: 与 ::warning:: 在日志中保留原文
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**workflow 命令 ::error:: 与 ::warning:: 在日志中保留原文**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-021
通过标准：
1. 日志中包含 ::error:: 原始文本
2. 日志中包含 ::warning:: 原始文本

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | emit error and warning | `echo "::error file=src/main.js,line=10::Missing semicolon"` | - | 仅 echo workflow command 字面量 |
| 1 | emit error and warning | `echo "::warning file=src/util.js,line=5::Deprecated function"` | - | 仅 echo workflow command 字面量 |
| 1 | emit error and warning | `echo "::notice::General notice"` | - | 仅 echo workflow command 字面量 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: "::error file=src/main.js,line=10::Missing semicolon" | ❌ VACUOUS | 步骤仅 echo 该字符串字面量，无 if:、无 ${{ }}、无 uses:、无实质命令 |
| 2 | run_logs | positive | contains: "::warning file=src/util.js,line=5::Deprecated function" | ❌ VACUOUS | 步骤仅 echo 该字符串字面量，无 if:、无 ${{ }}、无 uses:、无实质命令 |

### 问题
**断言 1, 2 — VACUOUS**: 步骤仅通过 `echo` 输出期望字符串的字面量，未包含任何真实逻辑（if、${{ }}、uses action、实质命令）。日志中该字符串的出现仅因步骤直接 echo 了它，不证明 runner 对 workflow commands 的处理行为。
---
