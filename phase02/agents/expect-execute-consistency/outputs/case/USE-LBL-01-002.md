# USE-LBL-01-002
- **标题**: runs-on 标签因容量不足排队时应提示排队状态而非无可用 runner
- **维度**: usability
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**runs-on 标签因容量不足排队时应提示排队状态而非无可用 runner**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-025
通过标准：
1. 状态或日志中是否出现排队/等待字样
2. 错误信息是否区分无匹配与容量不足

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | step | `echo "queued then ran"` | 无 | 纯 echo |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs eval=llm_assisted | nonfunctional | 无任何 `${{ }}` / `if:` / `uses:` / 真实命令，步骤纯 echo | 🔶 LLM_DEPENDENT | 断言依赖 LLM 辅助判定排队提示内容，步骤本身无平台行为验证能力 |

### 问题
唯一断言为 nonfunctional + llm_assisted，无任何可确定性判定的断言。
---
