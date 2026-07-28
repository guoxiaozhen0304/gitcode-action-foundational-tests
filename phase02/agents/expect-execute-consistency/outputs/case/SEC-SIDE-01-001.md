# SEC-SIDE-01-001
- **标题**: Secret 不经 output 侧信道绕过脱敏外泄
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
Secret 明文不应以未遮蔽形式出现在 job output 中。

## 做了什么
workflow 将 `${{ secrets.API_KEY }}` 写入 ATOMGIT_OUTPUT，再从 step output 读取，检查是否脱敏。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret: API_KEY | COVERED | `echo "result=${{ secrets.API_KEY }}" >> $ATOMGIT_OUTPUT` 及后续 echo `${{ steps.step1.outputs.result }}`，真实表达式引用 secret，平台脱敏 |
| 2 | step_output | negative | must_not_contain_secret: API_KEY | COVERED | harness 检查 step output 中 secret 已被遮蔽 |

