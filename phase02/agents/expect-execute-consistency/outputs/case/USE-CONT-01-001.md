# USE-CONT-01-001
- **标题**: container.image 文档声明可用与实际可用性的一致性
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**container.image 文档声明可用与实际可用性的一致性**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-042
通过标准：
1. 记录平台对 container.image 的实际处理行为
2. 文档不应把不可用的能力以正式语法呈现且不加状态标注
3. 能力可用性状态应在字段说明旁显式标注

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | inside container | `echo "in-container"` | container.image: ubuntu:22.04 | 仅 echo |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result | positive | eval: "deterministic" | ❌ MISSING_SOURCE | target=validation_result (eval deterministic)，非 run_logs/run_status，workflow 步骤不直接产生该断言输出 |
| 2 | documentation | negative | eval: "deterministic" | ❌ MISSING_SOURCE | target=documentation，依赖 harness 侧静态扫描，workflow 无法产生 |

### 问题
**断言 1, 2 — MISSING_SOURCE**: 两个断言 target (validation_result, documentation) 均非 workflow 步骤直接产生的输出类型。workflow 仅作为 container.image 探针存在，断言结果需 harness 外部比对。
---
