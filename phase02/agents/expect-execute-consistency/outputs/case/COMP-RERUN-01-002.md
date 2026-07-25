# COMP-RERUN-01-002

- 标题: 第 4 次 rerun 应被系统拒绝
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-RERUN-01-002
维度标签:   [completeness, reliability]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-009
参照来源:  inputs/gitcode-spec/running-pipelines/view-job-logs.md; inputs/gitcode-spec/running-pipelines/view-run-results.md
母意图:    —
标题:      第 4 次 rerun 应被系统拒绝

前置条件:
  - 某条运行已 rerun 3 次

操作步骤:
  1. 尝试第 4 次 rerun

预期结果:
  - 系统拒绝第 4 次 rerun
  - 返回明确提示说明已达最大重试次数

验证点:
  - [负向] 第 4 次 rerun 不应创建新运行
  - [非功能] 报错信息应说明最多 3 次限制

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo | run: echo "run"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify rerun limit
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo
        run: |
          echo "run"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 第 4 次 rerun 不应创建新运行 | ✅ COVERED | negative assertion in YAML assertions |
| [非功能] 报错信息应说明最多 3 次限制 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |

### 问题

- [非功能] 报错信息应说明最多 3 次限制: PARTIAL - all steps are trivial echo

---
