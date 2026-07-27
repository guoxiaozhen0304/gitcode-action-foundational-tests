# USE-ENV-01-002

- 标题: 引用 GITHUB_SHA 时日志应给出环境变量映射提示
- 维度: usability/compatibility | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

前置条件:
  - workflow 在 GitCode Runner 上执行

操作步骤:
  1. 在 run 步骤中输出 $GITHUB_SHA

预期结果:
  日志中应出现关于 GITHUB 变量不存在或建议使用 ATOMGIT 的提示

验证点:
  - [负向] 不应静默输出空值后继续
  - [非功能] 日志中是否出现 ATOMGIT 前缀的环境变量指引

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | echo GITHUB_SHA | `set -u; echo "sha=$GITHUB_SHA"` | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
id: USE-ENV-01-002
dimensions: ["usability", "compatibility"]
dimension: usability
priority: P1
title: "引用 GITHUB_SHA 时日志应给出环境变量映射提示"
intent_ref: INTENT-USE-003

setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
  on:
    workflow_dispatch:
  jobs:
    bad-env:
      name: test GITHUB env var hint
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: echo GITHUB_SHA
          run: |
            set -u
            echo "sha=$GITHUB_SHA"

trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: nonfunctional
    target: error_message
    eval: llm_assisted
    rubric: "日志警告是否足够醒目且包含有效指引：应提示 GITHUB_* 环境变量在 GitCode 中对应为 ATOMGIT_*"

teardown:
  reset: none
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo | default |
| Secrets | (none) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 不应静默输出空值后继续 | ❌ UNVERIFIABLE | 步骤含 `set -u` / `$GITHUB_SHA` 引用但仅 echo；single dispatch cannot prove negation of silent ignore |
| [非功能] 日志中出现 ATOMGIT_* 环境变量指引 | ❌ MISSING | 步骤仅 echo 变量值，不产生平台级 env var 映射提示；断言 eval=llm_assisted |

### 问题

- [负向] 不应静默输出空值后继续: UNVERIFIABLE — 步骤用 `set -u` 和 `$GITHUB_SHA` 引用试图触发行为，但单次运行无法证明"不会静默忽略"这一否定结论
- [非功能] ATOMGIT 前缀指引: MISSING — 步骤不产生平台级警告信息，断言依赖 LLM 评估 runner 日志

---
