# COMP-STATUS-01-002

- **标题**: 失败 step 的日志完整保留且可查看
- **维度**: 完备性
- **评级**: 部分不符

---

## 想测什么
验证失败 step 前后的日志完整保留。

## 做了什么
Step 1: `echo "BEFORE_FAILURE_MARKER"`（字面量 echo）。Step 2: `echo "ERROR_MARKER" && exit 1`（echo + 真实 exit 命令）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains BEFORE_FAILURE_MARKER | TRIVIAL | Step 1 仅 echo 字面量 |
| 2 | run_logs | positive | contains ERROR_MARKER | COVERED | Step 2 含 `exit 1` 真实命令，echo 是失败前的探针，整个 step 非 trivial |
