# REL-OUTPUT-01-017

- 标题: step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错

- [正向] step 状态=failure 或日志含 1MB/超出限制
- [负向] 不应静默截断且无提示

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | write 1MB+1 output | python3 -c "print('A'*1048577)" > out.txt echo "data=$(cat out.txt)" >> $ATOMGIT_OUTPUT | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_logs |  |
| positive | job_status | failure |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] step 状态=failure 或日志含 1MB/超出限制 | COVERED | 1 real steps, assertions present |
| [负向] 不应静默截断且无提示 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应静默截断且无提示: single dispatch cannot prove negative

---
