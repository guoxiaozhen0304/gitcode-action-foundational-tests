# SEC-RUN-01-001

- 标题: Job 结束后 workspace 与临时文件必须被彻底清理
- 维度: 安全性 | 优先级: P0
- 评级: 存在空洞

---

## 1. 想测什么（规格）

前置条件:
  - 仓库支持多 job workflow
操作步骤:
  1. 1. 提交一个多 job workflow，job A 写入敏感临时文件
  2. 2. job B 检查是否存在 job A 的残留文件
预期结果:
  - job B 绝不应读取到 job A 残留的敏感文件
  - 即使 job A 异常崩溃，清理钩子仍应执行

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Write temp secret | echo sensitive-data > /tmp/sensitive-temp.txt  | 是 |
| 2 | Check no residual | if [ -f /tmp/sensitive-temp.txt ]; then   echo "residual found"   exit 1 else   echo "cleaned as expected" fi  | 是 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: residual found | COVERED | 步骤 [Check no residual] 执行真实功能时输出该值 |
| [positive] run_logs equals: cleaned_as_expected | UNCOVERED | 期望值 [cleaned_as_expected] 未在任何步骤输出中找到 |

### 问题

- **断言 2 - MISSING_SOURCE**: 期望值 [cleaned_as_expected] 未在任何步骤输出中找到

---
