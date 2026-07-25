# REL-BIGRUNNER-01-066

- 标题: 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率

- [正向] 成功率≥90%
- [正向] 失败归因明确
- [负向] 不应出现同一规格今天成功明天失败

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | compile step | echo compiling sleep 30 | - |
| 2 | compile step | echo compiling sleep 30 | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | success_rate |  |
| positive | failure_attribution | clear |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 成功率≥90% | WEAK | assertions present but all steps trivial |
| [正向] 失败归因明确 | WEAK | assertions present but all steps trivial |
| [负向] 不应出现同一规格今天成功明天失败 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [正向] 成功率≥90%: assertions present but all steps trivial
- [正向] 失败归因明确: assertions present but all steps trivial
- [负向] 不应出现同一规格今天成功明天失败: single dispatch cannot prove negative

---
