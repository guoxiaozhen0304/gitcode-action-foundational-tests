# SEC-SIDE-01-001
- **标题**: Secret 不经 output 侧信道绕过脱敏外泄
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**Secret 不经 output 侧信道绕过脱敏外泄**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-032
通过标准：
1. Secret 明文不应以未遮蔽形式出现在 job output 中
2. output 中 secret 值应为 *** 或被拦截

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Write secret to output | `echo "result=${{ secrets.API_KEY }}" >> $ATOMGIT_OUTPUT` | - | 将 secret 写入 output 文件 |
| 2 | Check output masked | `echo "output is ${{ steps.step1.outputs.result }}"` | - | 读取 output 并打印（平台应脱敏） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | [API_KEY] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret: "API_KEY" | ✅ GENUINE | 步骤真实将 secret 写入 ATOMGIT_OUTPUT 后回读，平台应对输出脱敏 |
| 2 | step_output | negative | must_not_contain_secret: "API_KEY" | ✅ GENUINE | 步骤 1 使用 `${{ secrets.API_KEY }}` 写入 output，真实检测侧信道泄露 |
---
