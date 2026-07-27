# USE-ACT-01-004
- **标题**: 文档短名与市场名两种写法解析一致性验证
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**文档短名与市场名两种写法解析一致性验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-052
通过标准：
1. 记录两种写法的解析结果是否一致
2. 两种写法指向不同插件或其一报错而文档未说明即不合格

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | - | 短名引用 |
| 2 | use cache short name | uses: cache | - | 短名引用 |
| 3 | use cache market name | uses: AtomgitCache | - | 市场名引用 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result | positive | eval: "deterministic" | ❌ MISSING_SOURCE | 断言 target=validation_result 非 run_logs/run_status，workflow 步骤不直接产生该 target 输出 |

### 问题
**断言 1 — MISSING_SOURCE**: 虽然 workflow 使用了 `uses: checkout`、`uses: cache`、`uses: AtomgitCache` 等 Actions，但断言 target 为 validation_result（eval=deterministic），属于 harness 侧解析结果比对，非 workflow 步骤直接输出的目标。
---
