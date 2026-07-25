# REL-YAMLCACHE-01-060

- 标题: Workflow YAML 缓存失效——修改后无旧代码残留
- 维度: 可靠性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

```
用例 ID:   REL-YAMLCACHE-01-060
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-060
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      Workflow YAML 缓存失效——修改后无旧代码残留

前置条件:
  - 仓库具备 workflow 修改与触发权限

操作步骤:
  1. 第一轮执行记录输出 marker_v1
  2. 修改 workflow 输出为 marker_v2 并 push
  3. 立即触发 workflow

预期结果:
  - 新触发运行日志中出现 marker_v2
  - 不应出现 marker_v1 缓存残留

验证点:
  - [正向] 日志打印 marker_v2
  - [负向] 不应打印 marker_v1

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | echo marker (test) | echo marker_v1  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 日志打印 marker_v2 | 空洞 | no step produces 'marker_v2' |
| 不应打印 marker_v1 | 空洞 | step echo marker only echoes 'marker_v1', no real logic |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | marker_v2 | MISSING_SOURCE | no step produces 'marker_v2' |
| 2 | run_logs | negative | marker_v1 | VACUOUS | step echo marker only echoes 'marker_v1', no real logic |

### 问题

- 验证点 `日志打印 marker_v2` → 空洞: no step produces 'marker_v2'

- 验证点 `不应打印 marker_v1` → 空洞: step echo marker only echoes 'marker_v1', no real logic

- 断言 `[positive] run_logs` → MISSING_SOURCE: no step produces 'marker_v2'

- 断言 `[negative] run_logs` → VACUOUS: step echo marker only echoes 'marker_v1', no real logic

---
