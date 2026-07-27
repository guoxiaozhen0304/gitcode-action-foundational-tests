# COMP-BOUND-01-087

- **标题**: 步骤输出与跨 job 传递边界验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**步骤输出与跨 job 传递边界验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-087

通过标准：
1. [正向] ATOMGIT_OUTPUT 写入后同 job 可读取 —— 断言 K1=val1、K2=val2、output_ok

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Write output (id: writer) | `echo "key1=val1" >> "$ATOMGIT_OUTPUT"` + `echo "key2=val2" >> "$ATOMGIT_OUTPUT"` | - | 向平台输出文件写入键值对 |
| 2 | Read output | `echo "K1=${{ steps.writer.outputs.key1 }}"` + `echo "K2=${{ steps.writer.outputs.key2 }}"` + `echo "output_ok"` | - | 通过 steps 上下文读取并输出上一步写入的值 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: K1=val1 | ✅ GENUINE | `${{ steps.writer.outputs.key1 }}` 从 $ATOMGIT_OUTPUT 文件读取真实写入的值 |
| 2 | run_logs | positive | must_contain: K2=val2 | ✅ GENUINE | steps.writer.outputs 引用真实执行了 ATOMGIT_OUTPUT 写入的前置步骤 |
| 3 | run_logs | positive | must_contain: output_ok | ✅ GENUINE | 同一步骤包含 steps 上下文表达式，步骤整体为非空洞 |

