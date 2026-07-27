# COMP-PERMS-01-002

- **标题**: 声明 repository write 后 TOKEN 可推送代码
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**声明 repository write 后 TOKEN 可推送代码**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-013

通过标准：
1. [正向] 推送代码成功 —— 断言 run_status=success

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Push code | `git config` + `echo "change" >> README.md` + `git add` + `git commit` + `git push https://x-access-token:$ATOMGIT_TOKEN@${{ atomgit.server_url }}/...` | permissions: repository: write | git push 结果 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | `git push` 是真实 git 操作，使用 `$ATOMGIT_TOKEN` 和 `${{ atomgit.server_url }}`、`${{ atomgit.repository }}` 等平台上下文，测试 repository: write 权限的实际效果 |

