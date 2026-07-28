# REL-CACHE-01-047
- **标题**: cache 容量上限探测——500MB/1GB/2GB 单 cache 的接受/拒绝语义
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
补真实读回对账：新增 readback job（needs: save）restore 各档位 cache 并 md5sum -c 校验，损坏输出 READBACK_MD5_BAD_ 并 exit 1，超限拒绝时输出 CACHE_RESTORE_MISS_；readback_md5_match 断言改 must_not_contain READBACK_MD5_BAD_（确定性）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | write_outcome | positive | accepted_or_explicit_rejection_with_limit | ✅ GENUINE | cache action + dd 真实命令 |
| 2 | run_logs | negative | must_not_contain READBACK_MD5_BAD_ | ✅ GENUINE | 真实 md5 对账，损坏即出现 |
| 3 | silent_corruption_detected | negative | equals true | ✅ GENUINE | 负向验证 |
| 4 | measured_cache_limit | nonfunctional | equals recorded | 🔶 LLM_DEPENDENT | 上限实测记录非机器可判值 |

### 残留问题
measured_cache_limit=recorded 为实测记录指令，无数值阈值可机器判定，保留（YAML 已注释）。
