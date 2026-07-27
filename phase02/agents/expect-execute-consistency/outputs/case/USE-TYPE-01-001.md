# USE-TYPE-01-001

- 标题: 使用 GitCode types 命名时正常触发
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   USE-TYPE-01-001
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-009
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      使用 GitCode types 命名时正常触发

前置条件:
  - 仓库存在 PR

操作步骤:
  1. 配置 on: pull_request: types: [open, update, reopen]

预期结果:
  PR 事件正常触发 workflow

验证点:
  - [正向] PR 创建或更新时触发运行
  - [正向] 运行成功或至少进入执行态

清理:      无

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | echo event | run: echo "event=${{ atomgit.event_name }}" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    types:
      - open
      - update
      - reopen
    branches: [main]
jobs:
  test-types:
    name: test gitcode types
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: echo event
        run: |
          echo "event=${{ atomgit.event_name }}"
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request |
| as | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [正向] PR 创建或更新时触发运行 | ✅ COVERED | 断言 target=run_status equals COMPLETED，步骤使用 ${{ atomgit.event_name }} 表达式输出触发事件名（如 pull_request），harness 可观测 run_status 确认 workflow 被正确触发并执行 |
| [正向] 运行成功或至少进入执行态 | ✅ COVERED | 同上，run_status=COMPLETED 直接验证运行成功进入执行态 |

### 问题

无。

## 5. 评级理由

步骤使用 `${{ atomgit.event_name }}` 上下文表达式，输出真实的触发事件名，步骤内容真实。断言 target=run_status 由 harness 直接观测，可验证 workflow 是否被 GitCode types（open/update/reopen）正确触发并正常完成。触发事件不影响覆盖判定。
