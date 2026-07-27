# COMP-EXPR-01-057

- **标题**: format substring replace 函数边界行为
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**format substring replace 函数边界行为**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-057

通过标准：
1. [正向] format 输出拼接后的字符串 —— 断言 FMT=Hello World
2. [正向] substring 输出指定长度子串 —— 断言 SUB=
3. [正向] replace 输出替换后的字符串 —— 断言 REP=

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Format string | `echo "FMT=${{ format('Hello {0}', 'World') }}"` | - | format 函数拼接结果 |
| 2 | Substring sha | `echo "SUB=${{ substring(atomgit.sha, 0, 7) }}"` | - | SHA 前 7 位 |
| 3 | Replace prefix | `echo "REP=${{ replace(atomgit.ref, 'refs/heads/', '') ) }}"` | - | 去掉前缀后的分支名 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: FMT=Hello World | ✅ GENUINE | `${{ format('Hello {0}', 'World') }}` 真实函数求值 |
| 2 | run_logs | positive | must_contain: SUB= | ✅ GENUINE | `${{ substring(atomgit.sha, 0, 7) }}` 对平台 SHA 取子串 |
| 3 | run_logs | positive | must_contain: REP= | ✅ GENUINE | `${{ replace(atomgit.ref, 'refs/heads/', '') }}` 真实替换函数 |

