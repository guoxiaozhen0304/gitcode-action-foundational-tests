# REL-MEM-01-020

- **标题**: Runner 内存边界——small runner 分配 7.5 GB 应成功
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Runner 内存边界——small runner 分配 7.5 GB 应成功**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-020

通过标准：
1. type=positive, target=job_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | allocate 7.5GB | `python3 -c "a=bytearray(7680*1024*1024); print(len(a))"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: memory boundary test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: allocate 7.5GB
        run: |
          python3 -c "a=bytearray(7680*1024*1024); print(len(a))"
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
| 1 | job_status | positive | equals=success | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |

---