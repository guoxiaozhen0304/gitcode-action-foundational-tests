# COMP-JOB-01-068

- **标题**: job strategy 矩阵与 continue-on-error 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**job strategy 矩阵与 continue-on-error 验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-067

通过标准：
1. [正向] 矩阵变量在 step 中可访问 —— 断言 VERSION=a、VERSION=b
2. [正向] continue-on-error 和 fail-fast 字段被接受 —— 断言 strategy_ok

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Matrix value | `echo "VERSION=${{ matrix.version }}"` + `echo "strategy_ok"` | - (job 级: strategy.matrix, fail-fast: false, continue-on-error: true) | 矩阵展开的各版本值和标志 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: VERSION=a | ✅ GENUINE | `${{ matrix.version }}` 来自 strategy.matrix 展开，平台矩阵执行即真实被测行为 |
| 2 | run_logs | positive | must_contain: VERSION=b | ✅ GENUINE | 同上，矩阵第二维度的展开结果 |
| 3 | run_logs | positive | must_contain: strategy_ok | ✅ GENUINE | 同一步骤包含 `${{ matrix.version }}` 表达式，步骤整体为非空洞 |

