# COMP-ISOLATION-01-003

- **标题**: container.volumes 常规挂载在托管 Runner 的行为记录
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**container.volumes 常规挂载在托管 Runner 的行为记录**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-025

通过标准：
1. [正向/记录] 常规 volumes 挂载是否按声明工作 —— 🔶 LLM_DEPENDENT
2. [非功能] credentials/env/options 组合下的行为一致性 —— 🔶 LLM_DEPENDENT
3. [负向] volumes 声明不应被静默忽略 —— 🔶 LLM_DEPENDENT

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Probe container env | `echo "CONTAINER_PROBE_OK"` + `touch /cache/probe_marker && echo "VOLUME_WRITE_OK"` | - (container: image: ubuntu:22.04, volumes: /tmp/build-cache:/cache) | 容器内探针输出和卷写入结果 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | container_handling | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |
| 2 | silent_ignore | negative | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |

