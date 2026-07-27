# REL-CACHE-01-048
- **标题**: cache 同 key 并发写一致性——3 方并行写同一 key 不得产生混合/损坏内容
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**3 方并行写同一 cache key 不得产生混合/损坏内容**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-079
通过标准：
1. 读回内容完整且可归属单一写入方
2. 读回内容不应为混合态
3. 并发写语义实测结论记录

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | cache write step | `uses: cache` key=concurrent-same-key-probe | - | cache 保存 |
| 2 | write marker step | `echo "writer_${{ matrix.writer_id }}_full_content_marker" > shared_cache/owner.txt` | - | 写入标记 |
| 3 | cache restore step | `uses: cache` key=concurrent-same-key-probe | - | cache 恢复 |
| 4 | check attribution step | `cat shared_cache/owner.txt \|\| echo "cache_miss"` | - | 查看归属 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_content_attribution = single_writer_complete_or_explicit_conflict_error | positive | - | ✅ GENUINE | uses cache action + ${{ matrix.writer_id }} 表达式 + cat 真实命令 |
| 2 | mixed_or_truncated_content_detected = true | negative | - | ✅ GENUINE | 负向验证无混合内容 |
| 3 | concurrent_write_semantics = recorded | nonfunctional | - | 🔶 LLM_DEPENDENT | 非功能指标 |
---
