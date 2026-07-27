# REL-ART-01-041
- **标题**: 超大 artifact——100 MB artifact 上传后下游 job 应成功下载
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**超大 artifact——100 MB artifact 上传后下游 job 应成功下载**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-041
通过标准：
1. [正向] upload 成功
2. [正向] download 成功
3. [正向] MD5 校验通过

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | generate 100MB file (upload job) | `dd if=/dev/urandom of=artifact.bin bs=1M count=100` | - | 100MB 随机文件 |
| 2 | upload artifact step (upload job) | `uses: upload-artifact` with name=perf-artifact, path=artifact.bin | - | upload action 内部日志 |
| 3 | download artifact step (download job) | `uses: download-artifact` with name=perf-artifact | needs: upload | download action 内部日志 |
| 4 | verify artifact step (download job) | `ls -la perf-artifact` | needs: upload | 文件列表 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | upload_status | positive | equals="success" | ✅ GENUINE | 步骤使用 `uses: upload-artifact` 真实动作上传 artifact，harness 验证上传结果 |
| 2 | download_status | positive | equals="success" | ✅ GENUINE | 步骤使用 `uses: download-artifact` 真实动作下载 artifact，harness 验证下载结果 |
| 3 | md5_match | positive | equals="true" | ✅ GENUINE | harness 对外部校验上传/下载文件 MD5 一致性 |

---
