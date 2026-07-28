# COMP-ISOLATION-01-004
- **标题**: 托管 Runner 上特权 options 与敏感路径挂载的边界核查
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
托管 Runner 不应能无限制挂载宿主敏感路径或传入提权类 docker options。

## 做了什么
1. container: image: ubuntu:22.04, options: --privileged --network=host, volumes: /:/host-root
2. step `Probe host access`：检查 /host-root/etc 是否存在，输出 HOST_ROOT_READABLE 或 HOST_ROOT_BLOCKED

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_contain: HOST_ROOT_READABLE | COVERED | 步骤检查宿主根路径可读性，不希望出现 HOST_ROOT_READABLE |
| 2 | privilege_boundary | negative | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
