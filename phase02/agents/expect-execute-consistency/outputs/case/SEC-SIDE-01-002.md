# SEC-SIDE-01-002
- **标题**: Secret 不经 artifact 侧信道绕过脱敏外泄
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**Secret 不经 artifact 侧信道绕过脱敏外泄**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-032
通过标准：
1. Artifact 中不应包含 secret 明文
2. 若 artifact 包含 secret，应被拦截或遮蔽

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Write secret to file | `echo "token=${{ secrets.DEPLOY_TOKEN }}" > secret.txt` | - | 将 secret 写入文件 |
| 2 | Upload artifact | uses: upload-artifact | - | 上传含 secret 的文件为 artifact |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | [DEPLOY_TOKEN] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | artifact_content | negative | must_not_contain_secret: "DEPLOY_TOKEN" | ✅ GENUINE | 步骤真实写入 secret 到文件并通过 `uses: upload-artifact` 上传，artifact 内容由平台脱敏或拦截 |
| 2 | run_status | positive | equals: "blocked_or_masked" | ✅ GENUINE | 步骤使用 `uses:` action 和 `${{ secrets.DEPLOY_TOKEN }}`，平台可能阻止或遮蔽该运行 |
---
