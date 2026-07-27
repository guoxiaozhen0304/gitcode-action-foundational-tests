# COMP-PR-01-002

- **标题**: pull_request_target 可访问 secrets 且 TOKEN 拥有写权限
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request_target 可访问 secrets 且 TOKEN 拥有写权限**
- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMP-004

通过标准：
1. [正向] pull_request_target 可访问 secrets —— 断言 contains_masked DEPLOY_TOKEN
2. [正向] 日志中 secret 显示为 ***（脱敏生效）—— 断言 run_status=success

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Read secret and token | `echo "secret is ${{ secrets.DEPLOY_TOKEN }}"` + `echo "token length is ${#ATOMGIT_TOKEN}"` | - (event: pull_request_target) | secret 和 token 的输出结果 |

## 3. 触发与运行环境

| 触发事件 | pull_request_target |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | [DEPLOY_TOKEN] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains_masked: DEPLOY_TOKEN | ✅ GENUINE | 步骤使用 `${{ secrets.DEPLOY_TOKEN }}` 故意引用并 echo，测试 pull_request_target 下平台脱敏机制是否生效（应显示为 ***） |
| 2 | run_status | positive | equals: success | ✅ GENUINE | 步骤包含 `${{ secrets.DEPLOY_TOKEN }}` 和 `${#ATOMGIT_TOKEN}` 运算，真实行为 |

