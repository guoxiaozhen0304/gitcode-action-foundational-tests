# USE-MASK-01-001

- 标题: secret 脱敏文档描述与实际行为一致并给出缓解建议
- 维度: usability/security | 优先级: P0
- 评级: 混合问题

---

## 1. 想测什么（规格）

前置条件:
  - 仓库配置了 TEST_SECRET
操作步骤:
  1. 1. 在 workflow 中通过环境变量注入方式引用 secret
  2. 2. 检查日志脱敏效果
预期结果:
  日志中 secret 显示为 ***；文档若声明绕过风险，必须同时给出正确写法示例

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | echo secret via env | echo "secret length=${#SECRET_VAL}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [positive] run_logs must_not_contain_secret: TEST_SECRET | UNCOVERED | secret TEST_SECRET 从未被任何步骤使用，安全断言无效 |
| [nonfunctional] documentation  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 若文档声明存在绕过风险，必须同时给出正确写法与错误写法的代码示例对比；仅有风险声明而无缓解建议的视为可理解性不合格 |

### 问题

- **断言 1 - UNEXERCISED**: secret TEST_SECRET 从未被任何步骤使用，安全断言无效
- **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 若文档声明存在绕过风险，必须同时给出正确写法与错误写法的代码示例对比；仅有风险声明而无缓解建议的视为可理解性不合格

---
