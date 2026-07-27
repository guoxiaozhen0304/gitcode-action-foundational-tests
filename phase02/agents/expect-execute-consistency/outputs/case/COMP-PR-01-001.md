# COMP-PR-01-001

- **标题**: fork PR 触发 pull_request 时不可读取项目 secrets
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 触发 pull_request 时不可读取项目 secrets**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-004

通过标准：
1. [负向] 日志不含 DEPLOY_TOKEN 明文 —— 断言 must_not_contain_secret DEPLOY_TOKEN
2. [正向] fork PR 的 pull_request workflow 无 secret 访问权限 —— 断言 run_status=success_or_blocked

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt to read secret | `echo "secret value is ${{ secrets.DEPLOY_TOKEN }}"` | - (as: untrusted_contributor, event: pull_request) | 平台对 secret 的处理结果（脱敏或拒绝） |

## 3. 触发与运行环境

| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | with-secrets |
| Secrets | [DEPLOY_TOKEN] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret: DEPLOY_TOKEN | ✅ GENUINE | 步骤使用 `${{ secrets.DEPLOY_TOKEN }}` 故意引用 secret，测试 fork PR 下平台是否正确拦截/脱敏 |
| 2 | run_status | positive | equals: success_or_blocked | ✅ GENUINE | 步骤包含 `${{ secrets.DEPLOY_TOKEN }}` 表达式，平台上下文求值即真实行为 |

