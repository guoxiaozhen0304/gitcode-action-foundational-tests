# COMP-WFLOW-01-063

- **标题**: workflow concurrency 并发控制字段验证
- **维度**: 完备性
- **评级**: 部分不符

---

## 想测什么
验证合法 concurrency 配置（max、exceed-action、preemption.events）通过校验。

## 做了什么
workflow 级 concurrency 声明 enable/max/exceed-action/preemption，verify job echo "concurrency_ok"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | TRIVIAL | 仅有 echo 步骤，无条件失败路径，必然成功 |
| 2 | run_logs | positive | must_contain: concurrency_ok | COVERED | run 步骤直接 echo 该字符串 |
