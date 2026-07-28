# COMP-ACT-01-001

- **标题**: action inputs.required 未传参时平台不自动校验
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证平台对 action.yml 声明 `required: true` 的 input 在调用方未传参时不自动校验，action 内读取到的对应环境变量为空值。

## 做了什么
通过 `uses: ./.gitcode/actions/req-check` 调用声明了 required input 的本地 action，action 内部脚本在环境变量为空时输出 `REQ_INPUT_EMPTY` 标记。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | 本地 action `uses:` 执行真实逻辑，workflow 进入 action 内部运行，状态校验有意义 |
| 2 | run_logs | positive | must_contain: REQ_INPUT_EMPTY | COVERED | action 脚本在 required input 环境变量为空时输出该标记 |
