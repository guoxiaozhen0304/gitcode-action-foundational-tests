# COMP-SCRIPT-01-082

- 标题: 脚本权限设置与直接执行验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-SCRIPT-01-082
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-431~433
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      脚本权限设置与直接执行验证

前置条件:
  - 仓库已启用 AtomGit Action
  - 仓库根目录存在无执行权限脚本

操作步骤:
  1. 在 run 中先 chmod 再执行脚本
  2. 验证权限变更后脚本可直接执行

预期结果:
  - run 中可通过 chmod +x 赋予脚本执行权限，随后直接 ./script.sh 执行

验证点:
  - [正向] chmod 后脚本可执行
  - [正向] 直接执行输出正确

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Set permission and run | run: chmod +x ./scripts/hello.sh
./scripts/hello.sh
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify script permission and execution
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Set permission and run
        run: |
          chmod +x ./scripts/hello.sh
          ./scripts/hello.sh

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
| [正向] chmod 后脚本可执行 | ✅ COVERED | steps have real logic |
| [正向] 直接执行输出正确 | ✅ COVERED | steps have real logic |

### 问题

无

---
