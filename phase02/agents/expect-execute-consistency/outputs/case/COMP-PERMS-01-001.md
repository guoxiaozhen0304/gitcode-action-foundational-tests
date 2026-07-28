# COMP-PERMS-01-001

- **标题**: permissions 空对象时 ATOMGIT_TOKEN 仅 repository read
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `permissions: {}` 下 ATOMGIT_TOKEN 仅有 read 权限，写操作（git push）应失败返回 403。

## 做了什么
workflow 级 `permissions: {}`；step 执行真实 git 操作（config、add、commit、push）以 `$ATOMGIT_TOKEN` 认证推送代码。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success | COVERED | 缺少 write 权限的 push 应失败，status != success 有意义 |
| 2 | run_logs | positive | contains: 403 | COVERED | git push 失败时输出 HTTP 403 状态码，trace 到真实的权限拒绝 |
