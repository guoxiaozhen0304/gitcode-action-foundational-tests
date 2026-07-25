# USE-ENV-01-001

- 标题: 使用 ATOMGIT_SHA 环境变量时正常取值
- 维度: usability/compatibility | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - workflow 在 GitCode Runner 上执行
操作步骤:
  1. 1. 在 run 步骤中输出 $ATOMGIT_SHA
预期结果:
  环境变量正常输出当前 commit SHA

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | echo ATOMGIT_SHA | echo "sha=$ATOMGIT_SHA"  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [positive] run_logs contains: sha= | COVERED | 步骤 [echo ATOMGIT_SHA] 执行真实功能时输出该值 |

### 问题

- 无

---
