# USE-UNKN-01-003
- **标题**: step 标识 id 与 identifier 命名双轨的接受一致性与文档说明
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**step 标识 id 与 identifier 命名双轨的接受一致性与文档说明**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-036
通过标准：
1. 记录平台对两种写法的接受情况与行为一致性
2. 两种写法并存且行为不同而文档未说明差异即不合格

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | produce value (id 写法) | 写 `$ATOMGIT_OUTPUT`，用 `id: producer` | 无 | 设置 step output |
| 2 | consume value | `echo "via-id=[${{ steps.producer.outputs.result }}]"` | 无 | 通过 id 引用 output |
| 3 | produce value alt (identifier 写法) | 写 `$ATOMGIT_OUTPUT`，用 `identifier: producer` | 无 | 验证 identifier 别名是否可用 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result 确定性记录两种写法的接受情况和求值行为 | positive | `${{ steps.producer.outputs.result }}` 表达式 + `$ATOMGIT_OUTPUT` 平台环境变量 | ✅ GENUINE | 表达式求值 + 平台环境变量涉及真实行为；identifier 别名识别也是平台行为 |
| 2 | documentation 确定性校验：diff 文档字段集合与样本字段集合 | negative | 确定性文档检查 | ✅ COVERED | 确定性文档校验 |
---
