# USE-DEPR-01-001
- **标题**: 使用 ATOMGIT_OUTPUT 文件协议时正常生效
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用 ATOMGIT_OUTPUT 文件协议时正常生效**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-010
通过标准：
1. 输出参数正确设置，下游步骤可引用
2. 运行成功完成

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | set output | `echo "mykey=myvalue" >> "$ATOMGIT_OUTPUT"` | - | 写入环境变量指定的 output 文件 |
| 2 | read output | `echo "val=${{ steps.out.outputs.mykey }}"` | - | 读取前一步 output 值并打印 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: "val=myvalue" | ✅ GENUINE | 步骤 1 写入 $ATOMGIT_OUTPUT（实质命令），步骤 2 通过 `${{ steps.out.outputs.mykey }}` 表达式引用 |
---
