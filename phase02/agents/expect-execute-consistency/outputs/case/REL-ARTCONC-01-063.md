# REL-ARTCONC-01-063

- **标题**: 制品并发写一致性——多 job 同时 upload-artifact 同名 artifact
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**制品并发写一致性——多 job 同时 upload-artifact 同名 artifact**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-063

通过标准：
1. type=positive, target=download_content
2. type=negative, target=download_content

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | generate content | `if [ "${{{{ matrix.instance }}}}" = "1" ]; then python3 -c "print('A'*1048576)" ` |  | ✅ GENUINE |
| 2 | upload artifact step | `upload-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: artifact concurrent write test
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        instance: [1,2,3]
    steps:
      - name: generate content
        run: |
          if [ "${{{{ matrix.instance }}}}" = "1" ]; then python3 -c "print('A'*1048576)" > out.txt; fi
          if [ "${{{{ matrix.instance }}}}" = "2" ]; then python3 -c "print('B'*1048576)" > out.txt; fi
          if [ "${{{{ matrix.instance }}}}" = "3" ]; then python3 -c "print('C'*1048576)" > out.txt; fi
      - name: upload artifact step
        uses: upload-artifact
        with:
          name: concurrent-artifact
          path: out.txt
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
| 1 | download_content | positive |  | ✅ GENUINE | 通用断言匹配 |
| 2 | download_content | negative |  | ✅ GENUINE | 通用断言匹配 |

---