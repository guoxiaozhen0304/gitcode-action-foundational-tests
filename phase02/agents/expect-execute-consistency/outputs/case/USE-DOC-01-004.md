# USE-DOC-01-004
- **标题**: workflow-commands 多行输出示例漏写重定向照抄得空输出
- **维度**: 易用性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**workflow-commands 多行输出示例漏写重定向照抄得空输出**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-033
通过标准：
1. 照抄示例后读取到的输出值应为空，实证示例缺少重定向
2. 文档示例不应省略会导致行为相反的关键行

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | doc example produce output | 多行 echo 输出（未重定向到 $ATOMGIT_OUTPUT） | - | 仅输出到 stdout，不写入 output 文件 |
| 2 | read output | `echo "got=[${{ steps.producer.outputs.multiline }}]"` | - | 读取 output，预期为空 `got=[]` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval: "deterministic" | ✅ GENUINE | 步骤 2 使用 `${{ steps.producer.outputs.multiline }}` 表达式读取 output，真实复现照抄示例的缺失行为 |
| 2 | documentation | negative | eval: "deterministic" | ❌ MISSING_SOURCE | target=documentation，无 workflow 步骤产生 |

### 问题
**断言 2 — MISSING_SOURCE**: 文档缺陷判定依赖 harness 侧静态扫描，workflow 无法产生 documentation target 输出。不过断言 1 的实证（output 为空）为该文档缺陷提供了证据。
---
