# REL-ARTPERF-01-053
- **标题**: 制品传输性能——100MB artifact 上传下载耗时
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**100MB artifact 上传下载性能——hash 匹配**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-053
通过标准：
1. 上传≤30s
2. 下载≤30s
3. hash 100% 匹配

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | generate 100MB file | `dd if=/dev/urandom of=artifact.bin bs=1M count=100` | - | 100MB 随机文件 |
| 2 | upload artifact step | `uses: upload-artifact` | - | 上传 |
| 3 | download artifact step | `uses: download-artifact` | - | 下载 |
| 4 | verify artifact step | `ls -la perf-artifact` | - | 仅列出文件信息 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | upload_time_seconds le 30 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量 |
| 2 | download_time_seconds le 30 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量 |
| 3 | hash_match = true | positive | - | ❌ MISSING_SOURCE | 步骤仅执行 `ls -la perf-artifact`，无任何 hash 计算或比对逻辑 |
### 问题
**断言 3 — MISSING_SOURCE**: verify artifact step 仅执行 `ls -la perf-artifact`，未计算原始文件与下载文件的 hash 校验和。hash_match 断言在 workflow 中无对应步骤产出。
---
