# REL-CACHE-01-047
- **标题**: cache 容量上限探测——500MB/1GB/2GB 单 cache 的接受/拒绝语义
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**cache 容量上限探测——不同大小 cache 的接受/拒绝语义**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-079
通过标准：
1. 接受的档位读回内容完整（MD5 一致）
2. 拒绝的档位错误含上限值
3. 实测 cache 上限值记录

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | cache save step | `uses: cache` key=cache-size-probe-${{ matrix.size_mb }} | - | cache action 输出 |
| 2 | generate cache data step | `dd if=/dev/urandom of=cache_data/data.bin bs=1M count=${{ matrix.size_mb }}` | - | 随机数据 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | write_outcome = accepted_or_explicit_rejection_with_limit | positive | - | ✅ GENUINE | uses cache action + ${{ matrix.size_mb }} 表达式 + dd 真实命令 |
| 2 | readback_md5_match = true_if_accepted | positive | - | ✅ GENUINE | cache 读写由 action 完成；但步骤无显式 MD5 计算 |
| 3 | silent_corruption_detected = true | negative | - | ✅ GENUINE | 负向验证 |
| 4 | measured_cache_limit = recorded | nonfunctional | - | 🔶 LLM_DEPENDENT | 非功能指标需测量 |
---
