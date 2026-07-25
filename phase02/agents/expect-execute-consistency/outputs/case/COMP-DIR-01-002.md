# COMP-DIR-01-002

- 标题: .github/workflows/ 下的 YAML 不被识别为 workflow
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- 仓库 .github/workflows/ 目录下存在 ci.yml
- 仓库 .gitcode/workflows/ 下无同名 workflow

操作步骤:
1. 向默认分支推送代码变更
2. 观察 Actions 标签页是否出现新运行

预期结果:
- .github/workflows/ci.yml 不被识别为 workflow
- push 事件不会触发该文件对应的运行

验证点:
- [负向] 运行列表中不存在源自 .github/workflows/ci.yml 的运行

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| (无) | (空 workflow) | workflow: "" | — |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-DIR-01-002
dimensions: [completeness]
dimension: completeness
priority: P1
title: .github/workflows/ 下的 YAML 不被识别为 workflow
intent_ref: INTENT-COMP-001

setup:
  repo_fixture: github-workflows-dir
  secrets: []
  variables: {}
  branch_protection: default

workflow: |

trigger:
  event: push
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: negative
    target: run_list
    equals: no_run_from_github_dir

teardown:
  reset: none
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo | github-workflows-dir |
| Secrets | (none) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 运行列表中不存在源自 .github/workflows/ci.yml 的运行 | ✅ COVERED | negative assertion: run_list=no_run_from_github_dir |

### 问题

- 无

---
