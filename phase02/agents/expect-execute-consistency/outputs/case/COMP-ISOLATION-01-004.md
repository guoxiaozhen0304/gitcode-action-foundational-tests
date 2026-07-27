# COMP-ISOLATION-01-004

- **标题**: 托管 Runner 上特权 options 与敏感路径挂载的边界核查
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**托管 Runner 上特权 options 与敏感路径挂载的边界核查**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-025

通过标准：
1. [负向] 不应能读取宿主敏感路径内容 —— 断言 must_contain HOST_ROOT_READABLE（负向，期望不出现）
2. [负向] 提权类 docker options 不应被无过滤放行 —— 🔶 LLM_DEPENDENT（跳过）
3. [非功能] 记录拒绝时的报错信息 —— 🔶 LLM_DEPENDENT（跳过）

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Probe host access | `if [ -d /host-root/etc ]; then echo "HOST_ROOT_READABLE"; else echo "HOST_ROOT_BLOCKED"; fi` | - (container: image: ubuntu:22.04, options: --privileged --network=host, volumes: /:/host-root) | 探测宿主根路径可读性 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_contain: HOST_ROOT_READABLE | ✅ GENUINE | 步骤使用真实 bash `if [ -d ]` 命令检测宿主路径；若平台正确拦截则输出 HOST_ROOT_BLOCKED，负向断言成立 |
| 2 | privilege_boundary | negative | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |

