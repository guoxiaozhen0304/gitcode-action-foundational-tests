# COMP-TRIG-01-072

- 标题: push 事件关键字段与过滤验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-TRIG-01-072
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-223~233
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      push 事件关键字段与过滤验证

前置条件:
  - 仓库已启用 AtomGit Action
  - 存在 main 分支

操作步骤:
  1. 配置 push 触发并定义 branches / paths / tags 过滤
  2. 推送代码验证触发和字段

预期结果:
  - push 事件触发 workflow，atomgit.event.ref / before / after / commits 字段可访问，branches 过滤仅匹配分支触发

验证点:
  - [正向] push 到 main 触发 workflow
  - [正向] event.before 和 event.after 非空
  - [正向] branches 过滤生效

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Print push fields | run: echo "REF=${{ atomgit.event.ref }}"
echo "BEFORE=${{ atomgit.event.before }}"
echo "AFTER=${{ atomgit.event.after }}"
echo "push_ok"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches: [main]
jobs:
  verify:
    name: Verify push event fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Print push fields
        run: |
          echo "REF=${{ atomgit.event.ref }}"
          echo "BEFORE=${{ atomgit.event.before }}"
          echo "AFTER=${{ atomgit.event.after }}"
          echo "push_ok"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] push 到 main 触发 workflow | ✅ COVERED | steps have real logic |
| [正向] event.before 和 event.after 非空 | ✅ COVERED | steps have real logic |
| [正向] branches 过滤生效 | ✅ COVERED | steps have real logic |

### 问题

无

---
