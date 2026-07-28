# COMP-ISOLATION-01-003
- **标题**: container.volumes 常规挂载在托管 Runner 的行为记录
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
container.image 与 volumes 在托管 Runner 上的行为记录（是否被支持、挂载是否按声明工作）。

## 做了什么
1. container: image: ubuntu:22.04, volumes: /tmp/build-cache:/cache
2. step `Probe container env`：`echo "CONTAINER_PROBE_OK"`，`touch /cache/probe_marker && echo "VOLUME_WRITE_OK"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | container_handling | nonfunctional | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |
| 2 | silent_ignore | negative | llm_assisted | LLM_DEPENDENT | eval=llm_assisted |

注意：所有断言均为 LLM_DEPENDENT，按 Rule 5，LLM_DEPENDENT-only cases → 断言一致。
