# USE-ENV-01-002

- 标题: 引用 GITHUB_SHA 时日志应给出环境变量映射提示
- 维度: usability/compatibility | 优先级: P1
- 评级: 不可评估

---

## 1. 想测什么（规格）

前置条件:
  - workflow 在 GitCode Runner 上执行
操作步骤:
  1. 1. 在 run 步骤中输出 $GITHUB_SHA
预期结果:
  日志中应出现关于 GITHUB 变量不存在或建议使用 ATOMGIT 的提示

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | echo GITHUB_SHA | set -u echo "sha=$GITHUB_SHA"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [nonfunctional] error_message  | LLM_DEPENDENT | 非功能性/LLM辅助断言，不可静态评估: 日志警告是否足够醒目且包含有效指引：应提示 GITHUB_* 环境变量在 GitCode 中对应为 ATOMGIT_* |

### 问题

- **断言 1 - LLM_DEPENDENT**: 非功能性/LLM辅助断言，不可静态评估: 日志警告是否足够醒目且包含有效指引：应提示 GITHUB_* 环境变量在 GitCode 中对应为 ATOMGIT_*

---
