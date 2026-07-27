# USE-EXPR-01-004
- **标题**: 未文档化函数 default() 的文档缺失 diff（与平台行为断言合并证据链）
- **维度**: usability
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**未文档化函数 default() 的文档缺失 diff（与平台行为断言合并证据链）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-039
通过标准：
1. 记录 default() 的实际求值结果
2. 函数表缺少样本实际使用的函数每 1 个即一条缺陷

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | conditional step with default | `echo "default-evaluated-true"` | `if: "${{ default() }}"` | 记录 conditional step 是否执行 |
| 2 | always marker | `echo "job-ran"` | `if: ${{ always() }}` | 确保 job 运行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs 确定性记录 default() 求值结果 | positive | `if: "${{ default() }}"` 含 `${{ }}` 表达式 | ✅ GENUINE | 表达式求值涉及平台真实行为 |
| 2 | documentation 确定性校验：函数表函数名集合应包含 default | negative | 文档函数表集合检查 | ✅ COVERED | 确定性文档校验 |
---
