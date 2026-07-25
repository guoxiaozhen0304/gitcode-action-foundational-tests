# COMP-PUSH-01-003

- 标题: paths 过滤匹配前 300 个变更文件行为符合预期
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMP-PUSH-01-003
维度标签:   [completeness]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-003
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      paths 过滤匹配前 300 个变更文件行为符合预期

前置条件:
  - workflow 配置 paths: [src/**]

操作步骤:
  1. 推送仅修改 docs/ 下文件的 commit
  2. 观察 workflow 是否触发

预期结果:
  - 因 docs/ 不匹配 src/**，workflow 不应触发

验证点:
  - [负向] 运行列表中不存在该 push 触发的运行

清理:      none
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo triggered (verify) | echo "should not run"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | push |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 运行列表中不存在该 push 触发的运行 | 空洞 | no real logic, negative assertion may be vacuously true |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_created | negative | no_run_for_non_matching_path | VACUOUS | no real logic, negative assertion may be vacuously true |

### 问题

- 验证点 `运行列表中不存在该 push 触发的运行` → 空洞: no real logic, negative assertion may be vacuously true

- 断言 `[negative] run_created` → VACUOUS: no real logic, negative assertion may be vacuously true

---
