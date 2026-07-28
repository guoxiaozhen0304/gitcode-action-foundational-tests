# COMP-CTX-01-053
- **标题**: 上下文在 Action 插件参数中注入验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
Action 的 with 参数中可正常解析 atomgit 上下文。

## 做了什么
1. step `Checkout with explicit token`：`uses: checkout` with `ref: ${{ atomgit.ref }}`
2. step `Echo env in action param`：`echo "done"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | `uses: checkout` 是真实 action 调用，ref 参数使用 ${{ atomgit.ref }} |
