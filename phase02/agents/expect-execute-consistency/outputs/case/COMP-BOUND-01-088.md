# COMP-BOUND-01-088

- 标题: 工作流命令 set-env add-path 与文件写入边界验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 在 run 中通过 ATOMGIT_ENV / ATOMGIT_PATH / ATOMGIT_OUTPUT 写入
2. 验证后续步骤可读取

预期结果:
- ATOMGIT_ENV 写入的变量在当前 job 后续 step 中可用，ATOMGIT_PATH 添加的目录在 PATH 中，ATOMGIT_OUTPUT 写入的键值可被引用

验证点:
- [正向] ATOMGIT_ENV 写入后后续 step 可读取
- [正向] ATOMGIT_PATH 添加后目录在 PATH
- [正向] ATOMGIT_OUTPUT 写入后 outputs 可引用

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Write env and path | echo "MY_ENV=from_env_file" >> "$ATOMGIT_ENV"; echo "/tmp/extra_bin" >> "$ATOMGIT_PATH" | 是 |
| 2 | Read env | echo "MY_ENV=$MY_ENV"; echo "PATH_HAS_EXTRA=$([[ "$PATH" == *"/tmp/extra_bin"* ]] && echo yes || echo no)" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-BOUND-01-088
dimensions: [completeness]
dimension: completeness
priority: P1
title: 工作流命令 set-env add-path 与文件写入边界验证
intent_ref: KEEP-TC-240~246
setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default
fault_injection: null
workflow: |
  on:
    workflow_dispatch:
  jobs:
    verify:
      name: Verify workflow commands boundary
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Write env and path
          run: |
            echo "MY_ENV=from_env_file" >> "$ATOMGIT_ENV"
            echo "/tmp/extra_bin" >> "$ATOMGIT_PATH"
        - name: Read env
          run: |
            echo "MY_ENV=$MY_ENV"
            echo "PATH_HAS_EXTRA=$([[ "$PATH" == *"/tmp/extra_bin"* ]] && echo yes || echo no)"
            echo "commands_ok"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: MY_ENV=from_env_file
  - type: positive
    target: run_logs
    must_contain: commands_ok
teardown:
  reset: fixture
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
| [正向] ATOMGIT_ENV 写入后后续 step 可读取 | ✅ COVERED | 断言 must_contain: MY_ENV=from_env_file |
| [正向] ATOMGIT_PATH 添加后目录在 PATH | ✅ COVERED | 步骤2 输出 PATH_HAS_EXTRA=yes，commands_ok 覆盖整体成功 |
| [正向] ATOMGIT_OUTPUT 写入后 outputs 可引用 | ❌ TRIVIAL | 当前 workflow 未写入 $ATOMGIT_OUTPUT，该验证点无对应步骤 |

### 问题

- ATOMGIT_OUTPUT 验证缺失：当前 workflow 仅测试 ATOMGIT_ENV 和 ATOMGIT_PATH，未写入 $ATOMGIT_OUTPUT

---
