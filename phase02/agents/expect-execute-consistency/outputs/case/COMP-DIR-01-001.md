# COMP-DIR-01-001

- **标题**: .gitcode/workflows/ 下的 YAML 被正确识别并触发
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**.gitcode/workflows/ 下的 YAML 被正确识别并触发**

- 触发事件: `push`
- 规格引用: INTENT-COMP-001

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_file_path, equals=.gitcode/workflows/ci.yml

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo verify | `echo "workflow recognized"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches:
      - main
jobs:
  verify:
    name: Verify directory recognition
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo verify
        run: |
          echo "workflow recognized"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | ⚠️ STATUS_GUARANTEED | 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功 |
| 2 | run_file_path | positive | equals=.gitcode/workflows/ci.yml | ✅ GENUINE | 断言有条件可被步骤验证 |

### 问题

**断言 1 — STATUS_GUARANTEED**⚠️: 所有步骤均为 echo/trivial 命令，无条件失败路径，永远成功

---