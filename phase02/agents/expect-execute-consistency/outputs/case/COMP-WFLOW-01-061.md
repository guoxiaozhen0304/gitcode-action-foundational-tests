# COMP-WFLOW-01-061

- **标题**: workflow name 与 on 字段必填与类型验证
- **维度**: 完备性
- **评级**: 部分不符

---

## 想测什么
验证 workflow 含 name 字段被正确显示，on 为 map 时 workflow 可被触发。

## 做了什么
声明 name 和 on.workflow_dispatch，verify job echo "workflow_ok"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | TRIVIAL | 仅有 echo 步骤，无条件失败路径，必然成功 |
| 2 | run_logs | positive | must_contain: workflow_ok | COVERED | run 步骤直接 echo 该字符串 |
