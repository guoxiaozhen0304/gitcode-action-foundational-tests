# COMP-BOUND-01-088

- **标题**: 工作流命令 set-env add-path 与文件写入边界验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**工作流命令 set-env add-path 与文件写入边界验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-088

通过标准：
1. type=positive, target=run_logs, must_contain="MY_ENV=from_env_file"
2. type=positive, target=run_logs, must_contain="commands_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Write env and path | `echo "MY_ENV=from_env_file" >> "$ATOMGIT_ENV" echo "/tmp/extra_bin" >> "$ATOMGIT` |  | ❌ VACUOUS |
| 2 | Read env | `echo "MY_ENV=$MY_ENV" echo "PATH_HAS_EXTRA=$([[ "$PATH" == *"/tmp/extra_bin"* ]]` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
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
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=MY_ENV=from_env_file | ❌ VACUOUS | MY_ENV=from_env_file: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_logs | positive | must_contain=commands_ok | ❌ VACUOUS | commands_ok: VACUOUS (步骤仅 echo，未执行功能) |

### 问题

**断言 1 — VACUOUS**❌: MY_ENV=from_env_file: VACUOUS (步骤仅 echo，未执行功能)

**断言 2 — VACUOUS**❌: commands_ok: VACUOUS (步骤仅 echo，未执行功能)

---