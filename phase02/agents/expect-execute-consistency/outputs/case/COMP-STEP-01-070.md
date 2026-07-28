# COMP-STEP-01-070

- **标题**: step 可选字段 id env if with 验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 step 的 id / env / if 可选字段生效。

## 做了什么
Step 1: `id: mystep`, `echo "result=hello" >> "$ATOMGIT_OUTPUT"`（写入 ATOMGIT_OUTPUT—GENUINE）。Step 2: `echo "OUT=${{ steps.mystep.outputs.result }}"`（`${{ }}` 引用 step 输出）。Step 3: `if: ${{ true }}`, env STEP_VAR, `echo "STEP_VAR=$STEP_VAR"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain OUT=hello | COVERED | Step 1 写入 $ATOMGIT_OUTPUT 是真实验；Step 2 使用 ${{ steps.*.outputs.* }} 表达式读取 |
| 2 | run_logs | positive | must_contain STEP_VAR=step_value | COVERED | Step 3 含 if: ${{ true }} 条件 + env 注入，产生真实 env 变量输出 |
