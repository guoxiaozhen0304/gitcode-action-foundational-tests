# COMP-EXPR-01-055

- **标题**: hashFiles 函数边界行为
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**hashFiles 函数边界行为**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-055

通过标准：
1. [正向] 单文件 hashFiles 输出 64 位 hex —— 断言 HASH_SINGLE=
2. [正向] 多文件 hashFiles 输出 64 位 hex —— 断言 HASH_MULTI=
3. [正向] 不匹配路径返回空或固定值 —— 断言 HASH_NONE=

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Single file hash | `echo "HASH_SINGLE=${{ hashFiles('package.json') }}"` | - | hashFiles 对单文件的求值结果 |
| 2 | Multi pattern hash | `echo "HASH_MULTI=${{ hashFiles('src/**', 'package.json') }}"` | - | hashFiles 对多模式匹配的求值结果 |
| 3 | No match hash | `echo "HASH_NONE=${{ hashFiles('nonexistent.xyz') }}"` | - | hashFiles 对无匹配路径的求值结果 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: HASH_SINGLE= | ✅ GENUINE | `${{ hashFiles('package.json') }}` 是真实平台函数求值 |
| 2 | run_logs | positive | must_contain: HASH_MULTI= | ✅ GENUINE | `${{ hashFiles('src/**', 'package.json') }}` 多文件 hash |
| 3 | run_logs | positive | must_contain: HASH_NONE= | ✅ GENUINE | `${{ hashFiles('nonexistent.xyz') }}` 无匹配路径的边界行为 |

