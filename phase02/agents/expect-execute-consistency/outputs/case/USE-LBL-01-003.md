# USE-LBL-01-003
- **标题**: runs-on 标签写法跨文档形态扫描（同一字段不应出现三种以上互斥形态）
- **维度**: usability
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**runs-on 标签写法跨文档形态扫描（同一字段不应出现三种以上互斥形态）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-031
通过标准：
1. 同一字段在 3 个以上官方页面给出互不相同形态且无任何一处说明等价关系即为缺陷

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | workflow: null | 无 workflow 步骤 | — | 纯文档分析 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation 确定性校验：形态数大于 2 且未集中说明等价关系即不合格 | negative | gitcode-spec 全文 grep runs-on 归纳形态 | ✅ COVERED | 确定性文档校验 |
| 2 | documentation 确定性校验：selecting-runner-labels.md 列出全形态并标注推荐 | nonfunctional | 确定性文档检查 | ✅ COVERED | 虽标注 nonfunctional 但 eval=deterministic，可确定性判定 |
---
