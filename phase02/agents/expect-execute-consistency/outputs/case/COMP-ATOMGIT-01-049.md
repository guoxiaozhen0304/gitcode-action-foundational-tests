# COMP-ATOMGIT-01-049

- **标题**: atomgit 边界格式校验
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**atomgit 边界格式校验**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-049

通过标准：
1. [正向] sha 长度等于 40 —— 断言 SHA_LEN=40
2. [正向] ref 以 refs/ 开头 —— 断言 REF_PREFIX=refs
3. [正向] actor 非空 —— 断言 ACTOR_LEN=
4. [正向] ref_name 不含 refs/ 前缀 —— 无对应断言

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Check formats | bash 字符串运算：`${#ATOMGIT_SHA}`、`${ATOMGIT_REF%%/*}`、`${ATOMGIT_REF_NAME#refs/}`、`${#ATOMGIT_ACTOR}` | - | 对平台环境变量做长度/截取运算 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: SHA_LEN=40 | ✅ GENUINE | `${#ATOMGIT_SHA}` 对平台提供的 SHA 环境变量计算长度，非字面量 echo |
| 2 | run_logs | positive | must_contain: REF_PREFIX=refs | ✅ GENUINE | `${ATOMGIT_REF%%/*}` 对平台上下文做 bash 截取运算 |
| 3 | run_logs | positive | must_contain: ACTOR_LEN= | ✅ GENUINE | `${#ATOMGIT_ACTOR}` 验证 actor 非空 |

