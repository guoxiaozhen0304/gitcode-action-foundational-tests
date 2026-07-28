# COMP-STEP-01-069

- **标题**: step 必填与核心字段 name run uses 验证
- **维度**: 完备性
- **评级**: 部分不符

---

## 想测什么
验证 step 的 name + run 和 name + uses 基本组合。

## 做了什么
Step 1: `echo "run_ok"`（字面量 echo）。Step 2: `uses: checkout`（真实 action 插件）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain run_ok | TRIVIAL | Step 1 仅 echo 字面量 |
| 2 | run_status | positive | equals success | COVERED | Step 2 uses checkout action，可真实失败 |
