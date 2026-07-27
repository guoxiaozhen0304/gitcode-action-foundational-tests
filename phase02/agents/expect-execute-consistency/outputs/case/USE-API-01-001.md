# USE-API-01-001
- **标题**: API 字段值与事件类型命名同一概念分裂的对照检查
- **维度**: 易用性
- **优先级**: P2
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**API 字段值与事件类型命名同一概念分裂的对照检查**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-048
通过标准：
1. 同一概念命名应在事件、API、文档三处一致
2. 若已分裂，文档应在两处互相引用对照

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | (无 workflow) | — | — | — |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-pr |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | api_response | negative | eval: "deterministic" | ❌ MISSING_SOURCE | workflow: null，无步骤产生 api_response |

### 问题
**断言 1 — MISSING_SOURCE**: workflow 为 null，无任何步骤。API 命名对照检查完全依赖 harness 外部调用与文档扫描。
---
