# REL-CACHEPERF-01-054
- **标题**: 缓存加速比——cache 命中 vs 未命中构建耗时对比
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**cache 命中 vs 未命中构建加速比**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-054
通过标准：
1. 加速比≥2x
2. restore 耗时≤30s

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | restore cache | `uses: cache` key=cache-deps-${{ matrix.run }} | - | cache hit/miss |
| 2 | install deps | `npm ci \|\| true` | - | npm 安装（真实命令） |
| 3 | save cache | `uses: cache` key=cache-deps-${{ matrix.run }} | - | cache 保存 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | speedup_ratio ge 2 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量对比 |
| 2 | restore_time_seconds le 30 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量 |
---
