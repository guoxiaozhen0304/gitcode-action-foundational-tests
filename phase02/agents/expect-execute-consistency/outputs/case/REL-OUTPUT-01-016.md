# REL-OUTPUT-01-016

- 标题: step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: step output 边界值——ATOMGIT_OUTPUT 写入 1 MB 参数应成功传递

- [正向] 下游读取内容长度=1,048,576 bytes
- [负向] 不应截断或丢失

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | write 1MB output | python3 -c "print('A'*1048576)" > out.txt echo "data=$(cat out.txt)" >> $ATOMGIT_OUTPUT | Y |
| 2 | read 1MB output | echo "${{{{ steps.writer.outputs.data }}}}" test $(echo "${{{{ steps.writer.outputs.data }}}}" | wc  | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | step_output_length | 1048576 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 下游读取内容长度=1,048,576 bytes | COVERED | 2 real steps, assertions present |
| [负向] 不应截断或丢失 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应截断或丢失: single dispatch cannot prove negative

---
