# USE-CLI-01-001
- **标题**: Runner 无 gh 等效 CLI 时迁移指引的替代方案说明
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**Runner 无 gh 等效 CLI 时迁移指引的替代方案说明**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-045
通过标准：
1. 记录 Runner 上各 CLI 命令的存在性
2. Runner 无等效 CLI 且文档无对应说明即不合格
3. 从 GitHub 迁移章节应包含 gh CLI 替代方案小节

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | probe cli commands | `command -v gh || echo "gh=NOTFOUND"`，`command -v gitcode || echo "gitcode=NOTFOUND"`，`command -v atomgit || echo "atomgit=NOTFOUND"` | - | 各 CLI 存在性探测结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval: "deterministic" | ✅ GENUINE | 步骤使用 `command -v` 真实探测 CLI 存在性，输出由系统环境决定 |
| 2 | documentation | negative | eval: "deterministic" | ❌ MISSING_SOURCE | assertion target=documentation，无 workflow 步骤产生文档内容 |

### 问题
**断言 2 — MISSING_SOURCE**: workflow 步骤探测 CLI 存在性（断言 1），但文档迁移指引检查（断言 2）依赖 harness 侧静态扫描，workflow 无法产生 documentation target 输出。
---
