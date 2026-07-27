# COMP-BOUND-01-085

- **标题**: cron 表达式格式与位置边界验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**cron 表达式格式与位置边界验证**
- 触发事件: `schedule`
- 规格引用: INTENT-COMP-085

通过标准：
1. [正向] 含 * 的 cron 通过校验
2. [正向] 含 , 的 cron 通过校验
3. [正向] 含 - 和 / 的 cron 通过校验

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo ok | `echo "cron_boundary_ok"` | - | 字面量字符串 "cron_boundary_ok" |

## 3. 触发与运行环境

| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 唯一步骤仅为 echo，无条件失败路径 |
| 2 | run_logs | positive | must_contain: cron_boundary_ok | ❌ VACUOUS | 步骤仅 echo 字面量，无 if:、无 ${{ }}、无 real commands；cron 格式校验完全由平台在 trigger 层完成，步骤不做任何验证 |

### 问题

**断言 1 — STATUS_GUARANTEED**: 只有一个 echo 步骤，永远成功。cron 格式验证由平台在 YAML 解析阶段完成，workflow 一旦被触发执行就必然 echo 成功。

**断言 2 — VACUOUS**: 步骤仅 echo 了期望字符串。文本规格要求验证 `*/5 * * * *`、`0 2,14 * * *`、`0 9-17 * * 1-5` 三种 cron 表达式，步骤无任何验证逻辑。

