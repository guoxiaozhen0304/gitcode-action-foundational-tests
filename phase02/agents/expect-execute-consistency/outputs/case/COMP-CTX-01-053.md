# COMP-CTX-01-053

- **标题**: 上下文在 Action 插件参数中注入验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `uses:` 步骤的 `with:` 参数中 `atomgit` 上下文可正常解析并传入 Action。

## 做了什么
checkout action 的 `with.ref` 使用 `${{ atomgit.ref }}`，step 执行完成后 echo `done`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | `${{ atomgit.ref }}` 在 with 参数中求值后传给 checkout action，checkout 实际拉取对应 ref，成功完成 |
