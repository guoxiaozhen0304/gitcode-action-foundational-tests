# USE-UNKN-01-002
- **标题**: 未知字段报错若识别为 GitHub 特有应追加迁移提示
- **维度**: usability
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**未知字段报错若识别为 GitHub 特有应追加迁移提示**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-023
通过标准：
1. 报错中是否出现 GitHub Actions 特有等迁移提示

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | step | `echo "hello"` | 无 | 预期平台对 container 字段给出迁移提示 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message eval=llm_assisted | nonfunctional | LLM 判定报错迁移提示内容 | 🔶 LLM_DEPENDENT | 唯一断言为 LLM 辅助判定 |

### 问题
唯一断言为 nonfunctional + llm_assisted，步骤仅有纯 echo，完全依赖 LLM 判定报错质量。
---
