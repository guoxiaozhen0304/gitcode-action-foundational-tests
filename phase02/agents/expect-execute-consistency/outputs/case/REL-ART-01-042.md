# REL-ART-01-042
- **标题**: artifact 大小上限探测——2GB 上传应完整成功（MD5 一致）或上传阶段明确拒绝
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**artifact 大小上限探测——2GB 上传应完整成功（MD5 一致）或上传阶段明确拒绝**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-078
通过标准：
1. [正向] 上传成功 ↔ 下载 MD5 匹配；上传失败 ↔ 上传阶段明确报错
2. [负向] 不应「上传报成功但 artifact 列表查不到 / 下载 404 / MD5 不匹配」
3. [非功能] 实测 artifact 上限值记录完整，可回写 platform-config

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | generate file step (upload job) | `dd if=/dev/urandom of=big-artifact.bin bs=1M count=2048` → `md5sum big-artifact.bin > expected.md5` | - | 2GB 随机文件 + MD5 |
| 2 | upload artifact step (upload job) | `uses: upload-artifact` with name=big-artifact-2gb, path=big-artifact.bin | - | upload action 内部日志 |
| 3 | download artifact step (download job) | `uses: download-artifact` with name=big-artifact-2gb | needs: upload | download action 内部日志 |
| 4 | verify md5 step (download job) | `md5sum big-artifact-2gb` | needs: upload | 文件 MD5 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | upload_outcome | positive | equals="success_or_explicit_rejection_with_limit" | ✅ GENUINE | `dd` 生成 2GB 文件 + `uses: upload-artifact` 真实上传动作，测试平台 artifact 上限 |
| 2 | md5_match | positive | equals="true_if_upload_success" | ✅ GENUINE | 步骤计算 `md5sum` 并验证下载后一致性，harness 校验结果 |
| 3 | ghost_artifact_detected | negative | equals="true" | ✅ GENUINE | harness 检测不应出现 ghost artifact（上传成功但列表不可见） |
| 4 | measured_artifact_limit | nonfunctional | equals="recorded" | 🔶 LLM_DEPENDENT | 非功能：上限值记录回写 |

---
