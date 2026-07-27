# COMPAT-SHELL-01-002
- **标题**: 默认工作目录隐式行为差异 - 未显式声明时是否为仓库根目录
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**默认工作目录隐式行为差异 - 未显式声明时是否为仓库根目录**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-001
通过标准：
1. [正向] 当前工作目录路径与仓库根目录一致
2. [正向] 可访问到仓库根目录下的文件

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | `uses: checkout` | - | checkout 内部日志 |
| 2 | print working directory | `pwd` → `ls -la` | - | 当前目录路径, 文件列表 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains="README" | ✅ GENUINE | 步骤先执行 `uses: checkout` 再执行 `ls -la` 实质命令列出目录内容，若 repo 含 README 则 `ls` 输出天然包含 |

---
