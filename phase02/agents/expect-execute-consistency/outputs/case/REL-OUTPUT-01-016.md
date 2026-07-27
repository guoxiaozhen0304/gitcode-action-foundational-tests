# REL-OUTPUT-01-016
- **标题**: step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-016
通过标准：
1. 下游读取内容长度 = 1,048,576 bytes

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | write 1MB output | `python3 -c "print('A'*1048576)" > out.txt; echo "data=$(cat out.txt)" >> $ATOMGIT_OUTPUT` | — | 向 ATOMGIT_OUTPUT 写入 1MB 数据 |
| 2 | read 1MB output | `echo "${{ steps.writer.outputs.data }}"; test $(echo "${{ steps.writer.outputs.data }}" \| wc -c) -ge 1048576` | — | 读取并校验 output 长度 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_output_length = 1048576 | positive | — | ✅ GENUINE | `python3 -c` 真实生成 1MB 数据写入 `$ATOMGIT_OUTPUT`，下游 `${{ steps.writer.outputs.data }}` 读取并用 `test` 和 `wc -c` 校验长度。使用真实命令 python3、test、wc，非静态 echo |
---
