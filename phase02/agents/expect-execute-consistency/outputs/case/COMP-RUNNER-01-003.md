# COMP-RUNNER-01-003

- 标题: 不存在的标签组合导致 job 排队或失败
- 维度: 完备性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMP-RUNNER-01-003
维度标签:   [completeness, compatibility]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-010
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      不存在的标签组合导致 job 排队或失败

前置条件:
  - 平台不存在该标签组合对应的 Runner

操作步骤:
  1. 配置不存在的 runs-on 标签
  2. 触发 workflow

预期结果:
  - job 无法被调度，最终排队超时或失败

验证点:
  - [负向] job 不应成功执行
  - [非功能] 系统应给出标签无匹配的提示

清理:      none
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo (verify) | echo "should not run"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| job 不应成功执行 | 空洞 | no failure path exists, status=success guaranteed |
| 系统应给出标签无匹配的提示 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | success | IMPOSSIBLE | no failure path exists, status=success guaranteed |
| 2 | error_message | nonfunctional | 错误信息应提示无匹配 Runner 或标签格式指引 | LLM_DEPENDENT | LLM/nonfunctional assertion: 错误信息应提示无匹配 Runner 或标签格式指引 |

### 问题

- 验证点 `job 不应成功执行` → 空洞: no failure path exists, status=success guaranteed

- 断言 `[negative] run_status` → IMPOSSIBLE: no failure path exists, status=success guaranteed

---
