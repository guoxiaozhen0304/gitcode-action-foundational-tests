# COMP-ISOLATION-01-004

- **标题**: 托管 Runner 上特权 options 与敏感路径挂载的边界核查
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证托管 Runner 不应允许无限制挂载宿主敏感路径（`/:/host-root`）或传入提权类 docker options（`--privileged`、`--network=host`）。

## 做了什么
job 定义 `container.options: --privileged --network=host` 及 `volumes: /:/host-root`；step 检测 `/host-root/etc` 目录存在性，若存在输出 `HOST_ROOT_READABLE`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_contain: HOST_ROOT_READABLE | COVERED | 若挂载生效会输出 HOST_ROOT_READABLE；负向断言其不出现 = 宿主访问被阻止 |
| 2 | privilege_boundary | negative | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
