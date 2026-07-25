# USE-INPT-01-001

- 标题: 使用 string 类型 input 时正常通过校验
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-INPT-01-001
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-008
参照来源:  inputs/gitcode-spec/writing-pipelines/workflow-file-location-structure.md
母意图:    —
标题:      使用 string 类型 input 时正常通过校验

前置条件:
  - workflow 文件合法

操作步骤:
  1. 声明 workflow_dispatch inputs 的 type: string

预期结果:
  YAML 校验通过，可手动触发

验证点:
  - [正向] 运行可手动触发
  - [正向] 输入参数正常传递

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | echo input (test-input) | echo "env=${{ inputs.env }}"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 运行可手动触发 | 覆盖 | status assertion: COMPLETED |
| 输入参数正常传递 | 覆盖 | status assertion: COMPLETED |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | COMPLETED | CONSISTENT | status assertion: COMPLETED |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
