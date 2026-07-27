# COMP-JOB-01-066

- **标题**: job 必填字段 name runs-on steps 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**job 必填字段 name runs-on steps 验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-066

通过标准：
1. [正向] 完整 job 定义通过校验并执行 —— 断言 run_status=success、run_logs must_contain job_fields_ok
2. [负向] 缺 name 被平台拒绝 —— 未实现
3. [负向] 缺 steps 被平台拒绝 —— 未实现

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo ok | `echo "job_fields_ok"` | - | 字面量字符串 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 唯一步骤仅为 echo，永远成功 |
| 2 | run_logs | positive | must_contain: job_fields_ok | ❌ VACUOUS | 仅 echo 字面量，无 if:、无 ${{ }}、无 uses:、无 real commands |

### 问题

**断言 1 — STATUS_GUARANTEED**: 唯一步骤 echo 永远成功。

**断言 2 — VACUOUS**: 步骤仅 echo 期望字符串。文本规格要求验证「缺 name 被平台拒绝」「缺 steps 被平台拒绝」等负向场景，但 YAML 只包含一条正向 echo 步骤，完全没有实现缺失字段的负向测试。

