# REL-OUTPUT-01-016

- **标题**: step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-016

通过标准：
1. type=positive, target=step_output_length, equals=1048576

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | write 1MB output | `python3 -c "print('A'*1048576)" > out.txt echo "data=$(cat out.txt)" >> $ATOMGIT` |  | ✅ GENUINE |
| 2 | read 1MB output | `echo "${{{{ steps.writer.outputs.data }}}}" test $(echo "${{{{ steps.writer.outp` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: output boundary test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: write 1MB output
        id: writer
        run: |
          python3 -c "print('A'*1048576)" > out.txt
          echo "data=$(cat out.txt)" >> $ATOMGIT_OUTPUT
      - name: read 1MB output
        run: |
          echo "${{{{ steps.writer.outputs.data }}}}"
          test $(echo "${{{{ steps.writer.outputs.data }}}}" | wc -c) -ge 1048576
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
| 1 | step_output_length | positive | equals=1048576 | ✅ GENUINE | 断言有条件可被步骤验证 |

---