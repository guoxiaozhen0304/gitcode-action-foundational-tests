# USE-DISP-01-003
- **标题**: workflow_dispatch 手动触发 UI 与 YAML inputs 定义的集合一致性
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**workflow_dispatch 手动触发 UI 与 YAML inputs 定义的集合一致性**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-051
通过标准：
1. UI 渲染字段集合与 YAML inputs 集合一致
2. UI 不应渲染 YAML 未定义字段，不应漏渲染已定义字段
3. required、default、description 在 UI 均有对应呈现

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | marker step | `echo "dispatched"` | - | 仅 echo |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | ui | positive | eval: "deterministic" | ❌ MISSING_SOURCE | target=ui，无 workflow 步骤产生 UI 渲染 |
| 2 | ui | negative | eval: "deterministic" | ❌ MISSING_SOURCE | target=ui，无 workflow 步骤产生 UI 渲染 |
| 3 | ui | nonfunctional | eval: "deterministic" | ❌ MISSING_SOURCE | target=ui，无 workflow 步骤产生 UI 渲染 |

### 问题
**断言 1, 2, 3 — MISSING_SOURCE**: 三个断言全部 target=ui（手动触发 UI），但 workflow 仅含一个 echo 步骤，无任何步骤产生 UI 渲染数据。UI 一致性检查完全依赖 harness 侧人工/自动化 UI diff。
---
