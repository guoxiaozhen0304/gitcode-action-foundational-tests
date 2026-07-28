# REL-CACHE-01-048
- **标题**: cache 同 key 并发写一致性——3 方并行写同一 key 不得产生混合/损坏内容
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
归属检查步骤由 cat 改为 case 精确匹配：读回内容必须是某一写入方的完整标记（ATTRIBUTION_SINGLE_OK），混合/截断输出 ATTRIBUTION_MIXED_BAD 并 exit 1；新增 must_not_contain ATTRIBUTION_MIXED_BAD 确定性断言。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_content_attribution | positive | single_writer_complete_or_explicit_conflict_error | ✅ GENUINE | 真实 case 匹配校验 |
| 2 | run_logs | negative | must_not_contain ATTRIBUTION_MIXED_BAD | ✅ GENUINE | 混合内容出现时输出并 exit 1 |
| 3 | mixed_or_truncated_content_detected | negative | equals true | ✅ GENUINE | 负向验证 |
| 4 | concurrent_write_semantics | nonfunctional | equals recorded | 🔶 LLM_DEPENDENT | 实测记录指令，非机器可判值 |

### 残留问题
concurrent_write_semantics=recorded 同 REL-CACHE-01-047，保留。
