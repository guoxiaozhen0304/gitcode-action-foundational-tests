# REL-FAULT-01-038
- **标题**: 故障注入——artifact 上传中途 runner 被杀，半成品不得作为有效 artifact 出现
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**artifact 上传中途 runner 被杀后半成品不应作为有效 artifact**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-081
通过标准：
1. job 状态=failure，半成品不可见
2. 不应存在可下载但截断的 artifact
3. rerun 后同名 artifact 上传成功且 MD5 一致

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | generate file step | `dd if=/dev/urandom of=upload-probe.bin bs=1M count=100` | - | 100MB 测试文件 |
| 2 | upload artifact step | `uses: upload-artifact` name=upload-kill-probe | - | 上传（被中断） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | kill_runner at 50% artifact upload |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = failure | positive | - | ✅ GENUINE | kill_runner 在 upload 50% 时注入 → 真实 job 失败 |
| 2 | truncated_artifact_downloadable = true | negative | - | ✅ GENUINE | uses upload-artifact action + kill 中断，harness 验证无半成品 |
| 3 | rerun_upload_md5_match = true | positive | - | ✅ GENUINE | rerun 后完整上传，harness 验证 MD5 |
---
