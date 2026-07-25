# REL-MATRIX-01-038

- 标题: 大规模 matrix——20 个组合应全部生成并正确调度
- 维度: 稳定性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 大规模 matrix——20 个组合应全部生成并正确调度

- [正向] 20 个 jobs 全部生成
- [正向] 矩阵变量校验 100% 通过
- [负向] 不应出现重复组合或遗漏组合

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | verify matrix vars | echo os=${{{{ matrix.os }}}} arch=${{{{ matrix.arch }}}} compiler=${{{{ matrix.compiler }}}} mode=${ | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | generated_jobs_count | 20 |
| positive | run_status | completed(success) |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 20 个 jobs 全部生成 | COVERED | 1 real steps, assertions present |
| [正向] 矩阵变量校验 100% 通过 | COVERED | 1 real steps, assertions present |
| [负向] 不应出现重复组合或遗漏组合 | UNVERIFIABLE | single dispatch cannot prove negative |

### 问题

- [负向] 不应出现重复组合或遗漏组合: single dispatch cannot prove negative

---
