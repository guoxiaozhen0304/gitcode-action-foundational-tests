# USE-EXPR-01-001

- 标题: 引用不存在的上下文属性时报错应包含原始表达式与错误类型
- 维度: usability/compatibility | 优先级: P1
- 评级: 混合问题

---

## 1. 想测什么（规格）

前置条件:
  - workflow 文件位于 .gitcode/workflows/
操作步骤:
  1. 1. 在 run 步骤中使用 ${{ atomgit.nonexistent_property }}
预期结果:
  报错包含原始表达式字符串和错误类型说明（undefined property / unknown context）

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | bad expression | echo "val=${{ atomgit.nonexistent_property }}"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_status equals: COMPLETED | COVERED | 步骤含实际命令/action，失败状态取决于真实执行 |
| [nonfunctional] error_message  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 报错信息必须包含出错的原始表达式（或截断后的前 50 字符）和错误类型说明；若错误是未知上下文属性，应提示请检查上下文名称和属性名拼写 |

### 问题

- **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 报错信息必须包含出错的原始表达式（或截断后的前 50 字符）和错误类型说明；若错误是未知上下文属性，应提示请检查上下文名称和属性名拼写

---
