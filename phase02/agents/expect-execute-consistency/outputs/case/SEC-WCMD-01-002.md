# SEC-WCMD-01-002

- 标题: 跨运行 artifact 必须被视为不可信数据
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
  - 仓库支持 artifact 传递
操作步骤:
  1. 1. 提交一个不可信运行（fork PR）上传 artifact
  2. 2. 提交一个特权运行尝试下载并执行该 artifact
预期结果:
  - 特权运行不自动执行 artifact 内容
  - artifact 来源可追溯至其产出运行的信任级别

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Download untrusted artifact | uses: download-artifact | 是 |
| 2 | Do not auto execute | echo "Artifact downloaded but not executed automatically"  | 否 |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [negative] run_logs must_not_contain: auto_executed | COVERED | 期望值可能来自 action 内部日志输出: download-artifact |
| [positive] run_status equals: completed | COVERED | 步骤含实际命令或 action，运行状态取决于真实执行结果 |

### 问题

- 无

---
