# REL-NETFAULT-01-062
- **标题**: 网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-062
通过标准：
1. 可达地址成功
2. 不可达地址超时 ≤60s
3. 失败归因清晰

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | curl unreachable addresses | `curl --connect-timeout 10 --max-time 120 -v http://192.0.2.1/ \|\| true; curl --connect-timeout 10 --max-time 120 -v http://nonexistent-domain-test.example/ \|\| true` | — | curl 向不可达地址发起请求（|| true 始终成功） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | reachable_status = success | positive | — | ❌ MISSING_SOURCE | YAML 中无任何 curl 可达地址的步骤，仅有两个不可达地址的 curl。文本描述需依次 curl 可达与不可达端点，但 YAML 缺少可达地址测试 |
| 2 | unreachable_timeout_seconds ≤ 60 | positive | — | ⚠️ STATUS_GUARANTEED | `--max-time 120` 且 `|| true` 确保 job 始终成功。断言目标 `unreachable_timeout_seconds` 无对应 step 输出，为 harness 观测，但 step 本身使用真实 curl 命令访问不可达地址 |
| 3 | failure_attribution = clear | positive | — | ❌ VACUOUS | `|| true` 使 step 永不失败，无明确失败归因；且文本描述有可达地址验证但 YAML 未实现 |
### 问题
1. YAML 缺少文本描述的"可达地址 curl"步骤，reachable_status 断言无对应 step
2. 所有 curl 后面都加了 `|| true` 确保 step 始终成功，无法验证真实失败归因
3. unreachable_timeout_seconds 非出自 step 输出，依赖 harness 外部计时
---
