# USE-DOC-01-006
- **标题**: syntax-reference 章节编号连续性扫描
- **维度**: 易用性
- **优先级**: P2
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**syntax-reference 章节编号连续性扫描**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-034
通过标准：
1. 章节号应连续
2. 若官方确有跳号，应在跳号处显式注明沿革

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
| 1 | documentation | negative | eval: "deterministic" | ❌ MISSING_SOURCE | workflow: null，纯文档扫描，无 workflow 步骤 |

### 问题
**断言 1 — MISSING_SOURCE**: 纯文档编号扫描，无 workflow 执行。
---
