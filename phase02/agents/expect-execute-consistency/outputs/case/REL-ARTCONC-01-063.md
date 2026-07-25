# REL-ARTCONC-01-063

- 标题: 制品并发写一致性——多 job 同时 upload-artifact 同名 artifact
- 维度: 稳定性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: 制品并发写一致性——多 job 同时 upload-artifact 同名 artifact

- [正向] 下载内容确定
- [负向] 不应出现 ABA/BAB 等混合态

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | generate content | if [ "${{{{ matrix.instance }}}}" = "1" ]; then python3 -c "print('A'*1048576)" > out.txt; fi if [ " | Y |
| 2 | upload artifact step | uses: upload-artifact | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | download_content |  |
| negative | download_content |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 下载内容确定 | COVERED | 2 real steps, assertions present |
| [负向] 不应出现 ABA/BAB 等混合态 | COVERED | negative assertion present |

### 问题

无重大问题。

---
