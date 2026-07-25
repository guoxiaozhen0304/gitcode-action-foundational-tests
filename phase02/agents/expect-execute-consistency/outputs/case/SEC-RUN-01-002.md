# SEC-RUN-01-002

- 标题: Runner 环境变量与共享目录必须跨 job 隔离
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库支持多 job workflow
操作步骤:
  1. 1. 提交一个多 job workflow，job A 设置环境变量和 /tmp 文件
  2. 2. job B 检查环境变量和 /tmp 是否被污染
预期结果:
  - job B 的环境变量和共享目录在启动时为干净状态
  - job B 不应继承 job A 的设置

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Set env | echo MY_SECRET_ENV=leaked >> $ATOMGIT_ENV echo leaked-data > /tmp/env-test.txt  | 是 |
| 2 | Check env clean | if [ -n "$MY_SECRET_ENV" ] \|\| [ -f /tmp/env-test.txt ]; then   echo "isolation broken"   exit 1 else   echo "isolated as expected" fi  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: isolation broken | COVERED | 步骤 [Check env clean] 执行真实功能时输出该值 |
| [positive] run_logs equals: isolated_as_expected | UNCOVERED | 期望值 [isolated_as_expected] 未在任何步骤输出中找到 |

### 问题

- **断言 2 - MISSING_SOURCE**: 期望值 [isolated_as_expected] 未在任何步骤输出中找到

---
