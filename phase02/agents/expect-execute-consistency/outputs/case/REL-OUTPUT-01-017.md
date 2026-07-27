# REL-OUTPUT-01-017
- **标题**: step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-017
通过标准：
1. 日志含 1MB/超出限制 提示
2. job 状态 = failure

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | write 1MB+1 output | `python3 -c "print('A'*1048577)" > out.txt; echo "data=$(cat out.txt)" >> $ATOMGIT_OUTPUT` | — | 尝试向 ATOMGIT_OUTPUT 写入超过 1MB 限制的数据 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains "1MB" | positive | — | ✅ GENUINE | `python3 -c` 真实生成 1048577 字节写入 `$ATOMGIT_OUTPUT`，平台应在写入时检测到超限并输出含 "1MB" 的错误信息，日志由平台拒绝逻辑产生 |
| 2 | job_status = failure | positive | — | ✅ GENUINE | 写入超限数据 1048577 字节到 ATOMGIT_OUTPUT 会触发平台拒绝，有真实失败路径 |
---
