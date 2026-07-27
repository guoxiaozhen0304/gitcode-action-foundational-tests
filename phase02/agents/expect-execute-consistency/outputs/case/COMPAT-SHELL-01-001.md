# COMPAT-SHELL-01-001
- **标题**: 默认 shell 隐式行为差异 - 未显式声明时是否为 bash
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**默认 shell 隐式行为差异 - 未显式声明时是否为 bash**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-001
通过标准：
1. [正向] 日志包含 bash 字样
2. [正向] 命令按 bash 语法解析执行

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | `uses: checkout` | - | checkout 内部日志 |
| 2 | print shell info | `echo "Current shell: $SHELL"` → `echo "Shell via ps: $(ps -p $$ -o comm=)"` | - | `Current shell: /bin/bash`, `Shell via ps: bash` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains=bash | ✅ GENUINE | 步骤先执行 `uses: checkout` 再执行 `ps -p $$ -o comm=` 实质命令获取实际 shell 名称，`ps` 输出天然包含 `bash` |

---
