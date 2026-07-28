# COMP-WFLOW-01-065

- **标题**: workflow post 后处理阶段字段验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 post 阶段 run_always true 时主 job 失败仍执行 post。

## 做了什么
两个并行主 job（verify 和 failing），failing job 退出 exit 1；post 阶段 run_always: true echo "post_done"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: failure | COVERED | failing job 步骤 exit 1 导致失败 |
| 2 | run_logs | positive | must_contain: main_done | COVERED | verify job echo "main_done" |
| 3 | run_logs | positive | must_contain: post_done | COVERED | post 阶段 run_always true echo "post_done" |
