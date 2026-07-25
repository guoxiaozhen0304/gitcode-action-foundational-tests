# USE-EXPR-01-002

- 标题: 调用未知函数时报错应提示函数名错误与修正方向
- 维度: usability/compatibility | 优先级: P1
- 评级: 混合问题

---

## 1. 想测什么（规格）

前置条件:
  - workflow 文件位于 .gitcode/workflows/
操作步骤:
  1. 1. 在 if 条件中使用 ${{ unknownFunc() }}
预期结果:
  报错指出未知函数，并建议检查函数名拼写

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | bad function | echo "hello"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_status equals: COMPLETED | COVERED | 存在失败路径：有 fail 命令或条件分支可产生非成功状态 |
| [nonfunctional] error_message  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 报错信息必须包含出错的原始表达式（或截断后的前 50 字符）和错误类型说明 |

### 问题

- **断言 2 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 报错信息必须包含出错的原始表达式（或截断后的前 50 字符）和错误类型说明

---
