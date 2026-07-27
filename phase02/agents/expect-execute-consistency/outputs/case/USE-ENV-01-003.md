# USE-ENV-01-003
- **标题**: ATOMGIT 系统环境变量实际注入集合与文档清单双向 diff
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**ATOMGIT 系统环境变量实际注入集合与文档清单双向 diff**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-044
通过标准：
1. 实际注入集合应被完整记录
2. 文档列出而实际未注入的变量每 1 个即一条缺陷
3. 两页文档清单不一致即为缺陷

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | dump atomgit env vars | `env \| grep "^ATOMGIT_" \| sort` | - | 排序后的 ATOMGIT_* 环境变量清单 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: "ATOMGIT_" | ✅ GENUINE | 步骤使用 env + grep + sort 真实命令，输出由平台运行时环境决定 |
| 2 | documentation | negative | eval: "deterministic" | ❌ MISSING_SOURCE | target=documentation，无 workflow 步骤产生 |

### 问题
**断言 2 — MISSING_SOURCE**: 文档清单比对依赖 harness 侧静态扫描。断言 1 的实际注入集合为该比对提供了实证数据。
---
