# SEC-WCMD-01-004
- **标题**: ATOMGIT_OUTPUT 不被不可信输入污染提权
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**ATOMGIT_OUTPUT 不被不可信输入污染提权**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-030
通过标准：
1. 含换行/协议控制字符的不可信值写入 ATOMGIT_OUTPUT 时，不应注入计划外的 output 条目
2. 后续 step 不应读取到被劫持的 output

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Write malicious output | 写入含换行的多行值到 $ATOMGIT_OUTPUT | - | 尝试注入 hijacked 字段 |
| 2 | Check no hijack | `if [ "${{ steps.bad.outputs.hijacked }}" = "bad" ]; then echo "hijack succeeded"; exit 1; else echo "no hijack"; fi` | - | 检测 hijack 是否成功 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain: "hijack succeeded" | ✅ GENUINE | 步骤 2 使用 `${{ steps.bad.outputs.hijacked }}` + shell if/fi + exit 1 真实检测 output 注入 |
| 2 | run_logs | positive | equals: "no hijack" | ✅ GENUINE | 步骤 2 在注入失败时输出 "no hijack"，由真实条件判断和 ${{ }} 表达式求值产生 |
---
