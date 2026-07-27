# COMP-PERMS-01-001

- **标题**: permissions 空对象时 ATOMGIT_TOKEN 仅 repository read
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**permissions 空对象时 ATOMGIT_TOKEN 仅 repository read**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-013

通过标准：
1. [正向] permissions: {} 下无法执行写操作 —— 断言 run_status != success
2. [负向] 推送代码应返回 403 —— 断言 run_logs contains 403

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt write | `git config` + `echo "change" >> README.md` + `git add` + `git commit` + `git push https://x-access-token:$ATOMGIT_TOKEN@${{ atomgit.server_url }}/...` | permissions: {} | git push 结果（预期 403） |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success | ✅ GENUINE | `git push` 是真实 git 操作，使用 $ATOMGIT_TOKEN 和 `${{ atomgit.server_url }}` 等平台上下文；权限不足时 push 失败 |
| 2 | run_logs | positive | contains: 403 | ✅ GENUINE | git push 失败时 git 输出 403 状态码，真实被测行为 |

