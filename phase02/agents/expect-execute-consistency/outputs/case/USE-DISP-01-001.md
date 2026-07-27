# USE-DISP-01-001
- **标题**: workflow_dispatch 必填参数未提供时应给出明确校验错误
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**workflow_dispatch 必填参数未提供时应给出明确校验错误**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-030
通过标准：
1. 不应在缺少必填参数时触发运行
2. 报错中是否指出具体缺少的字段名

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo env | `echo "env=${{ inputs.environment }}"` | - | 仅 echo（若运行被触发） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: COMPLETED | ✅ GENUINE | YAML 定义 environment 为 required:true 但 params:{}（不提供），平台应拒绝执行。平台验证型测试 |
| 2 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 判定报错文本 |
---
