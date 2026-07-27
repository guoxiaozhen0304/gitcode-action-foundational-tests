# USE-DOC-01-007
- **标题**: environment 字段能力描述存在而语法参考缺失及平台报错指引
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**environment 字段能力描述存在而语法参考缺失及平台报错指引**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-043
通过标准：
1. 能力描述存在但语法参考缺失即不合格
2. 平台报错信息应包含该字段是否未来支持的指引

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | marker step | `echo "deploy"` | environment: production | 仅 echo |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | positive | eval: "deterministic" | ✅ GENUINE | YAML 使用 `environment: production` 字段，平台应拒绝并产生报错。平台验证型测试 |
| 2 | documentation | negative | eval: "deterministic" | ❌ MISSING_SOURCE | target=documentation，无 workflow 步骤产生 |

### 问题
**断言 2 — MISSING_SOURCE**: 文档一致性检查依赖 harness 侧静态扫描。断言 1 的报错实证为该文档缺陷提供证据。
---
