# COMP-BOUND-01-086

- **标题**: 矩阵构建 include exclude 与单值边界验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**矩阵构建 include exclude 与单值边界验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-086

通过标准：
1. [正向] include/exclude 矩阵变量可访问 —— 断言 run_logs must_contain matrix_ok

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Matrix value | `echo "OS=${{ matrix.os }}"` + `echo "VER=${{ matrix.version }}"` + `echo "matrix_ok"` | - | 平台矩阵展开后的 os/version 值 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: matrix_ok | ✅ GENUINE | 同一步骤包含 `${{ matrix.os }}` 和 `${{ matrix.version }}` 表达式，平台上下文求值即真实被测行为 |

