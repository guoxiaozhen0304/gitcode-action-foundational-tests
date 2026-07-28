# COMP-ISOLATION-01-003

- **标题**: container.volumes 常规挂载在托管 Runner 的行为记录
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
记录托管 Runner 对 `container.volumes` 声明的处理行为（正常执行 / 报错）。

## 做了什么
job 定义 `container.image: ubuntu:22.04` 及 `volumes: /tmp/build-cache:/cache`；step 探针输出 `CONTAINER_PROBE_OK` 并尝试写入挂载路径。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | container_handling | nonfunctional | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
| 2 | silent_ignore | negative | eval: llm_assisted | COVERED | LLM_DEPENDENT 断言 |
