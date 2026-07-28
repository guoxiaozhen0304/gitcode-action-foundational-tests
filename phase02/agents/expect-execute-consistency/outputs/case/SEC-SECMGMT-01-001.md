# SEC-SECMGMT-01-001
- **标题**: Secret 写入后任何 API/UI 路径绝不应回读明文
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
验证 secret 写入后，任何读取接口/UI 均不返回明文；workflow 正常引用且日志脱敏。

## 做了什么
workflow 中通过 `${{ secrets.DEPLOY_TOKEN }}` 引用 secret 并 echo 输出，由平台脱敏机制确保不泄露。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | masked_with_asterisks | COVERED | `echo "SECRET_REFERENCE_CHECK: ${{ secrets.DEPLOY_TOKEN }}"` — 真实表达式引用 secret，平台日志脱敏验证 |
| 2 | secret_mgmt_api | negative | must_not_contain_secret | COVERED | 外部 API 面验证，harness 可调用管理面 API 检查明文不回读 |

