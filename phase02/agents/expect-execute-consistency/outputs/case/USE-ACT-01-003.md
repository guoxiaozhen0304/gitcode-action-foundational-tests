# USE-ACT-01-003
- **标题**: 官方短名 Action 清单与 actions-market 插件目录的映射一致性
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**官方短名 Action 清单与 actions-market 插件目录的映射一致性**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-052
通过标准：
1. 文档应给出官方短名与市场插件名的完整对照表
2. 市场页应标识官方维护属性

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | (无 workflow) | — | — | — |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | eval: "deterministic" | ❌ MISSING_SOURCE | workflow: null，断言 target=documentation 无 workflow 步骤产生；文档比对为纯静态分析 |

### 问题
**断言 1 — MISSING_SOURCE**: workflow 为 null，无任何步骤产生 documentation target 的输出。全部文档一致性校验依赖 harness 侧静态扫描，workflow 未参与。
---
