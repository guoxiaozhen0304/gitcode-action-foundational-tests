# COMP-PRTARGET-01-001

- **标题**: pull_request_target 默认使用 base 分支 workflow 版本
- **维度**: 完备性
- **评级**: 部分不符

---

## 想测什么
验证 pull_request_target 事件触发时，执行的 workflow 版本来自 base 分支而非 fork 分支。

## 做了什么
单个 step 执行 `echo "BASE_VERSION_MARKER"`，无 `if:` 条件、无 `${{ }}`、无 `uses:` action、无实质命令。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains BASE_VERSION_MARKER | TRIVIAL | 步骤仅 echo 字面量 "BASE_VERSION_MARKER"，无 ${{ }}、无 condition、无 real 命令 |
| 2 | run_logs | negative | must_not_contain FORK_VERSION_MARKER | COVERED | step 只产出 BASE 标记，YAML 有 type=negative 断言，如 fork 含 FORK_VERSION_MARKER 则断言会 fail |
