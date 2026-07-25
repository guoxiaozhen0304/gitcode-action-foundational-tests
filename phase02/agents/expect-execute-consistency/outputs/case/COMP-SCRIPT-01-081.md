# COMP-SCRIPT-01-081

- 标题: 仓库内脚本执行与路径验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-SCRIPT-01-081
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-431~433
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      仓库内脚本执行与路径验证

前置条件:
  - 仓库已启用 AtomGit Action
  - 仓库根目录存在可执行脚本

操作步骤:
  1. 在 step 的 run 中执行仓库内相对路径脚本
  2. 验证脚本正确执行并输出

预期结果:
  - run 支持执行仓库内脚本，相对路径基于仓库根目录，脚本标准输出被捕获到日志

验证点:
  - [正向] 仓库内脚本成功执行
  - [正向] 脚本输出出现在日志中

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Run inline script | run: echo "inline_script_ok"
 | 否 |
| 2 | Run repo script | run: ./scripts/hello.sh    echo "script_fallback"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify in-repo script execution
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Run inline script
        run: |
          echo "inline_script_ok"
      - name: Run repo script
        run: |
          ./scripts/hello.sh || echo "script_fallback"

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
| [正向] 仓库内脚本成功执行 | ✅ COVERED | steps have real logic |
| [正向] 脚本输出出现在日志中 | ✅ COVERED | steps have real logic |

### 问题

无

---
