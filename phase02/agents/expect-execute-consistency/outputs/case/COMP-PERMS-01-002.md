# COMP-PERMS-01-002

- **标题**: 声明 repository write 后 TOKEN 可推送代码
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `permissions: { repository: write }` 下 ATOMGIT_TOKEN 可用于推送代码。

## 做了什么
workflow 级 `permissions: { repository: write }`；step 执行真实 git push 以 `$ATOMGIT_TOKEN` 认证，推送包含 `${{ atomgit.server_url }}` 和 `${{ atomgit.repository }}` 上下文。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | 真实 git push 操作验证 write 权限生效 |
