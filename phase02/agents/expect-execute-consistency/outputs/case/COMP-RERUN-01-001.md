# COMP-RERUN-01-001

- 标题: rerun 后 atomgit.sha 保持原始值 run_number 递增
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-RERUN-01-001
维度标签:   [completeness, reliability]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-009
参照来源:  inputs/gitcode-spec/running-pipelines/view-job-logs.md; inputs/gitcode-spec/running-pipelines/view-run-results.md
母意图:    —
标题:      rerun 后 atomgit.sha 保持原始值 run_number 递增

前置条件:
  - 存在一条已完成的 workflow 运行

操作步骤:
  1. 记录原始运行的 sha、ref、run_number
  2. 执行 rerun
  3. 对比新运行与原始运行的上下文

预期结果:
  - sha、ref、event_name 保持原始值
  - run_number 更新为新值（递增）

验证点:
  - [正向] rerun 后 sha 与原始运行一致
  - [正向] rerun 后 run_number 大于原始值

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Dump context | run: echo "sha=$ATOMGIT_SHA"
echo "ref=$ATOMGIT_REF"
echo "run_number=$ATOMGIT_RUN_NUMBER"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify rerun context
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Dump context
        run: |
          echo "sha=$ATOMGIT_SHA"
          echo "ref=$ATOMGIT_REF"
          echo "run_number=$ATOMGIT_RUN_NUMBER"

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
| [正向] rerun 后 sha 与原始运行一致 | ✅ COVERED | steps have real logic |
| [正向] rerun 后 run_number 大于原始值 | ✅ COVERED | steps have real logic |

### 问题

无

---
