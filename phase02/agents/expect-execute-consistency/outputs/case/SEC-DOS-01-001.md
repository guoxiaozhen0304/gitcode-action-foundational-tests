# SEC-DOS-01-001
- **标题**: 大 artifact / 大 cache 必须受配额与边界限制
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**超过大小上限的 artifact 上传应失败并报明确错误**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-033
通过标准：
1. 上传不成功
2. 日志包含 size_limit_exceeded_error
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Create large file | `dd if=/dev/zero of=large.bin bs=1M count=1100` | — | 1.1GB 文件 |
| 2 | Upload large artifact | `uses: upload-artifact` with name=large-artifact, path=large.bin | — | artifact 上传/失败 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status != success | negative | must_not_equal "success" | ✅ GENUINE | uses: upload-artifact 上传超大文件，依赖平台配额限制的真实行为；上传超限可能失败 |
| 2 | size_limit_exceeded_error | positive | run_logs equals | ❌ VACUOUS | uses: upload-artifact 的实际错误文本不会是 "size_limit_exceeded_error" 字面量；该值为外部判定器语义标签 |
### 问题
断言 2 VACUOUS：action 输出的是平台原始错误消息，不会精确匹配下划线语义标签。
---
