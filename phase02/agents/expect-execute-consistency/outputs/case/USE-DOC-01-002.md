# USE-DOC-01-002
- **标题**: stages 与 stages 内 jobs 字段语法跨文档四种形态互相矛盾的扫描
- **维度**: 易用性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**stages 与 stages 内 jobs 字段语法跨文档四种形态互相矛盾的扫描**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-032
通过标准：
1. 同一字段在同一页面给出两种形态而不加说明即为缺陷
2. 全文档形态组合数大于 1 且无集中等价说明即为缺陷
3. 工作流文件位置与基本结构页应给出 stages 单一权威形态定义

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
| 1 | documentation | negative | eval: "deterministic" | ❌ MISSING_SOURCE | workflow: null，target=documentation，无步骤产生文档内容 |
| 2 | documentation | nonfunctional | eval: "deterministic" | ❌ MISSING_SOURCE | workflow: null，target=documentation，无步骤产生文档内容 |

### 问题
**断言 1, 2 — MISSING_SOURCE**: workflow 为 null，全部文档一致性检查依赖 harness 侧静态文档扫描，workflow 内部无对应步骤。
---
