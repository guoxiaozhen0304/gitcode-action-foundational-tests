# SEC-WCMD-01-003
- **标题**: ATOMGIT_ENV 不被不可信输入污染提权
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**ATOMGIT_ENV 不被不可信输入污染提权**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-030
通过标准：
1. 含换行/协议控制字符的不可信值写入 ATOMGIT_ENV 时，不应注入计划外的环境变量
2. 多行值应经随机 delimiter 等机制安全写入

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Write malicious env | 写入含换行的多行值到 $ATOMGIT_ENV | - | 尝试注入 INJECTED_VAR |
| 2 | Check no injection | `if [ -n "$INJECTED_VAR" ]; then echo "injection succeeded"; exit 1; else echo "no injection"; fi` | - | 检测是否注入成功 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain: "injection succeeded" | ✅ GENUINE | 步骤 2 使用 shell if/fi + exit 1 真实检测 ATOMGIT_ENV 注入，仅注入成功时输出该字符串 |
| 2 | run_logs | positive | equals: "no injection" | ✅ GENUINE | 步骤 2 在注入失败时输出 "no injection"，由真实 shell 条件判断产生 |

### 问题
(无)
---
