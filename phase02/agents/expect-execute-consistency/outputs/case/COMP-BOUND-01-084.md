# COMP-BOUND-01-084

- **标题**: 路径与分支过滤组合及否定模式边界验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**路径与分支过滤组合及否定模式边界验证**
- 触发事件: `push`
- 规格引用: INTENT-COMP-084

通过标准：
1. [正向] branches + paths 组合过滤生效
2. [负向] 仅否定模式时不触发 workflow
3. [正向] 否定模式与肯定模式组合生效

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo ok | `echo "filter_boundary_ok"` | - | 字面量字符串 "filter_boundary_ok" |

## 3. 触发与运行环境

| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 唯一步骤仅为 echo，无条件失败路径，永远成功 |
| 2 | run_logs | positive | must_contain: filter_boundary_ok | ❌ VACUOUS | 步骤仅 echo 字面量，无 if:、无 ${{ }}、无 uses: action、无实质命令；触发级过滤行为由平台执行，步骤未做任何验证 |

### 问题

**断言 1 — STATUS_GUARANTEED**: 唯一步骤 `echo "filter_boundary_ok"` 永远成功，无法验证过滤行为。分支/路径过滤逻辑发生在 trigger 层，workflow 一旦被触发进入 step 执行就一定会 echo 成功。

**断言 2 — VACUOUS**: 步骤仅 echo 了期望字符串，未执行任何分支过滤组合验证。文本规格要求测试 branches+paths AND 关系、`!` 否定模式、仅否定模式不触发等，但 YAML 步骤完全不涉及这些验证。

