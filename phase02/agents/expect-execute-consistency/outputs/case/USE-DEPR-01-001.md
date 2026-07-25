# USE-DEPR-01-001

- 标题: 使用 ATOMGIT_OUTPUT 文件协议时正常生效
- 维度: 易用性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

```
用例 ID:   USE-DEPR-01-001
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-010
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      使用 ATOMGIT_OUTPUT 文件协议时正常生效

前置条件:
  - workflow 在 GitCode Runner 上执行

操作步骤:
  1. 在 run 步骤中使用 echo key=val >> $ATOMGIT_OUTPUT

预期结果:
  输出参数正确设置，下游步骤可引用

验证点:
  - [正向] 下游步骤通过 steps.*.outputs.key 获取到值
  - [正向] 运行成功完成

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | set output (test-output) | echo "mykey=myvalue" >> "$ATOMGIT_OUTPUT"  | GENUINE |
| 2 | read output (test-output) | echo "val=${{ steps.out.outputs.mykey }}"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 下游步骤通过 steps.*.outputs.key 获取到值 | 空洞 | no step produces 'val=myvalue' |
| 运行成功完成 | 空洞 | no step produces 'val=myvalue' |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | val=myvalue | MISSING_SOURCE | no step produces 'val=myvalue' |

### 问题

- 验证点 `下游步骤通过 steps.*.outputs.key 获取到值` → 空洞: no step produces 'val=myvalue'

- 验证点 `运行成功完成` → 空洞: no step produces 'val=myvalue'

- 断言 `[positive] run_logs` → MISSING_SOURCE: no step produces 'val=myvalue'

---
