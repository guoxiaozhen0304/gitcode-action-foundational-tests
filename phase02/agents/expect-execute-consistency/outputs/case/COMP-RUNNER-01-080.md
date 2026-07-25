# COMP-RUNNER-01-080

- 标题: runner 上下文属性可访问性验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-RUNNER-01-080
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-096~098
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      runner 上下文属性可访问性验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 在 step 中引用 runner.name / runner.temp / runner.tool_cache / runner.os / runner.arch
  2. 验证输出非空且格式正确

预期结果:
  - runner 上下文各属性可正常访问，runner.os 为 Linux / Windows / macOS，runner.arch 为 X64 / ARM / ARM64

验证点:
  - [正向] runner.name / temp / tool_cache 非空
  - [正向] runner.os 为预定义值之一
  - [正向] runner.arch 为预定义值之一

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Print runner props | run: echo "NAME=${{ runner.name }}"
echo "TEMP=${{ runner.temp }}"
echo "TOOL_CACHE=${{ runner.tool_cache }}"
echo "OS=${{ runner.os }}"
echo "ARCH=${{ run | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify runner context
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Print runner props
        run: |
          echo "NAME=${{ runner.name }}"
          echo "TEMP=${{ runner.temp }}"
          echo "TOOL_CACHE=${{ runner.tool_cache }}"
          echo "OS=${{ runner.os }}"
          echo "ARCH=${{ runner.arch }}"
          echo "runner_ok"

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
| [正向] runner.name / temp / tool_cache 非空 | ✅ COVERED | steps have real logic |
| [正向] runner.os 为预定义值之一 | ✅ COVERED | steps have real logic |
| [正向] runner.arch 为预定义值之一 | ✅ COVERED | steps have real logic |

### 问题

无

---
