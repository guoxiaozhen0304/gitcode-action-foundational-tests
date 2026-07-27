# COMP-ATOMGIT-01-048

- **标题**: atomgit 事件相关属性可访问性
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**atomgit 事件相关属性可访问性**
- 触发事件: `push`
- 规格引用: INTENT-COMP-048

通过标准：
1. [正向] event.ref、before、after 可访问 —— 断言 run_logs must_contain EVENT_REF=refs/、BEFORE=、AFTER=

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print event properties | 7 行 echo 语句，每行引用 `${{ atomgit.event.* }}` | - | 平台事件上下文字段的值 |

## 3. 触发与运行环境

| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: EVENT_REF=refs/ | ✅ GENUINE | `${{ atomgit.event.ref }}` 上下文求值是真实被测行为 |
| 2 | run_logs | positive | must_contain: BEFORE= | ✅ GENUINE | `${{ atomgit.event.before }}` 上下文求值 |
| 3 | run_logs | positive | must_contain: AFTER= | ✅ GENUINE | `${{ atomgit.event.after }}` 上下文求值 |

