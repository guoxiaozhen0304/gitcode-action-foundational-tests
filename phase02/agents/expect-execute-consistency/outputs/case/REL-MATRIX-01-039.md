# REL-MATRIX-01-039
- **标题**: 大规模 matrix——50 个组合应全部生成并正确调度
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**大规模 matrix——50 个组合应全部生成并正确调度**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-039
通过标准：
1. 50 个 jobs 全部生成
2. 调度时延 ≤300 秒（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | verify matrix vars | `echo v1=${{ matrix.v1 }} v2=${{ matrix.v2 }}` | — | 输出矩阵变量组合值 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | generated_jobs_count = 50 | positive | — | ✅ GENUINE | v1[5]×v2[10]=50 组合，step 使用 `${{ matrix.* }}` 表达式，对平台大规模 matrix 调度能力构成真实负载 |
| 2 | scheduling_latency_seconds ≤ 300 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
