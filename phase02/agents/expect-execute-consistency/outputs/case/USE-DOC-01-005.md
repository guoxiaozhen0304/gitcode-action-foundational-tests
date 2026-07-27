# USE-DOC-01-005
- **标题**: configure-steps 的 shell 类型与命令语言不匹配示例照抄失败
- **维度**: 易用性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**configure-steps 的 shell 类型与命令语言不匹配示例照抄失败**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-033
通过标准：
1. 两个照抄示例的 job 运行失败即为示例缺陷实证
2. 文档示例中 shell 类型应与示例命令语言匹配

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | bash-example | `shell: bash; Write-Host "hello"` | - | bash 执行 PowerShell 命令应失败 |
| 2 | python-example | `shell: python; echo "hello"` | - | python 执行 shell 命令应失败 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: "failure" | ✅ GENUINE | 两个 job 均由 platform 定义的 shell 执行不匹配的命令，应产生真实失败 |
| 2 | documentation | negative | eval: "deterministic" | ❌ MISSING_SOURCE | target=documentation，无 workflow 步骤产生 |

### 问题
**断言 2 — MISSING_SOURCE**: 文档缺陷判定依赖 harness 侧静态扫描。断言 1 的实证（运行失败）为该文档缺陷提供了证据。
---
