# USE-TOGGLE-01-001
- **标题**: 隐藏安全开关 ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS 默认值与文档缺失
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**隐藏安全开关 ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS 默认值与文档缺失**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-053
通过标准：
1. 记录开关的实际默认值
2. 平台不应存在影响安全行为但文档未提的开关
3. 开关清单应标注每个开关的安全影响与默认值

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo toggle value | `echo "allow_unsecure=[${ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS:-UNSET}]"` | 无 | 环境变量实际注入值或 UNSET |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs 确定性记录开关实际注入值 | positive | `$ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS` 为平台注入环境变量 | ✅ GENUINE | 平台环境变量注入是真实行为，${VAR:-UNSET} 语义依赖平台是否注入 |
| 2 | documentation 确定性校验：文档应列出开关名称、默认值与安全影响 | negative | 确定性文档检查 | ✅ COVERED | 确定性文档校验 |
---
